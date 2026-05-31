---
name: requerimiento-triage
description: >
  Triaje de un requerimiento judicial, citatorio, exhorto o requerimiento regulatorio recibido —
  clasificar, analizar alcance/carga/confidencialidad, cruzar con el portafolio, y producir un
  marco de objeciones, plan de cumplimiento y calendario de plazos procesales. Usar cuando el
  usuario diga "nos llegó un requerimiento", "nos notificaron", "recibimos un exhorto", o
  comparta un requerimiento judicial, citatorio, exhorto o requerimiento de autoridad regulatoria
  (COFECE, CNBV, INAI, IMPI, etc.) para evaluar.
argument-hint: "[ruta-al-requerimiento] [--slug=slug-personalizado]"
---

# /requerimiento-triage

1. Leer el requerimiento desde la ruta proporcionada.
2. Clasificar (requerimiento-judicial / citatorio / exhorto / requerimiento-regulatorio / orden-penal).
3. Si orden penal → parar, escalar por `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. De otro modo continuar.
4. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para cruce con portafolio. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → panorama, convenciones de confidencialidad, normas de escalamiento.
5. Seguir el flujo de trabajo y referencia abajo.
6. Extraer campos clave, analizar alcance/carga/confidencialidad, producir marco de objeciones + plan de cumplimiento + calendario de plazos.
7. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/triage.md`. Copiar o vincular el requerimiento a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/incoming.[ext]`.
8. Derivar: `/litigacion-legal-mexico:legal-hold --issue` si no hay retención en vigor; `/litigacion-legal-mexico:matter-intake` si la materialidad lo justifica; `/litigacion-legal-mexico:matter-briefing [slug]` si es requerimiento de parte en asunto existente.

---

# Triaje de Requerimiento

## Propósito

Los requerimientos judiciales, citatorios, exhortos y requerimientos regulatorios llegan con plazos procesales estrictos. Los modos de fallo: no cumplir el plazo (multas, medidas de apremio, desacato), entregar de más (revelar información confidencial o secreto profesional sin necesidad), entregar de menos (sanciones, cumplimiento forzoso), o no interponer los medios de defensa a tiempo. Este skill clasifica, analiza y produce un plan de cumplimiento con marco de objeciones.

## Contexto del sistema jurídico mexicano

México opera bajo un sistema de derecho civil codificado. No existe el concepto de _subpoena_ del derecho anglosajón. Los mecanismos equivalentes son:

- **Requerimiento judicial** — orden del juzgador para hacer, dejar de hacer o entregar algo (documentos, informes, bienes). Regulado por el código procesal aplicable (CFPC, Código de Comercio, CNPCF, Ley de Amparo).
- **Citatorio** — notificación judicial formal para comparecer o ser notificado personalmente. Regulado por las reglas de notificación del código procesal aplicable.
- **Exhorto** — solicitud de un tribunal a otro de distinta jurisdicción para que practique diligencias. Arts. 293-301 CFPC; Arts. 1071-1075 Código de Comercio.
- **Requerimiento regulatorio** — solicitud de información o documentación de una autoridad regulatoria (COFECE, CNBV, INAI, IMPI, SAT, PROFECO, STPS, etc.) en ejercicio de sus facultades de investigación o verificación.

## Supuesto de jurisdicción

La norma citada en el Paso 0 es la aplicable a este requerimiento en este foro. La práctica procesal varía materialmente: fuero federal vs. fuero local/estatal, materia (civil, mercantil, laboral, administrativa, amparo), reglas de notificación, plazos (días hábiles vs. naturales), y tipo de requerimiento. Todo resultado normativo aquí es un punto de partida heurístico — confirmar vigencia y la variante local antes de actuar.

## Contexto de postura procesal

Este skill es inherentemente defensivo — un requerimiento ha sido recibido y la postura es responder/objetar/cumplir. Leer `## Lado` en el perfil de práctica. Si el usuario es **actor**, recibir un requerimiento es normal (requerimientos de contraparte, de autoridades, etc.) pero el enfoque aquí siempre es "nos llegó un requerimiento, cómo respondemos." Si la materia tiene una postura diferente, solicitar al usuario que confirme antes de proceder.

