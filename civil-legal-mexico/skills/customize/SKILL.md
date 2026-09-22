---
name: customize
description: >
  Ajusta campos puntuales del perfil de práctica civil sin re-ejecutar la
  entrevista completa: agregar o cambiar una entidad federativa, el lado
  habitual, una posición del playbook de arrendamiento, el umbral de
  escalamiento, el rol del usuario o re-verificar integraciones. Usar cuando
  el usuario diga "cambia mi entidad", "agrega Nuevo León", "actualiza mi
  playbook", "edita mi perfil" o "customize".
argument-hint: "[campo o sección a ajustar]"
---

# /customize

## Propósito

`cold-start-interview` configura todo de una vez. `customize` edita campos puntuales sin riesgo de borrar configuración existente. Para agregar un módulo completo nuevo, usar `/civil-legal-mexico:cold-start-interview --module <slug>`.

## Flujo

### Paso 0: leer configuración activa

Leer el perfil de práctica en la ruta activa (local `.claude-legal/civil-legal-mexico/CLAUDE.md` → global `~/.claude/plugins/config/claude-for-legal/civil-legal-mexico/CLAUDE.md`). Si no existe o tiene `[PLACEHOLDER]`, redirigir:

> "No encontré configuración para este plugin. Ejecuta `/civil-legal-mexico:cold-start-interview` primero."

### Paso 1: identificar qué ajustar

Si el usuario no especificó qué cambiar, mostrar los campos disponibles:

**Entidades federativas**
- Entidad principal
- Agregar o quitar una entidad adicional (crea o elimina la fila de la tabla; al agregar, marcar si el plugin tiene referencia verificada para esa entidad)
- Código procesal vigente / estatus CNPCF de una entidad (con fecha de la declaratoria si se conoce)

**Módulo Arrendamiento**
- Lado habitual
- Destinos frecuentes
- Machote de casa (ruta)
- Posición de playbook: depósito / incremento / fiador / pena por terminación anticipada / inscripción en RPP
- Umbral de escalamiento
- Activar o desactivar el registro de arrendamientos

**Configuración general**
- Perfil civil (tipo de práctica)
- Rol del usuario y contacto de abogado
- Escalamiento
- Espacios de trabajo por asunto (habilitar / deshabilitar)
- Integraciones (re-verificar)

### Paso 2: recopilar el nuevo valor

Para cada campo, preguntar el nuevo valor. Si es una lista (entidades, destinos), preguntar si reemplaza o agrega. Si es una entidad nueva, recordar: "Esta entidad [tiene / no tiene] tabla de artículos verificada en el plugin; los skills citarán con `[VERIFICAR]` hasta que exista."

### Paso 3: escribir el cambio

Actualizar SOLO el campo indicado en el `CLAUDE.md` activo. No modificar ninguna otra sección. Confirmar:

> "Actualizado: [campo] → [nuevo valor]. El resto de la configuración no cambió."

Para re-verificar integraciones: ejecutar `/civil-legal-mexico:cold-start-interview --check-integrations`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
