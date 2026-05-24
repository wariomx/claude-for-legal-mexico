---
name: demand-intake
description: Recopilación de contexto previo a la redacción de una carta de requerimiento — partes, hechos, fundamento, apalancamiento, BATNA y filtros de confidencialidad — escrita en un intake.md estructurado que lee el skill demand-draft. Usar cuando el usuario quiera preparar un requerimiento, ejecutar el intake antes de redactar, o capturar contexto para un requerimiento de pago, incumplimiento/saneamiento, cesación de PI, rescisión laboral o preservación documental.
argument-hint: "[título] [--full]"
---

# /demand-intake

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → práctica de cartas de requerimiento, panorama, calibración de riesgo.
2. Seguir el flujo de trabajo y la referencia de abajo.
3. Ejecutar el intake adaptivo (8 preguntas base siempre; bloque estratégico si es material o `--full`).
4. Generar slug a partir de título + contraparte + año-mes.
5. Escribir `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/intake.md`.
6. Confirmar con el usuario: "Intake guardado. Ejecuta `/litigacion-legal-mexico:demand-draft [slug]` cuando estés listo."

---

# Intake de Requerimiento

## Propósito

La redacción viene después. El valor está en el trabajo previo — forzar las preguntas que una carta descuidada omite. Apalancamiento, BATNA, tolerancia al riesgo, filtros de confidencialidad, la audiencia real. Un requerimiento enviado sin pensar en esos aspectos es peor que no enviar nada.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → Práctica de cartas de requerimiento (tiempos de notificación a aseguradora, umbral de materialidad para creación de asunto, plantillas de documentos semilla), panorama (tipo de contraparte, patrones de adversarios recurrentes), calibración de riesgo (para pre-estimar materialidad), estilo de casa. **Tono, plazo de cumplimiento, formalidad de la comunicación y firmante NO son parámetros de práctica — se fijan por asunto en el paso `## Postura para este asunto` abajo.**

## Banderas

- `--full` → ejecutar el intake completo sin importar la heurística de materialidad (para abogados que prefieren exhaustividad siempre)

## El intake

### Postura para este asunto (preguntar PRIMERO, antes del bloque base)

> **Postura para este asunto.** El tono y los términos de una carta de requerimiento son caso por caso, no un default de práctica. Preguntar:
> - **Tono:** mesurado / asertivo / agresivo? (depende de la relación, el monto y la probabilidad de juicio)
> - **Plazo de respuesta:** ¿qué es razonable dado el reclamo? (15 días es común para requerimientos de pago; 30 días para saneamiento; 5-10 días para cesación — pero el contrato o la ley pueden fijar otro)
> - **Formalidad de la comunicación:** ¿requiere acta circunstanciada ante fedatario público? ¿Correo certificado con acuse de recibo? ¿Notificación personal? (determina el valor probatorio del requerimiento)
> - **Firmante:** tú, el cliente, el Director Jurídico, despacho externo?
> No asumir. Leer la correspondencia previa de requerimientos en el expediente si la hay — establece el registro de tono.

Registrar las respuestas en el intake bajo una sección `## Postura` antes de `## Partes`. Estas respuestas gobiernan el resto del intake y la redacción posterior — no recurrir a un default de práctica si el usuario dejó alguna en blanco; preguntar de nuevo.

### Bloque base — siempre se pregunta (8 preguntas)

**1. Tipo de requerimiento**
`pago | incumplimiento-saneamiento | cesación | rescisión-laboral | preservación | otro`

**2. Partes**
- **Remitente:** nuestra empresa (y entidad específica si es multi-entidad)
- **Destinatario:** contraparte — nombre, entidad, domicilio
- **Audiencia del destinatario:** quién realmente lee (Director Jurídico? Director General? persona física? abogado interno?)
- **Relación:** `cliente | proveedor | ex-empleado | competidor | tercero | otro`

