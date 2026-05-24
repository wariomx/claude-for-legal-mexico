---
name: demand-draft
description: Redactar una carta de requerimiento a partir de un intake completado, con compuerta de confidencialidad / admisión / conciliación, salida en .docx, checklist post-envío y oferta de crear asunto. Usar cuando el usuario diga "redacta el requerimiento", "escribe la carta de [tipo]", o tenga un intake terminado listo para convertir en borrador enviable.
argument-hint: "[slug] [--skip-gate] [--version=N]"
---

# /demand-draft

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/intake.md`. Rechazar si falta o si el bloque estratégico está vacío (para requerimientos materiales).
2. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → práctica de cartas de requerimiento, estilo de casa, tabla de documentos semilla.
3. Seguir el flujo de trabajo y la referencia de abajo.
4. Ejecutar la compuerta pre-redacción: filtro de confidencialidad, riesgo de admisión, transacción, postura de conciliación, escaneo de renuncia al secreto profesional, tono, exactitud fáctica. No proceder hasta que cada punto sea atendido.
5. Selección de plantilla: documento semilla si se proporcionó en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`; si no, plantilla flexible para el tipo de requerimiento.
6. Redactar en chat para revisión. Iterar hasta aprobación del usuario.
7. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/draft-v[N].docx` usando el skill docx.
8. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/checklist.md` (checklist post-envío).
9. Evaluar materialidad según heurística; ofrecer crear un asunto. Si acepta: entregar a `matter-intake` con campos pre-poblados.

---

# Redacción de Requerimiento

## Propósito

Tomar un intake completado y producir un borrador enviable. La mayor parte del valor está en rehusarse a redactar hasta que la confidencialidad, el riesgo de renuncia al secreto profesional, la admisión y la postura de conciliación hayan sido conscientemente abordados — el modo de falla es una carta que compromete el secreto profesional o constituye un reconocimiento de adeudo porque nadie se detuvo a verificar.

## Fidelidad al registro — citas y referencias precisas

Las cartas de requerimiento son abogacía, y cada línea citada de un contrato, un correo o una comunicación previa se convierte en una aserción que la contraparte va a verificar. Declaración canónica en las salvaguardas compartidas del CLAUDE.md del plugin; repetida aquí.

**Las citas textuales deben ser textuales.** Nunca poner comillas alrededor de palabras atribuidas a la contraparte, su abogado, un testigo o cualquier documento a menos que tengas el pasaje exacto frente a ti. Cuando quieras caracterizar sin las palabras exactas:

- **Parafrasear sin comillas**, con un marcador: "Su correo del [fecha] señaló X `[verificar cita exacta — referencia de correo pendiente]`."
- **Nunca llenar el vacío.** Una disposición contractual mal citada en un requerimiento es la forma más rápida de perder credibilidad ante el abogado contrario en la primera ronda.
- Cada `[verificar cita exacta]` debe señalarse en la nota de revisión antes de que la carta salga.

**Las citas puntuales deben respaldar toda la proposición.** Si el requerimiento afirma "La Cláusula 4.2 requiere el pago dentro de 30 días a partir de la recepción de la factura," la cláusula citada debe cubrir la obligación Y el detonante Y el plazo. Si solo cubre uno, dividir la cita (e.g., "Cláusula 4.2 (obligación de pago); Cláusula 4.3 (plazo de 30 días)") o acotar la proposición. Una cita contractual que respalda solo parte del reclamo es cómo la contraparte responde con el texto completo e invierte la postura.

## Franqueza sobre argumentos débiles

Cuando la ley o el registro van en contra de un punto, no disfrazarlo como sólido. Cuando un argumento en el requerimiento es débil — el lenguaje contractual es ambiguo, la autoridad va en sentido contrario, la teoría de daños es un estiramiento — señalarlo para el firmante:

> "El [reclamo / teoría] aquí es débil porque [autoridad / hecho]. Opciones: (a) presionar y enmarcar como `[encuadre alternativo]`, (b) eliminarlo y apoyarse en [reclamo más fuerte], (c) mantenerlo como gancho pero matizar el lenguaje. `[revisar — decisión estratégica]`."

