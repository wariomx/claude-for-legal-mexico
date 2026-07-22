#!/usr/bin/env python3
"""Safe workspace controller for the Mexico IP plugin.

Substantive skills must not enumerate, switch, create, or archive matters with
raw filesystem tools. This controller is the only component allowed to perform
those cross-matter operations. It accepts slugs—not client facts—on the command
line so sensitive intake data is written only after a matter becomes active.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path


PLUGIN_NAME = "propiedad-intelectual-legal-mexico"
GLOBAL_ROOT = (
    Path.home() / ".claude" / "plugins" / "config" / "claude-for-legal" / PLUGIN_NAME
)
LOCAL_PARTS = (".claude-legal", PLUGIN_NAME)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ACTIVE_RE = re.compile(r"^(\s*\*\*Asunto activo:\*\*\s*)(.*?)(\s*)$", re.MULTILINE)
ENABLED_RE = re.compile(r"^\s*\*\*Habilitado:\*\*\s*(.*?)\s*$", re.MULTILINE)
CROSS_RE = re.compile(
    r"^\s*\*\*Contexto(?: cruzado)? entre asuntos:\*\*\s*(.*?)\s*$", re.MULTILINE
)


class WorkspaceError(RuntimeError):
    """A safe, user-facing workspace error."""


@dataclass(frozen=True)
class WorkspaceState:
    profile: str
    config_root: str
    data_root: str
    scope: str
    enabled: bool
    active: str | None
    cross_matter: bool


def _ancestors(start: Path):
    current = start.resolve()
    if current.is_file():
        current = current.parent
    yield current
    yield from current.parents


def local_profile(start: Path) -> Path | None:
    """Return the nearest project-local profile, if one exists."""
    for parent in _ancestors(start):
        base = parent.joinpath(*LOCAL_PARTS)
        candidate = base / "CLAUDE.md"
        if candidate.is_file():
            if base.parent.is_symlink() or base.is_symlink() or candidate.is_symlink():
                raise WorkspaceError(
                    f"Perfil local rechazado porque usa un enlace simbólico: {candidate}"
                )
            return candidate
    return None


def resolve_profile(start: Path) -> tuple[Path, str]:
    local = local_profile(start)
    if local:
        return local, "local"
    global_profile = GLOBAL_ROOT / "CLAUDE.md"
    if global_profile.is_file():
        return global_profile, "global"
    raise WorkspaceError(
        "No existe un perfil local ni global. Ejecuta "
        "/propiedad-intelectual-legal-mexico:cold-start-interview "
        "(usa --local para aislar este cliente/proyecto)."
    )


def _is_true(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized.startswith("✓") or normalized.split(" ", 1)[0] in {
        "si",
        "sí",
        "true",
        "on",
        "activado",
        "habilitado",
    }


def _active_slug(value: str) -> str | None:
    normalized = value.strip().lower()
    if normalized.startswith(("ninguno", "none", "desactivado", "n/a")):
        return None
    slug = value.strip().split()[0]
    return slug if SLUG_RE.fullmatch(slug) else None


def load_state(start: Path) -> WorkspaceState:
    profile, scope = resolve_profile(start)
    text = profile.read_text(encoding="utf-8")
    enabled_match = ENABLED_RE.search(text)
    active_match = ACTIVE_RE.search(text)
    cross_match = CROSS_RE.search(text)
    enabled = bool(enabled_match and _is_true(enabled_match.group(1)))
    active = _active_slug(active_match.group(2)) if active_match else None
    if not enabled:
        active = None
    config_root = profile.parent
    if enabled and active:
        active_root = config_root / "matters" / active
        if (config_root / "matters").is_symlink() or active_root.is_symlink():
            raise WorkspaceError(
                "El almacén o asunto activo usa un enlace simbólico; se bloquea "
                "para evitar escapar del límite de datos."
            )
        data_root = active_root
    else:
        data_root = config_root
    return WorkspaceState(
        profile=str(profile.resolve()),
        config_root=str(config_root.resolve()),
        data_root=str(data_root.resolve()),
        scope=scope,
        enabled=enabled,
        active=active,
        cross_matter=bool(cross_match and _is_true(cross_match.group(1))),
    )


def _validate_slug(slug: str) -> str:
    if not SLUG_RE.fullmatch(slug):
        raise WorkspaceError(
            "Slug inválido. Usa minúsculas, números y guiones; ejemplo: "
            "acme-marca-2026."
        )
    return slug


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode if path.exists() else None
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        handle.write(text)
        temp_name = handle.name
    if mode is not None:
        os.chmod(temp_name, mode)
    os.replace(temp_name, path)


def _private_write(path: Path, text: str) -> None:
    _atomic_write(path, text)
    os.chmod(path, 0o600)


def _managed_dir(path: Path, *, create: bool = False) -> Path:
    if path.is_symlink():
        raise WorkspaceError(f"Directorio administrado rechazado por symlink: {path}")
    if create:
        path.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.exists():
        if not path.is_dir():
            raise WorkspaceError(f"La ruta administrada no es directorio: {path}")
        os.chmod(path, 0o700)
    return path


def _matter_dir(matters_root: Path, slug: str, *, must_exist: bool = False) -> Path:
    matter = matters_root / slug
    if matter.is_symlink():
        raise WorkspaceError(f"Asunto rechazado por symlink: {slug}")
    if must_exist and not matter.is_dir():
        raise WorkspaceError(f"No existe un asunto activo con slug '{slug}'.")
    return matter


def _set_active(profile: Path, slug: str | None) -> None:
    text = profile.read_text(encoding="utf-8")
    replacement = "ninguno" if slug is None else slug
    if not ACTIVE_RE.search(text):
        raise WorkspaceError("El perfil no contiene la línea **Asunto activo:**.")
    updated = ACTIVE_RE.sub(
        lambda match: f"{match.group(1)}{replacement}{match.group(3)}", text, count=1
    )
    _atomic_write(profile, updated)


def _require_enabled(state: WorkspaceState) -> None:
    if not state.enabled:
        raise WorkspaceError(
            "Los espacios por asunto están desactivados en el perfil activo. "
            "Actívalos mediante cold-start antes de administrar asuntos."
        )


def command_new(state: WorkspaceState, slug: str) -> dict:
    _require_enabled(state)
    slug = _validate_slug(slug)
    root = _managed_dir(Path(state.config_root))
    matters_root = _managed_dir(root / "matters", create=True)
    matter = _matter_dir(matters_root, slug)
    archived_root = matters_root / "_archived"
    if archived_root.is_symlink():
        raise WorkspaceError("El archivo de asuntos no puede ser un symlink.")
    archived = archived_root / slug
    if matter.exists() or archived.exists():
        raise WorkspaceError(
            f"El slug '{slug}' ya existe (activo o archivado); elige otro."
        )
    matter.mkdir(mode=0o700)
    _managed_dir(matter / "outputs", create=True)
    today = date.today().isoformat()
    _private_write(
        matter / "matter.md",
        "# Admisión pendiente\n\n"
        f"**Slug:** {slug}\n"
        f"**Apertura:** {today}\n"
        "**Estado:** admisión-pendiente\n\n"
        "Reemplazar este archivo con la plantilla de admisión del skill.\n",
    )
    _private_write(
        matter / "history.md",
        f"# Historial: {slug}\n\n---\n\n"
        f"## {today} — Espacio creado\n\n"
        "Admisión pendiente. El espacio se activó antes de escribir datos del cliente.\n",
    )
    _private_write(matter / "notes.md", "")
    _set_active(Path(state.profile), slug)
    return {
        "action": "new",
        "slug": slug,
        "active": slug,
        "matter_root": str(matter.resolve()),
        "intake_pending": True,
    }


def _matter_summary(path: Path, archived: bool, active: str | None) -> dict:
    if path.is_symlink():
        raise WorkspaceError(f"matter.md rechazado por symlink: {path.parent.name}")
    text = path.read_text(encoding="utf-8", errors="replace")[:8000]

    def field(name: str) -> str | None:
        match = re.search(
            rf"^\*\*{re.escape(name)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE
        )
        return match.group(1).strip() if match else None

    slug = path.parent.name
    return {
        "slug": slug,
        "status": "archivado" if archived else (field("Estado") or "activo"),
        "opened": field("Apertura"),
        "active": slug == active,
        "archived": archived,
    }


def command_list(state: WorkspaceState) -> dict:
    _require_enabled(state)
    matters_root = _managed_dir(Path(state.config_root) / "matters")
    for child in matters_root.iterdir() if matters_root.exists() else ():
        if child.is_symlink():
            raise WorkspaceError(f"Entrada de asunto rechazada por symlink: {child.name}")
    active_rows = [
        _matter_summary(path, False, state.active)
        for path in sorted(matters_root.glob("*/matter.md"))
        if path.parent.name != "_archived"
    ]
    archived_root = _managed_dir(matters_root / "_archived")
    for child in archived_root.iterdir() if archived_root.exists() else ():
        if child.is_symlink():
            raise WorkspaceError(
                f"Entrada de asunto archivado rechazada por symlink: {child.name}"
            )
    archived_rows = [
        _matter_summary(path, True, state.active)
        for path in sorted(archived_root.glob("*/matter.md"))
    ]
    return {
        "action": "list",
        "active": state.active,
        "matters": active_rows,
        "archived": archived_rows,
    }


def command_switch(state: WorkspaceState, slug: str) -> dict:
    _require_enabled(state)
    slug = _validate_slug(slug)
    matters_root = _managed_dir(Path(state.config_root) / "matters")
    matter_dir = _matter_dir(matters_root, slug, must_exist=True)
    matter = matter_dir / "matter.md"
    if matter.is_symlink():
        raise WorkspaceError(f"matter.md rechazado por symlink en '{slug}'.")
    if not matter.is_file():
        raise WorkspaceError(f"No existe un asunto activo con slug '{slug}'.")
    _set_active(Path(state.profile), slug)
    return {
        "action": "switch",
        "active": slug,
        "matter_root": str(matter.parent.resolve()),
    }


def command_close(state: WorkspaceState, slug: str) -> dict:
    _require_enabled(state)
    slug = _validate_slug(slug)
    root = _managed_dir(Path(state.config_root) / "matters")
    source = _matter_dir(root, slug, must_exist=True)
    archive = _managed_dir(root / "_archived", create=True)
    destination = archive / slug
    if destination.is_symlink():
        raise WorkspaceError(f"Destino archivado rechazado por symlink: {slug}")
    if not (source / "matter.md").is_file():
        raise WorkspaceError(f"No existe un asunto activo con slug '{slug}'.")
    if (source / "matter.md").is_symlink():
        raise WorkspaceError(f"matter.md rechazado por symlink en '{slug}'.")
    if destination.exists():
        raise WorkspaceError(f"Ya existe un asunto archivado con slug '{slug}'.")
    today = date.today().isoformat()
    history = source / "history.md"
    if history.is_symlink():
        raise WorkspaceError(f"history.md rechazado por symlink en '{slug}'.")
    with history.open("a", encoding="utf-8") as handle:
        handle.write(f"\n## {today} — Cerrado\n\nEspacio archivado; no eliminado.\n")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source), str(destination))
    new_active = state.active
    if state.active == slug:
        _set_active(Path(state.profile), None)
        new_active = None
    return {
        "action": "close",
        "slug": slug,
        "active": new_active,
        "archived_root": str(destination.resolve()),
    }


def command_none(state: WorkspaceState) -> dict:
    _require_enabled(state)
    _set_active(Path(state.profile), None)
    return {"action": "none", "active": None, "data_root": state.config_root}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("list")
    for name in ("new", "switch", "close"):
        child = sub.add_parser(name)
        child.add_argument("slug")
    sub.add_parser("none")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        state = load_state(Path.cwd())
        if args.command == "status":
            result = {"action": "status", **asdict(state)}
        elif args.command == "list":
            result = command_list(state)
        elif args.command == "new":
            result = command_new(state, args.slug)
        elif args.command == "switch":
            result = command_switch(state, args.slug)
        elif args.command == "close":
            result = command_close(state, args.slug)
        else:
            result = command_none(state)
    except (OSError, WorkspaceError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({"ok": True, **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
