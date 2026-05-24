---
name: portfolio-status
description: Consolidación del portafolio desde _log.yaml — distribución de riesgo, plazos próximos, asuntos sin movimiento, totales de materialidad, distribución por etapa procesal y anomalías señaladas. Úsalo cuando el usuario pregunte "¿cómo estamos?", "¿cuántos asuntos abiertos hay?" o quiera un resumen o estatus general de todos los asuntos activos.
argument-hint: "[--all | --risk=high | --stale]"
---

# /portfolio-status

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → calibración de riesgo (define cómo leer el campo `risk:`).
2. Seguir el flujo de trabajo y referencia a continuación.
3. Parsear `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`. Filtrar asuntos cerrados por defecto (incluir con `--all`).
4. Producir consolidación: distribución de riesgo, plazos en los próximos 14/30/60 días, asuntos sin actualización en >30 días, totales de materialidad, distribución por etapa procesal.
5. Señalar anomalías — todo lo marcado como crítico, next_deadline vencido, asuntos sin despacho externo asignado donde el riesgo es medio o alto.

---

# Estatus del Portafolio

## Propósito

Una lectura que responde: ¿qué tengo ahora mismo, qué necesita atención y qué se está rezagando? El resultado es escaneable — diseñado para un abogado que tiene tres minutos antes de su siguiente llamada.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — fuente de verdad
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — calibración de riesgo (para interpretar correctamente los campos de riesgo/materialidad)

## Banderas y filtros

Por defecto: solo asuntos activos (excluir `status: closed`).

Banderas:
- `--all` — incluir cerrados
- `--risk=high` (o `critical` / `medium` / `low`) — filtrar por banda de riesgo
- `--stale` — solo asuntos con `last_updated` > 30 días
- `--type=laboral` — filtrar por tipo de asunto
- `--owner=[nombre]` — filtrar por responsable de negocio/RH/comunicación

## La consolidación

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

# Estatus del Portafolio — [hoy]

**Asuntos activos:** [N]
**Cerrados (año en curso):** [N] *(se muestra solo con --all)*

---

## Por riesgo

| Riesgo | Cantidad | Asuntos |
|---|---|---|
| Crítico | [N] | [slugs] |
| Alto | [N] | [slugs] |
| Medio | [N] | [solo cantidad — expandir con `--risk=medium`] |
| Bajo | [N] | [solo cantidad] |

## Plazos próximos

| Dentro de | Asuntos |
|---|---|
| 14 días | [slug — plazo — breve descripción] |
| 15–30 días | [...] |
| 31–60 días | [...] |

*Los next_deadline vencidos se señalan por separado abajo.*

## Materialidad

| Categoría | Cantidad | Exposición total (punto medio) |
|---|---|---|
| Provisionado (NIF C-9) | [N] | [$X MXN] |
| Revelado (BMV/CNBV) | [N] | [$X MXN] |
| Monitoreado | [N] | — |
| Ninguno | [N] | — |

## Por etapa procesal

[tabla: instrucción / etapa probatoria / alegatos-sentencia / preparación de audiencia / convenio / apelación-amparo]

---

## ⚠️ Anomalías y señalamientos

- **Plazos vencidos:** [lista de slugs donde next_deadline ya pasó]
- **Sin movimiento (>30d sin actualización):** [lista]
- **Conflictos sin resolver:** [lista de slugs con `conflicts.status in [pending, not-run]`]
- **Conflictos con override activo:** [lista de slugs donde `conflicts.override.by` está poblado — señalamiento permanente hasta liberación manual]
- **Riesgo alto/crítico sin despacho externo:** [lista]
- **Provisionado sin actualización en >60d:** [lista] — probable necesidad de recalibración de provisión
- **Retención documental no emitida en litigio activo:** [lista]
- **Campos faltantes:** [slug → campo]

---

## Consejo de cierre

[Una o dos oraciones sobre qué revisar primero, si algo realmente destaca. No texto genérico — solo si algo verdaderamente resalta.]
```

## Reglas de anomalías

Estas son las verificaciones que hacen útil al skill en lugar de decorativo:

1. **Plazo vencido:** `next_deadline < hoy` y `status != closed`
2. **Sin movimiento:** `last_updated < hoy - 30d` y `status != closed`
3. **Conflictos sin resolver:** `conflicts.status in [pending, not-run]` y `status != closed`
3b. **Override de conflictos activo:** `conflicts.override.by != null` (nunca se limpia automáticamente)
4. **Riesgo alto sin cobertura:** `risk in [high, critical]` y `outside_counsel.firm == null`
5. **Provisión obsoleta:** `materiality == reserved` y `last_updated < hoy - 60d`
6. **Falta retención documental:** `status in [threatened, active, discovery, trial, appeal]` y `legal_hold.issued == false` — el deber de conservación documental (Cód. Comercio arts. 46–49) se activa desde la anticipación razonable de litigio, por lo que asuntos en etapa `threatened` están en alcance.
7. **Campos faltantes:** cualquier campo requerido nulo — `risk`, `materiality`, `status`, `opened`, `conflicts.status`

## Cerrar con el árbol de decisiones de siguientes pasos

Terminar con el árbol de decisiones de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, esperar y observar, algo más) son un punto de partida, no un candado. El árbol es el resultado; el abogado elige.

Si el portafolio tiene más de ~10 asuntos, o en cualquier momento que el usuario pida: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Adaptar la oferta a este resultado — conteos por nivel de riesgo, una línea de tiempo de plazos próximos, y una tabla de asuntos ordenable con estatus, verificación de conflictos y fecha de último movimiento.

## Qué no hace este skill

- Tomar decisiones. Muestra lo que necesita atención; el usuario decide la prioridad.
- Aparentar precisión que no tiene. Los puntos medios de exposición son aproximados y deben etiquetarse como tal.
- Reemplazar un sistema de gestión de asuntos real. Esta es una consolidación de memoria de trabajo, no un sistema de registro.
