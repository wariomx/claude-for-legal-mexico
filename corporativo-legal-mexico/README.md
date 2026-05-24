# Plugin de Derecho Corporativo México

Flujos de trabajo de abogacía corporativa interna en cuatro áreas de práctica: Fusiones y Adquisiciones (F&A), Consejo de Administración y Secretaría Corporativa, Sociedad bursátil / Emisoras, y Administración de entidades. Activa solo los módulos que apliquen a tu rol. La entrevista de arranque en frío es modular — hace preguntas específicas por área activa y escribe únicamente las secciones relevantes en tu perfil de práctica.

**Cada salida es un borrador para revisión del abogado — citado, señalizado y con compuerta — no una conclusión jurídica.** El plugin hace el trabajo: lee los documentos, aplica tu guía de trabajo, encuentra los problemas, redacta el memorándum. Un abogado revisa, verifica y decide. Las citas están etiquetadas por fuente para que sepas cuáles vinieron de una herramienta de investigación y cuáles necesitan verificación. Las marcas de secreto profesional se aplican de manera conservadora para que nada se pierda por accidente. Las acciones con consecuencias — presentar, enviar, firmar — están controladas por confirmación explícita.

## Para quién es

| Rol | Módulos activos |
|---|---|
| **Abogado interno de F&A** | F&A |
| **Secretario / Secretario adjunto del Consejo** | Consejo y Secretaría |
| **Director Jurídico de emisora** | F&A + Sociedad Bursátil + Consejo y Secretaría |
| **Director Jurídico de empresa privada** | F&A + Consejo y Secretaría + Administración de Entidades |
| **Operaciones legales / Director Jurídico único** | Los que apliquen — combínalos a tu medida |

## Primera ejecución

```
/corporativo-legal-mexico:cold-start-interview
```

Guía la selección de módulos, luego una entrevista corta y dirigida por cada área activa. Escribe un `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` modular con solo las secciones relevantes. Tu configuración se almacena en esa ruta y sobrevive las actualizaciones del plugin.

Configuración por operación (solo módulo F&A):

```
/corporativo-legal-mexico:cold-start-interview --new-deal
```

## Comandos

| Comando | Qué hace |
|---|---|
| `/corporativo-legal-mexico:cold-start-interview` | Arranque en frío modular, o `--new-deal` / `--module [f&a \| consejo \| emisora \| entidades]` |
| `/corporativo-legal-mexico:diligence-issue-extraction [carpeta]` | Lee documentos del VDR, extrae problemas en formato interno |
| `/corporativo-legal-mexico:tabular-review` | Revisión tabular — una fila por documento, una columna por dato, cada celda citada a fuente, salida en Excel |
| `/corporativo-legal-mexico:material-contract-schedule` | Anexo de revelaciones de contratos relevantes a partir de hallazgos de debida diligencia |
| `/corporativo-legal-mexico:closing-checklist` | Lista de verificación de cierre — qué está pendiente, ruta crítica |
| `/corporativo-legal-mexico:written-consent` | Consentimiento unánime por escrito — borrador con precedentes + seguimiento de firmantes |
| `/corporativo-legal-mexico:entity-compliance` | Seguimiento de cumplimiento de entidades — inicializar, reportar, actualizar, auditar, exportar |
| `/corporativo-legal-mexico:integration-management` | Plan de trabajo de integración post-cierre, seguimiento de consentimientos, cesión de contratos, reportes de estatus |
| `/corporativo-legal-mexico:matter-workspace` | Administrar espacios de trabajo por asunto (solo práctica privada multicliente) — nuevo, listar, cambiar, cerrar, ninguno |

## Prerrequisitos

Varias funciones hacen referencia a integraciones con Slack, Google Drive, SharePoint, Box, Intralinks o Datasite. Estas requieren servidores MCP configurados en tu entorno — **no vienen incluidos con el plugin**. Sin ellos, el plugin recurre a salida en archivos (borradores escritos localmente en lugar de publicados en un canal, archivos de seguimiento escritos en disco en lugar de leídos de un repositorio conectado).

Configura los servidores MCP en `.mcp.json` a nivel de repositorio o de usuario. Las habilidades y agentes detectarán lo que está disponible en tiempo de ejecución y ajustarán su comportamiento.

## Habilidades

