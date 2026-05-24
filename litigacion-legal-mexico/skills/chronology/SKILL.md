---
name: chronology
description: >
  Construir o actualizar una cronología a partir de fuentes documentales declaradas — eventos
  fechados extraídos, deduplicados y etiquetados por relevancia conforme a la teoría del caso.
  Usar cuando el usuario pida construir una cronología o línea de tiempo del asunto, diga
  "cronología del expediente", "qué pasó cuándo", o necesite una línea de tiempo de trabajo,
  capítulo de hechos, o cronología específica por testigo.
argument-hint: "[slug] [--format=trabajo|hechos|testigo-[nombre]]"
---

# /chronology

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` → teoría del caso, hecho pivote, hechos clave.
2. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → Fuentes de almacenamiento documental, patrón de carpeta de asunto por defecto.
3. Seguir el flujo de trabajo y referencia abajo.
4. Identificar fuentes en orden: rutas proporcionadas por el usuario en esta sesión, carpeta de asunto por defecto, fuentes declaradas en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`.
5. Para fuentes legibles: extraer eventos fechados. Para fuentes no accesibles: anotar en Lagunas.
6. Deduplicar, fusionar con lista de fuentes por evento.
7. Etiquetar relevancia (🔴/🟡/⚪) conforme a la teoría del caso.
8. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/chronology.md` (o variante de formato según la bandera).
9. Si existe versión previa: el número de versión se incrementa, resumen de diferencias presentado al usuario.
10. Confirmar antes de finalizar: "Aquí está lo que construí. Revisa las entradas 🔴 — ¿algo que haya clasificado mal?"

---

# Cronología

## Restricciones de uso de documentos del procedimiento

Antes de trabajar con un conjunto de documentos de litigio, preguntar: "¿Alguno de estos documentos fue obtenido a través de etapas procesales (exhibición de pruebas, desahogo de pruebas, requerimientos judiciales)?" Si la respuesta es afirmativa:

- **México (CFPC / CNPCF / Código de Comercio):** Los documentos obtenidos en la etapa probatoria de un procedimiento judicial pueden tener restricciones de confidencialidad impuestas por el juzgador. Las medidas de apremio (Arts. 73-74 CNPCF) pueden aplicar ante el uso indebido de documentos. Cuando el juez ha decretado reserva o confidencialidad sobre ciertos documentos o actuaciones (por ejemplo, en materia de secretos industriales o datos personales), usar esos documentos fuera del procedimiento puede generar responsabilidad.
- **Otras jurisdicciones:** Restricciones similares aplican comúnmente. Verificar la regla local.

Confirmar: "Este uso está dentro del procedimiento en el que los documentos fueron obtenidos, o tengo autorización / consentimiento, o los documentos son ahora públicos." Si no se confirma, señalar: "Los documentos del procedimiento pueden tener restricciones de uso. Confirmar que este uso está permitido antes de continuar."

## Propósito

Los hechos ocurren en orden. La cronología es la columna vertebral de la que cuelga toda narrativa — el capítulo de hechos de un escrito, memorándums de reserva, memorándums de transacción, preparación de testigos, preparación de audiencia. Construir una cronología a mano es lento; la IA es buena para la extracción estructurada. El riesgo: basura entra, basura sale. Este skill extrae de las fuentes que la configuración declara y de lo que el usuario suba.

## Modos

Este skill atiende dos entornos de práctica. Elegir un modo por defecto del `## Rol de práctica` en el CLAUDE.md de configuración del plugin; el usuario puede anular por ejecución con una bandera.

