---
description: >
  Triaje de nuevo caso de uso de IA — clasificación de riesgo conforme al EU
  AI Act (prohibido/alto/limitado/mínimo/GPAI) y marco mexicano, determinación
  de si requiere evaluación de impacto (EIPD-IA), y registro en el inventario
  de sistemas IA. Produce ficha de triaje con recomendaciones.
argument-hint: ""
---

# /use-case-triage

## Propósito

Clasificar un nuevo sistema o caso de uso de IA antes de ponerlo en producción o antes de comprometerse con un proveedor. El resultado es una **ficha de triaje** que el equipo jurídico puede presentar al área de tecnología o al comité de gobernanza con recomendaciones claras.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Extraer:
- ¿Hay nexo europeo confirmado? (Determina si el EU AI Act aplica)
- ¿Existe un umbral organizacional para EIPD-IA?
- ¿Quién es el responsable de gobernanza de IA?

Si el perfil no está configurado o tiene `[PLACEHOLDER]`: detener y pedir que ejecuten `/ia-governanza-legal-mexico:cold-start-interview`.

### 2. Recopilar información sobre el caso de uso

Si el usuario no la proporcionó como argumento, preguntar:

1. **¿Qué hace el sistema?** Descripción del funcionamiento técnico en términos generales.
2. **¿Qué datos procesa?** ¿Datos personales de clientes, empleados, público en general? ¿Datos sensibles (biométricos, salud, financieros)?
3. **¿Quién es afectado por los outputs?** ¿Clientes? ¿Empleados? ¿Público en general? ¿Personas vulnerables?
4. **¿El sistema toma o influye en decisiones sobre personas?** (ej., aprobación de crédito, selección de candidatos, contenido de feed, evaluación de riesgo, precios personalizados)
5. **¿En qué sector opera?** (biometría, infraestructura crítica, educación, empleo, servicios esenciales, aplicación de la ley, migración, justicia)
6. **¿Hay nexo europeo para este sistema específico?** (¿Los usuarios o afectados están en la UE?)
7. **¿Quién es el proveedor del sistema?** ¿Es un modelo de propósito general (LLM) o un sistema específico?

### 3. Clasificación EU AI Act

*(Solo si hay nexo europeo — ya sea a nivel organizacional o específico de este sistema)*

Aplicar la pirámide de riesgo del EU AI Act `[model knowledge — verify: EU AI Act guidance still emerging]`:

**🔴 PROHIBIDO (Art. 5) — BLOQUEANTE ABSOLUTO:**
Verificar si el sistema cae en alguna categoría prohibida:
- Sistemas de puntuación social por autoridades públicas basados en comportamiento
- Vigilancia biométrica en tiempo real en espacios públicos (con excepciones muy limitadas para fuerzas del orden)
- Técnicas subliminales que manipulan a personas sin su conciencia
- Explotación de vulnerabilidades de grupos específicos (niños, discapacitados)
- Inferencia de emociones en lugares de trabajo o educativos (con excepciones)
- Categorización biométrica para inferir características protegidas (raza, opinión política, religión, orientación sexual)
- Reconocimiento facial a partir de internet o CCTV para crear bases de datos de reconocimiento

Si hay algún indicio de prohibición → 🔴 **PROHIBIDO** — `[review]` — no proceder sin análisis legal detallado. Incluir el artículo específico que podría aplicar.

**🔴 ALTO RIESGO (Anexo III) — requiere cumplimiento completo:**
Verificar si el sistema cae en alguna categoría de Anexo III:
- Biometría: identificación, autenticación, categorización de personas físicas
- Infraestructura crítica: gestión de redes de energía, agua, transporte
- Educación: sistemas que determinan acceso, evaluación, clasificación de estudiantes
- Empleo: reclutamiento, selección, evaluación de desempeño, decisiones de ascenso/despido, monitoreo de trabajadores
- Servicios esenciales: scoring de crédito, evaluación de solicitudes de seguros, evaluación de solicitudes de asistencia pública
- Aplicación de la ley: evaluación de riesgo de reincidencia, detección de mentiras, análisis de pruebas
- Migración: evaluación de solicitudes de asilo, visas, permisos de residencia
- Administración de justicia: investigación de hechos, interpretación de la ley, aplicación de la ley

Si aplica → 🔴 **ALTO RIESGO** — requiere: registro en base de datos UE, EIPD-IA obligatoria, supervisión humana significativa, documentación técnica (Art. 11), datos de entrenamiento documentados (Art. 10), transparencia con afectados, conformidad del proveedor.

**🟡 RIESGO LIMITADO (Art. 50) — obligaciones de transparencia:**
- Chatbots que interactúan con personas → deben identificarse como IA
- Sistemas que generan contenido sintético (deepfakes, imágenes generadas) → deben etiquetarse
- Sistemas de reconocimiento de emociones en ciertos contextos → deben informar a los afectados
- Sistemas GPAI que generan contenido → marcado de contenido generado por IA

