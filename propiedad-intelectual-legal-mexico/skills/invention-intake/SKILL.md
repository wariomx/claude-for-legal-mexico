---
description: >
  Evaluación de primera pasada de invención — novedad, actividad inventiva,
  exclusiones de patentabilidad (Art. 4 LFPPI), divulgación pública, plazos
  de gracia, detectabilidad, valor estratégico, y clasificación de invención
  de empleado (LFT Art. 163). Usa cuando llega una divulgación de invención y
  necesita triaje sobre si amerita búsqueda de arte previo y revisión por
  abogado de patentes, investigar más, o declinar. Incluye rutas alternativas:
  modelo de utilidad, secreto industrial, y patente provisional (LFPPI 2026).
---

# /invention-intake

**Esta es una evaluación de primera pasada por un no especialista, no un
dictamen de patentabilidad.** La evaluación nunca concluye que una invención es
patentable — concluye que pasa la evaluación inicial y amerita una búsqueda de
arte previo y revisión por un practicante registrado, que necesita más
información, o que tiene un descalificador. Una búsqueda de arte previo es un
paso separado; este skill no la hace.

## Instrucciones

1. Leer `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`. Si
   contiene `[PLACEHOLDER]`, detenerse y dirigir a `/propiedad-intelectual-legal-mexico:cold-start-interview`. Si
   el perfil de práctica muestra solo marcas o solo derechos de autor (sin
   práctica de patentes), decirlo y enrutar al usuario — esta es la herramienta
   equivocada.
2. Seguir el flujo de trabajo abajo.
3. Ejecutar intake. Si el usuario pegó o subió una divulgación, leerla. Si no,
   hacer las preguntas de intake (qué / problema / diferencias / inventores /
   divulgación pública / estatus / área tecnológica / relación laboral) en un
   solo lote y esperar.
4. **Ejecutar la clasificación de titularidad de invención de empleado (LFT
   Art. 163) ANTES de las evaluaciones de patentabilidad.** Si la empresa no
   tiene derecho a solicitar la patente, el resto de las evaluaciones son
   irrelevantes hasta resolver la titularidad.
5. Ejecutar las seis evaluaciones: señales de novedad, señales de obviedad,
   exclusiones de patentabilidad (Art. 4 LFPPI), divulgación pública / plazos
   de gracia, detectabilidad, valor estratégico. Cada evaluación recibe un
   veredicto ✓ / 🟡 / 🔴 con razonamiento de una línea.
6. Escribir el memorándum de evaluación de invención en la carpeta del asunto
   (si hay un asunto activo) o la carpeta de resultados de la práctica. Aplicar
   el encabezado de confidencialidad conforme al rol.
7. Veredicto de conclusión: **PERSEGUIR** (agendar búsqueda de arte previo y
   revisión por abogado — incluir ruta recomendada: patente de invención,
   modelo de utilidad, o ambas) / **INVESTIGAR** (necesita más información
   sobre un punto abierto específico) / **DECLINAR** (declarar la razón
   concreta) / **RUTA ALTERNATIVA** (secreto industrial). Nunca decir
   "patentable."
8. Cerrar con el árbol de decisión (búsqueda de arte previo / seguimiento con
   inventor / revisión por especialista / declinar + agradecimiento / ruta de
   secreto industrial / ruta de modelo de utilidad) y la puerta para no
   abogados si el rol es no abogado.
9. Si la evaluación detecta una divulgación pública dentro del año de gracia
   (Art. 18 LFPPI `[model knowledge — verify]`) o cualquier divulgación pública
   con derechos extranjeros en alcance, señalar al inicio: **urgente**.