Un requerimiento que sobreafirma recibe una respuesta que cataloga cada exceso, desplaza el apalancamiento y quema la siguiente ronda. El requerimiento más fuerte es el que concede lo débil para que la contraparte no pueda hacerlo.

## Eco vs repetición

Si el asunto tiene correspondencia previa, hacer eco de los términos clave — la misma caracterización del incumplimiento, el mismo encuadre de la obligación principal, el mismo nombre para la transacción. No copiar oraciones enteras. Un requerimiento que lee como copia-pega del anterior señala que nada ha cambiado; la nueva carta debe avanzar la postura (nuevos hechos, nuevo plazo, nueva consecuencia), no reiterarla.

> **Entregable externo:** la carta de requerimiento redactada se envía a la contraparte. NO incluir un encabezado de `CONFIDENCIAL — SECRETO PROFESIONAL — PREPARADO BAJO LA DIRECCIÓN DEL ABOGADO` en la carta saliente. El checklist post-envío y el archivo de intake son producto de trabajo interno y sí llevan el encabezado.

## Contexto de lado

Redactar un requerimiento es inherentemente una aserción — el remitente está haciendo un reclamo. Leer `## Lado` en el perfil de práctica:

- **Actor / demandante** (default para este skill): demand-draft se alinea con la postura. La carta es el reclamo. Tono, lenguaje de consecuencias y reparación demandada fluyen del manual del lado actor.
- **Demandado / parte requerida**: los requerimientos desde la defensa son menos comunes pero ocurren — un litigante de defensa puede enviar un contra-requerimiento, una demanda de contribución o un requerimiento en un asunto no relacionado. Confirmar antes de redactar: "Tu default es defensa. ¿Este asunto es postura de actor para ti (estás afirmando un reclamo), o es una postura diferente?"
- **Ambos / varía**: preguntar por cada redacción qué postura aplica. El tono y el firmante default pueden diferir.

Para abogados internos de defensa que reciben más requerimientos de los que envían, redirigir a `demand-received` — ese skill maneja el caso de triaje de requerimientos recibidos.

## Postura para este asunto

Antes de la compuerta pre-redacción, confirmar la postura del asunto. El tono y los términos de un requerimiento son caso por caso, no un default de práctica. Confirmar con el usuario (leyendo la sección `## Postura` del intake si existe; preguntando si no):

> **Postura para este asunto.** El tono y los términos de una carta de requerimiento son caso por caso, no un default de práctica. Preguntar:
> - **Tono:** mesurado / asertivo / agresivo? (depende de la relación, el monto y la probabilidad de juicio)
> - **Plazo de respuesta:** ¿qué es razonable dado el reclamo? (15 días es común para requerimientos de pago; 30 días para saneamiento; 5-10 días para cesación — pero el contrato o la ley pueden fijar otro)
> - **Formalidad:** ¿requiere acta circunstanciada ante fedatario público? ¿Correo certificado? ¿Notificación personal? (determina el valor probatorio)
> - **Firmante:** tú, el cliente, el Director Jurídico, despacho externo?
> No asumir. Leer la correspondencia previa de requerimientos si la hay — establece el registro de tono.

Las respuestas determinan la selección de verbos de tono, el lenguaje de consecuencias, la formalidad del documento, el bloque de firma y el plazo de cumplimiento. Una postura no capturada en el intake se captura aquí — no recurrir a un default de práctica.

## Supuesto jurisdiccional

Esta redacción asume la jurisdicción identificada en el intake y el marco procesal aplicable del foro. Las reglas legales, plazos, costas, intereses moratorios y fundamentos legales varían materialmente por jurisdicción (federal vs. estatal, mercantil vs. civil vs. laboral). Si los hechos subyacentes tocan un foro diferente, el domicilio de la contraparte en otro estado, o una cuestión de ley aplicable, la redacción puede no aplicar tal cual — confirmar antes de enviar.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/intake.md` — requerido; rechazar si falta
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → Práctica de cartas de requerimiento (rutas de documentos semilla, tiempos de notificación a aseguradora, umbral de materialidad para creación de asunto), estilo de casa (marcas de confidencialidad, formato de directivas a despacho externo para referencia de tono). **Tono, plazo de cumplimiento, formalidad y firmante vienen de `## Postura para este asunto` — son de nivel asunto, no de nivel práctica.**
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — para verificar asuntos relacionados existentes (misma contraparte) y ofrecer enlace cruzado

