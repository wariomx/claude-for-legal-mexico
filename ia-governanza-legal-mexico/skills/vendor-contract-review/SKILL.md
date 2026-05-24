---
description: >
  Revisión de contrato con proveedor de IA — identifica cláusulas problemáticas
  en training-on-data, propiedad de outputs, liability caps, indemnización, y
  cumplimiento con EU AI Act. Produce marcado de cambios con recomendaciones.
argument-hint: "[--archivo <ruta> | --pegar-contrato]"
---

# /vendor-contract-review

## Propósito

Revisar el contrato con un proveedor de IA — ya sea un acuerdo negociado, un DPA, o unos términos de servicio (ToS) con opción de opt-out — para identificar cláusulas que crean riesgo para la organización. La prioridad es IA-específica: los riesgos que los contratos tecnológicos estándar no cubren adecuadamente.

Este skill no reemplaza la revisión general del contrato comercial (para eso, ver `corporativo-legal-mexico`). Se enfoca exclusivamente en las cláusulas de IA.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Extraer:
- ¿Hay nexo europeo? (Determina si el cumplimiento EU AI Act del proveedor es relevante)
- ¿Existe algún sistema de este proveedor ya en el registro de casos de uso con clasificación de riesgo?
- Postura de riesgo general de la organización.

### 2. Obtener el contrato

Si se invocó con `--archivo <ruta>`: leer el archivo en esa ruta.
Si se invocó con `--pegar-contrato`: pedir al usuario que pegue el texto.
Si no se proporcionó nada: pedir al usuario que comparta el contrato (ruta o texto pegado) e identificar el proveedor y tipo de sistema de IA.

Si el contrato es en inglés: trabajar en el idioma original para la revisión técnica; el reporte final se produce en español.

### 3. Revisión por checklist de IA

Para cada punto del checklist, identificar si la cláusula relevante existe, qué dice, y cuál es el riesgo. Usar la escala canónica: 🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo o inexistente.

---

#### 1. TRAINING-ON-DATA

**Qué buscar:** ¿El contrato permite al proveedor usar datos del cliente (inputs al sistema, outputs generados, datos de uso) para entrenar o mejorar sus modelos?

**Por qué importa:**
- Los datos del cliente pueden ser información confidencial o secretos comerciales
- Si los datos incluyen datos personales, el uso para entrenamiento requiere base legal bajo LGPDPPSP (consentimiento, o justificación de interés legítimo) y posiblemente un DPA
- Bajo el EU AI Act, los proveedores de sistemas de alto riesgo deben documentar los datos de entrenamiento (Art. 10); usar datos del cliente sin control puede complicar el cumplimiento
- Una vez en el modelo del proveedor, los datos son prácticamente irrecuperables

**Cláusulas a identificar:** "training," "improve," "model improvement," "feedback," "data use," "machine learning."

**Posiciones habituales:**
- ToS permisivos (ej., muchos proveedores SaaS de IA): el proveedor puede usar todos los datos por defecto
- Opt-out disponible: el cliente puede desactivar el entrenamiento, frecuentemente en configuración de cuenta enterprise
- DPA negociado: prohibición explícita de usar datos del cliente para entrenamiento

**Recomendación de redacción si se detecta problema:**
> "El Proveedor no utilizará los Datos del Cliente, incluyendo los inputs proporcionados por el Cliente al Sistema, los outputs generados para el Cliente, ni ningún dato derivado de la interacción del Cliente con el Sistema, para entrenar, ajustar (fine-tuning), mejorar, o desarrollar ningún modelo de aprendizaje automático o sistema de inteligencia artificial, propio o de terceros, sin el consentimiento previo, expreso y por escrito del Cliente."

---

#### 2. PROPIEDAD DE OUTPUTS

**Qué buscar:** ¿Quién es el titular de los outputs que genera el sistema con los datos o prompts del cliente?

**Por qué importa:**
- Si el proveedor retiene derechos sobre los outputs, la organización podría no poder usar libremente el contenido generado en productos, publicaciones, o trabajos para clientes
- Bajo LFDA, los outputs generados autónomamente por IA posiblemente no están protegidos por derechos de autor (no hay autor humano reconocible); pero si hay intervención humana significativa, podría haber derechos del usuario
- El contrato debe ser claro sobre qué puede hacer la organización con los outputs: usar internamente, publicar, modificar, sublicenciar, vender

**Posiciones habituales:**
- Outputs son del cliente (posición favorable): el proveedor no retiene derechos sobre los outputs específicos del cliente
- Licencia al cliente para usar los outputs: el proveedor retiene derechos pero otorga licencia amplia
- Ambigüedad: el contrato no dice nada → riesgo

**Recomendación de redacción:**
> "Los outputs generados por el Sistema en respuesta a los inputs del Cliente son propiedad exclusiva del Cliente. El Proveedor no adquiere ningún derecho de propiedad intelectual sobre dichos outputs. El Cliente tiene derecho irrestricto a usar, modificar, distribuir, sublicenciar, y crear obras derivadas de los outputs para cualquier propósito lícito."

---

#### 3. LIABILITY CAP

**Qué buscar:** ¿Cuál es el límite de responsabilidad del proveedor si el sistema causa daño? ¿Es razonable relativo al riesgo?

**Por qué importa:**
- Los proveedores de IA frecuentemente limitan su responsabilidad al valor de las cuotas pagadas en los últimos 12 meses — lo que para un servicio de $500/mes significa un cap de $6,000 MXN anuales
- Si el sistema toma decisiones que causan daño significativo (ej., denegación errónea de crédito, discriminación en contratación, falla de infraestructura), el cap puede ser insuficiente
- Para sistemas de alto riesgo bajo el EU AI Act, la responsabilidad del proveedor tiene implicaciones regulatorias adicionales