- **`--matter` mode (por defecto para jurídico interno).** Enfocado en el historial del asunto. Lee la teoría del caso y hechos clave de `matter.md`, extrae de fuentes de almacenamiento documental declaradas (Google Drive, SharePoint, Gmail, iManage, CLM — lo que la sección `## Panorama` del CLAUDE.md declare), y trata `history.md` como el registro interno en curso (decisiones, retenciones, memorándums de reserva — intencionalmente no en la cronología). Resultado centrado en el asunto: qué pasó a lo largo de la controversia, etiquetado para uso en defensa o demanda.
- **`--documents` mode (por defecto para abogado de despacho / pasante).** Enfocado en producción documental. Lee la teoría del caso de la configuración, luego extrae de un conjunto documental, una exportación por custodio, o una producción con foliado interno. Resultado centrado en los documentos: qué muestran los documentos, con referencias a fojas o identificadores internos, etiquetado conforme a la teoría del caso.

Ambos modos convergen en la misma estructura de salida (línea de tiempo, etiquetas de relevancia 🔴/🟡/⚪, lagunas, variante de capítulo de hechos). La diferencia es el perfil de fuentes y el marco de relevancia.

Si `## Rol de práctica` es `práctica-independiente` u `otro`, usar `--matter` por defecto pero mencionar ambos modos en la primera ejecución y dejar que el usuario elija.

## Encuadre por lado (etiquetas de relevancia)

El mismo evento es relevante de maneras distintas dependiendo de si el profesional está acreditando una pretensión o desvirtuándola. Leer `## Lado` en el perfil de práctica (y la postura por asunto si el asunto la anula):

- **Actor (encuadre ofensivo)** — 🔴 marca eventos que *acreditan* elementos de la pretensión (responsabilidad, nexo causal, daños, conocimiento de la contraparte), *cierran* lagunas que el demandado intentará abrir, o *inician* plazos de prescripción a favor del actor. 🟡 marca eventos que apoyan la pretensión pero son susceptibles de objeción. ⚪ es contexto de fondo.
- **Demandado (encuadre defensivo)** — 🔴 marca eventos que *rompen* elementos de la pretensión (falta de nexo causal, falta de conocimiento, improcedencia), *abren* defensas de prescripción o incompetencia, o *respaldan* excepciones (pago, novación, compensación, prescripción, cosa juzgada). 🟡 marca eventos que debilitan la narrativa del actor. ⚪ es contexto de fondo.
- **Ambos / varía** — preguntar al usuario por cronología qué lado enmarcar para las etiquetas de relevancia. La línea de tiempo subyacente es neutral; solo cambia la lectura de relevancia.

Anotar el encuadre aplicado al inicio del resultado: `Etiquetas de relevancia aplicadas desde la perspectiva del [actor / demandado].` Al producir la variante de capítulo de hechos, usar el lado por defecto salvo que el usuario especifique lo contrario.

## Cargar contexto

Común:
- CLAUDE.md de configuración del plugin → contexto de teoría del caso (jurídico interno: `## Panorama` para fuentes documentales; abogado de despacho: `## Teoría del caso` y `## Revisión documental` para plataforma + custodios), `## Resultados` para el encabezado de confidencialidad, `## Postura de decisión` para la regla de señalamiento de confidencialidad.
- `chronology.md` previo de este asunto, si existe.
- Cualquier archivo que el usuario suba o ruta que proporcione en sesión.

