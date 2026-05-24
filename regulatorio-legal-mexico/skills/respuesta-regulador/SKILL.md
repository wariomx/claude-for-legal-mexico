---
description: >
  Prepara la respuesta a requerimientos, solicitudes de información, visitas
  de verificación o sanciones propuestas de cualquier regulador federal
  mexicano. Identifica el plazo de respuesta, los hechos relevantes, los
  argumentos de defensa y la documentación requerida.
argument-hint: "[adjuntar o pegar el documento del regulador]"
---

# Skill: respuesta-regulador (regulatorio-legal-mexico)

## Propósito

Un requerimiento sin respuesta dentro del plazo equivale a aceptar los hechos imputados. Los plazos de reguladores federales mexicanos son generalmente no prorrogables — este skill identifica el plazo primero, clasifica la acción y construye la defensa estructurada.

## Flujo

### PRIMERO: extraer y mostrar el plazo

**Antes de cualquier análisis,** leer el documento y mostrar:

```
⏰ PLAZO DE RESPUESTA
[review: plazo regulador vence AAAA-MM-DD]
Fundamento del plazo: [artículo o disposición que lo establece]
Días hábiles/naturales restantes desde hoy: [N]
```

Si el plazo no es legible en el documento: "No puedo identificar el plazo en el documento proporcionado. Localizar la fecha límite de respuesta antes de continuar — los plazos de reguladores son generalmente no prorrogables."

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer:
- Reguladores en alcance y módulos activos
- Historial de procedimientos anteriores con este regulador
- Cadena de escalamiento configurada

### Paso 1: clasificar la acción

Determinar el tipo de acto regulatorio:

- **Requerimiento de información:** solicitud de documentos o datos — responder dentro del plazo con la información pedida más un oficio de presentación
- **Visita de verificación en curso:** identificar: ¿se designó representante? ¿se documentaron irregularidades durante la visita? ¿se firmó el acta con reservas o salvedades?
- **Acta de irregularidades:** derecho a presentar aportación de pruebas — plazo típico de 15 días hábiles, pero verificar por regulador y ley aplicable `[model knowledge — verify]`
- **Pliego de cargos / propuesta de sanción:** defensa sustantiva del fondo — el plazo y procedimiento dependen de la ley orgánica de cada regulador

### Paso 2: identificar el fundamento legal del procedimiento

Leer el número de oficio, el fundamento legal invocado y la dependencia emisora. Un error en el fundamento legal (responder al procedimiento equivocado, citar la ley derogada) puede implicar renuncia de defensas procesales o convalidar un acto que podría impugnarse.

Verificar:
- ¿El oficio identifica el artículo que faculta a la autoridad para solicitar esta información?
- ¿La autoridad emisora es competente para el tipo de acto y el sector del cliente?
- ¿El procedimiento cumplió con las formalidades de notificación? `[review]`

### Paso 3: construir la estrategia de defensa

**1. Hechos**
Reconstruir cronología desde documentos del cliente. ¿Qué pasó realmente?

**2. Cumplimiento legal**
¿Qué disposiciones aplican? ¿Qué evidencia documenta el cumplimiento?

**3. Defensas procedimentales**
- ¿La visita o requerimiento fue debidamente iniciado conforme a la ley orgánica del regulador?
- ¿Se respetaron los requisitos de notificación y plazos del procedimiento?
- ¿Tiene la autoridad competencia material y territorial sobre el acto?

**4. Defensas sustantivas**
- ¿Los hechos imputados constituyen en realidad una infracción?
- ¿Existe causa de exclusión de responsabilidad (fuerza mayor, caso fortuito, instrucción de autoridad)?
- ¿Hay jurisprudencia o criterios administrativos favorables? `[model knowledge — verify]`

**5. Proporcionalidad** (si la violación ocurrió)
Documentar buena fe, primera infracción, corrección inmediata y cooperación con la autoridad. Los criterios de sanción de la mayoría de leyes regulatorias pesan estos factores.

### Paso 4: notas por regulador

- **COFECE:** procedimiento bajo LFCE Arts. 69-75; derecho a ofrecer pruebas dentro de 30 días hábiles desde notificación del pliego de presuntas responsabilidades `[model knowledge — verify LFCE Arts. vigentes]`
- **CNBV:** procedimientos bajo LIC/LMV con plazos acotados — los oficios de la CNBV especifican el plazo exacto; verificar `[model knowledge — verify por sub-sector regulado]`
- **COFEPRIS:** procedimiento sancionatorio bajo Ley General de Salud Arts. 414 y siguientes `[model knowledge — verify]`
- **IFT:** procedimiento bajo LFTR (Ley Federal de Telecomunicaciones y Radiodifusión) `[model knowledge — verify]`
- **CRE:** procedimiento bajo Ley de los Órganos Reguladores Coordinados en Materia Energética `[model knowledge — verify]`

### Paso 5: producir borrador de respuesta y checklist

Redactar el oficio de respuesta con las siguientes secciones: (I) Fundamento de la comparecencia — representante legal, instrumento notarial, poderes; (II) Hechos — cronología documentada; (III) Respuesta numerada por punto del requerimiento; (IV) Documentación adjunta — lista numerada; (V) Defensas procedimentales, si aplica — argumentación con citas; (VI) Conclusión y protesta de ley.

**Checklist de documentación:**
- [ ] Identificación y poder del representante legal
- [ ] Acta constitutiva o resolución corporativa relevante
- [ ] Evidencia de cumplimiento de las disposiciones aplicables
- [ ] Comunicaciones previas con el regulador sobre el mismo asunto
- [ ] Documentación técnica de soporte según el tipo de requerimiento

### Paso 6: árbol de decisión

> **¿Qué sigue?**
> 1. **Completar y revisar el borrador** — agrego los hechos específicos y la evidencia que me proporciones.
> 2. **Impugnar el acto** — si hay vicios procedimentales, evalúo si conviene responder y simultáneamente impugnar, o impugnar primero.
> 3. **Escalar** — preparo nota de escalamiento para [cadena configurada en el perfil] con los hechos, el plazo y la exposición estimada.
> 4. **Negociar corrección voluntaria** — si la infracción ocurrió, estructuro una presentación de corrección voluntaria y buena fe para minimizar la sanción.
> 5. **Algo diferente** — dime qué necesitas.

---

**Nota del revisor:** Verificar siempre el fundamento legal del procedimiento (número de oficio, artículo habilitante, dependencia emisora) antes de responder. Una respuesta al procedimiento equivocado, o que no impugna los vicios procedimentales disponibles, puede convalidar el acto y cerrar defensas que estarían abiertas de otro modo.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
