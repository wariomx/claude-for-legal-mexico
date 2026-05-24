---
description: >
  Abre un nuevo asunto laboral: captura hechos clave, partes, pretensiones y
  riesgo inicial. Crea la carpeta del asunto en
  ~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/matters/<asunto-slug>/
  con un matter.md y lo registra en _log.yaml. Produce un resumen de hechos
  con riesgo preliminar y árbol de decisión de siguientes pasos.
argument-hint: "[descripción breve del asunto]"
---

# /matter-intake

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Si no está configurado, detener: "Ejecuta `/laboral-legal-mexico:cold-start-interview` antes de abrir asuntos."

2. **Capturar hechos básicos del asunto.** Preguntar de forma conversacional, no como formulario. Inferir lo que pueda del argumento inicial o de lo que el usuario ya escribió:

   - **Trabajador:** nombre, puesto, antigüedad (fecha de ingreso), salario diario (ordinario e integrado si lo sabe), tipo de contrato
   - **Empleador:** entidad legal empleadora (¿misma empresa del perfil de práctica o diferente?)
   - **Evento desencadenante:** qué pasó (terminación, queja, accidente, demanda recibida, etc.) y cuándo
   - **Pretensiones del trabajador** (si ya hay demanda): qué pide el trabajador, montos si los especifica
   - **Etapa procesal actual:** antes de presentar demanda / etapa prejudicial CJFCA / demanda presentada ante Tribunal Laboral / sentencia / ejecución
   - **Representación:** ¿el trabajador tiene abogado? ¿cuál despacho si se sabe?
   - **Documentos disponibles:** ¿qué documentos tiene el usuario sobre el asunto?

3. **Generar slug y crear la carpeta del asunto.** Crear el slug a partir del apellido del trabajador y el año: `<apellido>-<AAAA>`. Si hay colisión, agregar inicial del nombre. Crear:
   - `~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/matters/<slug>/matter.md` — hechos del asunto
   - Registrar en `~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/matters/_log.yaml` con `status: active`, fecha de apertura y datos básicos

4. **Calcular riesgo preliminar.** Con base en los hechos capturados, producir una evaluación inicial:

   - **Tipo de riesgo:** ¿Es un asunto de terminación (riesgo = liquidación constitucional + daños)? ¿Discriminación o acoso (riesgo = daño moral + multa STPS)? ¿Accidente de trabajo (riesgo = IMSS + responsabilidad patronal)?
   - **Monto aproximado de exposición:** si hay datos suficientes, dar un rango estimado — no un número exacto hasta ejecutar `/laboral-legal-mexico:liquidacion-calculator`. Marcar `[model knowledge — verify]` y recomendar el skill de cálculo.
   - **Plazo procesal urgente:** ¿hay algún plazo que ya está corriendo? (p. ej., plazo de prescripción de 1 año Art. 516 LFT `[settled — last confirmed 2026-05-24]`, plazo de respuesta CJFCA de 10 días hábiles)
   - **Severidad inicial:** 🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo

5. **Producir resumen del asunto.** Formato:

   ```
   **Asunto:** [slug] — [nombre del trabajador] · [puesto] · [antigüedad] años
   **Empleador:** [entidad legal]
   **Evento:** [descripción breve del evento]
   **Etapa:** [etapa procesal]
   **Riesgo inicial:** [severidad] — [descripción breve de exposición]
   **Plazo urgente:** [plazo | ninguno identificado]
   **Documentos disponibles:** [lista]
   **Asunto creado en:** [ruta de la carpeta]
   ```

6. **Árbol de decisión.** Cerrar con opciones concretas:

   > **¿Qué sigue?**
   > 1. **Calcular liquidación** — `/laboral-legal-mexico:liquidacion-calculator` con los datos de este asunto
   > 2. **Evaluar riesgo de terminación** — `/laboral-legal-mexico:termination-risk` para análisis completo de la terminación
   > 3. **Preparar conciliación CJFCA** — `/laboral-legal-mexico:cjfca-conciliacion` si la etapa prejudicial ya inició o va a iniciar
   > 4. **Redactar escrito** — `/laboral-legal-mexico:escrito-laboral` si hay que contestar demanda o presentar promoción
   > 5. **Observar** — registraré el asunto y lo incluiré en el monitoreo del agente `vigilante-plazos-laborales`

## Salvaguardas

- **No inventar montos de exposición.** Si no hay datos suficientes para estimar, decir "sin datos suficientes para estimar — ejecuta `/laboral-legal-mexico:liquidacion-calculator`."
- **No asumir la fecha de ingreso** si el usuario no la dio — el cálculo de antigüedad es determinante para la liquidación.
- **No crear el asunto sin confirmar el slug** — el slug es la llave del registro de asuntos.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
