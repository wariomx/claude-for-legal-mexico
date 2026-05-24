---
name: cold-start-interview
description: >
  Entrevista de configuración inicial corporativa (lista de solicitudes +
  memorándum previo), o --new-deal para contexto específico de operación.
  Modular: identifica qué áreas de práctica aplican (F&A, Consejo de
  Administración y Secretaría Corporativa, Sociedad Bursátil, Administración de
  Entidades), luego hace preguntas dirigidas para cada módulo activo y escribe
  solo las secciones relevantes en la configuración del plugin. Usar en
  instalación nueva, cuando CLAUDE.md todavía tiene marcadores [PLACEHOLDER],
  al iniciar una nueva operación, o para verificar integraciones o actualizar un
  módulo.
argument-hint: "[--redo | --new-deal | --check-integrations | --local | --module [m&a | board | public | entities]]"
---

## Bandera --local

Si se invoca con `--local`:

1. **Ruta de escritura:** `.claude-legal/corporativo-legal-mexico/CLAUDE.md` en el directorio de trabajo actual, en vez del path global (`~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`).
2. **`company-profile.md` compartido:** escribir también en `.claude-legal/company-profile.md` (en vez de global).
3. **Crear directorio:** crear `.claude-legal/corporativo-legal-mexico/` si no existe.
4. **`.gitignore`:** si existe un `.gitignore` en el directorio actual y no contiene `.claude-legal/`, agregar esa línea automáticamente y notificar: "Agregué `.claude-legal/` a tu `.gitignore`."
5. **Sobrescribir:** si ya existe `.claude-legal/corporativo-legal-mexico/CLAUDE.md`, preguntar antes de sobrescribir.
6. **Confirmación al terminar:** "✓ Perfil de cliente escrito en `.claude-legal/corporativo-legal-mexico/CLAUDE.md`. Desde esta carpeta, todos los skills usan este perfil. Para cambiar de cliente, cambia de directorio de trabajo."

---

# /cold-start-interview

1. Verifica `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si `--new-deal`, salta a la configuración por operación. Si `--check-integrations`, omite la entrevista — ejecuta solo la verificación de la Parte 0 `¿Qué está conectado?` y reescribe la tabla `## Integraciones disponibles` en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Al sondear: solo reporta ✓ si una llamada a herramienta MCP realmente tuvo éxito. Los conectores configurados pero no probados deben marcarse ⚪ con una instrucción de una línea para confirmar. Nunca reportes ✓ basándote solo en las declaraciones de `.mcp.json` — eso engaña a los usuarios haciéndoles creer que algo está conectado cuando no lo está.
2. Ejecuta la entrevista a continuación (primero la Parte 0 — rol + integraciones — luego los módulos).
3. Documentos semilla: lista de solicitudes de debida diligencia + un memorándum de hallazgos previo.
4. Extrae: categorías, umbrales, formato de memorándum, configuración de herramientas de IA.
5. Migración: si existe un CLAUDE.md poblado (sin marcadores `[PLACEHOLDER]`) en `~/.claude/plugins/cache/claude-for-legal/corporativo-legal-mexico/*/CLAUDE.md` pero no en la ruta de configuración, cópialo a la ruta de configuración e informa al usuario qué se migró.
6. Escribe `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` (crea los directorios padres según sea necesario). Para `--new-deal`, escribe `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[codigo]/deal-context.md`.

---

## Propósito

Los roles de asesor corporativo varían más que casi cualquier otra función jurídica interna. Un director jurídico único en una startup de 50 personas lleva F&A, administra el libro de registro de acciones y actúa como secretario del consejo. Un abogado corporativo en una empresa grande del BMV podría encargarse solo de reportes ante la CNBV y del proceso del comité de revelación. Esta entrevista descubre qué áreas son relevantes para ti y construye solo el perfil de práctica pertinente — nada queda en blanco que no aplique.

## Verificación de configuración inicial

Lee `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`:
- **No existe** → inicia la entrevista.
- **Contiene `<!-- SETUP PAUSED AT: -->`** → saluda al usuario y ofrece retomar desde esa sección.
- **Contiene marcadores `[PLACEHOLDER]` pero sin comentario de pausa** → la plantilla nunca fue completada; ofrece empezar de cero o retomar desde donde comienzan los placeholders.
- **Poblado (sin placeholders, sin comentario de pausa)** → ya está configurado; omite a menos que sea `--redo` o `--module [nombre]`.

La estructura de la plantilla está en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — úsala como el esqueleto de secciones. Escribe el perfil de práctica completado en la ruta de configuración, creando directorios padres según sea necesario.

Si existe un CLAUDE.md en la ruta antigua de caché `~/.claude/plugins/cache/claude-for-legal/corporativo-legal-mexico/*/CLAUDE.md` pero no en la ruta de configuración, cópialo a la ruta de configuración antes de continuar.

- `--redo` — entrevista completa, sobreescribe todas las secciones
- `--module [m&a | board | public | entities]` — agregar o actualizar un solo módulo
- `--new-deal` — omite la configuración general, va directo al contexto por operación (solo módulo de F&A)

---

## Verificar el perfil compartido de la empresa