Este skill nunca concluye que una invención es patentable. Si hay
incertidumbre, señalar — un abogado de patentes calificado decide.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:invention-intake "un nuevo algoritmo de evicción de caché que usa un modelo aprendido en lugar de LRU; concebido en Q1 de este año, no divulgado aún, prototipo en staging interno"
```

```
/propiedad-intelectual-legal-mexico:invention-intake
```

(Y el skill preguntará por la invención, el problema que resuelve, cómo difiere,
inventores, estatus de divulgación pública, estatus de uso, área tecnológica, y
relación laboral.)

---

## ESTA ES UNA EVALUACIÓN DE PRIMERA PASADA, NO UN DICTAMEN DE PATENTABILIDAD

**Decir esto al inicio de cada resultado. No omitirla, no suavizarla.**

> **Esta es una evaluación de primera pasada por un no especialista, no un
> dictamen de patentabilidad.** Un dictamen de patentabilidad requiere una
> búsqueda de arte previo, construcción completa de reivindicaciones, y el
> juicio de un abogado de patentes calificado. Esta evaluación no hace una
> búsqueda de arte previo, no evalúa qué hay en el estado de la técnica, y no
> construye reivindicaciones. Evalúa los descalificadores obvios (la invención
> ya está en el mercado, se divulgó públicamente hace dos años, es claramente
> materia excluida del Art. 4 LFPPI) y los go-aheads obvios (mecanismo nuevo,
> avance técnico, concepción reciente, uso secreto). Todo lo intermedio necesita
> una búsqueda de arte previo y revisión de un practicante registrado. Esta
> evaluación nunca concluye que algo es "patentable" — concluye que "pasa la
> evaluación inicial, amerita investigación" o que no.

Sub-señalar una invención que debió haberse presentado es una puerta de un solo
sentido — el plazo de gracia de 12 meses corre, los derechos extranjeros se
pierden con la primera divulgación pública, el competidor presenta primero.
Sobre-señalar solo significa una búsqueda de arte previo que regresa vacía.
Mantenerse del lado de la puerta de dos sentidos.

---

## Contexto de asunto

**Contexto de asunto.** Verificar `## Espacios de trabajo por asunto` en el
CLAUDE.md a nivel de práctica. Si `Habilitado` es `✗` (el valor por defecto
para usuarios de jurídico interno), omitir el resto de este párrafo — los
skills usan contexto a nivel de práctica y la maquinaria de asuntos es
invisible. Si está habilitado y no hay asunto activo, preguntar: "¿Para qué
asunto es esto? Ejecuta `/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` o di `nivel de
práctica`." Cargar el `matter.md` del asunto activo para contexto y
sobrescrituras específicas. Escribir resultados en la carpeta del asunto en
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<slug>/`.
Nunca leer archivos de otro asunto a menos que `Contexto entre asuntos` esté
activo.

Las divulgaciones de invención son particularmente candidatas comunes para
confidencialidad **reforzada** al abrir el asunto. Respetar la marca de
confidencialidad del asunto en `matter.md`. El contenido de la invención es
inherentemente sensible — no resumir, citar ni referenciar fuera de canales
confidenciales.

---

## Cargar el perfil de práctica primero

**Antes de leer la divulgación, leer
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.** Si no existe o
aún contiene placeholders, detenerse y ejecutar `/propiedad-intelectual-legal-mexico:cold-start-interview`. El
perfil de práctica indica:

- La **estrategia de presentación de patentes** de la empresa — ofensiva
  (construir portafolio de aserción), defensiva (presentar para proteger
  libertad de operación), híbrida, o licenciamiento. Esto determina el umbral
  de valor estratégico.
- Las **áreas tecnológicas de interés** — dónde la empresa presenta y dónde no.
  Una invención fuera de las áreas de interés frecuentemente es un declinar aun
  si la evaluación técnica está limpia.
- La **postura presupuestal de presentación** — agresiva (presentar todo lo que
  pase la evaluación), selectiva (presentar las mejores pocas), o mínima (solo
  lo que el negocio necesita proteger). Esto moldea la recomendación del
  resultado.
- La **cadena de aprobación** — quién aprueba una decisión de presentación, y a
  quién se enruta la invención si pasa la evaluación.
- La **política interna de cesión de invenciones** de `## Inventos de
  empleados` — cómo se clasifican los inventos y si existen cláusulas de cesión
  en contratos laborales.

Si el perfil de práctica muestra solo marcas o solo derechos de autor (sin
práctica de patentes), este skill es la herramienta equivocada — decirlo y
enrutar al usuario.

---

## Flujo de trabajo

### Paso 1: Recibir la divulgación

Si el usuario pega o sube una divulgación, leerla. Si no, preguntar — en un
solo lote, no una a la vez:

> Para evaluar esto, necesito:
>
> 1. **¿Qué es la invención?** En lenguaje llano — qué hace, qué la hace
>    funcionar, cuál es la idea clave.
> 2. **¿Qué problema resuelve?** Qué estaba roto o faltaba antes.
> 3. **¿Cómo difiere de lo que existía antes?** ¿Qué hacía la gente
>    previamente? ¿Qué hace esto de diferente?
> 4. **¿Quién la inventó, y cuándo?** Nombres y fecha aproximada de concepción.
> 5. **¿Ha sido divulgada públicamente?** Publicada, vendida, ofrecida en venta,
>    demostrada en una conferencia, mostrada a un cliente bajo NDA, publicada en
>    un repositorio público, escrita en un artículo, incluida en notas de
>    liberación de producto. Si sí, cuándo y dónde.
> 6. **¿Está en uso o es planeada?** ¿En producción ahora? ¿En piloto limitado?
>    ¿En el roadmap? ¿Aún en papel?
> 7. **¿Qué área tecnológica?** (Software, hardware, mecánica, biotecnología,
>    método de negocio, IA/ML, etc.)
> 8. **¿Cuál es la relación laboral de los inventores con la empresa?**
>    ¿Fueron contratados específicamente para investigar/inventar? ¿Usaron
>    recursos, datos, instalaciones o materiales de la empresa? ¿O la invención
>    es ajena a la actividad de la empresa y se realizó sin sus recursos?

Esperar las respuestas. No proceder con media divulgación — una evaluación de
"una nueva cosa de machine learning que ayuda a los usuarios" es peor que
ninguna evaluación.

Si la divulgación es un formulario de divulgación de invención (IDF) formal de
un IPMS o una plantilla, extraer estos campos del formulario y solo preguntar
lo que falta.

### Paso 2: Clasificación de titularidad — Inventos de empleados (LFT Art. 163)

**Esta clasificación es obligatoria y se ejecuta ANTES de las evaluaciones de
patentabilidad.** Si la empresa no tiene derecho a solicitar la patente, la
evaluación de patentabilidad es irrelevante hasta resolver la titularidad.

Clasificar la invención conforme al Art. 163 de la Ley Federal del Trabajo
`[model knowledge — verify]`:

#### Invento de empresa (Art. 163 Fr. I)

**Criterio:** El trabajador fue contratado específicamente para investigar o
realizar trabajos de invención.

**Consecuencia:** La propiedad de la invención corresponde al patrón. El
trabajador tiene derecho a:
- Ser reconocido como inventor (derecho moral — inalienable)
- Compensación complementaria si el invento supera las expectativas razonables
  del contrato de trabajo

**Señales:**
- Contrato laboral expresamente menciona investigación/invención como objeto
- Descripción de puesto incluye I+D, innovación, desarrollo de producto
- El trabajador está asignado a un laboratorio, centro de investigación, o
  equipo de I+D

**Veredicto:** ✓ La empresa puede solicitar la patente como titular.

#### Invento del trabajador (Art. 163 Fr. II)

**Criterio:** La invención se realizó con recursos, datos, instalaciones o
materiales del patrón, PERO el trabajador no fue contratado específicamente
para inventar.

**Consecuencia:** La propiedad es del TRABAJADOR. Sin embargo, el patrón tiene
**derecho preferente** a explotar la patente/registro, pagando al trabajador
una compensación.

**Señales:**
- El trabajador usó equipo de la empresa, pero su puesto no es de I+D
- La invención surgió como "efecto colateral" de su trabajo regular
- Se usaron datos o información de la empresa

**Veredicto:** 🟡 La empresa NO es titular automático. Tiene derecho
preferente de explotación, pero debe negociar compensación. Señalar para
revisión jurídica — ¿existe cláusula de cesión en el contrato laboral? ¿La
cláusula de cesión es válida bajo LFT? `[review]`

#### Invento libre (Art. 163 Fr. III)

**Criterio:** La invención es ajena a la actividad del patrón y se realizó sin
recursos, datos, instalaciones o materiales del mismo.

**Consecuencia:** La propiedad es exclusiva del trabajador. El patrón no tiene
ningún derecho sobre la invención.

**Señales:**
- La invención no tiene relación con el giro de la empresa
- Se desarrolló en tiempo personal, con recursos propios
- No se usó información confidencial de la empresa

**Veredicto:** 🔴 La empresa NO tiene derecho a solicitar esta patente. Si
se desea adquirir el derecho, se requiere un convenio de cesión separado con
contraprestación.

---

**Presentar la clasificación como un bloque antes de las evaluaciones:**

```
## Clasificación de titularidad — LFT Art. 163

