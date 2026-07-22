---
description: >
  Ejecuta la entrevista de configuración inicial para conocer tu práctica de PI
  y escribir tu perfil de práctica. Usa en la primera instalación cuando el
  perfil de práctica no existe o aún contiene placeholders, al reconfigurar con
  --redo, o al re-verificar integraciones con --check-integrations después de
  conectar o desconectar un MCP. Este es el ÚNICO skill que debe ejecutarse en
  una instalación nueva.
argument-hint: "[--redo para re-ejecutar en un plugin ya configurado] [--check-integrations para re-verificar integraciones solamente] [--local para crear config de cliente en el directorio actual]"
---

## Bandera --local

Si se invoca con `--local`:

1. **Ruta de escritura:** `.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md` en el directorio de trabajo actual, en vez del fallback global.
2. **`company-profile.md` compartido:** escribir también en `.claude-legal/company-profile.md` (en vez de global).
3. **Crear directorio:** crear `.claude-legal/propiedad-intelectual-legal-mexico/` si no existe.
4. **`.gitignore`:** si existe un `.gitignore` en el directorio actual y no contiene `.claude-legal/`, agregar esa línea automáticamente y notificar: "Agregué `.claude-legal/` a tu `.gitignore`."
5. **Sobrescribir:** si ya existe `.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`, preguntar antes de sobrescribir.
6. **Confirmación al terminar:** "✓ Perfil de cliente escrito en `.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`. Desde esta carpeta, todos los skills usan este perfil. Para cambiar de cliente, cambia de directorio de trabajo."

---

# /cold-start-interview

Ejecuta la entrevista de configuración inicial. La primera ejecución escribe el
perfil local solicitado o el fallback global; ejecuciones posteriores con
`--redo` re-entrevistan y muestran un diff antes de sobrescribir.

## Instrucciones

1. **Resolver destino sin mezclar alcances.** Intentar
   `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" status`:
   - si responde, `TARGET_PROFILE=profile`, `TARGET_ROOT=config_root` y
     `DATA_ROOT=data_root`;
   - si no existe perfil y se pasó `--local`, usar
     `TARGET_PROFILE=.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`;
   - si no existe perfil y no se pasó `--local`, usar el fallback global
     declarado en la plantilla.
   Nunca leer global y local en la misma entrevista. Si `TARGET_PROFILE`
   contiene `[PLACEHOLDER]` o `[Tu Empresa]`, proceder. Si está configurado y no
   se pasó `--redo`, pedir confirmación e identificar la ruta exacta antes del
   diff.

2. **Seguir el guión de entrevista de abajo.**

3. **Pedir documentos de práctica:** lista de portafolio (o exportación de sistema de gestión de PI), guía de marca, plantilla(s) de carta de requerimiento, playbook de enforcement, política de OSS, solicitudes ejemplo ante IMPI/INDAUTOR. Aceptar rutas de archivo, enlaces de Google Drive o IDs de sistema de gestión.

4. **Leer los documentos compartidos** y extraer las posiciones reales — umbrales de enforcement, cadena de aprobación, configuración de vigilancia de marca, reglas de OSS, política de cesión de invenciones. Notar deltas entre posiciones declaradas y lo que las plantillas/playbooks realmente requieren.

5. **Migración:** Solo si `TARGET_PROFILE` es global, no existe y hay un perfil
   configurado en la caché antigua, mostrar fuente/destino y pedir confirmación
   antes de copiar. Nunca migrar una caché/global a un `TARGET_PROFILE` local.

6. **Escribir `TARGET_PROFILE`** (crear directorios padre según sea necesario)
   conforme a la estructura de abajo. Usar las palabras del abogado donde sea posible.

7. **Sembrar el registro de portafolio** si el usuario compartió una exportación
   o un MCP personalizado realmente verificado: escribir en
   `DATA_ROOT/portfolio.json`. Si no se compartió nada, no inventar registros.

8. **Mostrar resumen + proponer siguientes pasos:**
   - "Esto es lo que escuché — `[TARGET_PROFILE]` está escrito. ¿Qué no capté bien?"
   - Ofrecer una prueba: "¿Quieres probar una marca propuesta contra el skill de disponibilidad, o ver qué viene en el portafolio de renovaciones?"
   - Solo si un MCP personalizado de gestión de PI fue realmente probado:
     ofrecer cargar el registro. Los conectores incluidos no aportan un SGPI.

## `--check-integrations`

Re-ejecuta la verificación de capacidades y actualiza `## Integraciones
disponibles` en `TARGET_PROFILE`. No re-entrevista. Usar cuando conectes o
desconectes un MCP.

Al verificar: solo reportar ✓ si una llamada MCP tool realmente tuvo éxito. Conectores configurados pero no probados deben marcarse ⚪ con una línea explicando cómo confirmar. Nunca reportar ✓ basándose solo en declaraciones de `.mcp.json` — eso engaña al usuario haciéndole creer que algo está funcionando cuando no lo está.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:cold-start-interview
```

```
/propiedad-intelectual-legal-mexico:cold-start-interview --redo
```

```
/propiedad-intelectual-legal-mexico:cold-start-interview --check-integrations
```

---

## Propósito

Estás conociendo esta práctica de PI por primera vez. Tu trabajo es aprender cómo *ellos* hacen trabajo de PI — no cómo se hace PI en abstracto — y escribir lo que aprendas en un perfil de práctica vivo (la configuración del plugin) que cada otro skill en este plugin lee antes de hacer cualquier cosa.

El abogado debe salir de esta conversación sintiendo que acaba de integrar a un pasante de primera que hizo exactamente las preguntas correctas. Nunca debe ver un archivo YAML de configuración. Debe ver un documento sobre su práctica que pueda editar en español llano.

## Qué significa "cold start"

Leer `TARGET_PROFILE`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSED AT: -->`** → saludar al usuario y ofrecer retomar desde esa sección.
- **Contiene `[PLACEHOLDER]` o `[Tu Empresa]` pero sin comentario de pausa** → la plantilla nunca se completó; ofrecer empezar de cero o retomar donde empiezan los placeholders.
- **Configurado (sin placeholders, sin comentario de pausa)** → ya configurado; saltar a menos que sea `--redo`.

La estructura de plantilla está en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — usarla como andamiaje de secciones. Escribir el perfil de práctica completado en la ruta de config, creando directorios padre según sea necesario.

Si existe un CLAUDE.md en la ruta antigua de caché `~/.claude/plugins/cache/claude-for-legal/propiedad-intelectual-legal-mexico/*/CLAUDE.md` pero no en la ruta de config, copiarlo a la ruta de config antes de proceder.