`--matter` mode también lee:
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` → teoría del caso, hechos clave, hecho pivote (para etiquetar relevancia), fechas clave.
- Patrón de carpeta de asunto por defecto del CLAUDE.md → dónde viven los documentos de este slug.

`--documents` mode también lee:
- Metadatos de la plataforma de gestión documental si un conector está disponible (DMS, CLM) — por custodio + rango de fechas.
- Índice de producción o manifiesto documental si el usuario lo señala.

**Compuerta de conflictos — no se puede eludir (`--matter` mode).** Antes de construir la cronología, verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rechazar y redirigir:

> "No encuentro [slug del asunto] en el registro de asuntos. Ejecuta `/litigacion-legal-mexico:matter-intake` primero para que se corra la verificación de conflictos y se configure el espacio de trabajo del asunto. No construiré una cronología de un asunto que no ha sido dado de alta — la verificación de conflictos es la compuerta."

No continuar con un asunto no dado de alta. El intake es lo que corre conflictos y escribe la fila de `_log.yaml` que este skill lee. `--documents` mode (operando contra un conjunto documental ad-hoc sin slug de asunto) está exento de la compuerta, pero sus resultados deben tratarse como investigación previa al asunto y no archivarse como producto de trabajo del asunto.

## Flujo de trabajo

### Paso 0: Compuerta de confidencialidad (se ejecuta primero, cada vez)

El trabajo de cronología extrae de documentos. Los documentos frecuentemente están protegidos por secreto profesional (Art. 36 Ley Reglamentaria del Art. 5° Constitucional; CPF Arts. 210-211) — los expedientes internos del asunto frecuentemente lo están por defecto; las producciones documentales de contraparte o de terceros pueden contener material confidencial o no revisado. Extraer contenido de un documento confidencial a una cronología que después se comparta puede *comprometer* la protección, dependiendo de quién la reciba. El análisis de pérdida de confidencialidad es casuístico — obtener autorización del abogado responsable antes de distribuir.

El skill no extraerá hasta que el usuario elija una postura de confidencialidad:

> Antes de extraer: ¿cómo se han revisado las fuentes en materia de confidencialidad?
>
> - **A. Todas las fuentes depuradas** — ya las revisaste. Extraigo sin marcas de confidencialidad. Resultado en postura de exhibición; aún marcado como análisis interno.
>
> - **B. Mixtas o no revisadas** — Extraigo y etiqueto cada entrada con una marca `conf`: `ok` (de material claramente no confidencial), `flag` (de material potencialmente confidencial — comunicación abogado-cliente, secreto profesional, interés común), o `review` (fuente poco clara). Las entradas marcadas se señalan visualmente en el resultado, y la variante de capítulo de hechos las filtra por defecto.
>
> - **C. Abortar — revisar primero** — pausar el skill. Revisar las fuentes. Regresar y re-ejecutar.

Registrar la elección en el encabezado de la cronología como `postura_confidencialidad: A-depuradas | B-mixtas | C-abortada`. Si B o C, registrar la justificación brevemente.

**Por qué una compuerta y no solo una advertencia:** una advertencia se lee una vez y se olvida. Una compuerta fuerza la decisión de postura al registro, lo que significa que cada archivo de cronología lleva su propia procedencia — cualquiera que lo lea después sabe si las entradas derivaron de material revisado en materia de confidencialidad.

### Paso 1: Identificar fuentes documentales

**`--matter` mode:**

1. **Rutas del usuario** — cualquier cosa proporcionada en esta sesión (rutas de archivos, enlaces a drive, exportaciones de correo).
2. **Carpeta de asunto por defecto** — del patrón de almacenamiento documental del CLAUDE.md, expandido para este slug (ej., `G:/Jurídico/Asuntos/acme-v-nosotros-2026`).
3. **Fuentes declaradas** — la tabla `Almacenamiento de documentos` del CLAUDE.md, filtrada a las que este asunto pueda tocar (ej., archivo de Gmail para comunicaciones del lado del emisor, carpeta jurídica de SharePoint).
4. **Preguntar** — si las fuentes parecen escasas, preguntar: "Puedo construir con lo que tengo, pero la cronología quedará incompleta. ¿Algo más que puedas señalarme? Correos clave, contratos, memorándums internos, requerimientos de la contraparte?"

**`--documents` mode:**

1. **Conjunto documental** — el usuario señala el directorio de producción o un manifiesto; el skill lee por rango de fojas/identificadores + fecha.
2. **Conector de DMS/CLM** — si un conector MCP está disponible (iManage, NetDocuments, CLM), jalar por custodio + rango de fechas.
3. **Archivos por custodio** — si el usuario proporciona buzones de correo o exportaciones de drive por custodio, leerlos también.
4. **Preguntar** — si la cobertura parece escasa para un custodio o rango de fechas clave, preguntar.

### Paso 2: Obtener + leer

Para cada fuente con archivos legibles:

- **PDFs, correos (.eml), .docx, .txt** — leer directamente.
- **Archivos de correo (Gmail, Outlook)** — si un conector MCP está autenticado, consultar por rango de fechas + contraparte / términos clave; si no, el usuario exporta los hilos relevantes a una carpeta.
- **DMS / CLM** — si el conector está disponible, jalar por custodio + rango de fechas; si no, el usuario proporciona una exportación.

Si el skill no puede acceder a una fuente declarada, nombrarla explícitamente en la sección de Lagunas del resultado en vez de continuar silenciosamente.

**Sin suplemento silencioso.** Si la cobertura de fuentes para una era del asunto es escasa — menos documentos de lo esperado para un periodo reclamado, un custodio cuyo buzón no es accesible, una producción que no ha llegado — reportar lo encontrado y detenerse. NO llenar lagunas desde búsqueda web, búsqueda de registros públicos o conocimiento del modelo sobre el asunto sin preguntar. Decir: "Las fuentes arrojaron [N] eventos para [periodo / custodio]. La cobertura parece escasa. Opciones: (1) señalarme fuentes adicionales (fojas, carpeta, buzón), (2) probar otro conector MCP si está configurado, (3) buscar en la web eventos de registro público en esta ventana — los resultados se etiquetarán `[web search — verify]` y deben verificarse contra una fuente primaria antes de confiar, o (4) detenerse aquí y anotar la laguna. ¿Cuál prefieres?" Un abogado decide si acepta fuentes de menor confianza; el skill no decide por ellos.

**Atribución de fuente.** Etiquetar cada entrada de la cronología con de dónde provino el evento: la ruta del archivo, número de foja, conector MCP, o fuente de almacenamiento documental declarada para eventos extraídos de documentos recuperados (ya capturado en la columna de Fuentes). Para cualquier evento o fecha que no pueda trazarse a un documento recuperado — ej., un hecho recordado del conocimiento del modelo, un evento de registro público encontrado vía búsqueda web — etiquetarlo en línea: `[web search — verify]`, `[model knowledge — verify]`, o `[user provided]` donde el usuario declaró el hecho en sesión. Las entradas etiquetadas con `verify` tienen mayor riesgo de fabricación que las entradas con fuente documental y deben verificarse primero. Nunca quitar o colapsar las etiquetas — son la señal más rápida del abogado sobre qué entradas verificar antes de incorporarlas a un escrito o capítulo de hechos.

**El etiquetado alcanza cada sección que declare una conclusión jurídica, plazo, o fecha computada — no solo las entradas de la línea de tiempo.** La línea de tiempo tiene fuente documental. La sección de Lagunas, la sección de Eventos clave, las líneas de vinculación con la teoría, y cualquier declaración de prescripción, caducidad, plazo procesal, o determinación de confidencialidad son análisis jurídico que el skill escribe desde conocimiento del modelo salvo que tengan fuente. Cada tal declaración lleva una etiqueta de procedencia: `[computado de: <regla citada con etiqueta>]`, `[model knowledge — verify]`, `[user provided]`, o una etiqueta de conector de investigación si se recuperó en esta sesión. Una ventana de prescripción sin etiqueta se marca como `[model knowledge — verify]` por defecto. Una línea de "evento clave" que caracteriza la relevancia jurídica de un hecho es análisis y necesita la etiqueta. La regla es simple: si es una aseveración sobre el derecho, no una aseveración sobre lo que dice un documento, debe llevar la misma etiqueta de procedencia que las entradas de la línea de tiempo. Cuando ningún conector de investigación es accesible y el skill computa plazos o cita disposiciones, registrarlo en la línea de **Fuentes:** de la nota del revisor (ver CLAUDE.md del plugin `## Resultados`) — no emitir un banner independiente.

