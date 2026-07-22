#!/usr/bin/env python3
"""PreToolUse guard for local-first and active-matter isolation."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

from matter_workspace import (  # noqa: E402
    GLOBAL_ROOT,
    PLUGIN_NAME,
    WorkspaceError,
    load_state,
)


FILE_KEYS = ("file_path", "path", "notebook_path")
MUTATING_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SHARED_DATA_FILES = {"portfolio.json", "portfolio.yaml", "verification-log.md"}
UNSCOPED_CLIENT_STORES = {
    "box",
    "definely",
    "googledrive",
    "imanage",
    "slack",
    "topcounsel",
}
MCP_WRITE_RE = re.compile(
    r"(?:^|_)(?:write|create|update|delete|send|upload|move|rename|share|comment|"
    r"post|publish|modify|edit|append|add|remove|archive|restore|invite)(?:_|$)",
    re.IGNORECASE,
)
MCP_READ_RE = re.compile(
    r"(?:^|_)(?:get|list|search|find|read|fetch|retrieve|query|lookup|download|"
    r"inspect|analyze|analyse|analysis|compare|resolve|summarize|summary|check|"
    r"validate|explain|extract|view|open|browse|status)(?:_|$)",
    re.IGNORECASE,
)
SHELL_META_RE = re.compile(r"[;&|><`\n]|\$\(")
BROAD_SCAN_RE = re.compile(
    r"(?:^|[;&|]\s*|\s)(?:rg|find|fd|tree)(?:\s|$)|"
    r"(?:^|[;&|]\s*|\s)grep\s+[^\n]*(?:-[^\s]*[Rr]|--recursive)(?:\s|$)|"
    r"(?:^|[;&|]\s*|\s)ls\s+[^\n]*-[^\s]*R(?:\s|$)|"
    r"(?:^|[;&|]\s*|\s)(?:tar\s+[^\n]*\s+\.|zip\s+-r[^\n]*\s+\.)"
)


def _deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            },
            ensure_ascii=False,
        )
    )


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _resolve(raw: str, cwd: Path) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(raw))
    path = Path(expanded)
    if not path.is_absolute():
        path = cwd / path
    return path.resolve(strict=False)


def _lexical_path(raw: str, cwd: Path) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(raw))
    path = Path(expanded)
    if not path.is_absolute():
        path = cwd / path
    return Path(os.path.abspath(path))


def _symlink_below(path: Path, root: Path) -> bool:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            return True
    return False


def _trusted_controller(command: str) -> bool:
    if SHELL_META_RE.search(command):
        return False
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False
    if len(tokens) < 3 or Path(tokens[0]).name not in {"python", "python3"}:
        return False
    controller = tokens[1].replace("${CLAUDE_PLUGIN_ROOT}", str(PLUGIN_ROOT))
    if Path(os.path.expandvars(controller)).resolve(strict=False) != (
        PLUGIN_ROOT / "scripts" / "matter_workspace.py"
    ).resolve():
        return False
    rest = tokens[2:]
    if rest in (["status"], ["list"], ["none"]):
        return True
    return len(rest) == 2 and rest[0] in {"new", "switch", "close"} and bool(
        re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", rest[1])
    )


def _trusted_renewal_watch(command: str) -> bool:
    """Allow only the canonical, read-only watcher invocation for DATA_ROOT."""
    if SHELL_META_RE.search(command):
        return False
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False
    if len(tokens) < 3 or Path(tokens[0]).name not in {"python", "python3"}:
        return False
    script = tokens[1].replace("${CLAUDE_PLUGIN_ROOT}", str(PLUGIN_ROOT))
    if Path(os.path.expandvars(script)).resolve(strict=False) != (
        PLUGIN_ROOT / "scripts" / "renewal_watch.py"
    ).resolve():
        return False
    rest = tokens[2:]
    if rest.count("--resolve") != 1 or "--portfolio" in rest:
        return False
    allowed_values = {
        "--as-of": re.compile(r"\d{4}-\d{2}-\d{2}"),
        "--days": re.compile(r"\d{1,4}"),
        "--verification-max-age": re.compile(r"\d{1,4}"),
        "--format": re.compile(r"(?:json|markdown)"),
    }
    seen: set[str] = set()
    index = 0
    while index < len(rest):
        token = rest[index]
        if token == "--resolve":
            index += 1
            continue
        pattern = allowed_values.get(token)
        if pattern is None or token in seen or index + 1 >= len(rest):
            return False
        if not pattern.fullmatch(rest[index + 1]):
            return False
        seen.add(token)
        index += 2
    return True


def _trusted_source_check(command: str) -> bool:
    """Allow the checker only with its canonical registries and safe flags."""
    if SHELL_META_RE.search(command):
        return False
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False
    if len(tokens) < 2 or Path(tokens[0]).name not in {"python", "python3"}:
        return False
    script = tokens[1].replace("${CLAUDE_PLUGIN_ROOT}", str(PLUGIN_ROOT))
    if Path(os.path.expandvars(script)).resolve(strict=False) != (
        PLUGIN_ROOT / "scripts" / "check_legal_sources.py"
    ).resolve():
        return False
    rest = tokens[2:]
    seen: set[str] = set()
    index = 0
    while index < len(rest):
        token = rest[index]
        if token == "--strict":
            if token in seen:
                return False
            seen.add(token)
            index += 1
            continue
        patterns = {
            "--as-of": re.compile(r"\d{4}-\d{2}-\d{2}"),
            "--format": re.compile(r"(?:json|markdown)"),
        }
        pattern = patterns.get(token)
        if pattern is None or token in seen or index + 1 >= len(rest):
            return False
        if not pattern.fullmatch(rest[index + 1]):
            return False
        seen.add(token)
        index += 2
    return True


def _existing_managed_roots(cwd: Path) -> list[Path]:
    roots: list[Path] = []
    current = cwd.resolve()
    for parent in (current, *current.parents):
        candidate = parent.joinpath(
            ".claude-legal", "propiedad-intelectual-legal-mexico"
        )
        if candidate.exists():
            roots.append(candidate.resolve())
    if GLOBAL_ROOT.exists():
        roots.append(GLOBAL_ROOT.resolve())
    return list(dict.fromkeys(roots))


def _mcp_server(raw_tool: str) -> str:
    parts = raw_tool.split("__")
    if len(parts) < 3:
        return ""
    return re.sub(r"[^a-z0-9]", "", parts[1].lower())


def _mcp_action(raw_tool: str) -> str:
    parts = raw_tool.split("__")
    return parts[-1] if len(parts) >= 3 else ""


def _unscoped_client_store(server: str) -> str | None:
    return next((name for name in UNSCOPED_CLIENT_STORES if name in server), None)


def _contains_local_plugin_root(path: Path) -> bool:
    parts = path.parts
    return any(
        parts[index : index + 2] == (".claude-legal", PLUGIN_NAME)
        for index in range(max(0, len(parts) - 1))
    )


def _guard_without_profile(
    tool: str, tool_input: dict, cwd: Path, roots: list[Path]
) -> str | None:
    """Fail closed for existing matter data when its profile is unavailable."""
    if not roots:
        return None
    for key in FILE_KEYS:
        raw = tool_input.get(key)
        if not raw:
            continue
        path = _resolve(str(raw), cwd)
        if any(_inside(path, (root / "matters").resolve()) for root in roots):
            return (
                "Datos de asuntos existentes detectados, pero el perfil no puede "
                "resolverse. Se bloquea el acceso hasta reparar CLAUDE.md."
            )
    if tool in {"Grep", "Glob"}:
        raw_root = tool_input.get("path")
        search_root = _resolve(str(raw_root), cwd) if raw_root else cwd
        pattern = str(tool_input.get("pattern") or tool_input.get("glob") or "")
        if any(_inside(root, search_root) for root in roots) and (
            tool == "Grep" or "**" in pattern or ".claude-legal" in pattern
        ):
            return (
                "Búsqueda bloqueada: incluye datos administrados cuyo perfil no "
                "puede resolverse. Repara el perfil antes de continuar."
            )
    if tool == "Bash":
        command = str(tool_input.get("command", ""))
        protected = (".claude-legal", "/matters/", *(str(root) for root in roots))
        if any(token in command for token in protected) or BROAD_SCAN_RE.search(command):
            return (
                "Acceso shell bloqueado: existen datos administrados pero el perfil "
                "no puede resolverse."
            )
    return None


def _guard_path(path: Path, state, lexical: Path | None = None) -> str | None:
    config_root = Path(state.config_root).resolve()
    matters_root = (config_root / "matters").resolve(strict=False)
    active_root = (
        (matters_root / state.active).resolve(strict=False) if state.active else None
    )

    # A local client profile always wins. Reading the global fallback in the
    # same run would silently merge two clients or practices.
    if state.scope == "local" and _inside(path, GLOBAL_ROOT.resolve()):
        return (
            "Aislamiento local activo: no se permite acceder al perfil global. "
            "Usa únicamente CONFIG_ROOT/DATA_ROOT devueltos por "
            "matter_workspace.py status."
        )

    # A direct absolute path must not hop into a different project's local
    # legal store, even when that project is not an ancestor of cwd.
    candidate_paths = (path,) if lexical is None else (path, lexical)
    if any(_contains_local_plugin_root(item) for item in candidate_paths) and not any(
        _inside(item, config_root) for item in candidate_paths
    ):
        return (
            "Acceso a otro almacén local bloqueado. El único CONFIG_ROOT "
            "permitido es el resuelto para esta ejecución."
        )

    if lexical is not None and _inside(lexical, config_root) and _symlink_below(
        lexical, config_root
    ):
        return (
            "Acceso bloqueado: una ruta administrada atraviesa un enlace simbólico. "
            "Mueve una copia real del documento a DATA_ROOT."
        )

    if _inside(path, matters_root):
        if not state.enabled:
            return "Los espacios por asunto están desactivados; no se permite leer matters/."
        if not active_root:
            return (
                "No hay asunto activo. Activa uno con matter_workspace.py switch <slug> "
                "antes de acceder a archivos de asunto."
            )
        if not _inside(path, active_root):
            return (
                f"Acceso entre asuntos bloqueado. El único asunto accesible es "
                f"'{state.active}'. Usa matter_workspace.py switch/list/close para "
                "administrar otros asuntos."
            )

    # Practice-wide registries can contain other clients. During substantive
    # work in an active matter, use the per-matter DATA_ROOT copy instead.
    if (
        state.enabled
        and state.active
        and path.parent == config_root
        and path.name in SHARED_DATA_FILES
    ):
        return (
            f"'{path.name}' a nivel de práctica está bloqueado mientras el asunto "
            f"'{state.active}' está activo. Usa DATA_ROOT/{path.name}."
        )
    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0
    raw_tool = str(payload.get("tool_name", ""))
    tool = raw_tool.split("__")[-1]
    tool_input = payload.get("tool_input") or {}
    cwd = Path(payload.get("cwd") or os.getcwd()).resolve()

    if tool == "Bash":
        command = str(tool_input.get("command", ""))
        if _trusted_controller(command):
            return 0
        if "matter_workspace.py" in command:
            _deny(
                "Invocación no permitida del controlador. Usa exactamente status, "
                "list, new <slug>, switch <slug>, close <slug> o none, sin cambiar cwd."
            )
            return 0

    # MCP writes are denied even if a profile is missing or temporarily
    # malformed. Capability verification for reading never implies writing.
    if raw_tool.startswith("mcp__"):
        action = _mcp_action(raw_tool)
        if MCP_WRITE_RE.search(action) or not MCP_READ_RE.search(action):
            _deny(
                "Acción MCP bloqueada: no está clasificada y verificada como "
                "solo lectura. Este plugin no autoriza escritura externa; usa "
                "un flujo separado, probado y con confirmación humana."
            )
            return 0

    # No configured profile means cold-start must be able to create it.
    try:
        state = load_state(cwd)
    except (WorkspaceError, OSError):
        managed_roots = _existing_managed_roots(cwd)
        if raw_tool.startswith("mcp__") and managed_roots:
            _deny(
                "Acceso MCP bloqueado: existen datos de asuntos pero PROFILE no "
                "puede resolverse. Repara CLAUDE.md antes de consultar una fuente "
                "externa para evitar mezclar clientes."
            )
            return 0
        reason = _guard_without_profile(tool, tool_input, cwd, managed_roots)
        if reason:
            _deny(reason)
        return 0

    if raw_tool.startswith("mcp__"):
        server = _mcp_server(raw_tool)
        blocked_store = _unscoped_client_store(server)
        if state.enabled and state.active and blocked_store:
            _deny(
                f"Conector '{blocked_store}' bloqueado durante el asunto '{state.active}': "
                "no existe un filtro de matter_id verificado que impida resultados "
                "de otros clientes. Usa documentos ya colocados en DATA_ROOT o un "
                "adaptador de alcance por asunto probado."
            )
            return 0

    if tool == "Bash":
        command = str(tool_input.get("command", ""))
        if state.enabled and state.active:
            if _trusted_renewal_watch(command) or _trusted_source_check(command):
                return 0
            _deny(
                f"Shell bloqueado durante el asunto '{state.active}'. Usa las "
                "herramientas de archivo dentro de DATA_ROOT; solo el controlador "
                "de asuntos, el chequeo canónico de fuentes y el vigilante "
                "canónico --resolve están autorizados."
            )
            return 0
        protected_tokens = (
            ".claude-legal",
            str(Path(state.config_root)),
            str(GLOBAL_ROOT),
            "/matters/",
        )
        if any(token in command for token in protected_tokens):
            _deny(
                "Acceso shell directo a datos administrados bloqueado. Usa herramientas "
                "Read/Write/Edit para el DATA_ROOT activo o matter_workspace.py para "
                "operaciones entre asuntos."
            )
            return 0
        if state.scope == "local" and state.enabled and BROAD_SCAN_RE.search(command):
            _deny(
                "Escaneo shell recursivo bloqueado porque podría atravesar "
                ".claude-legal. Acota la ruta fuera de ese directorio o usa "
                "Glob/Grep con una ruta segura."
            )
        return 0

    raw_paths = [tool_input.get(key) for key in FILE_KEYS if tool_input.get(key)]
    for raw in raw_paths:
        lexical = _lexical_path(str(raw), cwd)
        resolved = _resolve(str(raw), cwd)
        if (
            tool in MUTATING_TOOLS
            and state.enabled
            and state.active
            and resolved == Path(state.profile).resolve()
        ):
            _deny(
                "No se puede modificar PROFILE durante un asunto activo porque "
                "podría cambiar el límite de datos. Ejecuta matter_workspace.py none "
                "de forma confirmada antes de personalizar el perfil."
            )
            return 0
        reason = _guard_path(resolved, state, lexical)
        if reason:
            _deny(reason)
            return 0

    # A recursive search rooted above the managed local directory can reveal
    # every matter even when its pattern does not name matters explicitly.
    if tool in {"Grep", "Glob"} and state.scope == "local" and state.enabled:
        search_root_raw = tool_input.get("path")
        search_root = (
            _resolve(str(search_root_raw), cwd) if search_root_raw else cwd
        )
        config_root = Path(state.config_root)
        pattern = str(tool_input.get("pattern") or tool_input.get("glob") or "")
        if _inside(config_root, search_root):
            broad_glob = tool == "Glob" and (
                not pattern or "**" in pattern or pattern.lstrip().startswith("{")
            )
            if (
                ".claude-legal" in pattern
                or "matters" in pattern
                or tool == "Grep"
                or broad_glob
            ):
                _deny(
                    "Búsqueda amplia bloqueada: la raíz incluye datos de otros "
                    "asuntos. Acota la búsqueda al DATA_ROOT activo o fuera de "
                    ".claude-legal."
                )
                return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
