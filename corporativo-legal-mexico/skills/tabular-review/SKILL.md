---
name: tabular-review
description: >
  Revisión tabular — una fila por documento, una columna por dato, cada celda
  citada a fuente. Diseñada para debida diligencia de F&A ("revisa estos 200
  contratos de la sociedad objetivo buscando cláusulas de cambio de control,
  cesión y cláusula MAC") pero funciona para cualquier revisión por lotes que
  necesite una hoja de cálculo como producto final. Usar cuando el usuario diga
  "revisión tabular", "tabla de revisión", "construye una tabla", "extrae estos
  campos de estos contratos", "revisa estos documentos para X, Y, Z", "dame una
  hoja de cálculo de", "revisión en lote", o apunte a una carpeta de documentos
  y pida compararlos.
---

# /tabular-review

1. Cargar `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → estructura de debida diligencia, umbrales, formato interno.
2. Confirmar: qué documentos, qué columnas, a dónde va la salida.
3. Construir el esquema tipado. Escribir `.review-schema.yaml`. Confirmar con el usuario.
4. Ejecución de muestra (3–5 documentos). Ajustar esquema. Confirmar.
5. Desplegar — un subagente por documento, en paralelo. Cada celda: valor + estado + cita textual + ubicación.
6. Pase de normalización. Señalar valores atípicos e inconsistencias.
7. Salida: `.xlsx` o Google Sheets (preguntar cuál), más `.csv` + `_sources.csv` + markdown siempre. Encabezado de secreto profesional.
8. Resumen: carga de verificación (conteos de not_present / unclear / needs_review por columna), columnas señaladas, dónde están los archivos, recordatorio de que cada celda es una pista, no un hallazgo.

```
/corporativo-legal-mexico:tabular-review
/corporativo-legal-mexico:tabular-review --schema .review-schema.yaml --docs ./vdr/02-Contratos/
/corporativo-legal-mexico:tabular-review --template ma-diligence
```

**`--schema <ruta>`:** Usa un archivo de esquema existente en lugar de construir uno. Útil para re-ejecuciones y adiciones incrementales.

**`--template <nombre>`:** Parte de una plantilla en `references/`. Actualmente: `ma-diligence`.

**`--docs <ruta>`:** Fuente de documentos. Una carpeta local, un ID de carpeta de Drive, o una ruta de VDR. Si se omite, pregunta.

**`--output <xlsx|gsheets|csv>`:** Formato de salida. Si se omite, pregunta.

**`--sample <n>`:** Tamaño de muestra para la verificación del esquema. Predeterminado 5.

---

## Contexto del asunto

**Contexto del asunto.** Revisa `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗` (el predeterminado para usuarios internos), ignora el resto de este párrafo — las habilidades usan contexto a nivel de práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, pregunta: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `nivel de práctica`." Carga el `matter.md` del asunto activo para contexto y anulaciones específicas del asunto. Escribe las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leas archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

Tienes un montón de documentos y una lista de preguntas que necesitas responder de manera consistente en todos ellos. Una lista de requerimientos de debida diligencia. Una auditoría de contratos con proveedores. Una revisión de portafolio de arrendamientos. La salida es una tabla: filas de documentos, columnas de datos, y cada celda rastreable hasta las palabras exactas en la fuente.

Esto no es identificación de problemas. `diligence-issue-extraction` encuentra los 30 problemas ocultos en 2,000 documentos. Esta habilidad responde las mismas 15 preguntas sobre los 2,000 documentos. Ambas son legítimas; responden preguntas diferentes.

Esto tampoco es un sustituto de que un humano lea el documento. Cada celda que produce esta habilidad es una **pista que necesita verificación**, no un hallazgo. La salida está diseñada para hacer que la verificación sea rápida, no para omitirla.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → estructura de debida diligencia, umbrales de materialidad, preferencias de formato interno
- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/deal-context.md` si se trabaja una operación específica
- Un archivo de esquema existente si el usuario tiene uno (`.review-schema.yaml`)

## El sistema de tipos de columna

Lo que hace útil una revisión tabular es que la Columna C significa lo mismo en la fila 1 que en la fila 200. El texto libre se desvía. Los tipos se mantienen.

Cada columna tiene un **tipo** que restringe el formato de la respuesta:

| Tipo | Qué devuelve | Usar para |
|---|---|---|
| `verbatim` | Cita exacta del documento, carácter por carácter | Términos definidos, lenguaje de cláusulas operativas, cualquier cosa donde las palabras importen |
| `classify` | Un valor de una lista fija que tú defines | Sí/No, presente/ausente, variantes de cláusula (p. ej., "consentimiento exclusivo" / "consentimiento que no se negará injustificadamente" / "silencio") |
| `date` | Fecha ISO | Fecha de vigencia, vencimiento, plazo de notificación de terminación |
| `duration` | Número + unidad | Plazo del contrato, periodo de aviso, periodo de supervivencia |
| `currency` | Número + código de moneda | Límites, umbrales, honorarios, referencias al precio de compra |
| `number` | Número simple | Conteos, porcentajes, referencias a páginas |
| `free` | Resumen breve en texto libre | Usar con moderación — este es el tipo que se desvía. Solo cuando los demás genuinamente no aplican. |

**La regla del textual literal:** Cada columna que no sea `verbatim` también captura la cita exacta de la fuente que sustenta la respuesta, como campo acompañante. La respuesta en la celda es la interpretación; la cita es la evidencia. Una celda `classify` que dice "consentimiento que no se negará injustificadamente" es inútil sin la oración de donde provino, porque el trabajo del revisor es verificar si esa es la lectura correcta.

## Los tres estados de "no encontrado"

Una celda en blanco oculta información. Fuerza uno de tres estados explícitos cada vez que no puedas producir una respuesta positiva:

| Estado | Significado | Cuándo usar |
|---|---|---|
| `not_present` | El documento fue leído y la cláusula no está ahí | Tienes confianza de que el tema no se aborda |
| `unclear` | Algo hay pero no puedes clasificarlo con confianza | Redacción ambigua, cláusula parcial, disposiciones contradictorias |
| `needs_review` | Encontraste algo pero un humano debe tomar la decisión | Caso límite, redacción inusual, la respuesta depende de un juicio que el esquema no captura |

Estos son tres datos diferentes. Un equipo de operación maneja "el contrato guarda silencio sobre la cesión" de manera muy diferente a "la cláusula de cesión es ambigua." Colapsar ambos en una celda en blanco pierde la distinción.

## Flujo de trabajo

### Paso 0: Qué y dónde

Confirmar:
1. **Documentos.** ¿Dónde están? MCP de VDR (Box, Datasite, iManage), carpeta local, carpeta de Google Drive, o una lista de archivos. ¿Cuántos? Si >200, advertir que esto tomará tiempo y ofrecer comenzar con un subconjunto filtrado por materialidad.
2. **Esquema.** ¿Qué columnas? Dos caminos:
   - El usuario elige una plantilla de `references/` (la estándar de debida diligencia de F&A es la predeterminada)
   - El usuario describe las columnas en lenguaje natural y tú las estructuras en el esquema tipado
3. **Salida.** Excel (`.xlsx`) o Google Sheets — pregunta en cuál trabaja el equipo. CSV y markdown siempre se escriben como respaldos. La salida va a la carpeta de la operación, Drive, o donde el usuario indique.

### Paso 1: Construir y confirmar el esquema

Convierte la lista de columnas del usuario en un esquema estructurado. Para cada columna: un `id` estable, una `label` legible para humanos, un `type`, un `prompt` (la pregunta que un revisor leyendo el documento haría), y para columnas `classify` una lista de `options`.

Escríbelo en `.review-schema.yaml` junto a la salida. Este archivo es el artefacto reutilizable — el usuario puede editarlo, añadir una columna, re-ejecutar contra nuevos documentos. Muéstralo al usuario y confirma antes de desplegar.

```yaml
schema:
  name: "Debida Diligencia F&A — Proyecto [Código]"
  created: 2026-05-07
  columns:
    - id: counterparty
      label: "Contraparte"
      type: verbatim
      prompt: "¿Quién es la parte contratante distinta de la sociedad objetivo?"
    - id: effective_date
      label: "Fecha de Vigencia"
      type: date
      prompt: "¿Cuándo entró en vigor el contrato?"
    - id: change_of_control
      label: "Cambio de Control"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, automatic_termination, notice_only]
      prompt: "¿El contrato aborda un cambio de control de la sociedad objetivo? ¿Qué requiere?"
    - id: assignment
      label: "Restricciones de Cesión"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, freely_assignable, assignable_to_affiliates]
      prompt: "¿Puede la sociedad objetivo ceder este contrato? ¿Qué restricciones aplican?"
    # ... más columnas
```

### Paso 2: Ejecución de muestra

No despliegues a 200 documentos con un esquema sin probar. Ejecuta 3–5 documentos primero. Muestra las filas al usuario. Busca:
- Columnas donde la mayoría de respuestas son `unclear` — el prompt es ambiguo, reescríbelo
- Columnas `classify` donde las respuestas no encajan en las opciones — añade opciones o cambia a `free`
- Columnas `verbatim` que devuelven paráfrasis — refuerza que debe ser carácter por carácter

Ajusta el esquema, re-ejecuta la muestra, confirma. Esto le ahorra al usuario una ejecución completa que tiene que descartarse.

### Paso 3: Desplegar

Un subagente por documento, en paralelo. Cada subagente:

1. Lee el documento completo (no un fragmento de RAG — el documento entero).
2. Para cada columna, encuentra la disposición relevante.
3. Devuelve una fila estructurada: para cada columna, `{value, state, quote, location}`.
   - `value` es la respuesta tipada (o null si `state` no es `answered`)
   - `state` es `answered | not_present | unclear | needs_review`
   - `quote` es el texto de soporte textual literal (exacto, sin paráfrasis, sin puntos suspensivos dentro de una oración — si cortas, corta en límites de oración y márcalo)
   - `location` es dónde vive la cita (número de sección, encabezado, página — lo que el documento te dé)

**La cita no es opcional, y la regla del textual literal es mecánica, no exhortativa.** Cada subagente debe cumplir con todo lo siguiente antes de devolver una celda con `state: answered`:

- La `quote` DEBE ser una copia carácter por carácter de texto contiguo del documento fuente, recuperable en la `location` que el subagente cita. NO compongas una cita a partir de un encabezado de sección más texto estándar que esperas que esté ahí. NO parafrasees y lo llames textual literal. NO reconstruyas una cita de memoria de cómo "usualmente" se redactan tales cláusulas. NO llenes vacíos en la fuente con costura de puntos suspensivos a través de texto no contiguo.
- La `location` debe ser lo suficientemente específica para que el pase de normalización pueda reabrir el documento y releer el mismo tramo — un número de sección, encabezado o referencia de página a la que el revisor pueda navegar.
- Si el subagente no puede localizar y copiar el texto exacto (fuente truncada, basura de OCR, disposición implícita pero no escrita, encabezado de sección visible pero cuerpo no cargado), el estado de la celda es `needs_review`, el `value` es null, y `notes` DEBE contener `quote_unavailable: <razón>`. NUNCA es aceptable establecer `state: answered` con una cita compuesta o reconstruida.
- La misma regla aplica a columnas de tipo `verbatim` Y a las citas fuente acompañantes adjuntas a celdas de tipo `classify` / `date` / `duration` / `currency` / `number` / `free`. La cita de soporte lleva la misma obligación de literalidad que el valor de la celda.

El pase de normalización en el Paso 4 verifica esto por muestreo, reabriendo la fuente en la `location` citada y comparando la `quote` almacenada carácter por carácter contra el texto fuente. Una discrepancia degrada la celda a `needs_review`, anota `quote_mismatch`, y señala toda la columna para una verificación más amplia — si un subagente compuso una cita, otros en la misma ejecución pueden haberlo hecho también.

### Paso 4: Normalizar

Después del despliegue, lee la tabla completa columna por columna. Este es el pase que detecta el modo de falla de toda herramienta de revisión tabular: la misma cláusula interpretada de manera inconsistente entre documentos.

Para cada columna `classify`:
- Verifica que cada valor `answered` esté en la lista de opciones. Los atípicos se reclasifican o se elevan a `needs_review`.
- Busca agrupaciones: si 180 documentos dicen `consent_required` y 20 dicen `consent_not_unreasonably_withheld`, probablemente es real. Si 195 dicen `consent_required` y 5 dicen `freely_assignable`, examina los 5 — o son genuinamente diferentes o están mal clasificados.

Para cada columna `date` / `duration` / `currency`:
- Verifica consistencia de formato. Normaliza.
- Señala valores implausibles (un plazo de 99 años, un límite de $1) como `needs_review`.

Para cada columna `verbatim` Y para las citas fuente acompañantes de cada otra columna:
- Verifica por muestreo reabriendo el documento fuente en la `location` citada para una muestra aleatoria (al menos 3–5 filas por columna, o 10% de filas, lo que sea mayor) y comparando la `quote` almacenada carácter por carácter contra la fuente.
- Si alguna cita está compuesta, parafraseada, reconstruida, o no puede localizarse en el tramo citado: degrada esa celda a `needs_review` con `quote_mismatch` en notas, y señala toda la columna — expande la verificación por muestreo al resto de la columna en lugar de asumir que las otras filas están limpias. Una cita fabricada es suficiente para justificar la ampliación de la verificación.
- Una celda con `state: answered` y una cita con discrepancia es una falla de mayor gravedad que una celda `unclear` o `needs_review` — tergiversa la cadena de evidencia. Degrada agresivamente.

### Paso 5: Salida

Escribe la tabla en tres formatos:

**Markdown** (siempre, para revisión en sesión):
```markdown
| Documento | Contraparte | Fecha de Vigencia | Cambio de Control | Cesión | ⚠️ Señalamientos |
|---|---|---|---|---|---|
| Contrato Marco — Acme | Acme Corp | 2023-04-01 | consent_required | consent_required | — |
| Contrato de Suministro — Beta | Beta LLC | 2021-11-15 | ⚠️ unclear | silent | Cambio de control ambiguo §14.2 |
```

**CSV** (`.csv`, siempre):
Un archivo para los valores, un archivo acompañante para las citas y ubicaciones (`_sources.csv`). Mantiene el archivo principal limpio y la cadena de evidencia completa.

**Excel** (`.xlsx`) o **Google Sheets** — lo que use el usuario. Pregunta; no adivines. Ambos siguen la misma estructura de libro de trabajo (ver `references/excel-output.md` y `references/gsheets-output.md`). Para Excel: Claude in Excel (agente de Office) si está disponible, `openpyxl` como alternativa. Para Sheets: MCP de Sheets si está disponible, API de Sheets vía ADC, importación de CSV como alternativa. En la salida de hoja de cálculo:
- Cada columna de datos está emparejada con una columna fuente oculta que contiene la cita y ubicación. Los comentarios de celda (Excel) o notas (Sheets) en la columna visible muestran la cita al pasar el cursor.
- Código de colores por estado: blanco = answered, amarillo = unclear o needs_review, gris = not_present.
- Una columna `Verificado` por columna de datos, en blanco por defecto. El revisor la marca. Este es el patrón de verificar/señalar que hace auditable la tabla — el equipo de la operación puede ver de un vistazo qué ha revisado realmente un humano.
- Una hoja `_schema` con las definiciones de columna, para que el archivo sea autodocumentado.

Antepón el encabezado de secreto profesional de la configuración del plugin `## Resultados` como primera fila. Junto a él, incluye una nota de distribución:

> Esta revisión se deriva de documentos fuente que pueden estar protegidos por secreto profesional, ser confidenciales, o ambos. Hereda el estatus de privilegio y confidencialidad de las fuentes — la distribución fuera del círculo de secreto profesional puede constituir una renuncia a dicha protección. Almacena con los archivos protegidos del asunto y toma las decisiones de distribución de manera deliberada.

### Paso 6: Resumen

Después de escribir la tabla, proporciona al usuario un resumen de una pantalla:
- Conteo de documentos, conteo de columnas, filas completadas
- Conteo de `not_present`, `unclear`, `needs_review` por columna — esta es la carga de trabajo de verificación
- Cualquier columna donde el pase de normalización señaló >10% de las filas
- Dónde están los archivos de salida
- Un recordatorio: cada celda es una pista, no un hallazgo. Se requiere verificación antes de que esto informe una declaración, un anexo o un memorándum.

## Cierra con el árbol de decisión de siguientes pasos

Termina con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personaliza las opciones a lo que esta habilidad acaba de producir — las cinco ramas predeterminadas (redactar el X, escalar, obtener más hechos, vigilar y esperar, algo más) son un punto de partida, no un candado. El árbol es el producto; el abogado elige.

## Lo que esta habilidad no hace

- **No sustituye la lectura de los documentos.** Te dice dónde mirar.
- **No produce puntajes de confianza.** Un 0.73 no es información. Los estados `unclear` / `needs_review` y las citas textuales literales son la señal de confianza — si la cita no sustenta el valor, señálalo.
- **No omite documentos silenciosamente.** Cada documento al que el usuario apuntó obtiene una fila. Un documento que no pudo leerse obtiene una fila de `needs_review` con una nota.
- **No pretende que una paráfrasis es una cita.** La cadena de evidencia es todo el punto.

## Relación con otras habilidades

- `diligence-issue-extraction` encuentra problemas; esta extrae datos puntuales. Si una extracción revela un problema (una cláusula MAC que referencia una meta de utilidades específica, una cláusula de protección anti-dilución), anótalo y sugiere ejecutar diligence-issue-extraction en ese documento.
- `material-contract-schedule` construye una tabla específica (el anexo de revelaciones). Puede consumir directamente la salida de esta habilidad — el anexo es una vista filtrada y reformateada de una revisión tabular.
- `ai-tool-handoff` transfiere la revisión masiva a Luminance/Kira cuando el corpus es demasiado grande o el equipo prefiere una plataforma dedicada. Esta habilidad es la opción interna para todo lo que pueda manejar — ejecútala primero, transfiere el residuo.

## Salvaguardas de salida

Cada salida obtiene el encabezado de secreto profesional. Cada celda obtiene una cita fuente o un estado señalizado. El resumen dice explícitamente que se requiere verificación. La columna `Verificado` de Excel hace que el estado de verificación sea auditable. Esta no es una herramienta que te permite omitir la lectura; es una herramienta que hace la lectura más rápida.
