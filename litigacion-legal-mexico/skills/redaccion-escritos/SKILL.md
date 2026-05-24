---
name: redaccion-escritos
description: >
  Redacta escritos judiciales en formato procesal mexicano — demandas,
  contestaciones, alegatos, conceptos de violación, incidentes y recursos —
  con cada hecho citado, cada fundamento verificado y cada argumento vinculado
  a la teoría del caso.
argument-hint: "[tipo de escrito — e.g., 'demanda mercantil', 'contestación', 'conceptos de violación']"
---

# /redaccion-escritos

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → teoría del caso, estilo de casa, lado.
2. Seguir el flujo de trabajo y referencia abajo.
3. Redactar en formato procesal mexicano y en español. Consistente con la teoría del caso.
4. Salida: borrador del escrito. Señalar cada lugar donde un hecho o cita necesita verificación.

---

# Redacción de Escritos Judiciales

## Propósito

Un buen escrito judicial es consistente con la teoría del caso, citado al expediente, fundamentado en ley vigente y verificable. Este skill produce el primer borrador — énfasis en *borrador*. El abogado titular revisa, edita y firma.

## Sistema procesal mexicano — no es common law

México opera bajo un sistema de derecho civil codificado. No existe el concepto de _brief_ como en common law. Los escritos judiciales mexicanos siguen una estructura formalista dictada por el código procesal aplicable. Cada escrito se dirige a una autoridad jurisdiccional específica, invoca una vía procesal concreta y debe cumplir requisitos de forma que, de no satisfacerse, pueden resultar en prevención, desechamiento o inadmisión.

**No hay _discovery_, _depositions_, _Bates numbering_, _FRCP_, _Bluebook_, ni estructura CRAC.** Las pruebas se ofrecen y desahogan dentro del juicio. Las citas siguen la convención mexicana. Los argumentos se estructuran por fundamento legal, no por issue-rule-application-conclusion.

## Tipos de escrito que cubre este skill

| Tipo | Cuándo se usa | Código procesal |
|---|---|---|
| Demanda | Escrito inicial que ejercita la acción | Cód. Comercio / CFPC / CNPCF / LFT |
| Contestación de demanda | Respuesta punto por punto a la demanda | Mismo que la demanda |
| Alegatos | Argumentos finales después de la fase probatoria | Mismo que la demanda |
| Conceptos de violación | Argumentos constitucionales en amparo | Ley de Amparo |
| Incidentes | Promociones interlocutorias durante el juicio | Código procesal aplicable |
| Recurso de apelación | Agravios para revisión en segunda instancia | Código procesal aplicable |

## Vía procesal — preguntar antes de redactar

El tipo de documento no basta. La **vía procesal** determina qué artículos fundamentan las prestaciones, qué requisitos de forma exige el código y qué pruebas deben acompañar el escrito inicial:

- **Ordinaria mercantil** — Arts. 1377-1390 Código de Comercio. Demanda estándar; periodo probatorio de 40 días.
- **Ejecutiva mercantil** — Arts. 1391-1414 Código de Comercio. Requiere título ejecutivo (Art. 1391). Sin título, la vía es improcedente.
- **Ordinaria civil federal** — CFPC. Procedimiento supletorio.
- **Ordinaria civil local** — CNPCF o código procesal estatal aplicable.
- **Laboral** — LFT Arts. 684-A y ss. (nuevo sistema de justicia laboral). Conciliación prejudicial obligatoria ante CFCRL.
- **Amparo indirecto** — Ley de Amparo Arts. 107-113. Ante Juzgado de Distrito.
- **Amparo directo** — Ley de Amparo Arts. 170-178. Ante Tribunal Colegiado de Circuito.
- **Apelación** — Código procesal aplicable. Ante tribunal de segunda instancia.

Preguntar al usuario: "¿Cuál es la vía procesal?" Si no la conoce, ayudarle a determinarla a partir de los hechos, la relación jurídica y la pretensión.

## Fidelidad al expediente — citas y referencias puntuales

Dos reglas que gobiernan cada cita y cada referencia al expediente. Declaración canónica en las salvaguardas compartidas del CLAUDE.md del plugin; repetida aquí porque este skill es donde más se ponen a prueba.

**Las citas textuales del expediente deben ser textuales.** Nunca poner comillas alrededor de palabras atribuidas a la contraparte, un testigo, el juzgador o cualquier documento del expediente a menos que tengas el pasaje exacto frente a ti y puedas citarlo. Cuando quieras caracterizar lo que alguien dijo pero no encuentras las palabras exactas:

- **Parafrasear sin comillas**, atribuyendo claramente: "La demandada manifestó que X `[verificar contra expediente — foja __]`."
- **Marcar el marcador de posición:** `[verificar cita exacta — referencia del expediente pendiente]`
- **Nunca llenar el vacío.** Una cita inventada, incluso una palabra, es una fabricación. La nota de revisión debe señalar cada `[verificar cita exacta]` en la salida.

**Las citas puntuales deben soportar toda la proposición.** Si el argumento es "la demandada incumplió X, Y y Z según el contrato," verificar que la cláusula citada soporta X Y Y Y Z. Si solo soporta Z, dividir la cita o acotar la proposición.

## Formato de citas — convención mexicana

**Legislación:** Ley, artículo, fracción, inciso.
- Ejemplo: Art. 1391, fracción IV, del Código de Comercio.
- Ejemplo: Art. 107, fracción III, inciso a), de la Constitución Política de los Estados Unidos Mexicanos.

**Jurisprudencia y tesis aisladas del Poder Judicial de la Federación:**
```
Tesis: [registro digital], [instancia], [materia], [época], [tipo: aislada/jurisprudencia], [clave]
```
- Ejemplo: Tesis: 2024567, Tribunales Colegiados de Circuito, Civil, Undécima Época, Jurisprudencia, TC.IV.C. J/12 C (11a.) `[SCJN IUS]`

**Nunca usar Bluebook, ALWD ni ningún formato de cita anglosajón.** Las citas en el escrito siguen exclusivamente la convención mexicana.

## Franqueza sobre argumentos débiles

Cuando la ley o los hechos van en contra de un punto, decirlo. No construir un argumento endeble y presentarlo como sólido. Señalarlo:

> "Este punto es débil — [autoridad / hecho] va en sentido contrario. Opciones: (a) presionarlo enmarcándolo como [encuadre alternativo], (b) conceder y pivotar a [punto más fuerte], (c) eliminarlo. `[revisar — decisión estratégica]`."

Afirmar un argumento débil sin señalarlo erosiona la credibilidad del abogado ante el juzgador. El borrador debe hacer al abogado más informado, no más confiado sobre una mala posición.

## Eco vs repetición

Hacer eco de encuadres clave de escritos previos — la misma caracterización de los hechos, el mismo encuadre de la acción, la misma teoría del caso. Pero no copiar oraciones enteras. Un escrito que suena a copia del anterior señala que la posición no avanzó. El nuevo escrito debe avanzar el argumento.

## Cargar contexto