**3. Hecho detonante**
- Qué ocurrió y cuándo (las fechas importan — prescripción, plazos de notificación)
- Evidencia disponible (contratos, correos, registros, testigos)

*Oportunidad de documento semilla: "Si puedes compartir el contrato subyacente, la correspondencia o la evidencia, la redacción será materialmente más precisa. Las rutas de archivo funcionan."*

**4. Fundamento legal / contractual**
- Qué disposiciones — secciones específicas del contrato si aplica
- Ley aplicable (jurisdicción, cláusula de elección de ley)
- Leyes o artículos invocados (marcadores de posición OK — la redacción marcará `[CITA:___]` de todos modos)

**5. Resultado deseado**
- Solicitudes específicas. No "resolución" — pago de $X cantidad para fecha Y; cesación de actividad específica Z; saneamiento en N días; devolución de propiedad específica.
- Si hay múltiples solicitudes, ordenarlas (principal vs. subsidiaria)

**6. Plazos**
- Plazo externo que impulsa esto (prescripción, ventana de daño continuo, evento de negocio)
- Plazo de cumplimiento del requerimiento — cuánto tiempo le damos al destinatario. Usar el plazo de respuesta capturado en `## Postura para este asunto` arriba; no recurrir a un default de práctica.
- **Plazos de prescripción clave** (verificar contra el tipo de acción):
  - Mercantil general: 10 años (Art. 1047 Código de Comercio) `[model knowledge — verify]`
  - Civil: varía por código estatal (generalmente 5-10 años para acciones personales)
  - Laboral — la mayoría de acciones: 1 año (Art. 516 LFT) `[model knowledge — verify]`
  - Laboral — separación del trabajo (despido justificado o injustificado): 2 meses (Art. 518 LFT). Plazo se suspende durante conciliación previa (Art. 684-B LFT). `[verified 2026-05-23]`

**7. Contacto previo**
- ¿Se ha planteado esto informalmente? ¿Cuándo, por quién, en qué forma?
- ¿Alguna respuesta hasta ahora?
- ¿Por qué se escala ahora a un requerimiento formal?

**8. Distribución**
- Método de entrega (preguntar; no hay default de práctica):
  - Correo certificado con acuse de recibo
  - Notificación personal
  - Acta circunstanciada ante notario público
  - Correo electrónico (con consideraciones de cadena de custodia para valor probatorio)
- Firmante — capturado en `## Postura para este asunto` arriba
- Copias — interesados internos, aseguradora (si se notifica pre-requerimiento según regla de práctica), abogados

### Bloque estratégico — se pregunta si es material, o si `--full`

Heurística de materialidad: preguntar el bloque estratégico si cualquiera de las siguientes es verdadera.

- Tipo de requerimiento es `cesación`, `incumplimiento-saneamiento`, `rescisión-laboral` o `preservación`
- Valor del resultado deseado ≥ banda de severidad media de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` calibración de riesgo
- La contraparte es cliente, competidor o adversario frecuente según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` panorama
- El usuario ejecutó con `--full`

**Opción explícita de omitir.** Cuando se activa el bloque estratégico, el usuario puede declinar contestarlo. Preguntar claramente:

> Este es un requerimiento material según la heurística. El bloque estratégico (apalancamiento, BATNA, tono, filtros de confidencialidad) es donde está la mayor parte del valor pre-redacción. Omitirlo produce una redacción más débil.
> - **Contestar ahora** — recorrer el bloque estratégico (5-7 min)
> - **Contestar parcial** — recorrer el subconjunto que estés preparado para responder
> - **Omitir** — proceder a redacción solo con el bloque base; marcaré `strategic_block: skipped` en el intake

Si el usuario elige Omitir, el archivo intake lo registra:

```yaml
strategic_block: skipped        # answered | partial | skipped
skipped_reason: string | null   # capturado si el usuario dio razón
```

