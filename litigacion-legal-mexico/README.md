# Plugin de Litigacion Mexico

Soporte para abogados litigantes que gestionan un portafolio de asuntos. El arranque en frio captura tu calibracion de riesgo, panorama de controversias y estilo de casa — el marco contra el que cada asunto se clasifica. El intake uniforme convierte asuntos nuevos en entradas estructuradas del libro y archivos por asunto. Los rollups de portafolio y los briefings a profundidad leen del libro.

Construido para abogados que llevan muchos asuntos a la vez, la mayoria de los cuales los manejan despachos externos. Este plugin es un companero de razonamiento, no un sistema de gestion de asuntos. Si tienes un sistema de control de expedientes o gestion de asuntos, este no lo reemplaza — se sienta al lado, como tu capa de razonamiento estructurado.

**Cada salida es un borrador para revision del abogado — citado, senalizado y con compuerta — no una conclusion juridica.** El plugin hace el trabajo: lee los documentos, aplica tu guia de trabajo, encuentra los problemas, redacta el memorandum. Un abogado revisa, verifica y decide. Las citas estan etiquetadas por fuente para que sepas cuales vinieron de una herramienta de investigacion y cuales necesitan verificacion. Las marcas de secreto profesional se aplican de manera conservadora para que nada se pierda por accidente. Las acciones con consecuencias — presentar, enviar, firmar — estan controladas por confirmacion explicita.

## Prerrequisitos

Varias funciones hacen referencia a integraciones con Gmail y tareas programadas. Estas requieren servidores MCP configurados en tu entorno — no vienen incluidos:

- **Gmail MCP** — `/litigacion-legal-mexico:oc-status` crea borradores de Gmail si esta autenticado; de lo contrario recurre a borradores en markdown en `oc-status/[AAAA-MM-DD]/[slug].md`.
- **Tareas programadas MCP** — no se incluye programacion automatica. Configura un recordatorio recurrente en calendario para invocar los comandos semanales.

El contexto de investigacion juridica mexicana es esencial para aprovechar al maximo el plugin. Conecta herramientas de investigacion cuando esten disponibles:

- **SCJN IUS / Semanario Judicial de la Federacion** — busqueda de jurisprudencia y tesis aisladas, verificacion de vigencia de criterios
- **Portal PJF (Poder Judicial de la Federacion)** — consulta de expedientes electronicos, actuaciones judiciales, acuerdos y autos
- **DOF (Diario Oficial de la Federacion)** — monitoreo de reformas legislativas y acuerdos generales del CJF
- **IMPI** — consulta de expedientes de propiedad intelectual relacionados con litigios de PI

El plugin funciona de extremo a extremo sin ninguna integracion; estas son aditivas.

## Para quien es

| Rol | Uso principal |
|---|---|
| **Juridico interno (litigante)** | Todo — intake, clasificacion, estatus, historial, briefings |
| **Subdirector Juridico / Director Juridico adjunto** | Supervision del portafolio, rollups para reporte al Consejo |
| **Director Juridico** | Estatus rapido del portafolio, analisis a profundidad de cualquier asunto |
| **Abogado de despacho** | Gestion de cartera de asuntos, preparacion de escritos, control de plazos |
| **Practica independiente** | Carga de asuntos, contingencia o iguala, actualizacion al cliente |

## Primera ejecucion: arranque en frio

La entrevista de arranque en frio escribe el perfil de practica a nivel de *casa* — persistente entre todos los asuntos. Tres pilares:

- **Calibracion de riesgo** — apetito, umbrales de materialidad, disparadores de reserva/revelacion, autoridad de transaccion, perfil de seguros, matriz de severidad-probabilidad
- **Panorama** — empresa, jurisdicciones, estatus regulado, patrones de controversia, adversarios frecuentes, mesa de despachos externos, partes interesadas internas
- **Estilo de casa** — formato de memorandum al Consejo/Comite de Auditoria, formato de memorandum de reservas, estilo de directiva a despacho externo, convenciones de confidencialidad, normas de escalamiento

Ofrece valores por defecto razonables en cada paso (ej., una matriz 3x3 de severidad-probabilidad) y mantiene todo editable en formato libre. Si aun no tienes un marco escrito, esto es lo que fuerza la articulacion.

```
/litigacion-legal-mexico:cold-start-interview
```

