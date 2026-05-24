# Perfil de Conectores Legal México
*Generado por cold-start el [FECHA]. Si `[PLACEHOLDER]` aparece abajo, ejecuta `/conectores-legal-mexico:cold-start-interview`.*

## Resolución de configuración

Los skills de este plugin buscan la configuración en este orden:

1. **Local (proyecto):** `.claude-legal/conectores-legal-mexico/CLAUDE.md` en el directorio de trabajo actual — para aislamiento por cliente en despachos con múltiples clientes.
2. **Global (usuario):** `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md` — fallback para uso personal o de cliente único.

**Para crear config de cliente local:** ejecuta `/conectores-legal-mexico:setup-completo --local` desde la carpeta del proyecto de ese cliente. **`.claude-legal/` debe estar en `.gitignore`** — contiene datos del cliente que no deben versionarse.

---

Este no es un perfil de práctica jurídica — es el mapa de conectividad. Registra qué MCPs están activos, dónde están las llaves, y qué comportamiento esperar de cada conector. Los otros plugins lo leen para saber si un conector está disponible antes de usarlo.

---

## Estado de conectores

| Conector | Estado | Última verificación | Notas |
|---|---|---|---|
| LegalDataHunter | [✓ / ✗ / ⚪] | [FECHA] | [API key configurada / falta API key] |
| Solve Intelligence | [✓ / ✗ / ⚪] | [FECHA] | [Sin auth requerida] |
| Slack | [✓ / ✗ / ⚪] | [FECHA] | [Canal de destino: [PLACEHOLDER]] |
| Google Drive | [✓ / ✗ / ⚪] | [FECHA] | [Carpeta raíz: [PLACEHOLDER]] |
| Box | [✓ / ✗ / ⚪] | [FECHA] | |
| iManage | [✓ / ✗ / ⚪] | [FECHA] | |
| TopCounsel | [✓ / ✗ / ⚪] | [FECHA] | |
| Definely | [✓ / ✗ / ⚪] | [FECHA] | |
| CJJ — boletín público | [✓ / ✗ / ⚪] | [FECHA] | [Sin auth] |
| CJJ — Portal Ciudadano | [✓ / ✗ / ⚪] | [FECHA] | [Credenciales: [PLACEHOLDER — configuradas / pendientes]] |
| MXLegal (STJJ) | [✓ / ✗ / ⚪] | [FECHA] | [Sin auth — 82 572 sentencias] |

**Leyenda:** ✓ verificado con llamada real · ✗ falla · ⚪ configurado, no probado

---

## Instrucciones de uso para otros plugins

### LegalDataHunter

Herramienta primaria para búsqueda de jurisprudencia (SCJN), tesis, legislación federal y estatal, DOF, resoluciones IMPI/INDAUTOR/SAT. Requiere API key.

Antes de usar: verificar que el estado es ✓. Si es ✗ o ⚪, notificar en la nota del revisor: `LegalDataHunter no conectado — citas de conocimiento del modelo, verificar antes de confiar`.

### Solve Intelligence

Para búsquedas de patentes (arte previo, FTO, análisis de reivindicaciones). No requiere auth. Usar en skills de PI cuando se necesite búsqueda de literatura patentaria.

### CJJ

- **Boletín público:** Acceso sin credenciales a juzgados mercantiles ZMG. Usar `get_boletin` para consultar nuevas actuaciones.
- **Portal Ciudadano:** Requiere login con correo/contraseña CJJ. Usar `login` primero; el token JWT dura la sesión. Si las credenciales no están configuradas, señalarlo al usuario.

### MXLegal (STJJ)

- `search_stjj(page)` — lista sentencias (15/página, 5 505 páginas).
- `get_stjj_summary(id)` — **texto legible** del resumen IA (~1-3 KB). Usar para leer y analizar.
- `get_stjj_download_url(id)` — URL de descarga del PDF. **No descarga ni lee el PDF** — solo provee la URL para que el usuario descargue manualmente si necesita el documento completo.

Al citar una sentencia STJJ, incluir siempre: número de toca, sala, fecha, holding (de `get_stjj_summary`) y URL (de `get_stjj_download_url`).

### Slack

Para publicar alertas y reportes de agentes programados (vigilante-expedientes, vigilante-renovaciones, dataroom-watcher). Si no está conectado, escribir el reporte a archivo local en lugar de publicar — nunca fallar silenciosamente.

Canal de destino: [PLACEHOLDER — completar en cold-start]

---

## Re-verificar conectividad

```
/conectores-legal-mexico:cold-start-interview --check-integrations
```

Ejecutar después de cambiar una API key, renovar un OAuth token, o ante un error inesperado de un conector.
