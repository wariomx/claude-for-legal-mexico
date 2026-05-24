---
name: demand-received
description: Triaje de una carta de requerimiento recibida — extraer campos, verificar cruce con el portafolio, evaluar mérito, presentar opciones de respuesta con recomendación, y entregar a matter-intake o demand-intake si se justifica la escalación. Usar cuando el usuario diga "nos llegó un requerimiento", "triaje esta demanda/carta", o comparta un requerimiento recibido para evaluar.
argument-hint: "[ruta-al-documento] [--slug=slug-personalizado]"
---

# /demand-received

1. Leer el documento entrante de la ruta proporcionada.
2. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para verificación cruzada del portafolio.
3. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → calibración de riesgo, panorama, práctica de cartas de requerimiento.
4. Seguir el flujo de trabajo y la referencia de abajo.
5. Extraer campos; verificar cruce con portafolio; evaluar mérito; presentar opciones con recomendación.
6. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/triage.md`. Copiar o vincular el documento entrante a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/incoming.[ext]`.
7. Entregar según decisión del usuario:
   - Crear asunto → `matter-intake` pre-poblado
   - Responder con contra-requerimiento → `demand-intake` pre-poblado
   - Vincular a asunto existente → actualizar `related_matters` en el log
   - Independiente → sin acción adicional

---

# Requerimiento Recibido

## Propósito

Los requerimientos entrantes son el pan de cada día de una práctica de litigación interna. Una fracción pequeña necesita escalación; la mayoría puede manejarse con una respuesta estructurada o una carta de acuse. El modo de falla es tratar todos igual. Este skill triajea, verifica cruce con el portafolio y produce opciones.

## Cargar contexto

- El documento entrante (el usuario proporciona ruta o lo comparte en sesión)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — buscar asuntos relacionados (misma contraparte, contrapartes superpuestas vía relaciones de entidades, o tipo de asunto + fecha reciente)
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → calibración de riesgo (para evaluación de mérito), panorama (¿el remitente es adversario frecuente?), práctica de cartas de requerimiento (tono y defaults de respuesta de la casa)

## Flujo de trabajo

### Paso 1: Leer el requerimiento

Extraer del documento entrante:

- **Remitente** — entidad, firmante, abogado (si firma un despacho externo)
- **Destinatario** — qué entidad/persona de nuestra empresa
- **Entrega** — correo certificado, correo electrónico, notificación personal, acta circunstanciada (importa para cómputo de plazos)
- **Fecha de recepción** vs. **fecha de firma**
- **Tipo de requerimiento** — pago, incumplimiento/saneamiento, cesación, preservación, conciliación, otro
- **Solicitudes específicas** — qué piden, para cuándo
- **Hechos alegados** — su versión de lo ocurrido
- **Fundamento legal** — leyes, artículos, disposiciones contractuales, teorías citadas
- **Amenazas** — qué dicen que harán si no cumplimos
- **Postura de conciliación** — observar si el requerimiento incluye apertura a negociación, oferta de convenio o mediación. Nota: en México las tratativas previas no tienen protección exclusionaria automática — lo que se diga en negociaciones puede potencialmente utilizarse como prueba. Capturar tanto el lenguaje explícito (si lo hay) como una primera lectura de si la sustancia es realmente una oferta de transacción.

### Paso 2: Verificación cruzada del portafolio

Buscar en `_log.yaml`:

- **Coincidencia directa** — asunto con la misma contraparte (su slug coincide con el remitente)
- **Coincidencia por tipo** — tipo de asunto similar con esta contraparte en el pasado (asuntos cerrados cuentan — informan el patrón)
- **Superposición temática** — asuntos donde el tema podría ser la misma disputa (e.g., mismo contrato, mismo producto, mismo proyecto)

Presentar hallazgos:

- Si **coincidencia directa + activo:** señalar como casi seguramente el mismo asunto; recomendar agregar el entrante al asunto existente, no abrir uno nuevo. Actualizar `related_matters` si es tangencial.
- Si **coincidencia directa + cerrado:** señalar — la contraparte regresa. Puede ser una nueva disputa (abrir nuevo asunto) o una resucitada (reabrir o enmendar). El usuario decide.
- Si **coincidencia por tipo:** notar como precedente/contexto; probablemente asunto distinto pero informa la estrategia de respuesta.
- Si **sin coincidencia:** novedoso. Tratar como nuevo.

### Paso 3: Evaluación de mérito

No es una opinión legal — es una lectura estructurada:

- **Hechos** — ¿los hechos alegados coinciden con lo que sabemos? ¿Dónde está la desconexión?
- **Fundamento legal** — ¿las disposiciones/leyes citadas son realmente aplicables? (Señalar citas para verificación del usuario — no intentar validar la ley autónomamente.)
- **Fortaleza de su lado** — si fueran a juicio mañana, ¿cuál es su narrativa?
- **Fortaleza de nuestro lado** — ¿cuáles son nuestras probables defensas y excepciones?
- **Monto demandado vs. probable** — ¿la solicitud es proporcional a lo que un juez otorgaría si ganaran?
- **Apalancamiento y presión** — ¿están preparados de manera creíble para demandar? ¿Tienen capacidad? ¿Son adversario recurrente según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`?

Emitir una calificación de triaje: **mérito sustancial / debatible / débil / frívolo**. Ser directo. El usuario está triageando, no escribiendo un escrito.

### Paso 4: Opciones de respuesta

Presentar 3-4 opciones con compensaciones:

**Opción A — respuesta sustantiva**
- Cuándo: su requerimiento tiene mérito o al menos es debatible; una respuesta razonada protege el registro
- Compensación: nos compromete a una posición por escrito
- Siguiente paso: `/demand-intake` con campos pre-poblados para una carta de contra-respuesta

**Opción B — carta de emplazamiento / acuse**
- Cuándo: necesitamos tiempo para investigar; no queremos conceder nada ni activar su cómputo de plazos
- Compensación: no resuelve nada; compra 2-4 semanas
- Siguiente paso: borrador de acuse breve

**Opción C — oferta de conciliación / mediación**
- Cuándo: la resolución temprana es más barata que el litigio; disposición a dialogar
- Compensación: en México las tratativas previas no tienen protección exclusionaria — cualquier oferta o concesión puede usarse como prueba en juicio. Se debe estructurar la respuesta con cuidado. Considerar un convenio judicial o extrajudicial como mecanismo formal de arreglo.
- Siguiente paso: `/demand-intake` con `type: settlement-response`

**Opción D — ignorar + preservar**
- Cuándo: el requerimiento es frívolo o el plazo no crea perjuicio legal
- Compensación: el silencio puede usarse en nuestra contra en algunos contextos (e.g., confesión ficta en juicio); la conservación documental sigue siendo necesaria
- Siguiente paso: emitir retención legal vía `/legal-hold --issue` si no se ha hecho; registrar el requerimiento y seguir adelante

Recomendar una. Ser específico sobre por qué.

### Paso 5: Triaje de plazos

- **Su plazo declarado** — notarlo, pero no nos vincula
- **Nuestro plazo interno** — cuándo debemos decidir (frecuentemente: plazo declarado menos 5 días hábiles para redactar + aprobar)
- **Plazos legales** — prescripción, periodos contractuales de saneamiento, requisitos procesales
  - Mercantil general: 10 años (Art. 1047 Código de Comercio) `[model knowledge — verify]`
  - Civil: varía por código estatal
  - Laboral — la mayoría de acciones: 1 año (Art. 516 LFT) `[model knowledge — verify]`
  - Laboral — separación del trabajo (despido justificado o injustificado): 2 meses (Art. 518 LFT). Plazo se suspende durante conciliación previa (Art. 684-B LFT). `[verified 2026-05-23]`

Señalar plazos legales ajustados. Calendarizarlos.

**Sin suplemento silencioso.** Si el requerimiento entrante cita leyes, artículos, tesis o jurisprudencia que requieren verificación, y una consulta a la herramienta de investigación legal configurada (SCJN IUS, Semanario Judicial, DOF, o plataforma del despacho) devuelve pocos o ningún resultado para una autoridad dada, reportar lo encontrado y detenerse. NO llenar el vacío con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece delgada para [cita / doctrina]. Opciones: (1) ampliar la consulta, (2) probar una herramienta diferente, (3) buscar en la web — los resultados se etiquetarán `[búsqueda web — verificar]` y deben verificarse contra fuente primaria, o (4) dejar el marcador `[VERIFICAR SME]` y detenerse aquí. ¿Cuál prefieres?" El abogado decide si acepta fuentes de menor confianza; el skill no decide por ellos.

**Atribución de fuente.** Etiquetar cada cita llevada al triaje — incluyendo las autoridades citadas por el remitente, los fundamentos de nuestras opciones de respuesta, y cualquier investigación realizada para la evaluación de mérito — con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o el nombre de la herramienta MCP para citas obtenidas vía conector de investigación legal; `[búsqueda web — verificar]` para citas de búsqueda web; `[conocimiento del modelo — verificar]` para citas recordadas de datos de entrenamiento; `[proporcionado por usuario]` para citas suministradas en el requerimiento mismo. Las citas etiquetadas `verificar` tienen mayor riesgo de fabricación y deben verificarse primero. Nunca eliminar o colapsar las etiquetas.

### Paso 6: Escribir triaje

Salida: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/[slug]/triage.md`.

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

> **Herencia de confidencialidad.** Este triaje deriva del requerimiento entrante y del log del portafolio, y registra nuestra primera lectura de mérito y postura de respuesta. Esos análisis internos son material de secreto profesional y/o producto de trabajo. Distribuir este triaje fuera del círculo de confidencialidad — incluyendo reenviarlo al líder de negocio sin marca, compartirlo con la contraparte o adjuntarlo a una notificación de seguro sin depurar — puede comprometer la protección tanto de este documento como del razonamiento contenido. Almacenar con material confidencial del asunto, marcar consistentemente con las convenciones de confidencialidad de la casa, y tomar decisiones de distribución deliberadamente.

# Requerimiento Recibido — Triaje

