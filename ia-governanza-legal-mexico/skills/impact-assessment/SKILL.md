---
description: >
  Evaluación de impacto de sistemas IA — análisis por capas (datos, modelo,
  output, deployment) para identificar riesgos de privacidad, discriminación,
  responsabilidad, seguridad y cumplimiento regulatorio. Produce reporte de
  hallazgos con plan de mitigación.
argument-hint: "[--sistema <nombre>]"
---

# /impact-assessment

## Propósito

Producir una evaluación de impacto estructurada de un sistema de IA en producción o en evaluación previa al despliegue. La evaluación cubre cuatro capas: datos, modelo, output, y deployment. El resultado es un reporte con hallazgos clasificados por severidad y un plan de mitigación para los ítems de riesgo alto y medio.

Esta evaluación puede satisfacer en parte las obligaciones de EIPD-IA bajo el EU AI Act (Art. 9 para alto riesgo) y las obligaciones de evaluación de impacto bajo LGPDPPSP cuando el sistema procesa datos personales con decisiones automatizadas. No reemplaza el análisis legal completo que un abogado debe realizar.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Extraer:
- ¿Hay nexo europeo? (Determina qué marco de evaluación aplica)
- ¿El sistema ya está en el registro de casos de uso? ¿Tiene clasificación de triaje previa?
- ¿Cuál es el umbral organizacional para EIPD-IA?

### 2. Identificar el sistema a evaluar

Si no se proporcionó con `--sistema`, preguntar:
- ¿Qué sistema de IA se evaluará?
- ¿Está ya en el registro de casos de uso? (Buscar en `use-case-register.yaml`)
- ¿Hay un triaje previo (`/ia-governanza-legal-mexico:use-case-triage`) para este sistema? Si sí, leerlo y tomar la clasificación de riesgo como piso.

Si hay triaje previo con clasificación 🔴 PROHIBIDO → detener. Este sistema no debe ser evaluado para despliegue; debe ser revisado para discontinuación o rediseño fundamental.

### 3. Evaluación por capas

Para cada capa, recopilar información y asignar un nivel de riesgo por ítem: 🔴 Alto / 🟠 Medio / 🟡 Bajo / 🟢 Ninguno identificado.

---

#### CAPA 1: DATOS

Preguntas clave:

**Datos de entrenamiento:**
- ¿Con qué datos fue entrenado el modelo? (¿Datos propios, datos del proveedor, datos públicos?)
- ¿Se documentaron los datos de entrenamiento? ¿Hay información sobre su origen y proceso de curación?
- ¿Los datos de entrenamiento podrían tener sesgos (subrepresentación de grupos, datos históricos discriminatorios)?
- Si el modelo fue entrenado con datos propios: ¿se obtuvo consentimiento para ese uso? ¿Había datos personales?

**Datos en operación:**
- ¿Qué datos procesa el sistema en producción?
- ¿Incluye datos personales? ¿Datos sensibles (biométricos, salud, financieros, opinión política, origen racial, orientación sexual)?
- ¿Los afectados saben que sus datos son procesados por un sistema de IA?
- ¿Existe base legal para el procesamiento bajo LGPDPPSP (consentimiento, contrato, interés legítimo)?
- ¿El proveedor usa esos datos para entrenar sus modelos? (Training-on-data — verificar el contrato)
- ¿Dónde se almacenan los datos? ¿Hay transferencias internacionales (ej., a servidores en EE.UU.)? ¿Se cumple el régimen de transferencias de LGPDPPSP?

**Calidad y gobierno de datos:**
- ¿Hay un proceso para mantener los datos actualizados y precisos?
- ¿Existe control de acceso sobre quién puede consultar o modificar los datos del sistema?

---

#### CAPA 2: MODELO

Preguntas clave:

**Explicabilidad:**
- ¿El modelo es una "caja negra" o puede explicar sus decisiones?
- Si toma decisiones sobre personas: ¿puede explicar por qué tomó una decisión específica? ¿Es posible cumplir con el derecho de explicación bajo LGPDPPSP Art. 22?
- ¿El proveedor proporciona documentación técnica del modelo (arquitectura, datos de entrenamiento, métricas de desempeño)?

**Validación y auditoría:**
- ¿Ha sido auditado el modelo por terceros independientes?
- ¿Se han realizado pruebas de sesgo o discriminación? ¿Qué métricas se usaron?
- ¿Hay evidencia de desempeño diferenciado entre grupos (ej., distintas tasas de error para distintos grupos demográficos)?
- ¿Con qué frecuencia se re-entrena o actualiza el modelo? ¿Hay control de versiones?

**Manejo de incertidumbre:**
- ¿El modelo comunica cuándo no tiene suficiente confianza en una predicción?
- ¿Cómo maneja alucinaciones o casos fuera de distribución (inputs que el modelo no fue entrenado para manejar)?
- ¿Hay mecanismos para detectar deriva del modelo (model drift) en producción?

---

#### CAPA 3: OUTPUT

Preguntas clave:

**Uso de los outputs:**
- ¿Quién usa los outputs del sistema? (¿Empleados internos, clientes, sistemas downstream automatizados?)
- ¿Los outputs informan, recomiendan, o deciden? (Informar = más aceptable; Decidir = mayor riesgo)
- ¿Hay decisiones automatizadas sobre personas sin revisión humana? Si sí, ¿cuál es el impacto de esas decisiones?

**Revisión humana:**
- ¿Hay un paso de revisión humana antes de que los outputs afecten a personas?
- ¿Los usuarios humanos que revisan los outputs están capacitados para entender las limitaciones del sistema?
- ¿Hay riesgo de "automation bias" — que los revisores humanos confíen ciegamente en el sistema?

**Discriminación potencial:**
- ¿Los outputs podrían resultar en trato diferencial o discriminatorio para grupos protegidos?
- ¿Se monitorean los outputs para detectar disparidades en resultados entre grupos?
- En México: ¿las categorías protegidas relevantes son raza, género, edad, discapacidad, estado civil, origen social, opinión política, preferencia sexual?

**Derechos de autor de outputs:**
- ¿El sistema genera obras creativas (textos, imágenes, código)?
- ¿La organización necesita tener derechos sobre esos outputs? (Verificar el contrato del proveedor)
- Nota LFDA: la autoría de obras generadas autónomamente por IA no está reconocida bajo LFDA; el output puede no estar protegido.

---

#### CAPA 4: DEPLOYMENT

Preguntas clave:

**Monitoreo en producción:**
- ¿Hay monitoreo continuo del desempeño del sistema una vez en producción?
- ¿Existen alertas cuando el sistema falla o produce outputs anómalos?
- ¿Con qué frecuencia se revisa el desempeño del sistema?

**Mecanismo de reporte:**
- ¿Pueden los afectados reportar problemas o reclamar sobre decisiones del sistema?
- ¿Hay un proceso interno para recibir y resolver reclamaciones relacionadas con el sistema de IA?
- Si hay nexo europeo: ¿el proveedor tiene mecanismo de reporte de incidentes conforme al EU AI Act?

**Plan de contingencia:**
- ¿Qué pasa si el sistema falla o produce outputs incorrectos a gran escala?
- ¿Hay un "kill switch" o proceso para desactivar o revertir el sistema si se detecta un problema grave?
- ¿Existe un plan de comunicación para notificar a afectados si el sistema causa daño?

**Proveedores y cadena de responsabilidad:**
- ¿Está claro quién responde ante los afectados si el sistema causa daño? (¿La organización, el proveedor, o ambos?)
- Si hay nexo europeo: ¿el proveedor se identifica como "proveedor" (provider) bajo el EU AI Act con las obligaciones correspondientes, o la organización toma ese rol como "deployer"?

---

### 4. Reporte de hallazgos

Producir el reporte con el encabezado de confidencialidad del perfil de práctica.

**Formato:**

---

**EVALUACIÓN DE IMPACTO DE SISTEMA DE IA**

**Sistema evaluado:** [nombre]
**Proveedor:** [proveedor]
**Clasificación de riesgo (triaje previo):** [si existe]
**Fecha de evaluación:** [fecha]
**Alcance:** [capas evaluadas / información disponible]

**Resumen ejecutivo:** [2-3 párrafos: qué es el sistema, cuáles son los riesgos más relevantes, cuál es la recomendación general]

---

**Tabla de hallazgos por capa:**

| # | Capa | Hallazgo | Severidad | Mitigación recomendada | Responsable | Estado |
|---|---|---|---|---|---|---|
| 1 | Datos | [descripción] | 🔴/🟠/🟡/🟢 | [acción] | [quién] | Pendiente |
| 2 | Modelo | [descripción] | 🔴/🟠/🟡/🟢 | [acción] | [quién] | Pendiente |
| ... | | | | | | |

**Resumen de severidad:** [N] hallazgos — [N] Alto / [N] Medio / [N] Bajo / [N] Ninguno

---

**Plan de mitigación — ítems Alto y Medio:**

Para cada hallazgo 🔴 o 🟠:
- **Hallazgo:** [descripción]
- **Riesgo si no se mitiga:** [consecuencia concreta]
- **Acción recomendada:** [qué hacer]
- **Plazo sugerido:** [inmediato / antes del despliegue / dentro de 90 días]
- **Responsable:** [área/persona]

---

**Conclusión:**

¿Puede el sistema desplegarse en su estado actual? [Sí sin restricciones / Sí con las siguientes condiciones / No hasta resolver hallazgos bloqueantes]

[Si no: listar los hallazgos bloqueantes específicos]

---

Nota del revisor estándar arriba del encabezado de confidencialidad. Incluir:
- Fuentes (LegalDataHunter / conocimiento del modelo)
- Cobertura de la evaluación (información disponible vs. información no obtenida)
- Items marcados `[review]` para criterio del abogado
- Antes de confiar: verificar [los 1-2 items más críticos]

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