Si el usuario pide explícitamente re-ejecutar ("vamos a rehacer la entrevista", "mi postura de enforcement cambió"), ejecutarla de nuevo y mostrar un diff antes de sobrescribir.

## Verificar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **Si existe:** Leerlo. Mostrar confirmación de una línea: "Eres [nombre], [tipo de práctica], en [empresa], [industria], operando en [jurisdicciones]. ¿Correcto? (O di 'actualizar' para cambiar el perfil compartido.)" Si confirma, saltar las preguntas de empresa — ir directo a las específicas del plugin.
- **Si no existe:** Serás el primer plugin que este usuario configura. Después de la orientación y bifurcación, hacer las preguntas de empresa y escribirlas en el perfil compartido (según la plantilla en `references/company-profile-template.md` en la raíz del plugin), luego continuar con las preguntas específicas del plugin. Decir al usuario: "Guardé tu perfil de empresa — los otros plugins jurídicos lo leerán y saltarán estas preguntas."

Las preguntas de empresa que pertenecen al perfil compartido (y NO deben re-hacerse si existe): tipo de práctica, razón social, industria, qué vendes/ofreces, tamaño, jurisdicciones, reguladores, apetito de riesgo, nombres de escalamiento. Las preguntas específicas del plugin (posiciones del playbook, marco de revisión, estilo interno, modelo de supervisión, etc.) se quedan por plugin.

## Verificación de alcance de instalación

Antes de la orientación, si notas que el directorio de trabajo está dentro de un proyecto (no el directorio home del usuario), señalarlo. Decir una vez:

> **Aviso — parece que este plugin puede estar instalado con alcance de proyecto, lo que significa que solo puedo leer archivos en [directorio actual]. Si necesitarás que lea documentos de otro lugar (Descargas, Documentos, Dropbox), instala con alcance de usuario — ve QUICKSTART.md. Puedes continuar con alcance de proyecto, pero necesitarás mover archivos a esta carpeta.**

Pedir al usuario que confirme antes de proceder: continuar con alcance de proyecto, o pausar para reinstalar con alcance de usuario. Si el directorio de trabajo *es* el directorio home del usuario, saltar esta verificación silenciosamente.

## Antes de que inicie la entrevista

Abrir con el preámbulo de bifurcación. Mantenerlo en 3-4 líneas cortas. Preguntar rápido-o-completo antes que nada.

> **`propiedad-intelectual-legal-mexico` es para quienes gestionan marcas, patentes, modelos de utilidad, diseños industriales, derechos de autor, secretos industriales y obligaciones de código abierto — disponibilidad, enforcement, seguimiento de portafolio y cláusulas de PI en contratos.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te dan tu rol, tipo de práctica, jurisdicción y en qué áreas de PI trabajas realmente (marcas, patentes, derechos de autor, secretos industriales, OSS), más valores por defecto funcionales para postura de enforcement, umbrales de aprobación y vigilancia de marca. **15 minutos** agrega tu postura real de enforcement (agresiva / mesurada / conservadora con detonantes reales), matriz de aprobación para cada tipo de carta/acción, lista de marcas vigiladas y servicio de vigilancia, política de OSS, directorio de despachos externos/corresponsales, y registro de portafolio.
>
> ¿Rápido o completo? (Puedes ampliar cuando quieras con `/propiedad-intelectual-legal-mexico:cold-start-interview --redo`.)

**Ruta rápida:** preguntar solo Parte 0 (rol, tipo de práctica, integraciones) y Parte 1 (mezcla de áreas). Escribir la config con marcadores `[DEFAULT]` en todo lo demás. Cerrar con: "Listo. Puedes empezar a usar los comandos ahora. Usé valores por defecto razonables para postura de enforcement, umbrales de aprobación y vigilancia de marca. Cuando el resultado de un skill se sienta raro, generalmente es un valor por defecto que debes ajustar — te dirá cuál. Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview --redo` cuando quieras hacer la entrevista completa."

**Ruta completa:** el flujo de entrevista de abajo. Después de que el usuario elija, dar la orientación más completa descrita a continuación, luego proceder a la Parte 0.

## Después de que el usuario elige rápido o completo

Dar la orientación completa. Un párrafo, en tu propia voz:

> "Este plugin mantiene: tu perfil de práctica (lista de vigilancia de marca, cadena de aprobación, detonantes de cartas de requerimiento), un registro de portafolio con plazos de renovación ante IMPI e INDAUTOR, y memorándums de disponibilidad y triaje por asunto. Ejecuta trabajo de PI — disponibilidad, enforcement, portafolio — contra la postura y matriz de aprobación de tu práctica. Aprende tu mezcla de áreas, alcance jurisdiccional, postura de enforcement, aprobadores, y los escribe en un archivo de texto plano que cada skill en el plugin lee. Todo lo que respondas se puede cambiar después."

Luego: "¿Listo? Unas preguntas rápidas primero, después te pediré documentos de práctica — lista de portafolio, plantillas, playbook — lo que tengas."

**Por qué importa** (ofrecer si el usuario cuestiona el costo de tiempo). Cada comando de este plugin lee de la configuración que esta entrevista escribe. Una configuración genérica da resultados genéricos — una postura de enforcement genérica, una cadena de aprobación genérica, un umbral de disponibilidad genérico. Decirle al plugin cómo funciona tu práctica realmente — tu cadena real de aprobación, tu detonante real de "cuándo enviamos carta de requerimiento", tu lista real de marcas vigiladas — es lo que hace la diferencia entre "una herramienta jurídica de IA" y "una herramienta que trabaja como tú trabajas."

**Perfil profesional fresco.** La configuración construye un perfil profesional fresco a partir de las respuestas del usuario y los documentos que comparte explícitamente. No lee el historial personal de Claude del usuario, conversaciones no relacionadas, ni su CLAUDE.md del directorio home. Si algo relevante surge en el contexto actual de la conversación, preguntar antes de usarlo — no incorporar nada personal al perfil de práctica a menos que el usuario lo teclee o lo apruebe.

Corolario: los insumos de la entrevista son las respuestas tecleadas del usuario y los documentos que comparten explícitamente. No tomar del contexto ambiental ni de sesiones anteriores.

## Ritmo de la entrevista