Tu configuracion se almacena en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` y sobrevive las actualizaciones del plugin.

## Comandos

| Comando | Que hace |
|---|---|
| `/litigacion-legal-mexico:cold-start-interview` | Arranque en frio → escribe el perfil de practica en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` |
| `/litigacion-legal-mexico:matter-intake` | Intake uniforme → escribe `matters/[slug]/` + agrega a `_log.yaml` |
| `/litigacion-legal-mexico:portfolio-status` | Rollup del portafolio — distribucion de riesgo, plazos proximos, asuntos estancados |
| `/litigacion-legal-mexico:matter-briefing [slug]` | Briefing a profundidad de un asunto — listo para leer antes de una llamada con el DJ o con despacho externo |
| `/litigacion-legal-mexico:matter-update [slug]` | Agrega un evento fechado al historial de un asunto; refresca el `last_updated` del libro |
| `/litigacion-legal-mexico:matter-close [slug]` | Archiva un asunto fuera del portafolio activo (retenido, no eliminado) |
| `/litigacion-legal-mexico:matter-workspace` | Administrar espacios de trabajo por asunto (solo practica privada multicliente) — nuevo, listar, cambiar, cerrar, ninguno |
| `/litigacion-legal-mexico:demand-intake [titulo]` | Recopilacion de contexto pre-redaccion para una carta de requerimiento (pago / incumplimiento / cesacion / rescision laboral / preservacion) |
| `/litigacion-legal-mexico:demand-draft [slug]` | Redacta la carta desde el intake — aplica validacion de tratativas pre-litigiosas / confidencialidad, salida en `.docx`, escribe checklist post-envio |
| `/litigacion-legal-mexico:demand-received [ruta]` | Clasifica una carta de requerimiento recibida — analisis de opciones, cruce con portafolio, transferencia a matter/demand-intake |
| `/litigacion-legal-mexico:requerimiento-triage [ruta]` | Clasifica un requerimiento de tercero — clasificar, alcance/carga/confidencialidad, marco de objeciones, plan de cumplimiento |
| `/litigacion-legal-mexico:legal-hold [slug] [--issue/--refresh/--release/--status]` | Emitir, refrescar, liberar o reportar retenciones documentales — escribe `.docx` + actualiza libro |
| `/litigacion-legal-mexico:chronology [slug]` | Construye o actualiza una cronologia a partir de fuentes documentales declaradas + cargas — etiquetada por relevancia segun la teoria del asunto |
| `/litigacion-legal-mexico:oc-status` | Redacta correos semanales de solicitud de estatus a despachos externos en todo el portafolio; borradores en markdown + borradores de Gmail si MCP disponible |
| `/litigacion-legal-mexico:claim-chart` | Construye o revisa un cuadro de elementos — cuadro de reclamacion de patente (infraccion / invalidez / revision) o cuadro de elementos civiles/mercantiles (cualquier causa de accion o defensa) con deteccion de vacios |
| `/litigacion-legal-mexico:preparacion-pruebas [slug]` | Preparacion de ofrecimiento y desahogo de pruebas — estructura el acervo probatorio, identifica vacios, prepara guion de interrogatorios y cuestionarios |
| `/litigacion-legal-mexico:revision-confidencialidad [slug]` | Revision de documentos para clasificacion de confidencialidad — aplica criterios de secreto profesional, identifica documentos sensibles, genera registro de clasificacion |
| `/litigacion-legal-mexico:redaccion-escritos [slug]` | Redaccion de secciones de escritos procesales — demanda, contestacion, alegatos, agravios de apelacion, conceptos de violacion de amparo |
| `/litigacion-legal-mexico:boletin-monitor "NOMBRE" [--fecha YYYY-MM-DD]` | Monitorea el boletin diario del CJJ (Jalisco) por nombre de parte en juzgados mercantiles de la ZMG — deteccion de demandas, seguimiento de expedientes, vigilancia de contrapartes |
| `/litigacion-legal-mexico:revision-expedientes-jalisco [expediente]` | Acceso autenticado a expedientes del Poder Judicial de Jalisco via Portal Ciudadano CJJ — actuaciones, acuerdos, autos, notificaciones |
| `/litigacion-legal-mexico:plantillas-demanda [tipo]` | Genera escrito inicial desde plantilla para juicio ordinario mercantil, ejecutivo mercantil, oral mercantil, civil ordinario, hipotecario, requerimiento de pago o arrendamiento por falta de pago |

