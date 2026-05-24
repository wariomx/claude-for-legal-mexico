---
name: matter-workspace
description: >
  Gestión de espacios de trabajo por asunto — crear, listar, cambiar, cerrar o
  desactivar el asunto activo para que abogados con múltiples clientes mantengan
  el contexto de cada uno separado. Leído por cualquier skill sustantivo que
  necesite saber en qué asunto está trabajando. Usar cuando el usuario dice
  "nuevo asunto", "cambiar asunto", "listar asuntos", "cerrar asunto",
  "new matter", "switch matter", "list matters", "close matter", o quiere
  trabajar solo a nivel de práctica.
argument-hint: "<new | list | switch | close | none> [slug]"
---

# /matter-workspace

Los abogados de práctica múltiple trabajan con diversos clientes y asuntos. Un espacio de trabajo por asunto mantiene el contexto de un cliente o encargo separado de todos los demás. Este skill administra dichos espacios de trabajo.

## Subcomandos

- `/corporativo-legal-mexico:matter-workspace new <slug>` — crear un nuevo espacio de trabajo, ejecutar una entrevista corta de ingreso, escribir `matter.md`
- `/corporativo-legal-mexico:matter-workspace list` — listar asuntos con estado y bandera de activo
- `/corporativo-legal-mexico:matter-workspace switch <slug>` — establecer el asunto activo
- `/corporativo-legal-mexico:matter-workspace close <slug>` — archivar un asunto (mover a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/_archived/`, nunca eliminar)
- `/corporativo-legal-mexico:matter-workspace none` — desactivar cualquier asunto activo, trabajar solo a nivel de práctica

## Instrucciones

1. Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` — confirmar que la sección `## Espacios de trabajo por asunto` esté poblada. Si `Enabled` es `✗`, indicar al usuario: "Los espacios de trabajo por asunto están desactivados — estás configurado como práctica in-house con un solo cliente, así que el plugin funciona automáticamente desde el contexto a nivel de práctica. Si en realidad trabajas con múltiples clientes, ejecuta `/corporativo-legal-mexico:cold-start-interview --redo` y selecciona una configuración de práctica privada. De lo contrario, no necesitas `/matter-workspace` en absoluto." No marcar error — el estado desactivado es el esperado para usuarios in-house.
2. Usar el flujo de trabajo descrito abajo.
3. Despachar según el primer token de `$ARGUMENTS`:
   - `new` → ejecutar la entrevista de ingreso, escribir `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<slug>/matter.md`, inicializar `history.md` y `notes.md`.
   - `list` → enumerar `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/*/matter.md`, imprimir una tabla, marcar el asunto activo.
   - `switch` → actualizar la línea `Active matter:` en el CLAUDE.md a nivel de práctica.
   - `close` → mover `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<slug>/` a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/_archived/<slug>/`, registrar la fecha de cierre en `history.md`.
   - `none` → establecer `Active matter:` en `none — practice-level context only`.
4. Mostrar al usuario qué cambió y confirmar antes de escribir.

## Notas

- El skill nunca lee entre asuntos a menos que `Cross-matter context` sea `on` en el CLAUDE.md a nivel de práctica.
- Archivar no es eliminar — los asuntos cerrados permanecen legibles para fines de retención y conflictos de interés.
- Los slugs son en minúsculas con guiones. Si un slug se reutiliza entre archivados y activos, el archivado se preserva bajo `_archived/<slug>/`.

---

Los abogados de práctica múltiple (práctica privada — despacho individual, despacho mediano, despacho grande) trabajan en muchos asuntos. El contexto de uno no debe filtrarse a otro. Este skill es la capa delgada de gestión de archivos que hace eso posible.

**Estado predeterminado: desactivado.** Los usuarios in-house nunca ven esto — trabajan solo a nivel de práctica. Los espacios de trabajo por asunto se activan en el cold-start para usuarios de práctica privada, o editando `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗`, este skill no se ejecuta; `/corporativo-legal-mexico:matter-workspace` explica el estado desactivado y sugiere `/corporativo-legal-mexico:cold-start-interview --redo` para usuarios que realmente necesiten aislamiento por asunto.

## Estructura de almacenamiento

Todos los datos del asunto viven bajo:

```
~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/
├── CLAUDE.md                       # perfil de práctica a nivel general
└── matters/
    ├── <slug>/
    │   ├── matter.md               # cliente, contraparte, tipo de asunto, hechos clave, excepciones
    │   ├── history.md              # registro cronológico de eventos, decisiones, borradores, revisiones
    │   ├── notes.md                # notas de trabajo libres
    │   └── outputs/                # productos del skill para este asunto (subcarpeta opcional)
    └── _archived/
        └── <slug>/                 # asuntos cerrados — legibles pero no activos
```

Los slugs son en minúsculas con guiones. Ejemplos: `acme-compraventa-2026`, `zenith-renovacion`, `proveedor-xyz-nda`.

## El asunto activo está en el CLAUDE.md de práctica

La línea `Active matter:` bajo `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica es la única fuente de verdad. Cambiar de asunto edita esa línea. No hay archivo de estado separado.

## Lógica de subcomandos

### `new <slug>`

1. Confirmar que el slug no exista ya en `matters/<slug>/` ni en `matters/_archived/<slug>/`. Si se reutiliza, pedir al usuario que elija un slug diferente.
2. Ejecutar la entrevista de ingreso:
   - **Cliente** (la parte que representamos, o la unidad de negocio interna si es in-house)
   - **Contraparte** (la otra parte — puede haber varias)
   - **Tipo de asunto** (leer el perfil de práctica del plugin para categorías típicas; para corporativo-legal-mexico: F&A lado comprador | F&A lado vendedor | financiamiento | asunto del Consejo | reestructura corporativa | proyecto de integración | otro)
   - **Nivel de confidencialidad** (standard | heightened | clean-team — heightened genera cuidado adicional en configuraciones cross-matter)
   - **Hechos clave** (2–5 oraciones: de qué trata este asunto, quiénes son los interesados, qué está en juego)
   - **Excepciones específicas del asunto al playbook de práctica** (ej., "el cliente requiere cláusula penal del 20% no del 10%", "la contraparte es un socio estratégico — tono que preserve la relación")
   - **Asuntos relacionados** (slugs de asuntos conectados)
3. Escribir `matters/<slug>/matter.md` usando la plantilla de abajo.
4. Inicializar `matters/<slug>/history.md` con una sola entrada "Abierto".
5. Crear un `matters/<slug>/notes.md` vacío.
6. **No** cambiar automáticamente al nuevo asunto. Preguntar: "¿Deseas cambiar a `<slug>` ahora? (`/corporativo-legal-mexico:matter-workspace switch <slug>`)"

### `list`

Enumerar `matters/*/matter.md`. Leer el front-matter o las primeras líneas de cada archivo para extraer el estado. Imprimir una tabla:

| Slug | Cliente | Tipo de asunto | Estado | Apertura | Activo |
|---|---|---|---|---|---|

Marcar el asunto activo con `*`. Incluir `_archived/*` bajo un encabezado separado "Archivados" si existen.

### `switch <slug>`

1. Confirmar que `matters/<slug>/matter.md` exista. Si no, ofrecer `/corporativo-legal-mexico:matter-workspace new <slug>`.
2. Editar la línea `Active matter:` en el CLAUDE.md a nivel de práctica a `Active matter: <slug>`.
3. Mostrar al usuario el resumen de matter.md para que confirme que está en el asunto correcto.

### `close <slug>`

1. Confirmar que `matters/<slug>/` exista.
2. Agregar una entrada "Cerrado" a `matters/<slug>/history.md` con la fecha de hoy.
3. Mover `matters/<slug>/` → `matters/_archived/<slug>/`.
4. Si el asunto cerrado era el asunto activo, establecer `Active matter:` en `none — practice-level context only`.

### `none`

Establecer `Active matter:` en el CLAUDE.md a nivel de práctica en `none — practice-level context only`. Confirmar con el usuario.

## Plantilla de `matter.md`

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin` en el CLAUDE.md a nivel de práctica]

# Asunto: [Cliente] — [descripción breve]

**Slug:** [slug]
**Apertura:** [AAAA-MM-DD]
**Estado:** active
**Confidencialidad:** [standard / heightened / clean-team]

---

## Partes

**Cliente:** [nombre]
**Contraparte:** [nombre(s)]

## Tipo de asunto

[F&A lado comprador | F&A lado vendedor | financiamiento | asunto del Consejo | reestructura corporativa | proyecto de integración | contrato de compraventa de acciones | otro — con justificación en una línea]

## Hechos clave

[2–5 oraciones. De qué trata este asunto. Quiénes son los interesados. Qué está en juego. Qué lo diferencia del playbook predeterminado.]

## Excepciones específicas del asunto

*Cualquier desviación del playbook a nivel de práctica que aplique a este asunto y solo a este asunto.*

- [ej., "Cláusula penal: el cliente requiere 20%, no el estándar de la casa del 10%."]
- [ej., "Tono: preservar la relación — la contraparte es un socio estratégico."]
- [ej., "Ley aplicable: debe ser legislación de la Ciudad de México, no legislación federal."]

## Asuntos relacionados

- [slug — una línea explicando la relación]

## Notas sobre confidencialidad

[Si heightened o clean-team, describir por qué. Quién puede ver los archivos del asunto. Si el contexto cross-matter es permisible aunque esté activado globalmente.]
```

## Inicialización de `history.md`

```markdown
# Historial: [Cliente] — [descripción breve]

Registro cronológico de eventos (solo agregar). Más reciente arriba.

---

## [AAAA-MM-DD] — Asunto abierto

Ingreso completado. Slug: `[slug]`. Estado: active.
[Cualquier contexto inicial que valga la pena preservar más allá de matter.md — ej., "Abierto en respuesta a borrador de contrato de compraventa de acciones recibido de [contraparte]."]
```

## Contexto cross-matter

El CLAUDE.md a nivel de práctica tiene una bandera `Cross-matter context:`. Cuando está en `off` (predeterminado), un skill trabajando en el asunto A **nunca lee** archivos en `matters/B/` para cualquier otro `B`. Punto. Esta es la garantía de confidencialidad que ese ajuste existe para brindar.

Cuando está en `on`, un skill puede leer archivos entre carpetas de asuntos solo cuando el usuario lo pide explícitamente (ej., "compara nuestra posición sobre cláusulas penales en los últimos cinco asuntos de proveedores"). Incluso cuando está en `on`, el predeterminado es cargar solo el asunto activo a menos que el usuario pida una vista cross-matter.

## Lo que este skill no hace

- **Ejecutar una verificación de conflictos de interés.** Los conflictos son responsabilidad del abogado/despacho; el ingreso captura lo que el usuario declara.
- **Hacer cumplir la retención.** Cerrar archiva un asunto; no elimina. La política de retención está fuera de alcance.
- **Enrutar productos automáticamente.** El skill sustantivo decide dónde escribir; este skill le indica *cuál carpeta* está activa, no qué poner en ella.
- **Decidir si el cross-matter es apropiado.** Lee la bandera y obedece.
