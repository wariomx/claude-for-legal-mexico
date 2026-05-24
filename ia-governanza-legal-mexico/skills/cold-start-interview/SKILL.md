---
description: >
  Ejecuta la entrevista de configuración inicial para conocer tu práctica de
  gobernanza de IA y escribir tu perfil de práctica. Usa en la primera
  instalación cuando el perfil no existe o aún contiene placeholders, al
  reconfigurar con --redo, o al re-verificar integraciones con
  --check-integrations después de conectar o desconectar un MCP. Este es el
  ÚNICO skill que debe ejecutarse en una instalación nueva.
argument-hint: "[--redo | --check-integrations | --local]"
---

## Bandera --local

Si se invoca con `--local`:

1. **Ruta de escritura:** `.claude-legal/ia-governanza-legal-mexico/CLAUDE.md` en el directorio de trabajo actual, en vez del path global (`~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`).
2. **`company-profile.md` compartido:** escribir también en `.claude-legal/company-profile.md` (en vez de global).
3. **Crear directorio:** crear `.claude-legal/ia-governanza-legal-mexico/` si no existe.
4. **`.gitignore`:** si existe un `.gitignore` en el directorio actual y no contiene `.claude-legal/`, agregar esa línea automáticamente y notificar: "Agregué `.claude-legal/` a tu `.gitignore`."
5. **Sobrescribir:** si ya existe `.claude-legal/ia-governanza-legal-mexico/CLAUDE.md`, preguntar antes de sobrescribir.
6. **Confirmación al terminar:** "✓ Perfil de cliente escrito en `.claude-legal/ia-governanza-legal-mexico/CLAUDE.md`. Desde esta carpeta, todos los skills usan este perfil. Para cambiar de cliente, cambia de directorio de trabajo."

---

# /cold-start-interview

Ejecuta la entrevista de configuración inicial. La primera ejecución escribe `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`; ejecuciones posteriores con `--redo` re-entrevistan y muestran un diff antes de sobrescribir.

## Instrucciones

1. **Verificar estado actual:** Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Si contiene `[PLACEHOLDER]` o `[Tu Empresa]`, proceder con entrevista nueva. Si está configurado y no se pasó `--redo`, preguntar: "Parece que ya estás configurado. ¿Quieres re-ejecutar la entrevista? Esto sobrescribirá tu perfil de práctica (te mostraré un diff primero)."

2. **Seguir el guión de entrevista de abajo.**

3. **Pedir documentos de práctica:** política interna de uso de IA existente (si hay), contratos con proveedores de IA o terms of service aceptados, registros previos de evaluaciones de impacto, inventario de herramientas de IA en uso. Aceptar rutas de archivo, enlaces de Google Drive o contenido pegado.

4. **Leer los documentos compartidos** y extraer posiciones reales — qué herramientas están en uso real, qué cláusulas tiene el contrato con el proveedor más importante, si existe política escrita o solo práctica informal.

5. **Migración:** Si existe un CLAUDE.md configurado (sin marcadores `[PLACEHOLDER]`) en `~/.claude/plugins/cache/claude-for-legal/ia-governanza-legal-mexico/*/CLAUDE.md` pero no en la ruta de config, copiarlo a la ruta de config y mostrar al usuario lo que se migró.

6. **Escribir `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`** (crear directorios padre según sea necesario) conforme a la estructura de la plantilla. Usar las palabras del abogado donde sea posible.

7. **Sembrar el registro de casos de uso** si el usuario compartió un inventario de herramientas de IA: escribir en `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/use-case-register.yaml`. Si no se compartió nada, dejar un puntero placeholder que el skill de triaje pueda llenar después.

8. **Mostrar resumen + proponer siguientes pasos:**
   - "Esto es lo que escuché — tu perfil está escrito. ¿Qué no capté bien?"
   - Ofrecer una prueba: "¿Quieres clasificar tu primer caso de uso de IA con `/ia-governanza-legal-mexico:use-case-triage`, o revisar el contrato con tu proveedor más importante con `/ia-governanza-legal-mexico:vendor-contract-review`?"

## `--check-integrations`

Re-ejecuta la verificación de disponibilidad de integraciones (LegalDataHunter, almacenamiento de documentos, Slack) y actualiza `## Integraciones disponibles` en el perfil de práctica. No re-entrevista. Usar cuando conectes o desconectes un MCP y quieras que el plugin lo note sin re-ejecutar toda la configuración.

Al verificar: solo reportar ✓ si una llamada MCP tool realmente tuvo éxito. Conectores configurados pero no probados deben marcarse ⚪ con una línea explicando cómo confirmar. Nunca reportar ✓ basándose solo en declaraciones de `.mcp.json`.

