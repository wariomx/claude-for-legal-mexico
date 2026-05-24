---
description: >
  Análisis de exposición al EU AI Act para organizaciones con nexo europeo —
  determina qué sistemas IA caen bajo qué clasificación de riesgo, qué
  obligaciones aplican y en qué fechas, y produce hoja de ruta de cumplimiento.
argument-hint: ""
---

# /eu-ai-act-exposure

## Propósito

Determinar si el EU AI Act aplica a la organización (test de nexo europeo), y si aplica: para cada sistema de IA en el inventario, clasificar el riesgo, mapear las obligaciones específicas, y construir una hoja de ruta de cumplimiento con fechas.

**Advertencia fundamental:** El EU AI Act (Reglamento 2024/1689) es legislación nueva con actos delegados, guías de la Comisión Europea, y posiciones de autoridades nacionales de supervisión de IA (market surveillance authorities) en desarrollo activo. Toda fecha de vigencia, definición de riesgo, y obligación específica debe verificarse contra fuentes primarias antes de actuar.

`[model knowledge — verify: EU AI Act guidance — marco en evolución constante]`

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md`. Extraer:
- Nexo europeo ya determinado (si existe)
- Inventario de sistemas de IA con clasificaciones de triaje previas (si existen)
- Naturaleza del negocio (para determinar si la organización actúa como "provider," "deployer," o ambos bajo el EU AI Act)

Si hay clasificaciones de triaje previas (`/ia-governanza-legal-mexico:use-case-triage`), tomarlas como piso. No degradar una clasificación sin justificación explícita.

### 2. Test de nexo europeo

Si el nexo europeo no está determinado en el perfil, ejecutar el test:

El EU AI Act aplica cuando la organización:

**Como proveedor (provider):** Desarrolla o coloca en el mercado un sistema de IA destinado a ser usado en la UE, independientemente de dónde esté establecido el proveedor. `[model knowledge — verify]`

**Como importador:** Pone en el mercado de la UE un sistema de IA con marca o nombre de otra organización establecida fuera de la UE. `[model knowledge — verify]`

**Como distribuidor:** Hace disponible en el mercado de la UE un sistema de IA. `[model knowledge — verify]`

**Como deployer:** Usa un sistema de IA bajo su responsabilidad para un propósito profesional, cuando el uso ocurre en la UE o los efectos del uso se producen en la UE. Una empresa mexicana que usa un sistema de IA para tomar decisiones sobre personas en la UE (ej., evaluaciones de crédito de clientes europeos, reclutamiento de candidatos en Europa) puede ser deployer. `[model knowledge — verify]`

**Nexo indirecto:** La cadena contractual puede crear obligaciones. Si la organización es proveedor de otra empresa que despliega el sistema en la UE, puede tener obligaciones como "third-party supplier" bajo los requisitos que el deployer europeo impone al proveedor. `[model knowledge — verify]`

**Resultado del test:**
- **Aplica como provider:** la organización desarrolla y comercializa sistemas de IA en la UE
- **Aplica como deployer:** la organización usa sistemas de IA con efectos en la UE
- **Aplica indirectamente:** clientes o socios europeos requieren cumplimiento contractualmente
- **No aplica directamente:** sin nexo europeo verificable — anotar la conclusión y sus supuestos

Si el resultado es "no aplica," ofrecer igual la hoja de ruta para el marco mexicano vigente.

### 3. Clasificación de sistemas

Para cada sistema en el inventario (leer `use-case-register.yaml` si existe, o pedir al usuario que liste los sistemas):

Aplicar la pirámide de riesgo del EU AI Act (ver `/ia-governanza-legal-mexico:use-case-triage` para el árbol de decisión detallado). Producir una fila por sistema.

Si existe clasificación previa de triaje → tomar esa clasificación como piso confirmado.

`[model knowledge — verify: EU AI Act risk classification, Annex I and III]`

### 4. Mapa de obligaciones por clasificación

Para cada clasificación, las obligaciones aplicables `[model knowledge — verify]`:

**PROHIBIDO (Art. 5):**
- La práctica o sistema está prohibido a partir de febrero 2025
- Consecuencia: discontinuar o rediseñar fundamentalmente
- No hay hoja de ruta de cumplimiento — hay hoja de ruta de salida

**ALTO RIESGO (Anexo III):**
- Sistema de gestión de riesgos (Art. 9) — documentar y actualizar
- Datos y gobierno de datos (Art. 10) — documentar datos de entrenamiento
- Documentación técnica (Art. 11) — mantener documentación actualizada del sistema
- Registro de logs (Art. 12) — el sistema debe registrar automáticamente su funcionamiento
- Transparencia con deployers (Art. 13) — información clara al deployer sobre capacidades y limitaciones
- Supervisión humana (Art. 14) — diseñar el sistema para permitir supervisión humana efectiva
- Precisión, robustez, ciberseguridad (Art. 15) — requisitos técnicos de desempeño
- Registro en base de datos EU (Art. 49) — antes del despliegue (aplica a providers)
- Evaluación de conformidad (Art. 43) — autoevaluación o notified body según el caso
- Declaración CE de conformidad (Art. 48)
- Marcado CE (Art. 48)
- Evaluación de impacto de derechos fundamentales para deployers del sector público (Art. 27) `[model knowledge — verify]`

**RIESGO LIMITADO (Art. 50):**
- Transparencia: informar a los usuarios cuando interactúan con un sistema de IA (chatbots, deepfakes, reconocimiento de emociones)
- Etiquetado de contenido generado por IA

**RIESGO MÍNIMO:**
- Sin obligaciones específicas bajo el EU AI Act
- Buenas prácticas voluntarias (códigos de conducta opcionales)

**GPAI (Art. 55):**
- Documentación técnica y política de derechos de autor (aplica al proveedor del modelo)
- Resumen de datos de entrenamiento
- Para modelos GPAI de riesgo sistémico (>10^25 FLOPs): evaluaciones adversariales, reporte de incidentes, ciberseguridad

### 5. Hoja de ruta de cumplimiento

Producir la hoja de ruta con el encabezado de confidencialidad del perfil de práctica.

**Formato:**

---

**HOJA DE RUTA DE CUMPLIMIENTO — EU AI ACT**

**Organización:** [nombre]
**Rol bajo EU AI Act:** [provider / deployer / ambos / indirecto]
**Nexo europeo:** [naturaleza del nexo]
**Fecha del análisis:** [fecha]

**⚠️ Advertencia:** Todas las fechas de vigencia y obligaciones están sujetas a cambio. Verificar contra el texto oficial del Reglamento 2024/1689 (EUR-Lex) y las guías de la Comisión Europea antes de actuar. `[model knowledge — verify]`

---

**Fechas de aplicación escalonadas (referencia)** `[model knowledge — verify]`:

| Fase | Qué aplica | Fecha estimada |
|---|---|---|
| Fase 1 — Prohibiciones | Art. 5 — prácticas de IA prohibidas | Febrero 2025 |
| Fase 2 — GPAI | Art. 55 — modelos de propósito general | Agosto 2025 |
| Fase 3 — Alto riesgo (mayoría) | Anexo III — sistemas de alto riesgo | Agosto 2026 |
| Fase 4 — Alto riesgo (productos) | Anexo I — sistemas en productos regulados | Agosto 2027 |

---

**Inventario clasificado:**

| ID | Sistema | Clasificación | Rol (provider/deployer) | Obligaciones aplicables | Fecha límite | Estado actual |
|---|---|---|---|---|---|---|
| AI-001 | [nombre] | [prohibido/alto/limitado/mínimo/GPAI] | [provider/deployer] | [lista] | [fecha] | [pendiente/en curso/cumplido] |

---

**Acciones prioritarias por urgencia:**

🔴 **Inmediato (sistemas posiblemente prohibidos):**
- [lista de acciones]

🟠 **Antes de agosto 2026 (sistemas de alto riesgo — mayoría):**
- [lista de acciones]

🟡 **Antes de agosto 2027 (sistemas de alto riesgo en productos Anexo I):**
- [lista de acciones]

🟢 **Continuo (buenas prácticas):**
- [lista de acciones]

---

**Sistemas sin nexo europeo verificado:**
[Lista de sistemas que aplican solo al marco mexicano, con nota sobre qué obligaciones aplican bajo LGPDPPSP, CCF, etc.]

---

Nota del revisor estándar arriba del encabezado de confidencialidad. Incluir:
- Fuentes (LegalDataHunter / EUR-Lex / conocimiento del modelo)
- Advertencia de vigencia: el EU AI Act tiene actos delegados en desarrollo — verificar guías de la Comisión Europea y autoridades nacionales de supervisión antes de actuar
- Todos los items marcados `[review]` y `[model knowledge — verify]`
- Antes de confiar: verificar fechas de vigencia y clasificaciones contra fuentes primarias

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
