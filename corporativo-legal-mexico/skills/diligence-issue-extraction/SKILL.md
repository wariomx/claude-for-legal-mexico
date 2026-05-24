---
name: diligence-issue-extraction
description: >
  Leer documentos del VDR y extraer hallazgos conforme a las categorías de la
  firma y umbrales de materialidad, produciendo hallazgos en formato de
  memorándum interno. Usar cuando el usuario diga "revisar el data room",
  "extraer hallazgos de [carpeta]", "revisión de debida diligencia", "qué hay
  en el VDR", o señale documentos del VDR.
argument-hint: "[ruta de carpeta del VDR o nombre de categoría]"
---

# /diligence-issue-extraction

1. Cargar `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` + `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/deal-context.md`.
2. Usar el flujo de trabajo descrito abajo.
3. Revisar `ai-tool-handoff` — si la categoría es de volumen y la herramienta está configurada, hacer handoff primero.
4. Leer documentos, aplicar filtro de materialidad, extraer por categoría.
5. Hallazgos en formato de memorándum interno. Hacer handoff de consentimientos al checklist de cierre.

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omitir el resto de este párrafo — las habilidades usan el contexto a nivel práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y modificaciones. Escribir las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

El VDR tiene 2,000 documentos. En algún lugar están los 30 que importan para la operación. Esta habilidad lee documentos contra las categorías de debida diligencia y umbrales de materialidad de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`, extrae hallazgos y los escribe en formato de memorándum interno.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → Estructura de debida diligencia (categorías, umbrales de materialidad)
- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → Formato de memorándum de hallazgos (cómo se plantean los hallazgos)
- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/deal-context.md` → umbrales específicos de la operación, ubicación del VDR

Si deal-context.md no existe, preguntar para qué operación es.

## Flujo de trabajo

### Paso 1: Inventario del VDR

Si el MCP del VDR (Box/Intralinks/Datasite) está conectado, obtener el índice. Mapear las carpetas del VDR a las categorías de la lista de requerimientos de debida diligencia. Notar vacíos — categorías de la lista de requerimientos sin contenido correspondiente en el VDR.

```markdown
## Inventario del VDR: [Código de operación]

| Categoría de requerimiento | Carpeta VDR | Docs | Estatus |
|---|---|---|---|
| Corporativo y Organizacional | /01-Corporativo | 45 | Revisado |
| Contratos Relevantes | /02-Contratos | 312 | En progreso |
| Propiedad Intelectual | /03-PI | 89 | No iniciado |
| [etc.] | | | |

**Vacíos:** [Categorías de requerimiento sin contenido en el VDR — se necesita solicitud de seguimiento]
```

### Paso 2: Aplicar filtro de materialidad

Conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` / umbrales del deal-context. No revisar todo si el umbral dice contratos >$X.

Para contratos específicamente: ordenar por valor declarado (si está en el nombre de archivo/metadatos) o por importancia de la contraparte. Revisar de mayor a menor hasta alcanzar el umbral o agotar la categoría.

### Paso 3: Extraer hallazgos

Para cada documento leído, verificar contra las preocupaciones estándar de debida diligencia para su categoría:

**Contratos relevantes — conjunto estándar de extracción:**
- Cláusula de cambio de control (¿se detona por esta operación? ¿se requiere consentimiento?)
- Restricción de cesión (¿se puede transferir el contrato al comprador?)
- Exclusividad / cláusula de no competencia (¿restringe el negocio del comprador?)
- Nación más favorecida (NMF — restricciones de precio)
- Derechos de terminación (¿puede la contraparte terminar por la operación?)
- Indemnizaciones inusuales o exposición de responsabilidad

**Corporativo — conjunto estándar de extracción:**
- Exactitud del libro de registro de acciones, opciones/warrants vigentes
- Requisitos de resolución del Consejo de Administración para la operación
- Restricciones de convenios entre accionistas (arrastres, acompañamientos, derecho del tanto)
- Estructura de subsidiarias y acuerdos intercompañía

**Propiedad intelectual — conjunto estándar de extracción:**
- Cadena de titularidad (¿están en su lugar las cesiones de derechos de propiedad industrial de fundadores/empleados conforme a la LFPPI?)
- Código abierto en el producto (riesgo de copyleft)
- PI clave licenciada vs. propia
- Litigio de PI pendiente o amenazado (ante IMPI o tribunales)

**Laboral — conjunto estándar de extracción:**
- Detonantes de indemnización por cambio de control (costo de indemnización constitucional — 3 meses de salario + 20 días por año bajo LFT Art. 50; prima de antigüedad bajo LFT Art. 162)
- Riesgo de retención de personal clave
- Litigio laboral pendiente (ante Juntas de Conciliación y Arbitraje o Tribunales Laborales)
- Riesgo de simulación laboral (subcontratación regulada por reforma LFT 2021; verificar cumplimiento con REPSE e inscripción patronal ante IMSS/INFONAVIT)
- Obligaciones de aguinaldo, PTU (participación de los trabajadores en las utilidades) y prestaciones de ley
- Contingencias por IMSS/INFONAVIT (cuotas obrero-patronales, capitales constitutivos)

**Litigio — conjunto estándar de extracción:**
- Asuntos pendientes y reservas
- Reclamaciones amenazadas
- Investigaciones regulatorias (COFECE, CNBV, INAI, PROFECO, SAT)
- Litigio en serie (acciones colectivas bajo Art. 578-625 CFPC, demandas de consumidores ante PROFECO, etc.)

### Paso 4: Plantear cada hallazgo

> **Atribución de fuente.** Cuando un hallazgo haga referencia a una ley, reglamento, resolución judicial o acción de regulador — ej., una cláusula de cambio de control analizada bajo la ley aplicable, un vacío de titularidad de PI citado contra una doctrina específica, un litigio pendiente con una cita de resolución — etiquetar la cita con su origen: `[SCJN IUS]`, `[Semanario Judicial]`, `[DOF]`, o el nombre de la herramienta MCP para citas obtenidas de un conector de investigación legal; `[web search — verify]` para citas de búsqueda web; `[model knowledge — verify]` para citas recordadas de datos de entrenamiento; `[user provided]` para citas del VDR, memorandos del equipo de la operación o retroalimentación de abogados externos. Las citas de fuente documental (ruta VDR, Bates, nombre de archivo) conservan su referencia nativa. Las citas etiquetadas `verify` tienen mayor riesgo de fabricación y deben verificarse primero. Nunca eliminar ni colapsar las etiquetas.
>
> **Al disentir con una ley citada por el usuario, citar el texto o abstenerse de caracterizarla.** Si el usuario (o una nota del equipo, o una revelación del vendedor) cita una ley para una proposición que no crees correcta, y no tienes el texto legal disponible de una herramienta de investigación conectada o del VDR, no inventes una descripción de lo que dice la ley. Di en cambio: "Esa sección no coincide con lo que esperaría de un [aviso de traspaso de negocio / responsabilidad del sucesor / lo que sea] requisito — necesitaría consultar el texto real para decirte qué dice. `[statute unretrieved — verify]`" Luego (a) obtener el texto vía la herramienta de investigación configurada y citarlo, (b) pedir al usuario que pegue el texto, o (c) señalar para abogado externo. Una descripción errónea pero segura de una ley real es peor que "no sé" — un memorándum del equipo que cite un capítulo fabricado es más difícil de corregir que un vacío. Aplica en toda habilidad que caracterice una ley.
>
> **Sin suplemento silencioso.** Si una consulta de investigación a la herramienta de investigación legal configurada devuelve pocos o ningún resultado para una base legal que el hallazgo necesita (ej., la regla que gobierna un requisito de consentimiento por cambio de control, una doctrina de cesión de PI, una prueba de clasificación laboral), reportar lo que se encontró y detenerse. NO llenar el vacío con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece escasa para [regla / doctrina]. Opciones: (1) ampliar la consulta de búsqueda, (2) probar una herramienta de investigación diferente, (3) buscar en la web — los resultados se etiquetarán `[web search — verify]` y deben verificarse contra una fuente primaria antes de confiar en ellos, o (4) señalar como no verificado y detenerse. ¿Cuál prefieres?" Un abogado decide si aceptar fuentes de menor confianza.

Conforme a la plantilla de hallazgo en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si el memorándum semilla usó esto:

```
Hallazgo #N: [Título]
Categoría: [categoría de la lista de requerimientos]
Severidad: [nivel conforme al esquema de la firma]
Documentos: [ruta VDR + nombre del documento]
Hallazgo: [qué dice el documento y por qué importa]
Recomendación: [ajuste de precio / indemnización / consentimiento requerido / declaración y garantía / retirarse]
```

...entonces usar exactamente eso. Si el memorándum semilla fue viñetas, escribir viñetas.

**Calibración de severidad** (si el esquema de la firma es R/A/V):
- 🔴 **Rojo:** Afecta valor o estructura de la operación. Cambio de control que requiere consentimiento de cliente principal. Litigio material no revelado. Vacío de titularidad de PI.
- 🟡 **Amarillo:** Requiere atención, resoluble. Consentimiento requerido pero probablemente obtenible. Código abierto que requiere remediación. Riesgo de simulación laboral.
- 🟢 **Verde:** Anotado para el expediente. Consistente con las declaraciones. No requiere acción más allá de la declaración.

### Paso 5: Ensamblar por categoría

Agrupar hallazgos por categoría de la lista de requerimientos. Dentro de cada categoría, ordenar por severidad.

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

> Esta salida se deriva de materiales del VDR que están protegidos por secreto profesional, son confidenciales, o ambos. Hereda el estatus de protección y confidencialidad de la fuente — la distribución fuera del círculo de confidencialidad puede comprometer dicha protección. Almacenar con los archivos protegidos del asunto y tomar decisiones de distribución deliberadamente.

# Hallazgos de Debida Diligencia: [Código de operación] — [Categoría]

**Documentos revisados:** [N] de [M] en la categoría
**Cobertura:** [Todos | >$X umbral | Top N]
**Hallazgos:** [N]🔴 [N]🟡 [N]🟢

---

### Conclusión principal

[🔴 N bloqueantes · 🟠 N altos · 🟡 N medios] — [lo que el equipo de la operación necesita saber]

---

[Cada hallazgo en formato interno]

---

## Vacíos

- [Elemento de lista de requerimientos sin documento responsivo]
- [Documento referenciado pero no en el VDR]
```

