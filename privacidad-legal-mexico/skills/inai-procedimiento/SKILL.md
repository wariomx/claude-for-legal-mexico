---
description: >
  Prepara la postura y documentos para procedimientos ante el INAI —
  requerimiento de cumplimiento, recurso de revisión (Art. 49 LFPDPPP),
  recurso de inconformidad, y comparecencia ante el Pleno. Identifica los
  plazos del procedimiento y la estrategia de defensa del responsable.
argument-hint: "[--tipo requerimiento|recurso-revision|verificacion|inconformidad]"
---

# /inai-procedimiento

## Cuándo se ejecuta

El responsable ha recibido una notificación del INAI (requerimiento, apertura de procedimiento de verificación, o traslado de recurso de revisión interpuesto por un titular), o está considerando la interposición de un recurso. El skill ayuda a clasificar el procedimiento, calcular plazos, identificar defensas, y redactar la respuesta o postura.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público) — determina la ley aplicable y los recursos disponibles
- Sector o industria — factores sectoriales que el INAI puede considerar al graduar sanciones
- Historial de procedimientos ante el INAI (folio y tipo)
- Despacho externo designado para litigio ante INAI

Si el perfil no existe, continuar con advertencia: "Sin perfil de práctica configurado — responderé con el marco general. Para análisis calibrado a tu organización, ejecuta `/privacidad-legal-mexico:cold-start-interview`."

### 2. Clasificar el tipo de procedimiento

Si `--tipo` no fue especificado, preguntar: "¿Qué notificación recibiste del INAI? Puedes pegar el encabezado del oficio o describirme el procedimiento."

**Tipos de procedimiento y sus características:**

#### A. Requerimiento de cumplimiento (Art. 52 LFPDPPP)
El INAI solicita al responsable que corrija una conducta. El plazo de respuesta está indicado en el oficio de requerimiento. `[review: plazo ARCO — verificar plazo específico en el oficio de requerimiento]`
- Estrategia: responder dentro del plazo con evidencia de cumplimiento o argumentos de improcedencia.
- Si el responsable no cumple: el INAI puede imponer medidas correctivas y abrir procedimiento de infracción.

#### B. Recurso de revisión interpuesto por titular (Art. 49 LFPDPPP)
El titular impugna ante el INAI la respuesta del responsable a su solicitud ARCO (la negó, no respondió, o respondió indebidamente). El responsable tiene **15 días hábiles** para remitir al INAI el expediente ARCO completo y sus argumentos de defensa. `[settled — last confirmed 2026-05-24]`
- El INAI tiene 40 días hábiles para resolver. `[model knowledge — verify plazo actual de resolución]`
- Estrategia: demostrar que la respuesta ARCO fue oportuna, completa y correcta, o que aplica una excepción legal.

#### C. Procedimiento de verificación (Art. 55 LFPDPPP)
Investigación iniciada de oficio por el INAI para verificar el cumplimiento general de la LFPDPPP. Puede surgir de una denuncia, de medios de comunicación, o de inspección sectorial.
- Estrategia: colaborar con el INAI, presentar evidencia de cumplimiento, y demostrar buena fe.

#### D. Recurso de inconformidad (LGPDPPSOH)
Disponible cuando el responsable es un sujeto obligado del sector público (dependencia o entidad de la APF, estado o municipio). `[model knowledge — verify aplicabilidad al caso concreto y si la LGPDPPSOH es la ley vigente]`
- Ante el Pleno del INAI como órgano garante.

### 3. Extracción de hechos del expediente

Pedir al usuario que comparta (o describa) el expediente disponible y extraer:

| Elemento del expediente | Valor |
|---|---|
| Número de folio / expediente INAI | |
| Fecha de notificación al responsable | |
| Nombre del titular (si aplica) | |
| Derecho ejercido en la solicitud ARCO original | Acceso / Rectificación / Cancelación / Oposición |
| Fecha de la solicitud ARCO original | |
| ¿El responsable respondió? | Sí (fecha: ) / No / Extemporáneamente |
| Contenido de la respuesta del responsable | |
| Argumentos del titular en el recurso | |
| Fundamento legal invocado por el INAI | |

### 4. Análisis de defensas procedimentales y de fondo

**Defensas procedimentales — verificar primero:**

- ¿La solicitud ARCO original fue presentada conforme al Art. 29 LFPDPPP? (por el canal correcto, con identificación del titular, con descripción suficiente del derecho ejercido)
- ¿El responsable respondió dentro del plazo de 20 días hábiles? `[settled — last confirmed 2026-05-24]`
- ¿El recurso de revisión fue presentado por el titular dentro del plazo de 15 días hábiles posteriores a la respuesta del responsable o al vencimiento del plazo? `[model knowledge — verify plazo del titular para interponer recurso]`
- ¿El recurso de revisión fue presentado ante el órgano competente?

