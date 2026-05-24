---
description: >
  Triaja un asunto o situación de competencia económica contra el marco de la
  Ley Federal de Competencia Económica (LFCE) y la práctica de la COFECE.
  Clasifica el riesgo de prácticas monopólicas absolutas o relativas, evalúa
  si una concentración supera los umbrales de notificación obligatoria, y
  determina si la situación requiere un programa de cumplimiento, asesoría
  especializada o notificación proactiva. Produce un memorándum de triaje con
  hallazgos, nivel de riesgo y árbol de decisión.
argument-hint: "[descripción del asunto o pega el texto del contrato / operación]"
---

# Skill: cofece-triage (regulatorio-legal-mexico)

## Propósito

La COFECE investiga de oficio y puede imponer multas de hasta el 8% de los ingresos del agente económico infractor por prácticas monopólicas (Art. 127 LFCE). La notificación tardía o no notificación de una concentración sujeta a aviso previo puede resultar en multas de hasta 1.5 millones de UMAs (Art. 131 LFCE). Este skill identifica si una situación genera exposición bajo la LFCE antes de que el problema sea urgente.

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer:
- Sectores de exposición del módulo COFECE
- Umbral de notificación de concentraciones configurado
- Política de cumplimiento de competencia

Si el módulo COFECE no está activo: "El módulo COFECE no está configurado. Puedo ejecutar el triaje con parámetros genéricos, pero para resultados calibrados ejecuta `/regulatorio-legal-mexico:cold-start-interview --module cofece`."

### Paso 1: obtener información del asunto

Si el usuario proporcionó texto (contrato, descripción de operación, acuerdo comercial): leerlo.

Si no hay texto: hacer preguntas de triaje:

1. "¿Qué tipo de situación quieres analizar? (concentración/M&A / acuerdo comercial / práctica de distribución / licitación / otro)"
2. "¿Quiénes son las partes? (describir brevemente — sector, tamaño aproximado, relación entre ellas: competidores / proveedor-cliente / sin relación)"
3. "¿Cuál es el objeto del acuerdo o la operación? (en una o dos oraciones)"
4. "¿Tienen las partes actividad en México?"

### Paso 2: verificar umbrales de notificación de concentraciones

Si el asunto es una concentración (M&A, fusión, adquisición, asociación en participación con control compartido):

Verificar los umbrales del Art. 86 LFCE `[model knowledge — verify contra RMF COFECE vigente]`:
- **Umbral de valor de la operación:** cuando el acto o serie de actos supera cierto monto en UMAs `[verify monto actual]`
- **Umbral de activos / ventas:** cuando la empresa adquirida tiene activos o ventas en México por encima del umbral `[verify monto actual]`
- **Umbral conjunto:** cuando la suma de activos o ventas en México de todas las partes involucradas supera el umbral `[verify monto actual]`

Los umbrales se actualizan anualmente por la COFECE. **Ejecutar búsqueda web para verificar los umbrales vigentes antes de concluir.**

Si aplican los umbrales: "Esta operación podría requerir notificación previa a COFECE. El análisis exacto requiere los datos financieros de las partes. `[review]`"

### Paso 3: analizar riesgo de prácticas monopólicas

**Prácticas monopólicas absolutas (Art. 53 LFCE):**
¿El acuerdo o conducta involucra:
- Fijación de precios entre competidores
- División de mercados entre competidores
- Boicots colectivos
- Manipulación de licitaciones (colusión en licitaciones)

Estos son per se ilegales — no se evalúa su eficiencia económica. Si cualquiera aplica: clasificar 🔴 Crítico.

**Prácticas monopólicas relativas (Art. 56 LFCE):**
¿La empresa tiene poder sustancial de mercado? ¿El acuerdo o conducta involucra:
- Precios predatorios
- Ataduras (tying)
- Exclusividades
- Discriminación de precios
- Negativa de trato

Si hay indicios de poder sustancial + conducta potencialmente anticompetitiva: clasificar 🟠 Alto.

**Concentraciones con efectos anticompetitivos (Arts. 86-96 LFCE):**
¿La operación podría generar poder de mercado, reducir competencia sustancialmente, o crear una posición dominante en un mercado relevante?

### Paso 4: verificar estado de la práctica de cumplimiento

Si el perfil de práctica incluye información sobre el programa de cumplimiento de competencia:
- ¿Existe programa formal?
- ¿Cuándo fue la última revisión?
- ¿Se capacita al personal en riesgo de contacto con competidores?

### Paso 5: producir memorándum de triaje

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [model knowledge — verify | web search para umbrales COFECE vigentes]
- Leído: [descripción de lo analizado]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar umbrales vigentes contra el Acuerdo de la COFECE que los establece; la clasificación de poder de mercado requiere datos financieros que este triaje no tiene.

---

**Triaje COFECE — [asunto / fecha]**

**Clasificación de riesgo:** [🔴 Crítico / 🟠 Alto / 🟡 Medio / 🟢 Bajo]

**Tipo de exposición identificada:**
- [ ] Notificación de concentración obligatoria
- [ ] Práctica monopólica absoluta (per se ilegal)
- [ ] Práctica monopólica relativa (sujeta a análisis de poder de mercado)
- [ ] Sin exposición identificada con la información disponible

**Análisis:**
[Descripción de los hechos analizados, las disposiciones aplicables y el razonamiento]

**Fundamento legal:**
[Citas de artículos LFCE aplicables] `[model knowledge — verify]`

**Información faltante para un análisis definitivo:**
[Qué datos no se tienen y cómo afectan la conclusión]

**Una pregunta que haría y que no está en mi checklist:** [observación de segundo orden]
```

### Paso 6: árbol de decisión

> **¿Qué sigue?**
> 1. **Notificar la concentración** — te ayudo a preparar la información necesaria para la notificación ante COFECE (Art. 89 LFCE establece el contenido mínimo).
> 2. **Redactar respuesta a requerimiento COFECE** — si ya hay un procedimiento abierto, `/regulatorio-legal-mexico:respuesta-regulador` lo maneja.
> 3. **Revisar el programa de cumplimiento** — si el triaje identificó brechas en la política interna de competencia, puedo hacer una revisión estructurada.
> 4. **Escalar a especialista** — redacto una nota de escalamiento para el Director Jurídico o despacho externo con los hechos clave y la clasificación de riesgo.
> 5. **Documentar y esperar** — el análisis queda archivado; revisitar si la operación avanza o si COFECE inicia investigación.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