## Propósito

Estás conociendo esta práctica de gobernanza de IA por primera vez. Tu trabajo es aprender cómo *ellos* gestionan el riesgo de IA hoy — no cómo se debería hacer en abstracto — y escribir lo que aprendas en un perfil de práctica vivo que cada otro skill en este plugin lee antes de hacer cualquier cosa.

El abogado debe salir de esta conversación sintiendo que acaba de integrar a un pasante de primera que hizo exactamente las preguntas correctas. Nunca debe ver un archivo YAML de configuración. Debe ver un documento sobre su práctica que pueda editar en español llano.

## Qué significa "cold start"

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSED AT: -->`** → saludar al usuario y ofrecer retomar desde esa sección.
- **Contiene `[PLACEHOLDER]` o `[Tu Empresa]` pero sin comentario de pausa** → la plantilla nunca se completó; ofrecer empezar de cero o retomar donde empiezan los placeholders.
- **Configurado (sin placeholders, sin comentario de pausa)** → ya configurado; saltar a menos que sea `--redo`.

## Verificar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-for-legal/company-profile.md`.

- **Si existe:** Leerlo. Mostrar confirmación de una línea: "Eres [nombre], [tipo de práctica], en [empresa], [industria], operando en [jurisdicciones]. ¿Correcto?" Si confirma, saltar las preguntas de empresa — ir directo a las específicas del plugin.
- **Si no existe:** Hacer las preguntas de empresa y escribirlas en el perfil compartido, luego continuar con las preguntas específicas del plugin. Decir al usuario: "Guardé tu perfil de empresa — los otros plugins jurídicos lo leerán y saltarán estas preguntas."

## Verificación de alcance de instalación

Antes de la orientación, si notas que el directorio de trabajo está dentro de un proyecto (no el directorio home del usuario), señalarlo una vez:

> **Aviso — parece que este plugin puede estar instalado con alcance de proyecto, lo que significa que solo puedo leer archivos en [directorio actual]. Si necesitarás que lea documentos de otro lugar, instala con alcance de usuario. Puedes continuar con alcance de proyecto, pero necesitarás mover archivos a esta carpeta.**

## Apertura y bifurcación

Abrir con el preámbulo de bifurcación. Mantenerlo en 3-4 líneas cortas. Preguntar rápido-o-completo antes que nada.

> **`ia-governanza-legal-mexico` es para quienes gestionan el riesgo legal de sistemas de inteligencia artificial — triaje de casos de uso, evaluaciones de impacto, revisión de contratos con proveedores de IA, exposición al EU AI Act para operaciones con nexo europeo, y política interna de uso de IA.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te dan tu rol, tipo de práctica, si tu organización tiene nexo europeo (determina si el EU AI Act aplica), y qué herramientas de IA usan actualmente, más valores por defecto funcionales para todo lo demás. **15 minutos** agrega el inventario completo de sistemas de IA, análisis de contratos con proveedores, estatus de política interna, EIPDs realizadas y documentos semilla.
>
> ¿Rápido o completo? (Puedes ampliar cuando quieras con `/ia-governanza-legal-mexico:cold-start-interview --redo`.)

**Ruta rápida:** preguntar solo Parte 0 (rol, tipo de práctica, integraciones) y Parte 1 (nexo europeo). Escribir la config con marcadores `[DEFAULT]` en todo lo demás. Cerrar con: "Listo. Puedes empezar a usar los comandos ahora. Usé valores por defecto razonables. Cuando el resultado de un skill se sienta raro, generalmente es un valor por defecto que debes ajustar — te dirá cuál. Ejecuta `/ia-governanza-legal-mexico:cold-start-interview --redo` cuando quieras hacer la entrevista completa."

## Guión de entrevista

### Parte 0 — Rol e integraciones

*(Saltar si el perfil compartido de empresa ya existe y está confirmado)*

- ¿Cuál es tu rol? (Abogado titulado / profesional jurídico | No abogado con acceso a asesor legal | No abogado sin acceso a asesor legal)
- ¿Eres jurídico interno de una empresa o trabajas en un despacho con múltiples clientes? (Determina si los espacios de trabajo por asunto son relevantes)
- ¿Qué integraciones tienes disponibles? (LegalDataHunter, Google Drive, SharePoint, Box, Slack — probar cada una que mencione)

### Parte 1 — Nexo europeo

*(Determina si el EU AI Act aplica. Crítico — hacerlo antes del inventario)*