### Manejo de bloque estratégico omitido

Si el intake tiene `strategic_block: skipped` o `partial`, preguntar al usuario antes de ejecutar la compuerta pre-redacción:

> El intake omitió [todo / parte] del bloque estratégico (apalancamiento, BATNA, tono, filtros de confidencialidad). Redactar ahora producirá una carta utilizable pero las secciones estratégicas serán genéricas y marcadas con `[VERIFICAR SME]`.
>
> - **Completar bloque estratégico ahora** — pausar, regresar a `/demand-intake [slug] --resume-strategic`
> - **Proceder de todos modos** — continuar a compuerta pre-redacción; secciones posteriores marcadas

Si "proceder de todos modos," cada sección de la redacción que depende de una pregunta estratégica omitida lleva `[VERIFICAR SME: [pregunta específica]]` en línea.

## Banderas

- `--skip-gate` → omitir el checklist pre-redacción. Disponible pero se registra; usar solo cuando el checklist se ejecutó por separado y está documentado.
- `--version=N` → redactar como `draft-vN.docx` (default: siguiente número de versión)

## La compuerta pre-redacción

**Esto se ejecuta antes de cualquier redacción. Si el usuario no lo atiende, detener.**

```
CHECKLIST PRE-REDACCIÓN — [slug]

1. Filtro de confidencialidad
   Según filtros del intake: [lista]
   Confirmar: ¿ninguno de estos aparecerá en la redacción?  [s/n]

2. Riesgo de admisión
   Según riesgo del intake: [lista]
   Para cada uno, ¿la redacción está controlada o eliminada?  [s/n por elemento]

3. Riesgo de transacción
   Según intake: [riesgo señalado, si hay]
   ¿El requerimiento constituye inadvertidamente una transacción (Arts. 2944-2963
   CCF) o un reconocimiento de adeudo (Art. 1168 CCF) que afecte nuestra posición?  [s/n]

4. Postura de conciliación
   Identificar los mecanismos de resolución alternativa aplicables al foro.
   NOTA: en México las tratativas previas (discusiones de arreglo) NO tienen
   protección exclusionaria automática — lo dicho puede utilizarse como prueba.
   Laboral: conciliación prejudicial obligatoria ante CFCRL (Art. 684-A LFT).
   Comercial: mediación opcional; arbitraje bajo Cód. de Comercio Título IV.
   Intake dice: [apertura a convenio / aserción pura / caso por caso]
   La redacción reflejará la postura, cuidando que cualquier declaración pueda
   ser presentada como prueba en juicio.
   Confirmar.

5. Escaneo de renuncia al secreto profesional
   ¿Alguna oración en la redacción revelará la sustancia de nuestro análisis legal
   interno (no solo la conclusión)?  [s/n]
   Si sí, reformular antes de redactar.

6. Postura de tono
   Intake dice: [preservar-relación / mesurado / confrontativo]
   Esto determinará selección de verbos, encuadre y lenguaje de consecuencias.
   Confirmar.

7. Exactitud fáctica
   Cada hecho en la redacción debe estar verificado. No "probablemente cierto" —
   verificado. Listar hechos no verificados; serán marcados [VERIFICAR: ___] en línea.
```

Solo proceder cuando el usuario haya atendido cada punto. Un checklist aceptado en blanco es peor que ningún checklist.

## Selección de plantilla

### Paso 1: Documento semilla

Verificar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → Práctica de cartas de requerimiento → tabla de documentos semilla para el tipo de requerimiento del intake.