**Defensas de fondo — aplicar si las procedimentales no son suficientes:**

Verificar si aplica alguna de las excepciones de los Arts. 34-36 LFPDPPP `[model knowledge — verify excepciones aplicables al caso concreto]`:

| Excepción | ¿Aplica? | Evidencia de soporte |
|---|---|---|
| Los datos son necesarios para cumplir una obligación legal | `[review]` | |
| Los datos son necesarios para la ejecución de un contrato con el titular | `[review]` | |
| Existe resolución judicial o administrativa que ordena conservar los datos | `[review]` | |
| Los datos son necesarios para la defensa en procedimiento judicial | `[review]` | |
| La cancelación puede causar perjuicio a terceros | `[review]` | |
| Los datos forman parte de expediente médico (para cancelación) | `[review]` | |
| Investigación en curso por organismos públicos competentes | `[review]` | |

Marcar cada excepción con `[review]` — la determinación de si una excepción aplica es un juicio jurídico que requiere criterio del abogado y respaldo documental.

### 5. Estructura del escrito de respuesta

Producir el borrador con la siguiente estructura:

1. **Encabezado:** Autoridad a quien se dirige, folio del expediente, datos del responsable, domicilio para notificaciones.
2. **Hechos:** Narración cronológica objetiva — fecha de solicitud ARCO, fecha de respuesta, contenido de la respuesta, argumentos del titular en el recurso.
3. **Argumentos de derecho:** Defensas procedimentales primero; defensas de fondo en subsidio; excepciones legales aplicables con cita de artículo y fracción.
4. **Pruebas ofrecidas:** Lista de documentos que se acompañan — acuse de recibo de la solicitud ARCO, respuesta enviada al titular, evidencia del cumplimiento o la excepción, otros.
5. **Puntos petitorios:** Solicitar expresamente que se declare improcedente el recurso / que se confirme la respuesta del responsable / que se archive el expediente.

Marcar con `[review]` cada argumento cuya procedencia dependa de hechos no confirmados o de criterios discrecionales del INAI.

### 6. Calendario de plazos

Calcular y listar todos los plazos críticos del procedimiento:

| Evento | Fecha | Plazo |
|---|---|---|
| Fecha de notificación al responsable | | |
| Vencimiento del plazo de respuesta | | `[review: plazo ARCO — verificar días hábiles y días inhábiles INAI]` |
| Fecha estimada de resolución del INAI | | `[model knowledge — verify plazo actual]` |
| Plazo para impugnar resolución del INAI (si desfavorable) | | `[model knowledge — verify recurso disponible y plazo]` |

**REGLA DURA:** Los plazos ante el INAI son de días hábiles conforme al calendario de la institución — verificar el calendario de días inhábiles publicado por el INAI. Missing a deadline generally means losing the argument regardless of merit.

### 7. Exposición a sanciones

Si el procedimiento puede derivar en sanción, informar el rango aplicable:

- Arts. 63-64 LFPDPPP establecen multas de hasta 320,000 días de salario mínimo general vigente en el Distrito Federal para las infracciones más graves. `[model knowledge — verify valor actual de la UMA y el factor de días aplicable]`
- Factores de graduación: gravedad de la infracción, carácter intencional o culposo, antecedentes del responsable, capacidad económica, daño causado a los titulares.
- Para datos sensibles o de menores: el INAI aplica el rango más alto de la escala.

### 8. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Folio INAI:** [número de expediente]
> - **Tipo de procedimiento:** [requerimiento / recurso de revisión / verificación / inconformidad]
> - **Plazo crítico:** `[review: plazo vence AAAA-MM-DD — verificar calendario INAI y días inhábiles]`
> - **Defensas identificadas:** [N procedimentales / N de fondo / ninguna — solo mitigación]
> - **Marcado para tu criterio:** [N elementos marcados `[review]` en línea]
> - **Antes de presentar el escrito:** Confirmar plazo exacto con el oficio de notificación, verificar que se adjuntan todas las pruebas, aprobar con [responsable según perfil o despacho externo]

### 9. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Finalizar el escrito de respuesta** — Revisaré el borrador y produciré la versión final para firma y presentación ante el INAI.
> 2. **Profundizar en una defensa** — Desarrollo el argumento legal de la excepción más sólida con más detalle y referencia a resoluciones del INAI en casos similares.
> 3. **Evaluar si hay base para allanarse** — Analizo si conviene reconocer el incumplimiento, comprometerse a corregirlo, y solicitar al INAI un trato atenuado.
> 4. **Preparar la presentación ante el Pleno** — Si el procedimiento llegó a esa instancia, redacto los puntos de comparecencia y la estrategia de exposición oral.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
