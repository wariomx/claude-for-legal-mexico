---
name: revision-confidencialidad
description: >
  Revisión de primera pasada de confidencialidad de documentos — hacer las clasificaciones
  obvias de secreto profesional e información confidencial, y señalar las difíciles para
  revisión del abogado, sin hacer juicios subjetivos. Usar cuando el usuario diga "revisar
  confidencialidad", "clasificar documentos", "revisar secreto profesional", o tenga un
  conjunto de documentos que clasificar antes de producción o entrega.
argument-hint: "[archivo de registro, o conjunto de documentos]"
---

# /revision-confidencialidad

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → protocolo de revisión, formato de clasificación.
2. Seguir el flujo de trabajo y referencia abajo.
3. Para cada entrada: obviamente confidencial / obviamente no confidencial / requiere revisión del abogado. Señalar razones.
4. Producto: registro revisado con señalamientos. El abogado revisa todos los señalamientos antes de producción.

---

# Revisión de Confidencialidad

## Marco jurídico mexicano de confidencialidad

México **NO tiene la doctrina de _work product_ (producto del trabajo)** del derecho estadounidense (FRCP 26(b)(3)). Tampoco aplica el _legal professional privilege_ del derecho inglés ni la doctrina _Akzo Nobel_ de la UE. El marco de protección aplicable en México es:

### Secreto profesional del abogado

- **Art. 36 de la Ley Reglamentaria del Art. 5° Constitucional Relativo al Ejercicio de las Profesiones en la Ciudad de México** — el profesionista está obligado a guardar secreto de los asuntos que le sean confiados por sus clientes. (Nota: leyes similares existen en cada estado.)
- **Arts. 210-211 del Código Penal Federal** — tipifican como delito la revelación de secretos. La revelación sin justa causa de secretos conocidos con motivo de la profesión es sancionable penalmente.
- **Art. 16 Constitucional** — derecho a la privacidad y protección de documentos y papeles.

**Alcance del secreto profesional mexicano:** protege las comunicaciones entre abogado y cliente realizadas con el propósito de obtener o prestar asesoría jurídica. Sin embargo:

- NO existe una protección generalizada de "documentos preparados en anticipación de litigio" (no hay _work product_).
- Los análisis internos, memoranda, evaluaciones de riesgo y documentos preparados por el equipo legal interno NO tienen protección automática — su protección depende de si constituyen comunicaciones confidenciales entre abogado y cliente.
- Las autoridades regulatorias mexicanas (COFECE, CNBV, INAI, SAT) tienen amplias facultades de investigación y pueden compeler la producción de documentos internos.

### Información confidencial protegida por ley

- **LGPDPPSP (Ley General de Protección de Datos Personales en Posesión de Particulares)** — datos personales y datos personales sensibles tienen protección especial. Su transferencia requiere consentimiento y aviso de privacidad.
- **LFPPI (Ley Federal de Protección a la Propiedad Industrial)** — secretos industriales y comerciales están protegidos. Arts. 163-169 LFPPI.
- **Ley del Mercado de Valores / regulación CNBV** — información privilegiada y reservada en materia bursátil.
- **Ley General de Transparencia / LFTAIP** — información reservada y confidencial del sector público.
- **Ley Federal del Trabajo** — datos laborales confidenciales.

### Facultades de autoridades regulatorias

**COFECE** (competencia económica): Puede realizar visitas de verificación (_dawn raids_), requerir información y documentos, y sancionar la no cooperación. Los documentos internos del equipo legal NO están automáticamente protegidos. La Ley Federal de Competencia Económica (Arts. 73-77) otorga amplias facultades de investigación.

**CNBV** (supervisión financiera): Facultades amplias de inspección y vigilancia bajo la Ley del Mercado de Valores y la Ley de Instituciones de Crédito.

**INAI** (protección de datos): Puede realizar procedimientos de verificación y requerir documentación sobre tratamiento de datos personales bajo la LGPDPPSP.

**SAT** (fiscal): Facultades de auditoría y requerimiento de documentación contable y fiscal.

**IMPI** (propiedad industrial): Facultades de investigación en materia de infracciones bajo la LFPPI.

## Restricciones de uso de documentos obtenidos en procedimientos

Antes de trabajar con documentos de litigio, preguntar: "¿Alguno de estos documentos fue obtenido a través de un procedimiento judicial o administrativo?" Si sí:

- Verificar si existe alguna orden de confidencialidad del juzgador sobre los documentos del expediente.
- Verificar si los documentos contienen datos personales protegidos por la LGPDPPSP.
- Verificar si los documentos contienen secretos industriales protegidos por la LFPPI.
- Confirmar: "Este uso es dentro del procedimiento en el que los documentos fueron obtenidos, o tengo permiso/consentimiento, o los documentos son públicos." Si no se confirma, señalar: "⚠️ Los documentos pueden tener restricciones de uso. Confirme que este uso está permitido antes de proceder."