El skill de redacción respeta la omisión — la compuerta pre-redacción se ejecuta de todos modos, pero las secciones que dependen de respuestas del bloque estratégico llevan marcadores `[VERIFICAR SME: apalancamiento/tono/confidencialidad no capturados en intake]`. El comando `/demand-draft` también vuelve a preguntar, ofreciendo completar el bloque estratégico antes de redactar.

**9. Apalancamiento y BATNA**
- Qué nos da poder de negociación (derechos contractuales, apalancamiento fáctico, reputacional, comercial)
- Qué pasa si rehúsan — ¿estamos preparados para litigar? ¿Hacer público? ¿Aceptar un resultado menor?
- Su BATNA probable — ¿cuál es su mejor alternativa? (Si no creen que vamos a demandar, el requerimiento es débil.)

**10. Tolerancia al riesgo**
- Exposición reputacional si esto se hace público
- Riesgo de precedente — ¿esta carta establece un patrón que afecta otros asuntos?
- Implicaciones regulatorias / de divulgación (¿es el tipo de disputa que se convierte en un hecho relevante para la CNBV o la BMV?)
- Implicaciones de seguro — ¿enviar sin notificar a la aseguradora afecta la cobertura?

**11. Postura de tono**
- Ya capturada en `## Postura para este asunto` arriba. Aquí, explorar la tensión si el usuario eligió un tono más fuerte del que los hechos parecen justificar, o más débil.
- Vale la pena nombrar explícitamente: un tono agresivo quema la relación. Si quieres mantener la relación comercial pero proteger la posición legal, `mesurado` suele ser la opción correcta.

**12. Postura de conciliación**
- Identificar los mecanismos de resolución alternativa aplicables al foro:
  - **Laboral (LFT):** la conciliación prejudicial ante el Centro Federal de Conciliación y Registro Laboral es obligatoria antes de la demanda (Art. 684-A LFT y ss.) `[model knowledge — verify]`
  - **Comercial:** la mediación es opcional; el arbitraje está regulado por el Código de Comercio Título IV `[model knowledge — verify]`
  - **Civil:** la conciliación puede ser voluntaria u ordenada por el juez según el código procesal local
- **Nota importante:** las tratativas previas (discusiones de arreglo) NO tienen protección exclusionaria automática en el procedimiento probatorio mexicano — lo que se diga puede potencialmente ofrecerse como prueba. No existe un equivalente a las protecciones de comunicación para arreglo del common law.
- ¿Este requerimiento busca abrir la puerta a un convenio judicial o extrajudicial? ¿O es una aserción pura de derechos?
- Si hay intención conciliatoria: la redacción reflejará la apertura al diálogo pero cuidando que cualquier declaración pueda ser utilizada como prueba en caso de juicio.

**13. Filtros de confidencialidad**
- ¿Qué hay en nuestro análisis interno que NO debe aparecer en la carta? (Hechos no verificados, dudas sobre nuestro caso, razonamiento estratégico, discusiones previas de arreglo)
- Una sola oración mal redactada puede comprometer la confidencialidad del análisis relacionado (secreto profesional, Art. 36 Ley Reglamentaria del Art. 5° Constitucional). Ser explícito sobre qué se excluye.

**14. Riesgo de reconocimiento de adeudo y transacción**
- ¿Algo en la carta que la contraparte pudiera después caracterizar como un reconocimiento de adeudo (Art. 1168 CCF) o de hechos que afecten nuestra posición? `[model knowledge — verify]`
- ¿Este requerimiento corre el riesgo de constituir inadvertidamente una transacción (Arts. 2944-2963 CCF)? La transacción es un contrato por el cual las partes se hacen recíprocas concesiones para terminar una controversia — puede generarse implícitamente si el lenguaje no es cuidadoso. `[model knowledge — verify]`

## Escritura del intake

### Slug

