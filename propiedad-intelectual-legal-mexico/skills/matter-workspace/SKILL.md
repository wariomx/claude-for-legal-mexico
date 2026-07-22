---
name: matter-workspace
description: >
  Administra espacios aislados por asunto: resolver, crear, listar, cambiar,
  cerrar o desactivar el asunto activo. Úsalo en práctica privada multi-cliente
  y antes de cualquier trabajo sustantivo que requiera contexto de asunto.
argument-hint: "<status | new | list | switch | close | none> [slug]"
---

# /matter-workspace

Este skill administra el límite de confidencialidad entre asuntos. Las
operaciones entre carpetas se realizan exclusivamente mediante el controlador
del plugin; nunca con `find`, `mv`, `cp`, `Glob`, `Grep` o lectura directa de
otra carpeta.

## Regla de resolución obligatoria

Antes de leer o escribir datos, ejecutar exactamente:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" status
```

El resultado define estas variables lógicas para toda la ejecución:

- `PROFILE` = campo `profile`.
- `CONFIG_ROOT` = campo `config_root`; contiene configuración de práctica.
- `DATA_ROOT` = campo `data_root`; contiene datos del asunto activo o, si la
  función por asuntos está desactivada/no hay asunto, datos de práctica.
- `active` = único asunto que las herramientas sustantivas pueden leer.

La resolución es local primero: el perfil más cercano en
`.claude-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`; solo si no existe,
usa el perfil global. Cuando hay perfil local, nunca leer ni mezclar el global.

## Subcomandos seguros

Ejecutar solo uno de estos comandos exactos, después de confirmar con el
usuario cualquier operación que modifique estado:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" list
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" new <slug>
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" switch <slug>
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" close <slug>
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/matter_workspace.py" none
```

Los slugs admiten únicamente minúsculas, números y guiones. No colocar nombres
de clientes, hechos, secretos ni otra información sensible en argumentos de
shell.

### `status`

Mostrar alcance (`local`/`global`), asunto activo y `DATA_ROOT`; no mostrar
contenido confidencial. Si el perfil no existe, dirigir a `cold-start-interview`.

### `new <slug>`

1. Confirmar el slug con el usuario.
2. Ejecutar `new`. El controlador crea archivos mínimos y activa el asunto
   atómicamente antes de que se escriba cualquier dato del cliente.
3. Entrevistar: cliente, contraparte, tipo, confidencialidad, hechos clave,
   anulaciones específicas y asuntos relacionados.
4. Reemplazar `DATA_ROOT/matter.md` con la plantilla de abajo; completar
   `history.md` y `notes.md` dentro del mismo `DATA_ROOT`.
5. No leer ningún otro asunto para completar la admisión.

### `list`

Usar la salida estructurada del controlador. No enumerar `matters/` por cuenta
propia. Presentar activos y archivados en tablas separadas; el controlador solo
extrae metadatos limitados de admisión.

### `switch <slug>`

Confirmar el slug, ejecutar el controlador y después volver a ejecutar
`status`. Leer únicamente el `matter.md` dentro del nuevo `DATA_ROOT`.

### `close <slug>`

Confirmar expresamente. El controlador agrega una entrada de cierre, mueve el
directorio a `_archived` y limpia el asunto activo cuando corresponde. Archivar
no elimina. Un asunto archivado queda bloqueado para herramientas sustantivas.

### `none`

Desactiva el asunto activo y regresa a contexto de práctica. No concede permiso
para leer carpetas de asuntos. Úsalo para una auditoría agregada solo cuando el
usuario pidió explícitamente trabajo a nivel de práctica.

## Plantilla de `matter.md`

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD SEGÚN PROFILE]

# Asunto: [Cliente] — [descripción breve]

**Slug:** [slug]
**Apertura:** [AAAA-MM-DD]
**Estado:** activo
**Confidencialidad:** [estándar / reforzado / equipo-limpio]

## Partes

**Cliente:** [nombre]
**Contraparte:** [nombre(s)]

## Tipo de asunto

[tipo y una línea de alcance]

## Hechos clave

[2–5 oraciones]

## Anulaciones específicas del asunto

- [desviación respecto de la postura de práctica, o “ninguna”]

## Asuntos relacionados

- [slug y razón, sin leerlo; o “ninguno”]

## Notas sobre confidencialidad

[quién puede acceder y restricciones adicionales]
```

## Garantías y límite técnico

- El hook `PreToolUse` bloquea lectura/escritura de otro asunto, acceso al
  perfil global cuando existe uno local, registros compartidos durante un
  asunto activo y los accesos shell directos más comunes. También bloquea
  conectores de documentos/mensajería sin alcance `matter_id` verificado
  durante un asunto activo y escrituras MCP no verificadas.
- `Contexto entre asuntos` no anula este límite. Una comparación transversal
  requiere modo de práctica (`none`), petición explícita y un flujo agregado
  separado; no se habilita una lectura silenciosa desde un asunto activo.
- El hook es defensa en profundidad dentro de Claude Code, no un sustituto de
  controles del sistema operativo. Para separación ética estricta entre
  clientes, usar repositorios, cuentas y permisos del sistema separados.

## Lo que no hace

- No depura conflictos de interés.
- No elimina expedientes ni ejecuta políticas de retención.
- No permite acceso directo a archivados.
- No sincroniza sistemas de gestión de PI.