**Clasificación:** [Invento de empresa / Invento del trabajador / Invento libre]
**Base:** [razonamiento de 2-3 oraciones]
**Política interna:** [conforme a ## Inventos de empleados del perfil — existe
cláusula de cesión: sí/no/desconocido]

**Implicación para esta evaluación:**
- [✓ La empresa puede solicitar como titular / 🟡 Derecho preferente — resolver
  compensación antes de presentar / 🔴 Sin derecho — requiere cesión separada]
```

**Si la clasificación es "Invento libre" (🔴):** Detenerse y señalar que la
evaluación de patentabilidad no procede para la empresa hasta que se negocie y
formalice un convenio de cesión con el inventor. Ofrecer continuar la evaluación
técnica si el usuario lo desea (para informar la negociación del convenio), pero
dejar claro que la empresa no puede presentar sin resolver la titularidad.

**Si la clasificación es "Invento del trabajador" (🟡):** Señalar que se debe
resolver la cuestión de compensación y derecho preferente antes de presentar.
Continuar con la evaluación técnica marcando que la titularidad está pendiente
de resolución. `[review]`

**Si la clasificación es ambigua:** Señalar los factores que cortan en ambas
direcciones y marcar para revisión jurídica laboral. Considerar enrutar a
`/corporativo-legal-mexico:revision-contratos` (si está instalado) para
revisión de las cláusulas laborales relevantes.

### Paso 3: Evaluar contra el checklist

Recorrer las seis evaluaciones en orden. Cada una produce un veredicto por
evaluación: `✓ limpio`, `🟡 señalado — necesita mayor análisis`, o `🔴
bandera roja`. Explicar el razonamiento brevemente; no rellenar.

#### Evaluación 1: Señales de novedad

¿La divulgación describe algo nuevo? Esta no es un análisis de novedad completo
— eso requiere una búsqueda de arte previo. Esto evalúa la propia descripción
de la divulgación por problemas de novedad auto-evidentes.

**Banderas rojas (🔴):**
- "Solo aplicamos [técnica conocida] a [nuevo dominio]" — ej., "tomamos
  gradient boosting y lo aplicamos a predecir churn de clientes"
- "Es como [producto existente] pero para [X]" — encuadre de "Uber-para-X"
- "Los competidores hacen algo similar" — si la propia divulgación dice esto,
  la novedad está en cuestión
- La divulgación describe una funcionalidad de un producto público existente
  con afinación menor

**Señales verdes (✓):**
- Un nuevo **mecanismo** — una nueva manera de hacer la cosa, no una nueva
  aplicación
- Una nueva **combinación** que produce un resultado inesperado (no solo aditivo
  — "más rápido," "más pequeño," "más barato" a veces son inesperados, a veces
  obvios)
- Resuelve un problema que el campo **no había resuelto** — la divulgación
  explica por qué los enfoques previos fallaron y cómo este no

**Señalado (🟡):** cualquier cosa ambigua. La búsqueda de arte previo lo
resuelve.

#### Evaluación 2: Señales de obviedad (actividad inventiva)

¿Una persona versada en la materia habría llegado a esta combinación basándose
en lo conocido? Esto es una evaluación, no un análisis de actividad inventiva
bajo LFPPI Art. 13 `[model knowledge — verify]` — señalar para mayor
investigación, nunca concluir obviedad o no obviedad.

**Banderas rojas (🔴) para mayor investigación:**
- Combinar **elementos conocidos de manera predecible** — poner un sensor
  conocido en una máquina conocida para medir algo conocido
- **Optimización de rutina** — "ajustamos el parámetro existente de X a Y y
  obtuvimos mejores resultados"
- **Elección de diseño sin ventaja funcional** — cambios estéticos,
  ergonómicos o estilísticos que no cambian cómo funciona la cosa
- **Obvio de probar** — una de un número pequeño de soluciones identificadas
  con expectativa razonable de éxito

**Señales verdes (✓):**
- Enseñanza en contra (teaching away) — el arte previo esperaba el resultado
  opuesto o dijo que este enfoque no funcionaría
- Resultado inesperado — la combinación produce algo que la persona versada no
  habría predicho
- Necesidad largamente sentida — el problema era conocido, y los intentos de
  resolverlo habían fallado

#### Evaluación 3: Exclusiones de patentabilidad (Art. 4 LFPPI)

¿La invención cae en la lista de exclusiones del Art. 4 de la LFPPI? En
México, a diferencia de EE.UU. (donde la prueba Alice/Mayo es una evaluación de
dos pasos sobre materia "abstracta"), las exclusiones son una **lista cerrada
de categorías** `[model knowledge — verify]`. La evaluación es más simple en
forma pero con bordes más afilados.

**Categorías excluidas (🔴 si la invención cae claramente en una):**

- **Descubrimientos, teorías científicas, métodos matemáticos** — hechos de la
  naturaleza, no invenciones
- **Esquemas, planes, reglas y métodos para realizar actos mentales, juegos, o
  negocios** — métodos de negocio puros no son patentables en México
- **Programas de computación** (software) ***per se*** — esta es una exclusión
  importante. El software NO es patentable por sí solo en México. PERO: si la
  invención es un proceso técnico implementado por software que produce un
  efecto técnico más allá del funcionamiento normal de la computadora, PUEDE
  ser patentable. La frontera es difusa y requiere revisión por especialista
  `[review]`
- **Formas de presentar información** — interfaces puras, formatos de
  visualización
- **Métodos de tratamiento terapéutico, quirúrgico o de diagnóstico aplicables
  al cuerpo humano o animal** — excluidos expresamente
- **Material biológico tal como se encuentra en la naturaleza** — incluye genes
  aislados, microorganismos como se encuentran en la naturaleza
- **Razas animales y procesos esencialmente biológicos para obtener variedades
  vegetales** — enrutar a la Ley Federal de Variedades Vegetales

**Señales verdes (✓) para invenciones de software/IA:**
- Mejora técnica al **equipo de cómputo mismo** — nueva arquitectura, nueva
  técnica de entrenamiento, nueva interfaz hardware/software, nuevo mecanismo
  de seguridad
- **Medio técnico específico**, no solo resultados
- Mejora a un **campo técnico** (procesamiento de imagen, compresión,
  criptografía, robótica) con los medios técnicos descritos
- El software es una **herramienta** para lograr un resultado técnico, no el
  resultado en sí

**Cualquier cosa en la frontera recibe un 🟡 con "Art. 4 LFPPI — enrutar a
especialista para análisis de exclusión."** Un no especialista no debe decidir
una cuestión cercana de exclusión.

> **Las exclusiones difieren por jurisdicción.** La OEP (Art. 52 EPC) aplica una
> prueba de "efecto técnico" materialmente más permisiva para software e IA que
> la lista del Art. 4 LFPPI. JPO y CNIPA también aplican estándares diferentes.
> EE.UU. aplica la prueba Alice/Mayo de dos pasos. Una invención que evalúa 🔴
> bajo Art. 4 LFPPI puede ser perfectamente elegible en EPO/JPO/CNIPA/USPTO.
>
> Cuando el perfil de práctica incluye jurisdicciones fuera de México: "Esta
> evaluación bajo Art. 4 es específica de México. Si presentas internacionalmente,
> la postura de elegibilidad puede ser diferente — particularmente para software,
> IA/ML y métodos de negocio, donde EPO es más permisiva y USPTO aplica Alice.
> No declinar basándose solo en el Art. 4 LFPPI si tienes planes de presentación
> en EP/US/JP/CN."

#### Evaluación 4: Divulgación pública / plazos de gracia

¿La invención ha sido divulgada, vendida, ofrecida en venta, o usada
públicamente? Esta es la evaluación más sensible al tiempo — la respuesta puede
matar la patentabilidad de manera absoluta, o iniciar un reloj que no puede
detenerse.

Categorizar el estatus de divulgación:

**🔴 Probablemente imposibilitada:**
- Divulgada públicamente, vendida u ofrecida en venta por el **inventor o su
  causahabiente** hace **más de 12 meses** en México — el periodo de gracia del
  Art. 18 LFPPI `[model knowledge — verify]` ha corrido
- Divulgada por un **tercero** (no el inventor) antes de la fecha de solicitud
  — la novedad se destruye sin periodo de gracia
- **Cualquier** divulgación pública, en cualquier lugar, antes de presentar —
  barra de novedad absoluta en la UE, China, Japón, y la mayoría de los países
  fuera de México. Si el negocio le importan los derechos extranjeros, esto es
  potencialmente fatal aun si México sigue abierto.

**🟡 El reloj está corriendo:**
- Divulgada públicamente por el inventor dentro de los últimos 12 meses — el
  plazo de gracia mexicano bajo Art. 18 LFPPI está corriendo, derechos
  extranjeros pueden ya estar perdidos. Urgente. Confirmar la fecha de
  divulgación y enrutar a presentación inmediatamente.

**✓ Limpio:**
- Sin divulgación pública. Demostraciones confidenciales a clientes bajo NDA,
  uso interno, versiones beta a partes nombradas bajo NDA, borradores de
  artículos no enviados — usualmente no "públicas" para fines de novedad, pero
  depende de los hechos. Cuando la divulgación fue a un cliente o parte externa,
  incluso bajo NDA, señalar los detalles específicos para que el equipo de
  trámite los evalúe.

**Preguntar específicamente sobre:**
- Artículos enviados a revistas o conferencias (envío ≠ publicación; pero
  verificar la política de la revista y si se publicaron preprints)
- Pláticas en conferencias, meetups, eventos internos de la empresa abiertos a
  no empleados
- Posts en repositorios públicos, blogs, redes sociales, o foros
- Liberaciones de producto, incluso en beta limitada
- Actividad de venta incluyendo cotizaciones, respuestas a RFP, y ofertas en
  venta
- Divulgaciones a inversionistas o consejeros que no están bajo NDA

La **barra de oferta en venta** captura ofertas en venta de un producto que
incorpora la invención, no solo ventas completadas. Una respuesta a RFP que
describe la invención puede detonarla.

**Periodo de gracia en México vs. otros países:**
- **México:** 12 meses de gracia para divulgación por el inventor o su
  causahabiente (Art. 18 LFPPI `[model knowledge — verify]`). Solo aplica si
  fue divulgada por el propio inventor.
- **EE.UU.:** 12 meses de gracia (35 USC § 102(b))
- **UE/JP/CN/mayoría:** Sin gracia o gracia muy limitada. Novedad absoluta.
  Cualquier divulgación antes de solicitud destruye novedad.

#### Evaluación 5: Detectabilidad

Si un competidor infringiera esta invención, ¿podrías darte cuenta? Una
invención que se practica en secreto — procesamiento del lado del servidor,
operaciones de back-office, técnicas de manufactura interna — puede estar mejor
protegida como **secreto industrial** que como patente. Publicar una patente
sobre una invención indetectable es regalar a los competidores la invención a
cambio de un activo que nunca puedes hacer valer.

**🔴 Señales de baja detectabilidad:**
- Algoritmo del lado del servidor sin patrón de salida observable
- Proceso de manufactura interna (ej., un paso novedoso en un proceso de
  fabricación)
- Metodología de pipeline de datos o analítica que ocurre dentro de la
  infraestructura del competidor
- Composición de datos de entrenamiento o técnica de entrenamiento para un
  modelo de ML — visible solo a través de sondeo detallado, si acaso

Para estos, señalar la **decisión patente-vs-secreto-industrial.** La pregunta
no es "¿es patentable?" sino "¿deberíamos patentarla si pudiéramos?" Enrutar a
quien en el perfil de práctica posee las decisiones de clasificación de secreto
industrial.

**Protección como secreto industrial bajo LFPPI Título Quinto:**
Los secretos industriales bajo la LFPPI `[model knowledge — verify]` requieren:
- La información debe ser secreta (no generalmente conocida ni fácilmente
  accesible)
- Debe tener valor comercial por ser secreta
- Se deben haber tomado medidas razonables para mantenerla secreta
  (acuerdos de confidencialidad, controles de acceso, políticas internas)

La protección es indefinida (mientras se mantenga secreta) vs. 20 años para
patente o 15 años para modelo de utilidad. Si la detectabilidad es baja y la
invención puede mantenerse secreta, el secreto industrial puede ser el activo
de mayor valor.

**✓ Alta detectabilidad:**
- Producto de consumo — visible en el producto
- API publicada, SDK, protocolo — visible en tráfico de red o documentación de
  integración
- Mecanismo físico en un producto distribuido — susceptible de ingeniería
  inversa
- Código compilado con firmas distintivas en un binario distribuido

#### Evaluación 6: Valor estratégico

¿Se alinea esto con la estrategia de patentes de la empresa según el perfil de
práctica? Aquí es donde la evaluación se vuelve específica de la empresa en
lugar de doctrinal.

Verificar contra el perfil:

- **Estrategia ofensiva (construir para hacer valer):** ¿este activo es digno
  de aserción? Una patente estrecha, fácilmente evadible con diseño alternativo,
  tiene menor valor ofensivo que una reivindicación de mecanismo amplia. ¿El
  panorama competitivo es uno donde querrías demandar?
- **Estrategia defensiva (construir para proteger FTO):** ¿esto cubre un área
  tecnológica donde los competidores están presentando? Una presentación
  defensiva en un área donde nadie presenta es un gasto desperdiciado.
- **Estrategia de licenciamiento / ingresos:** ¿es licenciable? ¿Quién pagaría
  por ello, y bajo qué circunstancias?

También verificar:

- ¿Es tecnología **núcleo** (parte de la diferenciación del producto) o
  **periférica** (incidental a una funcionalidad secundaria)? Núcleo vale más.
- ¿Cuál es el **panorama competitivo**? Alto en patentes (semiconductores,
  farmacéutica) — presentar temprano o perder la carrera. Bajo en patentes
  (muchos segmentos de software de código abierto) — a veces omitir
  completamente y gastar el dinero en otro lado.
- ¿El área tecnológica está en la lista de **áreas tecnológicas de interés** de
  la empresa según el perfil de práctica? Si no, frecuentemente es un declinar
  independientemente de la doctrina.

### Paso 4: Evaluar ruta de protección recomendada

Además de la evaluación de patentabilidad como patente de invención, evaluar
explícitamente si un **modelo de utilidad** es una ruta apropiada:

**Modelo de utilidad — cuándo considerar:**
- La invención es un **objeto, utensilio, aparato o herramienta** (no un
  proceso — los modelos de utilidad no cubren procesos)
- Es una **innovación incremental** — mejora una cosa existente en vez de ser
  radicalmente nueva
- El **umbral de actividad inventiva es potencialmente bajo** — la invención
  puede no superar el estándar pleno de patente de invención, pero el umbral
  reducido del modelo de utilidad puede alcanzarse
- Se desea **protección más rápida** — el trámite de modelo de utilidad es
  generalmente más rápido ante IMPI
- La vigencia de **15 años** (vs. 20 de patente) es aceptable para el ciclo
  de vida del producto

**Presentar las rutas como opciones en el veredicto:**
- **Patente de invención:** 20 años, examen completo, productos y procesos
- **Modelo de utilidad:** 15 años, examen simplificado, solo objetos/dispositivos
- **Ambas:** presentar solicitud de patente y, si se rechaza por falta de
  actividad inventiva plena, convertir a modelo de utilidad (o presentar ambas
  en paralelo)
- **Secreto industrial:** protección indefinida, sin registro, requiere medidas
  de protección
- **Patente provisional (LFPPI 2026):** nuevo mecanismo que establece fecha de
  prioridad sin examen de fondo inmediato `[model knowledge — verify]` — útil
  para asegurar fecha mientras se completa la evaluación

**Estrategia PCT / Convenio de París desde México:**
Si el perfil de práctica incluye jurisdicciones internacionales, anotar:
- **Convenio de París:** 12 meses de prioridad desde la solicitud mexicana para
  presentar en otros países
- **PCT:** solicitud internacional que designa múltiples jurisdicciones, con
  fase nacional típicamente a los 30-31 meses
- **Provisional LFPPI 2026** como base para reclamar prioridad internacional
  `[model knowledge — verify]`

### Paso 5: Ensamblar el memorándum de evaluación de invención

Formato:

> **Memorándum de evaluación de invención — [título de la invención]**
>
> **Conclusión: [PERSEGUIR / INVESTIGAR / DECLINAR / RUTA ALTERNATIVA]**
>
> *[Una oración — la razón en lenguaje llano.]*
>
> **Ruta de protección recomendada:** [Patente de invención / Modelo de
> utilidad / Ambas / Secreto industrial / Patente provisional + evaluación
> posterior]
>
> ---
>
> ### Clasificación de titularidad — LFT Art. 163
>
> **Clasificación:** [Invento de empresa / Invento del trabajador / Invento
> libre]
> **Base:** [razonamiento]
> **Implicación:** [la empresa puede/no puede solicitar como titular]
>
> ---
>
> ### Resultados de evaluación
>
> | Evaluación | Veredicto | Notas |
> |---|---|---|
> | Novedad | [✓ / 🟡 / 🔴] | [razonamiento de una línea] |
> | Actividad inventiva | [✓ / 🟡 / 🔴] | [razonamiento de una línea] |
> | Exclusiones Art. 4 LFPPI | [✓ / 🟡 / 🔴] | [razonamiento de una línea] |
> | Divulgación pública / plazos | [✓ / 🟡 / 🔴] | [razonamiento + fechas] |
> | Detectabilidad | [✓ / 🟡 / 🔴] | [razonamiento de una línea] |
> | Valor estratégico | [✓ / 🟡 / 🔴] | [razonamiento, referido al perfil] |
>
> ---
>
> ### Rutas de protección
>
> | Ruta | Viabilidad | Notas |
> |---|---|---|
> | Patente de invención (IMPI) | [✓ / 🟡 / 🔴] | [razonamiento breve] |
> | Modelo de utilidad (IMPI) | [✓ / 🟡 / N/A] | [razonamiento — N/A si es proceso] |
> | Secreto industrial (LFPPI) | [✓ / 🟡 / 🔴] | [razonamiento] |
> | Patente provisional (LFPPI 2026) | [✓ / 🟡 / N/A] | [razonamiento `[model knowledge — verify]`] |
> | PCT / Convenio de París | [✓ / N/A] | [si hay jurisdicciones internacionales en perfil] |
>
> ---
>
> ### Preguntas abiertas
>
> *Cosas que cambiarían la respuesta. El inventor, el equipo de trámite, o un
> especialista necesitaría abordarlas antes de que esta evaluación se convierta
> en una decisión de presentación.*
>
> - [pregunta]
> - [pregunta]
>
> ### Siguientes pasos (árbol de decisión)
>
> Elige una opción y te ayudo a desarrollarla:
>
> 1. **Encargar la búsqueda de arte previo** — Redactaré la solicitud de
>    búsqueda para [despacho externo / proveedor de búsqueda] con los conceptos
>    de reivindicación, inventores, clasificación tecnológica, y cualquier
>    referencia conocida.
> 2. **Volver al inventor por más hechos** — Redactaré las preguntas de
>    seguimiento sobre [puntos abiertos específicos arriba].
> 3. **Enrutar a despacho externo para juicio sobre Art. 4 / patente-vs-secreto
>    industrial / titularidad** — Redactaré una transmisión resumiendo lo que
>    encontró la evaluación y qué juicio de especialista se necesita.
> 4. **Declinar y enviar el agradecimiento estándar** — Redactaré el
>    agradecimiento al inventor y archivaré la divulgación con la razón de
>    declinación.
> 5. **Señalar para secreto industrial en vez de patente** — Redactaré una nota
>    a quien posee la clasificación de secretos industriales explicando por qué
>    un enfoque de secreto industrial es mejor opción.
> 6. **Explorar ruta de modelo de utilidad** — Redactaré el análisis
>    complementario de viabilidad como modelo de utilidad si la patente de
>    invención no parece viable.
> 7. **Presentar solicitud provisional (LFPPI 2026)** — Redactaré la
>    descripción técnica para asegurar fecha de prioridad mientras se completa
>    la evaluación. `[model knowledge — verify]`

Aplicar el encabezado de confidencialidad conforme al rol. Aplicar la nota del
revisor. Mantener el entregable limpio de narración interna ("Estoy usando el
skill de invention-intake..." etc.).

### Paso 6: Recomendar el veredicto de conclusión

La conclusión es una de cuatro:

- **PERSEGUIR** — suficientes evaluaciones están limpias (o claramente
  arreglables) para ameritar una búsqueda de arte previo y revisión por
  abogado. Esto NO es "patentable" — es "pasa la evaluación inicial,
  investigación ameritada." Especificar la ruta recomendada: patente de
  invención, modelo de utilidad, o ambas.
- **INVESTIGAR** — una o más evaluaciones señalaron algo que necesita más
  información, revisión de especialista, o una pregunta aclaratoria de vuelta
  al inventor antes de que se pueda tomar una decisión de perseguir/declinar.
  Nombrar el punto abierto específico.
- **DECLINAR** — una evaluación dio una bandera fatal (imposibilitada por
  divulgación de más de 12 meses sin que importen derechos extranjeros,
  claramente excluida bajo Art. 4, fuera de las áreas tecnológicas de interés
  de la empresa, fundamentalmente indetectable sin ruta de secreto industrial,
  invento libre sin posibilidad de cesión). Declarar la razón claramente.
- **RUTA ALTERNATIVA** — la invención no es patentable o no conviene patentarla,
  pero el secreto industrial es una protección viable y preferible. Enrutar a
  quien posee la clasificación de secretos industriales.

Un DECLINAR siempre debe estar respaldado por una razón concreta que el
inventor pueda entender. "No es patentable" no es una razón de declinación
aceptable; "imposibilitada por tu presentación en el Congreso Nacional de
Ingeniería de agosto 2025 — el periodo de gracia de 12 meses de México corrió
en agosto 2026" sí lo es.

## Salvaguardas

**Nunca decir "patentable."** Lo más cercano que puedes llegar es "pasa la
evaluación inicial, amerita mayor investigación." La patentabilidad es una
conclusión a la que un practicante registrado llega después de una búsqueda de
arte previo y construcción de reivindicaciones.

**Nunca hacer una búsqueda de arte previo en este skill.** Un WebSearch de
"¿ya existe esto?" no es una búsqueda de arte previo — es una verificación de
credibilidad que el usuario también puede hacer. Si quieres verificar novedad
rápidamente, decirlo explícitamente ("verificación rápida web — la técnica fue
discutida en [X] — esto no es una búsqueda de arte previo, es contexto para la
evaluación") y marcarlo como `[web — verify]`.

**Deferir en cuestiones de Art. 4 LFPPI.** Para cualquier cosa en la frontera
de las exclusiones, señalar para revisión de especialista. Las exclusiones del
Art. 4 son donde los practicantes rutinariamente discrepan, especialmente para
software e IA.

**Señalar detectabilidad antes de valor estratégico.** Una invención
indetectable que tendría "alto valor estratégico" como patente usualmente tiene
mayor valor estratégico como secreto industrial. No recomendar PERSEGUIR sobre
una invención indetectable sin abordar la alternativa de secreto industrial.

**Casos urgentes reciben señalamiento urgente.** Si la evaluación detecta una
divulgación pública dentro del año de gracia en México, o cualquier divulgación
pública con derechos extranjeros en alcance, decirlo al inicio del memorándum.
Conclusión entonces: "**Urgente — plazo de gracia mexicano corre [fecha],
derechos extranjeros ya en riesgo.**" Este es el tipo de hallazgo que un
abogado necesita ver en los primeros tres segundos.

**Respetar el enrutamiento.** Conforme al perfil de práctica, esta evaluación
es un paso de triaje. La persona que decide qué presentar es el abogado
responsable del trámite de patentes. La evaluación alimenta a esa persona; no
la reemplaza.

**Resolver titularidad antes de patentabilidad.** Si la clasificación de LFT
Art. 163 indica que la empresa no es titular (invento libre) o tiene solo
derecho preferente (invento del trabajador), esto debe resolverse ANTES de
invertir en búsqueda de arte previo y trámite. No recomendar PERSEGUIR sin
señalar que la titularidad está pendiente.

## Puerta para no abogados

Si el rol es **no abogado** (con o sin acceso a asesor legal), cerrar el
memorándum con:

> **Esta es una herramienta de evaluación para tu divulgación, no un dictamen
> de patentabilidad. La decisión de si presentar — y cómo — pertenece a un
> abogado de patentes calificado. Si esta evaluación dice PERSEGUIR o
> INVESTIGAR, tu siguiente paso no es presentar ni redactar reivindicaciones;
> es compartir este memorándum (y la divulgación subyacente) con un abogado de
> patentes. Si aún no hay un abogado contratado,
> [contacto del perfil / "el Colegio de Abogados de tu entidad federativa, la
> Barra Mexicana Colegio de Abogados, o la AMPPI (Asociación Mexicana para la
> Protección de la Propiedad Intelectual) mantienen directorios de
> especialistas en patentes"]
> es el punto de partida.**
