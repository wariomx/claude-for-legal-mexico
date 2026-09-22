# Evals de civil-legal-mexico

Casos para `claude plugin eval`. Cada caso vive en `<caso>/` con `prompt.md` (frontmatter + prompt), `case.yaml` (contexto: `scaffold_script`), `fixture.sh`, `resources/` y `graders/*.md`.

## Correr

```bash
# desde la raíz del repo
claude plugin eval civil-legal-mexico --scaffold --trust-plugin --runs 1 --max-cost-usd 5 --no-publish
```

- `--scaffold` es obligatorio: `fixture.sh` copia el contrato sintético al directorio de trabajo del agente y siembra un perfil de práctica **local** en `.claude-legal/` (así la compuerta del Paso 0 encuentra configuración sin tocar `~/.claude/plugins/config` del usuario real).
- El brazo sin plugin corre automáticamente (`--ablation with-without`). Lo que importa es el **delta**: si el brazo con plugin empata al brazo sin plugin, la skill no está aportando.
- Los resultados van a `evals/results/` (ignorado por git).

## Dependencia de conectores en el sandbox

El sandbox del eval carga el plugin por ruta y **no resuelve** `dependencies` de marketplace. Con `"dependencies": ["conectores-legal-mexico@claude-for-legal-mexico"]` en `plugin.json`, el sandbox reporta `dependency-unsatisfied`, el plugin no se carga y el brazo "con plugin" corre sin skills (delta 0). Verificado el 2026-09-22 leyendo `trace.jsonl` con `--keep-temp`.

Mientras eso no cambie en Claude Code, medir la skill exige quitar la dependencia del manifest solo durante la corrida y restaurarla al terminar:

```bash
PJ=civil-legal-mexico/.claude-plugin/plugin.json
cp "$PJ" "$PJ.bak" && trap 'mv -f "$PJ.bak" "$PJ"' EXIT
python3 -c "import json;p='$PJ';d=json.load(open(p));d.pop('dependencies',None);open(p,'w').write(json.dumps(d,indent=2,ensure_ascii=False)+'\n')"
claude plugin eval civil-legal-mexico --scaffold --trust-plugin --runs 1 --max-cost-usd 5 --no-publish
```

No commitear el manifest sin la dependencia.

## Caso `arrendamiento-local-comercial`

Contrato de local comercial en Guadalajara, Jalisco, con siete defectos sembrados (renta en USD sin cláusula de conversión; 12 años sin inscripción en RPP; renuncia genérica a la preferencia; mejoras sin regla de destino; sin declaración de uso lícito; fiador sin inmueble identificado; representante sin poder identificado) más una cláusula que renuncia a los avisos irrenunciables del art. 2035. El prompt representa al arrendatario.

Graders: defectos sembrados (≥5 de 7), regla irrenunciable señalada como 🔴 con fundamento, higiene de citas de Jalisco, español y lado correcto, presencia de nota del revisor y tabla resumen, y `tool_used: Skill` como indicador de activación (solo brazo con plugin).

Resultados de referencia (2026-09-22, `claude` 2.1.278):

| Corrida | Juez | Con plugin | Sin plugin | Delta | Skill activada | Nota |
|---|---|---|---|---|---|---|
| 1 | haiku | 0.0 | 0.2 | −0.2 | no | `add_dirs` no expuso el contrato; ambos brazos sin archivo. Corregido: `fixture.sh` copia `contrato.md` al CWD |
| 2 | haiku | 0.4 | 0.4 | 0.0 | no | Plugin no cargado por `dependency-unsatisfied` (ver arriba) |
| 3 | haiku | 0.8 | 0.4 | +0.4 | sí | Solo falla `citas-jalisco` con evidencia limpia (54 arts. de Jalisco, 17 `[settled]`, 0 números del CCF) |
| 4 | haiku | 0.8 | 0.4 | +0.4 | sí | Grader de citas reescrito; vuelve a fallar con evidencia limpia (55 arts., 59 `[settled]`, 0 CCF) |
| 5 | sonnet | **1.0** | — (`--ablation none`) | — | sí | Mismo agente y graders; los siete pasan, incluido `citas-jalisco` |

El delta +0.4 con la skill activada es la evidencia de que el plugin aporta. El fallo de `citas-jalisco` con haiku sobre un mensaje de ~45k caracteres es del juez, no de la skill: con `--judge-model sonnet` el caso pasa al 100 %. **Recomendación:** correr este caso siempre con `--judge-model sonnet` (costo de juez ≈ USD 0.50 por brazo).