> **LECTURA PARA TRIAJE, NO OPINIÓN.** Este documento es un escaneo de intake y un análisis de opciones — no una opinión legal sobre el mérito. La `Calificación de triaje` abajo es una lectura estructurada para apoyar la decisión del abogado sobre cómo encauzar el requerimiento. No es una recomendación sobre el mérito y no sustituye el análisis legal específico del caso. Cada ley, artículo, tesis o jurisprudencia citada está señalada para verificación SME; cada decisión de mérito es del abogado, no de este skill.

**Slug:** [slug]
**Recibido:** [YYYY-MM-DD]
**Recibido por:** [entidad / persona]
**Archivo entrante:** [ruta]

---

## El requerimiento

**Remitente:** [entidad, firmante, abogado]
**Tipo de requerimiento:** [tipo]
**Solicitudes específicas:** [lista]
**Su plazo declarado:** [fecha]
**Postura de conciliación:** [con apertura / aserción pura / ambiguo] — *en México las tratativas previas no tienen protección exclusionaria; `[VERIFICAR SME]` contra el marco procesal aplicable*

## Hechos alegados

[su versión, en un párrafo]

## Fundamento legal citado

[citas — cada una marcada en línea con `[VERIFICAR SME: aplicabilidad / vigencia / jurisdicción]` — no confiar en ninguna cita aquí sin verificación independiente]

## Amenazas / siguientes pasos que declaran

[lista]

---

## Verificación cruzada del portafolio

**Coincidencia directa:** [slug si existe, o "ninguna"]
**Coincidencia por tipo / precedente:** [lista o "ninguno"]
**Superposición temática:** [lista o "ninguna"]
**Recomendación:** [nuevo asunto / agregar a existente / vincular vía related_matters / entrante independiente]

---

## Evaluación de mérito

**Hechos:** [alineación con nuestra versión; desconexiones]
**Fundamento legal:** [aplicabilidad, con señalamientos]
**Su caso si litigaran:** [un párrafo]
**Nuestras defensas y excepciones:** [un párrafo]
**Proporcionalidad de daños:** [evaluación]
**Credibilidad de la amenaza:** [¿van a demandar? ¿tienen capacidad? ¿adversario recurrente?]

**Calificación de triaje:** [sustancial / debatible / débil / frívolo] — *lectura estructurada para encauzamiento, no opinión de mérito; `[VERIFICAR SME: el abogado debe confirmar antes de confiar en esto]`*

---

## Opciones de respuesta

### A. Respuesta sustantiva
[Fundamento, compensaciones, siguiente paso]

### B. Carta de acuse / emplazamiento
[Fundamento, compensaciones, siguiente paso]

### C. Oferta de conciliación / mediación
[Fundamento, compensaciones, siguiente paso]

### D. Ignorar + preservar
[Fundamento, compensaciones, siguiente paso]

**Recomendación:** [A/B/C/D] — [dos oraciones por qué] — `[VERIFICAR SME: el abogado debe confirmar antes de ejecutar]`

---

## Plazos

- **Su plazo declarado:** [fecha]
- **Nuestro plazo interno de decisión:** [fecha]
- **Plazos legales:** [prescripción, periodos de saneamiento, procesales — con fechas]

---

## Acciones inmediatas

- [ ] Retención legal emitida — [sí/no] — si no, ejecutar `/legal-hold [slug] --issue`
- [ ] Asunto creado en log — [sí/no/por determinar]
- [ ] Abogado asignado — [quién]
- [ ] Notificación a aseguradora — [sí/no/N-A]
- [ ] Escalación interna (Director Jurídico / Director de Finanzas / líder de negocio) — [quién/cuándo]
```

### Paso 7: Entrega

Según recomendación y confirmación del usuario:

- Creación de asunto → entregar a `/matter-intake` con: contraparte, tipo, `source: demand-letter` (entrante), teoría inicial enmarcada defensivamente, pre-poblado.
- Contra-respuesta como requerimiento saliente → entregar a `/demand-intake` con: contraparte, contexto del triaje, resultado deseado como la respuesta.
- Vincular a asunto existente → actualizar `related_matters` de ese asunto en `_log.yaml`; agregar evento a su `history.md`.
- Independiente → dejar en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/inbound/`; sin cambio al portafolio.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill produjo — las cinco ramas default (redactar el X, escalar, obtener más hechos, observar y esperar, algo más) son un punto de partida, no un candado. El árbol es el resultado; el abogado elige.

## Lo que este skill NO hace

- **Validar ley citada.** Señala citas para que el usuario las verifique contra fuente primaria (confirmar vigencia y aplicabilidad) o consulte con despacho externo. Inventar análisis legal sobre requerimientos entrantes es exposición a responsabilidad profesional.
- **Enviar una respuesta.** Los borradores se redactan en `demand-draft`; este skill se detiene en la decisión de triaje.
- **Decidir el mérito definitivamente.** La calificación es una lectura para triaje; una opinión formal de mérito corresponde al despacho externo o a un análisis más profundo.
- **Tomar la decisión de creación de asunto.** Presenta la recomendación; el usuario decide.
