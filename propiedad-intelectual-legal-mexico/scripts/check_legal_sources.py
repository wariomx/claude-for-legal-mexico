#!/usr/bin/env python3
"""Validate integrity and review freshness of the Mexico legal rule registry.

This checker does not fetch the remote authorities or claim their content is
unchanged. It verifies the local chain of custody and makes that limitation
explicit so a stale or unreferenced rule cannot silently become operational.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUTHORITIES = PLUGIN_ROOT / "references" / "legal-authorities.json"
DEFAULT_RULES = PLUGIN_ROOT / "references" / "verified-rules.json"
OFFICIAL_HOSTS = {"www.diputados.gob.mx", "sidof.segob.gob.mx"}
RULE_ID_RE = re.compile(r"^MX-(?:LFPPI|LFDA|LFT|CPF|LRART5)-[A-Z0-9-]+-[0-9]{3}$")


class SourceCheckError(RuntimeError):
    pass


def _load(path: Path, label: str) -> dict[str, Any]:
    if path.is_symlink():
        raise SourceCheckError(f"Se rechazó {label} enlazado simbólicamente: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise SourceCheckError(f"No se pudo leer {label}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise SourceCheckError(f"JSON inválido en {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise SourceCheckError(f"{label} debe ser objeto JSON.")
    return value


def _date(value: Any, field: str) -> date:
    if not isinstance(value, str):
        raise SourceCheckError(f"{field} debe ser fecha ISO.")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise SourceCheckError(f"{field} no es fecha ISO válida: {value!r}") from exc


def build_report(
    authorities_doc: dict[str, Any],
    rules_doc: dict[str, Any],
    as_of: date,
    authorities_path: Path,
    rules_path: Path,
) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if authorities_doc.get("schema_version") != "1.0.0":
        errors.append("legal-authorities schema_version debe ser 1.0.0")
    if rules_doc.get("schema_version") != "1.0.0":
        errors.append("verified-rules schema_version debe ser 1.0.0")
    try:
        if _date(authorities_doc.get("as_of"), "legal-authorities.as_of") > as_of:
            errors.append("legal-authorities.as_of está después de --as-of")
        if _date(rules_doc.get("as_of"), "verified-rules.as_of") > as_of:
            errors.append("verified-rules.as_of está después de --as-of")
    except SourceCheckError as exc:
        errors.append(str(exc))

    raw_authorities = authorities_doc.get("authorities")
    raw_rules = rules_doc.get("rules")
    if not isinstance(raw_authorities, list) or not isinstance(raw_rules, list):
        raise SourceCheckError("Los registros requieren listas authorities y rules.")

    authority_map: dict[str, dict[str, Any]] = {}
    remote_unhashed: list[str] = []
    for index, authority in enumerate(raw_authorities):
        if not isinstance(authority, dict) or not isinstance(authority.get("id"), str):
            errors.append(f"authorities[{index}] carece de id válido")
            continue
        authority_id = authority["id"]
        if authority_id in authority_map:
            errors.append(f"authority_id duplicado: {authority_id}")
            continue
        authority_map[authority_id] = authority
        parsed = urlparse(str(authority.get("official_url") or ""))
        if parsed.scheme != "https" or parsed.hostname not in OFFICIAL_HOSTS:
            errors.append(f"{authority_id}: URL no está en host oficial permitido")
        try:
            if _date(authority.get("retrieved_at"), f"{authority_id}.retrieved_at") > as_of:
                errors.append(f"{authority_id}: retrieved_at está en el futuro")
        except SourceCheckError as exc:
            errors.append(str(exc))
        hash_status = authority.get("content_hash_status")
        content_hash = authority.get("content_sha256")
        if hash_status == "remote_primary_not_vendored":
            if content_hash is not None:
                errors.append(f"{authority_id}: hash no debe fingirse para fuente no vendorizada")
            remote_unhashed.append(authority_id)
        elif hash_status == "verified_hash":
            if not isinstance(content_hash, str) or not re.fullmatch(
                r"[a-f0-9]{64}", content_hash
            ):
                errors.append(f"{authority_id}: verified_hash sin SHA-256 válido")
        else:
            errors.append(f"{authority_id}: content_hash_status no reconocido")

    rule_rows: list[dict[str, Any]] = []
    seen_rules: set[str] = set()
    for index, rule in enumerate(raw_rules):
        if not isinstance(rule, dict) or not isinstance(rule.get("id"), str):
            errors.append(f"rules[{index}] carece de id válido")
            continue
        rule_id = rule["id"]
        if rule_id in seen_rules:
            errors.append(f"rule_id duplicado: {rule_id}")
            continue
        seen_rules.add(rule_id)
        if not RULE_ID_RE.fullmatch(rule_id):
            errors.append(f"rule_id fuera de esquema: {rule_id}")
        if not str(rule.get("status") or "").startswith("verified_primary"):
            errors.append(f"{rule_id}: status no es verified_primary")
        if rule.get("requires_human_review") is not True:
            errors.append(f"{rule_id}: requires_human_review debe ser true")
        references = rule.get("authority_refs")
        if not isinstance(references, list) or not references:
            errors.append(f"{rule_id}: authority_refs vacío")
        else:
            for reference in references:
                authority_id = reference.get("authority_id") if isinstance(reference, dict) else None
                if authority_id not in authority_map:
                    errors.append(f"{rule_id}: authority_id desconocido {authority_id!r}")
                if not isinstance(reference, dict) or not str(reference.get("pinpoint") or "").strip():
                    errors.append(f"{rule_id}: referencia sin pinpoint")
        try:
            last_verified = _date(rule.get("last_verified"), f"{rule_id}.last_verified")
            next_review = _date(rule.get("next_review"), f"{rule_id}.next_review")
            if next_review < last_verified:
                errors.append(f"{rule_id}: next_review precede last_verified")
                state = "invalid"
            elif last_verified > as_of:
                state = "future"
                errors.append(f"{rule_id}: last_verified está después de --as-of")
            elif next_review < as_of:
                state = "review_due"
                warnings.append(f"{rule_id}: revisión vencida {next_review.isoformat()}")
            else:
                state = "usable_with_human_review"
            rule_rows.append(
                {
                    "id": rule_id,
                    "state": state,
                    "last_verified": last_verified.isoformat(),
                    "next_review": next_review.isoformat(),
                }
            )
        except SourceCheckError as exc:
            errors.append(str(exc))

    operational_ok = not errors and not any(
        row["state"] in {"review_due", "future", "invalid"} for row in rule_rows
    )
    return {
        "schema_version": "1.0.0",
        "as_of": as_of.isoformat(),
        "authorities_source": str(authorities_path.resolve()),
        "rules_source": str(rules_path.resolve()),
        "integrity_ok": not errors,
        "operational_ok": operational_ok,
        "errors": errors,
        "warnings": warnings,
        "authority_count": len(authority_map),
        "rule_count": len(rule_rows),
        "remote_unhashed_authorities": remote_unhashed,
        "rules": rule_rows,
        "limitation": (
            "No se descargaron fuentes remotas. remote_primary_not_vendored "
            "confirma procedencia/fecha registrada, no identidad de contenido actual."
        ),
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Integridad de fuentes jurídicas México",
        "",
        f"Integridad: {'OK' if report['integrity_ok'] else 'ERROR'} · uso operativo: {'OK' if report['operational_ok'] else 'REVISAR'}",
        f"Autoridades: {report['authority_count']} · reglas: {report['rule_count']}",
        "",
        f"> {report['limitation']}",
        "",
    ]
    if report["errors"]:
        lines.extend(["## Errores", "", *(f"- {item}" for item in report["errors"]), ""])
    if report["warnings"]:
        lines.extend(["## Revisiones vencidas", "", *(f"- {item}" for item in report["warnings"]), ""])
    return "\n".join(lines)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authorities", type=Path, default=DEFAULT_AUTHORITIES)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--strict", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        as_of = _date(args.as_of, "as_of")
        report = build_report(
            _load(args.authorities, "autoridades"),
            _load(args.rules, "reglas"),
            as_of,
            args.authorities,
            args.rules,
        )
    except SourceCheckError as exc:
        print(json.dumps({"operational_ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    if args.format == "markdown":
        print(markdown(report), end="")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if args.strict and not report["operational_ok"] else 0


if __name__ == "__main__":
    sys.exit(main())
