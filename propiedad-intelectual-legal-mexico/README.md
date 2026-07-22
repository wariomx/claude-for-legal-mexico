# propiedad-intelectual-legal-mexico

Plugin de Claude Code para trabajo de **propiedad intelectual bajo derecho
mexicano**, con cobertura de propiedad industrial ante IMPI y derecho de autor
y reservas ante INDAUTOR. Está adaptado del plugin `ip-legal` de Anthropic y
añade controles específicos para una práctica mexicana con múltiples clientes.

> Es una herramienta de apoyo y triaje. No sustituye la revisión de una persona
> abogada ni un sistema oficial de docketing.

## Endurecimiento operativo

### Aislamiento por asunto

El perfil se resuelve siempre en este orden:

1. perfil local más cercano:
   `.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`;
2. perfil global, únicamente si no existe uno local:
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.

El controlador devuelve las rutas canónicas `PROFILE`, `CONFIG_ROOT` y
`DATA_ROOT`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" status
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" list
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" new acme-marca-2026
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" switch acme-marca-2026
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" close acme-marca-2026
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" none
```

Cuando hay un asunto activo, el hook `PreToolUse` bloquea lecturas, escrituras y
búsquedas hacia otro asunto, el archivo global y registros compartidos. También
bloquea shell general: solo admite el controlador exacto y el vigilante
canónico con `--resolve`, además del comprobador canónico de fuentes jurídicas.
Rechaza rutas con symlink, almacenes locales de otro proyecto y crea asuntos
con directorios `0700`/archivos `0600`. Los skills no enumeran `matters/`
directamente. El campo legado `Contexto entre asuntos` no desactiva la barrera.

El mismo hook cubre herramientas MCP. Durante un asunto activo bloquea
conectores de repositorio/mensajería sin filtro de asunto verificable (Drive,
Box, iManage, Slack, TopCounsel y Definely); usar documentos ya colocados en
`DATA_ROOT` o un adaptador que haga cumplir `matter_id`. Las acciones MCP de
escritura y las acciones no clasificadas como lectura permanecen bloqueadas
porque el paquete no ha verificado escritura.

`.claude-legal/` está ignorado por git porque puede contener información de
clientes. El hook reduce cruces accidentales dentro de Claude Code; no es un
sandbox del sistema operativo ni sustituye permisos, cifrado o controles DMS.

### Procedencia jurídica

Las proposiciones operativas ya no dependen solo de memoria del modelo:

- `references/legal-authorities.json`: fuente primaria oficial, fecha de
  consulta, vigencia/transición y estado de hash;
- `references/verified-rules.json`: proposición, cita puntual, fecha de última
  verificación, próxima revisión y requisito de revisión humana;
- `schemas/*.schema.json`: contratos de datos para autoridades, reglas,
  portafolio y reportes.

El registro fue revisado contra los textos oficiales consolidados disponibles
al 22 de julio de 2026: LFPPI con reforma del 3 de abril de 2026, LFDA con
reforma del 14 de mayo de 2026, LFT con reforma del 15 de enero de 2026 y
Código Penal Federal con reforma del 13 de marzo de 2026. También se delimitó
el alcance capitalino de la ley de profesiones usada para secreto profesional.
El nuevo Reglamento LFPPI del 28 de abril de 2026 permanece marcado como
transitorio: no se fija una fecha calendario hasta comprobar los días inhábiles
oficiales, y el procedimiento de infracción en línea requiere revisar su acuerdo
de implementación.

El conocimiento del modelo es únicamente una pista de investigación: no puede
sustentar una conclusión, plazo, escrito o acción. Una proposición operativa
debe resolver un `rule_id` vigente o una fuente primaria abierta en la
ejecución; si no, queda `[verify]` y se excluye de la conclusión. Los PDFs
consolidados remotos no están vendorizados, por lo que el registro declara hash
nulo y exige nueva consulta al vencer `next_review`.

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_legal_sources.py" \
  --strict --as-of 2026-07-22 --format markdown
```

Este chequeo valida la cadena local, referencias y fechas; no descarga ni
certifica que el contenido remoto siga idéntico.

Correcciones relevantes incluyen:

- patentabilidad y exclusiones: LFPPI arts. 45-52, no numeración de la ley
  abrogada;
- derechos de patente: art. 55;
- medidas provisionales: arts. 344 y siguientes; infracciones: art. 386;
- indemnización: arts. 396-410, incluido el indicador de valor legítimo y la
  posibilidad de vía directa bajo sus condiciones;
- aviso y contra-aviso ISP: LFDA art. 114 Octies;
- derechos morales: LFDA arts. 18-21, sin declarar automáticamente nulo todo el
  contrato;
- obra por encargo y laboral: LFDA arts. 83 y 84, como reglas distintas;
- invenciones laborales: LFT art. 163, sin categorías inventadas por uso de
  recursos;
- delitos de autor: CPF arts. 424-429 sin intercambiar sus tipos; las antiguas
  referencias federales a calumnia de los arts. 356-359 están derogadas y el
  art. 251 no regula calumnia;
- seis categorías actuales de reservas y sus vigencias bajo LFDA arts. 173 y
  189-191.

### Capacidades de conectores

`references/connector-capabilities.json` separa cinco estados:

- `verified`: todas las capacidades declaradas tienen prueba válida;
- `partially_verified`: solo algunas capacidades tienen prueba válida;
- `configured_unverified`: servidor declarado, pero no probado ahora;
- `unavailable`: servidor ausente o prueba fallida;
- `unsupported`: no existe conector incluido.

Comprobar deriva entre el registro y `conectores-legal-mexico/.mcp.json`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/check_connectors.py" --strict --format markdown
```

Una prueba runtime se entrega mediante un inventario saneado conforme a
`schemas/connector-runtime-inventory.schema.json`. El inventario contiene solo
nombres de servidores/herramientas y metadatos de la prueba; nunca consultas,
resultados, encabezados, tokens ni datos de cliente. Cada prueba liga una
capacidad a una herramienta observada, debe ser no sensible, registrar que hubo
resultado y tener menos de 15 minutos. El registro también fija el hash y los
endpoints del manifiesto revisado; `--strict` detecta cambios.

Los conectores revisados para este plugin son LegalDataHunter, Solve
Intelligence, Google Drive, Box, iManage y Slack. Anaqua, CPA Global, PatSnap,
Clarivate IPfolio, Alt Legal y FoundationIP **no están incluidos**. Marcanet,
MARCia, VIDOC y SIGA son herramientas de práctica, no MCPs. Ninguna capacidad de
escritura se presume a partir de una prueba de lectura.

### Vigilante de renovaciones

El portafolio v2 canónico es `DATA_ROOT/portfolio.json` (JSON válido, sin
dependencia de PyYAML) y guarda `deadline_events` documentados. Un
`portfolio.yaml` legado debe migrarse; el watcher no lo interpreta. Cada evento
requiere `rule_id`, fecha, fuente, fecha de captura, traza de cálculo,
verificación humana, `verified_by` y fecha de cotejo registral. El clasificador
no inventa fechas a partir del tipo de activo:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/renewal_watch.py" \
  --resolve --as-of 2026-07-22 --days 90 --format markdown
```

El reporte separa urgencia de confiabilidad:

- urgencia: `overdue`, `grace`, `due_today`, ventanas de 30/60/90/180 días;
- confiabilidad: `verified` o `review_required` con bloqueos explícitos;
- datos legados/incompletos: `unknown`, nunca “todo claro”.

El agente no se programa a sí mismo, no presenta ni paga trámites y no envía
Slack/correo. La cadencia debe vivir en cron, CI o un workflow externo y debe
proporcionar `as_of` con el calendario operativo de México. Un envío externo
requiere un worker separado, capacidad de escritura realmente probada,
confirmación del destino y revisión de confidencialidad.

## Instalación y configuración

```bash
claude plugin install ./propiedad-intelectual-legal-mexico
```

Después:

```text
/propiedad-intelectual-legal-mexico:cold-start-interview --local
```

Usar `--local` para despachos o proyectos por cliente. La entrevista configura
perfil, responsables, postura, portafolio e integraciones. Para repetir solo la
comprobación de conectores:

```text
/propiedad-intelectual-legal-mexico:cold-start-interview --check-integrations
```

## Skills

| Skill | Función |
|---|---|
| `carta-requerimiento` | Carta saliente o triaje de carta recibida |
| `clearance` | Disponibilidad y riesgo de signos distintivos |
| `cold-start-interview` | Perfil, alcance, portafolio e integraciones |
| `customize` | Cambios controlados al perfil |
| `fto-triage` | Primera pasada de libertad de operación |
| `invention-intake` | Admisión de invenciones, titularidad y ruta inicial |
| `matter-workspace` | Ciclo de vida aislado de asuntos |
| `notificacion-infraccion` | Avisos ISP/plataforma y rutas IMPI |
| `oss-review` | Cumplimiento de licencias de software libre |
| `portafolio` | Registro, conciliación y auditoría de activos/plazos |
| `reservas-derechos` | Reservas ante INDAUTOR |
| `revision-clausulas-pi` | Cláusulas de PI, autor y secretos industriales |
| `triaje-infraccion` | Hechos, defensas y rutas de enforcement |

## Pruebas

```bash
python3 -m unittest discover \
  -s propiedad-intelectual-legal-mexico/tests -v
```

Las pruebas cubren precedencia local/global, ciclo de vida de asuntos, bloqueo
entre clientes, búsquedas recursivas, integridad de fuentes/reglas, deriva de
conectores y clasificación de renovaciones.

## Marco institucional

| Institución | Materia principal | Ley base |
|---|---|---|
| IMPI | Patentes, modelos, diseños, marcas, avisos, secretos, DO/IG | LFPPI |
| INDAUTOR | Derecho de autor, derechos conexos y reservas | LFDA |

## Autoría

Softlaw S.A. de C.V.; adaptación mexicana basada en el plugin `ip-legal` de
Anthropic.
