#!/usr/bin/env python3
"""Deterministic, provenance-aware renewal watcher for Mexico IP assets.

This program classifies docketed deadline events. It does not infer a legal
deadline from an asset label, file a document, pay a fee, or send a message.
Every event remains a candidate until a human verifies it against the official
record and current rule source.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_PORTFOLIO = "portfolio.json"
CANONICAL_RULES = PLUGIN_ROOT / "references" / "verified-rules.json"
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

from matter_workspace import WorkspaceError, load_state  # noqa: E402


COMPLETED = {"tramitado", "completed", "filed", "paid", "closed"}
PENDING = {"pending", "pendiente", "scheduled", "programado"}
SOURCE_KINDS = {
    "official_registry",
    "official_certificate",
    "user_export",
    "correspondent_confirmation",
    "manual",
}
PORTFOLIO_SOURCE_KINDS = {
    "exportacion_usuario",
    "manual",
    "mcp_personalizado",
    "ninguno",
}
MAINTAINED_ASSET_TYPES = {
    "marca",
    "patente",
    "modelo_utilidad",
    "diseno_industrial",
    "aviso_comercial",
    "nombre_comercial",
    "reserva_derechos",
    "dominio",
}
TERMINAL_ASSET_STATUSES = {
    "abandonada",
    "abandonado",
    "caducada",
    "caducado",
    "cancelada",
    "cancelado",
    "cerrada",
    "cerrado",
    "expirada",
    "expirado",
    "nula",
    "nulo",
}
URGENCY_ORDER = {
    "overdue": 0,
    "grace": 1,
    "due_today": 2,
    "next_30_days": 3,
    "30_to_60_days": 4,
    "60_to_90_days": 5,
    "90_to_180_days": 6,
    "outside_window": 7,
}


class WatchError(RuntimeError):
    pass


def _load(path: Path) -> dict[str, Any]:
    if path.is_symlink():
        raise WatchError(f"Se rechazó un archivo enlazado simbólicamente: {path}")
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise WatchError(f"No se pudo leer {path}: {exc}") from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise WatchError(f"JSON inválido en {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise WatchError(f"{path} debe contener un objeto en la raíz.")
    return data


def _date(value: Any, field: str) -> date:
    if not isinstance(value, str):
        raise ValueError(f"{field} debe ser AAAA-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{field} no es una fecha ISO válida: {value!r}") from exc


def _timestamp_date(value: Any, field: str) -> date:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} debe ser fecha-hora ISO con zona")
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"{field} no es fecha-hora ISO válida: {value!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{field} debe incluir zona horaria")
    return parsed.date()


def _rule_map(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rules = registry.get("rules")
    if not isinstance(rules, list):
        raise WatchError("El registro de reglas no contiene una lista 'rules'.")
    result: dict[str, dict[str, Any]] = {}
    for rule in rules:
        if not isinstance(rule, dict) or not isinstance(rule.get("id"), str):
            raise WatchError("Regla sin id válido en verified-rules.json.")
        if rule["id"] in result:
            raise WatchError(f"ID de regla duplicado: {rule['id']}")
        result[rule["id"]] = rule
    return result


def _portfolio_assets(portfolio: dict[str, Any], as_of: date) -> list[Any]:
    metadata = portfolio.get("metadata")
    if not isinstance(metadata, dict):
        raise WatchError("portfolio.json requiere objeto 'metadata'.")
    if metadata.get("schema_version") != "2.0.0":
        raise WatchError("metadata.schema_version debe ser '2.0.0'.")
    try:
        updated = _date(metadata.get("ultima_actualizacion"), "ultima_actualizacion")
    except ValueError as exc:
        raise WatchError(str(exc)) from exc
    if updated > as_of:
        raise WatchError("metadata.ultima_actualizacion está en el futuro respecto de --as-of.")
    source_kind = metadata.get("sistema_fuente")
    if source_kind not in PORTFOLIO_SOURCE_KINDS:
        raise WatchError("metadata.sistema_fuente ausente o no permitido.")
    assets = portfolio.get("assets")
    if not isinstance(assets, list):
        raise WatchError("portfolio.json debe contener una lista 'assets'.")
    if assets and source_kind == "ninguno":
        raise WatchError(
            "Un portafolio con activos no puede declarar sistema_fuente='ninguno'."
        )
    return assets


def _urgency(as_of: date, due: date, grace_end: date | None, lookahead: int) -> tuple[str, int]:
    days = (due - as_of).days
    if days < 0:
        if grace_end is not None and as_of <= grace_end:
            return "grace", days
        return "overdue", days
    if days == 0:
        return "due_today", days
    if days <= 30:
        return "next_30_days", days
    if days <= 60:
        return "30_to_60_days", days
    if days <= 90:
        return "60_to_90_days", days
    if days <= 180:
        return "90_to_180_days", days
    return "outside_window", days


def _provenance_state(
    event: dict[str, Any], rule: dict[str, Any] | None, as_of: date, max_age: int
) -> tuple[str, list[str]]:
    blockers: list[str] = []
    rule_id = event.get("rule_id")
    if rule is None:
        blockers.append(f"rule_id desconocido: {rule_id!r}")
    else:
        if not str(rule.get("status", "")).startswith("verified_primary"):
            blockers.append(f"regla {rule_id} no tiene status verified_primary")
        try:
            if _date(rule.get("last_verified"), "last_verified") > as_of:
                blockers.append(f"regla {rule_id} fue verificada después de --as-of")
            if _date(rule.get("next_review"), "next_review") < as_of:
                blockers.append(f"regla {rule_id} vencida para revisión")
        except ValueError as exc:
            blockers.append(str(exc))

    source = event.get("source")
    if not isinstance(source, dict):
        blockers.append("falta objeto source")
    else:
        if source.get("kind") not in SOURCE_KINDS:
            blockers.append("source.kind ausente o no permitido")
        if not source.get("reference"):
            blockers.append("source.reference ausente")
        try:
            captured = _timestamp_date(source.get("captured_at"), "source.captured_at")
            if captured > as_of:
                blockers.append("source.captured_at está en el futuro")
        except ValueError as exc:
            blockers.append(str(exc))

    if not event.get("calculation_trace"):
        blockers.append("calculation_trace ausente")
    if not event.get("action"):
        blockers.append("action ausente")

    if event.get("human_verified") is not True:
        blockers.append("human_verified no es true")
    if not isinstance(event.get("verified_by"), str) or not event["verified_by"].strip():
        blockers.append("verified_by ausente")
    verified_at = event.get("verified_against_registry_at")
    if not verified_at:
        blockers.append("verified_against_registry_at ausente")
    else:
        try:
            verified_date = _timestamp_date(
                verified_at, "verified_against_registry_at"
            )
            age = (as_of - verified_date).days
            if age < 0:
                blockers.append("verificación registral está fechada en el futuro")
            elif age > max_age:
                blockers.append(f"verificación registral tiene {age} días (máximo {max_age})")
        except ValueError as exc:
            blockers.append(str(exc))
    return ("verified" if not blockers else "review_required", blockers)


def build_report(
    portfolio: dict[str, Any],
    registry: dict[str, Any],
    as_of: date,
    lookahead: int,
    verification_max_age: int,
    portfolio_path: Path,
) -> dict[str, Any]:
    if registry.get("schema_version") != "1.0.0":
        raise WatchError("verified-rules.json requiere schema_version '1.0.0'.")
    try:
        registry_as_of = _date(registry.get("as_of"), "verified-rules.as_of")
    except ValueError as exc:
        raise WatchError(str(exc)) from exc
    if registry_as_of > as_of:
        raise WatchError(
            "El registro de reglas está fechado después de --as-of; no usar "
            "conocimiento futuro en este reporte."
        )
    rules = _rule_map(registry)
    assets = _portfolio_assets(portfolio, as_of)
    alerts: list[dict[str, Any]] = []
    unknown: list[dict[str, Any]] = []
    skipped_completed = 0
    seen_asset_ids: set[str] = set()

    for asset_index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            unknown.append({"asset_id": f"index:{asset_index}", "reason": "activo no es objeto"})
            continue
        asset_id = str(asset.get("id") or f"index:{asset_index}")
        missing_asset_fields = [
            name
            for name in ("id", "type", "jurisdiction", "mark_or_title")
            if not isinstance(asset.get(name), str) or not asset[name].strip()
        ]
        if missing_asset_fields:
            unknown.append(
                {
                    "asset_id": asset_id,
                    "reason": "campos de activo ausentes o inválidos: "
                    + ", ".join(missing_asset_fields),
                }
            )
        if asset_id in seen_asset_ids:
            unknown.append({"asset_id": asset_id, "reason": "id de activo duplicado"})
            continue
        seen_asset_ids.add(asset_id)
        title = str(asset.get("mark_or_title") or asset.get("title") or "[sin título]")
        events = asset.get("deadline_events")
        if events is None and asset.get("next_deadlines") is not None:
            legacy_events = asset.get("next_deadlines")
            if not isinstance(legacy_events, list) or not legacy_events:
                unknown.append(
                    {
                        "asset_id": asset_id,
                        "reason": "next_deadlines legado vacío o inválido; migrar a deadline_events",
                    }
                )
            for legacy_index, legacy in enumerate(
                legacy_events if isinstance(legacy_events, list) else []
            ):
                unknown.append(
                    {
                        "asset_id": asset_id,
                        "event_id": f"legacy:{legacy_index}",
                        "reason": "next_deadlines legado carece de procedencia; migrar a deadline_events",
                        "candidate_due_date": legacy.get("due_date") if isinstance(legacy, dict) else None,
                    }
                )
            continue
        if not isinstance(events, list):
            unknown.append({"asset_id": asset_id, "reason": "deadline_events ausente o inválido"})
            continue
        seen_event_ids: set[str] = set()
        pending_valid_events = 0
        for event_index, event in enumerate(events):
            if not isinstance(event, dict):
                unknown.append(
                    {"asset_id": asset_id, "event_id": f"index:{event_index}", "reason": "evento no es objeto"}
                )
                continue
            event_id = str(event.get("event_id") or f"index:{event_index}")
            if event_id in seen_event_ids:
                unknown.append(
                    {"asset_id": asset_id, "event_id": event_id, "reason": "event_id duplicado"}
                )
                continue
            seen_event_ids.add(event_id)
            event_status = str(event.get("status", "")).lower()
            if event_status in COMPLETED:
                skipped_completed += 1
                continue
            if event_status not in PENDING:
                unknown.append(
                    {
                        "asset_id": asset_id,
                        "event_id": event_id,
                        "reason": f"status de evento no permitido: {event.get('status')!r}",
                    }
                )
                continue
            try:
                due = _date(event.get("due_date"), "due_date")
                grace = (
                    _date(event.get("grace_end"), "grace_end")
                    if event.get("grace_end")
                    else None
                )
            except ValueError as exc:
                unknown.append({"asset_id": asset_id, "event_id": event_id, "reason": str(exc)})
                continue
            if grace is not None and grace < due:
                unknown.append(
                    {
                        "asset_id": asset_id,
                        "event_id": event_id,
                        "reason": "grace_end es anterior a due_date",
                    }
                )
                continue
            pending_valid_events += 1
            rule_id = event.get("rule_id")
            rule = rules.get(rule_id) if isinstance(rule_id, str) else None
            verification_state, blockers = _provenance_state(
                event, rule, as_of, verification_max_age
            )
            urgency, days_remaining = _urgency(as_of, due, grace, lookahead)
            if days_remaining > lookahead:
                if blockers:
                    unknown.append(
                        {
                            "asset_id": asset_id,
                            "event_id": event_id,
                            "reason": "evento fuera de ventana con procedencia o verificación pendiente",
                            "candidate_due_date": due.isoformat(),
                            "blockers": blockers,
                        }
                    )
                continue
            alerts.append(
                {
                    "asset_id": asset_id,
                    "title": title,
                    "jurisdiction": asset.get("jurisdiction"),
                    "event_id": event_id,
                    "action": event.get("action"),
                    "rule_id": rule_id,
                    "due_date": due.isoformat(),
                    "grace_end": grace.isoformat() if grace else None,
                    "days_remaining": days_remaining,
                    "urgency": urgency,
                    "verification_state": verification_state,
                    "verification_blockers": blockers,
                    "source": event.get("source"),
                    "business_owner": asset.get("business_owner"),
                    "outside_counsel": asset.get("outside_counsel"),
                }
            )
        asset_type = str(asset.get("type") or "").lower()
        asset_status = str(asset.get("status") or "").lower()
        if (
            asset_type in MAINTAINED_ASSET_TYPES
            and asset_status not in TERMINAL_ASSET_STATUSES
            and pending_valid_events == 0
        ):
            unknown.append(
                {
                    "asset_id": asset_id,
                    "reason": "activo mantenible sin deadline_event pendiente válido",
                }
            )

    alerts.sort(
        key=lambda row: (
            URGENCY_ORDER.get(row["urgency"], 99),
            row["due_date"],
            row["asset_id"],
            row["event_id"],
        )
    )
    summary = Counter(row["urgency"] for row in alerts)
    summary["review_required"] = sum(
        row["verification_state"] != "verified" for row in alerts
    )
    summary["unknown"] = len(unknown)
    summary["skipped_completed"] = skipped_completed
    return {
        "schema_version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "as_of": as_of.isoformat(),
        "lookahead_days": lookahead,
        "verification_max_age_days": verification_max_age,
        "portfolio_source": str(portfolio_path.resolve()),
        "rule_registry_as_of": registry_as_of.isoformat(),
        "summary": dict(summary),
        "alerts": alerts,
        "unknown": unknown,
        "disclaimer": (
            "Candidatos de plazo para revisión. Verificar cada fecha, regla, "
            "expediente, día inhábil y presentación ante IMPI/INDAUTOR antes de actuar."
        ),
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# Vigilancia de renovaciones — {report['as_of']}",
        "",
        f"Ventana: {report['lookahead_days']} días · Registro de reglas: {report['rule_registry_as_of']}",
        "",
        f"> {report['disclaimer']}",
        "",
    ]
    alerts = report["alerts"]
    if not alerts:
        lines.extend(
            [
                "## Sin candidatos dentro de la ventana",
                "",
                "Esto confirma que el proceso corrió; no confirma integridad del portafolio.",
                "",
            ]
        )
    for urgency in URGENCY_ORDER:
        rows = [row for row in alerts if row["urgency"] == urgency]
        if not rows:
            continue
        lines.extend([f"## {urgency} ({len(rows)})", ""])
        for row in rows:
            marker = "✓" if row["verification_state"] == "verified" else "⚠ revisión"
            lines.append(
                f"- **{row['asset_id']} — {row['title']}**: {row.get('action') or '[acción faltante]'}; "
                f"{row['due_date']} ({row['days_remaining']} días), regla `{row.get('rule_id')}` · {marker}"
            )
            if row["verification_blockers"]:
                lines.append(f"  - Bloqueos: {'; '.join(row['verification_blockers'])}")
        lines.append("")
    if report["unknown"]:
        lines.extend([f"## Datos desconocidos ({len(report['unknown'])})", ""])
        for row in report["unknown"]:
            lines.append(
                f"- **{row.get('asset_id')} / {row.get('event_id', 'sin evento')}**: {row['reason']}"
            )
        lines.append("")
    lines.extend(
        [
            "---",
            "",
            "*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*",
            "",
        ]
    )
    return "\n".join(lines)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--resolve",
        action="store_true",
        required=True,
        help="Resolver DATA_ROOT local→global y usar DATA_ROOT/portfolio.json.",
    )
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--verification-max-age", type=int, default=90)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        as_of = _date(args.as_of, "as_of")
        if args.days < 1 or args.days > 3650:
            raise WatchError("--days debe estar entre 1 y 3650.")
        if args.verification_max_age < 0 or args.verification_max_age > 3650:
            raise WatchError("--verification-max-age debe estar entre 0 y 3650.")
        state = load_state(Path.cwd())
        portfolio_path = Path(state.data_root) / CANONICAL_PORTFOLIO
        legacy = Path(state.data_root) / "portfolio.yaml"
        if not portfolio_path.is_file() and legacy.is_file():
            raise WatchError(
                "Se encontró portfolio.yaml legado. Migra y valida a "
                "DATA_ROOT/portfolio.json con el skill portafolio antes de vigilar."
            )
        report = build_report(
            _load(portfolio_path),
            _load(CANONICAL_RULES),
            as_of,
            args.days,
            args.verification_max_age,
            portfolio_path,
        )
    except (OSError, ValueError, WatchError, WorkspaceError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    if args.format == "markdown":
        print(markdown(report), end="")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
