---
description: >
  Evalúa el riesgo jurídico de una terminación laboral individual o colectiva
  bajo la LFT. Analiza si la causa de rescisión es fundamentable (Art. 47 LFT),
  si hay evidencia suficiente, qué pretensiones puede ejercer el trabajador
  (Arts. 48-50 LFT), y produce un semáforo de riesgo con árbol de decisión.
  También cubre rescisión por parte del trabajador (Art. 51 LFT) y terminación
  colectiva (Arts. 433-439 LFT).
argument-hint: "[tipo: individual-con-causa | individual-sin-causa | rescision-trabajador | colectiva]"
---

# /termination-risk

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Si el módulo de Terminación y Liquidación no está activado, avisar y continuar de todos modos con un marco genérico.

2. **Identificar el tipo de terminación.** Si el argumento no lo especifica, preguntar:
   - ¿Es una terminación **con causa** (el empleador alega que el trabajador incurrió en una causal del Art. 47 LFT)?
   - ¿Es una terminación **sin causa** (el empleador paga liquidación sin alegar causa)?
   - ¿Es una **rescisión por parte del trabajador** (el trabajador alega que el empleador incurrió en una causal del Art. 51 LFT)?
   - ¿Es una **terminación colectiva** (restructuración, cierre, caso fortuito — Arts. 433-439 LFT)?

3. **Capturar hechos de la terminación.** Preguntar o extraer del `matter.md` activo:
   - Causal invocada (para terminación con causa: ¿cuál fracción del Art. 47 LFT?)
   - Evidencia disponible: actas administrativas, avisos previos, reportes de RRHH, testigos
   - Fecha del evento que motiva la terminación
   - ¿Se notificó al trabajador por escrito? ¿Con qué plazo?
   - ¿Tiene el trabajador fuero sindical, de maternidad, de enfermedad, u otro?

4. **Análisis de riesgo por tipo:**

   ### Terminación con causa (Art. 47 LFT)

   - ¿La causal invocada está en el catálogo del Art. 47 LFT? `[settled — last confirmed 2026-05-24]`
   - ¿Los hechos encuadran en la causal? Analizar elemento por elemento.
   - ¿Hay evidencia documental suficiente para demostrar la causal ante el Tribunal Laboral?
   - ¿Se notificó la rescisión dentro del plazo de prescripción de la causal (1 mes, Art. 517 frac. I LFT)? `[settled — last confirmed 2026-05-24]`
   - ¿Hay riesgo de que el Tribunal califique la terminación como injustificada?
   - Si se califica como injustificada: ¿cuál es la exposición? (reinstatement + salarios vencidos, o indemnización constitucional a elección del trabajador, Art. 48 LFT) `[settled — last confirmed 2026-05-24]`

   ### Terminación sin causa (Art. 50 LFT)

   - ¿Se están pagando correctamente los tres conceptos: 3 meses de salario + 20 días por año + prima de antigüedad (12 días por año, Art. 162 LFT)? `[settled — last confirmed 2026-05-24]`
   - ¿Se incluyen todos los conceptos proporcionales: aguinaldo, vacaciones, prima vacacional, PTU?
   - ¿El salario diario integrado está calculado correctamente (Art. 84 LFT)?
   - ¿Hay conceptos variables que se deben integrar?
   - **Riesgo residual:** aun pagando correctamente, el trabajador puede demandar por diferencias. ¿Es razonable el riesgo de diferencias?

   ### Rescisión por parte del trabajador (Art. 51 LFT)

   - ¿La causal invocada por el trabajador está en el catálogo del Art. 51 LFT?
   - ¿Hay evidencia que soporte o desvirtúe la causal?
   - Si se acredita la causal: el trabajador tiene derecho a la misma indemnización que en terminación sin causa (Art. 52 LFT). `[settled — last confirmed 2026-05-24]`
   - ¿Cuál es la probabilidad de que el Tribunal acredite la causal?

   ### Terminación colectiva (Arts. 433-439 LFT)

   - ¿Cuál es la causa invocada? (caso fortuito / fuerza mayor / agotamiento de materia prima / incosteabilidad notoria / cierre de empresa)
   - ¿Se requiere autorización del Tribunal Laboral? (para terminaciones por incosteabilidad y cierre de empresa, sí — Arts. 434-437 LFT) `[settled — last confirmed 2026-05-24]`
   - ¿Cuántos trabajadores involucra? ¿Hay sindicato?
   - ¿Cuál es la indemnización aplicable según la causa?

5. **Verificar fueros y protecciones especiales.**
   - ¿El trabajador tiene fuero sindical (Art. 174 LFT)?
   - ¿Está embarazada o en periodo de lactancia (Arts. 164-172 LFT)?
   - ¿Está incapacitado por riesgo de trabajo o enfermedad (Arts. 42-43 LFT)?
   - ¿Es un trabajador de confianza con régimen especial?
   - Cualquier fuero activo se marca `[review]` — requiere análisis específico antes de proceder.

6. **Semáforo de riesgo.** Producir una calificación:

   | Componente | Calificación | Notas |
   |---|---|---|
   | Fundamentabilidad de la causal | 🔴/🟠/🟡/🟢 | |
   | Suficiencia de evidencia | 🔴/🟠/🟡/🟢 | |
   | Riesgo de fueros | 🔴/🟠/🟡/🟢 | |
   | Exposición económica estimada | [rango] | Confirmar con `/laboral-legal-mexico:liquidacion-calculator` |
   | **Riesgo global** | **🔴/🟠/🟡/🟢** | |

7. **Árbol de decisión.** Cerrar con opciones:

   > **¿Qué sigue?**
   > 1. **Calcular liquidación exacta** — `/laboral-legal-mexico:liquidacion-calculator`
   > 2. **Preparar carta de rescisión** — `/laboral-legal-mexico:escrito-laboral --tipo carta-rescision`
   > 3. **Preparar conciliación CJFCA** — `/laboral-legal-mexico:cjfca-conciliacion` (etapa prejudicial obligatoria antes del Tribunal)
   > 4. **Escalar para revisión** — redactaré una nota de escalamiento al aprobador según tu perfil de práctica
   > 5. **Esperar — no proceder todavía** — agregaré el asunto al monitoreo del agente con nota de por qué

## Salvaguardas

- **No dictaminar la causa como "fundamentable" sin evidencia.** Si el usuario describe la causa pero no tiene evidencia documental, marcar el componente de suficiencia como 🔴 y explicar qué evidencia se necesitaría.
- **No omitir los fueros.** La lista de fueros se verifica siempre — un trabajador con fuero activo convierte una terminación de bajo riesgo en 🔴.
- **Marcar con `[review]` toda conclusión que dependa de jurisprudencia no verificada.**

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