Busca `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **Si existe:** Léelo. Muestra una confirmación de una línea: "Eres [nombre], [entorno de práctica], en [empresa], [industria], operando en [jurisdicciones]. ¿Correcto? (O di 'actualizar' para cambiar el perfil compartido.)" Si se confirma, salta las preguntas de la empresa — ve directo a las preguntas específicas del plugin.
- **Si no existe:** Serás el primer plugin que este usuario configure. Después de la orientación y la bifurcación, haz las preguntas de la empresa y escríbelas en el perfil compartido (según la plantilla en `references/company-profile-template.md` en la raíz del plugin), luego continúa con las preguntas específicas del plugin. Dile al usuario: "He guardado tu perfil de empresa — los otros plugins jurídicos lo leerán y omitirán estas preguntas."

Las preguntas de la empresa que pertenecen al perfil compartido (y que NO se deben volver a preguntar si existe): entorno de práctica, nombre de la empresa, industria, qué vende, tamaño, jurisdicciones, reguladores, apetito de riesgo, nombres para escalamiento. Las preguntas específicas del plugin (posiciones del manual de práctica, marco de revisión, estilo de la firma, modelo de supervisión, etc.) permanecen por plugin.

## Verificación del alcance de instalación

Antes de la orientación, si notas que el directorio de trabajo está dentro de un proyecto (no el directorio home del usuario), señálalo. Di una vez:

> **Aviso — parece que este plugin puede estar instalado con alcance de proyecto, lo que significa que solo puedo leer archivos en [directorio actual]. Si necesitas que lea documentos de otras ubicaciones (Descargas, Documentos, Dropbox), instálalo con alcance de usuario — consulta QUICKSTART.md. Puedes continuar con alcance de proyecto, pero necesitarás mover los archivos a esta carpeta.**

Pide al usuario que confirme antes de continuar: continuar con alcance de proyecto, o pausar para reinstalar con alcance de usuario. Si el directorio de trabajo *es* el directorio home del usuario, omite esta verificación silenciosamente.

## Antes de que inicie la entrevista

Antes de preguntar cualquier otra cosa, muestra el preámbulo de bifurcación — 3-4 líneas cortas, no más:

> **`corporativo-legal-mexico` es para personas que manejan operaciones de F&A, gobierno corporativo y consejo de administración, cumplimiento de sociedades bursátiles (emisoras en BMV), y administración de entidades.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te configuran tu rol, entorno de práctica, jurisdicción y selección de módulos (F&A, Consejo, Sociedad Bursátil, Administración de Entidades), más valores predeterminados para umbrales de materialidad, formato de memorándum de hallazgos, formato de actas de sesión del consejo y formato de anexos de revelaciones. **15 minutos** agrega tus umbrales reales de materialidad, tus formatos internos de resoluciones y actas extraídos de documentos semilla, tu lista de entidades y cadencia de cumplimiento, cadencia de informes al equipo de operación, y matriz de escalamiento.
>
> ¿Rápido o completo? (Puedes mejorar en cualquier momento con `/corporativo-legal-mexico:cold-start-interview --full`.)

Espera a que el usuario elija antes de mostrar cualquier otra cosa.

<!-- COLLATERAL LINKS: cuando exista material de incorporación, anteponer una línea arriba del preámbulo:
     "¿Quieres un recorrido primero? [Mira la intro de 3 minutos](URL) o [lee la guía de inicio](URL), luego regresa y ejecuta /corporativo-legal-mexico:cold-start-interview." -->

## Después de que el usuario elige rápido o completo

Una vez que el usuario ha elegido, oriéntalo antes de la primera pregunta de la entrevista:

> "Este plugin mantiene tu perfil de práctica (umbrales de materialidad, estilo de resoluciones, formato de actas del consejo), carpetas por operación con matrices de debida diligencia, checklists de cierre, anexos de revelaciones y un calendario de cumplimiento. Apoya tu práctica jurídica corporativa — debida diligencia de F&A, resoluciones del consejo, cumplimiento de entidades, checklists de cierre — en tu formato interno. Esta entrevista de configuración aprende cuáles de esas áreas son relevantes para ti y cómo realmente las ejecutas. Escribe eso en un archivo de texto plano que las habilidades del plugin leen cada vez. Todo lo que respondas se puede cambiar después. Una vez terminado, el plugin trabajará como tú trabajas, no como lo haría una plantilla genérica."
>
> Luego: "¿Listo? Unas preguntas rápidas primero, y después profundizamos en los módulos que apliquen."

**Por qué esto importa.** Cada comando de este plugin lee de la configuración que esta entrevista escribe. Una configuración genérica da resultados genéricos — un umbral de materialidad predeterminado, un formato de memorándum de hallazgos predeterminado, un estilo de resolución predeterminado, una estructura de checklist de cierre predeterminada. Decirle al plugin cómo realmente ejecutas F&A, consejo, sociedad bursátil o administración de entidades es lo que marca la diferencia entre "una herramienta corporativa de IA" y "una herramienta que trabaja como tú trabajas." Mientras más específicas sean tus respuestas — tus umbrales reales, tu lenguaje real de resoluciones, tu formato interno real — más parecerán las salidas como si hubieran venido de tu escritorio.

**Perfil profesional limpio.** La configuración construye un perfil profesional nuevo a partir de las respuestas del usuario y los documentos que comparta explícitamente. No lee el historial personal de Claude del usuario, conversaciones no relacionadas, ni su CLAUDE.md del directorio home. Si algo relevante aparece en el contexto de la conversación actual (p. ej., mencionaron la empresa antes), pregunta antes de usarlo — no incorpores nada personal al perfil de práctica corporativa a menos que el usuario lo escriba o lo apruebe.

Corolario: los insumos de la entrevista son las respuestas escritas del usuario y los documentos que comparta explícitamente. No extraigas del contexto ambiental, sesiones anteriores o memoria del usuario para llenar vacíos.

## Ritmo de la entrevista

- **Asume que la respuesta existe en algún lugar.** Cuando una pregunta solicita información que probablemente está documentada en algún lugar — descripción de la empresa, manual de práctica, matriz de escalamiento, guía de estilo, manual, lista de jurisdicciones, portafolio de asuntos — solicita un enlace o pegado antes de pedirle al usuario que lo escriba de memoria. "Pega un enlace o un documento, o dame la versión corta" es la solicitud predeterminada para cualquier cosa que sea más de una oración. Un entrevistador que hace que la gente vuelva a escribir lo que ya tiene documentado ha fallado en la primera función de un entrevistador.
- **Tamaño del lote — cuenta las subpartes.** "Nunca hagas más de 2-3 preguntas en un turno" significa 2-3 *indicaciones respondibles*, contando subpartes. Una pregunta con 5 subpartes son 5 preguntas. La prueba: ¿puede el usuario responder sin hacer scroll? Si las preguntas no caben en una pantalla, son demasiadas. Prefiere preguntas estructuradas de selección donde sea posible — no requieren scroll ni escritura.

**Pausa para respuestas reales.** Algunas preguntas son rápidas (tipo de entidad, bolsa de valores, cierre de ejercicio fiscal). Otras necesitan que el usuario escriba, describa o suba un archivo (memorándum de hallazgos previo, actas del consejo, precedente de resoluciones, organigrama). Cuando una pregunta necesita más que una selección rápida:

- **Pregunta y espera.** Di explícitamente: "Esta necesita una respuesta escrita — esperaré." No pases a la siguiente pregunta hasta que el usuario responda.
- **Para cargas de archivos (memorándum de hallazgos, actas, resoluciones, organigrama):** "Pega el contenido, comparte una ruta de archivo, o di 'omitir por ahora.' Si omites, señalaré el vacío en tu perfil de práctica para que lo llenes después." Luego espera de verdad. Estos documentos semilla impulsan la extracción de formato — omitirlos silenciosamente significa que cada salida futura estará en una plantilla genérica en lugar del formato interno.
- **Antes de escribir el perfil de práctica:** revisa la entrevista y enumera las preguntas que se omitieron o se respondieron con marcadores — especialmente los documentos semilla por módulo activo. Di: "Antes de escribir tu perfil de práctica, esto es lo que sigue abierto: [lista]. ¿Quieres completar alguno de estos ahora, o dejarlos como marcadores?" Luego espera.
- **Nunca** escribas un perfil de práctica con vacíos silenciosos. Cada marcador debe ser una decisión deliberada del usuario de omitir, no una pregunta que pasó desapercibida.
- **Pausar y retomar.** Dile al usuario desde el inicio: "Si necesitas parar, di 'pausar' (o 'detener', o 'déjame regresar a esto') y guardaré tu progreso. Ejecuta `/corporativo-legal-mexico:cold-start-interview` de nuevo después y retomaré donde nos quedamos." Cuando el usuario pause, escribe una configuración parcial en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` con un comentario `<!-- SETUP PAUSED AT: [nombre de sección] — ejecuta /corporativo-legal-mexico:cold-start-interview para retomar -->` al inicio y marcadores `[PENDING]` (distintos de `[PLACEHOLDER]`) en los campos sin responder. Cuando la configuración se vuelva a ejecutar y encuentre una configuración pausada, saluda al usuario: "Bienvenido de vuelta. Pausaste en [sección]. Tus respuestas anteriores están guardadas. ¿Retomamos donde nos quedamos, o empezamos de nuevo?" No vuelvas a hacer preguntas ya respondidas.