## Cargar contexto

- El documento del requerimiento (el usuario proporciona la ruta o lo comparte en sesión)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — para búsqueda de asuntos relacionados y estado de retención legal
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → panorama (reguladores con los que tratamos), convenciones de confidencialidad, normas de escalamiento

## Flujo de trabajo

### Paso 0: Investigar la norma aplicable

**Antes de analizar este requerimiento, investigar la norma procesal aplicable al foro y la materia (CFPC, Código de Comercio, CNPCF, Ley de Amparo, Ley Federal de Procedimiento Contencioso Administrativo, ley orgánica del regulador, etc.) y el tipo de requerimiento. Identificar: plazos para cumplimiento o impugnación (días hábiles/naturales, cómputo desde la notificación), medios de impugnación (recurso de revocación, incidente, queja, amparo indirecto), consecuencias del incumplimiento (multa, medidas de apremio, desacato, uso de la fuerza pública), y quién carga con los costos. Citar con referencias puntuales de artículo, fracción, inciso. Verificar vigencia — las leyes procesales cambian.**

**Sin complemento silencioso.** Si una consulta de investigación a la herramienta de investigación jurídica configurada (SCJN IUS, Semanario Judicial, DOF, plataforma del despacho) devuelve pocos o ningún resultado para la norma del foro, variante o punto específico, reportar lo encontrado y detenerse. NO llenar el vacío con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece escasa para [norma / foro / variante]. Opciones: (1) ampliar la consulta de búsqueda, (2) probar otra herramienta de investigación, (3) buscar en web — los resultados se etiquetarán `[búsqueda web — verificar]` y deben verificarse contra fuente primaria antes de confiar, o (4) detenerse aquí. ¿Cuál prefiere?" El abogado decide si acepta fuentes de menor confianza; el skill no decide por él.

**Atribución de fuentes.** Etiquetar cada referencia normativa, tesis, jurisprudencia, ley y reglamento en el producto del triaje con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, `[IMPI]`, `[INAI]`, o el nombre de la herramienta MCP para citas recuperadas de un conector de investigación jurídica; `[búsqueda web — verificar]` para citas de búsqueda web; `[conocimiento del modelo — verificar]` para citas recordadas de datos de entrenamiento; `[proporcionado por usuario]` para citas que el usuario suministró. Las citas etiquetadas `verificar` tienen mayor riesgo de fabricación y deben verificarse primero. Nunca eliminar ni colapsar las etiquetas — son la señal más rápida del abogado sobre qué citas verificar antes de actuar.

### Paso 1: Clasificar

Los requerimientos vienen en tipos con reglas distintas; confirmar los detalles contra la norma investigada:

- **Requerimiento judicial (civil/mercantil)** — orden del juez para producir documentos, informes, o realizar algún acto procesal. Puede ser dentro de un juicio en el que somos parte o como tercero ajeno al juicio. Categorías de objeción: improcedencia, incompetencia, secreto profesional, información confidencial, carga desproporcionada.
- **Citatorio** — notificación judicial formal para comparecer o ser notificado personalmente. Verificar si cumple requisitos de forma (Art. 282 CFPC, Arts. 1068-1070 Código de Comercio). Si hay vicios en la notificación, puede impugnarse la diligencia.
- **Exhorto** — solicitud inter-jurisdiccional de un tribunal a otro. Verificar que el exhorto cumpla los requisitos formales (identificación del tribunal exhortante, objeto de la diligencia, documentos anexos). Si el exhorto proviene de tribunal extranjero, aplican las reglas de cooperación judicial internacional y tratados.
- **Requerimiento regulatorio** — de COFECE (investigación de prácticas monopólicas), CNBV (supervisión financiera), INAI (verificación de protección de datos), IMPI (investigación de PI), SAT (auditoría fiscal), PROFECO (verificación de consumo), STPS (inspección laboral), u otra autoridad. Cada regulador tiene su propia ley orgánica con facultades, plazos y consecuencias distintas.
- **Orden penal (ministerial/judicial)** — orden de cateo, decomiso, aseguramiento o similar derivada de procedimiento penal. Escalar inmediatamente a abogado penalista; fuera del alcance de este skill.

