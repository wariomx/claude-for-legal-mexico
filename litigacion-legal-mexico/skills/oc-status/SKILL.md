---
name: oc-status
description: Generar borradores semanales de correo de solicitud de estatus al despacho externo a lo largo del portafolio activo — markdown por asunto, más borradores de Gmail cuando el MCP esté disponible. Usar cuando el usuario pida solicitudes de estatus a abogados externos, seguimiento semanal al despacho externo, o quiera borradores de correo por asunto desde el registro del portafolio.
argument-hint: "[--all | --slug=foo | --no-gmail]"
---

# /oc-status

Para ejecutar semanalmente, establecer un recordatorio recurrente para invocar `/litigacion-legal-mexico:oc-status`. La programación automatizada requiere una integración de tareas programadas, que no viene incluida.

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`, filtrar según reglas por defecto (o según banderas).
2. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → estilo de directiva a despacho externo, valores por defecto del firmante, postura de presupuesto.
3. Seguir el flujo de trabajo y la referencia que se describen abajo.
4. Para cada asunto en alcance: leer `matter.md` + `history.md`, redactar correo por asunto.
5. Escribir markdown en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/oc-status/[AAAA-MM-DD]/[slug].md`.
6. Si el MCP de Gmail está autenticado: crear borradores de Gmail. Si no: solo markdown, anotar en resumen.
7. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/oc-status/[AAAA-MM-DD]/_summary.md` — qué se ejecutó, qué se omitió y por qué.

---

# Estatus con despacho externo

## Propósito

Escribir el mismo correo de solicitud de estatus al despacho externo cada semana para 5–15 asuntos es una carga cognitiva mecánica. El contenido es consistente por asunto (estatus, decisiones pendientes, verificación de presupuesto). La audiencia es consistente (socio líder del despacho). El tono es consistente (según el estilo de directiva al despacho externo de la casa). Una tarea programada redacta todos; el abogado revisa y envía.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — la fuente de filtrado y campos
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — contexto del asunto (postura actual, preguntas abiertas)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` — eventos recientes para informar qué preguntar
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → estilo de directiva a despacho externo, nombre/correo del firmante, postura de presupuesto

## Filtrado — ¿cuáles asuntos?

Filtro por defecto:

- `status != cerrado`
- `outside_counsel.firm != null` Y `outside_counsel.lead != null`
- Cualquiera: última actualización hace más de 10 días (tiempo para que algo haya pasado) O tiene un `next_deadline` dentro de 21 días

Omitir asuntos que acaban de tener una actualización de estatus en los últimos 10 días (no hay necesidad de volver a contactar) y asuntos donde `outside_counsel.email` es null (se necesitan direcciones de correo para el borrador de Gmail; aún así producir markdown).

Banderas:
- `--all` → redactar para cada asunto activo sin importar la recencia
- `--slug=[slug]` → redactar solo para un asunto (solicitud ad-hoc)
- `--no-gmail` → omitir creación de borradores de Gmail aun si el MCP está disponible

## Borrador de correo por asunto

Cada correo tiene el mismo esqueleto; el contenido es específico del asunto.

