---
name: setup-cjj
description: >
  Configura y verifica el conector del Poder Judicial de Jalisco (CJJ) en tres
  capas: boletín público (sin credenciales), catálogo con token público, y
  Portal Ciudadano autenticado. Incluye árbol de diagnóstico por capa para
  resolver errores de credenciales, red o servidor. Usar en instalación nueva,
  al renovar credenciales, o cuando falle el conector CJJ en cualquier skill.
argument-hint: "[--check-integrations | --local]"
---

# /setup-cjj

El conector CJJ expone dos capacidades independientes:

- **Boletín público** — actuaciones nuevas en los 18 juzgados mercantiles de la Zona Metropolitana de Guadalajara (M01–M10, OM01–OM09). No requiere credenciales.
- **Portal Ciudadano** — acceso autenticado a expedientes completos, acuerdos y actuaciones del expediente. Requiere cuenta en nilo.cjj.gob.mx y tres credenciales: correo, contraseña y token público.

Ambas capas se verifican con llamadas reales. El árbol de diagnóstico al final de este skill permite distinguir errores de red, de token y de credenciales.

---

## Banderas

| Bandera | Comportamiento |
|---------|----------------|
| *(ninguna)* | Verificar las tres capas; guiar configuración de lo que falte. |
| `--check-integrations` | Saltar configuración interactiva; ir directo a verificación y actualizar solo las filas de CJJ en CLAUDE.md. |
| `--local` | Escribir estado en `.claude-legal/conectores-legal-mexico/CLAUDE.md` del directorio actual, no en el path global. |

---

## Paso 0 — Ruta de escritura

Determinar la ruta de CLAUDE.md según la bandera:

- **Sin `--local`:** `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md`
- **Con `--local`:** `.claude-legal/conectores-legal-mexico/CLAUDE.md` en el directorio actual.

Si se usa `--local` y el directorio no existe, crearlo. Si ya existe un CLAUDE.md en la ruta, leerlo antes de cualquier escritura — se actualizarán únicamente las dos filas de CJJ sin tocar el resto.

Si `--check-integrations`: ir directamente al Paso 1 sin mostrar presentación ni preguntar por credenciales.

---

## Paso 1 — Boletín público

El boletín no requiere credenciales — usa un endpoint distinto (`api.cjj.gob.mx/bulletin`). Esta prueba diagnostica la conectividad de red, independientemente de cualquier credencial.

Llamar:

```
mcp__CJJ__get_boletin(judged="M01", date="<fecha de hoy en formato YYYY-MM-DD>")
```

**Resultado:**

- **Responde con datos de expedientes** → ✓ Boletín público activo.
- **Error de red, timeout o 5xx** → ✗ Falla de red o servidor CJJ.
  > El servidor `api.cjj.gob.mx` no respondió. Esto no es un problema de credenciales — el boletín no requiere autenticación. Causas posibles: (1) el servidor CJJ está caído o con mantenimiento; (2) tu red bloquea el dominio `cjj.gob.mx`. Intentar de nuevo en unos minutos. Si el problema persiste, el boletín funcionará cuando el servidor se recupere — las credenciales y el Portal Ciudadano pueden configurarse igual.

Continuar al Paso 2 independientemente del resultado del boletín.

---

## Paso 2 — Token público (catálogo)

El token público es la credencial base del conector. Se usa como valor directo del encabezado `Authorization` (no como Bearer token) en todos los endpoints de catálogo y es también requerido por el flujo de login del Portal Ciudadano.

### 2a — ¿Está configurado?

Verificar si `userConfig.cjj_public_token` tiene valor.

**Si no está configurado:** ir al Paso 2b (configuración). **Si está configurado:** ir al Paso 2c (prueba).

### 2b — Configurar token público

> **El CJJ requiere un token público para acceder al catálogo de juzgados y para autenticar el Portal Ciudadano.**
>
> Para obtenerlo:
> 1. Inicia sesión en **nilo.cjj.gob.mx** con tu cuenta (o créala si no tienes).
> 2. Ubica tu token público en la sección de configuración o perfil del portal — aparece como "token" o "API token" una vez que la cuenta está activada.
> 3. Copia el token.
>
> Para guardarlo en Claude Code, ejecuta:
> ```
> claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
> ```
> Selecciona el campo **"CJJ API — token público"** e ingresa el valor.
>
> Una vez guardado, di **"listo"** y verifico la conexión.

Esperar confirmación del usuario. Luego continuar al Paso 2c.

Si el usuario no tiene cuenta en nilo.cjj.gob.mx aún:
> Para registrarte: ve a **nilo.cjj.gob.mx**, selecciona "Registrarse" o "Crear cuenta", y sigue el proceso de activación. El token estará disponible después de que la cuenta sea activada (puede tomar unas horas si requiere verificación manual).

### 2c — Verificar token público

Llamar:

```
mcp__CJJ__get_user_status()
```

**Resultado:**

- **Responde con estado del usuario** → ✓ Token público válido. Continuar al Paso 3.
- **401 / token inválido** → ✗ Token rechazado.
  > El token no fue aceptado. Verifica que copiaste el valor completo sin espacios adicionales. Para actualizar el token: `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` → campo "CJJ API — token público". Una vez actualizado, di "re-verificar token" y repito la prueba.
