---
description: >
  Redacción o revisión de política interna de uso responsable de IA —
  principios de uso aceptable, herramientas permitidas y prohibidas, proceso
  de aprobación de nuevos casos de uso, revisión humana obligatoria, y
  confidencialidad. Adapta la política al tipo de organización y sector.
argument-hint: "[--revisar <ruta> | --nueva]"
---

# /ai-policy-draft

## Propósito

Redactar desde cero una política interna de uso responsable de IA, o revisar y actualizar una política existente. La política es un documento interno de cumplimiento, no un documento legal técnico — debe ser legible por cualquier empleado, no solo por el equipo jurídico.

## Cuándo usar

- `--nueva`: no existe política interna; crear desde cero
- `--revisar <ruta>`: existe una política; revisarla contra los requisitos del EU AI Act (si hay nexo europeo), el inventario actual de herramientas, y las mejores prácticas

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Extraer:
- Inventario de herramientas de IA en uso
- Si existe política actual (y si se pasó `--revisar`, leer esa política)
- Nexo europeo (determina si la política debe considerar EU AI Act)
- Tipo de organización y sector (determina los riesgos específicos a cubrir)
- Herramientas de IA actuales en `## Política de IA`

### 2. Recopilar información de contexto

Si no está en el perfil o si `--nueva`:

- **¿Qué herramientas de IA usa actualmente el personal?** (ChatGPT, Copilot, Gemini, Claude, herramientas sectoriales específicas — ser específico)
- **¿Cuáles son los usos de IA que más preocupan al equipo de liderazgo?** (ej., datos de clientes en LLMs externos, alucinaciones en documentos legales o médicos, deepfakes, decisiones automatizadas sobre empleados)
- **¿Hay sectores regulados que imponen restricciones adicionales?** (financiero — CNBV; salud — COFEPRIS; datos personales — INAI)
- **¿Quién aprueba el uso de nuevas herramientas de IA actualmente?** (¿hay un proceso, aunque sea informal?)
- **¿El personal ha recibido capacitación sobre IA?** ¿Se contempla en el presupuesto?
- **¿La organización tiene nexo europeo que active el EU AI Act?**

Si se usa `--revisar`: leer la política existente primero y comparar contra los puntos de la sección 4.

### 3. Redactar o revisar

#### Para `--nueva`:

Redactar la política con las siguientes secciones:

---

**[NOMBRE DE LA ORGANIZACIÓN]**
**POLÍTICA DE USO RESPONSABLE DE INTELIGENCIA ARTIFICIAL**
**Versión:** 1.0 | **Fecha de aprobación:** [FECHA] | **Próxima revisión:** [FECHA + 1 año]
**Aprobado por:** [APROBADOR] | **Responsable:** [ÁREA]

---

**1. Propósito y alcance**

Esta Política establece los principios, responsabilidades y procedimientos para el uso de sistemas de inteligencia artificial (IA) por parte del personal de [ORGANIZACIÓN], incluyendo empleados, consultores y cualquier persona que acceda a sistemas o datos de la organización.

El objetivo es permitir que la organización aproveche las capacidades de la IA de forma segura, ética y responsable, mientras protege la información confidencial, cumple con las obligaciones legales aplicables, y mantiene la calidad y responsabilidad en el trabajo.

**Alcance:** [Todo el personal / Personal de las siguientes áreas / Solo para los siguientes tipos de herramientas]

---

**2. Principios de uso responsable de IA**

- **Supervisión humana:** La IA asiste; las decisiones importantes las toman personas. Todo output de IA que vaya a ser comunicado a clientes, presentado a directivos, utilizado en un producto, o tenga efectos sobre personas debe ser revisado por un ser humano con el criterio y la autoridad para validarlo.
- **Confidencialidad:** La información confidencial de la organización, de clientes, de empleados, o cualquier dato personal no debe ingresarse a herramientas de IA externas sin que se hayan verificado las condiciones del contrato con el proveedor y obtenido las autorizaciones correspondientes.
- **Precisión y verificación:** Los sistemas de IA generativa pueden producir información incorrecta (alucinaciones). Toda información factual generada por IA debe verificarse contra fuentes primarias antes de utilizarse en documentos, comunicaciones o decisiones.
- **Transparencia:** Cuando sea relevante, informar a clientes, contrapartes o terceros cuando un producto, servicio o comunicación fue generado o apoyado por sistemas de IA.
- **No discriminación:** Los sistemas de IA no deben usarse de manera que resulte en discriminación por motivos de género, edad, raza, origen étnico, discapacidad, estado civil, preferencia sexual, opinión política, o cualquier otra categoría protegida por la ley.

---

**3. Herramientas de IA**

**3.1 Herramientas aprobadas para uso del personal:**

| Herramienta | Proveedor | Usos autorizados | Restricciones |
|---|---|---|---|
| [HERRAMIENTA] | [PROVEEDOR] | [USOS] | [RESTRICCIONES] |

*Para solicitar que se evalúe una herramienta no incluida en esta lista, seguir el proceso del numeral 5.*

**3.2 Usos prohibidos:**

- Ingresar datos personales de clientes, empleados, o terceros en herramientas de IA externas sin verificar que el contrato del proveedor prohibe el uso de esos datos para entrenamiento y que existe base legal para el procesamiento.
- Ingresar información confidencial de la organización (secretos industriales, estrategias, información financiera no pública, información privilegiada) en herramientas de IA externas sin que el DPA o contrato con el proveedor garantice la confidencialidad y prohiba el uso para entrenamiento.
- Generar, distribuir, o usar deepfakes, imágenes o videos manipulados con IA, o cualquier contenido sintético que pueda engañar a clientes, contrapartes, autoridades, o al público.
- Usar IA para tomar decisiones automatizadas definitivas sobre empleados (contratación, despido, evaluación de desempeño) sin revisión humana significativa y sin cumplir con los requisitos de transparencia aplicables.
- Presentar como propio trabajo generado íntegramente por IA sin revisión, edición, y apropiación intelectual genuina del resultado.
- Usar herramientas de IA para actividades que violen la ley o las políticas internas de la organización.

