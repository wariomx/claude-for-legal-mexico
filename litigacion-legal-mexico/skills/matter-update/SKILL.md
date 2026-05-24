---
name: matter-update
description: >
  Agregar un evento fechado al historial de un asunto y actualizar la fila del log
  — captura nuevos desarrollos, cambios de estatus, re-evaluaciones de riesgo,
  modificaciones de plazos y cambios de autoridad de transaccion. Usar cuando el
  usuario quiere registrar una actualizacion de un asunto, anotar un desarrollo, o
  registrar un cambio de estatus contra el portafolio.
argument-hint: "[slug] [breve descripcion del evento]"
---

# /matter-update

1. Seguir el flujo de trabajo y la referencia que se describen abajo.
2. Confirmar que el slug existe en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/` y `_log.yaml`.
3. Solicitar tipo de evento, fecha (por defecto hoy), resumen y cualquier actualizacion de campo del log (cambio de riesgo, cambio de estatus, modificacion de plazo, reclasificacion de materialidad).
4. Agregar entrada fechada a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`.
5. Actualizar `_log.yaml` — establecer `last_updated` a hoy, aplicar cualquier actualizacion de campo.
6. Confirmar.

---

# Actualizacion del asunto

## Proposito

El portafolio solo es util si se mantiene al dia. Este skill hace que registrar una actualizacion sea barato — dos minutos de captura estructurada, sin desvios de forma libre.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — encontrar la fila
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` — destino de la adicion
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — referencia (no reescribir)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — calibracion de riesgo (si se re-evalua riesgo)

**Filtro de conflictos — infranqueable.** Antes de registrar una actualizacion, verificar `_log.yaml` para el slug del asunto. Si el asunto no esta en `_log.yaml`, rechazar y redirigir:

> "No encuentro [slug del asunto] en el registro de asuntos. Ejecuta `/litigacion-legal-mexico:matter-intake` primero para que la verificacion de conflictos se ejecute y el espacio de trabajo del asunto exista. No voy a agregar historial a un asunto no administrado — la verificacion de conflictos es el filtro, y no hay `history.md` al cual agregar hasta que el asunto sea ingresado."

## Entrada

Slug (requerido). Si no se proporciona, preguntar — con una lista breve de asuntos actualizados recientemente para elegir.

## La actualizacion

### 1. Tipo de evento

Ofrecer categorias:

- **Procesal** — demanda/contestacion presentada, auto dictado, audiencia celebrada, plazo fijado
- **Probatorio** — ofrecimiento/admision/desahogo de pruebas, inspeccion judicial, pericial rendida, requerimiento de exhibicion
- **Sustantivo** — hechos nuevos, documento clave identificado, resolucion sobre el fondo
- **Estrategia** — cambio de postura, oferta de convenio hecha/recibida, actualizacion de autoridad
- **Re-evaluacion de riesgo** — severidad o probabilidad cambio
- **Partes interesadas** — nueva persona involucrada, cambio de despacho externo
- **Administrativo** — carta compromiso ejecutada, presupuesto ajustado, retencion documental refrescada
- **Amparo** — amparo promovido, suspension concedida/negada, sentencia de amparo

O forma libre si ninguna aplica.

### 2. Fecha

Por defecto hoy. Aceptar una fecha diferente (ej., capturando un evento de la semana pasada).

### 3. Resumen

Un parrafo narrativo. Que paso, que significa, cualquier implicacion inmediata.

### 4. Cambios de campos del log

Recorrer los campos potencialmente afectados:

- `status:` — ha cambiado la etapa (ej., instruccion → juicio)?
- `stage:` — actualizacion de subetapa
- `risk:` — se requiere re-evaluacion?
- `materiality:` — algun cambio (hechos nuevos podrian detonar provision o revelacion)?
- `exposure_range:` — revisar si hay nueva informacion
- `next_deadline:` — nueva fecha proxima, si aplica
- `outside_counsel:` — cambio?
- `internal_owners:` — alguien nuevo o removido?
- `legal_hold:` — refrescada, expandida, liberada?

Solo preguntar por campos probablemente afectados por el tipo de evento. Actualizaciones procesales generalmente tocan solo `stage` y `next_deadline`; una oferta de convenio podria tocar `materiality`, `exposure_range`, `status`.

### 4pre. Filtro de aceptacion de convenio

Si la actualizacion de Estrategia es una **aceptacion de convenio** (la empresa esta aceptando una oferta de convenio, ejecutando un convenio judicial o extrajudicial, o autorizando la aceptacion en principio — no simplemente registrando una oferta hecha o recibida): Leer `## Quien usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Aceptar un convenio tiene consecuencias juridicas — resuelve pretensiones, tipicamente requiere un desistimiento o una liberacion de responsabilidad, y puede afectar seguros, impuestos y asuntos relacionados. Has revisado esto con un abogado titulado? Si si, continuar. Si no, aqui hay un resumen para llevarle:
>
> [Generar un resumen de 1 pagina: el asunto, terminos propuestos del convenio (monto, estructura, alcance de la liberacion, confidencialidad, no denigracion), exposicion en juego, estatus de la escalera de autoridad (ver `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` autoridad de transaccion), que podria salir mal, que preguntar al abogado antes de aceptar.]
>
> Si necesitas encontrar un abogado titulado y autorizado en tu jurisdiccion: la Barra Mexicana Colegio de Abogados, el Ilustre y Nacional Colegio de Abogados, el colegio de abogados de tu entidad federativa, o la verificacion de cedula profesional en el Registro Unico de Profesionistas (RUP) de la SEP son los puntos de partida mas rapidos.

