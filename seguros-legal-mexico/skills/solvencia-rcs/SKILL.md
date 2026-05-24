---
description: >
  Análisis del Requerimiento de Capital de Solvencia (RCS) para aseguradoras
  y afianzadoras mexicanas — el equivalente nacional de Solvencia II.
  Evalúa el capital requerido vs. disponible, la composición de fondos
  propios admisibles, las reservas técnicas, el catálogo de inversiones
  admisibles y el margen de solvencia. Produce un diagnóstico de solvencia
  con acciones prioritarias.
argument-hint: "[tipo de institución o estados financieros a analizar]"
---

# Skill: solvencia-rcs (seguros-legal-mexico)

## Propósito

El RCS (Requerimiento de Capital de Solvencia) es el pilar cuantitativo de la supervisión CNSF post-2015. Una institución que no cubre su RCS entra automáticamente en supervisión especial (LISF Art. 310), lo que puede derivar en medidas correctivas, restricciones operativas y eventualmente la revocación de la autorización. Este skill diagnostica el estado de solvencia y los pasos para remediar déficits.

## Marco regulatorio

| Norma | Relevancia |
|---|---|
| LISF Arts. 240-280 | RCS — fundamento legal del régimen de solvencia |
| LISF Arts. 216-239 | Reservas técnicas — constitución, valuación, inversión |
| LISF Arts. 190-215 | Capital mínimo pagado y fondos propios admisibles |
| Disposiciones CNSF — Capital y Reservas | Metodología de cálculo del RCS `[model knowledge — verify versión vigente DOF]` |
| Disposiciones CNSF — Inversiones | Catálogo de activos admisibles y límites `[model knowledge — verify]` |
| LISF Arts. 295-315 | Supervisión especial por incumplimiento de RCS |

**Nota metodológica.** El cálculo exacto del RCS requiere los estados financieros dictaminados, la nota técnica por ramo, el reporte actuarial y los datos del portafolio de inversiones. Sin estos insumos, este skill produce un diagnóstico cualitativo y señala los indicadores de alerta; el cálculo cuantitativo requiere al actuario responsable de la institución. Marcar los elementos que requieren el actuario con `[review: actuario requerido]`.

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo Operador:
- Tipo de institución y ramos
- Nombre del actuario responsable
- Fecha del último reporte de solvencia

Si el módulo Operador no está activo, advertir y continuar con análisis genérico.

### Paso 1: captura de insumos

Solicitar los documentos disponibles:

1. "¿Tienes el último reporte de solvencia enviado a CNSF? (para el período más reciente)"
2. "¿Tienes los estados financieros dictaminados?"
3. "¿Tienes el reporte del actuario responsable?"
4. "¿Cuál es el monto actual del capital mínimo pagado?"
5. "¿Tienes el inventario de inversiones que respaldan reservas técnicas?"

Si no hay insumos: señalar los indicadores que pueden evaluarse cualitativamente y los que requieren datos financieros.

### Paso 2: capital mínimo pagado

Verificar si el capital mínimo pagado cubre el mínimo legal:

| Tipo de institución | Capital mínimo aproximado (referencia) | `[verify monto vigente CNSF]` |
|---|---|---|
| Aseguradora de vida | [model knowledge — verify] | `[verify]` |
| Aseguradora de daños | [model knowledge — verify] | `[verify]` |
| Aseguradora de vida y daños | [model knowledge — verify] | `[verify]` |
| Afianzadora | [model knowledge — verify] | `[verify]` |
| Sociedad mutualista | [model knowledge — verify] | `[verify]` |

Los montos están expresados en UDIS o pesos conforme a las Disposiciones CNSF vigentes. `[verify con búsqueda web antes de reportar un monto]`

Clasificar: ✓ Capital mínimo cubierto / ✗ Déficit de capital mínimo 🔴

### Paso 3: fondos propios admisibles

Los fondos propios admisibles son los recursos con los que la institución puede cubrir el RCS. Se clasifican en Nivel 1, Nivel 2 y Nivel 3 según su capacidad de absorción de pérdidas.

- [ ] Fondos propios Nivel 1 (capital pagado + superávit por prima + utilidades retenidas) — sin límite
- [ ] Fondos propios Nivel 2 (deuda subordinada a largo plazo) — límite % del RCS `[verify límite vigente]`
- [ ] Fondos propios Nivel 3 (otros instrumentos) — límite más restrictivo `[verify]`
- [ ] Deducir activos no admisibles del catálogo CNSF `[model knowledge — verify catálogo vigente]`