### Paso 3: Extraer eventos

Para cada documento, identificar eventos fechados:

- **Correo:** `[fecha] [remitente] comunicó a [destinatario] [asunto/contenido]`
- **Reunión:** `[fecha] [asistentes] se reunieron sobre [tema]` (según entrada de calendario o minuta)
- **Decisión:** `[fecha] [decisor] decidió [qué]` (según documento que la formaliza)
- **Escrito procesal / promoción:** `[fecha] [parte] presentó [demanda/contestación/escrito/recurso]`
- **Evento externo:** `[fecha] [qué ocurrió]` (contrato firmado, producto lanzado, autoridad actuó, se cruzó un umbral regulatorio)

Un evento por documento generalmente. Ocasionalmente cero (sin fecha o ningún evento establecido). A veces múltiples (minuta de reunión que cubre varias decisiones).

**Marca de confidencialidad por entrada (solo cuando postura_confidencialidad == B-mixtas). Regla de tres estados — nunca decidir silenciosamente que una prueba subjetiva de confidencialidad no se cumple:**

- `conf: ok` — la fuente es **claramente** no confidencial (escritos presentados ante tribunal, correspondencia con autoridades, documentos públicos, comunicaciones de la contraparte sin participación de nuestro abogado). Usar solo cuando no hay teoría plausible de confidencialidad.
- `conf: flag` — la fuente es confidencial con seguridad o probabilidad (comunicaciones con el abogado, memorándums de estrategia, borradores protegidos por secreto profesional, material de interés común). **Valor por defecto para todo lo incierto** — si la determinación del propósito dominante es cercana, o la contemplación de litigio es dudosa, o el contenido es mixto, va aquí, no en `ok`.
- `conf: review` — la fuente es poco clara de entrada, pero el skill no pudo hacer la determinación en absoluto (sin metadatos de remitente/destinatario, ilegible, etc.).

