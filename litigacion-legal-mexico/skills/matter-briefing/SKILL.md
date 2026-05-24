---
name: matter-briefing
description: Briefing profundo de un asunto — postura actual, qué ha cambiado, próximo plazo, preguntas abiertas y una verificación de re-evaluación de riesgo, listo antes de una actualización al Director Jurídico o una llamada con despacho externo. Usar cuando el usuario dice "ponme al día sobre [asunto]", "¿dónde estamos con [asunto]?", o necesita un resumen de un asunto específico.
argument-hint: "[slug]"
---

# /matter-briefing

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → calibración de riesgo + partes interesadas relevantes.
2. Seguir el flujo de trabajo y la referencia que se describen abajo.
3. Leer `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` + `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` + fila del log de `_log.yaml`.
4. Producir briefing: postura actual, qué ha cambiado desde la última actualización, próximo plazo, preguntas abiertas, verificación de re-evaluación de riesgo ("¿el campo `risk:` todavía refleja la realidad?").
5. Señalar obsolescencia: si `last_updated` > 30 días, decirlo.

---

# Briefing del asunto

## Propósito

Dar al abogado un resumen limpio de un asunto en el tiempo que toma caminar a una sala de juntas. Postura actual, qué ha cambiado, qué sigue, qué vale la pena reconsiderar.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — fila estructurada
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — ingreso narrativo
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` — registro de eventos
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — calibración de riesgo (para que "risk: alta" signifique algo específico, no genérico)

**Filtro de conflictos — infranqueable.** Antes del briefing, verificar `_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rechazar y redirigir:

> "No encuentro [slug del asunto] en el registro de asuntos. Ejecuta `/litigacion-legal-mexico:matter-intake` primero para que la verificación de conflictos se ejecute y el espacio de trabajo del asunto se configure. No construiré un briefing sobre un asunto que no ha sido ingresado — la verificación de conflictos es el filtro."

## Entrada

Slug (requerido). Si es ambiguo o falta, pedir al usuario que elija de una lista de asuntos activos.

## El briefing

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según config del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

# [Nombre del asunto] — Briefing al [fecha de hoy]

**Estado:** [estado / etapa]
**Riesgo:** [calificación] ([severidad] × [probabilidad])
**Materialidad:** [categoría]
**Despacho externo:** [despacho — líder]
**Última actualización:** [fecha] [señalar ⚠️ OBSOLETO si >30d]
**Conflictos:** [estado — señalar ⚠️ si `pending` o `not-run`]

---

## Resumen en un párrafo

[Postura actual. Qué estamos haciendo y por qué. Nombrar el hecho decisivo si hay uno capturado.]

## Qué ha cambiado recientemente

[Últimas 3-5 entradas de history.md, la más reciente primero. Si el historial es escaso, decirlo.]

## Qué sigue

- **Plazo inmediato:** [next_deadline + qué es]
- **Hitos próximos:** [cualquier cosa con fecha en matter.md o historial reciente]
- **Decisiones pendientes:** [preguntas abiertas señaladas en matter.md]

## Exposición

[Rango + cualquier cambio desde el ingreso. Si está provisionado, provisión actual + si la recalibración está vencida.]

## Responsables internos

[Quién está involucrado; si alguien debería estar involucrado y no lo está]

## Verificación de re-evaluación de riesgo

*Un impulso, no una respuesta.*

- ¿El `risk: [calificación]` todavía se siente correcto, o el caso se ha movido?
- ¿La `materiality: [categoría]` todavía coincide? (Hechos nuevos podrían empujar hacia provisión o revelación.)
- ¿Alguna nueva parte interesada que el asunto necesite (ej., CISO se vuelve relevante después de un desarrollo en la etapa probatoria)?

## Preguntas abiertas

[De matter.md y cualquier cosa sin resolver en el historial]

## Para la conversación

[Si el usuario especificó un propósito — "ponme al día antes de la llamada con el despacho externo" — adaptar la sección final: preguntas a hacer, decisiones a obtener, actualizaciones a extraer. Si no se dio propósito, omitir esta sección.]
```

## Obsolescencia

Si `last_updated > 30 días atrás`: señalar arriba Y sugerir ejecutar `/litigacion-legal-mexico:matter-update [slug]` después de la reunión para capturar lo que se discuta.

## Tono

Esto no es mercadotecnia. Decir lo que se sabe; señalar lo que no. Si un asunto tiene historial escaso y recién se abrió, el briefing es corto — y eso es correcto. No rellenar.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, observar y esperar, algo diferente) son un punto de partida, no una restricción. El árbol es el resultado; el abogado elige.

## Lo que este skill no hace

- Predecir resultados. La calificación de riesgo es un criterio capturado, no un pronóstico.
- Recomendar estrategia. Expone preguntas; el abogado las responde.
- Re-clasificar. Si el usuario quiere re-clasificar, eso es un `/litigacion-legal-mexico:matter-update` con cambios de campo — este skill lee, no escribe.
