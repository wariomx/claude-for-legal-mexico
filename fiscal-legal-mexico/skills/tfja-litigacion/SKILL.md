---
description: >
  Prepara la demanda de nulidad ante el TFJA, la contestación, el amparo fiscal
  (Ley de Amparo Arts. 170-171), y los recursos del contencioso administrativo
  fiscal. Calcula plazos, identifica causales de nulidad, y estructura los
  conceptos de impugnación.
---

# Skill: tfja-litigacion (fiscal-legal-mexico)

## Propósito

La demanda de nulidad ante el TFJA es la primera línea de defensa contra un crédito fiscal firme. Un error en el plazo o en la estructura de los conceptos de impugnación puede cerrar la puerta a la defensa antes de que empiece. Este skill calcula el plazo exacto, identifica las causales de nulidad aplicables al acto concreto y genera el esquema de demanda con conceptos numerados listos para revisión del asesor litigador.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae del módulo TFJA: sala regional competente, expediente activo, acto impugnado, etapa procesal actual, plazos activos y estrategia de defensa.

### Paso 1: ⚠️ PLAZO — mostrar primero

> **⚠️ `[review: caducidad — demanda de nulidad vence AAAA-MM-DD]`**
> Notificación del acto: [fecha]
> Plazo: 30 días hábiles (Art. 13 LFPCA) [settled — last confirmed 2026-05-24]
> Días hábiles restantes a partir de hoy ([fecha actual]): [N]
> Sala competente: [Sala Regional según domicilio fiscal del contribuyente]

Si el plazo ya venció: advertir y analizar si procede amparo indirecto o si existe causa de fuerza mayor que justifique reposición del plazo `[review]`.

### Paso 2: identificar la vía procesal

| Criterio | Vía sumaria (Art. 58-1 LFPCA) | Vía ordinaria |
|---|---|---|
| Monto | Hasta 15 veces el valor anual de la UMA `[model knowledge — verify monto actual]` | Mayor al umbral |
| Plazo de resolución | Más breve | Estándar |
| Recursos disponibles | Limitados | Completos |
| Recomendación | Para créditos pequeños y defectos formales claros | Para casos de fondo o monto material |

### Paso 3: identificar causales de nulidad

Revisa el acto impugnado contra cada causal del Art. 51 LFPCA:

| Causal | Descripción | ¿Aplica al caso? | Tipo de nulidad |
|---|---|---|---|
| Frac. I | Incompetencia de la autoridad que dictó el acto | `[review]` | Lisa y llana |
| Frac. II | Omisión de formalidades esenciales del procedimiento | `[review]` | Para efectos |
| Frac. III | Vicios del procedimiento que afectaron defensas | `[review]` | Para efectos |
| Frac. IV | Ilegalidad de la resolución (base legal / fáctica incorrecta) | `[review]` | Lisa y llana |
| Frac. V | Omisión de requisitos formales en el acto | `[review]` | Para efectos |

Para cada causal aplicable, identifica: el defecto específico, el precepto violado y si la nulidad es lisa y llana (no puede emitirse nuevo acto) o para efectos (la autoridad puede subsanar).

### Paso 4: estructura de la demanda de nulidad

Genera el esquema con los elementos del Art. 14 LFPCA:

```
DEMANDA DE NULIDAD
Ante: Sala Regional del TFJA [nombre y domicilio]

I. ACTOR
   Nombre / RFC / domicilio para oír y recibir notificaciones

II. AUTORIDAD DEMANDADA
   [Administración SAT que emitió el acto / ADSC]

III. ACTO IMPUGNADO
   [Descripción precisa: resolución, fecha, número de oficio, monto]

IV. FECHA DE NOTIFICACIÓN
   [Fecha en que surtió efectos la notificación — base para cómputo del plazo]

V. VALOR EN CONTROVERSIA
   [Monto total del crédito: contribuciones + recargos + multas]

VI. CONCEPTOS DE IMPUGNACIÓN

   PRIMERO. [Causal Art. 51 frac. X LFPCA — Incompetencia / vicios formales]
   Argumento: [desarrollo del argumento]
   Fundamento: [artículos aplicables]
   Pruebas: [documentos que lo acreditan]
   Petición: Nulidad [lisa y llana / para efectos]

   SEGUNDO. [Causal de fondo — ilegalidad de la determinación]
   Argumento: [desarrollo]
   Fundamento: [CFF, LISR, LIVA, tesis aplicables `[model knowledge — verify]`]
   Pruebas: [documentos]
   Petición: Nulidad lisa y llana

   [Numeración continua para cada argumento adicional]

VII. PRUEBAS
   [Lista numerada de todos los documentos que se ofrecen]

VIII. INCIDENTE DE SUSPENSIÓN
   [Si se solicita suspensión de cobro: indicar garantía o razones para no garantizar]
```

### Paso 5: incidente de suspensión y amparo

**Incidente de suspensión:** para detener el cobro del crédito mientras se litiga. Requiere garantía equivalente al crédito (fianza, depósito en institución autorizada) o demostrar que el cobro causaría daño de difícil reparación `[review]`.

**Amparo directo (Art. 170 Ley de Amparo):** procede contra la sentencia definitiva del TFJA.
- Plazo: 15 días hábiles desde notificación de la sentencia [settled].
- Conceptos de violación difieren de las causales de nulidad TFJA — se argumenta violación a garantías constitucionales y/o convencionales `[review]`.

**Amparo indirecto (Art. 107 frac. III Ley de Amparo):** puede proceder contra actos dentro del procedimiento contencioso que sean de imposible reparación `[review]`.

---

**⚠️ Nota del revisor:** La litigación ante el TFJA requiere asesor especializado en contencioso fiscal. Este skill produce el esquema estructural, el análisis de causales y el cómputo de plazos — no un escrito listo para presentar. Los conceptos de impugnación deben desarrollarse con base en el expediente completo y la jurisprudencia del TFJA y la SCJN vigente al momento de la demanda `[model knowledge — verify jurisprudencia aplicable]`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