Cuando `conf: flag` o `conf: review`, agregar `[SME VERIFY: estatus de confidencialidad]` en línea para que el abogado lo vea durante revisión. Sub-marcar compromete la confidencialidad (puerta de un solo sentido); sobre-marcar lo corrige el abogado en revisión (puerta de dos sentidos). Preferir el error recuperable.

### Paso 4: Deduplicar

El mismo evento aparece en múltiples documentos: una reunión está en tres calendarios y produce un correo resumen — eso es **un evento con cuatro fuentes**, no cuatro eventos. Fusionar. La entrada fusionada cita todas las fuentes.

### Paso 5: Etiquetar relevancia — conforme a la teoría del caso

Leer el hecho pivote y hechos clave de `matter.md` (`--matter` mode) o de la sección `## Teoría del caso` de la configuración (`--documents` mode). Etiquetar cada evento:

- 🔴 **Clave** — el evento es parte del hecho pivote o un hecho clave a favor/en contra nuestra
- 🟡 **Relevante** — contexto, prueba de patrón, apoya un argumento secundario
- ⚪ **Fondo** — útil para completitud, no va en el escrito

**Disciplina:** una cronología de 300 entradas con 300 etiquetas 🔴 no tiene etiquetas. Reservar 🔴 para eventos que genuinamente moverían al juzgador. En caso de duda, 🟡.

**Etiquetado dudoso:** cuando una entrada se sitúa entre 🔴 y 🟡 (o 🟡 y ⚪), etiquetar en la relevancia inferior y agregar `[SME VERIFY — decisión de relevancia dudosa]` en línea. El criterio del abogado prevalecerá sobre la determinación del skill. Una cronología que sobre-etiqueta con seguridad es menos útil que una que expone su incertidumbre.

### Paso 6: Escribir

El resultado por defecto es la cronología de trabajo. Variantes bajo solicitud.

