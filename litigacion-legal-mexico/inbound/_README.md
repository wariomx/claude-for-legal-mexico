# inbound/ — correspondencia jurídica entrante

Esta carpeta contiene el triaje y el trabajo de respuesta para todo lo que llega del exterior: cartas de requerimiento recibidas, requerimientos judiciales y citatorios notificados a la empresa, consultas de reguladores, requerimientos de preservación y cartas de cesación dirigidas a nosotros.

Separada de `demand-letters/` (saliente) y `matters/` (portafolio rastreado) porque los documentos entrantes tienen su propio flujo de trabajo: leer → triaje → decidir → responder (o escalar a asunto). No todo lo que entra se convierte en un asunto rastreado.

## Estructura

```
inbound/
├── _README.md
└── [slug]/
    ├── incoming.pdf              # o .eml / .docx — el original (o enlace/referencia)
    ├── triage.md                 # análisis: alcance, mérito, opciones, recomendación
    └── response-v1.docx          # respuesta redactada, si respondemos (v2, v3 según iteraciones)
```

## Convención de slugs

`[tipo]-[remitente-corto]-[aaaa-mm]`. Ejemplos:

- `requerimiento-rec-acme-2026-04` (carta de requerimiento recibida)
- `citatorio-garcia-vs-nosotros-2026-04` (citatorio o requerimiento judicial)
- `regulador-cofece-consulta-2026-04`
- `preservacion-proveedor-2026-04` (carta de preservación recibida)

## Flujo de trabajo

| Tipo | Comando | Resultado |
|---|---|---|
| Carta de requerimiento recibida | `/litigacion-legal-mexico:demand-received [ruta]` | triage.md + borrador de respuesta opcional |
| Requerimiento judicial / citatorio | `/litigacion-legal-mexico:requerimiento-triage [ruta]` | triage.md + memorándum de objeciones |
| Consulta de regulador | *skill futuro* | |

Cada triaje cruza referencias con `matters/_log.yaml` buscando asuntos relacionados (misma contraparte, materia coincidente). Si existe un asunto relacionado, el triaje lo señala y ofrece agregarlo como entrada en related_matters. Si este documento entrante debería convertirse en un asunto rastreado, el triaje transfiere a `/litigacion-legal-mexico:matter-intake` con campos prellenados.

## Relación con asuntos

- Entrante + relacionado con asunto existente → enlace vía campo `related_matters` en `_log.yaml`; el archivo permanece en `inbound/`.
- Entrante + debe convertirse en asunto → crear asunto; matter.md enlaza de vuelta a `inbound/[slug]/`.
- Entrante + manejado y cerrado (no amerita asunto) → permanece en `inbound/` como registro.

## Relación con salientes

Si la respuesta a un requerimiento entrante es a su vez un requerimiento saliente (un contra-requerimiento), el triaje transfiere a `/litigacion-legal-mexico:demand-intake` prellenado. El requerimiento saliente reside en `demand-letters/`, con un enlace cruzado a esta carpeta de entrantes.
