---
description: >
  Gestión de solicitud de derechos ARCO (Acceso, Rectificación, Cancelación,
  Oposición) — recepción, clasificación, verificación de identidad, cómputo de
  plazo hábil de respuesta (20 días hábiles desde recepción), y borrador de
  respuesta. Marca con [review: plazo ARCO] la fecha límite calculada.
argument-hint: "[--tipo acceso|rectificacion|cancelacion|oposicion]"
---

# /arco-response

## Cuándo se ejecuta

El usuario ha recibido una solicitud de derechos ARCO y necesita: (a) registrarla, calcular el plazo y redactar la respuesta; o (b) revisar una solicitud ya recibida para determinar si procede.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Ventanilla ARCO (correo, formulario, dirección física)
- Responsable de atención
- Mecanismo de verificación de identidad
- Tabla de plazos activos

Si el módulo ARCO no está activado o el perfil no existe, detenerse: "Ejecuta `/privacidad-legal-mexico:cold-start-interview` primero."

### 2. Intake de la solicitud

Preguntar (o extraer del documento compartido por el usuario):

| Campo | Valor |
|---|---|
| Folio interno | [asignar si no existe] |
| Tipo de derecho | Acceso / Rectificación / Cancelación / Oposición |
| Nombre del titular | |
| Canal de recepción | correo / formulario / físico / otro |
| **Fecha y hora de recepción** | [CAMPO CRÍTICO — ver regla dura abajo] |
| ¿Se verificó identidad del titular? | Sí / No / Parcial |
| Datos solicitados / objeto de la solicitud | |
| ¿Solicitud completa? | Sí / No — ¿qué falta? |

**REGLA DURA — Fecha de recepción:**
El plazo de 20 días hábiles corre desde la **fecha de recepción de la solicitud**, no desde que fue leída, asignada o procesada. Si la solicitud llegó por correo electrónico el lunes a las 11 PM, el plazo corre desde ese momento, no desde el martes. Si llegó por cualquier canal, se registra con fecha y hora de llegada. Un sistema de acuse de recibo automático (respuesta automática de correo con fecha y hora) es la única defensa confiable contra disputas de plazos. `[settled — last confirmed 2026-05-24]`

### 3. Clasificación del tipo de derecho

Para cada tipo de derecho, el análisis previo a la respuesta es diferente:

**Acceso (Art. 23 LFPDPPP):** El titular tiene derecho a conocer qué datos personales trata el responsable, para qué los trata, y cómo los obtuvo. La respuesta debe informar los datos en un formato inteligible. Si la cantidad de datos es grande, puede responderse en entregas.

**Rectificación (Art. 24 LFPDPPP):** El titular tiene derecho a que sus datos sean corregidos cuando son inexactos o incompletos. El responsable debe verificar los datos y corregirlos, notificando al titular. Si los datos fueron transferidos a terceros, se debe notificar la rectificación a dichos terceros. `[settled — last confirmed 2026-05-24]`

**Cancelación (Art. 25 LFPDPPP):** El titular tiene derecho a que sus datos sean suprimidos cuando ya no sean necesarios para la finalidad, el plazo de conservación haya vencido, o el consentimiento haya sido revocado. La cancelación no es inmediata — los datos pasan a un período de bloqueo antes de su eliminación definitiva. `[model knowledge — verify plazo de bloqueo aplicable]`

**Oposición (Art. 27 LFPDPPP):** El titular puede oponerse al tratamiento cuando tiene una causa legítima y la ley le permite la oposición. También aplica para oponerse a finalidades secundarias (ej., marketing directo). El responsable debe cesar el tratamiento salvo que tenga causa legítima que prevalezca. `[settled — last confirmed 2026-05-24]`

### 4. Verificación de identidad del titular

El responsable puede requerir documentos que acrediten la identidad del titular antes de proceder. Verificar conforme al mecanismo registrado en el perfil de práctica:

- ¿Se presentó identificación oficial vigente (o su equivalente digital)?
- Si actúa un representante: ¿hay poder notarial o instrumento de mandato?
- ¿Los datos de contacto del titular coinciden con los registros del responsable?