`[tipo]-[contraparte-corto]-[yyyy-mm]`. Confirmar unicidad en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/`.

### `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/demand-letters/[slug]/intake.md`

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

# Intake de Requerimiento: [título]

**Slug:** [slug]
**Tipo de requerimiento:** [tipo]
**Elaborado por:** [abogado]
**Abierto:** [YYYY-MM-DD]
**Estatus:** intake | listo-para-redacción | redactado | enviado | cerrado
**Bloque estratégico:** answered | partial | skipped
**Razón de omisión:** [si aplica]

---

## Postura

- **Tono:** [mesurado / asertivo / agresivo — con justificación de una línea ligada a la relación y el monto]
- **Plazo de respuesta:** [N días — ligado al reclamo / contrato / protocolo]
- **Formalidad:** [correo certificado / notificación personal / acta circunstanciada ante notario / correo electrónico — con justificación]
- **Firmante:** [nombre / cargo — tú / cliente / Director Jurídico / despacho externo]

*Esta es la postura por asunto capturada en el intake. El skill de redacción lee de aquí.*

---

## Partes

- **Remitente:** [nuestra entidad]
- **Destinatario:** [contraparte, entidad, domicilio]
- **Audiencia del destinatario:** [quién lee]
- **Relación:** [tipo]

## Hecho detonante

[Qué ocurrió, cuándo, evidencia]

## Fundamento legal / contractual

[Disposiciones, ley aplicable, artículos]

## Resultado deseado

[Solicitudes específicas en orden de prioridad]

## Plazos

- **Externo:** [prescripción, ventana de daño continuo]
- **Cumplimiento:** [cuánto tiempo les damos]

## Contacto previo

[Historial, más reciente primero]

## Distribución

- **Entrega:** [método]
- **Firmante:** [nombre/cargo]
- **Copias:** [lista]

---

## Estratégico (si aplica)

### Apalancamiento y BATNA

[Nuestro poder, su probable respuesta]

### Tolerancia al riesgo

[Reputacional, precedente, regulatorio, seguro]

### Postura de tono

[preservar-relación / mesurado / confrontativo — con justificación]

### Postura de conciliación

[Conciliación obligatoria o voluntaria según tipo de acción. Tratativas previas sin protección exclusionaria en derecho mexicano — todo lo dicho es potencialmente utilizable como prueba. Convenio judicial/extrajudicial como mecanismo de arreglo.]

### Filtros de confidencialidad

[Qué NO puede aparecer en la redacción]

### Riesgo de reconocimiento de adeudo / transacción

[Riesgos específicos señalados]

---

## Documentos semilla

| Doc | Ruta |
|---|---|
| [contrato subyacente] | [ruta o "no compartido"] |
| [correspondencia previa] | [ruta o "no compartido"] |
| [evidencia] | [ruta o "no compartido"] |

---

## Evaluación de materialidad

**La heurística dice:** [material / inmaterial — con razonamiento]
**Decisión del usuario:** [material / inmaterial / por determinar post-envío]
```

## Confirmar antes de escribir

Mostrar al usuario el borrador de intake. Señalar lo que esté delgado:

> Aquí está el intake. Noto [puntos débiles]. Antes de guardar, ¿algo que agregar?

## Entrega a redacción

Terminar con:
> Intake guardado. Cuando estés listo: `/litigacion-legal-mexico:demand-draft [slug]`

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill produjo — las cinco ramas default (redactar el X, escalar, obtener más hechos, observar y esperar, algo más) son un punto de partida, no un candado. El árbol es el resultado; el abogado elige.

## Lo que este skill NO hace

- Redactar la carta. Eso es `demand-draft` — los dos pasos están intencionalmente separados para que el abogado pueda pausar para input de negocio, consulta con despacho externo o notificación a aseguradora antes de redactar.
- Decidir si enviar la carta. Algunas sesiones de intake terminan con "de hecho, no envíes — negociemos directamente." Ese es un resultado válido; el registro de intake conserva su valor.
- Ejecutar la verificación de conflictos. Si la contraparte es cliente o entidad conocida, señalar que debe pasar conflictos (según `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`) antes de enviar — pero la verificación misma vive en el flujo de matter-intake o fuera de este skill.
