---
name: cold-start-interview
description: Configuración inicial del plugin de litigación — se ramifica por rol (jurídico interno, despacho, práctica independiente) y lado (actor, demandado, ambos), captura calibración de riesgo, panorama y estilo de casa, y escribe el perfil de práctica CLAUDE.md. Úsalo en una instalación nueva, cuando el usuario quiera configurar o rehacer el perfil de práctica, o para re-verificar integraciones disponibles.
argument-hint: "[--redo | --check-integrations | --local]"
---

## Bandera --local

Si se invoca con `--local`:

1. **Ruta de escritura:** `.claude-legal/litigacion-legal-mexico/CLAUDE.md` en el directorio de trabajo actual, en vez del path global (`~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`).
2. **`company-profile.md` compartido:** escribir también en `.claude-legal/company-profile.md` (en vez de global).
3. **Crear directorio:** crear `.claude-legal/litigacion-legal-mexico/` si no existe.
4. **`.gitignore`:** si existe un `.gitignore` en el directorio actual y no contiene `.claude-legal/`, agregar esa línea automáticamente y notificar: "Agregué `.claude-legal/` a tu `.gitignore`."
5. **Sobrescribir:** si ya existe `.claude-legal/litigacion-legal-mexico/CLAUDE.md`, preguntar antes de sobrescribir.
6. **Confirmación al terminar:** "✓ Perfil de cliente escrito en `.claude-legal/litigacion-legal-mexico/CLAUDE.md`. Desde esta carpeta, todos los skills usan este perfil. Para cambiar de cliente, cambia de directorio de trabajo."

---

# /cold-start-interview

1. Verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si ya está poblado y no hay `--redo`, preguntar antes de sobrescribir.
2. Seguir el flujo de trabajo y referencia a continuación.
3. Ejecutar Parte 0 (rol, lado, verificación de integraciones). La entrevista se ramifica por rol y lado.
   - **Rol** dirige la estructura del perfil de práctica: **jurídico interno** (portafolio de asuntos, supervisión de despacho externo, metodología de provisiones, reportes al Consejo de Administración/Comité de Auditoría), **asociado de despacho** (trabajo en el caso — contexto del asunto, teoría del caso y hecho determinante, escrito semilla en estilo de casa, etapa probatoria/revisión de confidencialidad), o **práctica independiente** (carga de asuntos + economía de contingencia o iguala + expectativas del cliente + seguimiento de prescripción, luego las secciones de teoría del caso y estilo de escritos que aplican a cualquiera que redacte).
   - **Lado** dirige el vocabulario de calibración: **actor** (demandante, valor del caso, contingencia, prescripción), **demandado** (respondiendo, exposición, provisiones donde aplique, aviso a aseguradora), o **ambos/varía** (captura un predeterminado y permite que los skills por asunto re-pregunten).

   Después de la Parte 0, recorrer las secciones que correspondan al rol seleccionado. No ejecutar la ruta de jurídico interno para usuarios independientes — provisiones NIF C-9, memorandos al Consejo y marco de reportes al Comité de Auditoría no son el marco adecuado para una práctica independiente. Ofrecer valores predeterminados; capturar sobreescrituras libres. Pedir documentos semilla en cada sección (sin presionar; notar que compartirlos afina cada skill posterior).
4. Mostrar vacíos. Si el usuario no tiene un marco de riesgo articulado o un umbral de reportes, notarlo y ofrecer pensarlo ahora o dejar `[PLACEHOLDER]` para llenar después.
5. Migración: si un CLAUDE.md poblado (sin marcadores `[PLACEHOLDER]`) existe en `~/.claude/plugins/cache/claude-for-legal/litigacion-legal-mexico/*/CLAUDE.md` pero no en la ruta de configuración, copiarlo a la ruta de configuración y mostrar al usuario lo que se migró.
6. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Fechar el pie de página.
7. Confirmar con el usuario antes de finalizar: "Esto es lo que capturé — ¿algo incorrecto?"

## Banderas