- **Error de red** → ✗ (usar árbol de diagnóstico al final).

---

## Paso 3 — Portal Ciudadano

El Portal Ciudadano requiere las tres credenciales: correo, contraseña y token público. El token ya fue verificado en el Paso 2 — aquí solo se prueba el par correo/contraseña.

### 3a — ¿Están configuradas las credenciales completas?

Verificar si `userConfig.cjj_email` y `userConfig.cjj_password` tienen valor (además del token ya verificado).

**Si no están configuradas:**

> **El Portal Ciudadano da acceso a expedientes completos, acuerdos y actuaciones.** Si no lo necesitas ahora, puedes configurarlo después con `/conectores-legal-mexico:setup-cjj`.
>
> ¿Quieres configurarlo ahora? (sí / no / después)

Si el usuario dice que sí o ya tiene credenciales: guiar la configuración:
> Ejecuta `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` y llena los campos **"CJJ Portal Ciudadano — correo"** y **"CJJ Portal Ciudadano — contraseña"**. Una vez guardados, di "listo" y pruebo el login.

Si el usuario pospone: marcar `⚪` Portal Ciudadano en CLAUDE.md con nota "pendiente de configurar".

### 3b — Verificar login

Llamar:

```
mcp__CJJ__login()
```

**Resultado:**

- **Regresa JWT / token de sesión** → ✓ Portal Ciudadano activo. Acceso a expedientes habilitado.
- **401 / credenciales inválidas** → ✗ Correo o contraseña incorrectos.
  > Las credenciales fueron rechazadas. El token público fue verificado en el Paso 2 — el problema es el correo o la contraseña. Verifica que la cuenta en nilo.cjj.gob.mx esté activa y que estés usando las mismas credenciales que usas para iniciar sesión en el portal web. Para actualizar: `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico`.
- **Cuenta inactiva / suspendida** → ✗ Cuenta CJJ no activa.
  > Tu cuenta en nilo.cjj.gob.mx puede requerir activación manual por parte del CJJ. Revisa si recibiste un correo de confirmación o contacta el soporte del portal.
- **Error de red** → ✗ (usar árbol de diagnóstico al final).

---

## Árbol de diagnóstico

Cuando una prueba falla, la combinación de resultados identifica la capa del problema:

| Boletín (`get_boletin`) | Token (`get_user_status`) | Login (`login`) | Diagnóstico |
|-------------------------|--------------------------|-----------------|-------------|
| ✓ | ✓ | ✓ | Todo activo |
| ✓ | ✓ | ✗ | Correo o contraseña incorrectos — token verificado, el problema es la autenticación del usuario |
| ✓ | ✗ | — | Token público inválido o faltante |
| ✗ | ✗ | — | Red o servidor CJJ — no es problema de credenciales (boletín no requiere auth) |
| ✗ | ✓ | * | Infrecuente: `api.cjj.gob.mx` caído pero `nilo.cjj.gob.mx` responde; reportar ambos estados |

---

## Actualizar CLAUDE.md

Después de completar las tres pruebas, actualizar **solo** las filas de CJJ en el CLAUDE.md en la ruta determinada en el Paso 0. No modificar ninguna otra fila ni sección.

Reemplazar únicamente estas dos filas:

```
| CJJ — boletín público | [resultado] | [fecha de hoy YYYY-MM-DD] | Sin auth |
| CJJ — Portal Ciudadano | [resultado] | [fecha de hoy YYYY-MM-DD] | [nota de credenciales] |
```

Donde:
- `[resultado]` es `✓`, `✗` o `⚪` según el resultado de la prueba.
- La nota del Portal Ciudadano es: `Credenciales configuradas` / `Credenciales pendientes` / `Cuenta inactiva — ver notas` según corresponda.

Si el CLAUDE.md no existe aún, informar al usuario que puede generarlo completo ejecutando `/conectores-legal-mexico:cold-start-interview`.

---

## Cierre

Mostrar resumen de las tres capas:

```
CJJ — resultados:

  Boletín público (get_boletin):    [✓ activo / ✗ falla de red]
  Token público (get_user_status):  [✓ válido / ✗ token inválido / ⚪ no configurado]
  Portal Ciudadano (login):         [✓ activo / ✗ credenciales incorrectas / ⚪ no configurado]
```

**Si todo está activo:** "El conector CJJ está completamente configurado. Puedes usar los skills de vigilancia de expedientes y consulta del boletín ZMG."

**Si el Portal Ciudadano es ⚪:** "El boletín está activo. Cuando quieras configurar el acceso a expedientes, ejecuta `/conectores-legal-mexico:setup-cjj` de nuevo."

**Si el boletín falla:** "El boletín del CJJ no está respondiendo — esto es un problema del servidor, no de las credenciales. Los skills que dependen de `get_boletin` fallarán hasta que el servidor se recupere."

**Para re-verificar en cualquier momento:**
```
/conectores-legal-mexico:setup-cjj --check-integrations
```