`~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → teoría del caso, estilo de casa (formato de citas, estructura, tono).

**Puerta de conflictos — no eludible.** Antes de redactar, verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para el slug del asunto sobre el que se invoca este skill. Si el asunto no está en `_log.yaml`, rechazar y redirigir:

> "No veo [slug del asunto] en el registro de asuntos. Ejecute `/litigacion-legal-mexico:matter-intake` primero para que se ejecute la verificación de conflictos y se configure el espacio de trabajo del asunto. No redactaré escritos judiciales sobre un asunto que no ha sido recibido — la verificación de conflictos es la puerta."

No proceder con un asunto no recibido. El intake es lo que ejecuta conflictos, configura `matter.md` / `history.md`, y escribe la fila de `_log.yaml` que este skill lee.

## Flujo de trabajo

### Paso 1: ¿Qué escrito y en qué vía?

Preguntar y confirmar:
1. **Tipo de escrito** — demanda, contestación, alegatos, conceptos de violación, incidente, recurso de apelación.
2. **Vía procesal** — ordinaria mercantil, ejecutiva mercantil, ordinaria civil, laboral, amparo indirecto, amparo directo, apelación.
3. **Código procesal aplicable** — Código de Comercio, CFPC, CNPCF, LFT, Ley de Amparo.
4. **Autoridad jurisdiccional** — a qué juzgado o tribunal se dirige.

**Investigar las reglas del foro y procedimiento aplicables.** Citar fuentes primarias (artículo, fracción, inciso del código procesal). No aplicar un esquema genérico. Verificar vigencia.

### Paso 2: Verificación de teoría del caso

Antes de redactar: ¿qué necesita lograr este escrito para la teoría del caso?

- **Demanda:** Encuadrar los hechos de modo que nuestra teoría sea la lectura natural. Cada prestación debe ser la consecuencia lógica de los hechos y fundamentos.
- **Contestación:** Desmontar la teoría del actor hecho por hecho. Oponer excepciones que destruyan la acción o sus presupuestos procesales.
- **Alegatos:** Sintetizar las pruebas desahogadas y vincularlas con la teoría. Este es el último escrito antes de la sentencia.
- **Conceptos de violación:** Demostrar que el acto reclamado transgrede la Constitución. Cada concepto es un argumento autónomo.
- **Incidentes:** Resolver una cuestión procesal específica que afecta la marcha del juicio.
- **Recurso de apelación:** Demostrar que la resolución recurrida viola la ley con agravios específicos.

Si el escrito que se va a redactar contradice la teoría del caso — detenerse. O la teoría está mal o el enfoque del escrito está mal. Señalarlo, no disimularlo.

### Paso 3: Redactar según la plantilla del tipo de escrito

**Investigar las reglas procesales del foro para requisitos de forma, plazos, copias y formalidades de presentación; no depender de suposiciones. Citar fuentes primarias (artículo del código procesal) en las notas de redacción. Verificar vigencia — las leyes procesales cambian.**

Seleccionar la plantilla correspondiente de la Sección "Plantillas por tipo de escrito" abajo. Redactar en español. Aplicar el estilo de casa según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.

### Paso 4: Fundamentar y citar

Cada hecho → referencia al expediente (foja, documento, fecha).
Cada proposición jurídica → artículo de ley con fracción e inciso, o tesis/jurisprudencia.

**Disciplina de marcadores — usar liberalmente:**
- `[VERIFICAR: aseveración fáctica específica]` — cualquier hecho no confirmado contra el expediente
- `[INCIERTO: proposición jurídica específica]` — cualquier punto legal no confirmado contra autoridad vigente
- `[CITA NECESARIA: cita específica — hecho/norma que se cree pero cita no localizada]`

Un borrador con marcadores sin resolver no es final. Los marcadores hacen explícito el paso de verificación.

**Sin complemento silencioso.** Si una consulta a la herramienta de investigación jurídica configurada (SCJN IUS, Semanario Judicial, DOF, plataforma del despacho) devuelve pocos o ningún resultado para una autoridad que el escrito necesita, reportar lo encontrado y detenerse. No llenar el vacío con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece escasa para [tema / autoridad]. Opciones: (1) ampliar la consulta, (2) probar otra herramienta, (3) buscar en web — resultados etiquetados `[búsqueda web — verificar]`, o (4) dejar el marcador `[CITA NECESARIA]` y detenerse aquí. ¿Cuál prefiere?"

**Atribución de fuentes.** Etiquetar cada cita con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o el nombre de la herramienta MCP para citas obtenidas vía conector; `[búsqueda web — verificar]` para citas web; `[conocimiento del modelo — verificar]` para citas de entrenamiento; `[proporcionado por usuario]` para citas del abogado o del expediente. Citas etiquetadas `verificar` tienen mayor riesgo de fabricación. Nunca eliminar ni colapsar las etiquetas. **`[asentado — última confirmación AAAA-MM-DD]`** para referencias normativas estables verificadas contra fuente primaria en la fecha indicada.

### Paso 5: Salida

**Compuerta de presentación para no abogados.** Antes de que el escrito sea presentado ante el juzgado (el acto con consecuencias — este skill redacta, pero la compuerta se ejecuta al momento de la presentación): leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Presentar un escrito judicial tiene consecuencias legales: si es una demanda, el emplazamiento perfecciona la relación procesal, la litis contestatio fija los términos de la controversia (Arts. 1378-1380 Código de Comercio), la prescripción se interrumpe (Art. 1041 Código de Comercio / Art. 1168 CCF), y la inactividad procesal puede generar caducidad de la instancia. Si es un recurso, los plazos son fatales — una vez transcurridos, el derecho se pierde. ¿Ha revisado este escrito con un abogado con cédula profesional vigente?
>
> Si sí, proceder. Si no, aquí hay un resumen para llevarle:
>
> [Generar resumen de 1 página: tipo de escrito, teoría del caso, fundamentos jurídicos invocados, marcadores `[VERIFICAR]` / `[INCIERTO]` / `[CITA NECESARIA]` sin resolver, riesgos (aseveración fáctica errónea, cita no verificada, argumento fuera de la teoría), qué preguntar al abogado antes de presentar.]
>
> Si necesita encontrar un abogado con cédula profesional vigente: la Barra Mexicana de Abogados, el Colegio de Abogados de su entidad federativa, o el Ilustre y Nacional Colegio de Abogados de México son puntos de referencia.

No tratar el borrador como listo para presentar sin un sí explícito.

**Encabezado de confidencialidad condicional al rol (por `## Resultados` del CLAUDE.md del plugin):**
- Si el Rol es Abogado / profesional jurídico: `PRIVILEGIADO Y CONFIDENCIAL — SECRETO PROFESIONAL` (Art. 36 Ley Reglamentaria del Art. 5° Constitucional Relativo al Ejercicio de las Profesiones en la Ciudad de México).
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORÍA LEGAL`

**Nota: México no tiene la doctrina de _attorney work product_. La protección del secreto profesional se fundamenta en el Art. 36 de la Ley Reglamentaria del Art. 5° Constitucional. No invocar doctrinas de common law.**

El escrito, en formato procesal mexicano, con marcadores en línea.

Prefacio (no parte del escrito — nota al abogado revisor):

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — varía por rol]

## Notas de Redacción — [Tipo de Escrito] — [fecha]

**Vínculo con teoría del caso:** [Cómo este escrito soporta la teoría del caso]
**Vía procesal:** [vía y código procesal aplicable]
**Autoridades invocadas:** [lista — todas requieren verificación de vigencia]
**Referencias al expediente por verificar:** [N] señaladas en línea
**Preguntas pendientes para el abogado titular:** [cualquier supuesto del borrador que debe confirmarse]
**Extensión:** [páginas/palabras vs. norma del foro si aplica]

---

**Verificar citas antes de presentar.** Las citas normativas (artículos de ley, fracciones, incisos), tesis y jurisprudencia en este borrador fueron generadas por un modelo de IA y no han sido verificadas contra fuente primaria. Ejecutar cada ley, artículo, tesis y jurisprudencia a través de SCJN IUS, Semanario Judicial de la Federación, DOF, o su plataforma de investigación — confirmar vigencia, alcance y que la autoridad sostenga la proposición para la que se cita. Citas fabricadas o inexactas en escritos presentados ante tribunales generan responsabilidad profesional y pueden resultar en sanciones procesales.

**Borrador — no un escrito presentado.** Presentar este escrito inicia o participa en un procedimiento judicial con consecuencias procesales (emplazamiento, fijación de litis, caducidad, preclusión de derechos). Un abogado con cédula profesional vigente revisa, edita y asume la responsabilidad profesional antes de la presentación. No presentar sin revisión.
```

