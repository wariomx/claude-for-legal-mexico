---
description: >
  Analiza en profundidad si un riesgo o siniestro específico está cubierto
  bajo una póliza determinada. Mapea los hechos contra la cobertura, las
  exclusiones y las condiciones, evalúa la posición de la aseguradora,
  e identifica los argumentos de cobertura y defensa disponibles.
argument-hint: "[descripción del riesgo o siniestro y ramo de seguro]"
---

# Skill: cobertura-analysis (seguros-legal-mexico)

## Propósito

La aseguradora negó (o podría negar) la cobertura. O el usuario quiere saber antes del siniestro si un riesgo específico está cubierto. Este skill hace el análisis estructura por estructura: primero determina si los hechos activan la cobertura, luego evalúa cada exclusión invocada o invocable, y finalmente mapea los argumentos disponibles para el asegurado.

## Marco legal

| Norma | Relevancia |
|---|---|
| LCS Arts. 1-15 | Formación y validez del contrato de seguro |
| LCS Art. 25 | La póliza es prueba del contrato; discrepancia póliza/solicitud: prevalece la solicitud `[review: contexto específico]` |
| LCS Arts. 31-35 | Nulidad por inexacta o falsa declaración del asegurado — análisis de relevancia del hecho no declarado |
| LCS Art. 52 | Obligación del asegurado: no agravar el riesgo sin consentimiento |
| LCS Art. 66 | Aviso de siniestro; si se incumplió, evaluar perjuicio real a la aseguradora |
| LCS Arts. 67-72 | Procedimiento de liquidación |
| LCS Arts. 100-115 | Seguro de daños: interés asegurable, subrogación, infraseguro |
| LCS Arts. 151-192 | Seguro de personas: exclusión de preexistencias, suicidio, estado de embriaguez |
| Código de Comercio Art. 162 | Interpretación contra el redactor (aseguradora) en caso de ambigüedad |
| SCJN jurisprudencia | Las exclusiones se interpretan restrictivamente; la cobertura se interpreta extensivamente `[model knowledge — verify con Semanario Judicial]` |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer módulo relevante (asegurado corporativo / individual / operador) para calibrar el análisis.

### Paso 1: captura de hechos e insumos

Si el usuario no los proporcionó, solicitar:

1. "¿Cuáles son los hechos del siniestro o del riesgo que quieres evaluar? (descripción completa)"
2. "¿Tienes la póliza (condiciones generales + condiciones particulares + endosos)? Proporciona el documento o los textos relevantes."
3. "¿La aseguradora ya emitió un dictamen o carta de rechazo? Si sí, ¿qué argumentos usó?"
4. "¿Cuál es el objetivo del análisis? (evaluar cobertura antes de presentar reclamación / responder un rechazo / determinar estrategia procesal)"

### Paso 2: análisis de activación de cobertura

Verificar si los hechos activan el objeto asegurado:

- [ ] ¿El tipo de evento/daño está dentro del objeto del seguro según la cobertura grant?
- [ ] ¿El evento ocurrió durante la vigencia de la póliza?
- [ ] ¿El bien o la persona asegurada es el afectado?
- [ ] ¿El asegurado tenía interés asegurable al momento del siniestro? (Art. 85 LCS para daños)
- [ ] ¿La prima estaba al corriente? Si no, ¿qué dice la póliza sobre el efecto de falta de pago?

Clasificar: ✓ Cobertura activada / ⚠️ Activación dudosa [impacto: detallar] / ✗ Cobertura no activada

### Paso 3: análisis de exclusiones

Para cada exclusión relevante (las invocadas por la aseguradora y las que podrían invocarse):

**3A. Lectura literal**
- Citar el texto exacto de la exclusión
- ¿Los hechos caen literalmente dentro de la exclusión?

**3B. Interpretación restrictiva**
Las exclusiones se interpretan restrictivamente conforme al principio de contra proferentem (Art. 162 Código de Comercio) y la jurisprudencia de la SCJN. `[model knowledge — verify]`
- ¿Existe alguna lectura razonable de los hechos que quede fuera de la exclusión?
- ¿Es la exclusión ambigua? Si lo es, la ambigüedad favorece al asegurado.