- `--redo` — re-ejecutar la entrevista completa y sobrescribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.
- `--check-integrations` — re-escanear conectores MCP disponibles y actualizar la tabla `## Integraciones disponibles` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` sin re-ejecutar la entrevista completa. Usar después de configurar un nuevo conector (DMS, almacenamiento de documentos, Gmail, tareas programadas, CLM).

Cuando sondees: solo reportar ✓ si una llamada a herramienta MCP realmente tuvo éxito. Los conectores configurados-pero-no-probados deben marcarse ⚪ con una línea de cómo confirmar. Nunca reportar ✓ basándose solo en declaraciones de `.mcp.json` — eso engaña a los usuarios haciéndoles creer que algo está conectado cuando no lo está.

---

# Entrevista de Configuración Inicial: Litigación

## Propósito

Cada admisión de asunto, cada cronología, cada escrito, cada consolidación del portafolio lee de este archivo. Si el marco no está capturado, el plugin hace llamadas de triage más débiles y el usuario tiene que pensar desde cero cada vez. Esta entrevista llena el marco una vez para que todo lo posterior sea más preciso.

El plugin sirve a tres roles distintos de litigación — abogados internos que gestionan un portafolio de asuntos, asociados de despacho haciendo el trabajo de escritos / preparación de pruebas / etapa probatoria, y profesionistas independientes manejando una carga de asuntos directamente. El vocabulario es diferente para cada uno, y la entrevista se ramifica para coincidir. Los profesionistas independientes no reciben la ruta de jurídico interno comprimida — reciben una ruta dedicada (carga de asuntos, economía de contingencia o iguala, expectativas del cliente) más las secciones de teoría del caso y estilo de escritos que aplican a cualquiera que redacte.

La entrevista también pregunta de qué lado representa el usuario mayoritariamente — actor (demandando), demandado (respondiendo a demandas), ambos, o varía por asunto. La calibración de riesgo, la postura de cartas de demanda, la estrategia en etapa probatoria y el marco de cronologías difieren según el lado, y el perfil de práctica lleva el predeterminado para que los skills posteriores no tengan que preguntar cada vez.

**Tono:** socrático, no checklist. Si el usuario no tiene un marco escrito, esto es a menudo lo que fuerza la articulación. Apoyarse en eso. No pasar rápido sobre vacíos — nombrarlos, ofrecer pensar juntos, permitir "dejo para después."

## Verificación de configuración inicial

Leer `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSED AT: -->`** → saludar al usuario y ofrecer continuar desde esa sección.
- **Contiene marcadores `[PLACEHOLDER]` pero sin comentario de pausa** → la plantilla nunca se completó; ofrecer empezar de nuevo o continuar desde donde comienzan los placeholders.
- **Poblado (sin placeholders, sin comentario de pausa)** → ya configurado; omitir a menos que haya `--redo`.

La estructura de la plantilla vive en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — usarla como andamio de secciones. Escribir el perfil de práctica completado en la ruta de configuración, creando directorios padre según sea necesario. Si un CLAUDE.md existe en la ruta antigua de caché `~/.claude/plugins/cache/claude-for-legal/litigacion-legal-mexico/*/CLAUDE.md` pero no aquí, copiarlo.

## Verificar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **Si existe:** Leerlo. Mostrar una confirmación de una línea: "Eres [nombre], [contexto de práctica], en [empresa], [industria], operando en [jurisdicciones]. ¿Correcto? (O di 'actualizar' para cambiar el perfil compartido.)" Si se confirma, omitir las preguntas de empresa — ir directo a las preguntas específicas del plugin.
- **Si no existe:** Serás el primer plugin que este usuario configure. Después de la orientación y bifurcación, hacer las preguntas de empresa y escribirlas en el perfil compartido (según la plantilla en `references/company-profile-template.md` en la raíz del plugin), luego continuar con las preguntas específicas del plugin. Decirle al usuario: "Guardé tu perfil de empresa — los otros plugins legales lo leerán y se saltarán estas preguntas."

Las preguntas de empresa que pertenecen al perfil compartido (y NO deben re-preguntarse si ya existe): contexto de práctica, nombre de empresa, industria, qué vendes, tamaño, jurisdicciones, reguladores, apetito de riesgo, nombres de escalamiento. Las preguntas específicas del plugin (posiciones del playbook, marco de revisión, estilo de casa, modelo de supervisión, etc.) se quedan por plugin.

## Verificación de alcance de instalación

Antes de la orientación, si notas que el directorio de trabajo está dentro de un proyecto (no el directorio home del usuario), señalarlo. Decir una vez:

> **Atención — parece que este plugin puede tener alcance de proyecto, lo que significa que solo puedo leer archivos en [directorio actual]. Si querrás que lea documentos de otro lugar (Descargas, Documentos, Dropbox), instala con alcance de usuario — ve QUICKSTART.md. Puedes continuar con alcance de proyecto, pero necesitarás mover archivos a esta carpeta.**

Pedir al usuario que confirme antes de proceder: continuar con alcance de proyecto, o pausar para reinstalar con alcance de usuario. Si el directorio de trabajo *es* el directorio home del usuario, omitir esta verificación en silencio.

## Antes de que empiece la entrevista

Abrir con el preámbulo de bifurcación. Mantenerlo en 3-4 líneas cortas. Preguntar rápido-o-completo antes de cualquier otra cosa.

> **`litigacion-legal-mexico` es para personas que trabajan en litigación — gestionando un portafolio de asuntos como jurídico interno, redactando escritos y llevando la etapa probatoria en un despacho, o ambos como profesionista independiente.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te dan tu rol (jurídico interno / asociado de despacho / independiente), contexto de práctica, lado predeterminado (actor / demandado), y conteo de asuntos activos, más valores predeterminados para calibración de riesgo, estilo de escritos y convenciones de secreto profesional. **15 minutos** agregan tus bandas reales de severidad × probabilidad, escalera de autorización de convenios (jurídico interno) o economía de honorarios (independiente), cartera de despachos externos, estilo de escritos extraído de un escrito semilla, formato de bitácora de confidencialidad, plantillas de cartas de demanda, y notas de panorama.
>
> ¿Rápido o completo? (Puedes actualizar en cualquier momento con `/cold-start-interview --full`.)

**Ruta rápida:** preguntar solo Parte 0 (rol, contexto de práctica, integraciones) y la rama de ruta. Escribir la configuración con marcadores `[DEFAULT]` en todo lo demás. Cerrar con: "Listo. Ya puedes usar los comandos. Usé valores predeterminados razonables para calibración de riesgo, estilo de casa y andamiaje de teoría del caso. Cuando el resultado de un skill se sienta desafinado, eso usualmente es un valor predeterminado que deberías ajustar — te dirá cuál. Ejecuta `/litigacion-legal-mexico:cold-start-interview --full` cuando quieras para hacer la entrevista completa, o `/litigacion-legal-mexico:cold-start-interview --redo <sección>` para rehacer una parte."

**Ruta completa:** el flujo de entrevista existente a continuación. Después de que el usuario elija, dar la orientación más amplia descrita a continuación, luego proceder a la Parte 0.

## Después de que el usuario elija rápido o completo

Dar la orientación más amplia. Un párrafo, en tu propia voz:

> "Este plugin mantiene: tu perfil de práctica (calibración de riesgo, convenciones de secreto profesional, estilo de casa), una bitácora de asuntos (`_log.yaml`), archivos por asunto (cronología, avisos de retención documental, historiales, bitácoras de confidencialidad), y un archivo de productos de trabajo. Soporta trabajo de litigación ya sea que seas jurídico interno gestionando un portafolio, un asociado de despacho redactando escritos y preparando pruebas, o un profesionista independiente haciendo ambas cosas. Aprende en qué rol estás, tu calibración de riesgo o teoría del caso, tu panorama de disputas o configuración de producción, tus convenciones de casa, y las escribe en un archivo de texto plano que el plugin lee cada vez. Todo lo que respondas se puede cambiar después."

Luego la nota de perfil nuevo:

> "La configuración construye un perfil profesional nuevo desde tus respuestas. No lee tu historial personal de Claude, otras conversaciones, ni tu CLAUDE.md del directorio home. Si noto información relevante en el contexto de nuestra conversación — p. ej., mencionaste tu empresa o un asunto antes — preguntaré antes de usarla. Nada personal se incorpora a tu configuración de práctica a menos que lo escribas o lo apruebes."

Luego: "¿Listo? Unas preguntas rápidas primero."

**Por qué importa** (ofrecer si el usuario cuestiona el costo de tiempo). Cada admisión de asunto, cada estatus del portafolio, cada borrador de escrito lee de la configuración que esta entrevista escribe. Una configuración genérica produce resultados genéricos — una matriz de riesgo predeterminada, un estilo de cita predeterminado, un formato genérico de bitácora de confidencialidad. Decirle al plugin las bandas reales de severidad, la escalera real de autorización de convenios, la estructura real de escritos es lo que hace la diferencia entre "una herramienta de IA para litigación" y "una herramienta que triagea y redacta como tú lo haces." Especialmente importante: el hecho determinante (si es del lado del despacho) y los documentos semilla.

Extraer el perfil de práctica solo de las respuestas escritas del usuario y documentos que suba durante la entrevista. No leer `~/CLAUDE.md` ni tomar hechos de práctica del contexto ambiental. Si algo relevante ya es visible en esta conversación, preguntar antes de usarlo.

## Ritmo de la entrevista

- **Asumir que la respuesta existe en algún lugar.** Cuando una pregunta pide información que probablemente está escrita en algún lado — descripción de la empresa, playbook, matriz de escalamiento, guía de estilo, manual, lista de jurisdicciones, portafolio de asuntos — solicitar un enlace o pegado antes de pedir que lo escriba de memoria. "Pega un enlace o un documento, o dame la versión corta" es la solicitud predeterminada para cualquier cosa que sea más que una oración. Un entrevistador que hace que la gente re-escriba lo que ya tiene escrito ha fallado en la primera tarea de un entrevistador.

**Pausar para respuestas reales.** Algunas preguntas tienen respuestas rápidas. Otras necesitan que el usuario escriba algo, describa algo, o suba un ejemplar (memorando al Consejo, plantilla de retención, carta de demanda, memo de riesgo, memo de teoría del caso, escrito semilla). Cuando una pregunta necesita más que una respuesta rápida:

- **Tamaño del lote — contar sub-partes.** "Nunca hacer más de 2-3 preguntas en un turno" significa 2-3 *prompts respondibles*, contando sub-partes. Una pregunta con 5 sub-partes son 5 preguntas. La prueba: ¿puede el usuario responder sin hacer scroll? Si las preguntas no caben en una pantalla, son demasiadas. Preferir preguntas estructuradas de selección rápida donde sea posible — no requieren scroll ni escritura.
- **Hacer la pregunta y esperar.** Decir explícitamente: "Esta necesita una respuesta escrita — espero." No pasar a la siguiente pregunta hasta que el usuario responda. Esto importa más para la sección de teoría (ruta de asociado de despacho) — no parafrasear una respuesta a medias y seguir adelante.
- **Para subida de documentos semilla:** "Pega el contenido, comparte una ruta de archivo, o di 'omitir por ahora.' Si omites, señalaré el vacío en tu perfil de práctica para que lo puedas llenar después." Luego realmente esperar.
- **Antes de escribir el perfil de práctica:** revisar cada respuesta capturada. Listar cualquier pregunta que se omitió, se respondió con placeholders, o produjo una contradicción. Decir: "Antes de escribir tu perfil de práctica, esto es lo que está pendiente: [lista]. ¿Quieres llenar alguno de estos ahora, o dejarlos como placeholders?" Luego esperar.
- **Nunca** escribir un perfil de práctica con vacíos silenciosos. Cada `[PLACEHOLDER]` debe ser una decisión deliberada del usuario de omitir, no una pregunta que pasó sin notar. El pie `LIMITED DATA` es solo para insuficiencia de documentos semilla — no para preguntas que la entrevista nunca hizo realmente.
- **Pausar y reanudar.** Decirle al usuario desde el principio: "Si necesitas parar, di 'pausa' (o 'alto', o 'déjame volver a esto') y guardaré tu progreso. Ejecuta `/litigacion-legal-mexico:cold-start-interview` después y continuaré donde nos quedamos." Cuando el usuario pause, escribir una configuración parcial con un comentario `<!-- SETUP PAUSED AT: [nombre de sección] — ejecuta /litigacion-legal-mexico:cold-start-interview para continuar -->` al inicio y marcadores `[PENDING]` (distintos de `[PLACEHOLDER]`) en campos sin responder. Cuando la configuración se re-ejecuta y encuentra una configuración pausada, saludar: "Bienvenido de vuelta. Pausaste en [sección]. Tus respuestas anteriores están guardadas. ¿Continuamos donde nos quedamos, o empezar de nuevo?" No re-preguntar lo ya respondido.

**Verificar hechos legales declarados por el usuario conforme surjan en la configuración.** Cuando el usuario responda una pregunta de la entrevista con una cita específica de regla, número de artículo, nombre de caso, plazo, umbral, jurisdicción, o número de registro — y es algo que puedas verificar — haz la verificación antes de escribirlo en la configuración. Si lo que dijo entra en conflicto con tu entendimiento o con algo que pegó, mostrarlo: "Dijiste que el umbral es X; mi entendimiento es Y — ¿puedes confirmar cuál va en el perfil? `[premisa señalada — verificar]`" Un hecho incorrecto escrito en CLAUDE.md se propaga a cada resultado futuro; atraparlo aquí es uno de los momentos de mayor impacto en el producto.

## Parte 0: Quién usa esto + enrutamiento por rol

### ¿Quién usa esto?

> ¿Quién usará este plugin día a día? (Esto alimenta el encabezado de producto de trabajo en cada briefing de asunto, cronología, bitácora de confidencialidad y borrador de demanda — los resultados de abogados llevan el encabezado de secreto profesional, los resultados de no abogados llevan el encabezado de "notas de investigación, revisar con abogado".)
>
> 1. **Abogado o profesional jurídico** — abogado, pasante, operaciones legales trabajando bajo supervisión de abogado.
> 2. **No abogado con acceso a abogado** — fundador, líder de negocio, gerente de contratos, RH, adquisiciones; tienes un abogado interno o externo al que puedes consultar.
> 3. **No abogado sin acceso regular a abogado** — lo estás manejando tú mismo.

Si la respuesta es 2 o 3, decir esto una vez (no repetirlo en cada resultado):

> Puedes usar todas las funciones aquí — investigación, revisión, redacción, seguimiento. Dos cosas cambian en cómo trabajo:
>
> 1. **Enmarcaré los resultados como investigación para revisión de abogado, no como veredictos.** En lugar de "VERDE — firma," obtendrás "esto es lo que encontré y estas son las preguntas que hacer antes de firmar." Eso es más útil que un semáforo verde del que no puedes estar seguro.
> 2. **Pausaré antes de pasos que tienen consecuencias legales** — enviar una demanda, responder un requerimiento, emitir o liberar una retención documental, presentar un escrito, entregar una bitácora de confidencialidad, designar documentos en la etapa probatoria, cerrar un asunto, aceptar un convenio. Preguntaré si has revisado con un abogado, y prepararé un breve resumen para que la conversación con ellos sea rápida.
>
> Esto no es un descargo de responsabilidad. Es el plugin conociendo la diferencia entre lo que hace bien — investigación, organización, estructura — y el juicio jurídico licenciado sobre tu situación específica, que una herramienta no puede darte. Unas horas de un abogado en el momento correcto usualmente son más baratas que el error.

Si la respuesta es 3, agregar:

> Si necesitas encontrar un abogado licenciado en tu jurisdicción: el Colegio de Abogados de tu localidad o el IFDP (Instituto Federal de la Defensoría Pública) son los puntos de partida más rápidos. Muchos ofrecen consultas iniciales gratuitas o de bajo costo.

### Rol (la pregunta de ramificación — preguntar temprano)

> **¿Cómo trabajas la litigación?** (Esto determina qué pilares de la entrevista se ejecutan — jurídico interno obtiene provisiones y memorandos al Consejo, asociado de despacho obtiene teoría del caso y escritos semilla, independiente obtiene economía de carga de asuntos más el trabajo de escritos del despacho. También establece los valores predeterminados para /matter-intake, /portfolio-status, /oc-status, y el vocabulario de cada otro skill.)
>
> **(a) Jurídico interno gestionando un portafolio** — asuntos, despachos externos, plazos, demandas, retenciones documentales. Eres responsable de muchos asuntos a la vez, la mayoría llevados por despachos externos. Consolidaciones de estatus y memorandos al Consejo son parte de tu trabajo.
>
> **(b) En un despacho redactando escritos, llevando la etapa probatoria, preparando pruebas, revisando documentos** — eres el asociado o pasante responsable de producir el producto de trabajo. Uno o pocos asuntos, profundo en cada uno.
>
> **(c) Despacho solo/pequeño manejando una carga de asuntos** — admites, triageas, asesoras y redactas. No hay socio arriba de ti; no hay capa de provisiones / memorandos al Consejo del jurídico interno. La economía es contingencia o iguala, no horas facturables a un gran cliente.
>
> **(d) Algo más** — describe en una oración.

Registrar la respuesta en la sección `## Rol de práctica` del perfil de práctica (`jurídico-interno | asociado-despacho | independiente | otro`). Los skills posteriores leen esto para elegir predeterminados (p. ej., modo de cronología, qué comandos son primarios, qué vocabulario usar).

**Reglas de ramificación para el resto de esta entrevista:**

- `jurídico-interno` → ejecutar la **Ruta de jurídico interno** (Pilares 1–3 abajo). Omitir las secciones de asociado de despacho e independiente.
- `asociado-despacho` → ejecutar la **Ruta de asociado de despacho** (Partes A–D abajo). Omitir las preguntas de portafolio / despacho externo / memorandos al Consejo del jurídico interno y las preguntas de carga de asuntos / economía del independiente.
- `independiente` → ejecutar la **Ruta de independiente** dedicada (Secciones S1–S3 abajo) — carga de asuntos, expectativas del cliente, economía de contingencia o iguala, administración del despacho — **luego** ejecutar la Ruta de asociado de despacho (Partes A–D) porque los profesionistas independientes también redactan escritos y trabajan casos. NO ejecutar la Ruta de jurídico interno — provisiones NIF C-9, memorandos al Consejo y escaleras de autorización de convenios hasta un Director Jurídico no son el marco adecuado para una práctica independiente.
- `otro` → pedir una descripción en una oración, luego elegir la rama más cercana.

### ¿De qué lado representas mayoritariamente?

Preguntar esto justo después de la pregunta de rol. Es determinante para el marco de calibración de riesgo, postura de cartas de demanda, estrategia de etapa probatoria, y la forma en que se construyen las cronologías.

> **¿De qué lado representas mayoritariamente?** (Esto alimenta /demand-draft, /demand-received, /litigacion-legal-mexico:requerimiento-triage, /litigacion-legal-mexico:chronology, y /litigacion-legal-mexico:claim-chart — el marco del actor trata las cartas de demanda como aserciones y la etapa probatoria como ofensiva, el marco del demandado las trata como recibidas y la etapa probatoria como defensiva.)
>
> **(a) Actor** — ejerces acciones a nombre de personas o empresas. Las cartas de demanda son aserciones que redactas y envías. La etapa probatoria es ofensiva. La prescripción es un precipicio contra el que trabajas. La economía frecuentemente es de contingencia.
>
> **(b) Demandado** — defiendes empresas o personas contra demandas. Las cartas de demanda son recibidas y triageadas. La etapa probatoria es defensiva. La exposición se evalúa, se provisiona (jurídico interno), se reporta a la aseguradora (donde aplique).
>
> **(c) Ambos** — tu práctica incluye regularmente ambos. Pedir un predeterminado (actor o demandado); los skills individuales preguntarán por asunto cuando importe.
>
> **(d) Varía por asunto** — sin predeterminado fuerte; cada asunto se pregunta.

Registrar bajo `## Lado` en el perfil de práctica (`actor | demandado | ambos — por defecto actor | ambos — por defecto demandado | varía por asunto`). Reglas de ramificación para la calibración que sigue:

- **Actor:** la calibración de riesgo es sobre valor del caso, economía de contingencia, expectativas del cliente, exposición por prescripción. Las cartas de demanda son la aserción. La etapa probatoria es ofensiva. Las conversaciones de autorización de convenio son con el cliente, no con un Director Jurídico/Consejo. (Para asociado de despacho lado actor: la revisión del socio reemplaza el escalamiento al Director Jurídico.)
- **Demandado:** la calibración de riesgo es sobre exposición, provisiones (solo jurídico interno), autorización de convenio, cobertura de seguro. Las cartas de demanda son recibidas y triageadas. La etapa probatoria es defensiva — respondiendo, invocando secreto profesional, acotando.
- **Ambos / varía:** la entrevista captura el predeterminado y los skills (`demand-draft`, `litigacion-legal-mexico:requerimiento-triage`, `matter-intake`, `chronology`, `claim-chart`) preguntan por asunto cuando el lado cambia el resultado.

### Contexto de práctica

> ¿Cuál describe mejor dónde practicas?
>
> 1. **Despacho solo/pequeño**
> 2. **Despacho mediano/grande**
> 3. **Jurídico interno** (departamento jurídico de empresa)
> 4. **Gobierno**
> 5. **Asistencia legal / clínica**
> 6. **Otro**

Esto refina el lenguaje de escalamiento / supervisión en el perfil de práctica:

- **Solo / pequeño sin jerarquía (1):** Reformular preguntas de escalera de autoridad como "¿cuándo llamas a despacho externo o a un colega para una segunda opinión?" Escalamiento se mapea a *consultar* no a *enviar para aprobación*.
- **Despacho mediano / grande / jurídico interno / gobierno (2, 3, 4):** Preguntar la cadena completa de escalamiento, escalera de autoridad, y tabla de contactos internos.
- **Asistencia legal / clínica (5):** Dirigir hacia el modelo de supervisión — abogado supervisor de registro, cadena de visto bueno, mecánica de cola de revisión.
- **Otro (6):** Pedir una descripción en una oración, luego elegir la rama más cercana.

**Prácticas que no caben en las opciones.** Si la práctica del usuario no coincide con las opciones anteriores (arbitraje internacional, derecho público internacional, amicus curiae, consultoría académica, pro bono, derecho militar, derecho marítimo, derecho agrario, o cualquier otra cosa que las categorías estándar no contemplen), ofrecer: "Parece que tu práctica no cabe en mis categorías habituales. Cuéntame con tus propias palabras — qué haces, para quién, en qué jurisdicciones y foros, cómo se ve el trabajo — y construiré tu perfil desde eso en lugar de forzarte en categorías que no aplican. Omitiré o adaptaré las preguntas que no apliquen." Luego construir el perfil desde la descripción libre, señalando qué campos de plantilla se llenaron, adaptaron, o dejaron vacíos porque no aplican. Un perfil construido desde un ajuste forzado es peor que un perfil escaso construido desde lo que es realmente cierto.

### ¿Qué está conectado?

> Este plugin puede trabajar con: DMS (iManage), almacenamiento de documentos (Google Drive, SharePoint, Box), Gmail, tareas programadas, Portal del Poder Judicial, SCJN IUS (jurisprudencia y tesis aisladas), DOF (Diario Oficial de la Federación). Déjame verificar qué conectores tienes configurados — las funciones que los necesiten funcionarán, y las que no, caerán graciosamente en vez de fallar en silencio.

**Verificar lo que está realmente conectado, no lo que está configurado.** Un conector listado en `.mcp.json` está *disponible*. Un conector que realmente está respondiendo está *conectado*. Estos son diferentes, y confundirlos destruye la confianza. Para cada conector que este plugin usa:

- Si puedes probar la conexión (llamar a una herramienta MCP simple como un listado o búsqueda), reportar ✓ solo con una respuesta exitosa.
- Si no puedes probar (no hay forma de sondear desde aquí), reportar ⚪ "configurado pero no verificado — abre tu configuración MCP para confirmar" con una línea de cómo hacer.
- Nunca reportar ✓ basándose solo en configuración.

Para conectores que muestran como no conectados, decir al usuario cómo conectar. Los servidores MCP ya están preconfigurados a través del plugin `conectores-legal-mexico` (instalado automáticamente como dependencia) — el usuario no necesita agregar nada vía `/mcp`. Solo necesita autenticar:

- **LegalDataHunter (clave API):** "LegalDataHunter no está conectado. Ejecuta `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` e ingresa tu clave API cuando se solicite. La clave se guarda de forma segura en el llavero del sistema. Sin ella, las citas se marcarán como `[model knowledge — verify]` — pero conectarlo permite verificar jurisprudencia, tesis y DOF en tiempo real."
- **OAuth (Box, Slack, Google Drive, iManage):** "Box no está conectado. En Claude Cowork: Configuración → Conectores → Agregar → Box → iniciar sesión. En Claude Code: el servidor MCP ya está configurado — solo autoriza la conexión OAuth. Este plugin funciona sin él — pegarás documentos en lugar de jalarlos — pero conectarlo automatiza los jales de documentos."

Luego reportar hallazgos en esta forma:

> - ✓ [Integración] — conectado (probado)
> - ⚪ [Integración] — configurado pero no verificado. Abre tu configuración MCP para confirmar.
> - ✗ [Integración] — no encontrado. [Función] caerá en [alternativa manual]. [Cómo conectar.]

No necesitas todos estos. Las funciones básicas funcionan solo con acceso a archivos.

Escribir una sección `## Rol de práctica`, `## Quién usa este plugin`, y `## Integraciones disponibles` en la configuración del plugin inmediatamente después de la apertura. Agregar `## Resultados` con la regla de encabezado de producto de trabajo según la plantilla CLAUDE.md.

---

## Ruta de jurídico interno (rol == `jurídico-interno`)

*Omitir toda esta sección si el rol del usuario es `asociado-despacho` o `independiente`.*

> Quiero capturar el marco contra el cual triageas asuntos — tu calibración de riesgo, el panorama de disputas, y cómo escribes. Una vez, para que cada admisión de asunto lea de él. Ofreceré valores predeterminados donde haya valores razonables. Puedes aceptar, editar, o dejar en blanco para volver después.
>
> También pediré documentos semilla en el camino — memorandos previos al Consejo, memos de provisiones, plantillas de retención documental, cartas de demanda ejemplares, un memo de riesgo de muestra. De diez a veinte en total a lo largo de la entrevista es la meta. Cualquier cosa por debajo de diez y señalaré el perfil de práctica como LIMITED DATA en el pie — los skills seguirán funcionando, pero sus resultados serán más delgados porque están coincidiendo con patrones más débiles. Plantillas primero: si subes un ejemplar, lo leeré y solo preguntaré sobre vacíos en lugar de recorrer la estructura completa desde cero.

### Pilar 0 — Perfil de la empresa

Contexto a nivel de equipo. Si otro plugin `-legal` ya tiene un bloque `## Perfil de la empresa` poblado, copiarlo aquí en lugar de re-ingresar.

- Org / persona jurídica
- Industria
- Pública / privada / subsidiaria (si cotiza en la BMV, indicarlo)
- Estatus regulado
- Jurisdicciones clave (operativas + foros frecuentes)
- Número de empleados + tamaño del equipo jurídico
- Contactos internos clave (Director Jurídico, Director de Finanzas, responsable de RH, Comunicación, CISO, Presidente del Comité de Auditoría y Prácticas Societarias del Consejo) — nombres + cuándo involucrar
- Nombre de este abogado y línea de reporte

### Pilar 1 — Calibración de riesgo

> Antes de las preguntas estructuradas: ¿tienes un memo existente de calibración de riesgo, un documento de política de provisiones, o lineamientos de despachos externos que pueda leer? Pega el contenido, comparte rutas de archivo, o di 'no' y recorreré el pilar pregunta por pregunta. Si compartes uno, extraeré las bandas de severidad, umbrales de materialidad y escalera de autoridad y solo preguntaré sobre vacíos.

Si no:

**Apetito de riesgo (2 min)** — en una oración, ¿cómo aborda esta empresa la litigación? (Esto alimenta /matter-briefing y /portfolio-status — establece qué tan conservador o agresivo es cada briefing de asunto al calificar el nivel de riesgo de un asunto.)

**Severidad × probabilidad (3–5 min)** — ofrecer la matriz predeterminada 3×3. Bandas de severidad (detonadores monetarios y no monetarios). Bandas de probabilidad. Si no está articulado: "Entendido. Muchos abogados no lo tienen. ¿Quieres esbozarlo ahora, o dejar el predeterminado?"

**Umbrales de materialidad (2–3 min)** — detonador de provisión, detonador de revelación, Consejo de Administración/Comité de Auditoría y Prácticas Societarias, escalamiento solo al Director Jurídico. *Oportunidad de doc semilla:* plantilla de memo de provisión o checklist de revelación.

**Autorización de convenios (1–2 min)** — escalera por monto, excepciones especiales (la resolución estructural requiere Consejo sin importar el monto).

**Escalamiento en lenguaje llano (1 min).** Preguntar directamente:

> Cuando un asunto necesita algo por encima de tu autoridad — una oferta de convenio por encima de tu banda, una demanda que no puedes responder solo, una decisión de retención documental que necesita al Director Jurídico — ¿a quién va? Dame un nombre, un puesto, o "yo decido."

(Profesionistas independientes: "yo decido" es la respuesta correcta; la pregunta sigue importando para el registro. Si consultas a despacho externo para segundas opiniones, nombra el despacho.)

**Perfil de seguros (1–2 min)** — líneas vigentes (D&O, responsabilidad laboral, ciber, RC profesional), aseguradoras, límites, deducibles, protocolo de aviso a aseguradora.

**Ofrecer:** "Si no subiste un memo de calibración de riesgo, ¿quieres que escriba tu calibración de riesgo y escalera de autoridad como un memo independiente que puedas compartir y mantener?"

### Pilar 2 — Panorama

*El perfil de empresa vive en el Pilar 0. Panorama es específico de litigación.*

- Contexto de negocio (30 seg) — un párrafo sobre qué hacemos y por qué nos demandan.
- Patrones de disputas (2–3 min) — tipos de asuntos, frecuencia, postura.

  | Tipo | Frecuencia | Postura típica | Notas |
  |---|---|---|---|
  | Laboral | | | |
  | Mercantil | | | |
  | PI (propiedad intelectual) | | | |
  | Responsabilidad civil | | | |
  | Regulatorio / Investigaciones | | | |
  | Amparo | | | |
  | Requerimientos (terceros) | | | |

- Adversarios frecuentes (1–2 min).
- Cartera de despachos externos (2–3 min) — despachos, socios líderes, tipo de asunto, postura de honorarios, estatus de carta compromiso. *Doc semilla:* lineamientos de despachos externos. (Esto alimenta /oc-status — el skill luego redacta solicitudes de estatus semanales a estos despachos.)
- Foros frecuentes (30 seg) — Juzgados de Distrito, Tribunales Colegiados, SCJN, CAM (Centro de Arbitraje de México), Tribunales Laborales, TFJA.
- Almacenamiento de documentos (2–3 min) — dónde viven los documentos de asuntos (sistema de archivos, Drive, SharePoint, Box, Gmail, CLM, DMS), patrón predeterminado de carpeta de asunto, cómo se comparten documentos con despacho externo.
- Limpieza de conflictos (1–2 min) — cómo este equipo corre conflictos; quién lo hace; bloqueo duro en admisión o paralelo.

### Pilar 3 — Estilo de casa

> Antes de las preguntas estructuradas: ¿tienes una guía de estilo de casa, una plantilla de memo al Consejo, una plantilla de aviso de retención documental, o cartas de demanda ejemplares que pueda leer? Pega el contenido, comparte rutas de archivo, o di 'no' y recorreré las preguntas.

Si no:

- Memo al Consejo de Administración / Comité de Auditoría y Prácticas Societarias (2 min) — formato, tono, cadencia. *Doc semilla:* memo reciente al Consejo (redactado está bien).
- Memo de provisión — formato y aprobador. *Doc semilla:* memo de provisión de muestra.
- Directivas a despacho externo — formato de email, cadencia, postura presupuestaria.
- Convenciones de secreto profesional — marcado; postura predeterminada para llamadas subjetivas (marcar y señalar); mecánica de revisión (en línea / cola / ambas). (Esto alimenta /litigacion-legal-mexico:revision-confidencialidad — el skill aplica tus reglas de marcado y mecánica de revisión en cada pasada de la bitácora de confidencialidad.)
- Retención documental — plantilla, protocolo de emisión, cadencia de renovación. *Doc semilla:* plantilla de retención. (Esto alimenta /legal-hold — el skill emite, renueva y libera retenciones usando tu plantilla de casa.)
- Escalamiento — normas de canal, convención de línea de asunto.
- Práctica de cartas de demanda — *no se pregunta aquí.* La postura de demanda (tono, plazos, marcado, firmante) se establece por asunto, no por práctica. `/litigacion-legal-mexico:demand-intake` y `/litigacion-legal-mexico:demand-draft` preguntarán cuando lo necesiten — esas decisiones dependen de la relación, el monto, y si el litigio es probable, y un predeterminado a nivel de práctica tiende a descalibrar la carta específica. Lo que la entrevista de configuración *sí* quiere aquí: momento del aviso a aseguradora (a quién notificas y cuándo, antes de enviar) y umbral de materialidad para creación de asunto (por debajo de $X MXN, solo registro; por encima, crear asunto). Esos son a nivel de práctica.

**Ofrecer:** "Si no subiste una guía de estilo de casa o plantillas, ¿quieres que escriba tus reglas de estilo de casa como un memo independiente de estilo?"

---

## Ruta de independiente (rol == `independiente`)

*Omitir toda esta sección si el rol del usuario es `jurídico-interno` o `asociado-despacho`. Los usuarios independientes ejecutan esta ruta **y** la Ruta de asociado de despacho que sigue.*

> La práctica independiente tiene su propio marco — carga de asuntos, expectativas del cliente, economía de iguala o contingencia, administración del despacho. El mundo del jurídico interno (provisiones NIF C-9, memorandos al Consejo, supervisión de despacho externo, escaleras de autorización de convenios hasta un Director Jurídico) no aplica aquí, y no voy a pretender que sí. Las preguntas de provisiones del mundo corporativo tampoco aplican. Lo que necesito de ti es la forma de tu carga real de asuntos y cómo manejas tu práctica.
>
> Algunos documentos semilla ayudan — una carta de demanda previa, un contrato de iguala, un email de actualización al cliente que estés dispuesto a compartir como ejemplar. Cualquier cosa que podamos aprender ahorra un viaje redondo después.

### Sección S1 — Forma de práctica y carga de asuntos

- **Tamaño de carga** — ¿aproximadamente cuántos asuntos activos llevas a la vez? ¿Cuántos son demasiados?
- **Mezcla de asuntos** — porcentajes aproximados: actor vs demandado, áreas de práctica (p. ej., laboral, mercantil, PI, responsabilidad civil, familiar, arrendamiento). No necesitas ser preciso; una oración es suficiente.
- **Jurisdicciones** — el/los estado(s) y tribunales donde practicas principalmente. Incluir federal si es relevante.
- **Duración típica del caso** — ¿semanas, meses, años? Útil para que los skills posteriores escalen esfuerzo y horizontes de plazos.
- **Señales de capacidad** — ¿hay un punto donde dejas de aceptar casos? ¿Cómo sabes que estás sobre capacidad?

### Sección S2 — Expectativas del cliente y economía

*Esto reemplaza lo que la ruta de jurídico interno llama "calibración de riesgo / metodología de provisiones / escalera de autorización de convenios." Los independientes no manejan provisiones y no escalan a un Director Jurídico; las mismas decisiones se presentan como economía orientada al cliente.*

**Estructura de honorarios (el motor principal).** Elige la que describe la mayoría de tu trabajo:

- **Contingencia** (asunción predeterminada para lado actor en laboral, consumo): ¿cuál es tu porcentaje estándar? ¿Pre-juicio vs post-juicio? ¿Postura de adelanto de gastos — cliente, despacho, híbrido? ¿A qué exposición dejas de tomar un caso en contingencia?
- **Por hora / iguala**: tarifa por hora, iguala estándar, mecánica de cuenta de depósito.
- **Cuota fija**: qué tipos de asunto, y el rango de cuota.
- **Mixto**: describe la mezcla.

**Expectativas del cliente (2 min).** Preguntar directamente:

- ¿Con qué frecuencia actualizas a clientes sobre sus asuntos (semanal, mensual, por evento)?
- ¿Qué forma toman las actualizaciones — llamada, email, carta, portal de cliente?
- ¿Cuál es tu postura predeterminada sobre conversaciones de convenio con el cliente (empujar agresivamente a convenir, dejar que el cliente dirija, depende del caso)?

**Lectura de exposición / valor del caso (lado actor).** ¿Cuál es tu marco mental rápido para decidir si un caso vale la pena tomarlo? Ejemplos: "responsabilidad clara, daños >$1M MXN, prescripción tiene un año o más, cliente creíble" — sin juicio sobre los detalles; solo capturar el tuyo.

**Lectura de exposición (lado demandado independiente — menos común pero posible).** ¿Cuál es tu modelo mental de exposición aceptable vs reportable al cliente? La defensa independiente usualmente es para personas o pequeñas empresas sin capa de seguro — capturar cómo realmente piensas sobre esto.

**Cuándo llamas por ayuda.** Los independientes no tienen un Director Jurídico o socio arriba, pero la mayoría tienen a alguien — co-abogado, un mentor, un grupo de colegas, un comité del Colegio de Abogados. ¿A quién llamas para una segunda opinión, y sobre qué tipo de asuntos?

> Dame un nombre, un puesto, o "nadie — yo decido solo."

**Actualizaciones al cliente por escrito (1 min).** *Oportunidad de doc semilla:* un email o carta reciente de actualización al cliente (redactado). Este es el equivalente independiente de un memorando al Consejo del jurídico interno — es cómo comunicas estatus a tu interesado. Si el usuario comparte uno, leerlo y extraer la estructura y tono para la sección de estilo de casa.

### Sección S3 — Administración del despacho y panorama

*Omitir cualquier pregunta donde la respuesta sea obvia del contexto anterior.*

- **Seguimiento de prescripción** — ¿cómo rastreas los vencimientos de prescripción a lo largo de la carga de asuntos? (Calendario, software de gestión, un expediente en papel, memoria — lo que sea real.) Este es el equivalente independiente del "detonador de materialidad / provisión" del jurídico interno porque perder una prescripción es el modo de falla que termina una carrera independiente.
- **Software de gestión de casos** — Clio, MyCase, PracticePanther, Smokeball, expedientes en papel, hojas de cálculo, otro.
- **Almacenamiento de documentos** — Google Drive, Dropbox, OneDrive, sistema de archivos local, almacenamiento del software de gestión. ¿Dónde viven realmente los documentos de asuntos?
- **Foros frecuentes** — tribunales donde realmente compareces: Juzgados de Distrito, Tribunales Laborales, Juzgados Civiles/Mercantiles locales, etc.
- **Partes y abogados adversarios frecuentes** — jugadores recurrentes que ves regularmente del otro lado.
- **Cartera de co-abogados / abogados de referencia** — ¿a quién asocias para casos fuera de tu zona de confort? ¿Quién te refiere casos?
- **Limpieza de conflictos** — ¿cómo corres conflictos? La versión independiente usualmente es informal (memoria + revisión de lista de clientes), lo cual está bien — capturar lo que es.

### Estilo de casa del independiente

Omitir las preguntas de memo al Consejo / memo de provisión / directivas a despacho externo por completo. El estilo de casa del independiente es:

- **Actualización al cliente** — formato, tono, cadencia. *Doc semilla:* una carta o email reciente de actualización.
- **Contrato de iguala / carta compromiso** — plantilla. *Doc semilla:* el ejemplar (redactado está bien).
- **Convenciones de secreto profesional** — marcado; mecánica de revisión.
- **Retención documental** — aun para un independiente, el deber de conservación importa cuando se anticipa litigio (Cód. Comercio arts. 46–49). Plantilla, si existe. *Doc semilla:* aviso de retención si se ha emitido.
- **Práctica de cartas de demanda** — *no se pregunta aquí.* La postura de demanda (tono, plazos, marcado, firmante) se establece por asunto, no por práctica — el equivalente independiente de "quién firma" se responde solo (tú), y tono/marcado/tiempo dependen de la disputa específica. `/litigacion-legal-mexico:demand-intake` preguntará cuando redacte.

**Ofrecer:** "Si no subiste un ejemplar de actualización al cliente o iguala, ¿quieres que escriba tus reglas de estilo de casa como un memo independiente que puedas reutilizar?"

Después de la Sección S3, continuar a la **Ruta de asociado de despacho** a continuación. Los profesionistas independientes redactan escritos, construyen cronologías y preparan pruebas como los asociados de despacho — el trabajo de teoría del caso y escrito semilla aplica.

---

## Ruta de asociado de despacho (rol == `asociado-despacho` o `independiente`)

> Antes de tocar un documento, necesito la teoría. ¿Cuál es nuestra historia? ¿Cuál es la de ellos? ¿De qué depende el caso? Luego necesito ver cómo escribe tu despacho — un escrito del que estés orgulloso — para que mis borradores no parezcan de otro lado.

### Parte A: El asunto (2 min)

- Nombre del asunto, cliente, número de expediente, juzgado/tribunal
- Nuestro lado (actor / demandado)
- Socio y asociado senior (omitir si independiente / pequeño sin jerarquía)
- Etapa procesal (instrucción, etapa probatoria, alegatos-sentencia, preparación de audiencia)
- Fechas clave próximas

### Parte B: La teoría — esto es todo (3–4 min)

> Dime nuestra teoría del caso. No la demanda — la historia. Si tuvieras que decirle a un juez por qué ganamos en dos oraciones, ¿cuáles son?

- Nuestra teoría en un párrafo
- Su teoría en un párrafo (conoce al otro lado)
- **El hecho determinante** — el hecho del que depende el caso
- Hechos clave a nuestro favor
- Hechos clave en nuestra contra (los que te preocupan)
- La cuestión jurídica que más importa

### Parte C: Documentos semilla (3–4 min)

> Dos cosas:
>
> 1. **El memo de teoría del caso**, si existe. Si la teoría vive en la cabeza de alguien y no en papel, está bien — la acabamos de capturar arriba.
>
> 2. **Un escrito previo en estilo de casa.** No de este caso — de cualquier caso. El mejor que tengas. Aprenderé tu estilo de citas, estructura, tono, cómo organizas argumentos. (Esto alimenta /litigacion-legal-mexico:redaccion-escritos — cada futura sección de escrito se redactará en tu formato de cita extraído, estructura de encabezados y tono, no una plantilla genérica.)

**Del escrito:** formato de cita (Ley, artículo, fracción, inciso para legislación; Época, Registro Digital, Instancia, Materia, Tesis, Página para jurisprudencia y tesis aisladas), estructura de secciones, convenciones de encabezados, tono (agresivo / mesurado), normas de extensión.

### Parte D: Configuración de revisión documental (1–2 min)

> Antes de las preguntas: ¿tienes un formato de bitácora de confidencialidad, un formato de cronología, o un documento de protocolo de revisión que pueda leer? Pega el contenido, comparte rutas de archivo, o di 'no' y preguntaré una por una.

Si no:
- Plataforma de gestión documental (Box, iManage, sistema local)
- Protocolo de revisión — categorías de codificación, quién toma las decisiones de secreto profesional
- Formato de bitácora de confidencialidad
- Custodios clave y rango de fechas

**Ofrecer:** "Si no subiste una bitácora de confidencialidad o formato de cronología, ¿quieres que escriba tu protocolo de revisión y formato de bitácora de confidencialidad como una referencia independiente que puedas compartir con un equipo de revisión?"

---

## Antes de escribir — releer

Antes de comprometer la configuración del plugin, releer cada respuesta capturada en orden. Esto atrapa tres categorías de error:

1. **Contradicciones entre respuestas** — p. ej., el usuario dijo "pelear todo" en apetito de riesgo y "convenir rápido" en predeterminado de carta de demanda. Mostrar ambas, preguntar cuál gobierna.
2. **Datos que cambiaron** — nombres, fechas, umbrales que cambiaron entre secciones. Confirmar el valor final.
3. **Vacíos que vale la pena nombrar** — secciones en blanco que el usuario podría querer completar ahora en lugar de vía `--redo`.

También: si el rol es `asociado-despacho`, verificar que el hecho determinante y el escrito semilla fueron capturados. Estos son elementos de carga. Si falta alguno, nombrarlo explícitamente antes de escribir.

## Escribir el perfil de práctica

Escribir el perfil de práctica completado en la configuración del plugin, usando la plantilla en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` como andamio de secciones. Llenar cada sección capturada; dejar `[PLACEHOLDER]` para secciones que el usuario omitió. Fechar el pie de página.

**Secciones por rol:**

- `jurídico-interno` → estructura completa de jurídico interno (Perfil de la empresa, Calibración de riesgo con provisiones NIF C-9 / revelación BMV-CNBV / filas de memo al Consejo, Cartera de despachos externos, Memo al Consejo de Administración/Comité de Auditoría). Omitir o marcar N/A para secciones solo de independiente (estructura de honorarios, iguala, contingencia).
- `asociado-despacho` → estructura de despacho (teoría del caso, hecho determinante, revisión del socio, escrito semilla). Omitir secciones de provisión / memo al Consejo / NIF C-9; omitir secciones de honorarios / iguala del independiente.
- `independiente` → estructura de independiente (carga de asuntos, estructura de honorarios, expectativas del cliente, seguimiento de prescripción, iguala o contingencia, administración del despacho) **más** las secciones de asociado de despacho (teoría del caso, escrito semilla). Omitir secciones de provisión NIF C-9 / memo al Consejo / escalera-de-autorización-de-convenios-hasta-Director-Jurídico del jurídico interno por completo — no son el marco adecuado para una práctica independiente e incluirlas como placeholders agrega ruido en lugar de estructura.

Donde una sección de plantilla lleve vocabulario de solo-jurídico-interno ("provisiones NIF C-9", "memo al Consejo de Administración / Comité de Auditoría"), ya sea omitir la sección para roles no de jurídico interno o traducir el vocabulario al concepto equivalente independiente o de despacho. Equivalente independiente de "memo al Consejo" es "carta de actualización al cliente." Equivalente independiente de "metodología de provisiones" es "lectura de valor del caso" (actor) o "lectura de exposición" (demandado). No llevar el lenguaje de normas contables a un perfil independiente.

**Bandera LIMITED DATA:** si se compartieron menos de 10 documentos semilla a lo largo de la entrevista, agregar una nota `> LIMITED DATA` al inicio (bajo la fecha de escritura): "Este perfil de práctica fue escrito desde [N] documentos semilla y respuestas de entrevista. Los skills posteriores operarán pero los resultados serán más delgados hasta que se agreguen más ejemplares. Re-ejecuta `/cold-start-interview --redo` después de recolectar más plantillas para afinar la calibración."

## Mostrar vacíos

Después de la entrevista, antes de escribir, resumir y **esperar una respuesta**:

> Esto es lo que capturé. Vacíos que noté:
> - [listar secciones omitidas, placeholders en blanco, preguntas donde el usuario dijo "vuelvo después"]
>
> ¿Quieres llenar alguno de estos ahora, o dejarlos como placeholders? También puedes llenarlos después vía `/litigacion-legal-mexico:cold-start-interview --redo` o editando la configuración del plugin directamente. Este vale la pena pensarlo antes de que escriba: [nombrar el vacío más importante y por qué].

No proceder a escribir hasta que el usuario responda.

## Después de escribir

**Mostrar qué puede hacer este plugin.** Antes de cerrar, ofrecer:

> **¿Quieres ver en qué puedo ayudarte?**

Si sí, mostrar esta lista personalizada (no una plantilla genérica — estas son las cosas concretas que este plugin hace mejor):

> **Esto es en lo que soy bueno en la práctica de litigación:**
>
> - **Admitir un nuevo asunto** — p. ej., "Preguntas uniformes de admisión, escribe matter.md + history.md, agrega a la bitácora del portafolio." Prueba: `/litigacion-legal-mexico:matter-intake`
> - **Triagear una demanda recibida** — p. ej., "Análisis de opciones, cruce con el portafolio, pase a admisión si califica." Prueba: `/litigacion-legal-mexico:demand-received`
> - **Redactar una carta de demanda** — p. ej., "Compuerta de conciliación/secreto profesional, resultado .docx, checklist post-envío, oferta de creación de asunto." Prueba: `/litigacion-legal-mexico:demand-draft`
> - **Preparar pruebas y testimoniales** — p. ej., "Documentos + temas + contradicciones + probanzas, atados a la teoría del caso." Prueba: `/litigacion-legal-mexico:preparacion-pruebas`
> - **Emitir o renovar una retención documental** — p. ej., "Redactar el aviso de retención, actualizar la bitácora, programar renovación." Prueba: `/litigacion-legal-mexico:legal-hold`
> - **Consolidación del portafolio** — p. ej., "Distribución de riesgo, plazos próximos, asuntos sin movimiento a lo largo del portafolio activo." Prueba: `/litigacion-legal-mexico:portfolio-status`
>
> **Mi sugerencia para la primera:** Ejecuta `/litigacion-legal-mexico:portfolio-status` — te muestra de un vistazo dónde está el portafolio, y es sin datos de entrada para probar. O dime qué tienes pendiente y yo elijo.

Esto resuelve el problema de arranque en frío (el usuario no sabe qué hacer primero) y el problema de propuesta de valor (no sabe qué puede hacer el plugin) en una sola oferta. Hacer la lista específica. Omitir este paso si el usuario ya nombró una primera tarea concreta durante la entrevista.

- Si `jurídico-interno`: "El perfil de práctica de jurídico interno ya está escrito. Cada admisión de asunto leerá de él. ¿Quieres ejecutar `/litigacion-legal-mexico:matter-intake` en tu asunto más vivo para verlo en acción?"
- Si `asociado-despacho`: "Aquí está la teoría como la capturé. Lee el hecho determinante — ¿lo tengo bien? ¿Cuál es el siguiente plazo? Empecemos ahí."
- Si `independiente`: "Tu perfil de práctica independiente está escrito — forma de carga de asuntos, economía de honorarios, cómo manejas el despacho — más la teoría del caso y estilo de escritos para un asunto vivo. ¿Quieres ejecutar `/litigacion-legal-mexico:matter-intake` en tu asunto más vivo y ver cómo se ve la admisión con tu configuración?"

### Cerrar con la nota de "puedes cambiar todo después"

> "Tu perfil de práctica está en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — un archivo de texto plano que puedes leer y editar directamente. Cualquier cosa que respondiste se puede cambiar:
>
> - Editar el archivo directamente para un cambio rápido
> - Ejecutar `/litigacion-legal-mexico:cold-start-interview --redo` para una re-entrevista completa
> - Ejecutar `/litigacion-legal-mexico:cold-start-interview --new-matter` para reutilizar el perfil de práctica en un nuevo asunto (asociado de despacho / independiente)
> - Ejecutar `/litigacion-legal-mexico:cold-start-interview --check-integrations` para re-verificar qué está conectado
>
> Las secciones que la gente ajusta más: para jurídico interno, los **umbrales de severidad × probabilidad** y la **cartera de despachos externos**; para asociado de despacho, la **teoría del caso** (especialmente el hecho determinante) y el **estilo de escritos** extraído del escrito semilla; para independiente, la **estructura de honorarios** (porcentaje de contingencia o tarifa por hora) y el **lado predeterminado** (actor / demandado) — un predeterminado incorrecto ahí sesga cada resultado de carta de demanda y cronología. Cuando un resultado se siente desafinado, la corrección usualmente está aquí."

### Antes de tu primer asunto

**Conectar una herramienta de investigación.** Sin una, señalaré cada cita como no verificada — con una, las verifico contra una base de datos actualizada. Para el sistema jurídico mexicano: SCJN IUS (jurisprudencia y tesis aisladas), DOF (Diario Oficial de la Federación), o el Portal del Poder Judicial. En Cowork: Configuración → Conectores. En Claude Code: autoriza cuando un skill te lo solicite.

<!-- COLLATERAL LINKS: cuando exista material de onboarding, agregar aquí:
     "¿Quieres una guía? [Ve la intro de 3 minutos](URL) o [lee la guía de inicio rápido](URL)." -->

### Tu perfil de práctica aprende

Después de escribir el perfil de práctica, cerrar con esta nota:

> **Tu perfil de práctica aprende.** Mejora conforme usas los plugins:
>
> - Cuando el resultado de un skill se siente desafinado, eso usualmente es una posición que ajustar. El resultado te dirá cuál.
> - Siempre puedes decir "actualiza mi playbook para preferir X" o "cambia mi umbral de escalamiento a Y" y el skill relevante escribirá el cambio.
> - Ejecuta `/cold-start-interview --redo <sección>` para re-entrevistar una parte, o edita el archivo de configuración directamente.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que se lee como si lo hubieras escrito tú.

## Qué no hace este skill

- Decidir el marco por el usuario. Los predeterminados son puntos de partida; el juicio del usuario es el contenido real.
- Pretender que los vacíos no están ahí. Mejor dejar `[PLACEHOLDER]` honestamente que inventar un umbral.
- Pelear con el usuario. Si dicen "eso no lo tengo aún," anotarlo y seguir adelante.
- Leer `~/CLAUDE.md` personal u otro contexto ambiental sin preguntar.
