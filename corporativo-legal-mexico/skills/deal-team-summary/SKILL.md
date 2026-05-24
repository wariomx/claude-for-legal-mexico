---
name: deal-team-summary
description: >
  Agregar hallazgos de debida diligencia en un informe para el equipo de la
  operación al nivel adecuado para la audiencia — resumen ejecutivo para
  liderazgo, resumen de trabajo para el equipo. Usar cuando el usuario diga
  "informar al equipo de la operación", "cuál es el estado de la debida
  diligencia", "resumir hallazgos para [audiencia]", "actualización de la
  operación", o en la cadencia de informes programada.
---

# Resumen para el Equipo de la Operación

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omitir el resto de este párrafo — las habilidades usan el contexto a nivel práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y modificaciones. Escribir las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

El líder de la operación no lee 200 hallazgos. Lee: qué es material, qué cambió desde el último informe, qué necesita decisión. Esta habilidad comprime la salida de debida diligencia al nivel adecuado para el lector.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → Informe del equipo de la operación (cadencia, formato, qué lee el negocio)
- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/deal-context.md` → líder de la operación, cronograma
- Hallazgos actuales de la salida de diligence-issue-extraction

## Niveles de audiencia

Conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` — qué lee el negocio vs. qué es para el expediente. Niveles predeterminados:

| Audiencia | Recibe | No recibe |
|---|---|---|
| **Consejo / patrocinador ejecutivo** | Los 3-5 hallazgos materiales principales, impacto en precio/estructura, elementos de decisión | Detalle por categoría, hallazgos verdes, proceso |
| **Líder de la operación** | Todos los rojos, todos los amarillos, avance, elementos de decisión, siguientes pasos | Detalle de hallazgos verdes |
| **Equipo de trabajo** | Todo — hallazgos completos, estatus por categoría, vacíos | Nada retenido |

Preguntar qué nivel si no es evidente.

## El resumen

### Nivel ejecutivo

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

> Este informe agrega hallazgos de debida diligencia protegidos por secreto profesional y hereda el estatus de protección y confidencialidad de las fuentes. La distribución fuera del círculo de confidencialidad (incluyendo a equipos de negocio más amplios) puede comprometer dicha protección — confirmar que la lista de distribución corresponda al círculo de confidencialidad antes de enviar.

# [Código de operación] — Informe de Debida Diligencia — [fecha]

**Estatus:** [En tiempo / Hallazgos identificados / Hallazgos materiales]
**Cobertura:** [X]% del VDR revisado

## Hallazgos materiales

[3-5 máximo. Un párrafo cada uno. Qué es, por qué importa para la operación,
qué estamos haciendo al respecto.]

## Decisiones pendientes

- [ ] [Decisión específica — ajuste de precio, solicitud de indemnización, detonante de retiro]
  — [quién decide] — [para cuándo]

## Desde el último informe

[Qué cambió. Nuevos hallazgos, hallazgos resueltos, avance de cobertura.]
```

### Nivel líder de operación

Lo mismo que arriba más:

```markdown
## Todos los hallazgos abiertos por categoría

### 🔴 Rojo
[Título del hallazgo + una línea — enlace al hallazgo completo para detalle]

### 🟡 Amarillo
[igual]

## Avance

| Categoría | Docs revisados | Cobertura | Rojos | Amarillos | Estatus |
|---|---|---|---|---|---|
| [nombre] | [N/M] | [%] | [N] | [N] | [Completo / En progreso / Bloqueado] |

## Vacíos y seguimientos

- [Elementos de solicitud complementaria pendientes]
- [Preguntas a la administración]

## Próximas 72 horas

[Qué se va a revisar, qué informes están programados]
```

### Nivel equipo de trabajo

Detalle completo de hallazgos. Misma estructura que arriba pero cada hallazgo recibe su bloque completo en formato interno, no un resumen de una línea.

## Deltas

Si este es un informe recurrente (conforme a la cadencia en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`), abrir con lo que cambió:

- Nuevos hallazgos desde el último informe
- Hallazgos subidos/bajados de severidad
- Hallazgos resueltos (consentimiento obtenido, tema aclarado)
- Movimiento de cobertura

A los líderes de la operación les importa más el movimiento que el estado. "Siguen 12 amarillos" es menos útil que "2 nuevos amarillos, 3 resueltos."

## Handoffs

- **Desde diligence-issue-extraction:** Esta habilidad lee los hallazgos acumulados.
- **Hacia closing-checklist:** Cualquier elemento de "decisión pendiente" que se resuelva en condición de cierre va al checklist.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que esta habilidad acaba de producir — las cinco ramas predeterminadas (redactar el X, escalar, obtener más hechos, esperar y observar, algo más) son un punto de partida, no una restricción. El árbol es la salida; el abogado elige.

## Lo que esta habilidad no hace

- No toma la decisión de materialidad — reporta las decisiones que se hicieron al momento de la extracción.
- No decide qué hace el equipo de la operación respecto a un hallazgo — presenta la decisión.
- No distribuye el informe — lo redacta, un humano lo envía.
