---
description: >
  Audita el estado de cumplimiento de NOM-035-STPS-2018 (factores de riesgo
  psicosocial) y NOM-037-STPS-2023 (teletrabajo). Produce una lista de
  brechas por fase y obligación, con calificación de riesgo y plan de acción
  priorizado. También genera los documentos requeridos por las normas:
  política de prevención, guía de referencia, evidencia de aplicación de
  cuestionarios, política de teletrabajo y checklist de equipamiento.
argument-hint: "[nom-035 | nom-037 | ambas]"
---

# /nom-compliance

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer del módulo NOM-035/037: número de trabajadores, porcentaje de teletrabajadores, estatus actual de cumplimiento.

2. **Determinar el alcance.** Si el argumento no lo especifica, preguntar: ¿auditar NOM-035, NOM-037, o ambas?

3. **NOM-035-STPS-2018 — Factores de riesgo psicosocial.**

   Determinar la fase aplicable según el número de trabajadores:
   - **Hasta 15 trabajadores:** obligaciones de Fase 1 solamente
   - **De 16 a 50 trabajadores:** obligaciones de Fase 1 y Fase 2
   - **Más de 50 trabajadores:** obligaciones de Fase 1, Fase 2 y Fase 3

   `[settled — last confirmed 2026-05-24]`

   **Checklist de cumplimiento NOM-035:**

   | Obligación | Fase | Estatus | Evidencia requerida |
   |---|---|---|---|
   | Política de prevención de riesgos psicosociales | 1 | ¿✓/✗/N/A? | Documento firmado y difundido |
   | Medidas de prevención de violencia laboral | 1 | ¿✓/✗/N/A? | Política o procedimiento |
   | Difusión de la política a los trabajadores | 1 | ¿✓/✗/N/A? | Acuse de recibo o lista de asistencia |
   | Identificación de trabajadores expuestos a factores de riesgo psicosocial (cuestionario) | 2 | ¿✓/✗/N/A? | Cuestionarios aplicados, fecha |
   | Evaluación de los factores de riesgo psicosocial | 2 | ¿✓/✗/N/A? | Reporte de resultados |
   | Adopción de medidas para prevenir y controlar factores de riesgo | 2 | ¿✓/✗/N/A? | Plan de acción documentado |
   | Evaluación del entorno organizacional | 3 | ¿✓/✗/N/A? | Reporte de evaluación |
   | Control y seguimiento de las medidas adoptadas | 3 | ¿✓/✗/N/A? | Registro de seguimiento |
   | Practicar exámenes médicos a trabajadores expuestos | 3 | ¿✓/✗/N/A? | Registros médicos |

   Para cada obligación sin evidencia, marcar la brecha con severidad:
   - 🔴 **Bloqueante** — multa STPS si hay inspección (Arts. 992-994 LFT, Tabla de infracciones STPS) `[model knowledge — verify]`
   - 🟠 **Alto** — incumplimiento documental que se subsana con trabajo inmediato
   - 🟡 **Medio** — brecha menor, plan de acción a 30-60 días
   - 🟢 **Bajo** — mejora recomendable pero no urgente

4. **NOM-037-STPS-2023 — Teletrabajo.**

   Verificar si aplica: ¿hay trabajadores que prestan servicios en modalidad de teletrabajo más del 40% del tiempo desde su domicilio? `[settled — last confirmed 2026-05-24]`

   Si no hay teletrabajadores que superen el umbral, anotar "NOM-037 no aplicable" y continuar.

   **Checklist de cumplimiento NOM-037:**

   | Obligación | Estatus | Evidencia requerida |
   |---|---|---|
   | Política de teletrabajo | ¿✓/✗? | Documento firmado y registrado ante STPS |
   | Contrato o addendum de teletrabajo por trabajador | ¿✓/✗? | Contrato firmado por cada teletrabajador |
   | Lista de verificación de condiciones de seguridad del domicilio | ¿✓/✗? | Checklist firmado por trabajador |
   | Provisión de equipamiento: equipo de cómputo, silla, etc. | ¿✓/✗? | Acuse de entrega de equipos |
   | Pago de servicios proporcionales (Internet, electricidad) | ¿✓/✗? | Cláusula en contrato + comprobante de pago |
   | Mecanismo de desconexión digital | ¿✓/✗? | Política o cláusula en contrato |
   | Registro del teletrabajo en STPS | ¿✓/✗? | Acuse de registro `[model knowledge — verify]` |

5. **Plan de acción priorizado.** Para cada brecha identificada, producir:

   ```
   🔴/🟠/🟡/🟢 [Nombre de la obligación]
   - Brecha: [qué falta exactamente]
   - Acción: [qué hacer]
   - Responsable: [según perfil de práctica: RH / Salud Ocupacional / Jurídico]
   - Plazo sugerido: [inmediato / 30 días / 60 días / 90 días]
   - Documento a generar: [nombre del documento]
   ```

6. **Ofrecer generación de documentos.** Al final del plan de acción:

   > **¿Quieres que genere alguno de estos documentos?**
   > - Política de prevención de riesgos psicosociales (NOM-035)
   > - Política de teletrabajo (NOM-037)
   > - Checklist de condiciones de seguridad del domicilio (NOM-037)
   > - Addendum al contrato de trabajo para teletrabajadores
   > - Guía de referencia para trabajadores (explicación de la NOM en lenguaje llano)

   Si el usuario pide un documento, generarlo en español con la estructura mínima requerida por la norma. Marcar con `[review]` los párrafos que el abogado debe adaptar a la realidad de la empresa.

## Salvaguardas

- **No afirmar el monto exacto de multas STPS.** Las multas se calculan en UMAs y varían por infracción y reincidencia. Señalar que hay riesgo de multa y remitir a `[model knowledge — verify]` para el monto exacto.
- **No marcar como cumplido** ningún ítem sin que el usuario confirme que tiene la evidencia documental. La evidencia es lo que la STPS revisará en una inspección.
- **Verificar la vigencia de NOM-037.** La NOM-037-STPS-2023 es relativamente reciente. Añadir: "Verificar en el DOF si hay modificaciones a la NOM-037 posteriores a 2023 antes de confiar en este checklist. `[model knowledge — verify]`"

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
