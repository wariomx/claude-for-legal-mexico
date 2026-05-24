---
description: >
  Prepara el acuerdo conclusivo ante PRODECON (Arts. 69-C a 69-H CFF), la queja
  por actos del SAT, o la solicitud de representación legal. Identifica si el
  acuerdo conclusivo es la vía correcta y estructura los hechos y pretensiones
  para maximizar las probabilidades de éxito.
---

# Skill: prodecon-tramite (fiscal-legal-mexico)

## Propósito

El acuerdo conclusivo es la única vía que permite al contribuyente obtener la reducción del 100% de las multas fiscales durante una auditoría activa. Pero es una decisión estratégica con riesgos: al revelar la posición jurídica del contribuyente, el SAT obtiene información que puede usar si el acuerdo fracasa. Este skill analiza si conviene iniciarlo, estructura la solicitud y prepara los hechos y pretensiones para maximizar la probabilidad de éxito.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae del módulo PRODECON: tipo de procedimiento activo, número de expediente, fase actual, acuerdo conclusivo en proceso y postura de la empresa.

### Paso 1: clasificar el procedimiento PRODECON

| Tipo | Cuándo procede | Efecto sobre la auditoría |
|---|---|---|
| Acuerdo conclusivo (Arts. 69-C a 69-H CFF) | Auditoría en curso, hechos o ley en disputa | Suspende el plazo de la auditoría mientras está en proceso [settled — last confirmed 2026-05-24] |
| Queja | Conducta del SAT excesiva, abusiva o ilegal | No suspende ni interrumpe la auditoría |
| Representación legal PRODECON | Personas físicas con ingresos bajo umbral `[model knowledge — verify umbral actual]` | PRODECON actúa como representante ante SAT y TFJA |

### Paso 2: análisis de viabilidad — acuerdo conclusivo

Antes de iniciar, evalúa los requisitos y la conveniencia:

**Requisitos de procedencia:**
1. ¿Hay una auditoría en curso al momento de la solicitud? (Si ya se emitió el acta final, el acuerdo conclusivo NO procede.) [settled — last confirmed 2026-05-24]
2. ¿Los hechos o la interpretación jurídica están genuinamente en disputa? (No procede para aceptar llanamente la observación del SAT sin discusión de fondo.)

**Beneficio principal:**
- Reducción del 100% de multas fiscales aplicadas durante la auditoría [settled — last confirmed 2026-05-24].
- Los recargos no se reducen — siguen corriendo.
- Suspende el plazo de la auditoría durante la mediación.

**Riesgos a ponderar:**
- Al presentar la solicitud, el contribuyente revela su postura jurídica y los documentos de soporte al SAT.
- Si el acuerdo fracasa, el SAT retiene toda esa información y puede usarla al emitir el crédito.
- Evaluar la fortaleza jurídica de cada punto en disputa antes de revelar la posición. `[review]`

**Comparación con litigación TFJA:**
- Acuerdo conclusivo: reduce multas, resuelve más rápido, pero implica negociación y revelación de postura.
- Litigación TFJA: sin reducción de multas automática, más largo, pero el contribuyente controla su estrategia.

### Paso 3: ⚠️ PLAZOS del procedimiento

> **⚠️ `[review: caducidad — el acuerdo conclusivo suspende el plazo de la auditoría pero no extiende la caducidad del Art. 67 CFF sobre el ejercicio revisado]`**

Plazos del procedimiento PRODECON:
- PRODECON acepta o rechaza la solicitud: 20 días hábiles `[model knowledge — verify plazos procedimentales actuales]`
- Mediación: hasta 40 días hábiles adicionales `[model knowledge — verify]`
- Durante todo ese tiempo: el plazo de la auditoría está suspendido [settled — last confirmed 2026-05-24]

### Paso 4: estructura de la solicitud de acuerdo conclusivo

```
SOLICITUD DE ACUERDO CONCLUSIVO
Ante: Procuraduría de la Defensa del Contribuyente (PRODECON)

I. IDENTIFICACIÓN DEL CONTRIBUYENTE
   Nombre / RFC / ADSC / domicilio fiscal

II. REFERENCIA A LA AUDITORÍA EN CURSO
   Número de oficio de orden de auditoría: [número]
   Tipo de revisión: [visita domiciliaria / gabinete / electrónica]
   Período revisado: [ejercicio(s)]
   Impuestos revisados: [ISR / IVA / IEPS / otro]
   Última acta parcial emitida: [fecha y número, si aplica]

III. HECHOS EN DISPUTA

   Punto 1: [descripción del hecho u operación que el SAT cuestiona]
   Posición del SAT: [cómo lo interpreta el auditor]
   Posición del contribuyente: [interpretación correcta con fundamento]
   Documentos de soporte: [lista de evidencias para este punto]
   Propuesta de resolución: [qué resuelve cada punto — aceptación parcial / ajuste de monto / interpretación jurídica]

   Punto 2: [idem]

   [Un punto por cada observación en disputa — ser específico, no hacer objecciones genéricas]

IV. FUNDAMENTO LEGAL
   [Artículos del CFF / LISR / LIVA / LIEPS que respaldan la posición del
   contribuyente para cada punto] `[model knowledge — verify]`

V. DOCUMENTOS QUE SE ACOMPAÑAN
   [Lista numerada de anexos]

VI. PRETENSIÓN
   Que PRODECON intervenga como mediador para alcanzar un acuerdo conclusivo
   conforme a los Arts. 69-C a 69-H CFF, en los términos de los puntos anteriores.
```

### Paso 5: árbol de decisión

> **¿Qué sigue?**
> 1. **Iniciar acuerdo conclusivo** — presentar la solicitud estructurada en el Paso 4 ante PRODECON.
> 2. **Esperar más información antes de decidir** — si no tienes todos los documentos de soporte, reunirlos primero.
> 3. **Optar por litigación TFJA** — si el monto de multas es pequeño o la posición jurídica es muy sólida, puede convenir más litigar.
> 4. **Interponer queja** — si el problema es la conducta del auditor, no la discrepancia de fondo.

---

**⚠️ Nota del revisor:** El acuerdo conclusivo es una decisión estratégica que requiere análisis de la fortaleza jurídica de cada punto en disputa versus el costo de la revelación de postura. No iniciar sin consulta con asesor fiscal litigador. Los plazos procedimentales de PRODECON deben verificarse contra las reglas actuales publicadas por el organismo `[model knowledge — verify]`. La reducción de multas del 100% aplica por una sola ocasión (Art. 69-H CFF) [settled — last confirmed 2026-05-24].

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