| Habilidad | Módulo | Propósito |
|---|---|---|
| **cold-start-interview** | Todos | Entrevista modular — activa solo las secciones relevantes |
| **diligence-issue-extraction** | F&A | Documentos del VDR → problemas en formato interno, por categoría |
| **tabular-review** | F&A | Revisa un conjunto de documentos contra un esquema de columnas tipado; celdas citadas; salida en `.xlsx` / `.csv` / markdown; alimenta material-contract-schedule |
| **deal-team-summary** | F&A | Informes escalonados: ejecutivo / líder de operación / equipo de trabajo |
| **material-contract-schedule** | F&A | Anexo de revelaciones según la definición del Contrato de Compraventa de Acciones |
| **closing-checklist** | F&A | Auto-actualizable: incorpora datos de debida diligencia y construcción de anexos |
| **ai-tool-handoff** | F&A | Integración con Luminance/Kira — extracción masiva + capa de control de calidad |
| **board-minutes** | Consejo y Secretaría | Reuniones detectadas por calendario → borrador de actas en formato interno |
| **written-consent** | Consejo y Secretaría | Consentimientos unánimes por escrito con búsqueda de precedentes en el repositorio de consentimientos; advertencia de alcance para acciones mayores extraordinarias |
| **entity-compliance** | Administración de Entidades | Seguimiento de calendario de cumplimiento (YAML); plazos de presentación por entidad y jurisdicción; auditoría de salud; ingestión de reportes de agentes registrados; exportación CSV |
| **integration-management** | F&A | Seguimiento de integración post-cierre; plan de trabajo por fases (Día 1/30/90/180); seguimiento de consentimientos requeridos con plazos del CCA; cesión de contratos a escala (repositorio o lista manual); reportes de estatus semanales |
| **matter-workspace** | Crear, listar, cambiar y cerrar espacios de trabajo por asunto para prácticas multicliente; aísla cada cliente/asunto para que el contexto no se filtre entre ellos |

*Las habilidades de Sociedad Bursátil vendrán en la próxima versión.*

## Comandos interactivos vs. agentes programados

Los comandos anteriores se ejecutan cuando los invocas — para cuando estás trabajando un asunto. Los agentes siguientes se ejecutan por calendario — para lo que se mueve mientras no estás mirando:

| Agente | Módulo | Qué vigila | Cadencia predeterminada |
|---|---|---|---|
| **dataroom-watcher** | F&A | VDR en busca de nuevas cargas de documentos; señala cargas que coincidan con categorías de alta prioridad; ejecuta estatus de la lista de verificación de cierre | Semanal |

## Integraciones

**Conecta primero una herramienta de investigación — las salvaguardas de citación dependen de ella.** Sin una, cada cita se etiqueta como `[verify]` y la nota de revisión sobre cada entregable registra que las fuentes no fueron verificadas. Las habilidades funcionan de cualquier manera; una herramienta de investigación (SCJN IUS, Semanario Judicial de la Federación) simplemente traslada el trabajo de verificación fuera de tu carga.

Los conectores compartidos (LegalDataHunter, Slack, Google Drive, Box, iManage, TopCounsel, Definely) viven en el plugin `conectores-legal-mexico`, que se instala automaticamente como dependencia. Para configurar la API key de LegalDataHunter:

```bash
claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
```

- **LegalDataHunter** — busqueda agregada de documentos juridicos mexicanos (16M+ documentos de SCJN, DOF, SAT, IMPI y mas). API key gestionada via `claude plugin configure` — almacenada en el keychain del sistema, no en variables de entorno.
- **Slack** — buscar mensajes, leer canales, encontrar conversaciones
- **Google Drive** — buscar, leer y obtener documentos
- **Box** — data room y gestion documental
- **iManage** — contenido gobernado conectado a Claude
- **TopCounsel** — recomendaciones de abogados externos
- **Definely** — estructura contractual, definiciones, referencias cruzadas

Los conectores de Intralinks y Datasite para VDR pueden añadirse a `conectores-legal-mexico` cuando las URLs de los proveedores esten disponibles.

## Cómo aprende

Tu perfil de práctica en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` no es estático — mejora conforme usas el plugin. Las habilidades te avisan cuando una salida utilizó un valor predeterminado que deberías ajustar. Puedes volver a ejecutar la configuración, editar el archivo directamente, o decirle a una habilidad que registre una nueva posición.

## Notas de F&A

- La extracción de problemas aplica umbrales de materialidad — no lee todos los documentos si el umbral indica los N principales por valor.
- Se soportan tanto lado comprador como lado vendedor. El Perfil de Práctica captura qué lado aplica a esta operación; las habilidades ajustan su postura en consecuencia.
- La transferencia a herramientas de IA (Luminance/Kira) es opcional. Si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` dice que no hay herramienta, toda la extracción se ejecuta a través de la habilidad directa.
- La lista de verificación de cierre se inicializa desde el Contrato de Compraventa de Acciones, luego se auto-actualiza conforme la debida diligencia revela consentimientos requeridos.
