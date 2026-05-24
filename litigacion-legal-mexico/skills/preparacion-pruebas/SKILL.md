---
name: preparacion-pruebas
description: >
  Preparar la estrategia probatoria para un asunto — organizar pruebas documentales, elaborar
  pliego de posiciones (confesional), interrogatorio (testimonial), cuestionario (pericial),
  y vincular cada medio de prueba a la teoría del caso. Usar cuando el usuario diga "preparar
  pruebas para [asunto]", "elaborar pliego de posiciones", "preparar interrogatorio para
  [testigo]", "preparar cuestionario pericial", o necesite organizar su estrategia probatoria.
argument-hint: "[nombre del testigo o tipo de prueba]"
---

# /preparacion-pruebas

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → teoría del caso, hechos clave.
2. Seguir el flujo de trabajo y referencia abajo.
3. Identificar el periodo probatorio y tipo de procedimiento.
4. Construir la estrategia probatoria: pruebas a ofrecer, vinculación con hechos controvertidos, documentos, posiciones, interrogatorios, cuestionarios periciales.

---

# Preparación de Pruebas

## Contexto del sistema probatorio mexicano

México no tiene el concepto de _deposition_ (declaración jurada pre-juicio) del derecho anglosajón. El sistema probatorio mexicano opera dentro del juicio, durante el **periodo de ofrecimiento y desahogo de pruebas**. Los medios de prueba principales son:

- **Prueba confesional** (pliego de posiciones) — declaración jurada de la contraparte mediante posiciones articuladas por escrito. El absolvente responde "sí es cierto" o "no es cierto" a cada posición. Arts. 1232-1241 Código de Comercio; Arts. 308-326 CFPC.
- **Prueba testimonial** (interrogatorio) — testimonio de terceros mediante preguntas formuladas en audiencia. Arts. 1263-1276 Código de Comercio; Arts. 356-381 CFPC.
- **Prueba pericial** (cuestionario) — opinión de experto sobre cuestiones técnicas mediante cuestionario presentado por las partes. Arts. 1252-1258 Código de Comercio; Arts. 346-355 CFPC.
- **Prueba documental** — documentos públicos y privados. Arts. 1237-1251 Código de Comercio; Arts. 327-345 CFPC.
- **Prueba de inspección judicial** — visita del juzgador al lugar o cosa materia de la controversia.
- **Pruebas supervenientes** — pruebas que surgen o se conocen después del periodo probatorio ordinario.

**No existe el sistema de _discovery_ pre-juicio.** Las pruebas se ofrecen y desahogan dentro del juicio conforme al código procesal aplicable. No hay _Bates numbering_; la identificación de documentos sigue la nomenclatura del expediente judicial mexicano.

## Verificación de destino

Antes de producir el resultado, verificar a dónde va. Si el usuario ha nombrado un destino (un canal, una lista de distribución, una contraparte, "todos"), preguntar si está dentro del círculo de confidencialidad. Canales públicos, listas de toda la empresa, contraparte/abogado contrario, proveedores y clientes pueden comprometer el secreto profesional. Cuando el destino parezca fuera del círculo, señalarlo y ofrecer (a) la versión confidencial solo para el equipo legal, (b) una versión depurada para el canal más amplio, o (c) ambas. Ver `## Salvaguardas compartidas → Verificación de destino` en el CLAUDE.md de este plugin.

## Propósito

La preparación probatoria es el mapa estratégico: vincular cada hecho controvertido con los medios de prueba que lo acreditan, identificar vacíos probatorios, y preparar los escritos técnicos (pliegos de posiciones, interrogatorios, cuestionarios periciales) que se presentarán ante el juzgador. Este skill construye ese mapa a partir de los documentos y la teoría del caso.

## Fidelidad del expediente — citas y referencias puntuales

Dos reglas que gobiernan cada cita y cada referencia al expediente.

**Las citas textuales del expediente deben ser textuales.** Nunca poner comillas alrededor de palabras atribuidas a la contraparte, un testigo, el juzgador o cualquier documento del expediente a menos que tengas el pasaje exacto frente a ti y puedas citarlo. Cuando quieras caracterizar lo que alguien dijo pero no encuentras las palabras exactas:

- **Parafrasear sin comillas**, atribuyendo claramente: "El testigo previamente declaró que X `[verificar contra expediente — foja __]`."
- **Marcar el marcador de posición:** `[verificar cita exacta — referencia del expediente pendiente]`
- **Nunca llenar el vacío.** Una declaración inventada destruye la credibilidad probatoria.