## Handoffs

- **Hacia ai-tool-handoff:** Si Luminance/Kira está en uso conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`, hacer handoff de la revisión masiva de contratos ahí. Esta habilidad maneja los documentos de juicio (cartas complementarias, convenios modificatorios, cualquier cosa con la que la herramienta de IA tenga dificultades).
- **Hacia deal-team-summary:** Los hallazgos agregados alimentan el resumen del equipo de la operación.
- **Hacia material-contract-schedule:** Las extracciones a nivel contrato alimentan el anexo de revelaciones.
- **Hacia closing-checklist:** Cualquier hallazgo que implique una acción discreta previa al cierre se convierte en un elemento del checklist. El handoff no se limita a consentimientos de terceros — también cubre:
  - **Resolución de asamblea de accionistas / otra acción de cierre** — resoluciones de asamblea para aprobación de indemnizaciones por separación, resoluciones de asamblea requeridas (ordinaria o extraordinaria bajo LGSM Arts. 180-182), resoluciones del Consejo de Administración, ejercicio de derechos de preferencia, mecánicas de conversión, o cualquier otra aprobación corporativa que la operación necesite para cerrar. Caracterizar la acción, el quórum y mayoría requeridos, la fuente legal o estatutaria, y la restricción de tiempo.
  - **Trámites y autorizaciones regulatorias** — notificación de concentración a COFECE (LFCE), autorización de la Comisión Nacional de Inversiones Extranjeras (Ley de Inversión Extranjera), revisión de inversión extranjera, autorizaciones sectoriales señaladas durante la extracción.
  - **Consentimientos de contrapartes** — cambio de control, anti-cesión, consentimientos detonados por NMF.
  - **Liberaciones, terminaciones o pagos** — convenios de terminación laboral vinculados a cambio de control, cartas de pago, cancelación de gravámenes.
  - **Mecánicas de fideicomiso de garantía / retención** — si la extracción identifica un fideicomiso de garantía por indemnización, entregable de seguro de declaraciones y garantías (R&W), o retención vinculada a un hallazgo específico.
  Todo hallazgo con una etiqueta de acción previa al cierre debe llegar a closing-checklist, no solo los etiquetados "consentimiento." Si un hallazgo está en zona gris (podría necesitar acción de cierre, podría ser una obligación post-cierre), hacer handoff con una marca — closing-checklist puede descartarlo si el contrato de compraventa de acciones dice lo contrario. Sub-handoff es una puerta de un solo sentido; sobre-handoff se corrige en revisión.


**Responsabilidad del sucesor.** Señalar: demandas pendientes o amenazadas por responsabilidad extracontractual/productos, asuntos ambientales y obligaciones de remediación, exposición por traspaso de negocio en marcha (¿el vendedor retiene activos suficientes para pagar a sus acreedores restantes?), plan de disolución post-cierre del vendedor (si el vendedor se disuelve, los demandantes persiguen al comprador), y si el contrato de compraventa de acciones tiene un anexo de pasivos asumidos/excluidos que realmente cubra las exposiciones conocidas. En operaciones de compraventa de activos, la regla general bajo derecho mexicano es que la sociedad fusionante o la que adquiere un negocio en marcha puede asumir las obligaciones de la sociedad fusionada (Art. 224 LGSM — la sociedad que subsista o la que resulte de la fusión tomará a su cargo los derechos y obligaciones de las sociedades extinguidas). Para compraventas de activos, analizar si hay un traspaso de negociación mercantil (fondo de comercio) que pueda generar responsabilidad solidaria, así como las obligaciones laborales de sustitución patronal bajo LFT Art. 41 — este es el análisis que sorprende a los compradores que creen estar adquiriendo activos limpios.

## Procesamiento por lotes

Para categorías grandes (300 contratos), procesar en lotes. Después de cada lote, actualizar la lista acumulativa de hallazgos y señalar inmediatamente cualquier 🔴 — no esperar a que se complete la categoría para revelar un hallazgo que afecte la operación.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que esta habilidad acaba de producir — las cinco ramas predeterminadas (redactar el X, escalar, obtener más hechos, esperar y observar, algo más) son un punto de partida, no una restricción. El árbol es la salida; el abogado elige.

Si la extracción arrojó más de ~10 hallazgos, o en cualquier momento que el usuario lo solicite: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Adaptar la oferta para esta salida — conteos por severidad (🔴 / 🟠 / 🟡 / 🟢), conteos por categoría de la firma, y una tabla ordenable de hallazgos con materialidad, categoría y fuente del VDR.

## Lo que esta habilidad no hace

- No toma la decisión de materialidad en casos límite. Aplica el umbral; un humano decide lo fronterizo.
- No negocia declaraciones y garantías. Produce los hallazgos que las informan.
- No reemplaza la revisión masiva con IA. Para extracción de cláusulas de alto volumen, hacer handoff a Luminance/Kira conforme a `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Esta habilidad es para la capa de juicio.