## Contexto de asunto

**Contexto de asunto.** Verificar `## Espacios de trabajo por asunto` en el CLAUDE.md del nivel de práctica. Para litigacion-legal-mexico el valor por defecto es `Habilitado: ✓` — cada caso tiene su propio espacio de trabajo. Si `Habilitado` es `✗` (lo desactivó porque trabaja un caso a la vez), omitir este párrafo y usar contexto de nivel de práctica. Si habilitado y no hay asunto activo, preguntar: "¿Para cuál asunto es esto? Ejecute `/litigacion-legal-mexico:matter-workspace switch <slug>` o diga `nivel-de-práctica`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y anulaciones. Escribir productos en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` sea `on`.

---

## Propósito

Un registro de confidencialidad tiene tres tipos de entradas: obviamente confidenciales, obviamente no confidenciales, y las que necesitan análisis. Este skill clasifica los dos primeros tipos para que el tiempo del abogado se dedique enteramente al tercero.

**Esto es primera pasada. El abogado revisa cada señalamiento. Sin excepciones.**

## Fidelidad del expediente — referencias puntuales y cobertura de citas

Cuando este skill cita una norma, variante local o autoridad para una clasificación de confidencialidad, dos reglas aplican.

**Las citas puntuales deben soportar toda la proposición.** Si la revisión cita una norma para soportar una proposición de múltiples partes, verificar que la cita cubre cada elemento.

**Extraer todas las citas antes de verificar cualquiera.** Cuando esta revisión cita autoridad:

1. **Primera pasada: extraer.** Leer el documento y construir una lista de cada cita (normas, tesis, jurisprudencias, leyes). Reportar el conteo: "Encontré [N] citas."
2. **Segunda pasada: verificar.** Verificar cada una contra la fuente. No muestrear. No detenerse en las primeras cinco.
3. **Reportar cobertura.** "Verifiqué [N] de [M] citas. [K] no pudieron recuperarse — verificar manualmente. [J] confirmadas. [I] señaladas como posibles citas erróneas. [H] señaladas como mal fundamentadas (la cita existe pero no soporta la proposición)."
4. **Cuando el texto fuente no esté disponible, decir "no pude verificar," nunca "confirmado."**
5. **Los errores más difíciles son de soporte parcial.** Leer la proposición, leer la fuente, comparar elemento por elemento.

## Cargar contexto