### Paso 2: Extraer campos clave

- **Autoridad emisora** — tribunal (cuál juzgado, circuito, materia), autoridad regulatoria (cuál), o tribunal exhortante
- **Expediente / número de causa** — número de expediente del juicio o procedimiento
- **Partes del procedimiento** — actor y demandado (si aplica)
- **Objeto del requerimiento** — qué se solicita (documentos, información, comparecencia, acto específico)
- **Categorías de documentos solicitados** — lista numerada
- **Plazo para cumplimiento** — fecha de notificación + cómputo del plazo según norma aplicable (días hábiles o naturales)
- **Plazo para impugnación** — si existe medio de defensa, plazo para interponerlo
- **Consecuencias del incumplimiento** — multa, medidas de apremio, desacato, uso de la fuerza pública
- **Alcance geográfico** — custodios, ubicaciones, sistemas implicados
- **Persona requerida** — a quién se dirige el requerimiento dentro de la organización

### Paso 3: Cruce con portafolio

- **Requerimiento de parte → relacionado con asunto existente:** verificar que el expediente coincida con un asunto en `_log.yaml`. Si sí, vincular al flujo de trabajo de ese asunto; este triaje es informativo.
- **Requerimiento como tercero → expediente desconocido:** capturar las partes; registrar como asunto independiente entrante.
- **Múltiples requerimientos del mismo procedimiento:** señalar emisión coordinada; una estrategia única de respuesta puede aplicar.

### Paso 4: Analizar alcance, carga, confidencialidad

**Alcance / pertinencia**
- ¿Las categorías solicitadas corresponden a documentos que razonablemente tenemos?
- ¿Alguna categoría es una solicitud genérica o desproporcionada (sin relación con el objeto del procedimiento)?
- Verificar competencia territorial y material de la autoridad emisora.

**Carga**
- Custodios implicados, sistemas a buscar, periodo temporal
- Volumen estimado (aproximado: pequeño / mediano / grande / extremo)
- Costo — verificar si la norma aplicable permite solicitar reembolso de costos de reproducción o búsqueda.