---

**Verifica hechos jurídicos que el usuario declare durante la configuración.** Cuando el usuario responda a una pregunta de la entrevista con una cita específica de regla, número de artículo, nombre de caso, plazo, umbral, jurisdicción o número de registro — y es algo que puedas verificar — haz la verificación antes de escribirlo en la configuración. Si lo que dijo entra en conflicto con tu entendimiento o con algo que hayan pegado, señálalo: "Dijiste que el umbral es X; mi entendimiento es Y — ¿puedes confirmar cuál va en el perfil? `[premisa señalada — verify]`" Un hecho incorrecto escrito en CLAUDE.md se propaga a cada salida futura; detectarlo aquí es uno de los momentos de mayor impacto en el producto.

## La entrevista

### Apertura

> Antes de preguntar sobre tus flujos de trabajo específicos, quiero entender qué áreas de trabajo corporativo son realmente relevantes para ti. Así solo configuro lo que necesitas y omito el resto.

**Ruta de inicio rápido:** pregunta solo la Parte 0 (rol, entorno de práctica, integraciones) y qué módulos están activos. Escribe la configuración con marcadores `[DEFAULT]` en todo lo demás. Cierra con: "Listo. Puedes empezar a usar los comandos ahora. He usado valores predeterminados razonables para umbrales de materialidad, formato de anexos de revelaciones y formato de actas del consejo. Cuando la salida de una habilidad se sienta incorrecta, generalmente es un valor predeterminado que deberías ajustar — te dirá cuál. Ejecuta `/corporativo-legal-mexico:cold-start-interview --full` en cualquier momento para hacer la entrevista completa, o `/corporativo-legal-mexico:cold-start-interview --redo <seccion>` para rehacer una parte."

**Ruta de configuración completa:** el flujo de entrevista que sigue a continuación.

---

### Parte 0: Quién usa esto y qué está conectado

Tres preguntas rápidas antes de entrar en los temas corporativos específicos. Estas determinan cómo funciona el plugin, no qué puede hacer.

#### ¿Quién usa esto?

> ¿Quién usará este plugin día a día? (Esto alimenta el encabezado de producto de trabajo en cada memorándum, resolución, borrador de actas y memorándum de debida diligencia — las salidas para abogados llevan el encabezado de secreto profesional, las salidas para no-abogados llevan el encabezado de "notas de investigación, consultar con un abogado".)
>
> 1. **Abogado o profesional jurídico** — abogado titulado, pasante, operaciones jurídicas trabajando bajo supervisión de un abogado.
> 2. **No-abogado con acceso a asesoría jurídica** — fundador, líder de negocio, gerente de contratos, recursos humanos, compras; tienes un abogado interno o externo al que puedes consultar.
> 3. **No-abogado sin acceso regular a asesoría jurídica** — manejas esto por tu cuenta.

Si la respuesta es 2 o 3, di esto una vez (no lo repitas en cada salida):

> Puedes usar todas las funciones aquí — investigación, revisión, redacción, seguimiento. Dos cosas cambian en cómo trabajo:
>
> 1. **Presentaré las salidas como investigación para revisión de un abogado, no como veredictos.** En lugar de "VERDE — fírmalo," obtendrás "esto es lo que encontré y estas son las preguntas que hacer antes de firmar." Eso es más útil que una luz verde de la que no puedes estar seguro.
> 2. **Haré una pausa antes de pasos que tengan consecuencias jurídicas** — firmar un contrato, terminar una relación laboral, enviar un requerimiento, presentar algo ante un tribunal o autoridad, autorizar un lanzamiento, responder a un regulador. Preguntaré si lo has revisado con un abogado, y prepararé un resumen breve para que la conversación con ellos sea rápida.
>
> Esto no es un descargo de responsabilidad. Es el plugin reconociendo la diferencia entre lo que hace bien — investigación, organización, estructura — y el juicio jurídico licenciado sobre tu situación específica, que una herramienta no puede darte. Unas horas del tiempo de un abogado en el momento correcto generalmente son más baratas que el error.

Si la respuesta es 3, agrega:

> Si necesitas encontrar un abogado titulado: contacta a la Dirección General de Profesiones (SEP) para verificar la cédula profesional de un abogado, o consulta la Barra Mexicana de Abogados o el colegio de abogados de tu entidad federativa — la mayoría ofrecen servicios de referencia como punto de partida más rápido. Muchos abogados ofrecen consultas iniciales gratuitas o de bajo costo. Para pequeñas empresas, las clínicas jurídicas universitarias pueden orientarte. Para personas físicas, las defensorías de oficio y organizaciones de asistencia jurídica cubren muchas áreas de práctica.

#### ¿Qué está conectado?

> Este plugin puede trabajar con: VDR (Intralinks, Datasite, Box), portal de consejo (Diligent, BoardEffect), almacenamiento de documentos y Slack. Déjame verificar qué conectores tienes configurados — las funciones que los necesiten funcionarán, y las funciones que no los tengan volverán a modo manual de forma elegante en lugar de fallar silenciosamente.

**Verifica qué está realmente conectado, no qué está configurado.** Un conector listado en `.mcp.json` está *disponible*. Un conector que realmente responde está *conectado*. Son cosas diferentes, y confundirlas destruye la confianza. Para cada conector que usa este plugin:

- Si puedes probar la conexión (llamar a una herramienta MCP simple como list o search), reporta ✓ solo con una respuesta exitosa.
- Si no puedes probar (sin forma de sondear desde aquí), reporta ⚪ "configurado pero no verificado — abre tu configuración MCP para confirmar" con una instrucción de una línea.
- Nunca reportes ✓ basándote solo en la configuración.

Para conectores que muestran como no conectados, dile al usuario cómo conectarlos. Los servidores MCP ya están preconfigurados a través del plugin `conectores-legal-mexico` (instalado automáticamente como dependencia) — el usuario no necesita agregar nada vía `/mcp`. Solo necesita autenticar:

- **LegalDataHunter (clave API):** "LegalDataHunter no está conectado. Ejecuta `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` e ingresa tu clave API cuando se solicite. La clave se guarda de forma segura en el llavero del sistema. Sin ella, las citas se marcarán como `[model knowledge — verify]`."
- **OAuth (Box, Slack, Google Drive, iManage):** "Box no está conectado. En Claude Cowork: Configuración → Conectores → Agregar → Box → iniciar sesión. En Claude Code: el servidor MCP ya está configurado — solo autoriza la conexión OAuth. Sin él, el usuario pega documentos en lugar de extraerlos — pero conectarlo hace la extracción automática."

Luego reporta los hallazgos en esta forma:

> - ✓ [Integración] — conectada (probada)
> - ⚪ [Integración] — configurada pero no verificada. Abre tu configuración MCP para confirmar.
> - ✗ [Integración] — no encontrada. [Función] volverá a [alternativa manual]. [Cómo conectar.] Si lo configuras después, vuelve a ejecutar `/corporativo-legal-mexico:cold-start-interview --check-integrations`.
>
> No necesitas todas. Las funciones principales funcionan solo con acceso a archivos.

#### Entorno de práctica

Pregunta una vez, temprano, para que la Parte 1 (perfil de empresa) y las preguntas de escalamiento de cada módulo se ramifiquen correctamente:

> ¿Entorno de práctica? (Esto alimenta el marco de escalamiento de cada habilidad — interno obtiene "escala al director jurídico," despacho solo/pequeño obtiene "consulta con abogado externo," clínica obtiene "remite al abogado supervisor.")
>
> - **Despacho solo / pequeño (sin jerarquía)** — Omitiré preguntas de cadena de aprobación y preguntaré cuándo consultarías a un colega o abogado externo.
> - **Despacho mediano / grande** — Preguntaré sobre tu cadena de aprobación, umbrales de facturación y quién autoriza por encima de ti.
> - **Jurídico interno** — Preguntaré sobre tu matriz de escalamiento, quién es el director jurídico / vicepresidente jurídico, y cuándo algo pasa al negocio.
> - **Gobierno / asistencia jurídica / clínica** — Preguntaré sobre la estructura de supervisión y cualquier restricción en tu práctica.
> - **Mi práctica no encaja en ninguna de estas** — dilo. Me adapto.

**Prácticas que no encajan en las categorías.** Si la práctica del usuario no coincide con las opciones anteriores (arbitraje internacional, derecho público internacional, amicus curiae, consultoría académica, panel pro bono, juzgados agrarios, justicia militar, derecho marítimo, o cualquier otra cosa que las categorías estándar asumen), ofrece: "Parece que tu práctica no encaja en mis categorías habituales. Cuéntame en tus propias palabras — qué haces, para quién, qué jurisdicciones y foros, cómo es el trabajo — y construiré tu perfil a partir de eso en lugar de forzarte en categorías que no aplican. Omitiré o adaptaré las preguntas que no correspondan." Luego construye el perfil a partir de la descripción libre, señalando qué campos de la plantilla se llenaron, adaptaron o dejaron vacíos porque no aplican. Un perfil construido a la fuerza es peor que un perfil escueto construido a partir de lo que realmente es cierto.

Notas de ramificación:

- **Despacho solo o pequeño sin jerarquía:** omite o reformula las preguntas de cadena de escalamiento interna. En lugar de "quién aprueba por encima de tu autoridad," pregunta "cuándo traes a un abogado externo para una segunda opinión." En el perfil de práctica, escribe la línea `**Escalamiento:**` en `## Perfil de empresa` alrededor de los disparadores de consulta (despacho de abogado externo, colega senior nombrado), no niveles de aprobación internos. En el módulo de F&A, la pregunta de "líder de operación" sigue aplicando.
- **Jurídico interno, despacho mediano o grande:** pregunta la cadena de escalamiento como está diseñada actualmente (Parte 1).
- **Asistencia jurídica / clínica:** dirige hacia un marco de modelo de supervisión — quién supervisa, cuándo un asunto sube al abogado supervisor.
- **Gobierno:** adapta — cadena de aprobación dentro de la dependencia/oficina.

Registra esto en una línea `**Entorno de práctica:**` en `## Perfil de empresa`.

#### Escribir en la configuración

Escribe las secciones `## Quién usa esto`, `## Integraciones disponibles` y `## Salidas` inmediatamente después de la primera sección de la configuración, conforme a la plantilla. Estas determinan la elección del encabezado de producto de trabajo y el comportamiento de respaldo de funciones en cada habilidad de este plugin.

---

### Parte 0.5: Selección de módulos (1–2 min)

Pregunta cuáles de los siguientes aplican. Más de uno es común. Los cuatro no es inusual para un director jurídico.

> ¿Cuáles de estos forman parte de tu trabajo regular? (Esto determina qué secciones se construyen en tu perfil de práctica y qué habilidades se activan — elegir solo F&A omite las entrevistas de consejo, sociedad bursátil y administración de entidades por completo.)
>
> 1. **Fusiones y Adquisiciones (F&A)** — operaciones: comprar, vender, invertir o desinvertir unidades de negocio
> 2. **Consejo de Administración y Secretaría Corporativa** — preparación de sesiones del consejo, actas, resoluciones, gestión de comités, convocatorias, protocolización
> 3. **Sociedad Bursátil (emisoras en BMV)** — reportes ante CNBV, comité de revelación, información privilegiada, reportes de tenencia accionaria
> 4. **Administración de Entidades** — administración de subsidiarias, representantes legales, libro de registro de acciones, obligaciones periódicas ante el Registro Público de Comercio, SAT e IMSS
>
> Dime los números que apliquen. Siempre puedes agregar un módulo después con `/corporativo-legal-mexico:cold-start-interview --module [nombre]`.

Registra los módulos activos. Procede a la sección de cada módulo activo solamente. Omite el resto por completo.

---

### Parte 1: Perfil de empresa (2 min, siempre)

Estas preguntas aplican sin importar qué módulos estén activos.

