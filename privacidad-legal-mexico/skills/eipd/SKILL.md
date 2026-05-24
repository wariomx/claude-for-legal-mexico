---
description: >
  Conduce una Evaluación de Impacto en Protección de Datos (EIPD) para un
  tratamiento de datos nuevo o modificado — documenta el flujo de datos,
  identifica riesgos de privacidad, mapea las bases de licitud, y propone
  medidas de mitigación.
argument-hint: "[--tratamiento <nombre-del-tratamiento>]"
---

# /eipd

## Cuándo se ejecuta

La organización está lanzando un tratamiento nuevo o modificando uno existente y necesita evaluar el riesgo de privacidad antes de arrancar: procesamiento de datos sensibles, perfilado sistemático, tratamiento a gran escala, monitoreo de espacios públicos, o tratamiento de datos de menores. También se ejecuta cuando el INAI lo solicita o cuando el gap-analysis identificó la ausencia de EIPDs como hallazgo.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público) — determina la ley aplicable
- Tipos de datos personales tratados habitualmente (especialmente sensibles o de menores)
- Cadena de encargados activa (proveedores en nube, procesadores de datos)
- Umbral interno para activar EIPD

Si el perfil no existe o contiene `[PLACEHOLDER]` en campos críticos, detenerse: "Ejecuta `/privacidad-legal-mexico:cold-start-interview` primero."

### 2. Preguntas de activación — ¿se requiere EIPD?

Antes de iniciar la EIPD completa, confirmar que el tratamiento supera el umbral mínimo. El tratamiento requiere EIPD si involucra al menos uno de los siguientes factores de alto riesgo `[settled — last confirmed 2026-05-24]`:

| Factor de riesgo | Presente | Fundamento |
|---|---|---|
| Datos sensibles (Art. 3 Fr. VI LFPDPPP): salud, biométricos, origen racial, afiliación sindical, creencias | ¿Sí/No? | Arts. 8-9 LFPDPPP |
| Datos de menores de edad | ¿Sí/No? | Arts. 8-9 LFPDPPP |
| Perfilado sistemático o automatizado que produce decisiones con efectos jurídicos | ¿Sí/No? | Principio de finalidad, Art. 12 LFPDPPP |
| Tratamiento a gran escala (más del umbral definido en el perfil de práctica) | ¿Sí/No? | |
| Monitoreo sistemático de espacios públicos o de comunicaciones | ¿Sí/No? | |
| Transferencias internacionales de datos sensibles | ¿Sí/No? | Arts. 36-37 LFPDPPP |
| Uso de nuevas tecnologías con riesgos no evaluados previamente | ¿Sí/No? | |

Si ningún factor está presente: "El tratamiento descrito no supera el umbral mínimo para EIPD obligatoria. Puedes documentar esta determinación como memoria de decisión. Si quieres hacer igual una EIPD simplificada, continúa."

### 3. Paso 1 — Mapeo del flujo de datos

Documentar el tratamiento completo en la siguiente tabla:

| Elemento | Descripción |
|---|---|
| Nombre del tratamiento | |
| Finalidad primaria | |
| Finalidades secundarias (si aplica) | |
| Categorías de datos personales | |
| Categorías de datos sensibles (si aplica) | |
| Sujetos de datos | |
| Método de recolección | |
| Base de licitud del tratamiento | Consentimiento / Ejecución de contrato / Obligación legal / Interés legítimo `[model knowledge — verify base aplicable]` |
| Plazo de conservación | |
| Encargados y subencargados | |
| Transferencias a terceros | |
| Transferencias internacionales | Destino, base legal (Art. 37 LFPDPPP) |
| Tecnologías utilizadas | |

Marcar con `[review]` cualquier campo donde la determinación de la base de licitud requiera criterio jurídico.

### 4. Paso 2 — Necesidad y proporcionalidad

Evaluar si el tratamiento satisface el principio de minimización: los datos tratados deben ser estrictamente necesarios para la finalidad declarada. `[settled — last confirmed 2026-05-24]` (Art. 12 LFPDPPP, principio de proporcionalidad)

| Pregunta | Respuesta |
|---|---|
| ¿Cada categoría de dato es necesaria para la finalidad primaria? | `[review]` |
| ¿Podría lograrse la finalidad con menos datos o con datos anonimizados / seudonimizados? | `[review]` |
| ¿El plazo de conservación está justificado por la finalidad? | `[review]` |
| ¿Las finalidades secundarias pueden desvincularse de las primarias sin afectar el servicio? | `[review]` |