**Confidencialidad y secreto profesional**
- ¿Se implica secreto profesional del abogado? (Art. 36 Ley Reglamentaria del Art. 5° Constitucional; Arts. 210-211 CPF — revelación de secretos.)
- ¿Se implica información confidencial? (Datos personales protegidos por LGPDPPSP, secretos industriales protegidos por LFPPI, información financiera reservada ante CNBV.)
- ¿Se requiere una clasificación de documentos confidenciales? — señalar el formato según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`

**Otros fundamentos de objeción**
- **Improcedencia** — la autoridad no tiene facultades para requerir lo solicitado
- **Incompetencia** — la autoridad no es competente por materia, territorio o grado
- **Secreto profesional** — comunicaciones protegidas entre abogado y cliente
- **Cosa juzgada** — el asunto ya fue resuelto definitivamente
- **Prescripción / caducidad** — la acción o facultad de la autoridad ha prescrito o caducado
- **Información no poseída** — no tenemos lo que solicitan (documentar con especificidad)
- **Notificación defectuosa** — verificar si la notificación cumple los requisitos de forma de la norma procesal aplicable

### Paso 5: Marco de objeciones

Elaborar un esquema estructurado de objeciones — no la respuesta final, sino el esquema de qué objeciones aplican y por qué. El usuario (frecuentemente con abogado externo) finaliza.

Cada objeción:
- Fundamento legal — citar el artículo puntual de la norma investigada en el Paso 0
- Aplicación específica a este requerimiento (qué categorías, qué custodios)
- Fortaleza (fuerte / razonable / débil)

Medios de defensa a considerar:
- **Recurso de revocación** — ante el mismo juzgador (cuando la ley procesal lo permita)
- **Incidente** — para cuestiones accesorias (incompetencia, nulidad de notificación)
- **Queja** — contra resoluciones que no admiten recurso ordinario
- **Amparo indirecto** — contra actos de autoridad que violen garantías (Art. 107 Ley de Amparo). Plazo: 15 días hábiles desde la notificación.
- **Recurso de revisión** (en materia regulatoria) — ante la propia autoridad o tribunal administrativo (TFJA)

### Paso 6: Plan de cumplimiento

Aún cuando se objete, frecuentemente se produce parte de lo solicitado. Plan:

- **Alcance de la producción probable** — después de objeciones, qué produciríamos
- **Custodios a buscar** — nombres y sistemas
- **Rango de fechas**
- **Protocolo de revisión** — quién revisa por confidencialidad (nosotros, abogado externo, revisores)
- **Formato de producción** — según el requerimiento o según protocolo negociado (copias simples, copias certificadas, formato electrónico)
- **Requisitos de clasificación de información confidencial** — formato, campos
- **Acuse de recibo** — documentar la recepción y entrega para acreditar el cumplimiento (_desahogo del requerimiento_)

### Paso 7: Plazos procesales

Usar los plazos identificados en la investigación del Paso 0. Los plazos procesales en México se computan en días hábiles (salvo excepciones expresas) y corren a partir del día siguiente a la notificación. Verificar el cómputo contra la norma aplicable y el calendario del tribunal.

- **Plazo para cumplimiento** — según norma investigada; señalar si el usuario necesita más tiempo (solicitar prórroga al juzgador es el mecanismo estándar)
- **Plazo para interponer medio de defensa** — según norma investigada (recurso de revocación, incidente, queja)
- **Plazo para amparo indirecto** — 15 días hábiles desde la notificación (Art. 17 Ley de Amparo). Es improrrogable.
- **Fecha de producción** — si no prosperan las objeciones
- **Fecha límite para solicitar suspensión** — si se promueve amparo, la suspensión puede solicitarse junto con la demanda o después (Arts. 125-158 Ley de Amparo)

Calendarizar todos. Acción inmediata.

### Paso 8: Escribir triaje

Producto: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/triage.md`.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

# Triaje de Requerimiento

> **NO SUSTITUYE AL ABOGADO LITIGANTE.** Este es un análisis estructurado de clasificación y alcance para apoyar decisiones rápidas sobre plazos, retenciones y estrategia procesal. Toda referencia normativa es un punto de partida heurístico; el análisis jurisdiccional específico, la finalización de objeciones, la práctica de medios de defensa y las decisiones de fondo sobre confidencialidad requieren abogado litigante con conocimiento del foro. Involucrar al abogado externo para cualquier requerimiento que exceda el alcance rutinario.

**Slug:** [slug]
**Notificado:** [YYYY-MM-DD]
**Notificado a:** [entidad / representante legal / persona física]
**Archivo entrante:** [ruta]
**Clasificación:** [requerimiento-judicial / citatorio / exhorto / requerimiento-regulatorio / orden-penal]

---

## Campos clave

- **Autoridad emisora:** [tribunal/autoridad regulatoria]
- **Expediente:** [número]
- **Partes del procedimiento:** [actor vs. demandado]
- **Plazo para cumplimiento:** [fecha]
- **Plazo para medio de defensa:** [fecha]
- **Plazo para amparo indirecto:** [fecha]

## Categorías solicitadas (resumen)

[lista numerada, concisa]

## Custodios / sistemas probablemente implicados

[lista]

---

## Cruce con portafolio

**Asunto relacionado:** [slug o "ninguno"]
**Si requerimiento de parte:** [vinculado a asunto existente o nuevo asunto?]
**Si requerimiento como tercero:** [asunto independiente entrante]

---

## Análisis de alcance y carga

