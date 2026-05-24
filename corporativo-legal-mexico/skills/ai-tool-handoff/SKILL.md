---
name: ai-tool-handoff
description: >
  Detecta cuando Luminance, Kira u otra herramienta de revisión masiva está en
  uso, transfiere la extracción de cláusulas de alto volumen a ella, y aplica
  control de calidad a su salida conforme al nivel de confianza en
  `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`.
  Usar cuando el usuario diga "enviar a Luminance", "revisión masiva",
  "extracción con IA", o cuando diligence-issue-extraction encuentre una
  categoría de alto volumen.
---

# Transferencia a Herramienta de IA

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omitir el resto de este párrafo — las habilidades usan el contexto a nivel práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y modificaciones. Escribir las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

Luminance y Kira son buenas para una cosa: leer 500 contratos y encontrar cada cláusula de cambio de control. Son menos buenas en juicio — decidir si una cláusula de cambio de control en particular se detona efectivamente por la estructura de esta operación.

Esta habilidad transfiere la extracción masiva a la herramienta adecuada y luego aplica la capa de control de calidad a lo que regresa.

**Antes de transferir:** probar `tabular-review` primero (`/corporativo-legal-mexico:tabular-review`). Para todo lo que el entorno del usuario pueda manejar — unos cientos de documentos, un esquema de columnas definido — la revisión tabular nativa es más rápida de configurar, no tiene costo por documento, y mantiene el producto de trabajo local. Transferir a Luminance/Kira cuando el corpus sea genuinamente demasiado grande, el equipo ya tenga licencia y flujo de trabajo, o el asunto requiera una herramienta con una cadena de procedencia validada.

## Cargar contexto

`~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → Revisión asistida por IA:
- Herramienta en uso (Luminance / Kira / ninguna)
- Para qué se usa (qué tipos de cláusula)
- Nivel de confianza (usar tal cual / revisar muestra / re-revisión completa)
- Proceso de transferencia (quién carga, quién hace control de calidad)

Si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` dice que no hay herramienta de IA → esta habilidad es no-op. Todo pasa por diligence-issue-extraction directamente.

## Cuándo transferir

Transferir cuando se cumplan todas:
- La categoría tiene >50 documentos (por debajo de eso, es más rápido simplemente leerlos)
- El objetivo de extracción es un tipo de cláusula en el que la herramienta es buena (cambio de control, cesión, exclusividad, NMF, terminación, renovación automática)
- Los documentos son razonablemente uniformes (todos contratos con clientes en formatos similares — no una mezcla de contratos, cartas y actas del Consejo de Administración)

No transferir:
- Documentos a la medida o fuertemente negociados
- Cartas complementarias y convenios modificatorios (dependen del contexto, las herramientas pierden la interacción con el contrato principal)
- Cualquier caso donde la pregunta sea "qué significa esto para la operación" no "¿existe esta cláusula?"

## La transferencia

### Paso 1: Preparar el lote

- Identificar documentos para el lote (del inventario del VDR)
- Especificar objetivos de extracción conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` (qué tipos de cláusula)
- Anotar el umbral de materialidad para que la salida de la herramienta pueda filtrarse

### Paso 2: Cargar (o instruir al responsable de carga)

Conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` — quién carga. Si eres tú, generar las instrucciones de carga. Si es alguien más, generar la solicitud:

```markdown
## Solicitud de Carga a [Herramienta] — [Código de operación] — [Categoría]

**Documentos:** [N] docs de la carpeta VDR [ruta]
**Cargar en:** [Workspace/asunto de la herramienta]
**Objetivos de extracción:**
- Cambio de control / cesión
- Exclusividad
- [etc. conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`]

**Filtrar salida:** Señalar solo donde el objetivo de extracción esté presente — no se necesita "no se encontró cláusula de cambio de control" para cada documento.

**Entregar para:** [fecha]
```

### Paso 3: Control de calidad de la salida

Cuando la herramienta devuelva resultados, aplicar el nivel de confianza:

**"Usar tal cual":** Ingerir directamente en hallazgos de debida diligencia. (Solo si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` dice esto — es raro.)

**"Revisar muestra de X%":** Tomar una muestra aleatoria de X% de los documentos señalados. Para cada uno, leer la cláusula real y comparar con la extracción de la herramienta. Si la tasa de error es baja, aceptar el lote. Si se encuentran errores, ampliar la muestra.

**"Revisión humana completa de los señalados":** La herramienta reduce el universo (500 docs → 80 con cláusulas de cambio de control). Un humano lee los 80. La herramienta ahorró el tiempo de leer los 420 limpios.

### Paso 4: Capa de juicio

La herramienta encontró las cláusulas. Ahora aplicar juicio:

Para cada cláusula de cambio de control señalada: ¿se detona efectivamente por esta operación?
- Compraventa de acciones vs. compraventa de activos vs. fusión — distintos detonantes
- "Cambio de control" definido cómo en el contrato — ¿mayoría accionaria? ¿control del Consejo de Administración? ¿algo más?
- ¿Hay una excepción para este tipo de operación?

Esta es la parte que la herramienta no puede hacer. La salida va a hallazgos de debida diligencia en formato interno.

## Salida

> El resumen de control de calidad a continuación se deriva de documentos del VDR que están protegidos por secreto profesional, son confidenciales, o ambos. Hereda el estatus de protección y confidencialidad de las fuentes — la distribución fuera del círculo de confidencialidad puede comprometer dicha protección. Almacenar con los archivos protegidos del asunto.

```markdown
## Resumen de Transferencia a Herramienta de IA — [Categoría]

**Herramienta:** [Luminance / Kira]
**Documentos procesados:** [N]
**Objetivos de extracción:** [tipos de cláusula]

### Control de Calidad

**Nivel de confianza:** [conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`]
**Tamaño de muestra:** [N] docs revisados en muestra
**Tasa de error:** [X]% — [Aceptado / Muestra ampliada / Re-revisión completa activada]

### Resultados

| Tipo de cláusula | Docs señalados | Después de capa de juicio | Material |
|---|---|---|---|
| Cambio de control | [N] | [N efectivamente detonados por estructura de la operación] | [N por encima del umbral] |
| Cesión | [N] | [N] | [N] |

**→ [N] hallazgos agregados a temas de debida diligencia**
**→ [N] consentimientos agregados al checklist de cierre**
```

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que esta habilidad acaba de producir — las cinco ramas predeterminadas (redactar el X, escalar, obtener más hechos, esperar y observar, algo más) son un punto de partida, no una restricción. El árbol es la salida; el abogado elige.

## Lo que esta habilidad no hace

- No ejecuta Luminance ni Kira — gestiona la transferencia y el control de calidad. Un humano (o la propia interfaz de la herramienta) ejecuta la extracción.
- No reemplaza la salida de la herramienta con su propio juicio por completo — si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` dice revisar muestra del 10%, revisar el 10%, no el 100%.
- No decide el nivel de confianza — eso está en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`, establecido en cold-start basado en la experiencia del equipo con la herramienta.
