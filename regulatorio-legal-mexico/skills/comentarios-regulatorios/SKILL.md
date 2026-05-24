---
description: >
  Redacta comentarios públicos para consultas regulatorias — CONAMER
  (Manifestación de Impacto Regulatorio), proyectos de NOM en consulta,
  resoluciones de COFECE/CNBV/IFT en consulta pública. Estructura los
  comentarios con fundamento técnico-jurídico para maximizar su incorporación.
argument-hint: "[tipo de consulta: AIR/NOM/COFECE/CNBV/IFT] [descripción breve del proyecto]"
---

# Skill: comentarios-regulatorios (regulatorio-legal-mexico)

## Propósito

Las autoridades regulatorias reciben cientos de comentarios en cada consulta pública y descartan los vagos o meramente políticos. Este skill construye comentarios con fundamento técnico-jurídico estructurado — artículo por artículo, con alternativa redactada y justificación concreta — para maximizar las probabilidades de incorporación.

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo CONAMER:
- Sectores en alcance y postura de participación
- Cámara sectorial coordinadora (si aplica)
- Historial de comentarios regulatorios previos

Si el módulo CONAMER no está activo: continuar con parámetros genéricos y advertir.

### Paso 1: clasificar la consulta e identificar plazo

Identificar el tipo de consulta. Mostrar el plazo de cierre de forma prominente:

`[review: plazo regulador vence AAAA-MM-DD]`

- **CONAMER AIR (Análisis de Impacto Regulatorio):** período típico de 30 días naturales desde publicación en portal CONAMER `[model knowledge — verify plazo actual en portal CONAMER]`
- **Proyecto de NOM:** 60 días naturales desde publicación en DOF `[settled — last confirmed 2026-05-24]`
- **Consulta COFECE/IFT/CNBV:** plazo establecido en la propia publicación — revisar el documento

Si no se conoce la fecha de cierre: solicitarla al usuario antes de continuar. Un comentario presentado fuera de plazo no existe.

### Paso 2: obtener insumos del cliente

Si no se han proporcionado, preguntar:

1. El texto del proyecto regulatorio (pegar o adjuntar)
2. Los intereses específicos del cliente (industria, artículos afectados, impacto operativo)
3. El resultado deseado: rechazo total / modificación de artículos específicos / solicitud de aclaración
4. Evidencia técnica o económica disponible (estudios, datos de impacto, experiencia comparada)

### Paso 3: analizar el proyecto regulatorio

Para cada disposición que afecta al cliente:
- Identificar el problema que crea o la brecha que deja
- Evaluar si la justificación de la autoridad en el AIR es suficiente (para NOMs y regulación CONAMER)
- Detectar inconsistencias con leyes de jerarquía superior o con regulación ya vigente
- Identificar efectos desproporcionados en el mercado o en la competencia `[review]`

Ejecutar búsqueda web para verificar si hay precedentes de comentarios similares aceptados por la autoridad, o jurisprudencia relevante. `[model knowledge — verify]`

### Paso 4: redactar los comentarios

Estructura de un comentario efectivo:

**1. Identificación del comentarista e interés legítimo**
Nombre, representación, sector de actividad, y en qué calidad se presenta (afectado directo, representante sectorial, experto técnico).

**2. Resumen ejecutivo de la postura**
No más de tres oraciones. La autoridad lee el resumen primero; si no capta el argumento central aquí, el comentario pierde peso.

**3. Análisis por disposición**
Para cada artículo o sección impugnada, en este orden:
- *Problema:* qué crea la disposición tal como está redactada
- *Propuesta alternativa:* texto redactado de la disposición modificada (específico, numerado para seguimiento)
- *Justificación:* fundamento jurídico `[model knowledge — verify]`, evidencia técnica, análisis de impacto, y referencia a los criterios AIR si aplica

**4. Análisis de impacto económico y de competencia** (cuando aplica a NOMs y AIR CONAMER)
Cuantificar costos de cumplimiento, efectos sobre competencia, alternativas menos restrictivas. Los criterios del AIR de CONAMER (Art. 69 de la Ley General de Mejora Regulatoria) priorizan evidencia cuantitativa. `[model knowledge — verify art. aplicable]`

**5. Propuestas de redacción numeradas**
Listadas para facilitar el seguimiento por la autoridad.

**6. Conclusión**

### Paso 5: verificar requisitos de presentación

- **CONAMER:** portal web en https://www.conamer.gob.mx — verificar si acepta PDF o formato propio `[model knowledge — verify requisitos actuales del portal]`
- **NOMs publicadas en DOF:** la dependencia responsable especifica el medio de presentación en la propia publicación — confirmar antes de enviar
- **COFECE:** escrito formal con firma autógrafa o FIEL según el tipo de consulta `[model knowledge — verify requisitos actuales]`
- **IFT/CNBV:** revisar el acuerdo de consulta específico para el medio y formato requeridos

### Paso 6: árbol de decisión

> **¿Qué sigue?**
> 1. **Revisar y finalizar el comentario** — incorporo las correcciones y preparo la versión para firma.
> 2. **Agregar evidencia técnica** — si tienes estudios o datos, los integro al análisis de impacto.
> 3. **Coordinar con cámara sectorial** — adapto el comentario para presentación conjunta con [cámara configurada en el perfil].
> 4. **Monitorear resolución** — cuando la autoridad publique el análisis de comentarios, `/regulatorio-legal-mexico:dof-digest` identifica la publicación y compara con lo propuesto.
> 5. **Algo diferente** — dime qué necesitas.

---

**Nota del revisor:** La efectividad de los comentarios públicos depende de la especificidad. Las objeciones genéricas ("la norma es excesiva") se descartan rutinariamente; las propuestas de redacción concretas con justificación técnica tienen tasas de incorporación significativamente mayores. Un comentario que propone texto alternativo preciso — no solo señala el problema — es más difícil de ignorar que uno que solo objeta.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