---

**4. Datos personales y confidencialidad**

**4.1 Datos personales:** El uso de datos personales (de clientes, empleados, o cualquier persona identificable) en sistemas de IA está sujeto a las obligaciones de la Ley General de Protección de Datos Personales en Posesión de Particulares (LGPDPPSP) y a los avisos de privacidad vigentes. Antes de usar datos personales con un sistema de IA:

a) Verificar que existe base legal para el procesamiento con IA (consentimiento, ejecución de contrato, interés legítimo debidamente justificado).
b) Verificar que el Aviso de Privacidad informa sobre el uso de IA para el tratamiento de los datos.
c) Verificar que el contrato con el proveedor de IA garantiza la confidencialidad y prohibe el uso de los datos para entrenamiento del modelo.
d) Si hay afectados en la Unión Europea: verificar las obligaciones adicionales del RGPD.

**4.2 Información confidencial:** Se entiende por información confidencial toda aquella que la organización no ha hecho pública y cuya divulgación podría causar daño. Antes de ingresar información confidencial en una herramienta de IA externa, verificar que el contrato con el proveedor garantiza la confidencialidad. Si hay duda, contactar al [Área Jurídica / DPO / Responsable de IA].

---

**5. Proceso de aprobación para nuevos casos de uso o herramientas**

Para usar una herramienta de IA no incluida en la lista de herramientas aprobadas, o para un caso de uso significativamente diferente a los autorizados:

1. Completar el formulario de solicitud de nuevo caso de uso IA ([ruta del formulario / quién lo tiene]).
2. El formulario incluye: descripción del uso, herramienta propuesta, datos que se procesarán, beneficio esperado, responsable del uso.
3. La solicitud es revisada por [Área Jurídica / TI / Comité de IA / Responsable designado] en [plazo].
4. La aprobación puede ser: (a) sin restricciones, (b) con condiciones específicas, o (c) rechazada.
5. Las herramientas aprobadas se agregan a la lista del numeral 3.1.

---

**6. Capacitación y concientización**

- Todo el personal que use herramientas de IA debe completar el curso de inducción de uso responsable de IA [ruta del curso / frecuencia].
- Las personas que usen sistemas de IA de alto riesgo o con acceso a datos sensibles deben completar capacitación adicional [especificar].
- El [Área Jurídica / Responsable de IA] publicará actualizaciones cuando haya cambios importantes en el marco regulatorio o en la política.

---

**7. Reporte de incidentes**

Si el personal detecta:
- Un output de IA que parece incorrecto o engañoso y fue usado en una decisión o comunicación importante
- Una posible fuga de información confidencial a través de una herramienta de IA
- Un uso de IA que parece discriminatorio o contrario a esta Política
- Una reclamación de un cliente, empleado, o tercero relacionada con el uso de IA

Debe reportarlo a [correo / sistema de tickets / persona] dentro de [plazo]. Los reportes de buena fe no tendrán consecuencias negativas para quien los haga.

---

**8. Responsabilidades**

| Rol | Responsabilidad |
|---|---|
| [Área Jurídica / DPO] | Mantenimiento y actualización de esta Política; evaluación de nuevos casos de uso; cumplimiento regulatorio |
| [TI / Seguridad de la Información] | Evaluación técnica de herramientas; controles de acceso; monitoreo de herramientas no autorizadas |
| [Liderazgo / Gerentes] | Asegurar que su equipo conoce y cumple esta Política; reportar incidentes |
| [Todo el personal] | Cumplir con esta Política; completar la capacitación requerida; reportar incidentes |

---

**9. Actualizaciones y revisión**

Esta Política se revisará anualmente o antes si hay cambios significativos en el marco regulatorio (ej., nuevas guías del EU AI Act, reformas a LGPDPPSP, nueva legislación mexicana de IA) o en el uso de IA en la organización. Los cambios materiales se comunicarán a todo el personal y requerirán nueva aceptación. `[model knowledge — verify: estado de iniciativas legislativas de IA en México]`

---

#### Para `--revisar`:

Leer la política existente y evaluar contra:

**Brechas frente al EU AI Act (si hay nexo europeo):**
- ¿La política menciona los sistemas de alto riesgo bajo el EU AI Act y sus obligaciones específicas?
- ¿Hay un proceso de evaluación de conformidad para sistemas de alto riesgo?
- ¿La política cubre las obligaciones de transparencia del Art. 50 (identificación de chatbots)?
- ¿La política cubre los sistemas GPAI y sus consideraciones de copyright?

**Brechas frente al marco mexicano:**
- ¿La política cubre las obligaciones de LGPDPPSP para decisiones automatizadas?
- ¿Hay referencias al derecho de explicación (LGPDPPSP Art. 22)?
- ¿La política aborda la autoría de outputs generados por IA bajo LFDA?

**Brechas generales:**
- ¿Está actualizada frente al inventario actual de herramientas?
- ¿El proceso de aprobación existe y es operativo?
- ¿Hay mecanismo de reporte de incidentes?
- ¿La capacitación está definida y se ejecuta?
- ¿La política tiene dueño y fecha de revisión?

Producir un marcado de cambios con cada brecha identificada, la severidad, y el texto recomendado.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