## Formatos de resultado

### Cronología de trabajo (por defecto)

Ubicación: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/chronology.md`. Completa, etiquetada, anotada. El documento de referencia desde el que trabaja el abogado.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

> **Herencia de confidencialidad.** Esta cronología deriva de documentos del asunto que pueden estar protegidos por secreto profesional (Art. 36 Ley Reglamentaria del Art. 5° Constitucional; CPF Arts. 210-211), material de interés común, o una mezcla. Hereda el estatus de protección de sus fuentes. Distribuirla fuera del círculo de confidencialidad — a áreas de negocio ajenas al asunto, a la contraparte, a un regulador — puede comprometer la protección tanto de la cronología como de las fuentes subyacentes. Almacenar con material confidencial del asunto, marcar consistentemente con las convenciones de confidencialidad de la organización, y tomar decisiones de distribución deliberadamente. La postura de confidencialidad capturada abajo es la estampa de procedencia para cualquier decisión futura de distribución.

# Cronología — [Nombre del Asunto]

> Las etiquetas de relevancia (🔴/🟡/⚪) y marcas de confidencialidad (🔒) son lecturas de primer pase que requieren `[SME VERIFY]` antes de usarse en cualquier producto de trabajo externo (escritos, capítulo de hechos, memorándum al Consejo, entregable a despacho externo).

**Asunto:** [slug]
**Modo:** matter | documents
**Construida:** [AAAA-MM-DD]
**Fuentes:** [N] documentos de [tipos de fuentes]
**Entradas:** [N] ([N] 🔴 / [N] 🟡 / [N] ⚪)
**Hecho pivote:** [una oración]
**Postura de confidencialidad:** A-depuradas | B-mixtas | C-abortada
**Entradas señaladas:** [N] 🔒 *(solo presente cuando postura == B-mixtas)*

---

## Línea de tiempo

| Fecha | Evento | Etiqueta | 🔒 | Fuentes |
|---|---|---|---|---|
| [AAAA-MM-DD] | [qué ocurrió, una oración] | 🔴/🟡/⚪ | [vacío / 🔒-flag / 🔒-review] | [rutas de archivo o fojas] |

---

## Eventos clave (solo 🔴)

[Extraídos, cada uno con una línea sobre por qué importa para la teoría.]

### [fecha] — [título del evento]
- Qué: [una línea]
- Vinculación con la teoría: [por qué importa]
- Fuentes: [lista]

---

## Lagunas

**Rangos de fecha sin eventos:**
[rangos — ¿dónde están los documentos de este periodo?]

**Esperados pero ausentes:**
[eventos que esperaríamos ver documentados pero no están — ej., "convenios modificatorios entre 2024-06 y 2025-03 — no producidos"]

**Fuentes no accesibles:**
[fuentes declaradas en CLAUDE.md pero no accesibles en esta ejecución — ej., "Google Drive — Jurídico — sin conector MCP; se necesita exportación"]

---

## Disciplina de marcadores

- `[VERIFY: aseveración de hecho — fecha, participantes, contenido]` — aún no confirmado contra el documento subyacente
- `[UNCERTAIN: caracterización jurídica — ej., si un evento activa un plazo procesal o prescripción]`
- `[CITE NEEDED: foja / exhibición / página de acta]`
- `[SME VERIFY: estatus de confidencialidad | decisión de relevancia dudosa]` — se requiere criterio del abogado

---

## Versión
- v[N] construida el [fecha] a partir de [resumen de fuentes]
- v[N-1] construida el [fecha] (previa, supersedida)
```

### Cronología para capítulo de hechos (bajo solicitud)

Filtrar a solo 🔴 y 🟡 relevantes. Presentar como prosa en orden cronológico narrativo — el esqueleto para la sección de hechos de un escrito procesal. Cada párrafo es un evento o agrupación estrechamente vinculada, con citas al expediente.

