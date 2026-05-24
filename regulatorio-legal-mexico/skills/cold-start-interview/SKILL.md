---
description: >
  Configura el plugin regulatorio-legal-mexico para tu práctica. Hace preguntas
  sobre tu empresa, sectores regulados, reguladores relevantes (COFECE, CNBV,
  COFEPRIS, IFT, CRE, CONAMER), módulos activos y preferencias de monitoreo del
  DOF. Escribe el perfil de práctica en
  ~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/CLAUDE.md
  (o en .claude-legal/regulatorio-legal-mexico/CLAUDE.md con --local para
  aislamiento por cliente). Sin esta configuración todos los skills producen
  resultados genéricos.
argument-hint: "[--local] [--redo] [--module dof|cofece|cnbv|cofepris|ift|cre|conamer] [--check-integrations]"
---

# Skill: cold-start-interview (regulatorio-legal-mexico)

## Propósito

Configurar el plugin regulatorio-legal-mexico para que todos los skills produzcan resultados calibrados a tu práctica, sector y reguladores relevantes. Sin esta configuración, los skills son genéricos y no pueden adaptar sus análisis a tus umbrales de riesgo, reguladores específicos o políticas de cumplimiento.

## Rutas de configuración

- **Global (por defecto):** `~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/CLAUDE.md`
- **Local (con `--local`):** `.claude-legal/regulatorio-legal-mexico/CLAUDE.md` en el directorio de trabajo actual

Usar `--local` cuando trabajas en un proyecto de cliente específico y quieres aislamiento de configuración. **Agregar `.claude-legal/` al `.gitignore` del proyecto** — contiene datos del cliente.

El perfil compartido de la empresa se escribe (o actualiza) en:
- **Global:** `~/.claude/plugins/config/claude-for-legal/company-profile.md`
- **Local:** `.claude-legal/company-profile.md`

## Flags

- `--local` — escribe la configuración en `.claude-legal/regulatorio-legal-mexico/CLAUDE.md` en lugar de la ruta global.
- `--redo` — re-ejecuta la entrevista completa y sobreescribe la configuración existente.
- `--module [nombre]` — ejecuta solo la sección de un módulo específico: `dof`, `cofece`, `cnbv`, `cofepris`, `ift`, `cre`, `conamer`.
- `--check-integrations` — verifica el estado de las integraciones configuradas sin re-ejecutar la entrevista.

## Flujo de entrevista

### Paso 0: verificar estado

Antes de hacer preguntas, verificar si ya existe configuración:

- Si existe configuración sin `[PLACEHOLDER]` y el flag no es `--redo`: "Tu configuración de regulatorio-legal-mexico ya existe. Para actualizar un módulo específico usa `--module [nombre]`. Para re-hacer la entrevista completa usa `--redo`. Para verificar integraciones usa `--check-integrations`."
- Si existe configuración con `[PLACEHOLDER]`: continuar la entrevista desde donde se interrumpió.
- Si no existe configuración o se usa `--redo`: iniciar la entrevista completa.

### Paso 1: perfil de la empresa (saltar si company-profile.md ya existe)

Preguntas (todas opcionales — el usuario puede responder "omitir" o dejar en blanco):

1. "¿Cuál es el nombre legal de tu empresa o despacho?"
2. "¿En qué industria o sector opera principalmente?" *(Detectar reguladores relevantes a partir de la respuesta: farmacéutico → COFEPRIS, financiero → CNBV, telecomunicaciones → IFT, energía → CRE, cualquier sector → COFECE y CONAMER.)*
3. "¿Es una empresa privada, pública (BMV/BIVA) o subsidiaria de una empresa pública?"
4. "¿Cuál es tu rol? Abogado titulado, contador, ejecutivo de cumplimiento, u otro."

### Paso 2: módulos regulatorios

Preguntar cuáles reguladores son relevantes para el cliente:

"¿Con cuáles de los siguientes reguladores tiene interacción tu empresa o tus clientes? (marca todos los que apliquen)"

- DOF — monitoreo de cambios regulatorios publicados
- COFECE — competencia económica (concentraciones, prácticas monopólicas, licitaciones)
- CNBV — regulación financiera (banca, valores, fintech)
- COFEPRIS — regulación sanitaria (medicamentos, alimentos, dispositivos médicos)
- IFT — telecomunicaciones y radiodifusión (concesiones, tarifas)
- CRE — energía (electricidad, hidrocarburos)
- CONAMER — mejora regulatoria (consultas públicas, MIR)

Activar solo los módulos seleccionados.

### Paso 3: configuración del módulo DOF (si seleccionado)