`~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → formato de clasificación de confidencialidad, protocolo de revisión.

**Puerta de conflictos — no eludible.** Antes de revisar un registro de confidencialidad, verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rechazar y redirigir:

> "No veo [slug del asunto] en el registro de asuntos. Ejecute `/litigacion-legal-mexico:matter-intake` primero para que se ejecute la verificación de conflictos y se configure el espacio de trabajo del asunto. No revisaré un registro de confidencialidad de un asunto que no ha sido recibido — la verificación de conflictos es la puerta, y una revisión de confidencialidad es trabajo que necesita vivir en el expediente del asunto."

**La jurisdicción importa.** El alcance de la protección de confidencialidad, secreto profesional y las obligaciones de producción varían según el tipo de procedimiento (mercantil, civil, laboral, administrativo, amparo) y la autoridad ante la cual se litiga. Esta revisión aplica las reglas del foro especificado en la configuración. Si el asunto involucra un foro diferente, múltiples jurisdicciones, o un regulador con facultades especiales de investigación, las clasificaciones aquí pueden no transferirse.

## Paso 0: Investigar las reglas de confidencialidad del foro

**Antes de revisar entradas, investigar los requisitos de confidencialidad y producción documental del foro (código procesal aplicable, ley orgánica del regulador si aplica, y cualquier orden del juzgador sobre manejo de información confidencial). Identificar qué información puede clasificarse como confidencial y el procedimiento para hacerlo valer. Citar fuentes primarias.**

**Sin complemento silencioso.** Aplicar las mismas reglas que en otros skills: reportar, no llenar vacíos, ofrecer opciones.

**Atribución de fuentes.** Etiquetar cada referencia normativa y autoridad con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o la herramienta MCP; `[búsqueda web — verificar]` para citas web; `[conocimiento del modelo — verificar]` para citas de entrenamiento; `[proporcionado por usuario]` para citas del abogado. Nunca eliminar ni colapsar las etiquetas.

## Las clasificaciones

**Regla de tres estados. El skill nunca decide silenciosamente que un umbral subjetivo no se cumple.** En cualquier clasificación incierta — propósito dominante poco claro, contenido mixto legal/comercial, presencia de terceros ambigua — el skill mantiene la clasificación de confidencial y agrega una señal ⚠️ para el abogado. Sub-clasificar pierde protección (puerta de un solo sentido); sobre-clasificar es corregido por el abogado en revisión (puerta de dos sentidos). Preferir el error recuperable.

### Confidencial (✅) — mantener clasificación, sin señalamiento

- Comunicación directa entre abogado y cliente buscando/proporcionando asesoría jurídica (secreto profesional — Art. 36 Ley Reg. Art. 5°)
- Documentos que contienen datos personales sensibles protegidos por LGPDPPSP
- Documentos que contienen secretos industriales protegidos por LFPPI (Arts. 163-169)
- Comunicaciones internas del equipo legal sobre estrategia del asunto
- Información reservada clasificada por la organización conforme a normatividad aplicable

### Incierto — mantener clasificación Y señalar (✅ + ⚠️)

El valor por defecto para cualquier cosa que no esté confiadamente en ✅ o ❌. El skill no retira una clasificación de confidencialidad basado en su propia evaluación de un test subjetivo. Ejemplos:

- **Abogado interno haciendo trabajo legal y comercial** — ¿esta comunicación era asesoría jurídica o consejo de negocios? La clasificación del propósito dominante es del abogado, no del skill.
- **Tercero presente** — ¿el tercero está dentro del círculo de confidencialidad (co-abogado, perito contratado) o su presencia compromete la protección? Mantener la clasificación; señalar para el abogado.
- **Documentos de propósito mixto** — parte legal, parte comercial. ¿Redacción parcial? ¿Retención completa? ¿Producción? Mantener la clasificación; señalar para que el abogado decida el tratamiento.
- **Anexos** — analizar por separado y mantener la clasificación de cada anexo a menos que sea confiadamente ❌; señalar los que dependan de una clasificación subjetiva.
- **Documentos ante regulador** — las facultades de investigación de COFECE, CNBV, INAI u otro regulador pueden superar la protección de confidencialidad. Señalar: "Este documento puede ser compelido por [regulador] bajo [ley]. Señalar para revisión por especialista en la materia regulatoria."
- **Datos personales en contexto procesal** — verificar si la LGPDPPSP permite la transferencia en el contexto específico.

Cada señalamiento registra la pregunta abierta específica y la evidencia que corta en cada dirección, para que el abogado pueda decidir sin releer el documento en frío.

### No confidencial (❌) — recomendar retirar clasificación, pero registrar la evaluación

Solo para los casos inequívocos. El producto aún registra el razonamiento de la evaluación para que el abogado pueda verificar; no retira la clasificación del registro por su cuenta.

- Ningún abogado involucrado en ningún lugar
- Consejo de negocios donde un abogado fue copiado (copiar al abogado no hace confidencial la comunicación)
- Hechos subyacentes (los hechos no son confidenciales — las comunicaciones *sobre* hechos pueden serlo)
- Tercero copiado que claramente está fuera del círculo de confidencialidad
- Anexos que son independientemente no confidenciales (el correo puede ser confidencial; la hoja de cálculo de ventas adjunta no lo es)
- Documentos públicos (escrituras públicas, publicaciones del DOF, sentencias publicadas)

Si cualquiera de estos es *cercano* — el tercero podría ser un agente, la copia al abogado podría ser en realidad sobre una consulta jurídica — es incierto, no ❌. Enviar al grupo incierto y señalar.

## Flujo de trabajo

### Paso 1: Verificación de formato

¿El registro tiene lo que necesita?

| Campo | ¿Presente? |
|---|---|
| Fecha | |
| Autor | |
| Destinatarios (todos — PARA, CC, CCO) | |
| Tipo de documento | |
| Clasificación reclamada (secreto profesional, datos personales, secreto industrial, otro) | |
| Descripción (suficiente para evaluar sin revelar contenido confidencial) | |

Campos faltantes → señalar para completar antes de la revisión sustantiva.

### Paso 2: Entrada por entrada

Para cada entrada:

```
Entrada [N] ([ID del documento]): [✅ Confidencial | ✅ Confidencial + ⚠️ Señalamiento | ❌ No confidencial (evaluado)]
[Si ✅ (sin señalamiento): razón de una línea]
[Si ✅ + ⚠️: mantener clasificación; la pregunta específica que el abogado necesita responder; evidencia que corta en cada dirección]
[Si ❌: razón de una línea — pero la clasificación permanece en el registro hasta que el abogado la retire]
```

**Nunca producir una entrada que retire silenciosamente una clasificación de confidencialidad basada en la evaluación subjetiva del skill.** Un ❌ es una recomendación registrada junto al señalamiento; el abogado actúa sobre ella.

### Paso 3: Señalamientos de patrón

A través del registro:

- ¿Mismo problema repitiéndose? (Ej., mismo tercero en 50 entradas — una decisión resuelve 50 señalamientos)
- ¿Patrón de sobre-clasificación? (Si todo está clasificado sin diferenciación, señalar al abogado — pero la decisión de reducir el registro es del abogado, no del skill.)
- ¿Descripción insuficiente? (Descripciones tan vagas que un juzgador ordenaría revisión _in camera_)

## Producto

**Antes de que el registro de confidencialidad sea entregado a la contraparte o autoridad (el acto con consecuencias — esto incluye entregar el registro Y clasificar documentos como retenidos o producidos):** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No-abogado:

> Presentar una clasificación de confidencialidad y decidir la producción de documentos tiene consecuencias legales — sobre-clasificar puede resultar en sanciones y pérdida de credibilidad; sub-clasificar puede comprometer el secreto profesional o revelar información protegida de manera irrecuperable. ¿Ha revisado esto con un abogado? Si sí, proceder. Si no, aquí hay un resumen para llevarle:
>
> [Generar un resumen de 1 página: el asunto, conteos de entradas, los señalamientos ⚠️ y casos cercanos, observaciones de patrón (sobre-clasificación, descripciones vagas), postura de protección por tipo de información, qué podría salir mal en la producción, qué preguntar al abogado.]
>
> Si necesita encontrar un abogado litigante con licencia en su jurisdicción: el Colegio de Abogados o la Barra Mexicana de Abogados son un buen punto de partida.

No tratar el registro como listo para entregar sin un sí explícito. La revisión de primera pasada, clasificación y señalamiento no requieren la puerta — la entrega y producción sí.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

## Revisión de Confidencialidad: [Asunto] — [fecha]

**Norma aplicable:** [código procesal / ley orgánica del regulador / orden del juzgador — citas puntuales] `[INCIERTO — verificar vigencia]`
**Entradas revisadas:** [N]
**Resultados:** [N] ✅ confidencial confirmado / [N] ✅+⚠️ confidencial mantenido y señalado / [N] ❌ recomendar retirar (abogado confirma)

### ✅ + ⚠️ Señalados — clasificación mantenida, el abogado decide

| Entrada | ID del documento | Asunto | Evidencia a favor de confidencialidad | Evidencia en contra | Pregunta |
|---|---|---|---|---|---|
| [N] | [rango] | [qué es subjetivo] | [una línea] | [una línea] | [la decisión específica a tomar] |

### ❌ Recomendar retirar clasificación (abogado confirma antes de retirar)

| Entrada | ID del documento | Razón |
|---|---|---|

*Registrado, no ejecutado. El skill no retira clasificaciones de confidencialidad del registro — el abogado lo hace, después de revisar el razonamiento.*

### ✅ Confidencial (sin acción)

[Conteo. Lista disponible a solicitud.]

### Observaciones de patrón

[Problemas repetitivos, sobre-clasificación, problemas de descripción]

### Disciplina de marcadores

- `[VERIFICAR: aseveración fáctica sobre documento/custodio/fecha]`
- `[INCIERTO: clasificación de confidencialidad cercana / alcance de protección / cuestión doctrinal]`
- `[CITA NECESARIA: norma, variante local o autoridad que soporte una clasificación]`

---

**El abogado debe revisar todos los ⚠️ y ❌ antes de cualquier acción.**

**Material confidencial fuente.** Esta revisión lee entradas y documentos subyacentes que son, por definición, material candidato a protección de confidencialidad. El producto de la revisión hereda ese estatus — mantener con materiales confidenciales, marcar apropiadamente, y no circular fuera del círculo de confidencialidad. Distribuirlo puede comprometer la protección misma.
```

## Lo que este skill enfáticamente NO hace

- Hacer clasificaciones cercanas. ⚠️ significa "un humano decide." En cualquier test subjetivo (propósito dominante, contenido mixto legal/comercial, alcance de la protección ante reguladores) el skill mantiene la clasificación de confidencialidad y señala.
- Retirar una clasificación de confidencialidad del registro basada en su propia evaluación. ❌ es una *recomendación* registrada para el abogado, no una acción tomada contra el registro.
- Producir o retener documentos. Asesora; el abogado decide; el abogado actúa.
- Garantizar corrección en las clasificaciones ✅. El abogado es responsable del registro. Esto es una primera pasada.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, observar y esperar, otra cosa) son un punto de partida, no un candado. El árbol es el producto; el abogado elige.