---

## Plantillas por tipo de escrito

### A. Demanda

La demanda es el escrito que ejercita la acción y fija los términos de la pretensión. Su estructura varía por vía procesal, pero los elementos esenciales son:

1. **Rubro** — tribunal competente, tipo de juicio, nombre del actor
2. **Autoridad jurisdiccional** — "C. JUEZ [competencia] EN TURNO DE [circuito/distrito/partido judicial]" o juzgado específico
3. **Proemio** — nombre del actor, personalidad, domicilio para oír y recibir notificaciones, personas autorizadas (Art. 1069 Código de Comercio para mercantil)
4. **Nombre y domicilio del demandado** — para efectos de emplazamiento
5. **Vía procesal** — ordinaria mercantil / ejecutiva mercantil / ordinaria civil / laboral — con fundamento legal
6. **Prestaciones reclamadas** — cada prestación numerada, con su fundamento específico. En ejecutiva mercantil, identificar el título ejecutivo (Art. 1391 Código de Comercio) `[VERIFICAR: que el documento constituya título ejecutivo]`
7. **Hechos** — numerados, cronológicos, cada uno con prueba que lo soporta. Un hecho por párrafo numerado. Hechos que son advocacy a través de la selección y la secuencia, no argumento
8. **Fundamentos de derecho** — artículos específicos de ley con fracción e inciso. Separar sustantivos (que crean el derecho) de procesales (que regulan el procedimiento)
9. **Pruebas ofrecidas** — listar cada medio de prueba vinculado al hecho que acredita. Documentales, confesional, testimonial, pericial, inspección judicial, presuncional, instrumental de actuaciones
10. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ, ATENTAMENTE PIDO SE SIRVA:" + peticiones numeradas (admitir demanda, emplazar, tener por ofrecidas pruebas, dictar sentencia condenando a las prestaciones reclamadas)

**Para juicio ejecutivo mercantil:** adjuntar el título ejecutivo. Sin título, la vía es improcedente (Art. 1392 Código de Comercio). Verificar que el documento encuadre en alguna fracción del Art. 1391.

**Para juicio laboral:** la demanda laboral tiene requisitos propios (Art. 712 LFT vigente / Arts. 873-A y ss. para el nuevo sistema). La carga de la prueba se invierte frecuentemente al patrón (Art. 784 LFT). Verificar si se agotó la conciliación prejudicial obligatoria ante el CFCRL `[VERIFICAR: constancia de no conciliación]`.

**Prescripción y caducidad.** Antes de redactar la demanda, verificar plazos:
- **Prescripción de la acción** — varía por materia: 10 años para acciones civiles ordinarias (Art. 1159 CCF); plazos especiales en Código de Comercio (Art. 1043 y ss.); 1 año para acciones laborales de despido (Art. 518, fracción I, LFT); 15 días para amparo indirecto / 15 días para amparo directo (Arts. 17-18 Ley de Amparo). Un escrito que ejercita una acción prescrita será desechado o declarado improcedente por excepción de la contraparte `[VERIFICAR: cómputo de prescripción contra hechos del caso]`.
- **Caducidad de la instancia** — inactividad procesal por el plazo legal puede extinguir el procedimiento (Art. 1076 Código de Comercio para mercantil: 120 días de inactividad procesal; CFPC y códigos estatales tienen plazos propios). Verificar que no haya caducidad pendiente.