> Antes de hacer las preguntas estructuradas: ¿tienes una política de delegación de autoridad, una matriz de autorizaciones aprobada por el consejo, poderes notariales vigentes, o un memorándum previo de gobierno corporativo que pueda leer? Pega el contenido, comparte una ruta de archivo, o di 'no' y te haré las preguntas una por una. Si compartes uno, extraeré los niveles de aprobación y puntos de escalamiento en lugar de hacerte volver a escribirlos.

Si el usuario sube un archivo: léelo, extrae la identidad de la empresa, tamaño del equipo jurídico y estructura de escalamiento/autoridad, confirma lo que encontraste y omite las preguntas detalladas correspondientes.

Si no:

> **¿Qué hace [tu empresa]?** Este es el contexto más importante — el manual de una empresa de software (SaaS), el de una distribuidora industrial y el de una firma de servicios son completamente diferentes. No tienes que escribirlo: pega un enlace a tu sitio web, tu página "acerca de", tu artículo de Wikipedia, o tu último reporte anual, y extraeré lo que necesito. O dame la versión de una oración: qué venden, a quién, y cómo (ventas directas / canal / marketplace / suscripción).

- ¿Cuál es el nombre de la empresa (o el nombre que quieres usar en las salidas)?
- ¿En qué industria están?
- ¿Privada, emisora en BMV, o subsidiaria de una empresa pública?
- ¿En qué entidad federativa se protocolizó el acta constitutiva? (Nota: la LGSM es ley federal — la entidad determina el Registro Público de Comercio y el notario, pero la ley sustantiva es la misma en todo México.)
- ¿Qué tan grande es el equipo jurídico — solo tú, o un equipo?
- "Cuando una revisión encuentra algo que necesita que alguien más senior lo autorice — un tema nuevo en debida diligencia, una decisión de umbral de materialidad, un asunto de resoluciones con conflictos de interés de consejeros, un elemento de anexos que requiere juicio, o una decisión que está por encima de tu autoridad — ¿a quién va? Dame un nombre o un rol (el director jurídico, tu socio, el líder de operación), o di 'yo decido.' Así es como el plugin sabe cuándo decir 'tú puedes manejar esto' versus 'escala a [X].' (Esto alimenta a /diligence-issue-extraction, /material-contract-schedule, /written-consent y el enrutamiento de escalamiento de cada otra habilidad.)"

**Si el usuario no subió una delegación de autoridad:** al final de esta sección, ofrece: "¿Quieres que redacte tus líneas de escalamiento y autoridad como una nota independiente de delegación de autoridad / matriz de poderes que puedas compartir y mantener? El mismo contenido que acabo de capturar, en un formato que puedes circular."

Escribe en `## Perfil de empresa` en la configuración.

---

### Parte 2M: Módulo de F&A (4–6 min, si está activo)

#### 2M-a: Postura de operación

- ¿Lado comprador, lado vendedor, o ambos? Nota: la mayoría de las empresas han experimentado ambos con el tiempo, así que esto establece el predeterminado para la configuración general — la bandera por operación (`--new-deal`) captura el lado real para cualquier operación activa.
- ¿Adquirente serial con un manual estándar, o cada operación se diseña desde cero?
- ¿Quién lidera las operaciones de tu lado — desarrollo corporativo, jurídico, abogado externo como líder, o una combinación?
- ¿Qué autorizaciones regulatorias suelen aplicar a tus operaciones? (COFECE para concentraciones económicas, CNBV para el sector financiero, IFT para telecomunicaciones, CRE para energía, restricciones por Ley de Inversión Extranjera para participación de capital extranjero en sectores reservados o regulados — indica cuáles has manejado.)

#### 2M-b: Estructura de debida diligencia

> Antes de las preguntas: ¿tienes una lista estándar de solicitudes de debida diligencia o un memorándum de hallazgos previo que pueda leer? Pega el contenido, comparte una ruta de archivo, o di 'no' y te haré las preguntas una por una. Si los compartes, extraeré la estructura de categorías, umbrales de materialidad y formato interno y omitiré las preguntas correspondientes.

Si no:

- ¿Tienes una lista estándar de solicitudes de debida diligencia? ¿Cómo está organizada — por función (jurídico/finanzas/RH) o por tipo de documento?
- ¿Cuál es tu umbral de materialidad para revisión de contratos? (¿Todos los contratos? ¿Superiores a $X? ¿Los N principales por ingreso?) (Esto alimenta a /diligence-issue-extraction y /material-contract-schedule — el umbral decide qué contratos reciben revisión completa y cuáles se triangulan.)
- ¿Cuál es tu VDR habitual — Intralinks, Datasite, Box, SharePoint, otro?
- ¿Usas herramientas de revisión asistida por IA — Luminance, Kira, otra? ¿Para qué específicamente?

**Si el usuario no subió una lista de solicitudes o memorándum de hallazgos previo:** al final de este módulo, ofrece: "¿Quieres que redacte una lista inicial de solicitudes de debida diligencia y un esqueleto de memorándum de hallazgos en tu formato? Los basaré en lo que me dijiste sobre materialidad y estructura de categorías. Puedes editarlos y reutilizarlos en la próxima operación."

#### 2M-c: Formato del memorándum de hallazgos

> Dos cosas que necesito:
>
> 1. Tu lista estándar de solicitudes de debida diligencia — la que usas del lado comprador, o esperas ver del lado vendedor.
> 2. Un memorándum de hallazgos de una operación anterior — una operación cerrada, nada activo. Quiero ver cómo estructuras los hallazgos: cómo nombras las cosas, cómo categorizas los temas, qué esquema de severidad usas, a qué profundidad escribes.
>
> Estos dos documentos se convierten en la columna vertebral. Tus categorías, tu formato, tus estándares — no una plantilla genérica. (Estos alimentan a /diligence-issue-extraction — la habilidad reutiliza tu estructura de secciones, esquema de severidad y plantilla de hallazgos en cada operación futura.)

De la lista de solicitudes, extrae: estructura de categorías, umbrales de materialidad si están establecidos, exclusiones estándar.
Del memorándum de hallazgos, extrae: estructura de secciones, esquema de severidad, formato de hallazgo, profundidad, a quién va dirigido.

#### 2M-d: Específicos del lado vendedor (si el lado vendedor está activo)

Si el abogado trabaja del lado vendedor en algún momento, haz estas preguntas adicionales:

- Cuando preparas un data room, ¿quién decide qué se incluye?
- ¿Preparas un memorándum de revelación o bitácora de hallazgos anticipando lo que el comprador señalará?
- ¿Con quién te coordinas del lado del negocio para poblar el data room — desarrollo corporativo, director de finanzas, jefes funcionales?