- **Documento semilla proporcionado:** leerlo. Igualar estructura, tono, bloque de firma, marcas de confidencialidad, orden de secciones. El documento semilla es la plantilla.
- **Sin documento semilla:** usar la plantilla flexible de abajo para el tipo de requerimiento.

### Paso 2: Plantillas flexibles (solo cuando no hay documento semilla)

Cada una es un esqueleto — encabezados y contenido esperado. Desviarse cuando los hechos lo requieran.

**Esqueleto de requerimiento de pago:**
1. Partes y contexto de la relación (1 párrafo)
2. Hechos — la obligación y su fuente (contrato cláusula / factura / pedido), fechas
3. El incumplimiento — qué se adeuda, cuándo venció, qué ocurrió (o no)
4. Intereses moratorios — referencia a tasa legal (Art. 362 Código de Comercio para mercantil; tasa legal civil según código estatal) `[CITA: ley/artículo]`
5. Requerimiento — monto específico, plazo, método de pago
6. Consecuencias — ejercicio de acciones legales, intereses, costas, vía ejecutiva si procede
7. Aviso de conservación (si aplica)
8. Bloque de firma

**Esqueleto de incumplimiento / saneamiento:**
1. Partes y contrato (identificar — fecha de celebración, partes)
2. La obligación alegada como incumplida — cláusula del contrato, lenguaje llano
3. El incumplimiento — hechos específicos, fechas, evidencia disponible
4. Saneamiento — qué específicamente lo remediaría; plazo de saneamiento (contractual o razonable)
5. Consecuencias de no sanear — rescisión (Art. 1949 CCF), daños y perjuicios (Arts. 2104-2118 CCF), cláusula penal si pactada `[CITA: ley/artículo]`
6. Reserva de derechos
7. Bloque de firma

**Esqueleto de cesación (propiedad intelectual):**
1. Partes y nuestros derechos (marca/derecho de autor/patente/secreto industrial — identificar el derecho y su fundamento en LFPPI o LFDA) `[CITA: ley/artículo]`
2. Los actos infractores — actos específicos, fechas, evidencia
3. Requerimiento — cesación inmediata, retiro de productos/materiales, rendición de cuentas sobre uso pasado, confirmación por escrito del cumplimiento
4. Plazo de cumplimiento
5. Consecuencias del incumplimiento — demanda de infracción, medidas cautelares ante IMPI, indemnización por daños y perjuicios, multas administrativas `[CITA: LFPPI artículos aplicables]`
6. Requerimiento de preservación (documentos, metadatos, sistemas relacionados con la conducta alegada)
7. Bloque de firma

**Esqueleto de aviso de rescisión laboral:**
1. Partes y contexto de la relación laboral (trabajador, fechas de empleo, puesto)
2. Las causales de rescisión — artículo 47 LFT, fracciones específicas aplicables `[CITA: Art. 47, fracción ___, LFT]`
3. Los hechos específicos que configuran la causal — con referencia al acta administrativa si existe
4. Aviso por escrito — debe entregarse dentro de 5 días hábiles siguientes a la fecha de rescisión (Art. 47 último párrafo LFT); la falta de aviso hace presumir que el despido fue injustificado `[model knowledge — verify]`
5. Consecuencias de no dar aviso oportuno — se presume despido injustificado y el trabajador tiene derecho a indemnización constitucional (3 meses de salario) + 20 días por año + prima de antigüedad (Art. 48 LFT) `[model knowledge — verify]`
6. Oferta de resolución informal (solo si estratégicamente apropiado — considerar conciliación)
7. Referencia a entrega de finiquito / liquidación
8. Bloque de firma

**Esqueleto de preservación:**
1. Partes y contexto — qué disputa se anticipa o está en curso
2. Alcance — categorías de documentos, datos, sistemas, comunicaciones
3. Custodios — personas nombradas que se espera tengan material relevante
4. Rango de fechas
5. Obligación afirmativa de conservación — suspender eliminación automática, preservar metadatos, preservar dispositivos (fundamento: Arts. 46-49 Código de Comercio para comerciantes) `[CITA: ley/artículo]`
6. Consecuencias de destrucción — presunción adversa, obstaculización de la justicia
7. Solicitud de acuse de recibo
8. Bloque de firma