### B. Contestación de demanda

La contestación responde **punto por punto** a cada hecho y prestación de la demanda. No es una narrativa libre; es una respuesta estructurada a la litis planteada por el actor.

1. **Rubro** — mismo expediente, nombre del demandado
2. **Proemio** — nombre del demandado, personalidad, domicilio para notificaciones, personas autorizadas
3. **Respuesta a cada prestación** — negar o reconocer, con fundamento
4. **Respuesta a cada hecho** — para cada hecho numerado de la demanda, responder con una de tres posturas:
   - **"Cierto"** — se reconoce el hecho (cuidado: la admisión es vinculante)
   - **"Falso"** — se niega el hecho con la versión del demandado y la prueba que la soporta
   - **"No me consta"** — el demandado no tiene conocimiento del hecho (trasladar la carga probatoria al actor)
5. **Excepciones y defensas** — numeradas, cada una con fundamento legal. Separar excepciones procesales (incompetencia, litispendencia, conexidad, falta de personalidad, oscuridad de la demanda) de excepciones sustantivas (prescripción, pago, compensación, novación, cumplimiento)
6. **Hechos propios** — hechos que el demandado aporta y que no están en la demanda, numerados
7. **Fundamentos de derecho** — artículos que soportan las excepciones y defensas
8. **Pruebas ofrecidas** — medios de prueba del demandado, vinculados a los hechos que acreditan
9. **Reconvención** — si procede, con estructura de demanda completa (prestaciones, hechos, fundamentos, pruebas, puntos petitorios propios)
10. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ, ATENTAMENTE PIDO SE SIRVA:" + peticiones (tener por contestada la demanda, admitir excepciones, tener por ofrecidas pruebas, absolver al demandado)

**La estructura hecho-por-hecho es obligatoria.** Un hecho de la demanda no contestado puede tenerse por admitido tácitamente (Art. 1378, último párrafo, Código de Comercio, para mercantil). No omitir ningún hecho.

**Plazos fatales para contestar.** La contestación tiene plazo fatal que varía por vía procesal:
- Ordinario mercantil: 15 días hábiles (Art. 1378 Código de Comercio) `[INCIERTO — verificar plazo vigente]`
- Ejecutivo mercantil: 5 días hábiles (Art. 1396 Código de Comercio)
- Laboral: según citación a audiencia en el nuevo sistema
- Verificar siempre el plazo contra el código procesal aplicable y los acuerdos del juzgador. Un plazo vencido = rebeldía y pérdida del derecho a contestar.

### C. Alegatos

Los alegatos se presentan después del desahogo de pruebas y antes de que el juzgador dicte sentencia. Son el último escrito argumentativo.

1. **Rubro** — expediente, parte que presenta
2. **Objeto** — "Vengo a formular alegatos en el juicio [tipo] que se sigue ante este H. Juzgado"
3. **Síntesis de la litis** — los puntos controvertidos tal como quedaron fijados
4. **Valoración de pruebas** — análisis de cada prueba desahogada y su valor conforme al sistema de valoración aplicable (tasado para mercantil bajo Código de Comercio; libre convicción según CNPCF donde aplique)
5. **Argumentos jurídicos** — vincular las pruebas desahogadas con los fundamentos de derecho. Cada argumento: hecho probado + norma aplicable + conclusión favorable
6. **Desvirtuamiento de la posición contraria** — señalar las debilidades de las pruebas y argumentos de la contraparte
7. **Jurisprudencia y tesis aplicables** — sostener los argumentos con criterios del Poder Judicial de la Federación
8. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ, ATENTAMENTE PIDO SE SIRVA:" + petición de dictar sentencia favorable

**Escritos vs. orales.** Preguntar: "¿Los alegatos son por escrito o se formularán en audiencia?" Son oficios diferentes:
- **Escritos:** exhaustivos. Cubrir todos los puntos, desarrollar la autoridad, anticipar la réplica.
- **Orales (en audiencia):** estratégicos. Seleccionar los 3-4 puntos que más importan. Conceder o ignorar los débiles. El juzgador recuerda los primeros y últimos minutos. Si se responde a una posición compleja de la contraparte, señalar al abogado qué puntos presionar y cuáles dejar — eso es la estrategia, no solo las palabras.

### D. Conceptos de violación (amparo)