1. "¿Qué sectores o reguladores quieres monitorear en el DOF? (ej: farmacéutico, financiero, energía, telecomunicaciones)"
2. "¿Con qué frecuencia quieres el digest del DOF? (diaria / semanal / ad-hoc)"
3. "¿Tienes palabras clave específicas para alertas? (nombres de reguladores, NOM, siglas de programas)"
4. "¿A quién enviar el digest? (correos o canal Slack — o 'solo archivo local')"

### Paso 4: configuración por módulo (hacer para cada módulo seleccionado)

Para cada módulo activo, hacer 2-3 preguntas de configuración esencial. No hacer la entrevista completa del módulo aquí — obtener lo mínimo para que el skill funcione. El usuario puede profundizar con `--module [nombre]`.

**COFECE:** "¿Tu empresa realiza operaciones de M&A que podrían superar los umbrales de notificación del Art. 86 LFCE? ¿Tiene procedimientos activos ante COFECE?"

**CNBV:** "¿Qué tipo de entidad financiera es? (banco, casa de bolsa, SOFOM, SOFIPO, fintech, IFPE, otro). ¿Tiene un Oficial de Cumplimiento (CLCO) designado?"

**COFEPRIS:** "¿Qué tipo de productos regula COFEPRIS para tu empresa? ¿Tiene Responsable Sanitario designado?"

**IFT:** "¿Qué tipo de concesión tiene tu empresa? ¿Hay obligaciones de cobertura o reportes pendientes?"

**CRE:** "¿Qué tipo de permiso CRE tiene? ¿Hay obligaciones de reporte hacia CENACE o CENAGAS?"

**CONAMER:** "¿Tu empresa participa activamente en consultas públicas CONAMER? ¿Está suscrita al sistema SIMIR?"

### Paso 5: documentos semilla

"¿Tienes documentos de referencia que quieras cargar para calibrar los resultados? Por ejemplo:"
- Política de cumplimiento regulatorio vigente
- Requerimientos o resoluciones recientes de reguladores
- Títulos de concesión, registros sanitarios, autorizaciones

"Si los tienes, pégalos o señala la ruta. Si no, puedes agregar documentos después con `/regulatorio-legal-mexico:customize`."

Si el usuario carga documentos, leerlos y extraer:
- Reguladores mencionados y tipos de interacción
- Plazos y obligaciones de reporte
- Postura de cumplimiento implícita

### Paso 6: integraciones

Verificar si hay MCPs disponibles en el entorno:
- DOF monitoring: verificar si hay un MCP de DOF conectado
- Almacenamiento: verificar si Google Drive, SharePoint o Box están disponibles
- Slack: verificar si hay un MCP de Slack conectado
- Email: verificar si hay un MCP de correo conectado

Registrar estado (`✓ / ✗`) en la sección `## Integraciones disponibles` del CLAUDE.md.

Si no hay MCP de DOF: "El monitoreo del DOF funciona desde PDFs descargados manualmente. Deposita los archivos en `~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/dof/` y el skill dof-digest los procesará."

### Paso 7: escribir configuración

Con las respuestas recopiladas:

1. Si `company-profile.md` no existe, escribirlo en la ruta activa con los datos del Paso 1.
2. Leer la plantilla de `CLAUDE.md` de este plugin.
3. Reemplazar todos los `[PLACEHOLDER]` con los valores de la entrevista.
4. Omitir completamente los módulos no seleccionados (no dejar secciones vacías).
5. Escribir el archivo en la ruta activa (global o local según el flag).

### Paso 8: crear archivos de soporte

Crear el directorio de trabajo si no existe:
- `~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/` (global)
- O `.claude-legal/regulatorio-legal-mexico/` (local)

Crear un archivo de seguimiento vacío:
- `verification-log.md` — para el registro de verificaciones

Crear carpeta para archivos DOF si el módulo está activo:
- `dof/` — para PDFs del DOF descargados manualmente

### Paso 9: resumen y próximos pasos

Mostrar un resumen de la configuración escrita y las opciones disponibles:

```
✓ Configuración guardada en [ruta]

Módulos activos: [lista]
Integraciones: [lista con estado]

Skills disponibles:
  /regulatorio-legal-mexico:dof-digest — extrae cambios regulatorios del DOF relevantes para tu sector
  /regulatorio-legal-mexico:cofece-triage — triaja asuntos de competencia económica
  /regulatorio-legal-mexico:cofepris-tramite — gestiona trámites ante COFEPRIS
  /regulatorio-legal-mexico:respuesta-regulador — redacta respuestas a requerimientos de reguladores
  /regulatorio-legal-mexico:comentarios-regulatorios — prepara comentarios a consultas públicas

Para personalizar: /regulatorio-legal-mexico:customize
Para agregar un módulo: /regulatorio-legal-mexico:cold-start-interview --module [nombre]
```

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
