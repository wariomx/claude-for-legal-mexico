# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

`claude-for-legal` is a Claude Code plugin marketplace — twelve first-party
legal plugins, one vendor plugin, and five managed-agent cookbooks. Most work
here is editing prompt content (skills, agents, hooks), plugin metadata, or
cookbook config — not application code. Everything is markdown and JSON; no build
step.

## Layout

```
.claude-plugin/marketplace.json   # the marketplace manifest — one entry per plugin
<plugin>/                         # 12 first-party plugins (commercial-legal, privacy-legal, ...)
  .claude-plugin/plugin.json      # plugin manifest (name, version, description, author)
  .mcp.json                       # MCP servers the plugin connects to
  CLAUDE.md                       # practice-profile TEMPLATE (see "Plugin CLAUDE.md" below)
  README.md                       # per-plugin docs
  skills/<name>/SKILL.md          # one skill per directory
  agents/<name>.md                # subagent definitions
  hooks/hooks.json                # hook config (most plugins ship an empty stub)
  .gitignore
external_plugins/<vendor>/        # vendor-maintained plugins (CoCounsel)
managed-agent-cookbooks/<name>/   # CMA agent.yaml + subagents/ + steering-examples.json
scripts/                          # validate.py, lint-tool-scope.py, orchestrate.py,
                                  # deploy-managed-agent.sh, test-cookbooks.sh
references/                       # shared templates (company-profile, dashboard)
```

## Validation — run before opening a PR

There is no automated CI validation (only a CLA check). Run these locally:

```bash
# 1. Marketplace + per-plugin schema validation (source of truth)
claude plugin validate .claude-plugin/marketplace.json
for d in */; do [ -f "$d/.claude-plugin/plugin.json" ] && claude plugin validate "$d"; done
claude plugin validate external_plugins/cocounsel-legal

# 2. Cookbook tool-scope lint (orchestrators must not over-grant tools)
python3 scripts/lint-tool-scope.py

# 3. JSON/YAML sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"

# 4. Cookbook dry-run (runs deploy-managed-agent.sh in dry-run mode per cookbook)
bash scripts/test-cookbooks.sh
```

Note: `scripts/validate.py` is *not* for plugin validation — it validates CMA
subagent structured output against JSON schemas during deployment. Use
`claude plugin validate` for plugin structure.

### Marketplace invariants (I1–I11)

`claude-plugins-official` layers these on top of the schema check. They apply
here too — the ones most likely to trip a contributor:

- **I1** — `plugins[]` should be alpha-sorted by name (case-insensitive).
  *Currently a known warning: the array is in a curated display order. If you
  add a plugin, ask before re-sorting the whole array.*
- **I2** — no duplicate plugin names.
- **I3** — `description` 10–2000 chars, no leading/trailing whitespace.
- **I8** — every vendored `source` (`"./<dir>"`) must point at a directory that
  contains `.claude-plugin/plugin.json`.
- **I9** — `source` paths/URLs must contain no shell metacharacters or `..`.
- **I10** — no hidden Unicode (zero-width chars, bidi controls) in
  `name`/`description`.
- **I11** — `name` must match `^[a-z0-9][a-z0-9-]{1,63}$`.

### Frontmatter requirements

Every `agents/*.md` needs `name` and `description`. Every
`skills/<name>/SKILL.md` needs `description`. Every `commands/*.md` needs
`description`. Multi-line descriptions use `>` block scalars and that's fine —
`claude plugin validate` parses them correctly.

## Design principle

**SKILL.md encodes the right behavior; CLAUDE.md guardrails are the net.** If a
skill's correct output depends on a guardrail in the plugin's `CLAUDE.md`
catching a mistake the `SKILL.md` would have made, add the behavior to the
`SKILL.md` directly. The guardrail stays (belt and suspenders), but the skill
should carry the knowledge it needs on its own. See `CONTRIBUTING.md` for
worked examples.

## Conventions

### Version bumps

Bump the plugin version in `.claude-plugin/plugin.json` on material changes:
patch for behavior additions, minor for new skills or new required inputs.

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and
`author` should match the plugin's own `.claude-plugin/plugin.json` field for
field. If you change a plugin's description in one place, change it in the
other.

### Skill names in prose must be canonical

When a `SKILL.md` (especially `customize` or `cold-start-interview`) tells the
user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.
Short forms like `/triage` for `/use-case-triage` look right in prose but are
dead commands — the user types them and nothing happens. Refs to Claude Code
built-ins (`/mcp`, `/plugin`) and to other plugins (`/<other-plugin>:<skill>`)
are fine.

### Plugin CLAUDE.md is a template, not project context

Each `<plugin>/CLAUDE.md` is a practice-profile template that the
`cold-start-interview` skill copies to `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`
on the user's machine. It is *not* loaded as project context when the plugin is
installed — `claude plugin validate` warns about this and the warning is
expected. Don't "fix" it by moving the content into a skill.

### `external_plugins/` is vendor-maintained

Plugins under `external_plugins/` are built and maintained by the vendor
(README.md has the policy). Don't change vendor-authored content without
checking with them first; whitespace normalization and formatting are usually
fine since the vendor lands changes via PR rather than mirroring a fork.

### Formatting

- 2-space indent in all JSON and `.mcp.json` files.
- Final newline at end of every text file.
- No trailing whitespace.
- Markdown tables: pipe-aligned columns are nice but not required; just keep
  the column count consistent.

## Cookbooks

Each `managed-agent-cookbooks/<name>/` has `agent.yaml` (the orchestrator),
`subagents/*.yaml` (the leaves), `steering-examples.json`, and `README.md`. Two
rules that `scripts/lint-tool-scope.py` enforces:

1. The orchestrator gets local-only tools (`read`, `grep`, `glob`,
   `agent_toolset`); MCP and write tools belong to specific subagent leaves.
2. The README's security table and the `agent.yaml` comments must match what
   the YAML actually grants. Don't claim a tool a subagent doesn't have.

## First-time contributors

Sign the CLA. The CLA Assistant bot comments on your first PR with a link; reply
with `I have read the CLA Document and I hereby sign the CLA` and the check
passes. One-time only.

## Things to leave alone

- Per-plugin `.gitignore` files differ slightly across plugins. Probably
  intentional; ask before unifying.
- `hooks/hooks.json` is missing in two plugins. Hooks are optional; the missing
  files are not a bug.
- `references/` lives only at repo root and is not shipped inside any plugin
  directory. Several plugin `CLAUDE.md` templates reference it as if it were —
  that's a known gap, not a thing to silently move.