El lado vendedor se trata de anticipar los hallazgos del comprador y gestionar el flujo de información hacia afuera, no de revisar documentos entrantes. Esto da forma a cómo se comporta la habilidad de extracción de hallazgos de debida diligencia cuando el contexto de lado vendedor está establecido.

#### 2M-e: Checklist de cierre e informes al equipo de operación

- ¿Dónde vive el checklist de cierre — Excel, Smartsheet, una herramienta de gestión de operaciones?
- ¿Quién es responsable de las actualizaciones?
- ¿Cómo informas al equipo de operación — diario, semanal, por hito? ¿Email, Slack, llamada?
- ¿Qué lee realmente el lado del negocio versus qué es para el expediente?

Escribe en `## F&A` en la configuración.

---

### Parte 2B: Módulo de Consejo de Administración y Secretaría Corporativa (3–4 min, si está activo)

- ¿Cuál es tu rol formal — secretario del consejo, secretario suplente, o actúas en capacidad asesora sin el título formal?
- ¿De cuántos miembros es el consejo, y cuál es la composición — mayormente consejeros independientes, con peso de consejeros patrimoniales, consejo escalonado?
- ¿Qué comités existen? (Auditoría y Prácticas Societarias, Compensaciones, Nominaciones, Estrategia, ¿algún otro?)
- ¿Qué herramienta usas para los materiales del consejo — Boardvantage, Diligent, BoardEffect, solo correo electrónico, nada formal?
- ¿Cuántas sesiones ordinarias del consejo al año, y aproximadamente en qué meses?
- ¿Cuentan con Comisario designado? (Obligatorio para S.A. conforme a los Arts. 164-171 LGSM.) ¿Es el mismo despacho que el auditor externo, o es diferente?

**Asambleas de accionistas:**
- ¿Con qué frecuencia celebran asambleas ordinarias y extraordinarias?
- ¿Cómo emiten las convocatorias — publicación en DOF o periódico de mayor circulación, o segundo llamado sin quórum especial? ¿Cumplen los plazos de 15 días previos?
- ¿Qué tipos de acuerdos requieren asamblea extraordinaria? (Modificación de estatutos, aumento/reducción de capital, fusión, escisión, disolución, transformación.)

**Actas:**
- ¿Actas narrativas extensas, actas de acuerdos (solo resoluciones), o algo intermedio?
- ¿Qué tan rápido formalizan las actas después de una sesión?
- ¿Cómo se aprueban — se circulan para comentarios escritos, o se ratifican en la siguiente sesión?
- ¿Qué actas requieren protocolización ante notario público? (Típicamente: actas de asamblea extraordinaria que reforman estatutos, actos de fusión/escisión, aumento/reducción de capital.)

**Resoluciones unánimes fuera de asamblea:**
- ¿Utilizan habitualmente resoluciones unánimes fuera de asamblea en lugar de sesiones? ¿Para qué tipos de actos — nombramientos de funcionarios, otorgamiento de poderes, acciones anuales, o más ampliamente?
- Recuerda: conforme al Art. 178 de la LGSM, las resoluciones tomadas fuera de asamblea requieren el consentimiento UNÁNIME de TODOS los accionistas (o socios). ¿Es esto viable en tu estructura accionaria?
- ¿Alguna limitación sobre qué puede aprobarse por resolución fuera de asamblea versus requerir sesión formal (restricciones estatutarias, o simplemente práctica)?

**Actas semilla (requeridas para la habilidad de actas del consejo):**

> Sube 5–6 actas previas de consejo o comité. Solo de sesiones cerradas, nada actualmente en curso. Estas le enseñan a la habilidad tu formato interno — cómo se estructuran las actas, qué nivel de detalle de discusión capturas, cómo se redactan las resoluciones, cómo se registra la asistencia. Un juego completo de consejo y uno de comité si tienes ambos formatos. (Esto alimenta la habilidad de actas del consejo — cada borrador futuro de actas se construye a partir de tu estructura, profundidad de discusión y lenguaje de resoluciones extraídos.)
>
> Si no tienes actas compartibles ahora, puedes agregarlas después con `/corporativo-legal-mexico:cold-start-interview --module board`. La habilidad de actas del consejo te las pedirá si faltan.

De las actas semilla, extrae:
- Estructura general y orden de secciones
- Formato de encabezado (nombre de la sociedad, tipo de sesión, fecha, lugar)
- Formato de registro de asistencia (consejeros presentes/ausentes, directivos, invitados)
- Profundidad de discusión — narrativa extensa, actas de acuerdos, o híbrido
- Lenguaje de resoluciones (redacción exacta: "SE RESUELVE" / "SE ACUERDA" / "POR LO ANTERIOR, SE RESUELVE" / otro)
- Convención de referencia a exhibidos
- Formato de bloque de firmas
- Cualquier recital estándar o texto fijo que aparezca en cada juego
- Indicación de protocolización si aplica

Escribe el formato extraído como un bloque `**Plantilla de actas:**` en `## Consejo de Administración y Secretaría Corporativa` en la configuración.

**Repositorio de resoluciones (requerido para la habilidad de resoluciones):**

> ¿Tienes una carpeta o repositorio donde se almacenen las resoluciones unánimes fuera de asamblea ejecutadas? (Esto alimenta a /written-consent — la habilidad busca en el repositorio la resolución previa más cercana y la usa como punto de partida sustantivo, no solo por formato sino por el lenguaje específico de resolución ya aprobado para ese tipo de acto.)
>
> Si tienes uno: dime dónde está (ruta de carpeta, Google Drive, SharePoint, Box). La habilidad lo buscará en tiempo de ejecución.
>
> Si no tienes un repositorio centralizado: sube 3–5 resoluciones previas ahora para aprendizaje de formato. La habilidad seguirá funcionando — solo no tendrá capacidad de búsqueda de precedentes hasta que se configure un repositorio.

Del repositorio o resoluciones semilla, extrae:
- Lenguaje de resolución interno (redacción exacta: "SE RESUELVE" / "SE ACUERDA" / "POR LO ANTERIOR, SE RESUELVE" / otro)
- Estructura de recitales (CONSIDERANDO / POR LO QUE — profundidad y estilo)
- Lenguaje de autorización (delegación a funcionarios y otorgamiento de poderes al final)
- Lenguaje de firma electrónica y contrapartes (si está presente)
- Formato de bloque de firmas

Escribe en `## Consejo de Administración y Secretaría Corporativa` → `**Repositorio de resoluciones:**` y `**Formato de resoluciones:**` en la configuración.

**Ciclo anual de gobierno corporativo:**
- ¿Qué temas anuales manejas? (Elección de consejeros, ratificación del auditor externo, designación del Comisario, aprobación del informe del Comisario, aprobaciones de planes de acciones, asamblea ordinaria anual, informe anual del consejo, reporte de la política de información privilegiada si es emisora — lo que aplique a tu caso.)

