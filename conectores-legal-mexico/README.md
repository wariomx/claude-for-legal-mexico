# conectores-legal-mexico

Infraestructura MCP compartida para los plugins de derecho mexicano. Conecta LegalDataHunter, Solve Intelligence, Slack, Google Drive, Box, iManage, TopCounsel, Definely, CJJ (Poder Judicial de Jalisco) y STJJ (Supremo Tribunal de Justicia de Jalisco) a los flujos de trabajo de los otros plugins.

## Por qué existe este plugin

Los cuatro plugins mexicanos (`corporativo-legal-mexico`, `litigacion-legal-mexico`, `propiedad-intelectual-legal-mexico`, y el que uses en el futuro) necesitan los mismos conectores. En lugar de pedirte que configures LegalDataHunter cuatro veces, este plugin los centraliza: configurar una vez, usar en todos.

## Servidores incluidos

### Servidores HTTP (sin instalación)

| Conector | Qué hace | Auth |
|---|---|---|
| **LegalDataHunter** | 16M+ documentos jurídicos mexicanos — SCJN, DOF, IMPI, INDAUTOR, SAT, legislación federal y estatal | API key (`legaldatahunter_api_key` en userConfig) |
| **Solve Intelligence** | Literatura patentaria, estándares SEP, análisis de reivindicaciones | Sin auth |
| **Slack** | Búsqueda de mensajes, lectura de canales | OAuth (autoriza en `/mcp`) |
| **Google Drive** | Búsqueda y lectura de documentos | OAuth (autoriza en `/mcp`) |
| **Box** | Gestión documental, VDR | OAuth (autoriza en `/mcp`) |
| **iManage** | Contenido gobernado de despachos | OAuth (autoriza en `/mcp`) |
| **TopCounsel** | Recomendaciones de despachos externos | Sin auth |
| **Definely** | Navegación estructural de contratos, definiciones, referencias cruzadas | OAuth (autoriza en `/mcp`) |

### Servidores stdio (incluidos, cero dependencias externas)

| Servidor | Qué hace | Auth |
|---|---|---|
| **CJJ** | Boletín judicial público y Portal Ciudadano del Consejo de la Judicatura de Jalisco — expedientes, actuaciones, acuerdos | Boletín: sin auth. Portal Ciudadano: credenciales CJJ |
| **MXLegal** | 82 572 sentencias públicas del Supremo Tribunal de Justicia de Jalisco (STJJ) | Sin auth |

## Configuración rápida

### 1. LegalDataHunter (fuentes jurídicas federales y estatales)

```bash
# La API key se guarda en userConfig (keychain del sistema)
# En Claude Code: /plugin settings → conectores-legal-mexico → legaldatahunter_api_key
```

O ejecutar `/conectores-legal-mexico:cold-start-interview` — el skill te guía paso a paso.

### 2. CJJ (expedientes del Poder Judicial de Jalisco)

El boletín público funciona sin credenciales. Para el Portal Ciudadano (expedientes completos):

```bash
# Registrarse en: https://nilo.cjj.gob.mx
# Guardar correo, contraseña y token público vía:
# /plugin settings → conectores-legal-mexico → cjj_email / cjj_password / cjj_public_token
```

### 3. MCPs HTTP con OAuth

Slack, Google Drive, Box, iManage y Definely usan OAuth. Una vez que el `.mcp.json` está cargado:

```
/mcp   →   seleccionar el conector   →   autenticar
```

### 4. Verificar conectividad

```
/conectores-legal-mexico:cold-start-interview --check-integrations
```

Prueba cada conector con una llamada real y reporta ✓ / ✗ / ⚪ (configurado pero no probado).

## Dependencia

Este plugin es una dependencia de:

- `corporativo-legal-mexico`
- `litigacion-legal-mexico`
- `propiedad-intelectual-legal-mexico`

Si instalas cualquiera de los tres, este plugin ya está incluido. No necesitas instalarlo por separado.

## Licencia

PolyForm Noncommercial 1.0.0 — uso académico, no-profit y gobierno es libre. Uso comercial: contactar wario@soft.law.
