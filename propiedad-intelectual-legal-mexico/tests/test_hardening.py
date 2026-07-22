from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parent
SCRIPTS = PLUGIN_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import check_connectors  # noqa: E402
import check_legal_sources  # noqa: E402
import matter_workspace  # noqa: E402
import renewal_watch  # noqa: E402


PROFILE_TEXT = """# Perfil local de prueba

## Espacios de trabajo por asunto

**Habilitado:** ✓
**Asunto activo:** ninguno
**Contexto entre asuntos:** desactivado
"""


def write_local_profile(root: Path) -> Path:
    profile = (
        root
        / ".claude-legal"
        / matter_workspace.PLUGIN_NAME
        / "CLAUDE.md"
    )
    profile.parent.mkdir(parents=True)
    profile.write_text(PROFILE_TEXT, encoding="utf-8")
    return profile


class MatterWorkspaceTests(unittest.TestCase):
    def test_local_resolution_and_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            profile = write_local_profile(root)
            nested = root / "work" / "subdir"
            nested.mkdir(parents=True)

            state = matter_workspace.load_state(nested)
            self.assertEqual(state.scope, "local")
            self.assertEqual(Path(state.profile), profile.resolve())
            self.assertIsNone(state.active)
            self.assertEqual(Path(state.data_root), profile.parent.resolve())

            created = matter_workspace.command_new(state, "acme-marca-2026")
            self.assertEqual(created["active"], "acme-marca-2026")
            matter_root = Path(created["matter_root"])
            self.assertEqual(matter_root.stat().st_mode & 0o777, 0o700)
            self.assertEqual(
                (matter_root / "matter.md").stat().st_mode & 0o777, 0o600
            )
            active = matter_workspace.load_state(nested)
            self.assertEqual(active.active, "acme-marca-2026")
            self.assertEqual(
                Path(active.data_root),
                (profile.parent / "matters" / "acme-marca-2026").resolve(),
            )
            matter_workspace.command_new(active, "beta-patente")
            switched = matter_workspace.load_state(nested)
            self.assertEqual(switched.active, "beta-patente")
            matter_workspace.command_switch(switched, "acme-marca-2026")
            selected = matter_workspace.load_state(nested)
            listing = matter_workspace.command_list(selected)
            self.assertEqual(
                {row["slug"] for row in listing["matters"]},
                {"acme-marca-2026", "beta-patente"},
            )
            self.assertTrue(
                all("client" not in row and "matter_type" not in row for row in listing["matters"])
            )
            matter_workspace.command_close(selected, "acme-marca-2026")
            closed = matter_workspace.load_state(nested)
            self.assertIsNone(closed.active)
            self.assertTrue(
                (profile.parent / "matters" / "_archived" / "acme-marca-2026").is_dir()
            )

    def test_invalid_slug_is_rejected_before_write(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            state = matter_workspace.load_state(root)
            with self.assertRaises(matter_workspace.WorkspaceError):
                matter_workspace.command_new(state, "Acme Client")
            self.assertFalse((Path(state.config_root) / "matters").exists())


class MatterHookTests(unittest.TestCase):
    hook = PLUGIN_ROOT / "hooks" / "matter-isolation.py"

    def run_hook(self, cwd: Path, tool: str, tool_input: dict) -> dict | None:
        result = subprocess.run(
            [sys.executable, str(self.hook)],
            input=json.dumps(
                {"tool_name": tool, "tool_input": tool_input, "cwd": str(cwd)}
            ),
            text=True,
            capture_output=True,
            check=True,
            cwd=cwd,
        )
        return json.loads(result.stdout) if result.stdout.strip() else None

    def test_blocks_cross_matter_global_and_broad_searches(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            state = matter_workspace.load_state(root)
            matter_workspace.command_new(state, "active-client")
            config = Path(state.config_root)
            active = config / "matters" / "active-client"

            self.assertIsNone(
                self.run_hook(root, "Read", {"file_path": str(active / "matter.md")})
            )
            denied = self.run_hook(
                root,
                "Read",
                {"file_path": str(config / "matters" / "other-client" / "matter.md")},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root,
                "Read",
                {"file_path": str(matter_workspace.GLOBAL_ROOT / "CLAUDE.md")},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(root, "Glob", {"path": str(root), "pattern": "**/*"})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root, "Grep", {"path": str(config), "pattern": "cliente"}
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(root, "Grep", {"pattern": "cliente"})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root, "Edit", {"file_path": str(config / "CLAUDE.md")}
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root, "Bash", {"command": "rg cliente src"}
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_trusted_controller_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            command = f'python3 "{SCRIPTS / "matter_workspace.py"}" list'
            self.assertIsNone(self.run_hook(root, "Bash", {"command": command}))

            unsafe = (
                f'python3 "{SCRIPTS / "matter_workspace.py"}" '
                f'--cwd "{root.parent}" list'
            )
            denied = self.run_hook(root, "Bash", {"command": unsafe})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_fails_closed_if_profile_disappears_but_matters_remain(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            profile = write_local_profile(root)
            state = matter_workspace.load_state(root)
            matter_workspace.command_new(state, "protected-client")
            protected_file = profile.parent / "matters" / "protected-client" / "matter.md"
            profile.unlink()

            denied = self.run_hook(
                root, "Read", {"file_path": str(protected_file)}
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root,
                "mcp__LegalDataHunter__search",
                {"query": "artículo 386 LFPPI"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_mcp_client_stores_and_unverified_writes_are_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            state = matter_workspace.load_state(root)
            matter_workspace.command_new(state, "active-client")

            denied = self.run_hook(
                root,
                "mcp__Google_Drive__search_files",
                {"query": "client"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            self.assertIsNone(
                self.run_hook(
                    root,
                    "mcp__LegalDataHunter__search",
                    {"query": "artículo 386 LFPPI"},
                )
            )
            denied = self.run_hook(
                root,
                "mcp__LegalDataHunter__create_memo",
                {"title": "memo"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root,
                "mcp__plugin_conectores_google_drive__search_files",
                {"query": "client"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root,
                "mcp__LegalDataHunter__files_create",
                {"title": "memo"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            denied = self.run_hook(
                root,
                "mcp__LegalDataHunter__do_thing",
                {"value": "x"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_active_matter_denies_shell_except_canonical_read_only_watcher(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            state = matter_workspace.load_state(root)
            matter_workspace.command_new(state, "active-client")

            denied = self.run_hook(root, "Bash", {"command": "pwd"})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )
            watcher = (
                f'python3 "{SCRIPTS / "renewal_watch.py"}" '
                "--resolve --days 90 --format markdown"
            )
            self.assertIsNone(self.run_hook(root, "Bash", {"command": watcher}))
            source_check = (
                f'python3 "{SCRIPTS / "check_legal_sources.py"}" '
                "--strict --as-of 2026-07-22 --format markdown"
            )
            self.assertIsNone(
                self.run_hook(root, "Bash", {"command": source_check})
            )
            unsafe = (
                f'python3 "{SCRIPTS / "renewal_watch.py"}" '
                f'--portfolio "{root.parent / "other.json"}"'
            )
            denied = self.run_hook(root, "Bash", {"command": unsafe})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_blocks_another_projects_local_store(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "current"
            other = Path(temp) / "other"
            root.mkdir()
            other.mkdir()
            write_local_profile(root)
            other_profile = write_local_profile(other)
            state = matter_workspace.load_state(root)
            matter_workspace.command_new(state, "active-client")

            denied = self.run_hook(
                root, "Read", {"file_path": str(other_profile)}
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_rejects_symlink_escape_from_active_matter(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_local_profile(root)
            state = matter_workspace.load_state(root)
            created = matter_workspace.command_new(state, "active-client")
            outside = root / "outside-secret.txt"
            outside.write_text("other client", encoding="utf-8")
            link = Path(created["matter_root"]) / "linked-secret.txt"
            os.symlink(outside, link)

            denied = self.run_hook(root, "Read", {"file_path": str(link)})
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )

    def test_mcp_writes_fail_closed_without_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            denied = self.run_hook(
                root,
                "mcp__Slack__messages_send",
                {"channel": "x", "text": "y"},
            )
            self.assertEqual(
                denied["hookSpecificOutput"]["permissionDecision"], "deny"
            )


class RenewalWatcherTests(unittest.TestCase):
    def registry(self) -> dict:
        return {
            "schema_version": "1.0.0",
            "as_of": "2026-07-22",
            "rules": [
                {
                    "id": "MX-LFPPI-MARK-RENEWAL-001",
                    "status": "verified_primary",
                    "last_verified": "2026-07-22",
                    "next_review": "2027-01-01",
                }
            ],
        }

    @staticmethod
    def event(event_id: str, due: str, **overrides) -> dict:
        value = {
            "event_id": event_id,
            "rule_id": "MX-LFPPI-MARK-RENEWAL-001",
            "action": "Revisar y presentar renovación",
            "due_date": due,
            "grace_end": None,
            "status": "pending",
            "source": {
                "kind": "official_registry",
                "reference": "expediente 123",
                "captured_at": "2026-07-20T12:00:00-06:00",
            },
            "human_verified": True,
            "verified_by": "test-reviewer",
            "verified_against_registry_at": "2026-07-20T12:05:00-06:00",
            "calculation_trace": "fecha registral + regla vigente",
        }
        value.update(overrides)
        return value

    def test_classifies_only_docketed_events_and_preserves_unknowns(self) -> None:
        portfolio = {
            "metadata": {
                "schema_version": "2.0.0",
                "ultima_actualizacion": "2026-07-20",
                "sistema_fuente": "manual",
            },
            "assets": [
                {
                    "id": "MCA-1",
                    "mark_or_title": "Marca uno",
                    "jurisdiction": "MX-IMPI",
                    "deadline_events": [
                        self.event("renew", "2026-08-10"),
                        self.event(
                            "late",
                            "2026-07-21",
                            human_verified=False,
                            calculation_trace="",
                        ),
                        self.event("later", "2026-10-30"),
                    ],
                },
                {
                    "id": "LEGACY-1",
                    "mark_or_title": "Legada",
                    "next_deadlines": [{"due_date": "2026-08-01"}],
                },
                {
                    "id": "BAD-GRACE",
                    "mark_or_title": "Gracia inválida",
                    "deadline_events": [
                        self.event(
                            "bad-grace",
                            "2026-08-10",
                            grace_end="2026-08-09",
                        )
                    ],
                },
            ]
        }
        report = renewal_watch.build_report(
            portfolio,
            self.registry(),
            date(2026, 7, 22),
            180,
            90,
            Path("portfolio.json"),
        )
        by_id = {row["event_id"]: row for row in report["alerts"]}
        self.assertEqual(by_id["renew"]["urgency"], "next_30_days")
        self.assertEqual(by_id["renew"]["verification_state"], "verified")
        self.assertEqual(by_id["late"]["urgency"], "overdue")
        self.assertEqual(by_id["late"]["verification_state"], "review_required")
        self.assertIn("calculation_trace ausente", by_id["late"]["verification_blockers"])
        self.assertEqual(by_id["later"]["urgency"], "90_to_180_days")
        reasons = {row["reason"] for row in report["unknown"]}
        self.assertTrue(any("next_deadlines legado" in reason for reason in reasons))
        self.assertIn("grace_end es anterior a due_date", reasons)

    def test_rejects_false_clear_from_maintained_asset_without_events(self) -> None:
        portfolio = {
            "metadata": {
                "schema_version": "2.0.0",
                "ultima_actualizacion": "2026-07-22",
                "sistema_fuente": "manual",
            },
            "assets": [
                {
                    "id": "MCA-EMPTY",
                    "type": "marca",
                    "status": "registrada",
                    "mark_or_title": "Marca sin docket",
                    "jurisdiction": "MX-IMPI",
                    "deadline_events": [],
                }
            ],
        }
        report = renewal_watch.build_report(
            portfolio,
            self.registry(),
            date(2026, 7, 22),
            90,
            90,
            Path("portfolio.json"),
        )
        self.assertEqual(report["summary"]["unknown"], 1)
        self.assertIn("sin deadline_event", report["unknown"][0]["reason"])

    def test_surfaces_unverified_event_outside_window(self) -> None:
        portfolio = {
            "metadata": {
                "schema_version": "2.0.0",
                "ultima_actualizacion": "2026-07-22",
                "sistema_fuente": "manual",
            },
            "assets": [
                {
                    "id": "MCA-FUTURE",
                    "type": "marca",
                    "status": "registrada",
                    "mark_or_title": "Marca futura",
                    "jurisdiction": "MX-IMPI",
                    "deadline_events": [
                        self.event(
                            "future",
                            "2027-07-22",
                            human_verified=False,
                            verified_by=None,
                            verified_against_registry_at=None,
                        )
                    ],
                }
            ],
        }
        report = renewal_watch.build_report(
            portfolio,
            self.registry(),
            date(2026, 7, 22),
            90,
            90,
            Path("portfolio.json"),
        )
        self.assertEqual(report["alerts"], [])
        self.assertEqual(report["summary"]["unknown"], 1)
        self.assertIn("fuera de ventana", report["unknown"][0]["reason"])


class ConnectorCapabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry_path = PLUGIN_ROOT / "references" / "connector-capabilities.json"
        self.registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        relative = self.registry["dependency"]["source_manifest"]
        self.manifest_path = (self.registry_path.parent / relative).resolve()
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def test_declared_manifest_has_no_registry_drift(self) -> None:
        report = check_connectors.build_report(
            self.registry,
            self.manifest,
            None,
            self.registry_path,
            self.manifest_path,
        )
        self.assertTrue(report["ok"])
        self.assertTrue(
            all(row["status"] == "configured_unverified" for row in report["connectors"])
        )
        self.assertTrue(
            all(not row["write_capabilities_verified"] for row in report["connectors"])
        )

    def test_only_successful_sanitized_probe_is_verified(self) -> None:
        inventory = {
            "servers": [
                {
                    "name": "Slack",
                    "tools": ["search_messages", "read_channel"],
                    "read_probes": [
                        {
                            "capability": "message_search",
                            "tool": "search_messages",
                            "status": "passed",
                            "operation": "read-only synthetic search",
                            "tested_at": "2026-07-22T10:20:00Z",
                            "non_sensitive": True,
                            "result_observed": True,
                        },
                        {
                            "capability": "channel_read",
                            "tool": "read_channel",
                            "status": "passed",
                            "operation": "read-only synthetic channel metadata",
                            "tested_at": "2026-07-22T10:21:00Z",
                            "non_sensitive": True,
                            "result_observed": True,
                        },
                    ],
                }
            ]
        }
        now = datetime(2026, 7, 22, 10, 30, tzinfo=timezone.utc)
        report = check_connectors.build_report(
            self.registry,
            self.manifest,
            inventory,
            self.registry_path,
            self.manifest_path,
            now=now,
        )
        rows = {row["id"]: row for row in report["connectors"]}
        self.assertEqual(rows["slack"]["status"], "verified")
        self.assertEqual(
            set(rows["slack"]["capabilities_verified"]),
            {"message_search", "channel_read"},
        )
        self.assertFalse(rows["slack"]["write_capabilities_verified"])
        self.assertEqual(rows["legaldatahunter"]["status"], "unavailable")
        self.assertTrue(
            all(row["status"] == "unsupported" for row in report["unsupported_capabilities"])
        )

        inventory["servers"][0]["read_probes"][0]["tested_at"] = "2026-07-22 10:00:00"
        report = check_connectors.build_report(
            self.registry,
            self.manifest,
            inventory,
            self.registry_path,
            self.manifest_path,
            now=now,
        )
        slack = {row["id"]: row for row in report["connectors"]}["slack"]
        self.assertEqual(slack["status"], "partially_verified")
        self.assertEqual(slack["capabilities_verified"], ["channel_read"])

    def test_mutating_or_stale_tool_does_not_verify_read_capability(self) -> None:
        inventory = {
            "servers": [
                {
                    "name": "LegalDataHunter",
                    "tools": ["files_create"],
                    "read_probes": [
                        {
                            "capability": "mexico_legal_research",
                            "tool": "files_create",
                            "status": "passed",
                            "operation": "claimed read",
                            "tested_at": "2026-07-22T09:00:00Z",
                            "non_sensitive": True,
                            "result_observed": True,
                        }
                    ],
                }
            ]
        }
        report = check_connectors.build_report(
            self.registry,
            self.manifest,
            inventory,
            self.registry_path,
            self.manifest_path,
            now=datetime(2026, 7, 22, 10, 30, tzinfo=timezone.utc),
        )
        row = {item["id"]: item for item in report["connectors"]}[
            "legaldatahunter"
        ]
        self.assertEqual(row["capabilities_verified"], [])
        self.assertEqual(row["status"], "configured_unverified")


class ProvenanceAndRuleTests(unittest.TestCase):
    def test_authority_and_rule_references_are_internally_consistent(self) -> None:
        authorities_doc = json.loads(
            (PLUGIN_ROOT / "references" / "legal-authorities.json").read_text(
                encoding="utf-8"
            )
        )
        rules_doc = json.loads(
            (PLUGIN_ROOT / "references" / "verified-rules.json").read_text(
                encoding="utf-8"
            )
        )
        authority_ids = [row["id"] for row in authorities_doc["authorities"]]
        rule_ids = [row["id"] for row in rules_doc["rules"]]
        self.assertEqual(len(authority_ids), len(set(authority_ids)))
        self.assertEqual(len(rule_ids), len(set(rule_ids)))
        for authority in authorities_doc["authorities"]:
            self.assertRegex(
                authority["official_url"],
                r"^https://(www\.diputados\.gob\.mx|sidof\.segob\.gob\.mx)/",
            )
            self.assertNotEqual(authority["content_hash_status"], "verified_hash")
        known = set(authority_ids)
        for rule in rules_doc["rules"]:
            self.assertTrue(rule["status"].startswith("verified_primary"))
            self.assertLessEqual(rule["last_verified"], rule["next_review"])
            self.assertTrue(rule["requires_human_review"])
            for reference in rule["authority_refs"]:
                self.assertIn(reference["authority_id"], known)

    def test_operational_docs_do_not_reintroduce_known_wrong_citations(self) -> None:
        text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(PLUGIN_ROOT.rglob("*.md"))
        )
        forbidden = [
            "Art. 387 LFPPI",
            "LFPPI Arts. 211-212",
            "LFPPI Arts. 213-215",
            "LFPPI Arts. 221-222",
            "bajo LFPPI Art. 13",
            "Art. 143 LFPPI",
            "Art. 152 bis LFPPI",
            "denuncia de calumnia (Art. 251 CPF",
            "calumnia bajo CPF Art. 251",
            "responsabilidad por denuncia calumniosa (CPF Art. 356)",
            "Unidad Especializada en Investigación de Delitos contra el Ambiente y Previstos en Leyes Especiales",
            "LFPPI Arts. 163-170",
            "contiene una declaración bajo protesta de decir verdad",
            "Solo los abogados titulados con cédula profesional gozan",
            "agente de propiedad industrial registrado puede",
            "Centro de Mediación del IMPI",
            "por su cuenta a investigación",
            "responsabilidad objetiva por infracción",
            "está caduca y no es una barrera",
            "[model knowledge — verify]",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, text)
        self.assertIn("MX-LFT-EMPLOYEE-INVENTIONS-001", text)
        self.assertIn("MX-LFPPI-ENFORCEMENT-PROCEDURE-001", text)

    def test_every_schema_is_valid_json(self) -> None:
        for path in (PLUGIN_ROOT / "schemas").glob("*.json"):
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(value.get("$schema"), "https://json-schema.org/draft/2020-12/schema")

    def test_legal_source_registry_is_operational_on_review_date(self) -> None:
        authorities_path = PLUGIN_ROOT / "references" / "legal-authorities.json"
        rules_path = PLUGIN_ROOT / "references" / "verified-rules.json"
        report = check_legal_sources.build_report(
            json.loads(authorities_path.read_text(encoding="utf-8")),
            json.loads(rules_path.read_text(encoding="utf-8")),
            date(2026, 7, 22),
            authorities_path,
            rules_path,
        )
        self.assertTrue(report["integrity_ok"], report["errors"])
        self.assertTrue(report["operational_ok"], report["warnings"])
        self.assertEqual(
            len(report["remote_unhashed_authorities"]), report["authority_count"]
        )


if __name__ == "__main__":
    unittest.main()