Los conceptos de violación son el núcleo del escrito de amparo. Cada concepto es un argumento autónomo que demuestra cómo el acto reclamado transgrede la Constitución o los tratados internacionales. Un concepto que solo enuncia la violación sin argumentarla es inoperante.

1. **Rubro** — "AMPARO [INDIRECTO/DIRECTO]", autoridad, quejoso
2. **Autoridad responsable** — la autoridad que emitió el acto reclamado (ordenadora y ejecutora si aplica)
3. **Acto reclamado** — descripción precisa del acto que se impugna (sentencia, resolución, acto administrativo, ley auto-aplicativa)
4. **Tercero interesado** — la contraparte en el juicio de origen, si aplica
5. **Antecedentes** — hechos que generaron el acto reclamado, en orden cronológico
6. **Procedencia del amparo** — fundamentar por qué procede la vía (Arts. 107 y 170 Ley de Amparo para directo; Arts. 107 y 114 para indirecto `[VERIFICAR: numeración Art. 114 Ley de Amparo vigente 2013]`)
7. **Conceptos de violación** — cada uno numerado y con esta estructura:
   - **Artículo(s) constitucional(es) o convencional(es) violado(s)** — identificar con precisión (Arts. 14, 16, 17 Constitución; tratados internacionales aplicables)
   - **Acto específico que los viola** — qué hizo o dejó de hacer la autoridad responsable
   - **Argumentación** — por qué el acto viola el artículo constitucional. Desarrollar la lógica: premisa constitucional → acto contrario → consecuencia jurídica. No basta decir "se violó el Art. 14"; hay que demostrar *cómo* se violó
   - **Jurisprudencia y tesis de apoyo** — criterios del Poder Judicial de la Federación que sostienen la interpretación constitucional invocada
8. **Suspensión del acto reclamado** — si procede, solicitar la suspensión provisional y definitiva (Arts. 125-158 Ley de Amparo). Argumentar los requisitos: apariencia del buen derecho, peligro en la demora, ponderación del interés social, que no se sigan perjuicios al interés social ni se contravengan disposiciones de orden público
9. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ DE DISTRITO, ATENTAMENTE PIDO SE SIRVA:" + admitir demanda de amparo, conceder suspensión, declarar la inconstitucionalidad del acto reclamado y amparar y proteger al quejoso

**Un concepto de violación inoperante no demuestra nada.** Cada concepto debe articular: (a) el derecho fundamental invocado, (b) por qué el acto lo viola, (c) la argumentación jurídica que conecta (a) con (b), y (d) jurisprudencia o tesis que lo soporte. Sin (c), el concepto es inoperante — el tribunal lo desestimará por insuficiente.

**Amparo directo vs. indirecto — diferencias estructurales:**
- **Indirecto** (Art. 107 Ley de Amparo): procede contra leyes, actos de autoridad que no sean sentencias definitivas, actos en juicio ejecutados fuera de juicio o después de concluido, actos que afecten a personas extrañas al juicio. Se presenta ante Juzgado de Distrito. Puede solicitar suspensión del acto reclamado.
- **Directo** (Art. 170 Ley de Amparo): procede contra sentencias definitivas, laudos y resoluciones que pongan fin al juicio. Se presenta ante el Tribunal Colegiado de Circuito competente por conducto de la autoridad responsable. Los conceptos de violación atacan la sentencia misma — sus fundamentos, su valoración de pruebas, su aplicación de la ley.
- El error más común: plantear amparo indirecto cuando procede directo (o viceversa). Verificar la naturaleza del acto reclamado antes de determinar la vía `[VERIFICAR: procedencia de la vía de amparo]`.

### E. Incidentes

Los incidentes son promociones que resuelven cuestiones accesorias durante el juicio sin decidir el fondo.

1. **Rubro** — expediente, incidentista
2. **Tipo de incidente** — identificar con precisión: nulidad de actuaciones, nulidad de notificaciones, incompetencia por declinatoria, acumulación, separación de juicios, liquidación de sentencia, ejecución de sentencia, reposición de autos, entre otros
3. **Fundamento legal del incidente** — artículos específicos del código procesal que regulan el incidente invocado
4. **Hechos que motivan el incidente** — narración de los hechos procesales que dan lugar a la promoción
5. **Argumentos jurídicos** — por qué procede el incidente conforme al supuesto normativo
6. **Pruebas** — medios de prueba que acreditan los hechos del incidente
7. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ, ATENTAMENTE PIDO SE SIRVA:" + peticiones específicas al tipo de incidente (declarar la nulidad, declarar la incompetencia, ordenar la acumulación, etc.)

**Incidentes de previo y especial pronunciamiento** se resuelven antes de la sentencia definitiva y suspenden el procedimiento principal. Verificar si el incidente tiene ese efecto.

### F. Recurso de apelación