## Reglas de redacción

0. **Default para contratos de entregas parciales en disputas comerciales.** Para cualquier requerimiento de incumplimiento de contrato que involucre un contrato de entregas parciales o sucesivas bajo el Código de Comercio, distinguir entre el incumplimiento de una entrega específica y el incumplimiento que afecta sustancialmente la totalidad del contrato.

   En contratos de compraventa mercantil con entregas parciales:

   - Fundamentar en las disposiciones del Código de Comercio sobre compraventa mercantil (Arts. 371-387) y las disposiciones supletorias del CCF sobre obligaciones `[CITA: Código de Comercio / CCF artículos aplicables]`
   - Distinguir: ¿el incumplimiento es de una entrega específica (reclamación parcial) o afecta sustancialmente el objeto del contrato (rescisión total bajo Art. 1949 CCF)?
   - Si hay cláusula penal pactada, invocarla (Arts. 1840-1846 CCF). Si no, fundamentar daños y perjuicios (Arts. 2104-2118 CCF) `[CITA: ley/artículo]`
   - Señalar para el firmante en un bloque `[NOTA AL FIRMANTE:]` sobre la redacción: "Esta carta distingue entre incumplimiento parcial de una entrega y rescisión total del contrato. Confirmar la estructura de entregas del contrato antes de enviar."
   - Si la estructura de entregas no es clara del intake, marcar `[VERIFICAR: ¿es un contrato de entregas parciales o una entrega única dividida por conveniencia logística?]` — no afirmar silenciosamente que aplica uno u otro régimen.

1. **Especificidad sobre adjetivos.** "El 14 de marzo de 2026, usted envió X" supera a "Usted repetida e indebidamente envió X." Los adjetivos son la señal del redactor de que los hechos son delgados.

2. **Hechos rastreables a fuentes.** Cada aserción fáctica se mapea a un documento, fecha o testigo. Si no es verificable aún: `[VERIFICAR: afirmación específica]`.

3. **Citas como marcadores.** `[CITA: ley/artículo/fracción]` donde va la autoridad legal. No inventar citas. Si el usuario proporcionó autoridades en el intake, usarlas fielmente.

4. **Lenguaje de consecuencias según postura de tono.**
   - `preservar-relación`: "Confiamos en resolver esta situación sin necesidad de recurrir a instancias legales."
   - `mesurado`: "De no atender este requerimiento en el plazo señalado, nos veremos en la necesidad de ejercer las acciones legales que correspondan."
   - `confrontativo`: "El incumplimiento al presente requerimiento en el plazo de [N] días dará lugar al ejercicio inmediato de las acciones legales procedentes, incluyendo [recurso específico]."

5. **Redacciones alternativas en línea.** Donde el tono podría variar, la redacción incluye una alternativa compacta. Formato:
   > *La factura adjunta por la cantidad de $X permanece impagada.* [o más asertivo: *Ha incurrido usted en incumplimiento de pago respecto de la factura adjunta por $X, con vencimiento el [fecha].*]

6. **No discusión de arreglo en el registro sin intención.** Si el intake señaló la comunicación como aserción pura de derechos (sin postura conciliatoria), la redacción no incluye ninguna oferta de transigir, ni lenguaje que pudiera caracterizarse como oferta de convenio. Recordar que en México las tratativas previas no tienen protección exclusionaria — cualquier oferta o concesión puede ser presentada como prueba en juicio.

7. **Marcas de confidencialidad según estilo de casa.** Aplicar las convenciones de confidencialidad de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` exactamente.

## Salida

### Primario: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/draft-v[N].docx`

Usar el skill `docx` para producir un .docx con formato de carta:
- Membrete / bloque de dirección del remitente
- Fecha y lugar
- Bloque de dirección del destinatario
- Línea de referencia (concisa; no revelar estrategia confidencial)
- Saludo
- Cuerpo (según plantilla + reglas de redacción)
- Cierre
- Bloque de firma según intake

### Revisión en chat

