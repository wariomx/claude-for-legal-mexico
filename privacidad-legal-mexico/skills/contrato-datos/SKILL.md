---
description: >
  Revisión o redacción de cláusulas de protección de datos en contratos —
  DPA (Data Processing Agreement), cláusulas responsable-encargado, convenios
  de transferencia internacional. Identifica cláusulas problemáticas y brechas
  ante LFPDPPP/LGPDPPSP.
argument-hint: "[--tipo dpa|transferencia|revision]"
---

# /contrato-datos

## Cuándo se ejecuta

El usuario necesita: (a) revisar un contrato existente para identificar brechas de protección de datos; (b) redactar un DPA o cláusulas de encargado desde cero; o (c) revisar o redactar cláusulas para transferencias internacionales de datos.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público)
- Tipos de datos personales tratados (especialmente si hay sensibles o de menores)
- Módulo de Transferencias Internacionales activo
- DPA modelo existente (si está en Documentos semilla)

Si el perfil no existe o contiene `[PLACEHOLDER]`, detenerse: "Ejecuta `/privacidad-legal-mexico:cold-start-interview` primero."

### 2. Determinar el modo

**Modo revisión (`--tipo revision` o el usuario comparte un contrato existente):**
- Leer el contrato proporcionado.
- Ejecutar el checklist de cláusulas de DPA / transferencia (ver abajo).
- Producir tabla de hallazgos con severidad y marcado de cláusulas problemáticas.

**Modo redacción (`--tipo dpa` o `--tipo transferencia`):**
- Preguntar: "¿Para qué tipo de servicio es el contrato? ¿Qué datos personales tratará el encargado? ¿Los datos serán transferidos fuera de México?"
- Redactar las cláusulas o el DPA completo con todos los elementos requeridos, marcando con `[review]` cualquier elemento que dependa de información no disponible.

### 3. Checklist de DPA (contrato responsable-encargado)

El Reglamento de la LFPDPPP (Arts. 50-53) establece que el contrato con el encargado debe incluir: `[settled — last confirmed 2026-05-24]`

| # | Elemento | Presente | Severidad si ausente | Notas |
|---|---|---|---|---|
| 1 | Identificación de las partes (responsable y encargado) | | 🔴 | |
| 2 | Descripción de los datos personales objeto del tratamiento | | 🔴 | |
| 3 | Finalidades del tratamiento por el encargado | | 🔴 | |
| 4 | Obligación del encargado de tratar solo conforme a instrucciones del responsable | | 🔴 | |
| 5 | Obligación de confidencialidad del encargado y su personal | | 🔴 | |
| 6 | Medidas de seguridad a implementar por el encargado | | 🔴 | |
| 7 | Prohibición de subcontratar sin autorización del responsable (o condiciones para hacerlo) | | 🟠 | |
| 8 | Obligación de notificar vulneraciones de seguridad al responsable (y plazo) | | 🔴 | |
| 9 | Obligación de devolver o destruir los datos al término del contrato | | 🟠 | |
| 10 | Derechos de auditoría del responsable | | 🟡 | |
| 11 | Duración del tratamiento | | 🟠 | |
| 12 | Destino de los datos al vencimiento del contrato | | 🟠 | |

**Cláusulas problemáticas a identificar y señalar automáticamente como 🔴:**
- Cláusulas que pretendan que el encargado es "co-responsable" sin claridad sobre las obligaciones específicas de cada parte — la ambigüedad puede crear responsabilidad no deseada para el responsable.
- Cláusulas que autoricen al encargado a usar los datos para finalidades propias (ej., mejorar sus modelos de IA, vender datos a terceros) — esto convierte al encargado en responsable sin el consentimiento del titular, lo que es una violación a la LFPDPPP.
- Cláusulas de limitación de responsabilidad que pretendan eximir al encargado de toda responsabilidad por vulneraciones de seguridad — el responsable sigue siendo responsable ante los titulares aunque el encargado haya causado la vulneración.
- Cláusulas que renuncien a los derechos de auditoría del responsable — el responsable tiene la obligación de verificar que el encargado cumple con la ley.
- Ausencia de plazo de respuesta del encargado ante vulneraciones — sin plazo, el encargado puede demorar la notificación, impidiendo que el responsable cumpla su plazo de 72 horas ante el INAI.

