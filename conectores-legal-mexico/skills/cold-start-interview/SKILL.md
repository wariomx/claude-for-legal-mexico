---
name: cold-start-interview
description: >
  Configuración inicial de conectores — verifica conectividad de cada MCP con
  una llamada real, guía la configuración de LegalDataHunter API key y
  credenciales CJJ, y escribe el mapa de conectividad CLAUDE.md. Usar en
  instalación nueva, cuando falle un conector, o para re-verificar integraciones.
argument-hint: "[--check-integrations | --local]"
---

## Bandera --local

Si se invoca con `--local`:

1. **Ruta de escritura:** `.claude-legal/conectores-legal-mexico/CLAUDE.md` en el directorio de trabajo actual, en vez del path global.
2. **Crear directorio:** crear `.claude-legal/conectores-legal-mexico/` si no existe.
3. **`.gitignore`:** si existe un `.gitignore` en el directorio actual y no contiene `.claude-legal/`, agregar esa línea automáticamente y notificar: "Agregué `.claude-legal/` a tu `.gitignore`."
4. **Sobrescribir:** si ya existe `.claude-legal/conectores-legal-mexico/CLAUDE.md`, preguntar antes de sobrescribir.
5. **Confirmación al terminar:** "✓ Config de conectores escrita en `.claude-legal/conectores-legal-mexico/CLAUDE.md`. Esta carpeta usa su propio mapa de conectividad."

Útil cuando distintos proyectos de cliente usan diferentes conectores o API keys.

---

# /cold-start-interview

1. Verificar `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md`. Si ya está poblado y no hay `--redo` ni `--check-integrations`, preguntar antes de sobrescribir.
2. Si `--check-integrations`: ir directo al paso 4 (verificación de conectividad) sin preguntas adicionales. Actualizar solo la tabla de estado y la fecha de última verificación. No sobrescribir el resto del CLAUDE.md.
3. Si primera ejecución o `--redo`: dar bienvenida breve y continuar.
4. Verificar cada conector con una llamada real. Reportar ✓ / ✗ / ⚪ honestamente.
5. Guiar la configuración de los conectores que fallan o no están configurados.
6. Escribir `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md`.
7. Confirmar con el usuario y dar instrucciones para los conectores que requieren pasos manuales.

---

## Bienvenida (primera ejecución)

> **Este plugin centraliza los conectores MCP para todos los plugins de derecho mexicano.** Configura una vez, funciona en corporativo, litigación y PI.
>
> El proceso toma 3-5 minutos. Verificaré cada conector con una llamada real — no asumo que está conectado solo porque está en la configuración. Al final tendrás un mapa claro de qué funciona y qué necesita atención.

---

## Paso 1: LegalDataHunter

LegalDataHunter es la fuente primaria de jurisprudencia (SCJN), tesis, DOF, legislación federal y estatal, y resoluciones IMPI/INDAUTOR. La mayoría de los skills de investigación lo usan.

**Verificar si la API key ya está configurada:**
- Si `user_config.legaldatahunter_api_key` existe: intentar una búsqueda de prueba (`mcp__LegalDataHunter__search` o equivalente con query "prueba"). Si responde → ✓. Si falla → ✗ con el error.
- Si no existe: indicar cómo obtenerla y cómo configurarla.

**Si no está configurada o falla:**

> **LegalDataHunter requiere una API key.** Para obtenerla:
> 1. Regístrate en legaldatahunter.com
> 2. En Claude Code: escribe `/plugin settings` → selecciona `conectores-legal-mexico` → ingresa la key en `LegalDataHunter API key`
> 3. La key se guarda en el keychain del sistema — no en texto plano.
>
> Una vez configurada, di "verificar LegalDataHunter" y re-pruebo.

Si el usuario proporciona la key durante esta conversación, intentar la llamada de prueba inmediatamente.

---

## Paso 2: CJJ (Poder Judicial de Jalisco)

El CJJ tiene dos capas:

### Boletín público (sin auth)

Intentar `mcp__CJJ__get_boletin` o la herramienta equivalente del servidor CJJ. Si responde con datos de expedientes → ✓. Si falla → ✗ con el error (puede ser problema de conectividad de red o del servidor del CJJ).

### Portal Ciudadano (requiere credenciales)

