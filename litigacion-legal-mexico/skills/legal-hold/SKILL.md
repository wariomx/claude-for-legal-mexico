---
name: legal-hold
description: Emitir, refrescar, liberar o reportar retenciones documentales — redacta el aviso de retención como .docx, actualiza campos de legal_hold en _log.yaml y calendariza el próximo refrescamiento. Usar cuando el usuario diga "emite una retención", "refresca la retención", "libera la retención" o pida un reporte de estado de retenciones a nivel portafolio.
argument-hint: "[slug] [--issue | --refresh | --release | --status]"
---

# /legal-hold

1. Si `--status` (sin slug): leer `_log.yaml`, producir reporte de retenciones a nivel portafolio.
2. De lo contrario: cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` + fila del registro.
3. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → marcas de confidencialidad, apuntador de plantilla de retención, normas de escalamiento.
4. Seguir el flujo de trabajo y la referencia de abajo.
5. Enrutar por bandera:
   - `--issue`: capturar alcance, custodios, rango de fechas, sistemas. Redactar `legal-hold-v1.docx`. Actualizar campos de `legal_hold`. Agregar entrada al historial. Fijar `next_refresh` (por defecto +6 meses).
   - `--refresh`: capturar cambios de alcance/custodios. Redactar siguiente versión. Actualizar `last_refresh` + `next_refresh`. Señalar custodios que hayan dejado la empresa.
   - `--release`: capturar fecha de liberación, instrucción de retención. Redactar aviso de liberación. Fijar campo `released:`.
6. Confirmar antes de escribir. Mostrar al usuario el borrador del aviso y el diff del registro.

---

# Retención Documental

## Propósito

Una retención documental es el documento mecánico de más alto riesgo que el abogado interno redacta. El aviso en sí es plantilla. Los modos de falla son operacionales: emitida tarde, alcance demasiado estrecho, nunca refrescada, nunca liberada. Este skill maneja las cuatro fases: **emisión → refrescamiento → (liberación) → seguimiento**.

El portafolio ya señala retenciones faltantes; este skill las redacta.

## Marco de conservación documental en México

El deber de conservar documentos relevantes para una controversia en México se articula de forma diferente al common law. No existe una doctrina equivalente al "litigation hold" estadounidense derivada de jurisprudencia (como la línea de casos Zubulake). En su lugar, las obligaciones de conservación provienen de fuentes legislativas:

- **Código de Comercio (Arts. 46-49):** los comerciantes están obligados a conservar la correspondencia que tenga relación con el giro del comerciante y los libros, registros y documentos de su negocio durante un mínimo de 10 años. `[model knowledge — verify]`
- **Obligaciones fiscales (CFF / SAT):** la contabilidad y documentación soporte debe conservarse durante 5 años contados a partir de la fecha en que se presentaron o debieron presentar las declaraciones (Art. 30 CFF). `[model knowledge — verify]`
- **Ley Federal del Trabajo:** los registros laborales (contratos individuales, recibos de nómina, constancias de capacitación, registros de IMSS/INFONAVIT) deben conservarse mientras dure la relación laboral y por el plazo de prescripción de acciones laborales (1 año general, Art. 516 LFT). `[model knowledge — verify]`
- **Activación formal del deber procesal:** la obligación procesal de conservar documentos se activa formalmente con la presentación de la demanda y el emplazamiento. Sin embargo, la destrucción de documentos después de tener conocimiento de un procedimiento pendiente o previsible puede generar inferencias adversas y responsabilidad.
- **Consecuencias de la destrucción:** la destrucción de documentos relevantes no tiene un régimen sancionatorio equivalente al spoliation del common law con inferencias adversas automáticas. Sin embargo, el juez puede valorar la conducta procesal de las partes (Art. 1205 Código de Comercio para materia mercantil), y la falta de exhibición de documentos requeridos puede generar la presunción de que su contenido era desfavorable para quien los destruyó. `[model knowledge — verify]`

Los plazos, alcance y consecuencias de destrucción citados en el borrador son una lectura inicial para el foro identificado en el asunto — confirmar con el abogado antes de emitir, refrescar o liberar.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — fila del registro (campos de legal_hold + estatus)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — contexto del asunto (contraparte, hechos, custodios clave de internal_owners)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — estilo de casa para apuntador de plantilla de retención, marca de confidencialidad, normas de escalamiento

**Compuerta de conflictos — no se puede eludir.** Antes de emitir, refrescar o liberar una retención, verificar `_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rechazar y enrutar:

> "No encuentro [slug del asunto] en el registro de asuntos. Ejecuta `/litigacion-legal-mexico:matter-intake` primero para que se corra la verificación de conflictos y se configure el espacio de trabajo del asunto. No emitiré, refrescaré ni liberaré una retención documental sobre un asunto que no ha pasado por intake — la verificación de conflictos es la compuerta, y una retención emitida sobre un asunto no administrado no tiene fila en `_log.yaml` contra la cual rastrear `last_refresh` / `next_refresh` / `released`."

No proceder en un asunto sin intake. El intake es lo que ejecuta conflictos y escribe la fila de `_log.yaml` contra la cual operan las banderas `--refresh` / `--release` / `--status`.

## Modos

El comando toma una bandera: `--issue | --refresh | --release | --status`. Por defecto (sin bandera) → preguntar.

### `--issue` — primera emisión

Requerida cuando `legal_hold.issued == false` y el asunto está activo o razonablemente anticipado.

**Antes de emitir la retención a los custodios (el acto con consecuencias):** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Emitir una retención documental tiene consecuencias legales — el alcance, la lista de custodios y el momento crean el registro de conservación contra el cual se juzgará a la empresa si se argumenta destrucción de pruebas después. ¿Lo has revisado con un abogado? Si sí, procede. Si no, aquí hay un resumen para presentarle:
>
> [Generar un resumen de 1 página: el asunto y el detonante, el alcance y custodios propuestos, las obligaciones de conservación según el Código de Comercio y legislación aplicable investigadas, la exposición conocida por destrucción, qué podría salir mal (demasiado amplio / demasiado estrecho), qué preguntar al abogado.]
>
> Si necesitas encontrar un abogado titulado y autorizado en tu jurisdicción: la Barra Mexicana Colegio de Abogados, ANADE, tu colegio de abogados estatal o tu barra local son el punto de partida más rápido para una referencia.

No enviar el aviso sin un sí explícito. Redactar y definir alcance no requieren la compuerta — la emisión sí.

**Investigar la obligación de conservación aplicable antes de emitir.** Identificar la jurisdicción y la fuente de la obligación de conservación (Código de Comercio, CFF, LFT, normativa sectorial, contractual). Confirmar el estándar de activación actualmente vigente (cuándo se activa la obligación), el estándar de alcance (qué debe conservarse) y la exposición por destrucción (consecuencias procesales en el foro). Citar fuentes primarias. Notar que la ley mercantil, laboral, fiscal y administrativa pueden diferir materialmente en plazos y consecuencias — señalar el foro del que se depende. Si hay incertidumbre, decirlo y obtener visto bueno del despacho externo antes de emitir.

> **Entregable externo:** el aviso de abajo se envía a los custodios de información. NO incluir un encabezado de `CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL` en el aviso saliente; usar la marca de comunicación abogado-cliente en la plantilla. Confirmar la marca correcta para tu jurisdicción y asunto.

**Entradas:**
1. **Alcance** — categorías de documentos, datos, comunicaciones. Iniciar específico: contratos con la contraparte, todas las comunicaciones que referencien [proyecto/tema], registros financieros relacionados, entradas de calendario. `[VERIFICAR SME — alcance demasiado amplio = carga operacional; demasiado estrecho = riesgo de destrucción de pruebas]`
2. **Custodios de información** — personas nombradas que probablemente tengan material relevante. Obtener sugerencias de matter.md internal_owners y de roles comunes (líder de negocio, RH si es laboral, CISO si es datos). `[VERIFICAR SME — la lista de custodios es la diferencia entre conservación defendible y un argumento de laguna]`
3. **Rango de fechas** — desde cuándo conservar (generalmente: hecho detonante o antes), hasta el presente + en curso.
4. **Sistemas** — correo electrónico, Slack/Teams, repositorios en la nube, dispositivos (incluyendo BYOD si aplica), Jira/Asana, CRM, sistemas legados.
5. **Urgencia** — si ya se recibió el emplazamiento o demanda con amenaza de juicio, esto sale hoy.
6. **Fecha efectiva** — fecha de la retención.

**Redactar el aviso** a cada custodio de información, usando la plantilla de la casa en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` si hay una configurada; de lo contrario, la plantilla por defecto de abajo.

**Plantilla de aviso de retención por defecto:**

```
[CONFIDENCIAL — COMUNICACIÓN ABOGADO-CLIENTE]