No registrar la aceptacion ni voltear materialidad sobre la base de aceptacion sin un si explicito. Registrar ofertas o contraofertas no requiere el filtro — la aceptacion si.

### 4a. Disparador de materialidad — pregunta explicita

Ciertos tipos de evento fuerzan una re-verificacion de materialidad. Cuando el tipo de evento esta en esta lista, **siempre preguntar** — no dejar que el usuario avance sin una respuesta explicita:

| Tipo de evento | Pregunta disparadora de materialidad |
|---|---|
| Sustantivo (hechos nuevos, documento clave, resolucion sobre el fondo) | "Este evento es sustantivo. Empuja la `materialidad`? Actual: `[actual]`. Opciones: `provisionado / revelado / monitoreado / ninguno`. Cambiar?" |
| Estrategia (cambio de postura, oferta de convenio hecha o recibida) | "Actividad de convenio frecuentemente detona reclasificacion de materialidad. Actual: `[actual]`. Si la oferta, contraoferta o aceptacion mueve la exposicion o cambia de controvertido a probable-y-cuantificable, reclasificar." |
| Re-evaluacion de riesgo (severidad o probabilidad cambio) | "El riesgo se movio. La materialidad debe acompanar. Actual: `[actual]`. Reclasificar?" |
| Desarrollo regulatorio / cumplimiento forzoso | "Accion regulatoria (requerimiento de informacion de COFECE, oficio de investigacion de CNBV, resolucion de INAI, requerimiento de PROFECO, procedimiento de IMPI, acta de inspeccion de STPS) generalmente detona analisis de revelacion. Actual: `[actual]`. Cambiar?" |

Respuestas aceptables incluyen `sin cambio` — pero `sin cambio` debe ser explicito, no implicado por silencio. Capturar en la entrada del historial:

```markdown
**Verificacion de materialidad:** [sin cambio / cambio de X a Y]
**Razonamiento:** [una oracion]
```

Si la materialidad se mueve a `provisionado` o `revelado`, y el asunto no llevaba previamente provision o revelacion, senalar el evento como requiriendo notificacion a finanzas / comite de auditoria segun los umbrales de materialidad de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.

### 5. Pregunta de documento semilla (opcional)

Si la actualizacion referencia un documento (auto, escrito, correspondencia), preguntar si hay una ruta para vincular. Sin insistir.

## Escritura

### Agregar a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`

El mas reciente arriba, directamente bajo el `---` que sigue al encabezado.

```markdown
## [AAAA-MM-DD] — [Tipo de evento]: [titulo breve]

[Parrafo de resumen.]

**Campos modificados:**
- [campo]: [anterior → nuevo]
- [campo]: [anterior → nuevo]

**Documento relacionado:** [ruta, si se proporciono]
```

Si no se modificaron campos, omitir el bloque "Campos modificados".

### Actualizar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`

- Aplicar cualquier cambio de campo.
- Establecer `last_updated: [hoy]` (o la fecha del evento si el usuario la modifico — el log registra cuando el registro fue tocado por ultima vez).

## Confirmar

Mostrar al usuario la entrada del historial y el diff del yaml antes de escribir:

> Esto es lo que agregare y actualizare. Listo para registrar?

## Lo que este skill no hace

- Editar entradas pasadas del historial. Las correcciones son nuevas entradas que referencian y corrigen las anteriores.
- Cambiar silenciosamente el log. Cada cambio de campo se muestra al usuario antes de escribir.
- Decidir si un nuevo desarrollo amerita provision/revelacion. Expone la pregunta ("esto podria empujar la materialidad — quieres reclasificar?"), el usuario responde.
