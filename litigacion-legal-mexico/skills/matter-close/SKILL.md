---
name: matter-close
description: >
  Cerrar un asunto — capturar resultado, exposicion final y lecciones, luego
  archivarlo fuera del portafolio activo sin borrar el registro. Usar cuando el
  usuario quiere cerrar un asunto, dice "[asunto] termino", o necesita registrar
  un convenio, desistimiento, sentencia, sobreseimiento o acumulacion.
argument-hint: "[slug]"
---

# /matter-close

1. Seguir el flujo de trabajo y la referencia que se describen abajo.
2. Confirmar slug y estatus actual.
3. Capturar resultado: tipo de resolucion (convenio, desistimiento, sentencia-favorable, sentencia-desfavorable, sobreseimiento, acumulado, otro), fecha, exposicion/costo final, lecciones.
4. Actualizar `_log.yaml`: `status: cerrado`, agregar campos `closed: AAAA-MM-DD` y `outcome:`.
5. Agregar entrada final a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`.
6. El asunto permanece en `_log.yaml` y en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/` — no se borra. `/litigacion-legal-mexico:portfolio-status` lo filtra de los consolidados activos.

---

# Cierre del asunto

## Proposito

Los asuntos terminan. El resultado es el dato mas valioso que genera el portafolio — calibra el marco de riesgo para asuntos futuros. Cerrar un asunto captura el resultado de forma estructurada para que el registro sea util, no solo archivado.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — encontrar la fila
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — referencia (contexto del ingreso)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` — destino de la adicion

**Filtro de conflictos — infranqueable.** Antes de cerrar, verificar `_log.yaml` para el slug del asunto. Si el asunto no esta en `_log.yaml`, rechazar y redirigir:

> "No encuentro [slug del asunto] en el registro de asuntos. No hay nada que cerrar — o el slug esta mal o el asunto nunca fue ingresado a traves de `/litigacion-legal-mexico:matter-intake`. Verificar el slug primero; si genuinamente nunca fue ingresado, no hay fila que actualizar ni estructura de archivos que cerrar."

## Entrada

Slug (requerido).

## El cierre

### 1. Tipo de resolucion

- `convenio` — con contraparte, monto, terminos estructurales, clausula penal si aplica
- `desistimiento` — por el actor, con o sin consentimiento del demandado, circunstancias
- `sentencia-favorable` — en que etapa, exposicion a apelacion o amparo
- `sentencia-desfavorable` — en que etapa, estatus de apelacion o amparo, exposicion cristalizada
- `sobreseimiento` — por que causa (falta de interes juridico, litispendencia, conexidad, caducidad, incompetencia, otra), mecanismo procesal
- `acumulado` — fusionado con otro asunto (proporcionar slug del asunto padre)
- `otro` — con explicacion

### 2. Fecha de resolucion

La fecha en que el asunto efectivamente termino (convenio firmado, sentencia ejecutoriada, auto de sobreseimiento dictado, desistimiento presentado).

### 3. Exposicion final

- Costo real para la empresa (monto del convenio + honorarios + costo cautelar/estructural)
- vs. rango de exposicion inicial al ingreso (acertamos?)
- Precision de la provision (si se provisiono): provisionado vs. real

### 4. Lecciones

Dos o tres oraciones. Que hicimos bien? Que calculamos mal? Algo que el ingreso debio haber senalado antes?

Esta es la parte que futuros abogados releeran. Ser honesto. "Calculamos mal la probabilidad — el despacho de la contraparte fue mas agresivo de lo esperado" vale mas que "se resolvio favorablemente."

### 5. Pregunta de documento semilla

Convenio judicial/extrajudicial, sentencia ejecutoriada, auto de sobreseimiento — ruta si esta disponible. No es obligatorio.

## Escritura

**Antes de cerrar el asunto (el acto con consecuencias — el asunto se archiva y el seguimiento activo termina):** Leer `## Quien usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Cerrar un asunto tiene consecuencias juridicas — termina el seguimiento activo, puede afectar cualquier retencion documental asociada (ejecutar `/litigacion-legal-mexico:legal-hold --release` por separado si es apropiado), y establece el registro final en el que la empresa confia. Has revisado esto con un abogado titulado? Si si, continuar. Si no, aqui hay un resumen para llevarle:
>
> [Generar un resumen de 1 pagina: el asunto, tipo de resolucion y terminos, exposicion final vs. inicial, precision de la provision, asuntos relacionados o apelaciones/amparos aun vivos, que podria salir mal con un cierre prematuro, que preguntar al abogado.]
>
> Si necesitas encontrar un abogado titulado y autorizado en tu jurisdiccion: la Barra Mexicana Colegio de Abogados, el Ilustre y Nacional Colegio de Abogados, el colegio de abogados de tu entidad federativa, o la verificacion de cedula profesional en el Registro Unico de Profesionistas (RUP) de la SEP son los puntos de partida mas rapidos.

No escribir los campos de cierre ni agregar la entrada de cierre sin un si explicito.

### Actualizar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`

```yaml
status: cerrado
closed: [AAAA-MM-DD]
outcome: [tipo-de-resolucion]
final_cost: [monto]
last_updated: [hoy]   # el cierre es el ultimo toque; registrarlo
```

Retener todos los campos existentes. No borrar la fila.

### Agregar entrada final a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`

```markdown
## [AAAA-MM-DD] — Asunto cerrado: [tipo-de-resolucion]

**Resolucion:** [narrativa — que paso, en que terminos]
**Costo final:** [monto + terminos estructurales si los hay]
**vs. exposicion inicial:** [comparar con el rango del ingreso en matter.md]
**Precision de la provision:** [si aplica]

**Lecciones:**
[2-3 oraciones — retrospectiva honesta]

**Documento relacionado:** [convenio / sentencia ejecutoriada / auto de sobreseimiento / etc., si se proporciono]
```

### Tocar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md`

Agregar un bloque de cierre al final (no modificar secciones anteriores — son el ingreso historico):

```markdown
---

## Cerrado [AAAA-MM-DD]

[Resumen de la resolucion en un parrafo. Apuntador a la entrada final del historial para detalle.]
```

## Confirmar

Mostrar al usuario la entrada completa de cierre y los cambios del yaml antes de escribir.

## Lo que este skill no hace

- Borrar asuntos. Los asuntos cerrados permanecen en `_log.yaml` y en disco — son el conjunto de entrenamiento para el criterio del portafolio.
- Re-abrir. Si un asunto cerrado regresa (apelacion, amparo, litigio relacionado), abrir un nuevo asunto que referencie al cerrado en `matter.md`.
- Resumir lecciones que el usuario no dijo. Si el usuario omite la seccion de lecciones, dejarla vacia en vez de inventar.