**Alcance:** [evaluación de pertinencia por categoría]
**Estimación de carga:** [pequeña / mediana / grande / extrema — con razonamiento]
**Cuestiones de competencia territorial/material:** [si las hay]

## Análisis de confidencialidad

*La clasificación de confidencialidad es una primera lectura; la decisión final es del abogado, no de este skill.*

**Secreto profesional probablemente implicado:** [sí/no + qué categorías] `[VERIFICAR CON EXPERTO]`
**Información confidencial implicada:** [datos personales, secretos industriales, información financiera reservada] `[VERIFICAR CON EXPERTO]`
**Formato de clasificación requerido:** [según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`]

---

## Marco de objeciones

*Cada fila requiere `[VERIFICAR CON EXPERTO]` antes de plasmarse por escrito — jurisdicción, vigencia normativa, riesgo de preclusión.*

| Objeción | Fundamento legal | Aplica a | Fortaleza | ¿Verificado? |
|---|---|---|---|---|
| Improcedencia | [norma] | [categorías] | [fuerte/razonable/débil] | [ ] |
| Incompetencia | [norma] | [categorías] | | [ ] |
| Secreto profesional | Art. 36 Ley Reg. Art. 5° / Arts. 210-211 CPF | [categorías con comunicaciones abogado-cliente] | fuerte (siempre) | [ ] |
| Carga desproporcionada | [norma] | [categorías] | | [ ] |
| Prescripción/caducidad | [norma] | [si aplica] | | [ ] |
| Notificación defectuosa | [norma procesal] | [si aplica] | | [ ] |
| [otra] | | | | [ ] |

---

## Medios de defensa disponibles

| Medio | Fundamento | Plazo | Ante quién | Observaciones |
|---|---|---|---|---|
| Recurso de revocación | [norma] | [plazo] | Mismo juzgador | |
| Incidente | [norma] | [plazo] | Mismo juzgador | |
| Queja | [norma] | [plazo] | Tribunal superior | |
| Amparo indirecto | Arts. 107, 114 Ley de Amparo | 15 días hábiles | Juzgado de Distrito | Solicitar suspensión del acto |
| Recurso de revisión (regulatorio) | [ley orgánica] | [plazo] | TFJA / autoridad superior | |

---

## Plan de cumplimiento (si se responde)

- **Alcance de producción probable:** [después de objeciones]
- **Custodios / sistemas:** [lista]
- **Rango de fechas:** [rango]
- **Protocolo de revisión:** [quién, cómo]
- **Formato de producción:** [formato]
- **Clasificación de confidencialidad:** [formato, entradas estimadas]
- **Acuse de recibo / desahogo:** [procedimiento para acreditar cumplimiento]

---

## Plazos procesales (calendarizar estos)

*Todos los plazos abajo provienen de la investigación normativa del Paso 0. `[VERIFICAR CON EXPERTO]` confirma la norma, variante y cómputo para este foro y tipo de requerimiento — los plazos varían según materia (civil, mercantil, laboral, administrativo) y fuero (federal/local).*

- **Plazo para cumplimiento:** [fecha] `[VERIFICAR CON EXPERTO]`
- **Plazo para medio de defensa ordinario:** [fecha] — cita: [norma + artículo] `[VERIFICAR CON EXPERTO]`
- **Plazo para amparo indirecto:** [fecha] — 15 días hábiles desde notificación `[VERIFICAR CON EXPERTO]`
- **Plazo para solicitar suspensión:** [fecha] `[VERIFICAR CON EXPERTO]`
- **Fecha de producción:** [fecha]

---

## Acciones inmediatas

- [ ] Retención legal emitida — [sí/no] — si no, ejecutar `/litigacion-legal-mexico:legal-hold [slug] --issue` con alcance del requerimiento
- [ ] Abogado externo contratado — [sí/quién/pendiente]
- [ ] Solicitud de prórroga presentada — [sí/no/pendiente]
- [ ] Asunto creado en el registro — [sí/no/pendiente — generalmente sí para cualquier requerimiento que no sea menor]
- [ ] Análisis de seguro / cobertura — [si la carga es grande]
- [ ] Escalamiento interno — [a quién]

---

## Recomendación

[Dos párrafos: qué hacer. Postura de objeción. Postura de cumplimiento. Si el abogado externo maneja las objeciones o nosotros. Si conviene promover amparo o medio de defensa.]

---

## Verificación de citas

Toda referencia normativa, tesis, jurisprudencia, ley y reglamento en este triaje — incluyendo las citas de la investigación del Paso 0, fundamentos de objeción, y el formato de clasificación de confidencialidad — es generada por IA y no está verificada. Antes de confiar en cualquier cita (especialmente en objeciones, medios de defensa, o correspondencia con la autoridad emisora), ejecutar un pase de verificación contra una herramienta de investigación jurídica (SCJN IUS, Semanario Judicial de la Federación, DOF, o la plataforma del despacho) para precisión, vigencia normativa y variantes locales. Citas fabricadas o mal citadas en escritos presentados ante tribunal han resultado en sanciones y responsabilidad profesional. Las etiquetas de fuente en cada cita (ej., `[SCJN IUS]`, `[búsqueda web — verificar]`) muestran su procedencia; las etiquetas `verificar` tienen mayor riesgo de fabricación y deben verificarse primero.
```

### Paso 9: Derivar

**Antes de responder al requerimiento (presentar objeciones, producir documentos, comparecer, o promover medio de defensa — cualquier respuesta sustantiva a la autoridad emisora o tribunal):** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No-abogado:

> Responder a un requerimiento tiene consecuencias legales — no cumplir un plazo implica riesgo de medidas de apremio o desacato, producir de más puede revelar información confidencial o secreto profesional, producir de menos implica riesgo de sanciones y cumplimiento forzoso. ¿Ha revisado esto con un abogado? Si sí, proceder. Si no, aquí hay un resumen para llevarle:
>
> [Generar un resumen de 1 página: tipo de requerimiento, autoridad emisora, plazos, alcance de lo solicitado, marco de objeciones y fortaleza, cuestiones de confidencialidad y carga, postura de respuesta propuesta, qué podría salir mal, qué preguntar al abogado.]
>
> Si necesita encontrar un abogado litigante con licencia en su jurisdicción: el Colegio de Abogados o la Barra Mexicana de Abogados son un buen punto de partida. Para asuntos regulatorios especializados, buscar despachos con experiencia ante la autoridad específica (COFECE, CNBV, INAI, etc.).

No proceder más allá de esta puerta sin un sí explícito. El triaje, la clasificación y el calendario interno no requieren la puerta — la respuesta a la autoridad emisora sí.

- Si clasificado como **orden penal** → parar, señalar para escalamiento según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`, no proceder con triaje estándar.
- Si clasificado como **requerimiento regulatorio**: señalar que aplican normas específicas del regulador; recomendar abogado externo especializado en la materia regulatoria.
- De otro modo: ofrecer crear un asunto (generalmente sí — los requerimientos casi siempre son suficientemente materiales para rastrear).
- Si no se ha emitido retención legal con alcance del requerimiento, derivar a `/litigacion-legal-mexico:legal-hold --issue` inmediatamente.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, observar y esperar, otra cosa) son un punto de partida, no un candado. El árbol es el producto; el abogado elige.

## Lo que este skill NO hace

- **Redactar la respuesta final al requerimiento.** Produce el marco; la respuesta es redactada por el usuario + abogado externo.
- **Promover amparos o medios de defensa.** Señala la opción; la promoción es trabajo jurídico que requiere análisis jurisdiccional específico.
- **Validar normas entre jurisdicciones.** La investigación del Paso 0 produce la norma operativa para este requerimiento; el skill no confirma independientemente vigencia o variantes locales. Señalar para verificación del abogado antes de actuar.
- **Manejar órdenes penales.** Escala. Esto está fuera del alcance del triaje.
