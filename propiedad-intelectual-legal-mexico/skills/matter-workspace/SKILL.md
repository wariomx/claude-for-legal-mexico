---
name: matter-workspace
description: >
  Administra espacios de trabajo por asunto — crear, listar, cambiar, cerrar o
  desactivar el asunto activo. Úsalo en práctica privada multi-cliente para
  mantener el contexto de un cliente separado del de otro, o cuando un skill
  sustantivo necesita saber en qué asunto está trabajando.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Los profesionales de PI trabajan en múltiples clientes y asuntos. Un espacio de trabajo por asunto mantiene el contexto de un cliente o encargo separado de todos los demás. Este skill administra esos espacios de trabajo.

## Subcomandos

- `/propiedad-intelectual-legal-mexico:matter-workspace new <slug>` — crear un nuevo espacio de trabajo, ejecutar una admisión breve, escribir `matter.md`
- `/propiedad-intelectual-legal-mexico:matter-workspace list` — listar asuntos con estado y marca de activo
- `/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` — establecer el asunto activo
- `/propiedad-intelectual-legal-mexico:matter-workspace close <slug>` — archivar un asunto (mover a `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/_archived/`, nunca eliminar)
- `/propiedad-intelectual-legal-mexico:matter-workspace none` — desactivar cualquier asunto activo, trabajar solo a nivel de práctica

## Instrucciones

1. Leer `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md` — confirmar que la sección `## Espacios de trabajo por asunto` está configurada. Si `Habilitado` es `✗`, decir al usuario: "Los espacios de trabajo por asunto están desactivados — estás configurado como práctica in-house con un solo cliente, así que el plugin trabaja desde contexto a nivel de práctica automáticamente. Si realmente trabajas con múltiples clientes, vuelve a ejecutar `/propiedad-intelectual-legal-mexico:cold-start-interview --redo` y selecciona un entorno de práctica privada. De lo contrario, no necesitas `/propiedad-intelectual-legal-mexico:matter-workspace` en absoluto." No marcar error — el estado desactivado es el esperado para usuarios in-house.
2. Seguir la lógica de subcomandos abajo.
3. Despachar según el primer token de `$ARGUMENTS`:
   - `new` → ejecutar la entrevista de admisión, escribir `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<slug>/matter.md`, sembrar `history.md` y `notes.md`.
   - `list` → enumerar `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/*/matter.md`, imprimir una tabla, marcar el asunto activo.
   - `switch` → actualizar la línea `Asunto activo:` en el CLAUDE.md a nivel de práctica.
   - `close` → mover `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<slug>/` a `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/_archived/<slug>/`, registrar la fecha de cierre en `history.md`.
   - `none` → establecer `Asunto activo:` a `ninguno — solo contexto a nivel de práctica`.
4. Mostrar al usuario lo que cambió y confirmar antes de escribir.

## Notas

- El skill nunca lee entre asuntos a menos que `Contexto cruzado entre asuntos` esté en `on` en el CLAUDE.md a nivel de práctica.
- Archivar no es eliminar — los asuntos cerrados permanecen legibles para fines de retención y conflictos de interés.
- Los slugs son en minúsculas con guiones. Si un slug se reutiliza entre archivados y activos, el archivado se preserva bajo `_archived/<slug>/`.

---

Los profesionales de PI en práctica privada (despacho solo, pequeño, grande) trabajan en muchos asuntos. El contexto de uno no debe filtrarse al de otro. Este skill es la capa delgada de gestión de archivos que hace eso posible.

**El estado por defecto es desactivado.** Los usuarios in-house nunca ven esto — trabajan solo a nivel de práctica. Los espacios de trabajo por asunto se activan en el cold-start para usuarios de práctica privada, o editando `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Habilitado` es `✗`, este skill no se ejecuta; en su lugar explica el estado desactivado y sugiere `/propiedad-intelectual-legal-mexico:cold-start-interview --redo` para usuarios que realmente necesitan aislamiento por asunto.

