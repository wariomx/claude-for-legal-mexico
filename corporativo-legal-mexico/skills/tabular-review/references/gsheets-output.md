# Especificación de Salida en Google Sheets

Para equipos en Google Workspace. Misma estructura que la salida en Excel, diferente mecánica. Si ambas opciones (Excel y Sheets) están disponibles, pregunta al usuario cuál prefiere — no adivines a partir de tu entorno.

## Cómo escribirlo

Tres caminos, en orden de preferencia:

1. **MCP de Google Sheets** (si un MCP de `gdrive` o `gsheets` con capacidad de escritura/creación está conectado). Crea la hoja de cálculo, escribe las hojas, configura el formato vía la API.
2. **API de Google Sheets vía ADC** (si el usuario tiene configurado `gcloud auth application-default login --enable-gdrive-access` y Python `google-api-python-client` disponible). Usa `sheets.spreadsheets().create()` y `batchUpdate` para el formato.
3. **Alternativa: CSV + importación manual.** Escribe los CSVs, indica al usuario que los importe a Sheets. También escribe un `format-instructions.md` para que puedan aplicar la codificación de colores y la validación de datos manualmente.

No asumas acceso de escritura que no hayas verificado. Verifica primero; recurre a la alternativa con gracia.

## Estructura del libro de trabajo

Refleja la especificación de Excel exactamente — mismas hojas, misma semántica, mecánica nativa de Sheets:

**Hoja: `Revisión`** (la tabla principal)
- Fila 1: Encabezado de producto de trabajo (celda combinada)
- Fila 2: Etiquetas de columna
- Fila 3+: Una fila por documento
- Columna A: Nombre / enlace del documento (si los documentos fuente están en Drive, hipervínculo al archivo — esta es una ventaja de Sheets sobre Excel)
- Columnas B en adelante: una por columna del esquema
- **Las citas fuente van en notas de celda** (notas de Sheets, no comentarios — las notas son anotaciones persistentes, los comentarios son hilos de colaboración). Las notas aparecen al pasar el cursor y se exportan a `.xlsx` como comentarios.
- Relleno de celda por estado: predeterminado = `answered`, amarillo claro = `unclear` o `needs_review`, gris claro = `not_present`. Usa `repeatCell` con `userEnteredFormat.backgroundColor` en `batchUpdate`.
- Una columna `Verificado` después de cada grupo: en blanco por defecto, validación por lista desplegable `✓ | ✗ | ?` vía `setDataValidation`.

**Hoja: `Marcas`**
- Igual que la especificación de Excel. Una fila por celda marcada.

**Hoja: `_schema`**
- Definiciones de columna de `.review-schema.yaml`.

**Hoja: `_summary`**
- Conteos, columnas señaladas, recordatorio de verificación.

## Ventajas específicas de Sheets a aprovechar

- **Hipervínculos a documentos fuente.** Si los documentos revisados están en Drive (común para exportaciones de VDR y repositorios internos), el nombre del documento de cada fila debe ser un hipervínculo al archivo. Este es el patrón de clic-a-fuente, y Sheets lo hace de forma nativa.
- **Revisión compartida.** Sheets maneja la revisión concurrente mejor que un `.xlsx` local. Si el equipo de la operación quiere dividir el trabajo de verificación, este es el formato a usar.
- **Rangos con nombre para el esquema.** Define un rango con nombre sobre cada columna para que las fórmulas posteriores (tablas dinámicas, conteos condicionales) sean legibles.
- **Formato condicional por columna de estado.** Si escribes una columna oculta `_state` por columna de datos, puedes controlar la codificación de colores desde ella con reglas de formato condicional — más limpio que formato celda por celda y sobrevive al ordenamiento.

## Precauciones específicas de Sheets

- **Las notas son por celda e invisibles en impresión.** Si la salida se va a imprimir o convertir a PDF para una reunión de socios, también escribe las citas en la hoja `Marcas` para que sobrevivan.
- **Sheets tiene un límite de 10 millones de celdas.** No lo alcanzarás en una revisión legal, pero si alguien intenta hacer una tabla de 50,000 documentos con 30 columnas más columnas de fuente, adviérteles.
- **Configuración de compartir predeterminada.** Según el perfil de práctica del plugin, esto es producto de trabajo protegido por secreto profesional. Crea la hoja de cálculo con permisos restringidos (solo propietario), y dile al usuario que la comparta deliberadamente. No uses "cualquiera con el enlace" como predeterminado.
- **Escape de fórmulas.** Si una cita textual comienza con `=`, `+`, `-` o `@`, prefíjala con una comilla simple (`'`) para que Sheets no intente interpretarla como fórmula. Este es un modo de falla real: una cláusula contractual que empieza con "- Las partes acuerdan..." se mostrará como un error de fórmula sin el escape.

## Qué no hacer

Igual que la especificación de Excel: sin porcentajes de confianza, sin citas truncadas, sin celdas combinadas en la región de datos, y siempre escribe las hojas `_schema` y `_summary`.


## Defensa contra inyección de fórmulas

Antes de escribir cualquier celda en Excel, Sheets o CSV, neutraliza la inyección de fórmulas. El texto proveniente de contrapartes (citas de contratos, nombres de partes, datos de agentes registrados, exportaciones de CLM) es controlado por el atacante. Una celda que comience con `=`, `+`, `-`, `@`, `	`, `` o `
` será interpretada como fórmula o romperá la estructura de la fila.

- **Prefija con una comilla simple:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (se muestra como texto, no se ejecuta)
- **Aplica a toda celda que contenga texto proveniente de un documento, resultado de herramienta o pegado del usuario.** Los encabezados de columna que tú controlas y los valores calculados que tú produces son seguros.
- **CSV: también escapa comas incrustadas, comillas dobles y saltos de línea** (formato RFC 4180).
- Esto no es opcional. Una hoja de cálculo que tu usuario abre en Excel y que dispara una macro o exfiltra datos vía DDE es un ataque a la cadena de suministro contra tu usuario.