## Habilidades

| Habilidad | Proposito |
|---|---|
| **cold-start-interview** | Perfil de practica — calibracion de riesgo, panorama, estilo de casa |
| **customize** | Editar secciones especificas del perfil de practica sin re-ejecutar la entrevista completa |
| **matter-intake** | Preguntas de intake uniformes; escribe archivo de asunto + fila en el libro |
| **matter-briefing** | Lectura a profundidad de un asunto desde su archivo + historial |
| **matter-update** | Agrega evento estructurado; actualiza `last_updated` en el libro |
| **matter-close** | Semantica de archivo; captura resultado |
| **matter-workspace** | Crear, listar, cambiar y cerrar espacios de trabajo por asunto para practicas multicliente; aisla cada cliente/asunto para que el contexto no se filtre entre ellos |
| **portfolio-status** | Rollup del libro — riesgo, plazos, estancamiento |
| **oc-status** | Redactor semanal de correos de solicitud de estatus a despachos externos en todo el portafolio; markdown + borradores de Gmail |
| **demand-intake** | Recopilacion adaptativa de contexto para carta de requerimiento — partes, hechos, apalancamiento, filtros de confidencialidad |
| **demand-draft** | Validacion de tratativas pre-litigiosas / confidencialidad, luego redacta `.docx` con marcadores `[CITE:___]`; escribe checklist post-envio; ofrece creacion de asunto |
| **demand-received** | Clasificacion de requerimiento recibido — merito, opciones, cruce con portafolio |
| **requerimiento-triage** | Clasificar requerimiento de tercero, analizar alcance/carga/confidencialidad, producir marco de objeciones + plan de cumplimiento |
| **legal-hold** | Emitir / refrescar / liberar / reportar retenciones documentales; escribe aviso en `.docx`; actualiza campos `legal_hold` del libro |
| **chronology** | Extraer eventos fechados de fuentes documentales declaradas + cargas; desduplicar; etiquetar relevancia segun teoria del asunto |
| **claim-chart** | Cuadro de reclamacion de patente (infraccion / invalidez / revision) o cuadro de elementos civiles/mercantiles (cualquier causa de accion o defensa). Mapeo elemento por elemento, cada celda con cita puntual, deteccion de vacios. Incluye biblioteca de plantillas de causas de accion. |
| **preparacion-pruebas** | Estructura el acervo probatorio del asunto, identifica vacios, prepara guiones de interrogatorios y cuestionarios para desahogo de pruebas |
| **revision-confidencialidad** | Revision de documentos para clasificacion de secreto profesional, identificacion de documentos sensibles, generacion de registro de clasificacion |
| **redaccion-escritos** | Redaccion de secciones de escritos procesales — demanda, contestacion, alegatos, agravios de apelacion, conceptos de violacion de amparo, con marcadores de cita y validacion de fundamento legal |
| **boletin-monitor** | Monitoreo del boletin judicial del CJJ (Jalisco) — busqueda por nombre de parte en los 18 juzgados mercantiles de la ZMG via API publica sin autenticacion |
| **revision-expedientes-jalisco** | Acceso autenticado a expedientes del Poder Judicial de Jalisco via la API del Portal Ciudadano CJJ (nilo.cjj.gob.mx) — actuaciones completas, catalogos judiciales, seguimiento detallado |
| **plantillas-demanda** | Genera escritos desde plantilla para 7 tipos de accion — juicio ordinario mercantil, ejecutivo mercantil, oral mercantil, civil ordinario, hipotecario, requerimiento de pago, arrendamiento por falta de pago |

## Comandos interactivos vs. agentes programados

Los comandos anteriores se ejecutan cuando los invocas — para cuando estas trabajando un asunto. Los agentes siguientes se ejecutan por calendario — para lo que se mueve mientras no estas mirando:

| Agente | Que vigila | Cadencia predeterminada |
|---|---|---|
| **vigilante-expedientes** | Expedientes judiciales de asuntos en el portafolio activo — obtiene nuevas actuaciones de tribunales federales (PJF) y estatales (CJJ Jalisco), calcula plazos procesales candidatos, cruza contra el historial y entregables de cada asunto | Semanal |
| **verificador-juridico** | QA legal bajo demanda — cruza plazos procesales, citas de articulos y fundamentos legales contra fuentes primarias (Codigo de Comercio, CFPC, CNPCF, Ley de Amparo, LFT, LFPPI, LFDA, LGSM); senala discrepancias | Bajo demanda |

