# matters/ — datos del portafolio

Esta carpeta contiene el portafolio de litigios. Dos capas:

- **`_log.yaml`** — el libro. Una fila por asunto. Parseable por los skills. Fuente de verdad para resúmenes.
- **`[slug]/`** — detalle por asunto. Narrativa e historial. Donde los humanos leen y editan.

## Estructura

```
matters/
├── _log.yaml                  # libro (todos los asuntos, incluyendo cerrados)
├── _README.md                 # este archivo
└── [slug-asunto]/
    ├── matter.md              # narrativa de intake + teoría del caso + postura
    └── history.md             # registro de eventos (solo agregar, nunca borrar)
```

## Convención de slugs

Minúsculas, guiones, año al final. Ejemplos:
- `acme-vs-nosotros-2026`
- `cofece-investigacion-2026`
- `laboral-garcia-2026`
- `amparo-reforma-fiscal-2026`

El año estabiliza el slug incluso si surge un asunto similar después. El nombre de la carpeta coincide exactamente con el slug.

## Quién escribe qué

| Archivo | Escrito por | ¿Editar directamente? |
|---|---|---|
| `_log.yaml` | `/litigacion-legal-mexico:matter-intake`, `/matter-update`, `/matter-close` | Sí, pero refleja el cambio en el `history.md` del asunto |
| `matter.md` | `/litigacion-legal-mexico:matter-intake` al inicio; completado por `/matter-close` | Sí, para notas de evolución de la teoría del caso / postura |
| `history.md` | `/litigacion-legal-mexico:matter-intake` siembra; `/matter-update` y `/matter-close` agregan | Solo agregar en la práctica — tratar las entradas pasadas como registro |

## Asuntos cerrados

Permanecen aquí. No borrar. `/litigacion-legal-mexico:portfolio-status` los filtra de los resúmenes activos por defecto; `/portfolio-status --all` los incluye. Los asuntos cerrados son el conjunto de entrenamiento para el criterio del portafolio.

## Correcciones

Si una entrada del historial fue errónea, no la edites. Agrega una nueva entrada que referencia y corrige la anterior. El registro de la corrección es tan importante como la corrección misma.