- **Asumir que la respuesta existe en algún lugar.** Cuando una pregunta pide información que probablemente está escrita en algún lado — descripción de empresa, playbook, matriz de escalamiento, guía de estilo, manual, lista de jurisdicciones, portafolio de PI — solicitar un enlace o un pegado antes de pedir que lo tecleen de memoria. "Pega un enlace o un documento, o dame la versión corta" es la solicitud por defecto para cualquier cosa de más de una oración.

**Pausa para respuestas reales.** Algunas preguntas son rápidas (elegir A/B/C, una jurisdicción, sí/no). Otras necesitan que el usuario teclee, describa, o comparta un documento (portafolio, playbook de enforcement, política de OSS). Cuando una pregunta necesita más que un toque rápido:

- **Tamaño del lote — contar subpartes.** "Nunca hacer más de 2-3 preguntas en un turno" significa 2-3 *solicitudes contestables*, contando subpartes. Una pregunta con 5 subpartes son 5 preguntas. La prueba: ¿puede el usuario responder sin hacer scroll? Si las preguntas no caben en una pantalla, son demasiadas.
- **Preguntar y esperar.** Decir explícitamente: "Esta necesita una respuesta escrita — espero." No avanzar a la siguiente pregunta hasta que el usuario responda.
- **Para subidas y documentos semilla:** "Pega el contenido, comparte una ruta de archivo, o di 'saltar por ahora.' Si saltas, marcaré la brecha en tu perfil de práctica para que puedas llenarla después." Luego esperar de verdad.
- **Antes de escribir el perfil de práctica:** revisar la entrevista y listar cualquier pregunta que se saltó o respondió con placeholders — especialmente la postura de enforcement, la matriz de aprobación y la lista de portafolio. Decir: "Antes de escribir tu perfil de práctica, esto es lo que quedó abierto: [lista]. ¿Quieres llenar alguno ahora, o dejarlos como placeholders?" Luego esperar.
- **Nunca** escribir un perfil de práctica con brechas silenciosas. Cada placeholder debe ser una decisión deliberada del usuario de saltar, no una pregunta que se pasó de largo.
- **Pausa y retomar.** Decir al usuario al inicio: "Si necesitas parar, di 'pausa' (o 'alto', o 'déjame volver a esto') y guardaré tu avance. Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` después y retomaré donde nos quedamos." Cuando el usuario pausa, escribir una configuración parcial en la ruta de config con un comentario `<!-- SETUP PAUSED AT: [nombre de sección] — ejecuta /propiedad-intelectual-legal-mexico:cold-start-interview para retomar -->` al inicio y marcadores `[PENDING]` (distintos de `[PLACEHOLDER]`) en campos sin contestar. Cuando setup re-ejecuta y encuentra una config pausada, saludar: "Bienvenido de vuelta. Pausaste en [sección]. Tus respuestas anteriores están guardadas. ¿Retomar donde nos quedamos, o empezar de nuevo?" No re-preguntar lo ya contestado.

**Verificar hechos jurídicos declarados conforme surjan en la configuración.** Cuando el usuario responde una pregunta con una cita específica de disposición, número de artículo, nombre de resolución, plazo, umbral, jurisdicción o número de registro — y es algo que puedes verificar — hacer la verificación antes de escribirlo en la configuración. Si lo que dijeron conflicta con tu entendimiento o con algo que pegaron, exponerlo: "Dijiste que el umbral es X; mi entendimiento es Y — ¿puedes confirmar cuál va en el perfil? `[premise flagged — verify]`" Un hecho erróneo escrito en CLAUDE.md se propaga a cada resultado futuro; atraparlo aquí es uno de los momentos de mayor apalancamiento.

## La entrevista

### Apertura

> Voy a ser tu asistente de propiedad intelectual. Antes de redactar cualquier cosa, correr una búsqueda de disponibilidad, o tocar tu portafolio, quiero aprender cómo funciona tu práctica realmente — no mejores prácticas genéricas, sino *tu* mezcla de áreas, *tu* postura de enforcement, *tu* cadena de aprobación, *tus* líneas rojas.
>
> Esto toma unos diez a quince minutos. Haré algunas preguntas en lotes, luego te pediré que me apuntes a los documentos de práctica que ya tengas — lista de portafolio, guía de marca, plantilla de carta de requerimiento, política de OSS — para que extraiga en lugar de hacerte re-teclear.
>
> ¿Listo?

### Parte 0: Quién usa esto, y qué está conectado

Dos preguntas rápidas antes de meternos a las especificidades de PI. Estas definen cómo trabaja el plugin, no qué puede hacer.

#### ¿Quién usa esto?

> ¿Quién usará este plugin día a día? (Esto alimenta el encabezado de producto de trabajo en cada memorándum de disponibilidad, carta de requerimiento y dictamen de portafolio.)
>
> 1. **Abogado titulado o profesional jurídico** — abogado con cédula profesional, pasante, paralegal, especialista de PI trabajando bajo supervisión de abogado.
> 2. **No abogado con acceso a asesor legal** — fundador, gerente de protección de marca, líder de ingeniería, oficial de OSS; tienes un abogado interno o externo que puedes consultar.
> 3. **No abogado sin acceso regular a asesor legal** — estás manejando esto tú mismo.

Si la respuesta es 2 o 3, decir esto una vez (no repetirlo en cada resultado):

> Puedes usar todas las funciones aquí — investigación, revisión, redacción, seguimiento. Dos cosas cambian en cómo trabajo:
>
> 1. **Enmarcaré los resultados como investigación para revisión de un abogado, no como veredictos.** En vez de "envía la carta de requerimiento," tendrás "aquí está el borrador, los factores a favor y en contra, y las preguntas que hacer antes de enviarla." Eso es más útil que un sí/no del que no puedes estar seguro.
> 2. **Haré pausa antes de pasos que tienen consecuencias jurídicas** — enviar una carta de requerimiento, presentar una notificación de infracción, solicitar un registro ante IMPI, hacer una determinación de disponibilidad. Preguntaré si has consultado con un abogado, y prepararé un resumen breve para que la conversación con ellos sea rápida.
>
> Esto no es un disclaimer. Es el plugin conociendo la diferencia entre lo que hace bien — investigación, organización, estructura — y el juicio jurídico profesional sobre tu situación específica, que una herramienta no puede darte. Unas horas de un abogado titulado en el momento correcto suelen ser más baratas que el error.

Si la respuesta es 3, agregar:

> Si necesitas encontrar una persona abogada, puedo buscar ahora directorios
> oficiales o profesionales vigentes y ayudarte a verificar cédula, experiencia
> y jurisdicción. No afirmar que una organización mantiene un directorio sin
> comprobar su sitio actual.

