# Plugin de Derecho Civil México

Práctica civil mexicana con el marco legal parametrizado por **entidad federativa**. El derecho civil en México son 32 códigos civiles estatales más el Código Civil Federal como supletorio: los plazos máximos, los umbrales de inscripción, los derechos de preferencia y las reglas de orden público cambian de un estado a otro y la numeración no coincide. Este plugin fija la entidad antes de citar un solo artículo, cita con tabla verificada donde la tiene, y marca `[VERIFICAR]` donde no.

**Cada salida es un borrador para revisión del abogado — citado, señalizado y con compuerta — no una conclusión jurídica.** El plugin lee el contrato, aplica tu playbook, encuentra las cláusulas que contradicen una regla irrenunciable, las omisiones que la ley suple con una regla que quizá no te conviene, y las posiciones negociables. Un abogado revisa, verifica y decide.

## Versión 1.0.0 — alcance

Esta versión trae el módulo de **Arrendamiento de inmuebles** con **Jalisco** como única entidad con tabla de artículos verificada (Código Civil del Estado de Jalisco, Título Sexto, arts. 1980-2146 y disposiciones conexas, verificado contra la compilación del Congreso del Estado el 2026-09-22). Para cualquier otra entidad, el checklist se conserva y las citas llevan `[VERIFICAR: <código> art. <n>]`.

Módulos planeados para versiones posteriores: contratos civiles (mutuo, comodato, donación, mandato, servicios, obra), compraventa y promesa de inmuebles, garantías civiles, plazos y prescripción, responsabilidad civil, sucesiones y convenios familiares.

## Para quién es

| Perfil | Uso típico |
|---|---|
| **Despacho civilista** | Revisión de arrendamientos para clientes arrendadores y arrendatarios, con playbook de casa |
| **Notaría (apoyo jurídico)** | Revisión previa a protocolización o inscripción |
| **Jurídico interno con cartera inmobiliaria** | Locales, bodegas, oficinas y naves que la empresa toma o da en arrendamiento |
| **Administrador de inmuebles** | Contratos por cuenta de propietarios, control de vencimientos y preferencias |
| **Persona física con asesoría** | Revisar su propio contrato antes de firmar, con un abogado de referencia |

## Primera ejecución

```
/civil-legal-mexico:cold-start-interview
```

Entrevista de 8 a 12 minutos: perfil civil, entidades federativas (principal y adicionales, con estatus del CNPCF por entidad), lado habitual, playbook de arrendamiento, rol del usuario e integraciones. Escribe `~/.claude/plugins/config/claude-for-legal/civil-legal-mexico/CLAUDE.md`. Con `--local` escribe en `.claude-legal/civil-legal-mexico/CLAUDE.md` del proyecto actual, para aislar clientes.

Ningún skill sustantivo corre con el perfil en `[PLACEHOLDER]`: sin entidad fijada, una revisión civil cita el código equivocado con seguridad.

## Comandos

| Comando | Qué hace |
|---|---|
| `/civil-legal-mexico:cold-start-interview` | Configuración inicial; `--local`, `--redo`, `--check-integrations`, `--module arrendamiento` |
| `/civil-legal-mexico:revision-arrendamiento` | Revisión cláusula a cláusula de un arrendamiento de inmueble bajo el código civil de la entidad del inmueble — 14 temas, reglas irrenunciables, posiciones por lado, calendario derivado |
| `/civil-legal-mexico:customize` | Ajusta un campo del perfil (entidad, lado, playbook, rol) sin re-entrevista |
| `/civil-legal-mexico:matter-workspace` | Espacios de trabajo por asunto para práctica multicliente — `new`, `list`, `switch`, `close`, `none` |

## Habilidades