**Las citas puntuales deben soportar toda la proposición.** Si un punto probatorio es "el testigo dijo X, Y y Z en [fecha]," verificar que la cita puntual soporta X Y Y Y Z. Si solo soporta Z, dividir la cita o limitar la proposición.

## Calibración procesal

Los escritos probatorios se presentan ante el juzgador y se desahogan en audiencia. Esto significa:

- Para el **pliego de posiciones**: articular posiciones claras, cerradas, que solo admitan "sí es cierto" o "no es cierto". Evitar posiciones compuestas, oscuras o que contengan más de un hecho. Las posiciones que no cumplen requisitos de forma pueden ser desechadas por el juzgador.
- Para el **interrogatorio testimonial**: formular preguntas claras, directas, no capciosas ni sugestivas (salvo en repreguntas permitidas). Máximo de preguntas según la ley procesal aplicable.
- Para el **cuestionario pericial**: formular preguntas técnicas claras, específicas al objeto del peritaje, que permitan al perito dar una opinión fundada.
- Priorizar los 3-4 puntos que realmente importan. Un pliego de 200 posiciones pierde efectividad.

## Cargar contexto

`~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → teoría del caso (teoría, hecho pivote, hechos clave a favor/en contra), integración con almacenamiento documental.

**Puerta de conflictos — no eludible.** Antes de preparar pruebas, verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rechazar y redirigir:

> "No veo [slug del asunto] en el registro de asuntos. Ejecute `/litigacion-legal-mexico:matter-intake` primero para que se ejecute la verificación de conflictos y se configure el espacio de trabajo del asunto. No prepararé estrategia probatoria sobre un asunto que no ha sido recibido — la verificación de conflictos es la puerta."

No proceder con un asunto no recibido. El intake es lo que ejecuta conflictos y escribe la fila de `_log.yaml` que este skill lee.

## Flujo de trabajo

### Paso 1: ¿Cuál es el asunto y qué se necesita probar?

- Tipo de procedimiento (juicio ordinario mercantil, juicio ejecutivo mercantil, juicio ordinario civil, juicio laboral, amparo, procedimiento administrativo)
- Código procesal aplicable (Código de Comercio, CFPC, CNPCF, LFT, Ley de Amparo, LFPCA)
- Hechos controvertidos — qué hechos están en disputa entre las partes
- Carga de la prueba — quién tiene la obligación de probar qué (actor vs. demandado; en laboral, frecuentemente la carga se invierte al patrón)

### Paso 1a: Identificar el periodo probatorio

Verificar en qué etapa procesal se encuentra el asunto y cuáles son los plazos:

- **Juicio ordinario mercantil** — periodo probatorio de 40 días (Art. 1382 Código de Comercio); primeros 10 días para ofrecimiento.
- **Juicio ordinario civil federal** — periodos según CFPC o CNPCF aplicable.
- **Juicio laboral** — las pruebas se ofrecen en la audiencia de conciliación, demanda y excepciones y ofrecimiento y admisión de pruebas (nuevo sistema: audiencia preliminar).
- **Amparo** — las pruebas se ofrecen con la demanda o en la audiencia constitucional; reglas especiales para pruebas supervenientes.

**Investigar las reglas probatorias aplicables al foro y tipo de procedimiento.** Citar fuentes primarias. No aplicar un esquema genérico.

**Sin complemento silencioso.** Si una consulta a la herramienta de investigación jurídica configurada (SCJN IUS, Semanario Judicial, DOF, plataforma del despacho) devuelve pocos o ningún resultado para las reglas probatorias del foro o una cita necesaria, reportar lo encontrado y detenerse. No llenar el vacío sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece escasa para [norma / autoridad]. Opciones: (1) ampliar la consulta, (2) probar otra herramienta, (3) buscar en web — resultados etiquetados `[búsqueda web — verificar]`, o (4) dejar el marcador `[INCIERTO]` y detenerse aquí. ¿Cuál prefiere?"

**Atribución de fuentes.** Etiquetar cada referencia normativa, tesis y jurisprudencia con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o el nombre de la herramienta MCP; `[búsqueda web — verificar]` para citas web; `[conocimiento del modelo — verificar]` para citas de entrenamiento; `[proporcionado por usuario]` para citas del abogado. Nunca eliminar ni colapsar las etiquetas.

### Paso 2: Organizar los documentos del asunto

Del almacenamiento documental (Google Drive / SharePoint / DMS si está conectado):

- Documentos base del asunto (contratos, correspondencia, facturas, etc.)
- Documentos de la contraparte (demanda, contestación, escritos previos)
- Documentos de autoridades (notificaciones, resoluciones interlocutorias)
- Peritajes previos, dictámenes, informes

Organizar por fecha. Señalar los documentos clave — los que más importan para la teoría del caso.

### Paso 3: Construir la estrategia probatoria por tipo de prueba

#### A. Prueba documental

Para cada documento a ofrecer:
- Descripción del documento
- Hecho que acredita (vincular a hecho controvertido específico)
- Si es público o privado (afecta su valor probatorio)
- Si requiere cotejo o reconocimiento
- Cómo se relaciona con la teoría del caso

#### B. Prueba confesional (pliego de posiciones)

**Postura del absolvente:**
- **Representante legal de persona moral** — puede absolver posiciones en nombre de la empresa. Verificar que tenga facultades suficientes. Arts. 1232-1241 Código de Comercio.
- **Persona física (contraparte)** — comparece personalmente.
- **Confesión ficta** — si no comparece o se rehúsa a contestar, se tienen por confesados los hechos (Art. 1236 Código de Comercio). Verificar requisitos.

Reglas para articular posiciones:
- Cada posición debe contener un solo hecho
- Deben ser claras, precisas y en sentido afirmativo
- No deben ser insidiosas (que tiendan a confundir al absolvente)
- Se articulan por escrito y se presentan en sobre cerrado en la audiencia
- Máximo de posiciones según la norma aplicable

**Estructura del pliego:**
1. Posiciones sobre hechos no controvertidos (fijar la base)
2. Posiciones sobre hechos favorables (asegurar admisiones)
3. Posiciones sobre hechos desfavorables (obtener la versión de la contraparte en nuestros términos)
4. Posiciones sobre el hecho pivote de la teoría del caso

#### C. Prueba testimonial (interrogatorio)

**Postura del testigo:**
- **Testigo propio** — preguntas abiertas que permitan narrar los hechos.
- **Testigo de la contraparte** — preguntas directas y cerradas para fijar hechos específicos.
- **Testigo tercero neutral** — mezcla; preguntas abiertas para obtener la narrativa, cerradas para fijar detalles.

Reglas del interrogatorio:
- Las preguntas se formulan verbalmente en la audiencia (salvo legislaciones que permiten escrito)
- No deben ser capciosas ni sugestivas (salvo repreguntas)
- Se permite hacer repreguntas
- Máximo de testigos y preguntas según la norma aplicable

**Estructura del interrogatorio:**
1. Antecedentes (establecer relación del testigo con los hechos)
2. Hechos directamente percibidos por el testigo
3. Hechos favorables a nuestra posición
4. Circunstancias que contradicen la versión de la contraparte
5. El hecho pivote de la teoría del caso

#### D. Prueba pericial (cuestionario)

**Tipo de peritaje:**
- Contable, financiero, grafoscópico, valuatorio, informático, médico, de ingeniería, etc.
- Cada parte designa un perito; el juez puede designar perito tercero en discordia.

Reglas del cuestionario:
- Las preguntas deben ser técnicas y relevantes al objeto del peritaje
- Se presentan por escrito al ofrecer la prueba
- La contraparte puede adicionar preguntas
- El perito rinde su dictamen por escrito y puede ser llamado a ratificarlo

**Estructura del cuestionario:**
1. Preguntas sobre la metodología aplicable
2. Preguntas sobre los hechos técnicos relevantes
3. Preguntas que vinculen la opinión técnica con los hechos controvertidos
4. Preguntas que anticipen y desacrediten la posición técnica de la contraparte

### Paso 4: Escribir el producto

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

# Estrategia Probatoria: [Nombre del Asunto]

**Fecha:** [fecha]
**Tipo de procedimiento:** [juicio ordinario mercantil / ejecutivo mercantil / ordinario civil / laboral / amparo / otro]
**Código procesal aplicable:** [Código de Comercio / CFPC / CNPCF / LFT / Ley de Amparo]
**Reglas probatorias aplicables:** [artículos específicos con citas puntuales] `[INCIERTO — verificar vigencia]`
**Periodo probatorio:** [fechas de inicio y término / etapa procesal actual]
**Carga de la prueba:** [quién prueba qué — regla general y excepciones aplicables]
**Vínculo con teoría del caso:** [cómo esta estrategia probatoria soporta la teoría]

---

## I. Hechos controvertidos

[Lista de hechos en disputa, vinculados con los puntos de la litis fijados por el juzgador]

## II. Pruebas documentales a ofrecer

| # | Documento | Hecho que acredita | Tipo (público/privado) | Requiere cotejo | Observaciones |
|---|---|---|---|---|---|
| 1 | [descripción] | [hecho] | [público/privado] | [sí/no] | [notas] |

## III. Prueba confesional — Pliego de posiciones

**Absolvente:** [nombre, carácter]
**Objetivo:** [qué se busca obtener con la confesional]

### Posiciones

| # | Posición | Hecho que acredita | Fortaleza | Verificado |
|---|---|---|---|---|
| 1 | "Diga si es cierto que..." | [hecho] | [fuerte/moderada/débil] | ☐ |

## IV. Prueba testimonial — Interrogatorio

**Testigo:** [nombre]
**Relación con los hechos:** [descripción]
**Postura del testigo:** [propio / contraparte / neutral]

### Preguntas

[La secuencia de preguntas, organizadas por tema y vinculadas a los hechos controvertidos.]

## V. Prueba pericial — Cuestionario

**Tipo de peritaje:** [materia]
**Objetivo:** [qué se busca acreditar con el peritaje]

### Cuestionario

| # | Pregunta | Objetivo técnico | Hecho que vincula |
|---|---|---|---|
| 1 | [pregunta técnica] | [objetivo] | [hecho controvertido] |

---

## VI. Matriz de hechos vs. pruebas

| Hecho controvertido | Documental | Confesional | Testimonial | Pericial | Estado |
|---|---|---|---|---|---|
| [hecho 1] | [docs] | [posiciones] | [testigos] | [pericial] | [acreditado/parcial/vacío] |

## VII. Vacíos probatorios

> **Hechos con prueba insuficiente o inexistente:** [lista]
>
> - Si somos **actor**: estos vacíos debilitan nuestra posición y pueden resultar en absolución del demandado. Cerrarlos antes de que concluya el periodo probatorio.
> - Si somos **demandado**: estos son puntos débiles del actor que podemos explotar en alegatos.
> - Si estamos en **etapa previa al ofrecimiento**: estas son las pruebas que debemos conseguir u ofrecer.

---

## Disciplina de marcadores

Usar en línea durante la elaboración y revisión:
- `[VERIFICAR: aseveración fáctica]` — cualquier hecho no confirmado contra el expediente
- `[INCIERTO: proposición jurídica]` — cualquier punto legal no confirmado contra autoridad vigente
- `[CITA NECESARIA: cita específica]` — referencia del expediente o autoridad pendiente

## Notas para el abogado

- [Cualquier cosa que la estrategia no capture — observaciones estratégicas, decisiones a tomar en la audiencia]

---

**Material confidencial / secreto profesional.** Esta estrategia probatoria está elaborada a partir de materiales del caso y trabajo del equipo legal, y hereda su estatus de protección. Mantener en la carpeta de materiales confidenciales, marcar apropiadamente, y tomar cualquier decisión de distribución (co-abogados, cliente, peritos) deliberadamente — la distribución fuera del círculo de confidencialidad puede comprometer el secreto profesional.

**Verificar toda autoridad citada.** Las citas normativas (Código de Comercio, CFPC, CNPCF, LFT, etc.) y cualquier tesis o jurisprudencia incluida fueron generadas por un modelo de IA. Verificar cada una contra SCJN IUS, Semanario Judicial, DOF, o su plataforma de investigación — confirmar vigencia y alcance antes de usar en el procedimiento. Las etiquetas de fuente en cada cita (ej., `[SCJN IUS]`, `[búsqueda web — verificar]`) muestran su procedencia; las etiquetas `verificar` tienen mayor riesgo de fabricación y deben verificarse primero.
```

## Lo que este skill NO hace

- Desahogar las pruebas. La estrategia es el mapa; el abogado la ejecuta en audiencia.
- Predecir lo que el absolvente o testigo dirá. Prepara para respuestas probables, pero siempre hay sorpresas.
- Decidir qué preguntar en el acto. Las repreguntas y ajustes son decisión del abogado en el momento.
- Sustituir la valoración del juzgador sobre admisibilidad y valor probatorio de cada prueba.
