# demand-letters/ — trabajo de requerimiento pre-litigio

Esta carpeta contiene el producto de trabajo de cada carta de requerimiento que el abogado envía: requerimientos de pago, avisos de incumplimiento y saneamiento, cartas de cesación (propiedad intelectual), avisos de rescisión laboral y requerimientos de preservación documental.

Separada de `matters/` porque:

- No toda carta de requerimiento amerita un asunto en el portafolio. Los requerimientos de pago de montos menores y las cobranzas rutinarias no necesitan una fila en el libro.
- Toda carta de requerimiento tiene la misma forma de flujo de trabajo (intake → borrador → envío → checklist), independientemente de si después se convierte en asunto.
- Cuando una carta de requerimiento sí se convierte en asunto, el `matter.md` del asunto enlaza de vuelta aquí — el historial de redacción permanece con la carta.

## Estructura

```
demand-letters/
├── _README.md                     # este archivo
└── [slug]/
    ├── intake.md                  # recopilación de contexto, estrategia, ventaja procesal, filtros de confidencialidad
    ├── draft-v1.docx              # la carta (v2, v3 según iteraciones)
    └── checklist.md               # checklist post-envío — acuse de recibo, copias, plazos, seguimiento
```

## Convención de slugs

`[tipo]-[contraparte]-[aaaa-mm]`. Ejemplos:

- `pago-acme-2026-04`
- `cesacion-competidor-x-2026-04`
- `incumplimiento-proveedor-2026-04`
- `rescision-laboral-garcia-2026-04`
- `preservacion-proveedor-2026-04`

## Flujo de trabajo

1. `/litigacion-legal-mexico:demand-intake [título]` → ejecuta intake adaptativo, escribe `intake.md`
2. `/litigacion-legal-mexico:demand-draft [slug]` → ejecuta checklist de conciliación / confidencialidad / postura, redacta `.docx`, escribe `checklist.md`, ofrece crear un asunto

## Relación con asuntos

Después de redactar una carta de requerimiento, `demand-draft` evalúa la materialidad (heurística del perfil de práctica en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`) y ofrece crear un asunto. Si la respuesta es sí, se agrega una fila al `matters/_log.yaml` con `source: carta-requerimiento`, y `matters/[slug-asunto]/matter.md` enlaza de vuelta a esta carpeta de carta de requerimiento.

Las cartas inmateriales permanecen solo aquí. Siguen siendo un registro de producto de trabajo — simplemente no se rastrean en el portafolio.

## Correcciones y versiones

Nunca sobrescribas un borrador enviado. Si una carta fue enviada y necesita revisión (ej., un requerimiento complementario), comienza `draft-v2.docx`. El historial de versiones es en sí mismo un registro útil.