El recurso de apelación impugna resoluciones del juzgador de primera instancia ante el tribunal de segunda instancia. La estructura gira alrededor de los **agravios**.

1. **Rubro** — expediente, apelante, resolución recurrida
2. **Resolución recurrida** — identificar con precisión: sentencia definitiva, sentencia interlocutoria, auto específico. Fecha y contenido
3. **Oportunidad del recurso** — fundamentar que se interpone dentro del plazo legal (Arts. 1336-1340 Código de Comercio para mercantil; código procesal aplicable para civil)
4. **Agravios** — cada agravio numerado, con esta estructura:
   - **La resolución recurrida dice** — citar con precisión qué resolvió el juzgador en el punto impugnado
   - **El agravio** — en qué consiste la violación (indebida aplicación, falta de aplicación, violación de formalidades esenciales del procedimiento, valoración incorrecta de pruebas, incongruencia)
   - **Fundamento legal violado** — artículo(s) específico(s) que el juzgador debió aplicar o aplicó indebidamente
   - **Argumentación** — por qué la resolución es contraria a derecho. Vincular con las constancias del expediente
   - **Jurisprudencia aplicable** — criterios que sostienen la posición del apelante
5. **Puntos petitorios** — "POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, AL H. TRIBUNAL DE ALZADA, ATENTAMENTE PIDO SE SIRVA:" + revocar/modificar la resolución recurrida

**Un agravio genérico es inoperante.** "El juez violó la ley" no es un agravio. Cada agravio debe identificar: la parte específica de la resolución que se impugna, la norma concreta violada, y la argumentación de por qué es contraria a derecho.

**Tipos de agravios más frecuentes:**
- **Indebida valoración de pruebas** — el juzgador valoró una prueba en contravención del sistema de valoración aplicable (tasado o libre)
- **Falta de aplicación de ley** — el juzgador omitió aplicar una norma que debió gobernar el caso
- **Indebida aplicación de ley** — el juzgador aplicó una norma que no correspondía a los hechos probados
- **Violación a formalidades esenciales del procedimiento** — se privó al apelante de su derecho de defensa (falta de emplazamiento, falta de oportunidad probatoria, incongruencia entre lo pedido y lo resuelto)
- **Incongruencia de la sentencia** — la sentencia no resuelve todos los puntos litigiosos (citra petita), resuelve más de lo pedido (ultra petita), o resuelve cosas no pedidas (extra petita)

---

## Cobertura de extracción de citas

Cuando este borrador sea revisado — por ti, por otro skill, o por un revisor —, la verificación debe ser exhaustiva, no selectiva:

1. **Primera pasada: extraer.** Leer todo el escrito y construir una lista de cada cita — leyes, artículos, tesis, jurisprudencia, referencias al expediente. Reportar la cuenta: "Encontradas [N] citas."
2. **Segunda pasada: verificar.** Verificar cada una contra la fuente. No muestrear. No detenerse.
3. **Reportar cobertura.** Al final: "Verificadas [N] de [M] citas. [K] no pudieron recuperarse — verificar manualmente. [J] confirmadas. [I] señaladas como posibles citas erróneas. [H] señaladas como parcialmente fundamentadas (la cita existe pero no soporta la proposición)."
4. **Cuando el texto fuente no está disponible, decir "no pude verificar," nunca "confirmada."**
5. **Los errores más difíciles son de fundamentación parcial.** Una cita que respalda parte de un argumento pero no todo. Leer la proposición del escrito, leer lo que la autoridad realmente dice, y comparar elemento por elemento.

## Verificación previa de conectores de investigación

Antes de iniciar la redacción que requiera citas de autoridad, verificar si un conector de investigación (SCJN IUS, Semanario Judicial de la Federación, DOF, o herramienta MCP configurada) está respondiendo, no solo configurado. Si ninguno responde, registrarlo en la línea **Fuentes:** de la nota de revisión — ej., `no conectado — citas de conocimiento del modelo, verificar antes de confiar`. No emitir un banner separado. La nota de revisión es el lugar único para esta señal; las etiquetas `[conocimiento del modelo — verificar]` por cita se mantienen en línea.

## Registro de verificación