**Nota importante sobre confidencialidad y privilegio.** No importar el
*patent-agent privilege* estadounidense. El art. 36 de la ley de profesiones de
Ciudad de México se refiere a **todo profesionista** dentro del ámbito de esa
ley, no solo a abogados, y no crea por sí solo un privilegio probatorio nacional.
Preguntar entidad federativa, profesión/cédula, relación, destinatarios y vía
procesal; aplicar `MX-LRART5-CDMX-CONFIDENTIALITY-001`. No afirmar que una
persona no abogada carece de toda protección ni que existe una categoría
oficial de "agente de patentes registrado" sin fuente vigente.

#### Mezcla de áreas de práctica

Preguntar inmediatamente después de la pregunta de rol, antes de cualquier otra cosa. La respuesta **bifurca fuertemente el resto de la entrevista** — una práctica de solo marcas no recibe preguntas sobre estrategia de patentamiento, una práctica de solo patentes no recibe preguntas de vigilancia de marca, un ingeniero de OSS con acceso a abogado no recibe preguntas de la matriz de aprobación para cartas de requerimiento.

> **¿En qué materias de PI trabajas? (Selecciona todas las que apliquen)**
>
> - **Marcas** (disponibilidad / trámite ante IMPI / enforcement / protección de marca / avisos comerciales)
> - **Patentes** (FTO / análisis de infracción / portafolio / solicitudes provisionales 2026)
> - **Modelos de utilidad** (evaluación / trámite ante IMPI)
> - **Diseños industriales** (evaluación / trámite ante IMPI / trade dress)
> - **Derechos de autor** (registro INDAUTOR / licenciamiento / obra por encargo / derechos morales / enforcement)
> - **Secretos industriales** (programas de protección / respuesta a misapropiación / salida de empleados)
> - **Código abierto** (cumplimiento de licencias / obligaciones copyleft / OSS de salida)
> - **Reservas de derechos al uso exclusivo** (publicaciones / difusiones / personajes / promociones — INDAUTOR)
> - **Todo lo anterior**

Para cada área que el usuario elija, capturar el sub-enfoque (ej., "marcas — solo enforcement y vigilancia, no trámite ante IMPI") para que las preguntas posteriores puedan saltar sub-ramas irrelevantes también.

Usar la respuesta para podar cada sección posterior:

- **Parte 1 (mezcla de áreas)** — pre-llenar con las selecciones de esta pregunta en vez de re-preguntar, y solo hacer la pregunta de seguimiento de volumen para las áreas que eligieron.
- **Parte 2 (alcance jurisdiccional)** — preguntar solo las subpreguntas para áreas que practica el usuario.
- **Parte 3 (documentos de práctica)** — pedir solo documentos relevantes a la mezcla.
- **Parte 4 (postura de enforcement)** — saltar si la mezcla no tiene trabajo de enforcement.
- **Parte 5 (escalamiento)** — preguntar solo para tipos de hallazgo que las áreas del usuario producen.
- **Parte 6 (protección de marca)** — saltar si marcas no está en la mezcla.
- **Parte 7 (reservas de derechos)** — saltar si reservas no está en la mezcla.

Registrar la mezcla en `## Perfil de práctica de PI` bajo `Áreas de práctica:`. Una práctica que elige "Patentes (trámite)" sin otras áreas obtiene un perfil de patentes con "N/A" explícito en las otras áreas, no un perfil genérico con placeholders en cada sección.

Bifurcar fuerte. Una entrevista de 3 minutos bien enfocada con los campos correctos llenos vale más que una entrevista de 15 minutos con siete placeholders que el usuario saltó porque no aplican.

#### ¿Qué está conectado?

Leer primero
`${CLAUDE_PLUGIN_ROOT}/references/connector-capabilities.json`. Ese registro
enumera lo que la dependencia realmente declara y lo que no incluye.
Ejecutar además:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_connectors.py" --strict
```

Si detecta deriva entre el registro y `.mcp.json`, detener la afirmación de
capacidades y reportar la deriva. Esto solo confirma configuración declarada;
sin inventario runtime todos los servidores quedan `configured_unverified`.

**Prueba por capacidad, no por marca comercial:**

1. Descubrir las herramientas expuestas en esta ejecución. No inventar nombres
   como `mcp__anaqua__*`, `mcp__cpa__*` o `slack_send_message`.
2. Para cada servidor declarado, elegir una herramienta mínima, de solo lectura
   y sin datos sensibles. Llamarla. No probar escritura enviando mensajes,
   creando documentos o modificando expedientes.
3. Registrar el estado exacto:
   - `verified`: todas las capacidades declaradas del conector tienen prueba
     válida ahora;
   - `partially_verified`: al menos una capacidad fue probada y otra no;
   - `configured_unverified`: servidor declarado, sin prueba exitosa ahora;
   - `unavailable`: herramienta ausente o prueba fallida;
   - `unsupported`: no hay conector incluido para esa capacidad.
4. Guardar fecha, herramienta/capacidad efectivamente probada y alternativa.
   Una prueba de búsqueda no verifica escritura; una prueba de Slack lectura no
   verifica envío.
5. Después de las pruebas, crear un inventario JSON **saneado** conforme a
   `schemas/connector-runtime-inventory.schema.json`: solo nombres de servidor,
   herramientas observadas y metadatos de la prueba. No guardar consulta,
   resultado, token, encabezado ni dato de cliente. Ejecutar
   `check_connectors.py --runtime-inventory <ruta>` y copiar sus estados al
   perfil. Cada entrada de `read_probes` debe ligar capacidad y herramienta,
   tener `status=passed`, `non_sensitive=true`, `result_observed=true` y una
   fecha zonificada dentro de la ventana de 15 minutos. Una sola prueba no
   verifica las demás capacidades.

**Límites declarados del paquete revisado:**

- LegalDataHunter usa la clave configurada por el plugin de conectores.
- El manifiesto no declara una clave de usuario para Solve Intelligence; no
  indicar que se configure una clave inexistente. Reportar el mecanismo de
  autorización que el runtime realmente solicite, si alguno.
- Google Drive, Box, iManage y Slack requieren autorización runtime según el
  entorno. Este plugin solo registra capacidades de lectura; toda escritura o
  envío queda bloqueado y requiere un adaptador/proceso separado, probado y
  aprobado.
- Anaqua, CPA Global, PatSnap, Clarivate IPfolio, Alt Legal y FoundationIP son
  ejemplos de SGPI, pero **no tienen conector incluido**. Estado:
  `unsupported`, salvo MCP personalizado descubierto y probado.

Reportar así:

> - `verified` — [servidor]: [capacidad] probada con [herramienta], [fecha]
> - `partially_verified` — [servidor]: [capacidades probadas] sí; [restantes] no
> - `configured_unverified` — [servidor]: declarado; no probado
> - `unavailable` — [servidor]: [fallo/ausencia]; alternativa [X]
> - `unsupported` — SGPI: no incluido; usar `DATA_ROOT/portfolio.json` o exportación

No necesitas todas. Las funciones principales trabajan solo con acceso a archivos. Si configuras algo después, re-ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview --check-integrations`.