**Filtro de confidencialidad por defecto:** cuando `postura_confidencialidad == B-mixtas`, las entradas 🔒-flag y 🔒-review se **excluyen** por defecto. La variante de capítulo de hechos está destinada para uso externo eventual (escritos, desahogo de vistas, comunicaciones con contraparte) — las entradas 🔒 no pertenecen ahí hasta que el abogado confirme el estatus de confidencialidad. Si el usuario quiere incluir entradas 🔒 de todos modos, requerir reconocimiento explícito `--include-flagged`; capturar el reconocimiento en el encabezado del resultado como registro permanente.

### Cronología específica por testigo (bajo solicitud)

Filtrar a eventos donde un testigo nombrado es remitente, destinatario, asistente, o sujeto. Alimenta la preparación de testigos y ayuda a reconstruir qué sabía un testigo y cuándo.

## Construcciones incrementales

Si `chronology.md` existe:

- Leer versión previa
- Construir nueva cronología de fuentes actuales
- Diferencias: nuevos eventos (desde última construcción), entradas modificadas (nuevas fuentes agregadas a eventos existentes), entradas eliminadas (raro; anotar por qué)
- Preservar el número de versión previo; escribir nueva versión con `v[N+1]`
- Resumen de resultado de lo que cambió

## Integración con matter.md / history.md

**Intencionalmente separados** (jurídico interno, `--matter` mode). `history.md` es el registro en curso del abogado — decisiones, actualizaciones, hitos procesales, notas de estrategia interna. `chronology.md` es la línea de tiempo de hechos orientada a la defensa/demanda. Se traslapan pero no se fusionan:

- Se emitió una retención documental → va en history.md (acción interna). Generalmente no en cronología (no es un hecho de la controversia).
- La contraparte envió un requerimiento de pago el 14 de marzo → va en chronology.md (🟡 — establece conocimiento de la contraparte). También en history.md si el intake lo referenció.
- Nuestro memorándum de recomendación de reserva fue redactado → solo history.md.

Cuando el abogado quiera eventos del historial en la cronología, puede pegarlos. El valor por defecto es que permanecen separados.

## Hitos procesales mexicanos (referencia para etiquetas de relevancia)

Los hitos procesales relevantes para etiquetar eventos en el sistema jurídico mexicano incluyen:

- **Emplazamiento** — momento en que se notifica formalmente al demandado; inicia plazos para contestar.
- **Contestación de demanda** — fija la litis y los hechos controvertidos.
- **Periodo de pruebas** — ofrecimiento, admisión y desahogo de pruebas.
- **Alegatos** — argumentos finales de las partes antes de sentencia.
- **Sentencia** — resolución del juzgador de primera instancia.
- **Recursos (apelación / revocación)** — impugnación ante segunda instancia.
- **Amparo (indirecto / directo)** — control constitucional; puede suspender actos de autoridad.
- **Ejecución de sentencia** — cumplimiento forzoso de la resolución.

## Lo que este skill no hace

- **Resolver contradicciones.** Cuando dos documentos dicen cosas diferentes sobre cuándo ocurrió un evento, ambas entradas se incluyen con una marca. La resolución es decisión del abogado; puede requerir declaración de testigo o mayor investigación.
- **Inventar eventos que no están en las fuentes.** Si no está en los documentos (ni en matter.md ni en la configuración como hecho capturado), no está en la cronología — pero "Lagunas" puede señalarlo como ausente.
- **Garantizar completitud.** Una cronología es tan buena como sus fuentes. Si la producción documental está en curso y solo ha llegado el 20%, la cronología lo refleja. Nombrar la limitación.
- **Decidir el estatus de confidencialidad por el usuario.** La compuerta del Paso 0 fuerza la decisión de postura; la marca `conf` por entrada captura la clasificación de primer pase. Las determinaciones definitivas de confidencialidad son decisión del abogado conforme a las marcas `[SME VERIFY]`.
