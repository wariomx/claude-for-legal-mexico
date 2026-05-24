---
name: boletin-monitor
description: >
  Monitorea el boletín diario del Tribunal de Justicia de Jalisco (CJJ) por
  nombre de parte (actor o demandado) en todos los juzgados mercantiles de la
  ZM Guadalajara. Usa la API pública zmg_date sin autenticación. Genera
  reporte con matches, historial y notificaciones.
argument-hint: '"NOMBRE DE PARTE" [--fecha YYYY-MM-DD] [--juzgados M01,M02,...] [--todos]'
---

# /boletin-monitor

Monitoreo del boletín judicial diario del Consejo de la Judicatura de Jalisco
(CJJ) — juzgados mercantiles de la Zona Metropolitana de Guadalajara.

## Propósito

El boletín judicial es la fuente pública de actuaciones procesales. Antes de
demandar, necesitas saber si tu deudor ya fue demandado por otro acreedor.
Mientras litigas, necesitas saber si hubo movimiento en tus expedientes. Este
skill consulta el boletín del CJJ por nombre de parte y genera un reporte
estructurado.

**Casos de uso principales:**
- Saber si un deudor ya fue demandado por otro acreedor antes de iniciar demanda
- Monitorear expedientes propios sin autenticación
- Detectar movimiento en autos de interés
- Vigilancia preventiva de contrapartes

## Restricciones

⚠️ **Este skill consulta SOLO el extracto del boletín público.** NO consulta
expedientes certificados ni el contenido completo de las actuaciones. Para
seguimiento detallado de expedientes con acceso autenticado, usar
`/litigacion-legal-mexico:revision-expedientes-jalisco`.

⚠️ **Solo juzgados de la ZMG (Zona Metropolitana de Guadalajara).** Para
tribunales federales, usar el `vigilante-expedientes` agent o las herramientas
del Portal del PJF.

## Herramienta MCP

Usar `mcp__CJJ__get_boletin(judged, date)` del servidor MCP `CJJ`
(incluido en `conectores-legal-mexico`). No requiere autenticación.

**Respaldo directo** (si el MCP CJJ no está disponible): WebFetch al
endpoint público `https://api.cjj.gob.mx/bulletin/zmg_date?judged={CODIGO}&date={YYYY-MM-DD}`

**Respuesta JSON:** cada registro contiene:

| Campo | Descripción |
|---|---|
| `EXP` | Número de expediente (ej. "07/2026") |
| `CVE_JUZ` | Clave del juzgado (ej. "M02", "OM06") |
| `FCH_PRO` | Fecha de la promoción (ISO 8601) |
| `FCH_ACU` | Fecha del acuerdo (ISO 8601) |
| `BOLETIN` | Texto del acuerdo/boletín |
| `TIPO` | Tipo de procedimiento (ej. ".") |
| `NOTIFICACI` | Tipo de notificación (ej. "B" = boletín) |
| `DI` | Indicador (ej. "N") |
| `FCH_RES` | Fecha de resolución (puede ser null) |
| `CVE_JUI` | Clave del tipo de juicio (ej. "ME" = Mercantil Ejecutivo) |
| `DESCRIP` | Descripción del tipo de juicio (ej. "MERCANTIL EJECUTIVO") |
| `act_names` | Nombres de la parte actora |
| `dem_names` | Nombres de la parte demandada |

**Respuesta envuelta en:** `{"success": 1, "data": [...]}`

## Juzgados mercantiles ZMG (18 juzgados)

| Código | Juzgado |
|---|---|
| M01–M07 | Juzgados Mercantiles 1° al 7° |
| M09–M10 | Juzgados Mercantiles 9° y 10° |
| OM01–OM09 | Juzgados Mercantiles Orales 1° al 9° |

**Nota:** M08 no está en el catálogo activo. Los juzgados orales mercantiles
manejan juicios ejecutivos mercantiles y de cuantía menor.

## Flujo de trabajo

### Paso 1 — Parámetros

