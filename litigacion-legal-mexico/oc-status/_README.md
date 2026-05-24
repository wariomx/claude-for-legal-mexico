# oc-status/ — borradores semanales de solicitud de estatus a abogados externos

Resultado de `/litigacion-legal-mexico:oc-status`. Carpetas por ejecución fechadas por día; cada una contiene un archivo markdown por asunto redactado, más un `_summary.md`.

## Estructura

```
oc-status/
├── _README.md                       # este archivo
└── [AAAA-MM-DD]/
    ├── _summary.md                  # qué se ejecutó, qué se omitió y por qué
    ├── [slug-1].md                  # un borrador de correo por asunto
    ├── [slug-2].md
    └── ...
```

Cuando el MCP de Gmail está autenticado, los borradores de Gmail también se crean en la bandeja de entrada del usuario. Los archivos markdown son el registro persistente; los borradores de Gmail son la capa de acción.

## Cadencia

Semanal (lunes AM) cuando se programa. Registra el calendario con `/litigacion-legal-mexico:oc-status --setup-schedule`.

Ad-hoc en cualquier momento con `/litigacion-legal-mexico:oc-status` (filtro predeterminado) o `/litigacion-legal-mexico:oc-status --slug=[slug]` (un asunto).

## Limpieza

Las carpetas fechadas antiguas se acumulan. Nada las necesita después de que el despacho externo haya respondido y el historial del asunto esté actualizado. Se pueden eliminar las de más de 30 días de antigüedad.