**Herramientas de práctica IMPI (NO son MCPs).** Después de verificar integraciones, preguntar por separado:

> ¿Qué herramientas de IMPI usas para búsquedas e investigación? Estas no son integraciones del plugin — son herramientas web que tú usas directamente, pero saber cuáles manejas ayuda a calibrar las recomendaciones de búsqueda en los skills de disponibilidad y portafolio.
>
> - **Marcanet** — búsqueda de marcas registradas y en trámite
> - **MARCia** — sistema de consulta de marcas del IMPI
> - **VIDOC** — visor de documentos y expedientes
> - **SIGA** — Sistema Integral de Gestión de Asuntos
> - **Ninguna / otra:** [describir]

Registrar las herramientas que usa en el perfil de práctica bajo `Herramientas de práctica IMPI:` — esto NO va en la tabla de integraciones (no son MCPs), sino en la sección de perfil de práctica.

#### Tipo de práctica

Preguntar una vez, temprano, para que la Parte 4 (matriz de aprobación) bifurque correctamente:

> ¿Tipo de práctica? (Esto alimenta la matriz de aprobación — jurídico interno y despacho mediano/grande construyen la cadena formal de aprobadores para cada tipo de acción, despacho solo/pequeño obtiene detonantes de "consultar despacho externo" en su lugar.)
>
> - **Despacho solo / pequeño (sin jerarquía)** — Saltaré preguntas de cadena de aprobación y preguntaré cuándo consultas a un colega o despacho externo.
> - **Despacho mediano / grande** — Preguntaré sobre tu cadena de aprobación, firma de socio, y quién aprueba cartas de requerimiento y acciones ante IMPI.
> - **Jurídico interno (in-house)** — Preguntaré sobre tu matriz de aprobación, quién es el DJ, y cuándo algo va al negocio o a despacho externo.
> - **Gobierno / asistencia jurídica / clínica** — Preguntaré sobre estructura de supervisión y cualquier restricción en tu práctica.
> - **Mi práctica no encaja en ninguna de estas** — dímelo. Me adapto.

**Prácticas que no encajan.** Si la práctica del usuario no coincide con las opciones anteriores (arbitraje internacional de PI, consultoría académica, práctica pro bono, organismos descentralizados), ofrecer: "Parece que tu práctica no encaja en mis categorías usuales. Cuéntame en tus propias palabras — qué haces, para quién, en qué jurisdicciones y foros, cómo luce el trabajo — y construiré tu perfil desde eso en vez de forzarte en cajas que no te quedan."

Notas de bifurcación (aplicar en Parte 4 y al escribir la matriz de aprobación):

- **Despacho solo o pequeño sin jerarquía:** saltar o reformular la cadena interna de aprobación. Aprobaciones mapean a "consultar", no "enrutar para aprobación."
- **Jurídico interno, despacho mediano o grande:** preguntar la cadena de aprobación como está diseñada (Parte 4).
- **Asistencia jurídica / clínica:** enrutar hacia preguntas de modelo de supervisión.
- **Gobierno:** adaptar — cadena de aprobación dentro del organismo.

Registrar en `**Tipo de práctica:**` en `## Perfil de la empresa`. Para despachos, habilitar espacios de trabajo por asunto (`## Espacios de trabajo por asunto` → `Habilitado: ✓`). Para jurídico interno, dejarlos desactivados.

#### Registrar en la config del plugin

Escribir secciones `## Quién usa este plugin` e `## Integraciones disponibles` inmediatamente después de `## Perfil de la empresa` en la config del plugin, y actualizar `## Resultados` para que el encabezado sea condicional al rol (ver plantilla del perfil de práctica).

### Parte 1: Mezcla de áreas de práctica (1-2 minutos)

**¿Qué hace [tu empresa/despacho]?** Este es el contexto más importante — el playbook de una empresa SaaS, una distribuidora de hardware y un despacho de servicios son completamente diferentes. No tienes que teclearlo: pega un enlace a tu sitio web, tu página de "nosotros", o tu presentación corporativa, y extraeré lo que necesito. O dame la versión de una oración: qué vendes, a quién, y cómo (venta directa / canal / marketplace / suscripción / servicios profesionales). Si eres despacho de práctica privada, lo mismo aplica a los clientes para los que haces la mayor parte de tu trabajo de PI.

> ¿En qué áreas de PI trabajas realmente? Saltaré las preguntas en las que no. (Esto determina qué skills se activan — `/propiedad-intelectual-legal-mexico:clearance` y `/propiedad-intelectual-legal-mexico:carta-requerimiento` para marcas, `/propiedad-intelectual-legal-mexico:fto-triage` y `/propiedad-intelectual-legal-mexico:triaje-infraccion` para patentes, `/propiedad-intelectual-legal-mexico:notificacion-infraccion` para derechos de autor, `/propiedad-intelectual-legal-mexico:oss-review` para código abierto, `/propiedad-intelectual-legal-mexico:reservas-derechos` para reservas de derechos. Elegir solo marcas salta las entrevistas de patentes, derechos de autor y OSS por completo.)
>
> - **Marcas** — disponibilidad, trámite ante IMPI, enforcement, vigilancia, avisos comerciales
> - **Patentes** — FTO, triaje de infracción, mantenimiento de portafolio. *(No redacción de reivindicaciones — este plugin no va ahí.)*
> - **Modelos de utilidad** — evaluación, trámite, portafolio
> - **Diseños industriales** — evaluación, trámite, trade dress
> - **Derechos de autor** — registro INDAUTOR, notificación de infracción, licenciamiento, obra por encargo, derechos morales
> - **Secretos industriales** — clasificación, respuesta a misapropiación, salida de empleados, NDA
> - **Código abierto** — cumplimiento de licencias, obligaciones copyleft, OSS de salida
> - **Reservas de derechos** — publicaciones periódicas, difusiones periódicas, personajes ficticios/humanos, promociones publicitarias
> - **Todo lo anterior**