Obtener del usuario:
- **Nombre de la parte** (requerido) — nombre completo o parcial para buscar
  en `act_names` y `dem_names`
- **Fecha** (opcional) — `YYYY-MM-DD`, por defecto hoy. Usar `--todos` para
  barrer los últimos 7 días
- **Juzgados** (opcional) — lista de códigos separados por coma. Por defecto:
  todos los 18 juzgados mercantiles ZMG

### Paso 2 — Consulta

Para cada juzgado × fecha:
1. Llamar `mcp__CJJ__get_boletin(judged="{código}", date="{fecha}")`
2. Filtrar registros donde `act_names` o `dem_names` contengan el nombre
   buscado (búsqueda case-insensitive, matching parcial, tolerante a diacríticos)
3. Acumular matches

**Manejo de errores:**
- Si el endpoint devuelve error o array vacío para un juzgado/fecha, registrar
  y continuar con el siguiente — no fallar por un juzgado inactivo
- Si todos los juzgados fallan, reportar: "No se pudo conectar a la API del
  CJJ. Verificar disponibilidad del servicio."

### Paso 3 — Reporte

Generar reporte estructurado:

```
📋 Boletín CJJ — Búsqueda por parte: "[NOMBRE]"
Fecha(s): [fecha(s) consultadas] | Juzgados: [N] consultados

🔍 MATCHES ([N] encontrados)

• Expediente: [EXP] — Juzgado [CVE_JUZ]
  Tipo: [TIPO]
  Actor: [act_names]
  Demandado: [dem_names]
  Acuerdo: [FCH_ACU] — [DESCRIP]
  Notificación: [NOTIFICACI]

[repetir por cada match]

📊 RESUMEN
• Total de registros revisados: [N]
• Matches encontrados: [N]
• Juzgados con matches: [lista]
• Juzgados sin movimiento: [lista]

⚠️ Este reporte se basa en el boletín público del CJJ.
No sustituye la revisión del expediente certificado.
Para seguimiento detallado: /litigacion-legal-mexico:revision-expedientes-jalisco
```

### Paso 4 — Integración con portafolio

Si el usuario tiene asuntos activos en `_log.yaml` con jurisdicción Jalisco:
- Cruzar matches contra expedientes conocidos en el portafolio
- Señalar matches nuevos que no correspondan a expedientes registrados
  (posible demanda de tercero contra la misma parte)
- Ofrecer agregar nuevos expedientes detectados al portafolio

### Paso 5 — Opciones

> **¿Qué sigue?**
> 1. **Ampliar búsqueda** — barrer más fechas o juzgados adicionales
> 2. **Seguimiento detallado** — abrir el expediente con
>    `/litigacion-legal-mexico:revision-expedientes-jalisco` (requiere
>    autenticación del portal ciudadano CJJ)
> 3. **Agregar al portafolio** — registrar el expediente en `_log.yaml` para
>    vigilancia automatizada por el `vigilante-expedientes` agent
> 4. **Programar vigilancia** — configurar monitoreo recurrente de esta parte
>    en el boletín

## Integración con vigilante-expedientes

Cuando el `vigilante-expedientes` agent detecta asuntos con jurisdicción
Jalisco en `_log.yaml`, invoca la lógica de este skill para verificar el
boletín del CJJ en adición a las fuentes federales. El agente no duplica
la consulta — este skill es la fuente única para boletín CJJ.

## Notas técnicas

- La API es pública y no requiere autenticación
- Los datos del boletín se publican al final del día hábil — consultas
  antes de las 18:00 pueden no reflejar las actuaciones del día
- Los nombres pueden tener variaciones de acentuación y formato — la
  búsqueda debe ser tolerante a diacríticos
- `act_names` y `dem_names` pueden ser `null` — usar null-safe handling
- `CVE_JUI` indica el tipo de juicio: "ME" = Mercantil Ejecutivo,
  "MO" = Mercantil Ordinario, etc.
- El boletín solo cubre juzgados de la ZMG, no del interior del estado