### 5. Paso 3 — Matriz de riesgos

Calificar cada riesgo por **Probabilidad** (Alta/Media/Baja) × **Impacto** (Alto/Medio/Bajo) = nivel de riesgo inherente (antes de controles).

| # | Riesgo | Probabilidad | Impacto | Riesgo inherente | Notas |
|---|---|---|---|---|---|
| R1 | Acceso no autorizado (interno o externo) | | | | |
| R2 | Divulgación no intencional a terceros | | | | |
| R3 | Pérdida o destrucción de datos | | | | |
| R4 | Desviación de finalidad (uso para un propósito no declarado) | | | | |
| R5 | Discriminación o afectación de derechos del titular | | | | |
| R6 | Robo de identidad o uso fraudulento | | | | |
| R7 | Vulneración por proveedor o encargado | | | | |
| R8 | Transferencia a jurisdicción sin nivel adecuado de protección | | | | [review: solo si hay transferencias internacionales] |

### 6. Paso 4 — Medidas de mitigación

Para cada riesgo con nivel Alto o Medio, proponer las medidas de mitigación técnicas, organizativas y contractuales:

**Técnicas:**
- Cifrado en reposo y en tránsito
- Control de acceso por roles (principio de menor privilegio)
- Seudonimización o anonimización donde sea posible
- Monitoreo de accesos y alertas de anomalías
- Políticas de retención y eliminación automatizada

**Organizativas:**
- Capacitación al personal con acceso a los datos
- Procedimientos de respuesta a incidentes
- Auditorías periódicas del tratamiento
- Designación de responsable interno del tratamiento

**Contractuales:**
- Contratos de encargado (DPA) con todos los procesadores (Arts. 50-53 Reglamento LFPDPPP) `[settled — last confirmed 2026-05-24]`
- Cláusulas de transferencia internacional si aplica (Art. 37 LFPDPPP)
- Cláusulas de notificación de vulneraciones en contratos con encargados

### 7. Paso 5 — Determinación del riesgo residual

Después de aplicar las medidas de mitigación, recalificar cada riesgo:

| # | Riesgo | Riesgo inherente | Mitigaciones aplicadas | Riesgo residual |
|---|---|---|---|---|
| R1 | | | | |
| R2 | | | | |
| R3 | | | | |
| R4 | | | | |
| R5 | | | | |
| R6 | | | | |
| R7 | | | | |
| R8 | | | | |

**Determinación final:**
- 🟢 **Bajo** — el tratamiento puede proceder.
- 🟡 **Medio** — el tratamiento puede proceder con las medidas de mitigación implementadas y revisión periódica.
- 🟠 **Alto** — el tratamiento requiere aprobación del responsable de privacidad antes de proceder, con plan de mitigación adicional documentado.
- 🔴 **Alto no mitigable** — se recomienda consultar con el INAI o rediseñar el tratamiento antes de lanzar. No lanzar en este estado. `[review: determinar si el riesgo residual es aceptable]`

### 8. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Tratamiento evaluado:** [nombre del tratamiento]
> - **Riesgo residual:** [🔴 Alto no mitigable / 🟠 Alto / 🟡 Medio / 🟢 Bajo]
> - **Marcado para tu criterio:** [N elementos marcados `[review]` en línea | ninguno]
> - **Formato INAI:** El INAI no ha mandado un formato específico de EIPD a la fecha de 2026 — esta EIPD sigue mejores prácticas internacionales alineadas con los principios de la LFPDPPP. `[model knowledge — verify lineamientos INAI vigentes sobre EIPDs]`
> - **Antes de lanzar:** [las 1-2 cosas más urgentes antes de iniciar el tratamiento]

### 9. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Exportar la EIPD como documento** — Produciré el documento EIPD completo en formato limpio, listo para archivar o presentar.
> 2. **Diseñar medidas de mitigación adicionales** — Si el riesgo residual es Alto, profundizaré en las opciones de mitigación para ese riesgo específico.
> 3. **Consultar el INAI** — Si el riesgo residual es no mitigable, redactaré una consulta formal al INAI.
> 4. **Rediseñar el tratamiento** — Identificaré qué elementos del tratamiento generan más riesgo y propondré alternativas de diseño con menor impacto en privacidad.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