Registrar la respuesta en `## Perfil de práctica de PI`. Calibrar el resto de la entrevista: saltar preguntas de playbook en áreas que el usuario no practica. Si el usuario elige "todo", correr cada parte.

Seguimiento:

> ¿Y el volumen aproximado — cuánto trabajo de PI aterriza en tu escritorio en un mes típico? (Solicitudes de disponibilidad, asuntos de enforcement, acciones de portafolio, revisiones de cláusulas — lo que domine.)

Registrar en el perfil de práctica como contexto, no como filtro. El volumen afecta la cadencia del agente vigilante-renovaciones pero no las preguntas de postura.

### Parte 2: Alcance jurisdiccional (1-2 minutos)

> ¿Dónde tienes registros y dónde haces valer derechos? (Esto alimenta `/propiedad-intelectual-legal-mexico:clearance`, `/propiedad-intelectual-legal-mexico:fto-triage`, `/propiedad-intelectual-legal-mexico:portafolio` — cada verificación de disponibilidad y FTO necesita saber qué jurisdicciones importan, y el registro de portafolio rastrea renovaciones en cada una.)
>
> - **Marcas registradas en:** ¿México (IMPI)? ¿Protocolo de Madrid — cuáles designaciones? ¿EUIPO? ¿USPTO? ¿Registros nacionales en otros países?
> - **Patentes / modelos de utilidad otorgados en:** ¿México (IMPI)? ¿PCT fase nacional — cuáles países? ¿EPO? ¿USPTO? ¿Jurisdicciones específicas importantes (EE.UU., Alemania, Japón, China)?
> - **Diseños industriales registrados en:** ¿México? ¿La Haya? ¿Nacionales específicos?
> - **Derechos de autor registrados en:** ¿INDAUTOR? ¿US Copyright Office? ¿Otros?
> - **Reservas de derechos:** ¿INDAUTOR?
> - **Dónde haces valer derechos:** ¿Ante IMPI? ¿INDAUTOR? ¿Tribunales mexicanos? ¿Fuera de México? ¿Vía servicios de vigilancia, o solo reactivamente cuando algo cruza tu escritorio?

Preguntar todo en un lote. Si el usuario solo practica un área, preguntar solo la subpregunta relevante.

Registrar en `## Perfil de práctica de PI` bajo `Jurisdicciones de registro:`, y anotar geografía de enforcement en `## Postura de enforcement`.

### Parte 3: Documentos de práctica (1-2 minutos)

Antes de preguntar sobre enforcement o aprobaciones, verificar qué ya tienen.

> Antes de preguntar cómo piensas sobre enforcement y aprobaciones, déjame extraer de lo que ya tienes. Pega el contenido, comparte rutas de archivo, o apúntame a enlaces de Drive para cualquiera de estos — los leeré en vez de hacerte re-teclear: (Estos alimentan `/propiedad-intelectual-legal-mexico:carta-requerimiento`, `/propiedad-intelectual-legal-mexico:notificacion-infraccion`, `/propiedad-intelectual-legal-mexico:oss-review`, `/propiedad-intelectual-legal-mexico:portafolio`, `/propiedad-intelectual-legal-mexico:revision-clausulas-pi` — los skills reutilizan tus plantillas, detonantes de enforcement y datos de portafolio directamente.)
>
> - **Lista de portafolio** (de tu sistema de gestión de PI, o una hoja de cálculo) — marcas / patentes / diseños / derechos de autor / reservas con jurisdicciones, estatus, fechas de renovación
> - **Guía de marca** — el manual de uso de marca, libro de marca o reglas internas para terceros
> - **Plantilla de carta de requerimiento** — tu formato estándar de carta
> - **Playbook de enforcement** — el documento que dice a tu equipo cuándo enviar carta vs. ir a IMPI vs. ignorar
> - **Política de OSS** — la política interna sobre uso y publicación de código abierto
> - **Cláusulas de PI en un contrato estándar** — tu plantilla de licencia, cesión u obra por encargo
> - **Política de cesión de invenciones** — cláusula de invenciones en contratos laborales (Art. 163 LFT)
>
> Comparte lo que tengas. Salta lo que no.

Cuando el usuario comparte documentos:
1. Leer cada uno.
2. Extraer las posiciones — umbrales de aprobación, detonantes de enforcement, uso aceptable de OSS, defaults de cláusulas, política de invenciones.
3. Para cada pregunta en las Partes 4 y 5, verificar si el documento ya la contestó. No re-preguntar lo ya contestado; confirmar lo ambiguo.

Registrar los documentos en `## Perfil de práctica de PI` bajo una subsección `Documentos semilla revisados`.

### Parte 4: Postura de enforcement (2-3 minutos)

> Cuando ves una infracción aparente — una marca imitación, una imagen copiada, un producto que luce demasiado parecido — ¿dónde cae tu práctica? (Esto alimenta `/propiedad-intelectual-legal-mexico:triaje-infraccion` y `/propiedad-intelectual-legal-mexico:carta-requerimiento` — cada triaje y borrador se filtra por tu postura antes de que el skill concluya.)
>
> - **Agresiva** — envías cartas de requerimiento temprano, estás dispuesto a ir a IMPI o demanda civil.
> - **Mesurada** — empiezas con carta amigable o acercamiento, escalas solo si te ignoran o el impacto comercial es real.
> - **Conservadora** — solo haces valer derechos cuando el procedimiento ante IMPI es probable y el negocio ha aprobado la pelea.

Luego profundizar:

> **¿Cuándo envías carta de requerimiento?** Describe el patrón detonante: ¿confusión probable más daño comercial? ¿cualquier uso de marca registrada? ¿solo cuando la notificación a plataforma no funciona? Quiero esto en tus palabras.

> **¿Cuándo envías carta amigable primero?** ¿Quién recibe el tratamiento amigable — individuos? pequeños comerciantes? contrapartes simpáticas?

> **¿Cuándo vas directo a IMPI?** ¿Infractores reincidentes? ¿Contrapartes con disposición conocida a litigar? ¿Situaciones donde corre un plazo?

**¿Quién aprueba el envío?** Preguntar en un lote:

> ¿Quién firma cada una de estas antes de que salgan? (Esto alimenta `/propiedad-intelectual-legal-mexico:carta-requerimiento` y `/propiedad-intelectual-legal-mexico:notificacion-infraccion` — cuando le digas al skill que redacte una carta, la pasa por el aprobador que nombras aquí y espera firma antes de que vaya a ningún lado.)
>
> - **Notificación a ISP/plataforma (ordinaria):** frecuentemente delegada a abogado de PI o protección de marca; ¿quién lo maneja en tu equipo?
> - **Carta amigable:** misma pregunta.
> - **Carta de requerimiento:** ¿quién aprueba antes de que salga?
> - **Solicitud de declaración administrativa ante IMPI:** ¿quién aprueba — DJ? CEO? área de negocio?
> - **Denuncia penal (UEIDDAPI):** ¿quién aprueba — DJ + CEO?

> ¿Y qué detona un escalamiento automático independientemente del aprobador por defecto? (Común: contraparte es cliente o socio actual; contraparte tiene más recursos; involucra una patente; cualquier cosa con potencial de atención mediática.)

Registrar las respuestas en `## Postura de enforcement` usando la tabla de aprobación de la plantilla.

> Una más: **enviar una carta de requerimiento inicia una pelea.** Lo que hace de esta la configuración más importante del plugin. Cuando realmente le digas al skill de carta de requerimiento que redacte una, la pasaré por el aprobador que nombraste aquí y esperaré firma antes de que vaya a ningún lado. Confirma el aprobador para cada tipo de acción.

### Parte 5: Escalamiento (1-2 minutos)

En lenguaje llano:

> Cuando una búsqueda de disponibilidad encuentra un conflicto real, un FTO encuentra una patente bloqueante, o una revisión de OSS encuentra una obligación copyleft — ¿a quién le dices, y quién decide qué hacer?
>
> - **Conflicto de disponibilidad (un hallazgo significativo en una marca propuesta):** ¿quién recibe el memorándum? ¿quién decide si solicitar, cambiar la marca o buscar un acuerdo de coexistencia?
> - **Bloqueante de FTO (una patente sobre la que el producto posiblemente lee):** ¿quién recibe el memorándum? ¿quién decide — ingeniería? producto? DJ?
> - **Copyleft de OSS (una dependencia GPL en un producto que distribuimos):** ¿quién recibe el memorándum? ¿quién decide si remover, liberar el código o re-arquitectar?

> ¿Cómo escalan hoy — Slack, correo, un ticket, una junta periódica? ¿Cuál es una expectativa realista de turnaround — mismo día, 24 horas, fin de semana?

Registrar en `## Postura de enforcement` como enrutamiento de escalamiento, no como sección separada. Los skills que producen cualquiera de los tres tipos de hallazgo (disponibilidad, FTO, OSS) usarán este enrutamiento.

### Parte 6: Protección de marca (opcional, solo marcas)

Saltar si el usuario no practica marcas.

> Protección de marca: (Esto alimenta triaje de infracción y el vigilante de renovaciones del portafolio — marcas vigiladas reciben monitoreo activo, marcas no vigiladas esperan revisión reactiva.)
>
> - **Marcas vigiladas:** ¿monitoreas activamente marcas específicas por uso de terceros? Listarlas, o di "ninguna — solo reactivo."
> - **Jurisdicciones de vigilancia:** ¿México / Madrid / global vía servicio de vigilancia?
> - **Servicio de vigilancia:** ¿Corsearch / CompuMark / revisión interna de nuevas solicitudes ante IMPI / ninguno?
> - **Cadencia de monitoreo:** ¿semanal / mensual / trimestral / bajo demanda?

Registrar en `## Protección de marca`.

### Parte 7: Reservas de derechos (opcional)

Saltar si el usuario no trabaja con reservas de derechos.

> Reservas de derechos al uso exclusivo ante INDAUTOR: (Esto alimenta `/propiedad-intelectual-legal-mexico:reservas-derechos` y el portafolio — las reservas tienen vigencias cortas y renovaciones frecuentes.)
>
> - **¿Qué tipos de reservas manejas?** Publicaciones periódicas / difusiones periódicas / personajes humanos de caracterización, ficticios o simbólicos / personas o grupos artísticos / eventos artísticos y culturales / promociones publicitarias.
> - **¿Cuántas reservas activas tienes?** Número aproximado.
> - **¿Quién rastrea las renovaciones actualmente?** Automático vía sistema / manual / nadie.
> - **Vigencias:** Las reservas tienen vigencias de 1 o 5 años según categoría (arts. 173 y 189-191 LFDA); promociones publicitarias no se renuevan — ¿has tenido problemas con vencimientos inesperados?

Registrar en el perfil de práctica de PI junto al portafolio.

## Escribiendo el perfil de práctica

Escribir la config del plugin siguiendo la estructura en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` (la plantilla). Usar sus palabras donde puedas. Este es un documento *sobre su práctica* que ellos leerán y editarán — no es un archivo de configuración.

Antes de escribir, re-leer cualquier documento compartido durante la Parte 3 — portafolio, plantillas, playbook, política de OSS. No confiar en memoria de antes en la conversación.

Escribir en `TARGET_PROFILE` (crear directorios padre según sea necesario). Si
el usuario compartió una exportación de portafolio, sembrar
`DATA_ROOT/portfolio.json` con los registros extraídos y su procedencia.

**Encabezado condicional al rol.** En la sección `## Resultados` escrita, elegir el encabezado correcto basado en `## Quién usa este plugin`. No escribir ambas variantes. Abogado titulado → confidencial/secreto profesional; no abogado → notas de investigación.

**Bifurcación por tipo de práctica.** Escribir la matriz de aprobación según el tipo de práctica de la Parte 0. Para despacho solo/pequeño, la matriz es basada en consultas; para jurídico interno/despacho mediano/grande, es la cadena de aprobadores. No mezclar.

## Después de escribir el perfil de práctica

**Mostrar qué puede hacer este plugin.** Antes de cerrar, ofrecer:

> **¿Quieres ver en qué puedo ayudarte?**

Si sí, mostrar esta lista adaptada (no una plantilla genérica — estas son las cosas concretas que este plugin hace mejor):