**Evaluar:** cap vs. riesgo máximo estimado del sistema. Si el cap es < 10% del riesgo estimado, marcar 🔴.

**Recomendación si el cap es desproporcionadamente bajo:**
Negociar un cap mayor vinculado al riesgo del caso de uso específico, o excluir del cap los daños causados por incumplimiento del proveedor de sus propias obligaciones de cumplimiento regulatorio.

---

#### 4. INDEMNIZACIÓN

**Qué buscar:** ¿El proveedor defenderá e indemnizará al cliente si hay una reclamación de terceros relacionada con el sistema de IA?

**Por qué importa:**
- Reclamaciones de copyright por outputs del modelo (el modelo generó texto que infringe derechos de autor de un tercero): ¿quién defiende al cliente?
- Reclamaciones por datos personales (el modelo reprodujo datos personales de terceros): ¿quién notifica al regulador y responde?
- Reclamaciones por discriminación (el modelo tomó una decisión discriminatoria): ¿quién asume responsabilidad?

**Verificar:**
- ¿El proveedor indemniza al cliente por reclamaciones de IP sobre los outputs?
- ¿El proveedor indemniza por daños causados por fallas del sistema?
- ¿Hay exclusiones que vacíen la indemnización (ej., "solo si el cliente usó el sistema exactamente como se documenta")?

---

#### 5. CUMPLIMIENTO EU AI ACT

*(Solo si hay nexo europeo confirmado en el perfil de práctica)*

**Qué buscar:** ¿El proveedor garantiza que el sistema cumple con el EU AI Act para la clasificación de riesgo aplicable?

**Por qué importa:**
- Si el sistema es "alto riesgo" bajo el EU AI Act, el proveedor (en su rol de "provider") debe cumplir con Art. 9-15 y registrar el sistema en la base de datos EU
- Si la organización es el "deployer," debe verificar que el proveedor cumple y cooperar con las autoridades de supervisión
- Los incumplimientos del proveedor pueden crear responsabilidad para el deployer

**Verificar:**
- ¿El contrato identifica si el sistema es de alto riesgo bajo el EU AI Act?
- ¿El proveedor declara cumplimiento con el EU AI Act (declaración CE de conformidad)?
- ¿El proveedor se compromete a notificar al cliente cambios en el sistema que afecten la clasificación de riesgo?
- ¿El proveedor proporciona la documentación técnica requerida (Art. 11)?

`[model knowledge — verify: EU AI Act compliance requirements for providers]`

---

#### 6. NOTIFICACIÓN DE INCIDENTE / DATA BREACH

**Qué buscar:** ¿En qué plazo y bajo qué circunstancias notificará el proveedor al cliente si hay un incidente de seguridad, fuga de datos, o falla del sistema?

**Por qué importa:**
- LGPDPPSP requiere notificación al INAI dentro de plazos establecidos cuando hay una brecha de datos personales; el proveedor debe notificar al cliente con suficiente anticipación para que el cliente cumpla sus obligaciones
- Si hay nexo europeo, el RGPD requiere notificación a la autoridad en 72 horas
- Una notificación tardía del proveedor puede hacer que el cliente incumpla sus propias obligaciones regulatorias

**Recomendación:** El proveedor debe notificar al cliente en no más de 24-48 horas de detectar un incidente que afecte datos del cliente.

---

#### 7. PORTABILIDAD Y ELIMINACIÓN AL TERMINAR

**Qué buscar:** Al terminar el contrato, ¿puede el cliente recuperar sus datos (inputs, outputs, configuraciones) y solicitar la eliminación de los mismos del sistema del proveedor?

**Por qué importa:**
- Datos del cliente en los sistemas del proveedor después de la terminación crean riesgo de fuga y uso no autorizado
- LGPDPPSP da al titular de datos el derecho de cancelación; si hay datos personales, deben eliminarse
- Si el proveedor usó datos del cliente para entrenamiento (aunque no debería bajo el punto 1), la eliminación puede ser técnicamente difícil — el contrato debe abordar esto

**Verificar:**
- ¿Hay un período de exportación post-terminación?
- ¿El proveedor confirma por escrito la eliminación?
- ¿La eliminación incluye copias de respaldo y logs de entrenamiento?

---

### 4. Reporte de revisión

Producir el reporte con el encabezado de confidencialidad del perfil de práctica.

**Formato:**

---

**REVISIÓN DE CONTRATO CON PROVEEDOR DE IA**

**Proveedor:** [nombre]
**Tipo de sistema:** [LLM / vision / prediction / otro]
**Tipo de documento revisado:** [MSA / DPA / ToS / otro]
**Fecha de revisión:** [fecha]
**Ley aplicable:** [LGPDPPSP / EU AI Act / ambas / solo México]

| # | Cláusula | Posición actual | Riesgo | Recomendación |
|---|---|---|---|---|
| 1 | Training-on-data | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |
| 2 | Propiedad de outputs | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |
| 3 | Liability cap | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |
| 4 | Indemnización | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |
| 5 | Cumplimiento EU AI Act | [descripción o "no aplica"] | 🔴/🟠/🟡/🟢 | [acción] |
| 6 | Notificación de incidente | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |
| 7 | Portabilidad y eliminación | [descripción] | 🔴/🟠/🟡/🟢 | [acción] |

**Resumen:** [N] bloqueantes / [N] alto / [N] medio / [N] bajo

**Cláusulas de redacción alternativa recomendadas:** [incluir texto de las cláusulas problemáticas con la versión recomendada]

---

Nota del revisor estándar arriba del encabezado de confidencialidad.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
