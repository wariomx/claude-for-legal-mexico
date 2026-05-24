---
description: >
  Identifica opciones de planeación fiscal lícita — estructuras societarias,
  regímenes especiales, tratados de doble imposición, diferimiento de ingresos,
  deducciones permitidas — con análisis de riesgo de recaracterización
  (simulación, fraude a la ley, sustancia económica).
---

# Skill: planeacion-fiscal (fiscal-legal-mexico)

## Propósito

La planeación fiscal lícita reduce la carga tributaria dentro del marco legal vigente. La línea entre planeación lícita y elusión (con riesgo de recaracterización) no siempre es clara, y el Art. 5 CFF da al SAT amplias facultades para desconocer estructuras sin sustancia económica. Este skill analiza las opciones de planeación disponibles para el perfil del cliente, evalúa el riesgo de cada una y genera la matriz de decisión para que el asesor fiscal elija con información completa.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae del módulo Planeación Fiscal: estructura corporativa actual, jurisdicciones de operación, tratados de doble imposición aplicables, régimen fiscal, tasa efectiva actual, sector económico y postura ante planeación agresiva.

### Paso 1: delimitar el alcance

Confirma con el usuario qué áreas de planeación quiere analizar:

```
¿Qué áreas de planeación fiscal quieres explorar?

  1. Optimización de régimen fiscal (RESICO / régimen general / maquiladora / AGAPE)
  2. Estructura corporativa (holding, series de acciones, fideicomiso, SAPI, SA vs. SRL)
  3. Tratados de doble imposición (operaciones internacionales o con partes relacionadas en el extranjero)
  4. Diferimiento de ingresos (ventas en parcialidades, fideicomisos de distribución diferida, opciones sobre acciones)
  5. Deducciones frecuentemente omitidas (PTU acumulada, pensiones, I+D — Art. 189 LISR)
  6. Repatriación de dividendos y cuentas CUFIN
  7. Precios de transferencia y documentación contemporánea (Art. 76 frac. IX LISR)
```

Para cada área seleccionada, realiza el análisis del Paso 2.

### Paso 2: análisis por área

**1. Optimización de régimen:**
- Compara la carga fiscal efectiva bajo el régimen actual vs. los regímenes alternativos aplicables al tipo de actividad `[model knowledge — verify tasas y umbrales vigentes en LISR y RMF]`.
- Identifica si el cambio de régimen genera obligaciones de aviso ante el SAT.

**2. Estructura corporativa:**
- Evalúa la conveniencia de holding para separar activos, dividir riesgos o facilitar M&A.
- Analiza el tratamiento fiscal de SA de CV vs. SRL de CV vs. SAPI para el perfil específico `[model knowledge — verify tratamiento LISR actual]`.
- Fideicomisos: verifica si el fideicomiso tiene consecuencias de transparencia fiscal o retención.

**3. Tratados de doble imposición:**
- Identifica el tratado aplicable para cada jurisdicción de operación. México tiene más de 60 tratados vigentes `[model knowledge — verify lista actualizada en SAT y DOF]`.
- Para cada tratado relevante: verifica tasas de retención reducidas para dividendos, intereses, regalías y ganancias de capital.
- Advierte sobre los requisitos de sustancia económica en la jurisdicción del beneficiario para acceder a los beneficios del tratado (Anti-BEPS) `[review]`.

**4. Diferimiento de ingresos:**
- Ventas en parcialidades: el ingreso se acumula conforme se cobra (personas morales) `[model knowledge — verify regla actual LISR]`.
- Evalúa si el diferimiento tiene sentido dado el perfil de flujo de caja del cliente.

**5. Deducciones frecuentemente omitidas:**
- PTU deducida: solo la efectivamente pagada en el ejercicio (Art. 27 frac. VIII LISR) `[model knowledge — verify]`.
- Aportaciones a fondos de pensiones y jubilaciones.
- Gastos de I+D: deducción adicional del Art. 189 LISR `[model knowledge — verify porcentaje y límites vigentes]`.
- Identificar cualquier deducción inmediata de inversiones aplicable al sector.

**6. Dividendos y CUFIN:**
- Verifica el saldo de la Cuenta de Utilidad Fiscal Neta (CUFIN).
- Dividendos pagados de CUFIN: sin impuesto adicional [settled — last confirmed 2026-05-24].
- Dividendos fuera de CUFIN: impuesto adicional del 10% (Art. 10 LISR) [settled — last confirmed 2026-05-24] `[review: confirmar tasa vigente]`.

**7. Precios de transferencia:**
- ¿El cliente realiza operaciones entre partes relacionadas nacionales o internacionales?
- Requisito de documentación contemporánea: Art. 76 frac. IX LISR [settled — last confirmed 2026-05-24].
- Identifica si se requiere estudio de precios de transferencia para el ejercicio en curso.

### Paso 3: evaluación de riesgo de recaracterización

Para cada opción analizada, evalúa el riesgo conforme al Art. 5 CFF (cláusula anti-abuso de sustancia económica):

| Opción | Propósito de negocio | Sustancia económica real | Riesgo de recaracterización | Nivel |
|---|---|---|---|---|
| [Opción 1] | [sí / parcial / no] | [sí / parcial / no] | [descripción del riesgo] | 🔴 / 🟠 / 🟡 / 🟢 |

**Criterio de recaracterización:** una estructura cuyo principal o único propósito sea el ahorro fiscal, sin sustancia económica real (activos, personal, función de negocio genuina), está en riesgo de ser desconocida por el SAT bajo el Art. 5 CFF [settled — last confirmed 2026-05-24].

**Revelación de esquemas reportables:** si la opción califica como esquema reportable bajo los Arts. 197-202 CFF, indicarlo y asesorar sobre la obligación de revelar. `[review]`

### Paso 4: matriz de opciones

```
MATRIZ DE PLANEACIÓN FISCAL — [Nombre del cliente / RFC]
Fecha del análisis: [fecha] | Ley vigente: LISR/LIVA/CFF [ejercicio]
[model knowledge — verify cambios del Paquete Económico más reciente]

| Opción | Ahorro estimado | Riesgo | Complejidad de implementación | Recomendada |
|---|---|---|---|---|
| [Opción 1] | [$ / %] | 🟢 Bajo | Baja | ✓ |
| [Opción 2] | [$ / %] | 🟡 Medio | Media | Condicional |
| [Opción 3] | [$ / %] | 🔴 Alto | Alta | ✗ |

RECOMENDACIÓN DE PRIORIDAD:
  1. Implementar de inmediato: [opciones de bajo riesgo y alto impacto]
  2. Evaluar con asesor: [opciones de riesgo medio que requieren análisis adicional]
  3. Descartar o esperar: [opciones de riesgo alto o bajo impacto]
```

---

**⚠️ Nota del revisor:** La LISR, el CFF y la RMF se modifican anualmente con el Paquete Económico. Este análisis refleja el derecho vigente al momento del análisis — cualquier opción que dependa de tasas, umbrales o deducciones específicas debe verificarse contra la legislación del ejercicio en que se implementará `[model knowledge — verify]`. Las estructuras internacionales deben validarse contra las reglas BEPS y los tratados aplicables con asesoría especializada en fiscalidad internacional.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