- ¿Tu organización tiene clientes, usuarios finales o beneficiarios de sus productos/servicios en algún país de la Unión Europea?
- ¿Tiene empleados, oficinas o subsidiarias en algún país de la UE?
- ¿Tiene contratos con empresas europeas donde tu organización proporciona un sistema de IA o sus outputs?
- ¿Es tu organización proveedor de otra empresa que opera en la UE?

Si alguna respuesta es sí → nexo europeo confirmado, EU AI Act potencialmente aplicable. Anotar la naturaleza del nexo.
Si todas son no → nexo europeo ausente. El EU AI Act aún puede ser relevante de forma indirecta (ej., si un proveedor de IA de tu organización te requiere cumplimiento). Anotar la conclusión.
Si hay incertidumbre → marcar como "verificar con análisis más detallado" y ofrecer `/ia-governanza-legal-mexico:eu-ai-act-exposure`.

### Parte 2 — Inventario de IA

*(Para cada sistema o herramienta de IA en uso)*

Preguntar: ¿Qué herramientas o sistemas de IA usa tu organización actualmente? Incluir tanto herramientas que usa el personal (ChatGPT, Copilot, Gemini, etc.) como sistemas de IA integrados en procesos de negocio (modelos de predicción, sistemas de decisión automatizada, chatbots de atención a clientes, etc.).

Para cada sistema identificado, recopilar:
- Nombre / proveedor
- Propósito (¿para qué se usa?)
- ¿Procesa datos personales de clientes o empleados? (Sí/No/Parcialmente)
- ¿Genera decisiones o recomendaciones que afectan a personas? (Sí/No)
- ¿Quién en la organización es el responsable interno?

Hacer triaje inicial de clasificación EU AI Act solo si hay nexo europeo confirmado (una sola pregunta por sistema: ¿involucra biométrica, infraestructura crítica, evaluación educativa, decisiones de empleo, servicios esenciales, aplicación de la ley, migración, o justicia? — si sí, es posiblemente alto riesgo; si no, probablemente mínimo o limitado).

### Parte 3 — Política de IA

- ¿Existe una política interna de uso de IA? (Sí — pedir la ruta o que la peguen / En desarrollo / No)
- Si existe: ¿Qué herramientas de IA generativa están permitidas para el personal? ¿Hay herramientas prohibidas?
- ¿Quién puede aprobar el uso de una nueva herramienta de IA? ¿Hay un proceso formal?
- ¿Existe alguna restricción sobre qué información puede ingresarse a herramientas de IA externas (datos de clientes, información confidencial, datos personales)?

### Parte 4 — Contratos con proveedores de IA

- ¿Has revisado los contratos o términos de servicio con los proveedores de tus herramientas de IA más importantes (ej., OpenAI, Microsoft, Google, AWS)?
- Para los contratos más importantes: ¿El proveedor menciona explícitamente si usa tus datos para entrenamiento? ¿Tienes opt-out?
- ¿Quién es dueño de los outputs que genera el sistema?
- ¿El proveedor tiene algún límite de responsabilidad relevante?

### Parte 5 — Evaluaciones de impacto

- ¿Ha realizado la organización alguna evaluación de impacto de privacidad (DPIA/EIPD) para sistemas de IA que procesan datos personales?
- ¿Hay un umbral definido para cuándo se requiere una evaluación de impacto de IA?
- ¿Existe algún proceso de aprobación antes de poner en producción un nuevo sistema de IA?

### Parte 6 — Documentos semilla

- ¿Puedes compartir la política de uso de IA existente (si hay)?
- ¿Puedes compartir el contrato con el proveedor de IA más importante o el que más datos maneja?
- ¿Tienes un registro de herramientas de IA (Excel, YAML, lista en algún sistema)?
- ¿Tienes resultados de alguna evaluación de impacto previa?

Aceptar rutas de archivo, enlaces de Google Drive, o contenido pegado directamente.

## Escritura del perfil

Al completar la entrevista, escribir el perfil de práctica completo en `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md` usando la plantilla como andamiaje. Reemplazar cada `[PLACEHOLDER]` con las respuestas del usuario. Para campos no preguntados en la ruta rápida, usar `[DEFAULT — ejecuta cold-start-interview --redo para configurar]`.

Si el usuario compartió documentos:
- Extraer cláusulas relevantes del contrato con proveedor y poblar la tabla de Contratos con Proveedores de IA
- Extraer herramientas del inventario y poblar la tabla del Registro de Casos de Uso
- Escribir `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/use-case-register.yaml` con los sistemas identificados

Mostrar al usuario: "Esto es lo que escuché —" seguido de las 5-6 decisiones más importantes capturadas. Pedir confirmación. Escribir el archivo solo después de la confirmación.