### 4. Checklist de cláusulas de transferencia internacional

Para transferencias de datos personales fuera de México, verificar la base legal y los elementos contractuales:

**Base legal (Art. 37 LFPDPPP):** `[settled — last confirmed 2026-05-24]`

| # | Base legal disponible | Aplica | Elementos requeridos |
|---|---|---|---|
| 1 | Consentimiento expreso del titular | | El titular consintió la transferencia internacional en el aviso de privacidad o en forma separada |
| 2 | Tratado o acuerdo del que México forme parte | | Identificar el tratado y verificar que aplica a esta transferencia |
| 3 | La transferencia es necesaria para el cumplimiento de un contrato entre el responsable y el titular | | El contrato con el titular debe haber requerido la transferencia |
| 4 | La transferencia es necesaria para la ejecución de un contrato entre el responsable y un tercero, en interés del titular | | El interés del titular debe ser claro |
| 5 | La transferencia es necesaria para la prevención o diagnóstico médico, salud, asistencia social | | Solo para datos de salud |
| 6 | La transferencia la requiere una autoridad pública competente | | Acreditar la solicitud de la autoridad |
| 7 | La transferencia es a una sociedad controladora, subsidiaria o afiliada bajo el control común del responsable | | Verificar la relación corporativa y que el nivel de protección sea equivalente |

**Nota:** México no ha publicado lista de países con nivel adecuado de protección a la fecha. En la práctica, las transferencias internacionales requieren consentimiento expreso del titular o cláusulas contractuales como mecanismo habitual. `[model knowledge — verify estado actual]`

**Elementos de las cláusulas de transferencia internacional:**

| # | Elemento | Presente | Severidad si ausente |
|---|---|---|---|
| 1 | Identificación del destinatario y su jurisdicción | | 🔴 |
| 2 | Base legal de la transferencia | | 🔴 |
| 3 | Finalidades del tratamiento por el destinatario | | 🔴 |
| 4 | Obligación del destinatario de tratar con nivel de protección equivalente a la LFPDPPP | | 🔴 |
| 5 | Obligación de confidencialidad | | 🔴 |
| 6 | Medidas de seguridad aplicables | | 🔴 |
| 7 | Restricción de sub-transferencias sin autorización | | 🟠 |
| 8 | Obligación de notificación de vulneraciones | | 🔴 |
| 9 | Mecanismo de resolución de disputas | | 🟡 |
| 10 | Ley aplicable y jurisdicción | | 🟠 |

### 5. Análisis de cláusulas de limitación de responsabilidad

Identificar y marcar con `[review]` toda cláusula que limite la responsabilidad del encargado o del destinatario de una transferencia, evaluando:
- ¿La limitación es razonable o pretende eximir de responsabilidad por negligencia grave o dolo?
- ¿La limitación crea un riesgo de que el responsable no pueda recuperar daños frente al encargado si ocurre una vulneración?
- ¿La limitación es incompatible con las obligaciones del responsable ante el INAI y los titulares?

Un responsable que firma un DPA con limitación de responsabilidad a $0 por vulneraciones sigue siendo responsable ante el INAI y los titulares por el daño causado. La cláusula limita su recuperación contra el encargado, no su exposición regulatoria. Señalarlo explícitamente.

### 6. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Tipo de contrato analizado:** [DPA / transferencia internacional / revisión general]
> - **Hallazgos:** [N] — 🔴 [N] críticos / 🟠 [N] altos / 🟡 [N] medios
> - **Marcado para tu criterio:** [N elementos marcados `[review]`]
> - **Antes de firmar:** [las 1-2 cláusulas más urgentes a resolver]

### 7. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Redactar cláusulas correctivas** — Produciré el texto de reemplazo para las cláusulas problemáticas identificadas, listo para negociación.
> 2. **Redactar DPA completo** — Si no existe un DPA, redactaré uno desde cero con todos los elementos requeridos.
> 3. **Escalar** — Redactaré una nota de escalamiento con las brechas críticas y qué decisión de negociación se necesita.
> 4. **Revisar las cláusulas de limitación de responsabilidad** — Análisis más profundo del riesgo que crean para el responsable frente al INAI.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
