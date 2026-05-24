---
name: customize
description: >
  Ajusta la configuración de conectores sin re-ejecutar la entrevista completa —
  cambia el canal de Slack de alertas, actualiza una API key, activa o desactiva
  un conector específico, o añade notas de conectividad. Usar cuando un conector
  cambie de estado, cuando renueves credenciales, o cuando quieras ajustar el
  comportamiento de un conector específico sin tocar el resto.
argument-hint: "[nombre del conector o ajuste específico]"
---

# /customize

1. Leer `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md`. Si no existe, dirigir a `/conectores-legal-mexico:cold-start-interview`.
2. Identificar qué ajuste quiere el usuario (ver opciones abajo).
3. Si el ajuste requiere re-verificar conectividad, hacerlo con una llamada real.
4. Actualizar CLAUDE.md con el cambio específico. No modificar lo que no se pidió cambiar.
5. Confirmar el cambio con el usuario.

---

## Ajustes disponibles

### Cambiar canal de Slack para alertas

> "Cambia el canal de Slack a #litigacion-jalisco"

Actualizar la línea `Canal de destino` en CLAUDE.md. Si Slack está ✓, verificar que el canal existe y el bot tiene acceso.

### Actualizar una API key

> "Actualicé mi API key de LegalDataHunter"

Re-verificar el conector con una llamada de prueba. Actualizar estado y fecha en la tabla. No pedir la key nueva — se configura en `/plugin settings`.

### Marcar un conector como no disponible

> "Ya no uso Box, márcalo como no disponible"

Actualizar el estado a ✗ y añadir nota en la tabla. Los skills que intenten usar ese conector reportarán "no conectado" en la nota del revisor.

### Re-verificar un conector específico

> "Verifica si LegalDataHunter está respondiendo"

Hacer la llamada de prueba. Actualizar estado y fecha. Reportar el resultado.

### Añadir nota de conectividad

> "El CJJ está caído esta semana, anótalo"

Añadir nota en la columna "Notas" del conector afectado con la fecha. Los skills leen estas notas para saber si un conector tiene un problema temporal conocido.

---

## Regla de modificación mínima

Este skill modifica **solo lo que se pidió cambiar**. El resto del CLAUDE.md queda intacto — incluidas las fechas de verificación de otros conectores, el canal de Slack, y las notas existentes. Nunca sobrescribir la tabla completa para cambiar un solo campo.
