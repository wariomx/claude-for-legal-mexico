---
description: >
  Ajusta secciones específicas del perfil de práctica fiscal sin re-ejecutar la
  entrevista completa — actualiza régimen, agrega un asunto TFJA nuevo, cambia
  parámetros de módulos, o registra un nuevo acuerdo conclusivo PRODECON.
argument-hint: "[nombre de sección o módulo a ajustar]"
---

# Skill: customize (fiscal-legal-mexico)

## Propósito

Cuando cambia un dato del perfil de práctica —RFC actualizado, nueva auditoría activa, cambio de régimen, nuevo asunto ante el TFJA, acuerdo conclusivo recién iniciado— este skill permite actualizarlo sin re-ejecutar la entrevista completa. Lee la sección relevante, hace solo las preguntas necesarias, muestra el cambio propuesto y escribe únicamente si el usuario confirma.

## Flujo

### Paso 0: resolver ruta de configuración

Lee el perfil en este orden:
1. **Local:** `.claude-legal/fiscal-legal-mexico/CLAUDE.md` en el directorio de trabajo actual.
2. **Global:** `~/.claude/plugins/config/claude-for-legal/fiscal-legal-mexico/CLAUDE.md`.

Si no existe en ninguna ruta o contiene `[PLACEHOLDER]` generalizados: detente. Di: "Este plugin no está configurado todavía. Ejecuta `/fiscal-legal-mexico:cold-start-interview` primero."

### Paso 1: identificar la sección a ajustar

Si el argumento no especifica la sección, muestra el menú:

```
¿Qué sección quieres actualizar?

  1. Perfil de empresa / RFC
  2. Obligaciones fiscales activas
  3. Configuración CFDI (PAC, versión, tipos de comprobante)
  4. Historial SAT (carta invitación, requerimiento, auditoría activa)
  5. Módulo: CFDI Review
  6. Módulo: Discrepancias SAT
  7. Módulo: Auditorías SAT
  8. Módulo: Litigación TFJA
  9. Módulo: PRODECON
 10. Módulo: Planeación Fiscal
 11. Documentos semilla
```

Espera la selección antes de continuar.

### Paso 2: hacer solo las preguntas necesarias

Para la sección seleccionada, muestra el valor actual del campo y pregunta solo lo necesario para actualizarlo. No re-hacer preguntas de otras secciones.

Ejemplos de cambios frecuentes:

**Auditoría SAT nueva:**
- ¿Tipo de revisión? (visita domiciliaria / gabinete / electrónica / dictamen)
- ¿Número de oficio / expediente y fecha de inicio?
- ¿Período revisado e impuestos bajo revisión?
- ¿Representante legal designado?
- `[review: caducidad — verificar que el período bajo revisión esté dentro del plazo del Art. 67 CFF]`

**Nuevo asunto TFJA:**
- ¿Sala regional competente?
- ¿Número de expediente y acto impugnado?
- ¿Monto del crédito y etapa procesal actual?
- ¿Plazo procesal próximo y su fecha de vencimiento?
- `[review: caducidad — demanda de nulidad debe haberse interpuesto dentro de 30 días hábiles de la notificación — Art. 13 LFPCA]` [settled — last confirmed 2026-05-24]

**Nuevo acuerdo conclusivo PRODECON:**
- ¿Número de expediente y auditoría de origen?
- ¿Etapa actual y fecha de admisión?
- ¿Postura del contribuyente en los hechos controvertidos?

**Cambio de régimen fiscal:**
- ¿Nuevo régimen y fecha de efecto?
- ¿Nuevas obligaciones que esto genera? (cambio de periodicidad de declaraciones, nuevas declaraciones informativas)

### Paso 3: confirmar antes de escribir

Muestra el diff del cambio propuesto:

```
CAMBIO PROPUESTO
───────────────
Sección: [nombre de la sección]

ANTES:
[texto actual del campo]

DESPUÉS:
[texto nuevo propuesto]

¿Confirmas este cambio? (sí / no / ajustar)
```

Espera confirmación antes de escribir. Si el usuario dice "ajustar", permite edición libre del campo.

### Paso 4: escribir y confirmar

Escribe solo los campos modificados en la ruta activa. Confirma: "Actualizado en [ruta]. Cambio registrado el [fecha]."

---

**⚠️ Nota del revisor:** Los cambios al perfil de práctica afectan todos los outputs futuros del plugin. Si se actualizan plazos o fechas de auditoría activa, verifica que los datos coincidan con la documentación oficial del SAT o el TFJA antes de guardar. Para agregar un módulo nuevo, usa `/fiscal-legal-mexico:cold-start-interview --module [módulo]`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