**Asunto:** según convención de la casa (de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` estilo de directiva a despacho externo; alternativa: `[Asunto: [nombre del asunto]] — Actualización semanal de estatus`)

**Cuerpo esqueleto:**

```
[nombre del socio líder],

[Una oración de apertura — natural, que coincida con el tono de la casa.]

Te escribo para dar seguimiento a [nombre del asunto]. Algunos puntos:

1. **Estatus desde [fecha de la última actualización capturada en history.md]** — ¿qué ha avanzado, qué está pendiente? ¿Algún escrito presentado, audiencia, correspondencia o llamada desde nuestra última comunicación?

2. **Plazos próximos** — tengo registrado [next_deadline del log + cualquier plazo en matter.md]. Confirma el plan de cobertura y cualquier fecha que debamos agregar.

3. **Decisiones pendientes** — [extraer preguntas abiertas de matter.md que requieran opinión del despacho externo; si no hay, omitir este punto y renumerar]

4. **Presupuesto** — [mensual / trimestral / a solicitud según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` postura de presupuesto]. ¿Dónde estamos contra [autorización de presupuesto de matter.md]? ¿Alguna variación que señalar?

[Si es material y relevante: 5. Solicitud específica — ej., "Por favor envíame el último borrador del escrito de contestación antes del [fecha]" — extraída de preguntas abiertas de matter.md.]

[Despedida — nombre, cargo, contacto. Del valor por defecto del firmante para directivas al despacho externo en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.]
```

Adaptar tono según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` estilo de directiva a despacho externo — algunos despachos son formales ("estimado licenciado"); otros usan primer nombre y viñetas. Coincidir.

## Resultados

### Borradores en markdown

Escribir en: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/oc-status/[AAAA-MM-DD]/[slug].md`

Cada archivo es un correo, formateado como:

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según config del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

# [Nombre del asunto] — Solicitud de estatus al despacho externo — [AAAA-MM-DD]

**Para:** [outside_counsel.email del log] ([outside_counsel.lead], [outside_counsel.firm])
**De:** [nombre / correo del firmante de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`]
**Asunto:** [línea de asunto]

> El encabezado de confidencialidad arriba aplica a este registro interno. El cuerpo del correo saliente abajo va al despacho externo en un asunto en el que están retenidos, lo cual es en sí una comunicación privilegiada — aplicar la marca de privilegio de la casa (`~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` convenciones de privilegio) en la parte superior del correo enviado, típicamente `Confidencial — Comunicación Protegida por Secreto Profesional`, no este encabezado de confidencialidad interno.

---

[cuerpo según esqueleto]
```

### Filtro de envío (nota de cierre en cada borrador)

Agregar lo siguiente a cada borrador en markdown, inmediatamente debajo del cuerpo y arriba de los metadatos de ejecución — retirar antes de enviar:

> Este es un borrador de correo de estatus para revisión del abogado antes de enviarlo al despacho externo. Verificar que no haya contenido privilegiado que no pretendías compartir fuera del círculo del encargo, exactitud de hechos, tono y postura de presupuesto. No enviar sin revisar — incluso seguimientos semanales rutinarios pueden exponer teoría, estrategia o concesiones que el remitente no pretendía poner por escrito.

### Borradores de Gmail (si el MCP está disponible)

Si el MCP de creación de borradores de Gmail está autenticado:

- Crear un borrador en el Gmail del usuario por asunto con `to`, `from`, `subject`, `body` poblados
- El borrador queda en la carpeta Borradores; el usuario revisa y envía el lunes por la mañana
- Si el MCP de Gmail NO está disponible o falla: recurrir a solo markdown e informar al usuario

### Resumen de la ejecución

Después de procesar todos los asuntos, escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/oc-status/[AAAA-MM-DD]/_summary.md`:

```markdown
# Ejecución de estatus con despacho externo — [AAAA-MM-DD]

**Asuntos procesados:** [N]
**Borradores creados:** [N]
**Borradores de Gmail:** [creados / omitidos — razón]

## Borradores generados para

| Asunto | Líder del despacho | Última actualización | Razón de inclusión |
|---|---|---|---|
| [slug] | [líder] | [fecha] | [obsoleto / plazo próximo / --all / --slug] |

## Omitidos

| Asunto | Razón |
|---|---|
| [slug] | actualización reciente (última vez tocado [fecha]) |
| [slug] | sin correo del despacho en el log — actualizar con `/litigacion-legal-mexico:matter-update [slug]` |

## Anomalías

- Asuntos sin despacho externo asignado: [lista — si alguno es de riesgo alto/crítico, señalado]
- Asuntos con despacho externo pero sin correo en el log: [lista]
```

## Programación

Este skill está diseñado para ejecutarse semanalmente. La programación automatizada requiere una integración de tareas programadas que no viene incluida con el plugin. Para ejecutar semanalmente, establecer un recordatorio recurrente para invocar `/litigacion-legal-mexico:oc-status` — ej., lunes por la mañana en tu calendario.

Ad-hoc: `/litigacion-legal-mexico:oc-status` en cualquier momento. `/litigacion-legal-mexico:oc-status --slug=foo` para un solo asunto.

## Lo que este skill no hace

- **Enviar los correos.** Solo borradores. El abogado revisa y envía.
- **Generar contenido que no tiene.** Si `matter.md` es escaso, el correo es corto y hace preguntas de estatus amplias. El skill no inventa preguntas específicas de la nada.
- **Reintentar fallas.** Si la creación de borradores de Gmail falla a mitad de ejecución, el skill registra la falla y continúa con markdown. El usuario puede reintentar después de corregir la autenticación.
- **Reescribir history.md.** Lo lee para contexto; no lo modifica. (Si la respuesta del despacho externo revela nuevos eventos, usar `/litigacion-legal-mexico:matter-update [slug]` para registrarlos.)
- **Aplicar una plantilla mínima obligatoria.** Si el tono de la casa es "una línea, primer nombre, listo", el borrador honra eso y omite la estructura de viñetas. Coincidir con `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.
