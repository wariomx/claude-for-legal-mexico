---
name: revision-expedientes-jalisco
description: >
  Revisión y monitoreo de expedientes en el Poder Judicial de Jalisco (CJJ)
  en tiempo real vía la API del Portal Ciudadano (nilo.cjj.gob.mx). Consulta
  materias, partidos judiciales, municipios y expedientes con autenticación JWT.
  Complementa al boletin-monitor con acceso completo al expediente.
argument-hint: "[expediente o nombre de parte]"
---

# /revision-expedientes-jalisco

Acceso autenticado a expedientes del Poder Judicial del Estado de Jalisco vía
el Portal Ciudadano del CJJ.

## Propósito

El boletín público (`/litigacion-legal-mexico:boletin-monitor`) muestra
extractos. Este skill accede al expediente completo vía la API autenticada del
Portal Ciudadano — acuerdos, autos, actuaciones, notificaciones, promociones
y documentos del expediente electrónico. Útil para:

- Seguimiento detallado de expedientes propios o de interés
- Consulta de catálogos judiciales (materias, partidos, municipios, juzgados)
- Verificación de datos procesales contra el expediente certificado
- Monitoreo de expedientes de la contraparte

## Herramientas MCP — CJJ

Las credenciales del Portal Ciudadano CJJ se gestionan automáticamente vía el
servidor MCP `CJJ` (incluido en `conectores-legal-mexico`). Configurar con:

```
claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
```

**Herramientas disponibles:**

| Herramienta | Auth | Descripción |
|---|---|---|
| `mcp__CJJ__get_boletin(judged, date)` | Ninguna | Boletín público — juzgados mercantiles ZMG |
| `mcp__CJJ__login()` | — | Autentica y almacena JWT en sesión |
| `mcp__CJJ__get_all_matters()` | Token público | Catálogo de 7 materias judiciales |
| `mcp__CJJ__get_municipalities()` | Token público | 125 municipios de Jalisco |
| `mcp__CJJ__get_judicial_parties()` | Token público | 54 partidos judiciales |
| `mcp__CJJ__get_user_status()` | Token público | Estado del sistema Nilo |
| `mcp__CJJ__fetch(method, path, body?)` | JWT (auto) | Petición autenticada a cualquier endpoint |

`mcp__CJJ__fetch` auto-autentica: si no hay JWT activo, hace login automáticamente
antes de enviar la petición. Llamar `mcp__CJJ__login()` explícitamente solo si
se necesita renovar una sesión expirada.

**Si el MCP CJJ no está disponible** (servidor no configurado), usar WebFetch
directamente con el token desde las variables de entorno `CJJ_NILO_EMAIL`,
`CJJ_NILO_PASSWORD`, `CJJ_NILO_PUBLIC_TOKEN`. Ver referencia de API abajo.

## Referencia de API: nilo.cjj.gob.mx

**Base URL:** `https://nilo.cjj.gob.mx/api/v1`

Endpoints de catálogo (para consulta directa vía WebFetch como respaldo):

| Endpoint | Auth | Descripción |
|---|---|---|
| `POST /auth/sign_in` | Raw token | Login — body: `{"email","password","app_id":2}` |
| `GET /matters/get_all_matters` | Bearer token | 7 materias judiciales |
| `GET /catalogs/municipalities` | Raw token | 125 municipios |
| `GET /judicial_parties/list` | Raw token | 54 partidos judiciales |
| `GET /users/status` | Raw token | Estado del sistema |
| `GET https://api.cjj.gob.mx/bulletin/zmg_date?judged={COD}&date={YYYY-MM-DD}` | Ninguna | Boletín público |

**Materias judiciales:**

| ID | Materia |
|---|---|
| 1 | Familiar |
| 2 | Civil |
| 3 | Mercantil Tradicional |
| 4 | Laboral |
| 6 | Mercantil Oral |
| 7 | Penal |

## Flujo de trabajo

### Paso 1 — Autenticación

1. Verificar que el MCP `CJJ` está disponible intentando `mcp__CJJ__get_user_status()`
2. Si el MCP está disponible, la autenticación es automática — continuar al Paso 2
3. Si no está disponible: informar al usuario que configure el plugin con
   `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico`
4. Si las credenciales están incompletas, el MCP retorna un error descriptivo

### Paso 2 — Determinar qué consultar

Según la solicitud del usuario:

**Modo A — Consulta de expediente específico:**
- El usuario proporciona número de expediente y juzgado
- Usar `mcp__CJJ__fetch("GET", "/expedientes/{id}")` o el endpoint equivalente
- Consultar actuaciones, acuerdos, autos y estado