## Como se organizan los datos

```
litigacion-legal-mexico/
├── CLAUDE.md                          # Perfil de practica a nivel de CASA — riesgo, panorama, estilo
├── matters/
│   ├── _log.yaml                      # el libro del portafolio (una entrada por asunto)
│   └── [asunto-slug]/
│       ├── matter.md                  # intake del asunto + teoria + postura procesal
│       ├── history.md                 # bitacora de eventos (solo agregar)
│       ├── chronology.md              # cronologia para el litigio (bajo demanda)
│       └── legal-hold-v[N].docx       # avisos de retencion documental (emision, refrescamiento, liberacion)
├── demand-letters/                    # requerimientos salientes
│   └── [slug]/
│       ├── intake.md
│       ├── draft-v1.docx
│       └── checklist.md
├── inbound/                           # requerimientos entrantes, cartas de contraparte, oficios de autoridad
│   └── [slug]/
│       ├── incoming.[ext]
│       ├── triage.md
│       └── response-v1.docx           # si respondemos
└── oc-status/                         # borradores semanales de solicitud de estatus a despachos externos
    └── [AAAA-MM-DD]/
        ├── _summary.md
        └── [slug].md                  # un correo por asunto
```

Carpetas separadas porque cada flujo de trabajo es distinto. Los asuntos se rastrean en el portafolio; las cartas de requerimiento y los documentos entrantes pueden o no llegar a ser un asunto; los borradores de estatus a despachos externos son artefactos periodicos. Cuando las cosas se relacionan, el campo `related_matters` y los enlaces cruzados en `matter.md` los conectan.

El libro esta en YAML porque es parseable por los skills de rollup. Los archivos por asunto estan en markdown porque ahi es donde lees y editas. Ambos se guardan en la carpeta como texto plano — nada propietario.

## Conectores y verificacion de citas

**Conecta primero una herramienta de investigacion — las salvaguardas de citacion dependen de ella.** Sin una, cada cita se etiqueta como `[verify]` y la nota del revisor sobre cada entregable registra que las fuentes no fueron verificadas. El plugin funciona de cualquier manera; simplemente hace mas de la verificacion por ti cuando una herramienta de investigacion esta conectada.

Los conectores de investigacion juridica en este plugin no son solo fuentes de datos — son la diferencia entre una cita verificada y una cita que tienes que revisar. Una cita obtenida a traves de **SCJN IUS** (jurisprudencia y tesis aisladas de la Suprema Corte de Justicia de la Nacion, verificacion de vigencia de criterios), **Semanario Judicial de la Federacion** (publicacion oficial de criterios judiciales, busqueda por epoca, instancia y materia), **Portal PJF** (expedientes electronicos, actuaciones judiciales, consulta de acuerdos y autos en juzgados de distrito, tribunales colegiados y SCJN), o **DOF** (reformas legislativas, acuerdos generales del CJF, decretos) se etiqueta con su fuente y puede rastrearse. Una cita del conocimiento del modelo o de busqueda web se etiqueta `[verify]` o `[verify-pinpoint]` y debe verificarse contra una fuente primaria antes de que alguien confie en ella. El plugin clasifica sus citas por nivel para que tu tiempo de verificacion se concentre donde importa.

## Integraciones

Los conectores compartidos (LegalDataHunter, Slack, Google Drive, Box, iManage, TopCounsel, Definely) viven en el plugin `conectores-legal-mexico`, que se instala automaticamente como dependencia. Para configurar la API key de LegalDataHunter:

```bash
claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
```

- **LegalDataHunter** — busqueda agregada de documentos juridicos mexicanos (16M+ documentos de SCJN, DOF, SAT, IMPI y mas). API key gestionada via `claude plugin configure` — almacenada en el keychain del sistema, no en variables de entorno.
- **Slack** — buscar mensajes, leer canales, encontrar conversaciones
- **Google Drive** — buscar, leer y obtener documentos
- **Box** — gestion documental y almacenamiento de expedientes
- **iManage** — contenido gobernado conectado a Claude
- **TopCounsel** — recomendaciones de abogados externos
- **Definely** — estructura contractual, definiciones, referencias cruzadas

### Poder Judicial de Jalisco (CJJ)