FECHA: [fecha efectiva]
PARA: [nombre del custodio de información]
DE: [firmante — según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` por defecto]
ASUNTO: AVISO DE RETENCIÓN DOCUMENTAL — [nombre corto del asunto]

Usted recibe este aviso porque [empresa] ha determinado que [descripción
de una oración de la controversia / investigación, evitando detalle
perjudicial]. La empresa tiene la obligación legal de conservar documentos
y comunicaciones potencialmente relevantes para este asunto, conforme a lo
establecido en el Código de Comercio (Arts. 46-49) y la legislación
aplicable.

CON EFECTOS INMEDIATOS, usted debe conservar:

1. Todos los documentos, correos electrónicos, mensajes de texto,
   mensajes de Slack/Teams y otras comunicaciones relacionados con
   [alcance punto 1].
2. [alcance punto 2]
3. [alcance punto 3]
...

Esta obligación de conservación aplica a:
- Correo electrónico (incluyendo enviados, archivados, eliminados)
- Plataformas de mensajería (Slack/Teams/WhatsApp)
- Repositorios compartidos y almacenamiento en la nube
- Dispositivos personales usados para actividades de la empresa (BYOD)
- Documentos en papel
- Mensajes de voz
- Entradas de calendario y notas de reuniones

NO:
- Eliminar, modificar, destruir o desechar ningún material potencialmente
  relevante
- Ejecutar eliminación automática o "Inbox Zero" de correo o mensajería
- Alterar metadatos de archivos o comunicaciones

Coordine con [contacto jurídico] antes de compartir este aviso con
reportes directos o con el área de TI.

Dirija sus preguntas sobre este aviso o sus obligaciones de conservación
a [contacto jurídico]. Puede continuar discutiendo el tema de negocio
subyacente con colegas según sea necesario para su trabajo, pero no
discuta este aviso legal, la controversia ni la estrategia jurídica.

EN CASO DE DUDA sobre si algo está cubierto, ACTÚE A FAVOR DE CONSERVAR.

Por favor acuse recibo de este aviso mediante [respuesta / enlace /
formulario] dentro de tres días hábiles. Si tiene preguntas, contacte a
[correo del firmante].

Este aviso permanece en vigor hasta que reciba notificación escrita de su
liberación. Se le podrá solicitar que reafirme su cumplimiento en
intervalos periódicos.

[Bloque de firma del firmante]
```

**Compuerta de envío (nota de cierre en el borrador):** Agregar a la vista previa del aviso en chat — se elimina antes de que el aviso llegue a los custodios:

> Este es un borrador de aviso de retención documental para revisión del abogado, no un aviso listo para emitir. Emitir una retención activa obligaciones de conservación contra las cuales se juzgará a la empresa en cualquier argumento posterior de destrucción de pruebas, y el aviso mismo puede ser exhibido como prueba. Un abogado titulado revisa, aprueba y emite. No distribuir este borrador sin revisión.

**Escribe:**
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/legal-hold-v1.docx` vía el skill `docx`
- Agrega a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`:
  ```
  ## [YYYY-MM-DD] — Retención documental emitida

  Retención emitida a [N] custodios de información: [lista].
  Alcance: [resumen de una línea].
  Próximo refrescamiento: [YYYY-MM-DD (por defecto fecha de emisión + 6 meses)].
  ```
- Actualiza fila de `_log.yaml`:
  ```yaml
  legal_hold:
    issued: true
    issued_date: [YYYY-MM-DD]
    scope: "[resumen de una línea]"
    custodians: [lista]
    last_refresh: [YYYY-MM-DD]   # igual a issued_date en primera emisión
    next_refresh: [YYYY-MM-DD]   # por defecto: issued_date + 6 meses
    released: null
  ```

### `--refresh` — reafirmación periódica

Cadencia de refrescamiento: por defecto 6 meses; ajustable por asunto. Cuando `next_refresh < today` (o el usuario invoca manualmente), el skill redacta un aviso de refrescamiento.

**Entradas:**
1. Cualquier **cambio de alcance** desde el último refrescamiento (nuevos temas surgidos en el proceso, nuevos custodios, nuevos sistemas).
2. Cualquier **custodio a agregar o remover** (las bajas requieren manejo especial — ver abajo).
3. Lenguaje de reconfirmación.

**Plantilla de aviso de refrescamiento:** similar a la emisión; abre con "Esta es una reafirmación de la retención documental originalmente emitida el [fecha]." Lista el alcance actual (enmendado si es necesario). Solicita re-acuse de recibo.

**Custodios dados de baja:** si un custodio de información ha dejado la empresa desde el último refrescamiento, el skill señala esto como un punto de acción de conservación — los archivos y correo electrónico del empleado saliente necesitan ser preservados a nivel de TI, no solo vía aviso al individuo. Registra esto en history.md como una entrada separada que requiere acción.

**Escribe:**
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/legal-hold-v[N].docx` (siguiente número de versión)
- Entrada en `history.md`
- `_log.yaml`: actualiza campos `last_refresh` y `next_refresh`; modifica lista de `custodians` si cambió

### `--release` — cerrar la retención

Usualmente al cierre del asunto. Confirmar que el asunto realmente terminó (no en apelación, no en amparo, no hay probabilidad de reapertura, prescripción de acciones conexas vencida).

**Antes de liberar la retención (el acto con consecuencias — las obligaciones de conservación regresan a la retención normal):** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Liberar una retención documental tiene consecuencias legales — una vez liberada, los custodios de información pueden comenzar a eliminar material. Liberar en el momento equivocado crea exposición por destrucción de pruebas. ¿Lo has revisado con un abogado? Si sí, procede. Si no, aquí hay un resumen para presentarle:
>
> [Generar un resumen de 1 página: el estatus del asunto, por qué se propone liberar ahora, exposición por acciones conexas / apelación / amparo / prescripción, impacto en custodios, qué podría salir mal, qué preguntar al abogado.]
>
> Si necesitas encontrar un abogado titulado y autorizado en tu jurisdicción: la Barra Mexicana Colegio de Abogados, ANADE, tu colegio de abogados estatal o tu barra local son el punto de partida más rápido para una referencia.

No enviar el aviso de liberación sin un sí explícito.

**Entradas:**
1. Confirmación de autoridad de liberación (usualmente el firmante o el Director Jurídico).
2. Fecha de liberación.
3. Instrucción de retención — qué pasa con el material que estaba bajo retención? (¿Regresar a retención normal? ¿Continuar conservando por período definido? ¿Transferir a archivo?)

**Plantilla de aviso de liberación:** un párrafo, formal. "La retención documental emitida el [fecha] respecto del asunto [asunto] queda liberada con efectos a partir del [fecha]. Se reanuda la política de retención normal de la empresa."

**Escribe:**
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/legal-hold-release.docx`
- Entrada en `history.md`
- `_log.yaml`: fija `released: [YYYY-MM-DD]`

### `--status` — reporte a nivel portafolio

Leer `_log.yaml`. Producir un reporte:

```markdown
# Estado de Retenciones Documentales — [hoy]

## Retenciones activas

| Asunto | Emitida | Último refrescamiento | Próximo refrescamiento | Custodios | Estado |
|---|---|---|---|---|---|
| [slug] | [fecha] | [fecha] | [fecha] | [N] | [ok / ⚠️ refrescamiento pendiente / ❌ vencida] |

## ⚠️ Atención

- **Refrescamiento vencido:** [lista de slugs donde next_refresh < hoy]
- **Refrescamiento pendiente en 30 días:** [lista]
- **Asuntos activos sin retención emitida:** [lista — riesgo alto/crítico primero]
- **Asuntos cerrados con retención aún activa:** [lista — considerar liberación]

## Liberadas recientemente

[últimas 5 retenciones liberadas con fechas]
```

Esta es una invocación de comando separada (`/legal-hold --status` sin slug) O invocada por `/portfolio-status` como una sección en el rollup del portafolio.

## Integración con portfolio-status

El skill `portfolio-status` ya señala "Retención no emitida en litigio activo." Este skill es lo que resuelve esas señales. Vale la pena hacer referencia cruzada en el briefing cuando se abre un asunto: si `legal_hold.issued == false`, `/litigacion-legal-mexico:matter-intake` cierra ofreciendo ejecutar `/litigacion-legal-mexico:legal-hold --issue`.

## Lo que este skill NO hace

- **Hacer cumplir la conservación.** Emite el aviso; TI/custodios de información conservan. El skill señala cuando un custodio deja la empresa (para que TI conserve a nivel de sistema) pero no llega a los sistemas.
- **Tomar decisiones de alcance solo.** El skill propone alcance a partir del contexto del asunto; el usuario confirma. Alcance demasiado amplio = carga operacional. Alcance demasiado estrecho = riesgo de destrucción de pruebas. Criterio del usuario.
- **Auto-refrescar sin revisión.** Aun cuando `next_refresh` se cumpla, el usuario revisa cambios de alcance antes de que salga el aviso de refrescamiento.
- **Enviar el aviso.** Redacta .docx; el usuario envía por correo según la convención de la casa. (Integración futura: Gmail/O365 MCP podría enviar directamente después de revisión del usuario.)
