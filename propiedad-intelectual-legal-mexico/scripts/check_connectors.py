#!/usr/bin/env python3
"""Audit declared and runtime connector capabilities without assuming tools.

The script never calls an MCP server. A Claude workflow performs a minimal,
read-only probe and may provide a sanitized runtime inventory. Only an explicit
successful, non-sensitive probe earns ``verified`` status.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = PLUGIN_ROOT / "references" / "connector-capabilities.json"
PROBE_MAX_AGE_SECONDS = 15 * 60
MUTATING_TOOL_RE = re.compile(
    r"(?:^|_)(?:write|create|update|delete|send|upload|move|rename|share|comment|"
    r"post|publish|modify|edit|append|add|remove|archive|restore|invite)(?:_|$)",
    re.IGNORECASE,
)
READ_TOOL_RE = re.compile(
    r"(?:^|_)(?:get|list|search|find|read|fetch|retrieve|query|lookup|download|"
    r"inspect|analyze|analyse|analysis|compare|resolve|summarize|summary|check|"
    r"validate|explain|extract|view|open|browse|status)(?:_|$)",
    re.IGNORECASE,
)


class ConnectorCheckError(RuntimeError):
    pass


def _load_object(path: Path, label: str) -> dict[str, Any]:
    if path.is_symlink():
        raise ConnectorCheckError(f"Se rechazó {label} enlazado simbólicamente: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ConnectorCheckError(f"No se pudo leer {label} {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ConnectorCheckError(f"JSON inválido en {label} {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConnectorCheckError(f"{label} debe contener un objeto JSON.")
    return value


def _key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _runtime_servers(inventory: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if inventory is None:
        return {}
    servers = inventory.get("servers")
    if not isinstance(servers, list):
        raise ConnectorCheckError("runtime inventory debe contener una lista 'servers'.")
    result: dict[str, dict[str, Any]] = {}
    for index, server in enumerate(servers):
        if not isinstance(server, dict) or not isinstance(server.get("name"), str):
            raise ConnectorCheckError(f"runtime servers[{index}] no tiene name válido.")
        normalized = _key(server["name"])
        if normalized in result:
            raise ConnectorCheckError(f"Servidor runtime duplicado: {server['name']}")
        result[normalized] = server
    return result


def _zoned_timestamp(value: Any) -> tuple[str, datetime] | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.strip()
    candidate = normalized[:-1] + "+00:00" if normalized.endswith("Z") else normalized
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return normalized, parsed.astimezone(timezone.utc)


def _probe_status(
    probe: dict[str, Any] | None,
    tools: list[str],
    now: datetime,
) -> tuple[str, dict[str, Any] | None]:
    if probe is None:
        return "configured_unverified", None
    status = probe.get("status")
    if status == "failed":
        return "unavailable", {
            "status": "failed",
            "tested_at": probe.get("tested_at"),
            "operation": probe.get("operation"),
            "tool": probe.get("tool"),
        }
    timestamp = _zoned_timestamp(probe.get("tested_at"))
    tested_at = timestamp[0] if timestamp else None
    tested_datetime = timestamp[1] if timestamp else None
    tool = probe.get("tool")
    observed_tool = isinstance(tool, str) and tool in tools
    safe_read_tool = (
        observed_tool
        and not MUTATING_TOOL_RE.search(tool)
        and bool(READ_TOOL_RE.search(tool))
    )
    fresh = False
    if tested_datetime is not None:
        age = (now - tested_datetime).total_seconds()
        fresh = -300 <= age <= PROBE_MAX_AGE_SECONDS
    if (
        status == "passed"
        and probe.get("non_sensitive") is True
        and probe.get("result_observed") is True
        and isinstance(probe.get("operation"), str)
        and bool(probe["operation"].strip())
        and tested_at is not None
        and safe_read_tool
        and fresh
    ):
        return "verified", {
            "status": "passed",
            "tested_at": tested_at,
            "operation": probe["operation"],
            "tool": tool,
            "non_sensitive": True,
            "result_observed": True,
        }
    return "configured_unverified", {
        "status": str(status or "not_run"),
        "tested_at": probe.get("tested_at"),
        "operation": probe.get("operation"),
        "tool": tool,
    }


def build_report(
    registry: dict[str, Any],
    manifest: dict[str, Any],
    inventory: dict[str, Any] | None,
    registry_path: Path,
    manifest_path: Path,
    now: datetime | None = None,
) -> dict[str, Any]:
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None or now.utcoffset() is None:
        raise ConnectorCheckError("now debe incluir zona horaria.")
    now = now.astimezone(timezone.utc)
    declared = manifest.get("mcpServers")
    if not isinstance(declared, dict):
        raise ConnectorCheckError("El manifiesto no contiene un objeto 'mcpServers'.")
    connectors = registry.get("connectors")
    unsupported = registry.get("unsupported_capabilities")
    if not isinstance(connectors, list) or not isinstance(unsupported, list):
        raise ConnectorCheckError(
            "El registro requiere listas 'connectors' y 'unsupported_capabilities'."
        )

    runtime = _runtime_servers(inventory)
    checked: list[dict[str, Any]] = []
    drift: list[str] = []
    reviewed_names: set[str] = set()
    seen_connector_ids: set[str] = set()
    seen_server_names: set[str] = set()

    expected_hash = (registry.get("dependency") or {}).get("source_manifest_sha256")
    if not isinstance(expected_hash, str) or not re.fullmatch(r"[a-f0-9]{64}", expected_hash):
        drift.append("dependency.source_manifest_sha256 ausente o inválido")
    else:
        try:
            actual_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        except OSError as exc:
            raise ConnectorCheckError(f"No se pudo hashear manifiesto: {exc}") from exc
        if actual_hash != expected_hash:
            drift.append("El hash del manifiesto cambió; requiere revisión explícita.")

    for index, connector in enumerate(connectors):
        if not isinstance(connector, dict):
            raise ConnectorCheckError(f"connectors[{index}] no es un objeto.")
        server_name = connector.get("declared_server")
        connector_id = connector.get("id")
        if not isinstance(server_name, str) or not isinstance(connector_id, str):
            raise ConnectorCheckError(f"connectors[{index}] carece de id/declared_server.")
        if connector_id in seen_connector_ids:
            raise ConnectorCheckError(f"ID de conector duplicado: {connector_id}")
        if server_name in seen_server_names:
            raise ConnectorCheckError(f"Servidor revisado duplicado: {server_name}")
        seen_connector_ids.add(connector_id)
        seen_server_names.add(server_name)
        reviewed_names.add(server_name)
        is_declared = server_name in declared
        runtime_server = runtime.get(_key(server_name)) if inventory is not None else None
        manifest_entry = declared.get(server_name)
        expected_manifest = connector.get("expected_manifest")
        manifest_valid = is_declared and isinstance(manifest_entry, dict)
        if not is_declared:
            status = "unavailable"
            drift.append(
                f"{connector_id}: servidor declarado en registro no existe en manifiesto: {server_name}"
            )
        elif not isinstance(manifest_entry, dict):
            status = "unavailable"
            drift.append(f"{connector_id}: definición de manifiesto no es objeto")
        if is_declared:
            if not isinstance(expected_manifest, dict):
                drift.append(f"{connector_id}: expected_manifest ausente en registro")
            elif isinstance(manifest_entry, dict):
                for field in ("type", "url"):
                    expected = expected_manifest.get(field)
                    actual = manifest_entry.get(field)
                    if not isinstance(expected, str) or actual != expected:
                        drift.append(f"{connector_id}: {field} cambió respecto del registro")

        tools: list[str] = []
        if runtime_server is not None and isinstance(runtime_server.get("tools"), list):
            tools = sorted(
                value for value in runtime_server["tools"] if isinstance(value, str)
            )
        declared_capabilities = connector.get("capabilities")
        if not isinstance(declared_capabilities, list) or not declared_capabilities or not all(
            isinstance(value, str) and value for value in declared_capabilities
        ):
            raise ConnectorCheckError(
                f"{connector_id}: capabilities debe ser lista de identificadores."
            )
        probes_by_capability: dict[str, dict[str, Any]] = {}
        if runtime_server is not None:
            raw_probes = runtime_server.get("read_probes", [])
            if not isinstance(raw_probes, list):
                raise ConnectorCheckError(
                    f"{connector_id}: read_probes runtime debe ser lista."
                )
            for probe_index, probe in enumerate(raw_probes):
                if not isinstance(probe, dict) or not isinstance(
                    probe.get("capability"), str
                ):
                    raise ConnectorCheckError(
                        f"{connector_id}: read_probes[{probe_index}] inválido."
                    )
                capability = probe["capability"]
                if capability in probes_by_capability:
                    raise ConnectorCheckError(
                        f"{connector_id}: prueba duplicada para {capability}."
                    )
                probes_by_capability[capability] = probe
            undeclared = sorted(set(probes_by_capability) - set(declared_capabilities))
            if undeclared:
                drift.append(
                    f"{connector_id}: pruebas para capacidades no declaradas: {', '.join(undeclared)}"
                )

        capability_checks: list[dict[str, Any]] = []
        for capability in declared_capabilities:
            if not manifest_valid or (inventory is not None and runtime_server is None):
                capability_status, evidence = "unavailable", None
            elif inventory is None:
                capability_status, evidence = "configured_unverified", None
            else:
                capability_status, evidence = _probe_status(
                    probes_by_capability.get(capability), tools, now
                )
            capability_checks.append(
                {
                    "capability": capability,
                    "status": capability_status,
                    "read_probe": evidence,
                }
            )

        verified_count = sum(
            row["status"] == "verified" for row in capability_checks
        )
        if not manifest_valid or (inventory is not None and runtime_server is None):
            status = "unavailable"
        elif verified_count == len(capability_checks):
            status = "verified"
        elif verified_count:
            status = "partially_verified"
        elif capability_checks and all(
            row["status"] == "unavailable" for row in capability_checks
        ):
            status = "unavailable"
        else:
            status = "configured_unverified"
        checked.append(
            {
                "id": connector_id,
                "declared_server": server_name,
                "declared_in_manifest": is_declared,
                "status": status,
                "capabilities_declared": declared_capabilities,
                "capabilities_verified": [
                    row["capability"]
                    for row in capability_checks
                    if row["status"] == "verified"
                ],
                "capability_checks": capability_checks,
                "runtime_tools_observed": tools,
                "write_capabilities_verified": False,
                "fallback_required": verified_count != len(capability_checks),
            }
        )

    unsupported_rows = [
        {
            "id": row.get("id"),
            "status": "unsupported",
            "examples": row.get("examples", []),
            "fallback": row.get("fallback"),
        }
        for row in unsupported
        if isinstance(row, dict)
    ]
    return {
        "schema_version": "1.0.0",
        "generated_at": now.replace(microsecond=0).isoformat(),
        "registry_source": str(registry_path.resolve()),
        "manifest_source": str(manifest_path.resolve()),
        "runtime_inventory_supplied": inventory is not None,
        "ok": not drift,
        "drift": drift,
        "connectors": checked,
        "unsupported_capabilities": unsupported_rows,
        "declared_unreviewed_servers": sorted(set(declared) - reviewed_names),
        "policy": (
            "Solo una prueba por capacidad, fresca, observada, no sensible y ligada "
            "a una herramienta de lectura expuesta verifica esa capacidad. "
            "La escritura permanece no verificada y requiere prueba y confirmación separadas."
        ),
    }


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Comprobación de conectores de PI México",
        "",
        f"Estado del registro: {'sin deriva' if report['ok'] else 'DERIVA DETECTADA'}",
        "",
        "| Conector | Servidor | Estado | Lectura probada | Escritura |",
        "|---|---|---|---|---|",
    ]
    for row in report["connectors"]:
        verified = ", ".join(row.get("capabilities_verified", [])) or "ninguna"
        lines.append(
            f"| {row['id']} | {row['declared_server']} | `{row['status']}` | "
            f"{verified} | no verificada |"
        )
    if report["drift"]:
        lines.extend(["", "## Deriva", ""])
        lines.extend(f"- {item}" for item in report["drift"])
    lines.extend(["", f"> {report['policy']}", ""])
    return "\n".join(lines)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Manifiesto .mcp.json; por defecto usa dependency.source_manifest.",
    )
    parser.add_argument(
        "--runtime-inventory",
        type=Path,
        help="Inventario JSON saneado después de pruebas de solo lectura.",
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--strict", action="store_true", help="Fallar si hay deriva.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        registry = _load_object(args.registry, "registro")
        manifest_path = args.manifest
        if manifest_path is None:
            source = (registry.get("dependency") or {}).get("source_manifest")
            if not isinstance(source, str) or not source:
                raise ConnectorCheckError("dependency.source_manifest ausente.")
            manifest_path = (args.registry.parent / source).resolve()
        manifest = _load_object(manifest_path, "manifiesto")
        inventory = (
            _load_object(args.runtime_inventory, "runtime inventory")
            if args.runtime_inventory
            else None
        )
        report = build_report(
            registry, manifest, inventory, args.registry, manifest_path
        )
    except ConnectorCheckError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    if args.format == "markdown":
        print(markdown(report), end="")
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if args.strict and not report["ok"] else 0


if __name__ == "__main__":
    sys.exit(main())
