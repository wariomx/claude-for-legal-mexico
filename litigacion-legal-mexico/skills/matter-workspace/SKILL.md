---
name: matter-workspace
description: >
  Gestión de espacios de trabajo por asunto para prácticas con múltiples clientes
  — crear, listar, cambiar, cerrar o desactivar el asunto activo. Usar cuando el
  usuario quiere crear un nuevo espacio de trabajo por asunto, cambiar el asunto
  activo, listar asuntos, archivar un asunto, o trabajar solo a nivel de práctica
  sin un asunto activo.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Los abogados litigantes trabajan con múltiples clientes y asuntos. Un espacio de trabajo por asunto mantiene el contexto de un cliente o encargo separado de todos los demás. Este skill administra dichos espacios de trabajo.

## Subcomandos

- `/litigacion-legal-mexico:matter-workspace new <slug>` — crear un nuevo espacio de trabajo, ejecutar un ingreso corto, escribir `matter.md`
- `/litigacion-legal-mexico:matter-workspace list` — listar asuntos con estado y bandera de activo
- `/litigacion-legal-mexico:matter-workspace switch <slug>` — establecer el asunto activo
- `/litigacion-legal-mexico:matter-workspace close <slug>` — archivar un asunto (mover a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_archived/`, nunca eliminar)
- `/litigacion-legal-mexico:matter-workspace none` — desactivar cualquier asunto activo, trabajar solo a nivel de práctica

Nota: `/litigacion-legal-mexico:matter-briefing [slug]` (sin subcomando) es un comando separado que produce un briefing sobre un asunto específico — útil para revisión de portafolio in-house. La gestión de espacios de trabajo por asunto vive aquí.

## Instrucciones

1. Leer `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — confirmar que la sección `## Espacios de trabajo por asunto` esté poblada. Si `Enabled` es `✗`, indicar al usuario: "Los espacios de trabajo por asunto están desactivados — estás configurado como práctica in-house con un solo cliente, así que el plugin funciona automáticamente desde el contexto a nivel de práctica. Si en realidad trabajas con múltiples clientes, ejecuta `/litigacion-legal-mexico:cold-start-interview --redo` y selecciona una configuración de práctica privada. De lo contrario, no necesitas `/matter-workspace` en absoluto." No marcar error — el estado desactivado es el esperado para usuarios in-house.
2. Seguir el flujo de trabajo y la referencia que se describen abajo.
3. Despachar según el primer token de `$ARGUMENTS`:
   - `new` → ejecutar la entrevista de ingreso, escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/<slug>/matter.md`, inicializar `history.md` y `notes.md`.
   - `list` → enumerar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/*/matter.md`, imprimir una tabla, marcar el asunto activo.
   - `switch` → actualizar la línea `Active matter:` en el CLAUDE.md a nivel de práctica.
   - `close` → mover `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/<slug>/` a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_archived/<slug>/`, registrar la fecha de cierre en `history.md`.
   - `none` → establecer `Active matter:` en `none — practice-level context only`.
4. Mostrar al usuario qué cambió y confirmar antes de escribir.

## Notas

- El skill nunca lee entre asuntos a menos que `Cross-matter context` sea `on` en el CLAUDE.md a nivel de práctica.
- Archivar no es eliminar — los asuntos cerrados permanecen legibles para fines de retención/conflictos.
- Los slugs son en minúsculas con guiones. Si un slug se reutiliza entre archivados y activos, el archivado se preserva bajo `_archived/<slug>/`.

---

# Espacio de trabajo por asunto

Los abogados litigantes de práctica múltiple (práctica privada — despacho solo, pequeño, grande) trabajan con muchos asuntos. El contexto de uno no debe filtrarse a otro. Este skill es la capa delgada de gestión de archivos que hace eso posible.

**El estado por defecto es desactivado.** Los usuarios in-house nunca ven esto — trabajan solo a nivel de práctica. Los espacios de trabajo por asunto se activan en cold-start para usuarios de práctica privada, o editando `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗`, este skill no se ejecuta; el skill `/matter-workspace` explica el estado desactivado y sugiere `/litigacion-legal-mexico:cold-start-interview --redo` para usuarios que realmente necesiten aislamiento por asunto.

## Estructura de almacenamiento

Todos los datos de asuntos viven bajo:

```
~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/
├── CLAUDE.md                       # perfil de práctica a nivel de práctica
└── matters/
    ├── <slug>/
    │   ├── matter.md               # cliente, contraparte, tipo de asunto, hechos clave, anulaciones
    │   ├── history.md              # registro fechado de eventos, decisiones, borradores, revisiones
    │   ├── notes.md                # notas de trabajo de forma libre
    │   └── outputs/                # resultados de skills para este asunto (subcarpeta opcional)
    └── _archived/
        └── <slug>/                 # asuntos cerrados — legibles pero no activos
```

Los slugs son en minúsculas con guiones. Ejemplos: `acme-demanda-2026`, `laboral-garcia-2026`, `cofece-investigacion-2026`.

## El asunto activo está en el CLAUDE.md de práctica

La línea `Active matter:` bajo `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica es la fuente única de verdad. Cambiar un asunto edita esa línea. No hay archivo de estado separado.

## Lógica de subcomandos

### `new <slug>`

1. Confirmar que el slug no esté ya presente en `matters/<slug>/` o `matters/_archived/<slug>/`. Si se reutiliza, pedir al usuario que elija un slug diferente.
2. Ejecutar la entrevista de ingreso:
   - **Cliente** (la parte que representamos, o la unidad de negocio interna si es in-house)
   - **Contraparte** (la otra parte — puede ser múltiple)
   - **Tipo de asunto** (leer el perfil de práctica del plugin para categorías típicas; para litigacion-legal-mexico: mercantil | laboral | propiedad intelectual | regulatorio / investigación | administrativo | acción colectiva | amparo | otro)
   - **Nivel de confidencialidad** (estándar | elevada | equipo limpio — elevada indica cuidado extra en configuraciones de asuntos cruzados)
   - **Hechos clave** (2–5 oraciones: de qué trata este asunto, quiénes son las partes interesadas, qué está en juego)
   - **Anulaciones específicas del asunto al playbook de práctica** (ej., "el cliente requiere que el convenio incluya cláusula de confidencialidad obligatoria", "la contraparte es un socio estratégico — tono de preservación de relación")
   - **Asuntos relacionados** (slugs de cualquier asunto conectado)
3. Escribir `matters/<slug>/matter.md` usando la plantilla que aparece abajo.
4. Inicializar `matters/<slug>/history.md` con una sola entrada "Abierto".
5. Crear un `matters/<slug>/notes.md` vacío.
6. **No** cambiar automáticamente al nuevo asunto. Preguntar: "¿Quieres cambiar a `<slug>` ahora? (`/litigacion-legal-mexico:matter-workspace switch <slug>`)"

### `list`

Enumerar `matters/*/matter.md`. Leer los primeros metadatos o líneas de cada archivo para extraer estado. Imprimir una tabla:

| Slug | Cliente | Tipo de asunto | Estado | Abierto | Activo |
|---|---|---|---|---|---|

Marcar el asunto activo con `*`. Incluir `_archived/*` bajo un encabezado separado "Archivados" si existen.

### `switch <slug>`

1. Confirmar que `matters/<slug>/matter.md` existe. Si no, ofrecer `/litigacion-legal-mexico:matter-workspace new <slug>`.
2. Editar la línea `Active matter:` en el CLAUDE.md a nivel de práctica a `Active matter: <slug>`.
3. Mostrar al usuario el resumen de matter.md para que confirme que está en el asunto correcto.

### `close <slug>`

1. Confirmar que `matters/<slug>/` existe.
2. Agregar una entrada "Cerrado" a `matters/<slug>/history.md` con la fecha de hoy.
3. Mover `matters/<slug>/` → `matters/_archived/<slug>/`.
4. Si el asunto cerrado era el asunto activo, establecer `Active matter:` en `none — practice-level context only`.

### `none`

Establecer `Active matter:` en el CLAUDE.md a nivel de práctica en `none — practice-level context only`. Confirmar con el usuario.

## Plantilla de `matter.md`

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según config del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin` en el CLAUDE.md a nivel de práctica]

# Asunto: [Cliente] — [descripción corta]

**Slug:** [slug]
**Abierto:** [AAAA-MM-DD]
**Estado:** activo
**Confidencialidad:** [estándar / elevada / equipo limpio]

---

## Partes

**Cliente:** [nombre]
**Contraparte:** [nombre(s)]

## Tipo de asunto

[mercantil | laboral | propiedad intelectual | regulatorio | administrativo | acción colectiva | amparo | otro — con justificación de una línea]

## Hechos clave

[2–5 oraciones. De qué trata este asunto. Quiénes son las partes interesadas. Qué está en juego. Qué lo distingue del playbook estándar.]

## Anulaciones específicas del asunto

*Cualquier desviación del playbook a nivel de práctica que aplique a este asunto y solo a este asunto.*

- [ej., "Convenio: el cliente requiere cláusula de confidencialidad en cualquier acuerdo."]
- [ej., "Tono: preservación de relación — la contraparte es un socio estratégico."]
- [ej., "Jurisdicción: debe ser arbitraje ICC, no jurisdicción ordinaria."]

## Asuntos relacionados

- [slug — una línea de por qué están relacionados]

## Notas sobre confidencialidad

[Si es elevada o equipo limpio, describir por qué. Quién puede ver los archivos del asunto. Si el contexto cruzado entre asuntos es permisible aun cuando está globalmente activado.]
```

## Inicialización de `history.md`

```markdown
# Historial: [Cliente] — [descripción corta]

Registro de eventos de solo agregar. El más reciente arriba.

---

## [AAAA-MM-DD] — Asunto abierto

Ingreso completado. Slug: `[slug]`. Estado: activo.
[Cualquier contexto inicial que valga preservar más allá de matter.md — ej., "Abierto en respuesta a demanda notificada por [contraparte]."]
```

## Contexto cruzado entre asuntos

El CLAUDE.md a nivel de práctica tiene una bandera `Cross-matter context:`. Cuando está `off` (por defecto), un skill trabajando en el asunto A **nunca lee** archivos en `matters/B/` para cualquier otro `B`. Punto. Esta es la garantía de confidencialidad que el ajuste existe para proveer.

Cuando está `on`, un skill puede leer archivos entre carpetas de asuntos solo cuando el usuario lo pide explícitamente (ej., "compara nuestra posición sobre topes de responsabilidad en los últimos cinco asuntos mercantiles"). Aun cuando está `on`, el comportamiento por defecto es cargar solo el asunto activo a menos que el usuario pida una vista cruzada.

## Lo que este skill no hace

- **Ejecutar una verificación de conflictos.** Los conflictos son responsabilidad del abogado/despacho; el ingreso captura lo que el usuario declara.
- **Aplicar retención documental.** Cerrar archiva un asunto; no elimina. La política de retención está fuera de alcance.
- **Redirigir resultados automáticamente.** El skill sustantivo decide dónde escribir; este skill le indica *cuál carpeta* está activa, no qué poner en ella.
- **Decidir si el contexto cruzado es apropiado.** Lee la bandera y obedece.