| Habilidad | Módulo | Propósito |
|---|---|---|
| **cold-start-interview** | Todos | Entrevista modular; escribe `## Entidades federativas` y el playbook de arrendamiento |
| **revision-arrendamiento** | Arrendamiento | Clasifica destino, lado, entidad y tipo de opción de compra; recorre 14 temas (legitimación, objeto, plazo, renta, fiscal, garantías, conservación y mejoras, subarriendo y traspaso, preferencia y tanto, enajenación e inscripción, terminación y pena, uso lícito, jurisdicción, datos personales); filtra contra la tabla de reglas irrenunciables; emite señales 🔴🟠🟡🟢, tabla resumen y calendario. Referencia verificada: `skills/revision-arrendamiento/references/ccj-jalisco-arrendamiento.md` |
| **customize** | Todos | Edición puntual del perfil |
| **matter-workspace** | Todos | Aislamiento por cliente o asunto; el `matter.md` puede fijar una entidad distinta a la principal |

## Cómo cita

- Entidad con referencia verificada en el plugin (Jalisco, arrendamiento): `[settled — last confirmed AAAA-MM-DD]`. Si la fecha tiene más de seis meses, el skill degrada a `[model knowledge — verify]`.
- Cualquier otra entidad: `[VERIFICAR: <código> art. <n>]`, siempre. Nunca se traslada la numeración del Código Civil Federal ni de otra entidad.
- Materia procesal: `[VERIFICAR: estatus CNPCF en <entidad>]` — la incorporación del Código Nacional de Procedimientos Civiles y Familiares es por declaratoria estatal.
- Jurisprudencia: Época, Registro Digital, Instancia, Materia, Tesis, con holding y enlace, o `[model knowledge — verify]`.

## Integraciones

**Conecta primero una herramienta de investigación.** Para códigos civiles estatales, el conector que los cubre es **LegalDataHunter** (fuente OrdenJuridicoEstatal, además de SCJN y DOF). Sin él, las entidades sin referencia local se citan de conocimiento del modelo con `[VERIFICAR]` y la nota del revisor lo registra. Los skills funcionan igual; el conector traslada la verificación fuera de tu carga.

Los conectores compartidos viven en `conectores-legal-mexico`, que se instala automáticamente como dependencia:

```bash
claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
```

- **LegalDataHunter** — legislación estatal y federal, jurisprudencia, DOF. API key en el keychain del sistema.
- **CJJ** — Poder Judicial de Jalisco: boletín y Portal Ciudadano, para asuntos que ya están en juicio (`/conectores-legal-mexico:setup-cjj`).
- **Google Drive / Box / iManage** — lectura de contratos y anexos.
- **Slack** — alertas, si se activan agentes en versiones posteriores.
- **Registro Público de la Propiedad** — sin MCP; el usuario pega el certificado de gravámenes y el skill lo lee como documento.

## Ruteo a otros plugins

| Situación | Destino |
|---|---|
| Rentas vencidas o negativa a desocupar: hay que demandar | `/litigacion-legal-mexico:plantillas-demanda arrendamiento-renta` |
| CFDI, IVA, retenciones de arrendamiento | `/fiscal-legal-mexico:cfdi-review` |
| Fianza de institución afianzadora o póliza jurídica | `/seguros-legal-mexico:poliza-review` |
| Aviso de privacidad para datos del arrendatario y fiador | `/privacidad-legal-mexico:aviso-privacidad` |
| Cláusulas universales (moneda extranjera, confidencialidad, fuerza mayor) y arrendamiento financiero | `/corporativo-legal-mexico:revision-contratos` mientras no exista el plugin comercial |

## Cómo aprende

El perfil de práctica no es estático. Cada revisión termina con un árbol de decisión y, si lo pides, registra el vencimiento, la ventana de preferencia y el incremento en `arrendamientos/registro.yaml`. Cuando una salida usa un valor por defecto que deberías fijar, el skill te lo dice; lo ajustas con `/civil-legal-mexico:customize`.

## Licencia

AGPLv3+. Ver `LICENSE` y `LICENSE-EXCEPTIONS.md` para la licencia comercial de Softlaw S.A. de C.V.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