Escribe en `## Consejo de Administración y Secretaría Corporativa` en la configuración.

---

### Parte 2P: Módulo de Sociedad Bursátil (3–4 min, si está activo)

- ¿En qué segmento de la BMV cotizan — mercado local, mercado global (SIC), o están listados en otra bolsa?
- ¿Cuándo cierra tu ejercicio fiscal?
- ¿Cuál es la clasificación de tu emisora? (En México no aplica el sistema de filers de la SEC. Indica si son emisora con valores inscritos en el RNV, si emiten deuda, capital, o ambos, y si participan en algún índice como el IPC.)

**Comité de auditoría y prácticas societarias:**
- ¿Tienen un comité de auditoría y prácticas societarias formalmente constituido conforme a la LMV? ¿Quiénes lo integran — consejeros independientes, director de finanzas, relación con inversionistas, jurídico, otros?
- ¿Con qué frecuencia sesiona — trimestralmente previo a la publicación de resultados, o según sea necesario?

**Reportes de tenencia accionaria:**
- ¿Quién da seguimiento a los cambios en tenencia accionaria de consejeros y funcionarios relevantes — tú, abogado externo, relación con inversionistas, o una combinación?
- ¿Cuál es tu objetivo interno para presentar los avisos de cambio de tenencia ante la CNBV y BMV? (El plazo regulatorio es típicamente al cierre del día hábil siguiente.)
- ¿Tu política de información privilegiada requiere autorización previa para operaciones con valores de la emisora? ¿Quién autoriza?

**Política de información privilegiada:**
- ¿Cuándo están abiertos los periodos de operación con valores en relación con la publicación de resultados?
- ¿Quién está cubierto por los requisitos de autorización previa — todos los funcionarios y consejeros, o una lista más amplia que incluya personas con acceso a información privilegiada?
- ¿Cuál es el proceso para una excepción al periodo de veda si alguna vez se necesita?

**Publicación de resultados:**
- ¿Cuál es el rol del área jurídica en la preparación de la publicación de resultados — revisión del comunicado, preparación de preguntas y respuestas, algo más, o sin participación directa?
- ¿Con cuánta anticipación a la publicación participas típicamente?

Escribe en `## Sociedad Bursátil` en la configuración.

---

### Parte 2E: Módulo de Administración de Entidades (2–3 min, si está activo)

> Si tienes un organigrama corporativo o lista de entidades — aunque sea uno aproximado, aunque sea una hoja de cálculo — súbelo ahora. Lo leeré y extraeré la estructura de entidades, jurisdicciones, porcentajes de participación y tipos de entidad. Eso es más rápido y preciso que responder estas preguntas de memoria. (Esto alimenta a /entity-compliance — la habilidad inicializa el calendario de cumplimiento a partir de esta lista y muestra las fechas límite de obligaciones ante el Registro Público de Comercio, SAT e IMSS.)
>
> Si no tienes uno a la mano, responde las preguntas a continuación y construiré una tabla inicial de entidades a partir de tus respuestas.

**Del organigrama o lista de entidades subidos, extrae:**
- Nombres y tipos de entidad (SA de CV, S de RL de CV, SAS, SA, SC, sucursal, etc.)
- Entidad federativa de constitución para cada una
- Cadena de propiedad y porcentajes de participación
- Cualquier entidad señalada como inactiva o en proceso de liquidación

**Si no hay carga de archivo, pregunta:**

- ¿Cuántas entidades legales activas estás administrando, aproximadamente?
- ¿Cuáles son las jurisdicciones clave — todo en la misma entidad federativa, o con presencia significativa en múltiples estados o en el extranjero?
- ¿Quién es tu notario público de cabecera para protocolización de actos corporativos? ¿Usas el mismo para todas las entidades, o varía? ¿Cuentas con corredor público para algún tipo de acto?
- ¿Usas un sistema de administración de entidades — Athena, Blueprint — o trabajas con hojas de cálculo?
- ¿Cuál es la situación de tu libro de registro de acciones — Carta, Shareworks, manual, o no aplica si son subsidiarias al 100% sin capital externo?
- ¿Quién se encarga del trabajo rutinario de cumplimiento — avisos al Registro Público de Comercio, declaraciones ante el SAT, obligaciones ante IMSS e INFONAVIT? ¿Jurídico, operaciones jurídicas, o lo maneja un despacho externo?
- ¿Tus subsidiarias tienen su propia cadencia de gobierno corporativo (asambleas, sesiones de consejo), o son efectivamente sociedades tenedoras inactivas?
- ¿Tienen convenios intercompañía vigentes — contratos de prestación de servicios, licencias de PI, préstamos intercompañía?

Escribe en `## Administración de Entidades` en la configuración.

---

### Después de escribir

**Muestra lo que este plugin puede hacer.** Antes de cerrar, ofrece:

> **¿Quieres ver en qué puedo ayudarte?**

Si dice que sí, muestra esta lista personalizada (no una plantilla genérica — estos son las cosas concretas que este plugin hace mejor):

> **Esto es en lo que soy bueno en práctica corporativa y de F&A:**
>
> - **Extraer hallazgos de debida diligencia del VDR** — p. ej., "Apunta a una carpeta del VDR y obtén hallazgos categorizados según tus umbrales de materialidad internos." Prueba: `/corporativo-legal-mexico:diligence-issue-extraction`
> - **Construir el anexo de contratos relevantes** — p. ej., "A partir de los hallazgos de debida diligencia, construye el anexo de revelaciones en el formato del contrato de compraventa de acciones." Prueba: `/corporativo-legal-mexico:material-contract-schedule`
> - **Redactar una resolución unánime fuera de asamblea del consejo o comité** — p. ej., "Búsqueda de precedentes en tu repositorio de resoluciones, luego redactada en formato interno." Prueba: `/corporativo-legal-mexico:written-consent`
> - **Rastreador de cumplimiento de entidades** — p. ej., "Mira qué obligaciones vencen en los próximos 30 / 60 / 90 días entre tus subsidiarias." Prueba: `/corporativo-legal-mexico:entity-compliance`
> - **Estado del checklist de cierre** — p. ej., "Qué falta para cerrar — condiciones suspensivas, documentos, autorizaciones, inscripciones — con ruta crítica." Prueba: `/corporativo-legal-mexico:closing-checklist`
> - **Integración post-cierre** — p. ej., "Plan de trabajo por fases, seguimiento de consentimientos, cesión de contratos a escala para una operación recién cerrada." Prueba: `/corporativo-legal-mexico:integration-management`
>
> **Mi sugerencia para tu primera vez:** Si tienes una operación activa, ejecuta `/corporativo-legal-mexico:closing-checklist` — muestra inmediatamente dónde encaja el plugin en tu flujo de trabajo. O dime qué tienes en tu escritorio y yo elijo.