`[review: actuario requerido para cálculo exacto de fondos propios admisibles]`

### Paso 4: reservas técnicas

Las reservas técnicas deben ser suficientes para cubrir las obligaciones con los asegurados. Su cálculo es actuarial.

- [ ] **Reserva de Riesgos en Curso (RRC)** — para riesgos vigentes no ocurridos: ¿calculada por el actuario responsable con la metodología CNSF? `[review: actuario requerido]`
- [ ] **Reserva para Siniestros Pendientes (RSP)** — para siniestros reportados no pagados y IBNR (incurridos no reportados): ¿estimación IBNR documentada? `[review: actuario requerido]`
- [ ] **Reserva de Previsión (RP)** — para fluctuaciones estadísticas: ¿constituida conforme a disposiciones por ramo? `[model knowledge — verify]`
- [ ] **Reserva Especial (RE)** — si aplica por ramo específico
- [ ] Las reservas están invertidas en los activos admisibles del catálogo CNSF `[verify catálogo]`
- [ ] Las reservas están registradas ante CNSF dentro de los plazos de reporte

### Paso 5: RCS — diagnóstico cualitativo

Si no hay el reporte RCS disponible, evaluar cualitativamente los componentes de riesgo:

| Módulo de riesgo | Estado | Indicadores de alerta |
|---|---|---|
| Riesgo de suscripción (vida / daños / salud) | `[review: datos de siniestralidad requeridos]` | Siniestralidad sobre prima > umbral del ramo |
| Riesgo de mercado | `[review: portafolio de inversiones requerido]` | Concentración en activos de baja calidad crediticia |
| Riesgo de crédito / contraparte | `[review: datos de reaseguro requeridos]` | Reaseguradores sin calificación o en mora |
| Riesgo operacional | `[review: evaluación interna requerida]` | Ausencia de controles internos documentados |
| Riesgo de concentración | `[review: portafolio requerido]` | > X% en un solo activo o grupo `[verify umbral]` |

### Paso 6: inversiones admisibles

Verificar que las inversiones que respaldan reservas técnicas estén dentro del catálogo de activos admisibles CNSF y los límites por tipo de activo:

- [ ] Inversiones dentro del catálogo de activos admisibles CNSF `[verify catálogo vigente]`
- [ ] Límites por tipo de instrumento (valores gubernamentales, renta variable, bienes raíces, préstamos) respetados
- [ ] Política de inversiones aprobada por el Consejo de Administración
- [ ] Calificaciones mínimas de crédito para instrumentos de deuda cumplidas
- [ ] Diversificación mínima requerida observada
- [ ] Reporte de inversiones enviado a CNSF en los plazos establecidos

`[review: verificar catálogo actual — las Disposiciones CNSF se actualizan]`

### Paso 7: producir reporte

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [reporte RCS proporcionado ✓ | sin estados financieros — análisis cualitativo]
- Leído: [descripción de insumos]
- Marcado para tu criterio: [N elementos [review: actuario requerido]]
- Antes de confiar: los montos de capital mínimo y umbrales RCS deben verificarse contra las Disposiciones de Carácter General CNSF vigentes; los elementos marcados [review: actuario requerido] necesitan validación del actuario responsable de la institución.

---

**Diagnóstico de Solvencia RCS — [institución] — [fecha]**

**Capital mínimo:** [cubierto / déficit — monto] [🔴 si hay déficit]
**Fondos propios admisibles:** [estimación o N/A si no hay datos]
**Reservas técnicas:** [estado cualitativo]
**RCS:** [cubierto / déficit / no calculado — requiere actuario]
**Inversiones:** [dentro de catálogo / brecha identificada]

[Hallazgos por componente]

**Acciones prioritarias:**
1. [Acción más urgente — 🔴 si aplica]
2. [Siguiente acción]

**Una pregunta que haría y que no está en mi checklist:** [observación]
```

> **¿Qué siges?**
> 1. **Plan de capitalización** — si hay déficit de RCS o capital mínimo, elaboro un plan de acción con las opciones disponibles (aportación de capital, reducción de exposición, reaseguro adicional).
> 2. **Análisis de cumplimiento CNSF** — `/seguros-legal-mexico:cnsf-compliance` para el panorama regulatorio completo.
> 3. **Revisar inversiones** — analizo el portafolio actual contra el catálogo CNSF admisible.
> 4. **Responder requerimiento CNSF** — si la CNSF ya notificó un déficit o emitió requerimiento, preparo la respuesta.
> 5. **Escalar** — redacto nota para el Consejo de Administración con el estado de solvencia y las acciones requeridas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