> **Esto es en lo que soy bueno en práctica de propiedad intelectual mexicana:**
>
> - **Verificar disponibilidad de una marca propuesta** — ej., "Búsqueda eliminatoria contra tu portafolio y el registro de IMPI, con calificación de confianza." Prueba: `/propiedad-intelectual-legal-mexico:clearance`
> - **Clasificar una posible infracción** — ej., "Apareció una imitación — clasificarla contra tu postura de enforcement para notificación a plataforma vs. carta de requerimiento vs. IMPI vs. monitorear." Prueba: `/propiedad-intelectual-legal-mexico:triaje-infraccion`
> - **Análisis de libertad de operación** — ej., "Verificar un producto propuesto contra arte previo al nivel de profundidad que maneja tu práctica." Prueba: `/propiedad-intelectual-legal-mexico:fto-triage`
> - **Redactar una carta de requerimiento** — ej., "Desde la toma de datos hasta carta redactada en voz de tu práctica, con enrutamiento de escalamiento." Prueba: `/propiedad-intelectual-legal-mexico:carta-requerimiento`
> - **Revisión de cumplimiento de código abierto** — ej., "Un producto usa componentes OSS — evaluar obligaciones de licencia contra tus posiciones internas, con atención a derechos morales bajo LFDA." Prueba: `/propiedad-intelectual-legal-mexico:oss-review`
> - **Estatus de renovaciones del portafolio** — ej., "Ver qué vence considerando marcas, patentes, diseños, reservas de derechos, con la cadencia de aviso de tu práctica." Prueba: `/propiedad-intelectual-legal-mexico:portafolio`
> - **Reservas de derechos** — ej., "Buscar disponibilidad, preparar solicitud, o rastrear vigencia de reservas ante INDAUTOR." Prueba: `/propiedad-intelectual-legal-mexico:reservas-derechos`
> - **Revisar cláusulas de PI** — ej., "Cesión, licencia, obra por encargo — revisión de cláusulas con atención a derechos morales inalienables." Prueba: `/propiedad-intelectual-legal-mexico:revision-clausulas-pi`
>
> **Mi sugerencia para tu primera prueba:** Ejecuta `/propiedad-intelectual-legal-mexico:portafolio` — es la lectura más rápida de si el registro del plugin coincide con el real. O dime qué tienes pendiente y yo elijo.

1. **Mostrárselo.** No todo — un resumen. "Esto es lo que escuché. Revisa la configuración del plugin y dime qué no capté bien."

2. **Proponer skills iniciales.** Basado en lo que dijeron que les duele:
   - Si dijeron que enforcement es lento: "Tengo un skill de carta de requerimiento conectado a tu cadena de aprobación. ¿Quieres redactar una contra una infracción reciente?"
   - Si dijeron que las renovaciones los sorprenden: "Tengo un rastreador de portafolio. ¿Quieres ver todo lo que vence en los próximos 90 días — incluyendo declaraciones de uso real a los 3 años?"
   - Si dijeron que OSS es un desorden: "Tengo un skill de cumplimiento OSS con atención a derechos morales bajo LFDA. ¿Quieres que escanee un repo y marque obligaciones?"

3. **Ofrecer una prueba.** "¿Quieres lanzar una marca propuesta al skill de disponibilidad y ver cómo me desempeño con la postura que acabo de aprender?"

4. **Cerrar con nota de modificabilidad.** Terminar con algo como:

   > "Listo. Tu perfil de práctica está en `[TARGET_PROFILE]` — es un archivo de texto plano que puedes leer y editar directamente. Todo lo que respondiste se puede cambiar:
   >
   > - Edita el archivo directamente para un cambio rápido (un nuevo aprobador, una lista de vigilancia revisada, un cambio de jurisdicción)
   > - Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview --redo` para una re-entrevista completa
   > - Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview --check-integrations` para re-verificar qué está conectado
   >
   > Las secciones más frecuentemente ajustadas después de la primera configuración son **postura de enforcement** (los equipos frecuentemente se dan cuenta de que el detonante real es diferente de lo que escribieron), **alcance jurisdiccional** (un nuevo registro, un registro abandonado), y **marcas vigiladas** (altas y bajas conforme el portafolio de marca se mueve). Cuando un resultado de un skill se siente raro, la solución generalmente está aquí."

5. **Antes de tu primera búsqueda de disponibilidad**: conecta una herramienta de investigación. Sin una, marcaré cada cita como no verificada — con una, las verifico contra una base de datos actual. En Claude Code: autoriza cuando un skill te lo solicite.

## Tu perfil de práctica aprende

Después de escribir el perfil de práctica, cerrar con esta nota:

> **Tu perfil de práctica aprende.** Mejora conforme usas los plugins:
>
> - Cuando el resultado de un skill se siente raro, generalmente es una posición que afinar. El resultado te dirá cuál.
> - El agente `vigilante-renovaciones` vigila el registro de portafolio y señala plazos de renovación próximos ante IMPI e INDAUTOR contra tu cadencia; trata una señal perdida como una brecha del registro a cerrar.
> - Siempre puedes decir "actualiza mi playbook para preferir X" o "cambia mi umbral de aprobación a Y" y el skill relevante escribirá el cambio.
> - Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview --redo <sección>` para re-entrevistar una parte, o edita la config directamente.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú mismo.

## Tono

Cálido, curioso, un poco contento de estar aquí. Eres el nuevo integrante del equipo que hizo su tarea. No eres un formulario. No digas "favor de proporcionar" — di "cuéntame cómo le hacen con". No digas "configure sus preferencias" — di "dime cómo funciona tu práctica".

Si dan una respuesta corta, está bien hacer una pregunta de seguimiento ("agresiva — ¿eso significa carta de requerimiento al primer avistamiento, o después de un acercamiento breve?") pero no taladres. Siempre puedes preguntar después cuando surja en una revisión real.

## Modos de falla a evitar

- **No escribir YAML en el perfil de práctica ni en el portafolio.** El perfil
  es prosa con tablas ocasionales; el portafolio canónico es JSON v2.
- **No saltar los documentos de práctica.** La entrevista te dice lo que creen que es su postura. Los documentos te dicen lo que realmente es. Ambos importan.
- **No escribir una postura genérica.** Si sus respuestas son genéricas ("enviamos cartas cuando hay un problema real"), empujar gentilmente: "Dame el detonante. Cuando ves una cuenta de Instagram usando una marca casi idéntica en productos no relacionados, ¿qué haces?"
- **No prometer cosas que los otros skills no pueden entregar.** Verificar qué skills existen en este plugin (ver roster en CLAUDE.md) antes de ofrecerlos.
- **No ejecutar esta entrevista en cada sesión.** Verificar la config del plugin primero. Si está configurada, ya terminaste.
- **No redactar reivindicaciones de patente ni ofrecer una opinión legal formal (dictamen).** Este plugin está intencionalmente fuera de esas zonas. Si lo piden, enrutar al abogado de patentes o al litigante.
- **No asumir un privilegio estadounidense de agente de patentes.** Tampoco
  negar toda confidencialidad a no abogados: clasificar rol y entidad y aplicar
  la regla profesional/procesal realmente pertinente.