Mostrar la redacción como texto plano legible para que el usuario revise y solicite ediciones. Iterar antes de escribir el .docx final. Una vez aprobado, escribir a disco.

### Compuerta de envío (nota de cierre en la redacción)

Agregar lo siguiente, separado del cuerpo, a la presentación en chat y a cualquier vista previa interna — se elimina antes de que la carta salga:

> Este es un borrador de carta de requerimiento para revisión del abogado, no una carta lista para enviar. Enviarlo puede constituir una interpelación formal (mora — Art. 2080 CCF), detonar intereses moratorios (Art. 362 Código de Comercio), e interrumpir el cómputo de prescripción. Un abogado con cédula profesional vigente revisa, edita y asume la responsabilidad profesional antes del envío. No enviar este borrador sin revisión.

### Verificación de citas

Cada marcador `[CITA:___]` — y cualquier cita tomada del intake o del documento semilla — no está verificada hasta que un humano la consulte contra la fuente primaria. Antes de enviar, ejecutar un paso de verificación: verificar cada ley, artículo, fracción, tesis y jurisprudencia contra una herramienta de investigación legal (SCJN IUS / Semanario Judicial de la Federación, DOF, o la plataforma de tu despacho) para exactitud, vigencia e historial legislativo. Citas fabricadas o mal citadas en requerimientos enviados y documentos presentados ante tribunales han resultado en responsabilidad profesional.

**Atribución de fuente.** Etiquetar cada cita en la redacción con su procedencia: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o el nombre de la herramienta MCP específica para citas obtenidas vía conector de investigación legal; `[búsqueda web — verificar]` para citas encontradas por búsqueda web; `[conocimiento del modelo — verificar]` para citas recordadas de datos de entrenamiento; `[proporcionado por usuario]` para citas suministradas en el intake o documento semilla. Las citas etiquetadas `verificar` tienen mayor riesgo de fabricación que las obtenidas por herramienta y deben verificarse primero. Nunca eliminar o colapsar las etiquetas — son la señal más rápida del firmante sobre qué citas verificar antes de enviar.

**Sin suplemento silencioso.** Si una consulta de investigación a la herramienta legal configurada (SCJN IUS, Semanario Judicial, DOF, o plataforma del despacho) devuelve pocos o ningún resultado para una autoridad que la redacción necesita, reportar lo encontrado y detenerse. NO llenar el vacío con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece delgada para [tema]. Opciones: (1) ampliar la consulta, (2) probar una herramienta diferente, (3) buscar en la web — los resultados se etiquetarán `[búsqueda web — verificar]` y deben verificarse contra fuente primaria antes de confiar, o (4) dejar el marcador `[CITA:___]` y detenerse aquí. ¿Cuál prefieres?" El abogado decide si acepta fuentes de menor confianza; el skill no decide por ellos.

### `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/checklist.md` — el checklist post-envío

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`. Este encabezado aplica al archivo de checklist interno; la carta saliente NO lo lleva.]

# Checklist Post-Envío — [slug]

**Versión de redacción enviada:** [v1 / v2 / etc.]
**Fecha de envío:** [YYYY-MM-DD — se llena después del envío]
**Firmante:** [nombre]

## Pre-envío (antes de que la carta salga)

- [ ] Lectura final por el firmante
- [ ] Exactitud fáctica: todos los marcadores [VERIFICAR] resueltos
- [ ] Citas: todos los marcadores [CITA] llenados y verificados contra fuente primaria (confirmar vigencia)
- [ ] Marcas de confidencialidad aplicadas según estilo de casa — nota: esto es un entregable externo; no incluir el encabezado de `CONFIDENCIAL — SECRETO PROFESIONAL` en la versión enviada a la contraparte
- [ ] Postura de conciliación [reflejada / ausente] según lo especificado en el intake, y la sustancia alineada con la postura
- [ ] Copias internas aprobadas (según lista de distribución del intake)
- [ ] Notificación a aseguradora enviada (si requerida según práctica de la casa)
- [ ] Conflictos confirmados (si aún no se verificaron)

**Antes de enviar la carta (el acto con consecuencias):** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`. Si el Rol es No abogado:

> Enviar esta carta de requerimiento tiene consecuencias legales — crea un registro, puede constituir una interpelación formal (mora), detonar intereses moratorios e interrumpir la prescripción. ¿Has revisado esto con un abogado? Si sí, procede. Si no, aquí hay un resumen para llevarle:
>
> [Generar resumen de 1 página: contraparte y disputa, el requerimiento y plazo, postura de tono, postura de conciliación, riesgos de confidencialidad y admisión señalados en la compuerta pre-redacción, qué podría salir mal, qué preguntar al abogado antes de enviar.]
>
> Si necesitas encontrar un abogado con cédula profesional vigente en tu jurisdicción: la Barra Mexicana de Abogados o el Colegio de Abogados de tu estado son el punto de partida más rápido para una referencia.

No marcar como enviado — no ejecutar las mecánicas de envío de abajo — sin un sí explícito.

## Mecánicas de envío

- [ ] Método de entrega ejecutado: [correo certificado con acuse / notificación personal / acta circunstanciada ante notario / correo electrónico]
- [ ] Prueba de entrega retenida (acuse de recibo, constancia de notificación, acta notarial, acuse de correo electrónico)
- [ ] Copias enviadas según lista de distribución

## Después del envío

- [ ] Plazo de cumplimiento calendarizado: [YYYY-MM-DD]
- [ ] Plan de escalamiento si no hay respuesta: [siguiente paso + fecha]
- [ ] Revisión de seguimiento calendarizada: [fecha — típicamente plazo + 2 días hábiles]
- [ ] Asunto creado en `_log.yaml`: [sí / no — ver materialidad abajo]

## Decisión de materialidad

**La heurística dice:** [material / inmaterial]
**Razón:** [tipo de requerimiento / exposición / tipo de contraparte]
**Tu decisión:** [material → crear asunto] [inmaterial → solo registro en demand-letters]

Si material: `/litigacion-legal-mexico:matter-intake` con `source: demand-letter` pre-poblado desde este intake.
```

### Oferta de auto-creación de asunto

Después de redactar y escribir el checklist, evaluar materialidad según heurística:

- **Default sí si CUALQUIERA de:**
  - Tipo de requerimiento es `cesación`, `incumplimiento-saneamiento`, `rescisión-laboral` o `preservación`
  - Valor del resultado deseado ≥ banda de severidad media de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`
  - La contraparte es cliente, competidor o adversario frecuente según panorama
- **Default no en caso contrario**

Presentar la decisión:
> Heurística de materialidad: [resultado]. [Una oración de razón.]
> ¿Crear un asunto rastreado en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`? (default: [sí/no])

Si el usuario acepta: activar `matter-intake` con campos pre-poblados del intake (contraparte, tipo, jurisdicción, `source: demand-letter`, teoría inicial, interesados internos). El usuario revisa campos pre-llenados y confirma.

Si el usuario rechaza: actualizar intake `status: drafted` (después `sent` cuando el usuario confirme). El registro permanece solo en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/`.

## Versionado

Nunca sobreescribir una redacción que ha sido enviada. Si se revisa después del envío, `draft-v2.docx`. El historial de versiones enviadas es en sí mismo el registro de lo que la contraparte recibió.

## Lo que este skill NO hace

- **Enviar la carta.** Solo redacción. El usuario envía.
- **Investigar citas.** Los marcadores `[CITA:___]` permanecen como marcadores. Si el usuario proporcionó autoridades en el intake, se usan; de lo contrario, espacios en blanco. Inventar citas es exposición a responsabilidad profesional.
- **Omitir la compuerta pre-redacción.** Incluso con `--skip-gate`, el skill anota en el archivo de redacción que la compuerta fue omitida y por qué.
- **Reescribir el intake.** Si el intake está delgado, enviar al usuario de regreso a `demand-intake`. La redacción es tan buena como lo que lee del intake.
- **Decidir materialidad.** La heurística ofrece un default; la decisión del usuario es el registro.