## Estructura de almacenamiento

Todos los datos de asuntos viven bajo:

```
~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/
├── CLAUDE.md                       # perfil de práctica a nivel de práctica
└── matters/
    ├── <slug>/
    │   ├── matter.md               # cliente, contraparte, tipo de asunto, hechos clave, anulaciones
    │   ├── history.md              # bitácora de eventos, decisiones, borradores, revisiones
    │   ├── notes.md                # notas de trabajo de forma libre
    │   └── outputs/                # salidas de skills para este asunto (subcarpeta opcional)
    └── _archived/
        └── <slug>/                 # asuntos cerrados — legibles pero no activos
```

Slugs en minúsculas con guiones. Ejemplos: `acme-marca-2026`, `zenith-patente-fto`, `novacorp-licencia-pi`.

## El asunto activo está en el CLAUDE.md de práctica

La línea `Asunto activo:` bajo `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica es la única fuente de verdad. Cambiar de asunto edita esa línea. Sin archivo de estado separado.

## Lógica de subcomandos

### `new <slug>`

1. Confirmar que el slug no existe ya en `matters/<slug>/` ni en `matters/_archived/<slug>/`. Si se reutiliza, pedir al usuario que elija un slug diferente.
2. Ejecutar la entrevista de admisión:
   - **Cliente** (la parte que representamos, o la unidad de negocio interna si es in-house)
   - **Contraparte** (la otra parte — pueden ser varias; puede ser "infractor no identificado" para asuntos originados por vigilancia)
   - **Tipo de asunto** (leer el perfil de práctica del plugin para categorías típicas; para propiedad-intelectual-legal-mexico: solicitud de registro de marca | solicitud de patente | declaración administrativa de infracción | solicitud de reserva de derechos | opinión de FTO | dictamen de patentabilidad | licencia de PI | cesión de derechos | obra por encargo | vigilancia de marca | cumplimiento OSS | otro)
   - **Nivel de confidencialidad** (estándar | reforzado | equipo-limpio — reforzado genera cuidado extra en contexto cruzado; equipo-limpio es común en trabajo de FTO de patentes)
   - **Hechos clave** (2–5 oraciones: de qué trata este asunto, quiénes son las partes interesadas, qué está en juego)
   - **Anulaciones específicas del asunto a la postura de práctica** (p. ej., "el cliente quiere postura agresiva solo para esta marca", "la contraparte es un socio estratégico — solo tono mesurado", "inventor no disponible — no contactar para entrevista")
   - **Asuntos relacionados** (slugs de asuntos conectados)
3. Escribir `matters/<slug>/matter.md` usando la plantilla abajo.
4. Sembrar `matters/<slug>/history.md` con una entrada de "Apertura".
5. Crear un `matters/<slug>/notes.md` vacío.
6. **No** cambiar automáticamente al nuevo asunto. Preguntar: "¿Quieres cambiar a `<slug>` ahora? (`/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>`)"

### `list`

Enumerar `matters/*/matter.md`. Leer el encabezado o las primeras líneas de cada archivo para extraer el estado. Imprimir una tabla:

| Slug | Cliente | Tipo de asunto | Estado | Apertura | Activo |
|---|---|---|---|---|---|
| | | | | | |

Marcar el asunto activo con `*`. Incluir `_archived/*` bajo un encabezado separado de "Archivados" si existen.

### `switch <slug>`

1. Confirmar que `matters/<slug>/matter.md` existe. Si no, ofrecer `/propiedad-intelectual-legal-mexico:matter-workspace new <slug>`.
2. Editar la línea `Asunto activo:` en el CLAUDE.md a nivel de práctica a `Asunto activo: <slug>`.
3. Mostrar al usuario el resumen de matter.md para que confirme que está en el asunto correcto.

### `close <slug>`

1. Confirmar que `matters/<slug>/` existe.
2. Agregar una entrada de "Cerrado" a `matters/<slug>/history.md` con la fecha de hoy.
3. Mover `matters/<slug>/` → `matters/_archived/<slug>/`.
4. Si el asunto cerrado era el activo, establecer `Asunto activo:` a `ninguno — solo contexto a nivel de práctica`.

### `none`

Establecer `Asunto activo:` en el CLAUDE.md a nivel de práctica a `ninguno — solo contexto a nivel de práctica`. Confirmar con el usuario.

## Plantilla de `matter.md`

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin` en el CLAUDE.md a nivel de práctica]

# Asunto: [Cliente] — [descripción breve]

**Slug:** [slug]
**Apertura:** [AAAA-MM-DD]
**Estado:** activo
**Confidencialidad:** [estándar / reforzado / equipo-limpio]

---

## Partes

**Cliente:** [nombre]
**Contraparte:** [nombre(s)]

## Tipo de asunto

[solicitud de registro de marca | solicitud de patente | declaración administrativa de infracción | solicitud de reserva de derechos | opinión de FTO | dictamen de patentabilidad | licencia de PI | cesión de derechos | obra por encargo | vigilancia de marca | cumplimiento OSS | otro — con justificación de una línea]

## Hechos clave

[2–5 oraciones. De qué trata este asunto. Quiénes son las partes interesadas. Qué está en juego. Qué lo diferencia de la postura por defecto.]

## Anulaciones específicas del asunto

*Cualquier desviación de la postura a nivel de práctica que aplica a este asunto y solo a este asunto.*

- [p. ej., "Postura de enforcement: mesurada aquí aunque la postura de casa es agresiva — la contraparte es un socio comercial clave."]
- [p. ej., "Aprobación para aserción: se requiere visto bueno adicional de mercadotecnia antes de enviar cualquier carta."]
- [p. ej., "Equipo-limpio: archivos del asunto no legibles incluso con contexto cruzado activado."]

## Asuntos relacionados

- [slug — una línea de por qué está relacionado]

## Notas sobre confidencialidad

[Si es reforzado o equipo-limpio, describir por qué. Quién puede ver archivos del asunto. Si el contexto cruzado es permisible incluso cuando está globalmente activado.]
```

## Semilla de `history.md`

```markdown
# Historial: [Cliente] — [descripción breve]

Bitácora de eventos de solo-agregar. Más reciente arriba.

---

## [AAAA-MM-DD] — Asunto abierto

Admisión completada. Slug: `[slug]`. Estado: activo.
[Cualquier contexto inicial que valga la pena preservar más allá de matter.md — p. ej., "Abierto en respuesta a hallazgo de vigilancia de marca `APEXLEAF` en clase 25 ante IMPI."]
```

## Contexto cruzado entre asuntos

El CLAUDE.md a nivel de práctica tiene una bandera `Contexto cruzado entre asuntos:`. Cuando está en `off` (por defecto), un skill trabajando en el asunto A **nunca lee** archivos en `matters/B/` para cualquier otro `B`. Punto. Esta es la garantía de confidencialidad que existe para proveer esta configuración.

Cuando está en `on`, un skill puede leer archivos entre carpetas de asuntos solo cuando el usuario lo solicita explícitamente (p. ej., "muéstrame cada carta de enforcement que hemos enviado sobre esta marca en todos los asuntos"). Incluso cuando está en `on`, lo predeterminado es cargar solo el asunto activo a menos que el usuario pida una vista cruzada.

## Lo que este skill no hace

- **Ejecutar una depuración de conflictos de interés.** Los conflictos son responsabilidad del profesional / despacho; la admisión captura lo que el usuario declara.
- **Aplicar política de retención.** Cerrar archiva un asunto; no lo elimina. La política de retención está fuera del alcance.
- **Enrutar salidas automáticamente.** El skill sustantivo decide dónde escribir; este skill le indica *qué carpeta* está activa, no qué poner en ella.
- **Decidir si el contexto cruzado es apropiado.** Lee la bandera y obedece.