**🟢 RIESGO MÍNIMO — sin obligaciones específicas EU AI Act:**
La mayoría de las aplicaciones de IA: filtros de spam, sistemas de recomendación de contenido sin decisiones de alto riesgo, herramientas de productividad sin impacto en personas, modelos de predicción de demanda.

**⚪ GPAI / Modelo de propósito general (Art. 55):**
Si el sistema ES un modelo de propósito general (LLM como GPT-4, Gemini, Claude, etc.) — no una aplicación que usa un LLM, sino el modelo en sí: obligaciones de documentación y copyright para el proveedor. Como usuario/deployer del GPAI, las obligaciones dependen de para qué lo uses.

### 4. Marco mexicano

Independientemente del nexo europeo, verificar:

- **LGPDPPSP / LFPDPPP:** ¿El sistema procesa datos personales de personas en México? Si sí → requiere base de procesamiento, Aviso de Privacidad, y posiblemente EIPD bajo LGPDPPSP si hay decisiones automatizadas significativas.
- **LFT Art. 163:** ¿El sistema involucra creaciones o invenciones de empleados mexicanos? → reglas de titularidad aplicables.
- **COFECE:** ¿El sistema podría coordinarse con competidores (pricing algorithms, data sharing con competidores)? → riesgo de prácticas anticompetitivas.
- **CCF (responsabilidad civil):** ¿El sistema podría causar daños a terceros con outputs incorrectos? → verificar si la cadena de responsabilidad está clara.
- **LFDA:** ¿El sistema genera obras (textos, imágenes, código)? → la autoría de obras generadas por IA no está reconocida bajo LFDA; el output puede no estar protegido por derechos de autor.

### 5. Determinación de EIPD-IA

Determinar si se requiere Evaluación de Impacto de IA:

- **Obligatoria** si: el sistema es alto riesgo bajo EU AI Act (con nexo europeo), o si procesa datos personales en escala y toma decisiones automatizadas con efectos significativos sobre personas (LGPDPPSP Art. 22).
- **Recomendada** si: el sistema afecta a grupos vulnerables, tiene alto potencial de discriminación, o el proveedor no puede garantizar explicabilidad.
- **No requerida** si: riesgo mínimo, sin datos personales, sin decisiones sobre personas.

### 6. Ficha de triaje

Producir la ficha con el encabezado de confidencialidad del perfil de práctica, seguido de:

---

**FICHA DE TRIAJE DE CASO DE USO IA**

**Sistema evaluado:** [nombre/descripción]
**Proveedor:** [proveedor]
**Fecha de triaje:** [fecha]
**Clasificación EU AI Act:** [prohibido / alto riesgo / riesgo limitado / riesgo mínimo / GPAI / no aplica (sin nexo europeo)] `[model knowledge — verify: EU AI Act guidance]`
**Marco mexicano — riesgos identificados:** [LGPDPPSP / COFECE / CCF / LFDA / LFT / ninguno]

| Dimensión | Hallazgo | Severidad | Acción requerida |
|---|---|---|---|
| Nexo europeo | [aplica/no aplica/verificar] | | |
| Clasificación EU AI Act | [clase] | 🔴/🟠/🟡/🟢 | |
| Datos personales involucrados | [sí/no/qué tipo] | | |
| Decisiones automatizadas sobre personas | [sí/no/parcialmente] | | |
| EIPD-IA requerida | [sí/no/recomendada] | | |
| Cumplimiento del proveedor EU AI Act | [garantizado/no verificado/no aplica] | | |
| Transparencia con afectados | [requerida/no requerida] | | |
| Supervisión humana | [requerida/recomendada/no requerida] | | |
| Riesgo discriminación/sesgo | [alto/medio/bajo/no evaluado] | | |

**Recomendación:** [proceder sin restricciones / proceder con medidas de mitigación / pausar hasta obtener información adicional / no proceder]

**Próximos pasos recomendados:**
- [ ] [acción 1]
- [ ] [acción 2]

---

Nota del revisor estándar arriba del encabezado.

### 7. Actualizar el registro de casos de uso

Si el usuario aprueba proceder, agregar una entrada al registro en `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/use-case-register.yaml`:

```yaml
- id: AI-XXX
  nombre: "[nombre del sistema]"
  proveedor: "[proveedor]"
  proposito: "[propósito]"
  datos_personales: [true/false]
  clasificacion_eu_ai_act: "[prohibido/alto/limitado/minimo/gpai/na]"
  eipd_requerida: [true/false/recomendada]
  responsable: "[nombre]"
  fecha_triage: "[AAAA-MM-DD]"
  estado: "[en_evaluacion/aprobado/pausado/rechazado]"
```

Hacerlo sin narrar la acción — simplemente escribir el archivo y confirmar en la nota del revisor que se actualizó.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