Si la solicitud es incompleta o la identidad no está acreditada, el responsable puede solicitar información adicional **dentro del plazo de respuesta** — esto no amplía el plazo; el titular tiene 10 días hábiles para completar la solicitud. `[model knowledge — verify]`

### 5. Cómputo del plazo

**Plazo de respuesta:** 20 días hábiles desde la fecha de recepción de la solicitud. `[settled — last confirmed 2026-05-24]`

**Prórroga:** el responsable puede prorrogar el plazo por 20 días hábiles adicionales, **notificando al titular antes de que venza el plazo original** y expresando la causa de la prórroga.

**Para acceso:** una vez notificada la resolución favorable, el titular tiene 15 días hábiles adicionales para recoger o recibir los datos.

**Cómputo de días hábiles:** los días inhábiles excluyen sábados, domingos y días festivos conforme al calendario oficial de la Federación (Art. 74 Ley Federal del Trabajo, aplicable por referencia) y los días que el INAI declare inhábiles en sus Lineamientos. `[model knowledge — verify calendario INAI vigente]`

Marcar la fecha límite calculada con: `[review: plazo ARCO vence AAAA-MM-DD — verificar días inhábiles aplicables]`

### 6. Análisis de procedencia

Determinar si la solicitud es:

**Procedente:** el titular tiene derecho al ejercicio solicitado y no aplica ninguna excepción legal.

**Improcedente (con causa legal):** el responsable puede negar el ejercicio cuando:
- Los datos son necesarios para cumplir una obligación legal del responsable
- Los datos son necesarios para la ejecución de un contrato con el titular
- Existe una resolución judicial o administrativa que ordena conservar los datos
- Los datos son necesarios para la defensa en un procedimiento judicial
- Los datos son parte de investigaciones en curso por organismos públicos
- La cancelación pueda causar un perjuicio a terceros
- Los datos son parte del expediente médico (para cancelación)

`[model knowledge — verify excepciones aplicables al caso concreto]`

Marcar la causa de improcedencia con `[review]` — la determinación de si una excepción aplica es un juicio jurídico.

**Información adicional requerida:** si la solicitud no contiene suficiente información para identificar los datos o el alcance, informar al titular qué documentos o información debe aportar.

### 7. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Folio:** [número de folio]
> - **Plazo vence:** `[review: AAAA-MM-DD — verificar días inhábiles]`
> - **Marcado para tu criterio:** [N elementos marcados `[review]` | ninguno]
> - **Antes de enviar la respuesta:** [las 1-2 cosas más urgentes]

### 8. Borrador de respuesta

Producir el borrador de respuesta al titular en español llano. La respuesta debe:
- Confirmar la recepción y el folio asignado
- Indicar el tipo de derecho ejercido
- Indicar si es procedente, improcedente o si se requiere información adicional
- Si es procedente: informar cómo y cuándo se cumplirá el derecho
- Si es improcedente: expresar la causa legal aplicable y los medios de impugnación disponibles (Procedimiento de Protección de Derechos ante el INAI)
- Si es con prórroga: expresar la causa y la nueva fecha límite

Marcar con `[review]` cualquier determinación que requiera criterio del abogado (ej., si una excepción legal aplica al caso concreto, si los datos son o no "necesarios" para la relación).

### 9. Actualizar el perfil de práctica

Actualizar la tabla de plazos activos en `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md` con la nueva solicitud registrada.

### 10. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Enviar la respuesta** — Revisaré el borrador una vez más y te daré la versión final para firma.
> 2. **Escalar** — Redactaré una nota de escalamiento al [responsable según el perfil] con los hechos clave y qué decisión se necesita (especialmente si la solicitud toca datos sensibles o hay una excepción legal dudosa).
> 3. **Requerir información adicional al titular** — Redactaré el escrito de requerimiento de información adicional.
> 4. **Revisar excepciones legales** — Analizo más a fondo si la excepción invocada aplica a los hechos concretos.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