**3C. Validez de la exclusión**
- ¿La exclusión anula prácticamente la cobertura principal? Si sí, puede ser abusiva `[review]`
- ¿La exclusión contraviene las condiciones generales aprobadas por la CNSF para este ramo? `[verify — CNSF portal]`
- ¿La exclusión fue comunicada claramente al asegurado antes de contratar?

**3D. Clasificación de cada exclusión**
| Exclusión | Literalmente aplica | Interpretación restrictiva | Validez | Probabilidad de éxito para asegurado |
|---|---|---|---|---|
| [texto] | Sí/No/Dudoso | [análisis] | Válida/Dudosa | [%] `[review]` |

### Paso 4: analizar argumentos de incumplimiento del asegurado

Si la aseguradora invoca incumplimiento de obligaciones:

**Aviso tardío (Art. 66 LCS)**
- ¿El aviso fue realmente tardío? Calcular desde la fecha de conocimiento, no del hecho.
- Si fue tardío: ¿la aseguradora demostró que el retraso le causó perjuicio real? La LCS no permite reducir la indemnización sin perjuicio demostrable `[model knowledge — verify jurisprudencia SCJN]`.
- Argumento: el perjuicio debe ser probado por la aseguradora, no simplemente presumido.

**Agravación del riesgo (Art. 52 LCS)**
- ¿Hubo agravación del riesgo previa al siniestro?
- ¿La agravación fue comunicada a la aseguradora?
- ¿La agravación fue la causa del siniestro?

**Inexacta declaración (Arts. 31-35 LCS)**
- ¿El hecho no declarado era conocido por el asegurado al contratar?
- ¿El hecho era relevante para la evaluación del riesgo?
- ¿La inexactitud fue dolosa o culposa? La consecuencia es distinta.
- `[review: análisis de dolo vs. culpa requiere hechos específicos]`

### Paso 5: posición negociadora y estrategia

Basado en el análisis:

**Posición de la aseguradora:**
- ¿Cuál es el argumento más fuerte de la aseguradora para negar?
- ¿Cuál es la debilidad principal de su posición?

**Posición del asegurado:**
- Argumento principal de cobertura: [el más sólido]
- Argumentos de respaldo: [2-3 argumentos adicionales]
- Debilidades propias: [ser honesto — qué puede usar la aseguradora en contra]

**Recomendación de ruta:**
| Ruta | Viabilidad | Ventajas | Riesgos |
|---|---|---|---|
| Negociación directa con la aseguradora | [alta/media/baja] | Rapidez, confidencialidad | [riesgos] |
| Queja CONDUSEF (conciliación) | [alta/media/baja] | Gratuito, rápido, informal | Solo hasta cierto monto `[verify tope CONDUSEF]` |
| Arbitraje CONDUSEF | [alta/media/baja] | Ejecutable, confidencial | Más formal |
| Demanda civil / mercantil | [alta/media/baja] | Fuerza ejecutoria | Costo, tiempo |

### Paso 6: output final

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [póliza proporcionada ✓ | condiciones generales CNSF: model knowledge — verify]
- Leído: [descripción de insumos]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar el texto exacto de las condiciones generales aprobadas por CNSF para este ramo; y contrastar con jurisprudencia de SCJN sobre interpretación de exclusiones.

---

**Análisis de Cobertura — [ramo] — [asegurador] — [fecha]**

**Activación de cobertura:** [clasificación con razones]
**Exclusiones analizadas:** [N; tabla del Paso 3]
**Evaluación global:** [cubierto / dudoso / excluido]
**Probabilidad de cobro en cobertura:** [estimación] `[review]`

[Tabla de exclusiones del Paso 3D]

[Análisis de incumplimientos del Paso 4]

[Tabla de rutas del Paso 5]

**Una pregunta que haría y que no está en mi checklist:** [observación]
```

> **¿Qué sigue?**
> 1. **Redactar respuesta al rechazo** — elaboro una carta formal a la aseguradora refutando el rechazo con los argumentos del análisis.
> 2. **Preparar queja CONDUSEF** — `/seguros-legal-mexico:recurso-condusef` con este análisis como base.
> 3. **Revisar la póliza completa** — `/seguros-legal-mexico:poliza-review` para identificar otras cláusulas relevantes.
> 4. **Estrategia de litigio** — si el análisis apunta a demanda, identifico los hechos que hay que probar y los medios de prueba disponibles.
> 5. **Escalar** — redacto nota de escalamiento para el Director Jurídico con el análisis y la recomendación de ruta.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