**Verificar si las credenciales están configuradas:**
- `cjj_email`, `cjj_password`, `cjj_public_token` en userConfig.

**Si no están configuradas:**

> **El Portal Ciudadano del CJJ da acceso a expedientes completos, actuaciones y acuerdos.** Para configurarlo:
> 1. Regístrate en: **nilo.cjj.gob.mx** (si no tienes cuenta)
> 2. En Claude Code: `/plugin settings` → `conectores-legal-mexico` → llena `CJJ Portal Ciudadano — correo`, `contraseña` y `token público`
> 3. El token público se obtiene en el portal después de activar tu cuenta.
>
> ¿Ya tienes cuenta? Di "tengo credenciales" y te guío para ingresarlas.

**Si están configuradas:** intentar `mcp__CJJ__login` con las credenciales. Si regresa JWT → ✓ Portal Ciudadano activo. Si falla → ✗ con el error (credenciales incorrectas, cuenta inactiva, o el servidor del CJJ no responde).

---

## Paso 3: MXLegal (STJJ)

El servidor MXLegal no requiere auth. Intentar `mcp__MXLegal__search_stjj` con `page=1`. Si regresa datos de tocas → ✓. Si falla → ✗ (problema de red o del servidor STJJ).

Este es un servidor stdio local — si falla, el problema más probable es que Node.js no está instalado o la ruta del servidor es incorrecta. Reportar el error exacto.

---

## Paso 4: MCPs HTTP con OAuth

Los siguientes conectores requieren autorización OAuth del usuario. No se pueden probar automáticamente sin que el usuario haya autorizado — reportar ⚪ si no hay evidencia de autorización previa, y dar instrucciones.

Para cada uno:

**Slack:**
> Para autorizar Slack: `/mcp` → selecciona "Slack" → sigue el flujo de autorización. Una vez autorizado, di "verificar Slack" y confirmo.

**Google Drive:**
> Para autorizar Google Drive: `/mcp` → selecciona "Google Drive" → autoriza con tu cuenta de Google.

**Box:**
> Para autorizar Box: `/mcp` → selecciona "Box" → autoriza con tu cuenta de Box.

**iManage:**
> Para autorizar iManage: `/mcp` → selecciona "iManage" → authoriza con tus credenciales de iManage Cloud.

**Definely:**
> Para autorizar Definely: `/mcp` → selecciona "Definely" → autoriza con tu cuenta de Definely.

Si el usuario confirma que autorizó alguno, intentar una llamada de prueba (búsqueda simple) y marcar ✓ o ✗ según el resultado.

**TopCounsel y Solve Intelligence** no requieren auth — intentar una llamada de prueba directamente.

---

## Paso 5: Configuración de Slack para alertas

Si Slack está ✓, preguntar:

> ¿En qué canal de Slack deben publicarse las alertas de los agentes (vigilante-expedientes, vigilante-renovaciones, dataroom-watcher)?
>
> Formato: `#nombre-del-canal` o `@usuario` para mensajes directos.

Guardar el canal en el CLAUDE.md bajo `Canal de destino`.

---

## Escribir el CLAUDE.md

Después de verificar todos los conectores, escribir:
`~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md`

Usando la plantilla en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`, completar:
- Tabla de estado con ✓ / ✗ / ⚪ y fecha de hoy para cada conector
- Canal de Slack (si se configuró)
- Notas de conectividad para cada conector que falló

Fechar el encabezado del archivo con la fecha de hoy.

---

## Cierre

Mostrar resumen:

```
✓ Conectores activos: [lista]
✗ Fallaron: [lista con el problema específico]
⚪ No probados (requieren OAuth manual): [lista]

Para los conectores que fallaron:
[instrucción específica por conector]

Para re-verificar en cualquier momento:
/conectores-legal-mexico:cold-start-interview --check-integrations
```

Si todo está ✓: "Todos los conectores activos. Los plugins de derecho mexicano están listos para usar investigación jurídica conectada."

---

## Banderas

- `--check-integrations` — re-verificar conectividad sin re-hacer la entrevista. Actualiza solo la tabla de estado en CLAUDE.md.
- `--redo` — re-ejecutar la entrevista completa y sobrescribir CLAUDE.md.
