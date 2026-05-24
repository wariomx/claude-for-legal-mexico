# Especificación de Salida en Excel

El archivo de Excel es el entregable que la mayoría de los equipos de operación realmente abrirán. Hazlo bien.

## Si Claude in Excel / agente de Office está disponible

Construye el libro de trabajo directamente en Excel mediante el agente de Office. Este es el camino preferido porque preserva el formato, permite al revisor trabajar en su herramienta nativa y soporta el patrón de comentarios en celda de forma nativa.

## Si no, usa openpyxl

Verifica con `python3 -c "import openpyxl"`. Si no está instalado, ofrece instalarlo (`pip3 install openpyxl`) o recurre a CSV como alternativa.

## Estructura del libro de trabajo

**Hoja 1: `Revisión`** (la tabla principal)
- Fila 1: Encabezado de producto de trabajo (celda combinada, el encabezado de la configuración del plugin `## Resultados`)
- Fila 2: Etiquetas de columna
- Fila 3+: Una fila por documento
- Columna A: Nombre / ruta del documento
- Columnas B en adelante: una por columna del esquema, en orden del esquema
- Después de cada columna de datos, una columna oculta `_source` con `[cita] | [ubicación]`
- Comentario en la celda de datos = la cita y ubicación (para que aparezca al pasar el cursor incluso con `_source` oculta)
- Relleno de celda por estado: sin relleno = `answered`, `#FFF2CC` (amarillo claro) = `unclear` o `needs_review`, `#EFEFEF` (gris claro) = `not_present`
- Una columna `Verificado` después de cada grupo de [datos + _source]: en blanco por defecto. El revisor la completa. Validación por lista desplegable: `✓`, `✗`, `?`.

**Hoja 2: `Marcas`**
- Una fila por celda marcada como `unclear` o `needs_review`
- Columnas: Documento, Columna, Estado, Valor (si existe), Cita, Ubicación, Nota
- Esta es la cola de trabajo de verificación. Ordena por columna para que el revisor pueda agrupar juicios similares.

**Hoja 3: `_schema`**
- Las definiciones de columna de `.review-schema.yaml`, una fila por columna: id, label, type, options, prompt
- Hace que el archivo sea autodocumentado. Un socio que lo abra seis meses después puede ver exactamente qué se preguntó.

**Hoja 4: `_summary`**
- Conteo de documentos, conteo de columnas, fecha de ejecución
- Conteos por columna de answered / not_present / unclear / needs_review
- Lista de columnas señaladas por el pase de normalización
- El texto recordatorio de verificación

## Qué no hacer

- No escribas una columna de porcentaje de confianza. No es información útil. El estado + cita es la señal.
- No trunces las citas para que quepan en una celda. Ajusta el texto o pon la cita completa en el comentario.
- No combines celdas en la región de datos. Los abogados van a ordenar y filtrar.
- No escribas la tabla sin las hojas `_schema` y `_summary`. La autodocumentación es lo que hace que el archivo sea confiable.


## Defensa contra inyección de fórmulas

Antes de escribir cualquier celda en Excel, Sheets o CSV, neutraliza la inyección de fórmulas. El texto proveniente de contrapartes (citas de contratos, nombres de partes, datos de agentes registrados, exportaciones de CLM) es controlado por el atacante. Una celda que comience con `=`, `+`, `-`, `@`, `	`, `` o `
` será interpretada como fórmula o romperá la estructura de la fila.

- **Prefija con una comilla simple:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (se muestra como texto, no se ejecuta)
- **Aplica a toda celda que contenga texto proveniente de un documento, resultado de herramienta o pegado del usuario.** Los encabezados de columna que tú controlas y los valores calculados que tú produces son seguros.
- **CSV: también escapa comas incrustadas, comillas dobles y saltos de línea** (formato RFC 4180).
- Esto no es opcional. Una hoja de cálculo que tu usuario abre en Excel y que dispara una macro o exfiltra datos vía DDE es un ataque a la cadena de suministro contra tu usuario.