**Modo B — Búsqueda por parte:**
- El usuario proporciona nombre de persona o empresa
- Usar `mcp__CJJ__fetch("GET", "/expedientes/search?party_name={nombre}")` o endpoint equivalente
- Complementar con búsqueda en boletín público:
  `mcp__CJJ__get_boletin(judged, date)` para cada juzgado mercantil ZMG

**Modo C — Consulta de catálogos:**
- `mcp__CJJ__get_all_matters()` — 7 materias judiciales
- `mcp__CJJ__get_municipalities()` — 125 municipios de Jalisco
- `mcp__CJJ__get_judicial_parties()` — 54 partidos judiciales
- Útil para validar jurisdicción y competencia antes de demandar

**Modo D — Monitoreo de expediente existente:**
- El expediente ya está en `_log.yaml` del portafolio
- Usar `mcp__CJJ__fetch("GET", "/expedientes/{id}/actuaciones")` para nuevas actuaciones
- Actualizar `history.md` del asunto

### Paso 3 — Consulta y procesamiento

Para cada expediente o resultado:
1. Obtener las actuaciones y acuerdos más recientes
2. Clasificar tipo de actuación (auto admisorio, auto de trámite, sentencia,
   emplazamiento, notificación, etc.)
3. Si hay plazos procesales derivados, calcularlos como **candidatos** usando
   las reglas del `vigilante-expedientes` agent — **nunca como plazos
   definitivos**
4. Cruzar contra el portafolio de asuntos si existe

### Paso 4 — Reporte

```
📋 Expediente [NÚMERO] — Juzgado [CLAVE] — Materia: [MATERIA]

Actor: [nombre(s)]
Demandado: [nombre(s)]
Estado: [activo / archivado / sentenciado]

📄 ACTUACIONES RECIENTES
[fecha] — [tipo] — [descripción]
[fecha] — [tipo] — [descripción]
...

⏰ PLAZOS CANDIDATOS (verificar contra autos del juzgado)
• [plazo] — vence [fecha] — fundamento: [artículo] [model knowledge — verify]

⚠️ Los plazos calculados son estimaciones basadas en el tipo de actuación.
Verificar contra los autos del juzgado y la ley procesal aplicable antes
de asentar en el sistema de control de expedientes.
```

### Paso 5 — Integración

> **¿Qué sigue?**
> 1. **Agregar al portafolio** — registrar en `_log.yaml` para monitoreo
>    automatizado
> 2. **Cronología** — alimentar las actuaciones a
>    `/litigacion-legal-mexico:chronology` para construir línea de tiempo
> 3. **Preparación de pruebas** — si el expediente está en periodo probatorio,
>    ejecutar `/litigacion-legal-mexico:preparacion-pruebas`
> 4. **Redacción de escrito** — redactar promoción en respuesta a la última
>    actuación con `/litigacion-legal-mexico:redaccion-escritos`
> 5. **Boletín** — buscar a esta parte en el boletín público con
>    `/litigacion-legal-mexico:boletin-monitor`

## Integración con vigilante-expedientes

El `vigilante-expedientes` agent usa este skill como fuente de datos para
asuntos con jurisdicción Jalisco (state-level). El agente:

1. Detecta asuntos en `_log.yaml` cuyo `jurisdiction` incluya "Jalisco",
   "CJJ", o un juzgado con clave de la ZMG
2. Para esos asuntos, usa la API de Nilo (este skill) en lugar de las
   herramientas del PJF (que son para tribunales federales)
3. Los plazos y actuaciones se integran al mismo reporte del agente

## Fuentes de datos — SCJN (federal)

Para expedientes ante tribunales federales (juzgados de distrito, tribunales
colegiados, SCJN), NO usar las APIs del CJJ. Usar:

- **LegalDataHunter MCP:** `mcp_legaldatahunter_search(query, country=["MX"],
  namespace="case_law")` — 16M+ documentos indexados incluyendo ~354K de SCJN
- **Datos Abiertos SCJN:** `https://datos.scjn.gob.mx/` — acceso público sin
  API key
- **Portal PJF / SCJN IUS / Semanario Judicial:** vía MCPs configurados en el
  plugin

**El token público (`$CJJ_NILO_PUBLIC_TOKEN`) es del CJJ (Jalisco, estatal), NO de la SCJN (federal).**

## Seguridad

- Credenciales gestionadas por el plugin via keychain del sistema — nunca en código ni en archivos
- El servidor MCP CJJ almacena el JWT solo en memoria de proceso — nunca en disco
- El JWT tiene expiración — el MCP renueva automáticamente si la sesión expira
- Las consultas automatizadas deben respetar rate limits del portal CJJ