Los skills `boletin-monitor` y `revision-expedientes-jalisco` acceden a las APIs del Consejo de la Judicatura de Jalisco:

| API | URL | Auth | Uso |
|---|---|---|---|
| Boletin publico | `api.cjj.gob.mx/bulletin/zmg_date` | Ninguna | Extracto diario del boletin judicial — busqueda por parte |
| Portal Ciudadano (Nilo) | `nilo.cjj.gob.mx/api/v1` | JWT via credenciales | Expediente completo — actuaciones, acuerdos, catalogos |

**El `vigilante-expedientes` agent detecta automaticamente asuntos con jurisdiccion Jalisco en `_log.yaml` y consulta estas APIs en adicion a las fuentes federales (PJF/SCJN).**

Disenado para ser util sin nada conectado. Si/cuando quieras obtener documentos de plataformas de produccion documental, CLMs o correo, se pueden agregar skills de integracion sin cambiar la arquitectura central.

## Configuracion para produccion

### Variables de entorno

Copiar `.env.example` a `.env` en la raiz del repositorio y configurar:

```bash
cp .env.example .env
# Editar .env con tus valores reales
```

| Variable | Requerida | Descripcion |
|---|---|---|
| `CJJ_NILO_EMAIL` | Para Jalisco | Correo del Portal Ciudadano CJJ |
| `CJJ_NILO_PASSWORD` | Para Jalisco | Contrasena del Portal Ciudadano CJJ |
| `CJJ_NILO_PUBLIC_TOKEN` | Para Jalisco | Token publico del API Nilo (proporcionado al registrarse en el portal) |

La API key de LegalDataHunter se configura por separado via keychain (ver seccion Integraciones arriba) — no va en `.env`.

**Nunca commitear `.env` al repositorio.** El `.gitignore` ya excluye `.env`, `.env.local` y `.env.production`.

### Registro en el Portal Ciudadano CJJ

Para usar `revision-expedientes-jalisco` con acceso autenticado:

1. Registrarse en [ciudadano.cjj.gob.mx](https://ciudadano.cjj.gob.mx)
2. Configurar `CJJ_NILO_EMAIL` y `CJJ_NILO_PASSWORD` en `.env`
3. El skill obtiene un JWT automaticamente al ejecutarse

El skill `boletin-monitor` NO requiere registro — usa la API publica del boletin.

## Como aprende

Tu perfil de practica en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` no es estatico — mejora conforme usas el plugin. Los skills te avisan cuando una salida utilizo un valor predeterminado que deberias ajustar. Puedes volver a ejecutar la configuracion, editar el archivo directamente, o decirle a un skill que registre una nueva posicion.

## Notas

- Cada skill lee de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` primero. Si tu apetito de riesgo cambia o contratas un nuevo despacho externo, actualiza el perfil — no lo parches en asuntos individuales.
- `## Perfil de la empresa` es la primera seccion de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` por convencion. Si usas otros plugins `-legal-mexico`, puedes copiarlo entre ellos en lugar de re-capturar el mismo contexto.
- `_log.yaml` es la fuente de verdad para el estado del portafolio. Mantenlo limpio.
- El historial de asuntos es solo-agregar. Si algo estaba equivocado, anota la correccion como una nueva entrada — no edites el pasado.
- Los asuntos cerrados se quedan en `_log.yaml` (historial consultable). `/litigacion-legal-mexico:portfolio-status` los filtra de los rollups activos por defecto.

## Convenciones de marcadores en linea

Tres marcadores aparecen en las salidas y borradores de los skills. No son disclaimers — son elementos de accion:

- `[CITE: cita especifica necesaria]` — un marcador de autoridad juridica. El abogado llena o confirma antes de enviar.
- `[VERIFY: hecho especifico]` — una afirmacion de hecho aun no confirmada contra fuente. El abogado verifica antes de confiar.
- `[SME VERIFY: decision de criterio especifica]` — un juicio (lectura de merito, etiqueta de relevancia, fuerza de objecion, estatus de confidencialidad) que requiere revision de experto en la materia. SME = abogado titulado habilitado en la jurisdiccion / area relevante. Se usa liberalmente — cualquier cosa pesada en criterio debe llevar este marcador.

Un borrador o clasificacion con marcadores sin resolver no es final, sin importar lo pulido que se lea.

## Pruebas y QA