Esto resuelve el problema de arranque en frío (el supervisor no sabe qué hacer primero) y el problema de propuesta de valor (no saben qué puede hacer el plugin) en una sola oferta. Haz la lista específica. Omite este paso si el supervisor ya nombró una primera tarea concreta durante la entrevista.


**Indicación de conector de investigación.** Antes de mostrar los módulos activos, di:

> "Antes de tu primera extracción de debida diligencia o resolución: conecta una herramienta de investigación. Sin ella, marcaré cada cita como no verificada — con ella, las verifico contra una base de datos actualizada. En Cowork: Configuración → Conectores. En Claude Code: autoriza cuando una habilidad te lo solicite."

Luego muestra los módulos activos y las secciones pobladas:

> Esto es lo que capturé: [lista de módulos activos]. El Perfil de Práctica está escrito. Algunas cosas por revisar:
> - [Señala respuestas escuetas o ambiguas que valga la pena revisar]
> - [Si F&A está activo y no se proporcionaron documentos semilla: "Envíame tu lista de solicitudes y un memorándum de hallazgos previo cuando los tengas — actualizaré las secciones de estructura de debida diligencia y formato de memorándum."]
> - [Si F&A está activo: "Cuando llegue una operación, ejecuta `/corporativo-legal-mexico:cold-start-interview --new-deal` para configurar contexto específico de la operación sobre tu enfoque general. Habilidades de F&A disponibles ahora: extracción de debida diligencia, resúmenes para el equipo de operación, anexo de contratos relevantes, checklist de cierre e integración post-cierre."]
> - [Si Consejo de Administración está activo: "Habilidades de Consejo disponibles ahora: `/corporativo-legal-mexico:written-consent` para resoluciones unánimes fuera de asamblea, y la habilidad de actas del consejo para redactar actas en tu formato interno."]
> - [Si Administración de Entidades está activo: "Habilidad de Entidades disponible ahora: `/corporativo-legal-mexico:entity-compliance` inicializa un rastreador de cumplimiento a partir de tu lista de entidades y muestra qué vence."]
> - [Si Sociedad Bursátil está activo: "Las habilidades de Sociedad Bursátil se publicarán en una versión futura — la sección del perfil de práctica está lista para poblarse cuando se lancen."]

Cierra con una nota sobre la posibilidad de cambios:

> "Tu perfil de práctica está en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` — es un archivo de texto plano que puedes leer y editar directamente. Cualquier cosa que hayas respondido se puede cambiar:
>
> - Edita el archivo directamente para un cambio rápido (un nuevo umbral, una jurisdicción agregada, un comité renombrado)
> - Ejecuta `/corporativo-legal-mexico:cold-start-interview --redo` para una entrevista completa
> - Ejecuta `/corporativo-legal-mexico:cold-start-interview --module [m&a | board | public | entities]` para agregar o actualizar un módulo
> - Ejecuta `/corporativo-legal-mexico:cold-start-interview --check-integrations` para verificar qué está conectado
>
> Las secciones que más se ajustan después de la primera configuración son los umbrales de materialidad de F&A, el formato de anexos de revelaciones / plantilla de memorándum de hallazgos, y la cadencia del rastreador de entidades."

## Tu perfil de práctica aprende

Después de escribir el perfil de práctica, cierra con esta nota:

> **Tu perfil de práctica aprende.** Mejora conforme usas los plugins:
>
> - Cuando la salida de una habilidad se sienta incorrecta, generalmente es una posición que ajustar. La salida te dirá cuál.
> - Siempre puedes decir "actualiza mi manual para preferir X" o "cambia mi umbral de escalamiento a Y" y la habilidad relevante escribirá el cambio.
> - Ejecuta `/corporativo-legal-mexico:cold-start-interview --redo <seccion>` para re-entrevistar una parte, o edita el archivo de configuración directamente.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú mismo.

---

## Configuración por operación (`--new-deal`, solo módulo de F&A)

Cuando inicia una operación activa, ejecuta una entrevista más ligera enfocada solo en el contexto específico de la operación. El enfoque general permanece de la configuración del plugin.

Pregunta:
- Nombre clave de la operación
- Lado para esta operación (comprador o vendedor — puede diferir del predeterminado general)
- Nombre del objetivo o del adquirente
- Ubicación del VDR (ruta de carpeta o URL)
- Nombre del líder de operación
- Fecha de firma y fecha de cierre (si se conocen)
- Cualquier diferencia de umbral específica de la operación (una operación de $50M puede revisar contratos más pequeños que una de $1,000M)
- Despacho de abogados externos y contacto principal para esta operación

Escribe en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[nombre-clave]/deal-context.md`. Las habilidades leen tanto la configuración del plugin (general) como `deal-context.md` (esta operación), con deal-context.md prevaleciendo en conflictos.

---

## Verificación de calidad del Perfil de Práctica

Antes de terminar, vuelve a leer lo que se escribió. Señala:
- Cualquier sección que todavía muestre un placeholder porque la respuesta se omitió o fue vaga — vuelve a preguntar
- Cualquier módulo activo donde no se proporcionó documento semilla — señálalo y pide al usuario que proporcione uno cuando esté disponible
- La línea `*Módulos activos:*` al inicio de la configuración del plugin — actualízala para listar exactamente qué módulos están encendidos

---

## Modos de fallo

- **No asumas que todos los módulos están activos.** Pregunta primero, entrevista solo para lo que es relevante. Un abogado que solo hace operaciones no necesita configuración de gobierno corporativo de sociedad bursátil.
- **No predetermines lado comprador.** El perfil de práctica captura la tendencia general; la bandera por operación maneja el lado real. Escribe el perfil de práctica general de forma agnóstica al lado; la postura se establece por operación en `--new-deal`.
- **No escribas placeholders genéricos.** Si la respuesta fue vaga ("umbrales de materialidad estándar"), pregunta qué significa eso en números. El perfil de práctica solo es útil si los umbrales son umbrales reales.
- **La postura de lado vendedor no es el lado comprador al revés.** Del lado vendedor anticipas los hallazgos del comprador y gestionas el flujo de información hacia afuera, no revisas documentos entrantes. Señala esta distinción si el lado vendedor está activo.
- **No solicites documentos semilla para módulos inactivos.** Solo pide la lista de solicitudes y el memorándum de hallazgos si F&A está activo. Un abogado que solo lleva consejo no necesita proporcionar documentos de debida diligencia.