Cuando tú o el usuario verifiquen un elemento señalado — confirmen una cita contra fuente primaria, verifiquen un plazo contra el código procesal, confirmen una tesis en SCJN IUS —, registrarlo para que nadie re-verifique. Escribir una línea en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/verification-log.md`:

`[AAAA-MM-DD] [cita o hecho] verificado por [nombre] contra [fuente] — [resultado: confirmado / corregido a X / no pude verificar]`

Cuando un elemento señalado ya está en el registro de verificación y tiene menos de [la ventana de frescura relevante], la nota de revisión dice: "Previamente verificado por [nombre] el [fecha] contra [fuente]."

## Verificación de destino

Antes de producir el resultado, verificar a dónde va. Si el usuario ha nombrado un destino (un canal, una lista, una contraparte), preguntar si está dentro del círculo de confidencialidad. El escrito judicial se presenta ante un tribunal y por tanto es público; pero las notas de redacción, la estrategia y las observaciones al abogado titular son producto de trabajo interno protegido por el secreto profesional. Tratar cada pieza según su naturaleza.

## Hechos — advocacy a través de la selección

Los hechos de una demanda o contestación son advocacy a través de la selección y la secuencia, no argumentación directa.

- Cronológicos salvo que haya razón para otro orden
- **Cada hecho debe citar al expediente o documento soporte** — foja, documento, fecha, exhibición. "O reconocido" no sustituye una referencia documental. Si el hecho se establece por reconocimiento o confesión de la contraparte, citar el acta, escrito o audiencia donde consta.
- Encuadrar a través de la selección: qué hechos abren, cuáles reciben una línea, cuáles se omiten (si no son necesarios ni útiles)
- No argumentar en los hechos. "El contrato inequívocamente exige X" es argumento. "El contrato establece en su Cláusula 4.2: 'X.'" es hecho.

## Argumentos jurídicos — especificidades

- Abrir con la norma aplicable, luego vincular con los hechos (salvo que el estilo de casa diga lo contrario)
- Un argumento por sección. Si realmente son dos argumentos, son dos secciones.
- Abordar el mejor contraargumento de la contraparte. No evitarlo — un escrito que ignora el contraargumento obvio es un escrito en el que el juzgador no confía.
- Las citas de jurisprudencia y tesis ganan su espacio. Si una tesis no agrega algo que la ley por sí sola no dice, eliminarla. Citar jurisprudencia para proposiciones evidentes diluye el impacto de las citas que sí importan.

## Códigos procesales de referencia

Este skill redacta escritos bajo los siguientes ordenamientos procesales. El abogado confirma cuál aplica; el skill no asume:

| Código | Ámbito | Artículos clave para escritos |
|---|---|---|
| Código de Comercio (Libro Quinto) | Juicios mercantiles | Arts. 1049-1414 — competencia, demanda, contestación, pruebas, alegatos, sentencia |
| CFPC (Código Federal de Procedimientos Civiles) | Procedimientos civiles federales | Arts. 1-427 — supletorio al Código de Comercio |
| CNPCF (Código Nacional de Procedimientos Civiles y Familiares) | Procedimientos civiles y familiares | Armonización procesal nacional — verificar entrada en vigor por entidad `[INCIERTO — verificar vigencia estatal]` |
| Ley Federal del Trabajo | Procedimiento laboral | Arts. 684-A y ss. (nuevo sistema); Arts. 870-891 (procedimiento ordinario anterior) |
| Ley de Amparo | Juicio de amparo | Título II (amparo indirecto); Título III (amparo directo) |

**El CNPCF es de implementación gradual.** No todas las entidades federativas lo han implementado. Verificar si el foro específico ya opera bajo el CNPCF o sigue con el código procesal estatal anterior antes de fundamentar en él.

## Lo que este skill NO hace

- **Producir un escrito final.** Produce un borrador. Cada cita necesita verificación, cada argumento necesita los ojos del abogado titular.
- **Decidir estrategia.** Si hay dos formas de plantear la acción o de estructurar los conceptos de violación, señalar ambas y dejar que el abogado decida.
- **Presentar nada.** Nunca. La presentación ante el juzgado es acto exclusivo del abogado.
- **Inventar jurisprudencia o tesis.** Si no se localiza la tesis que se necesita, dejar `[CITA NECESARIA]` — no fabricar un registro digital o una clave de tesis.
- **Aplicar derecho extranjero.** Este skill redacta escritos para tribunales mexicanos bajo derecho mexicano. Si los hechos tocan otra jurisdicción, señalarlo y detener la redacción en ese punto.
- **Omitir los puntos petitorios.** Todo escrito judicial mexicano cierra con puntos petitorios. Un escrito sin puntos petitorios está incompleto.
- **Sustituir al abogado en audiencia.** El skill prepara escritos; lo que ocurre en audiencia (repreguntas, incidentes orales, desahogo de pruebas) es competencia exclusiva del abogado.
- **Opinar sobre la competencia del juzgador.** Si hay duda sobre si el juzgado es competente por materia, cuantía, territorio o grado, señalarlo como `[VERIFICAR: competencia del juzgador — [razón de la duda]]` y dejar que el abogado resuelva. La incompetencia es excepción que la contraparte puede oponer y el juzgador puede declarar de oficio.
