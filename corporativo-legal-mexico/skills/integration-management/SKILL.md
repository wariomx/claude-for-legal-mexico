---
name: integration-management
description: >
  Rastreador de integración post-cierre de F&A — plan de trabajo por fases,
  seguimiento de consentimientos, cesión de contratos a escala, reportes de
  avance semanales. Inicializa a partir de los documentos disponibles de la
  operación (contrato de compraventa de acciones, resumen de la operación,
  checklist de cierre) y se conecta a deal-context.md y closing-checklist.yaml
  del cold-start de F&A. Usar cuando el usuario dice "integración",
  "post-cierre", "consentimientos pendientes", "cesión de contratos",
  "estado de integración", "qué falta de la operación", "integration",
  "post-close", "consents outstanding", o "what's left on the deal".
argument-hint: "[--init | --contracts | --report | --update | --export [--format csv|table] [--section all|consents|contracts|workplan]] [--deal [code]]"
---

# /integration-management

1. Cargar `deal-context.md` para código de operación, objetivo, fecha de cierre, líder de la operación.
2. Cargar `integration-tracker.yaml` si existe (o crear con --init).
3. Usar el flujo de trabajo descrito abajo.
4. Despachar por bandera:
   - `--init`: Modo 1 — leer contrato de compraventa, construir plan de trabajo por fases, rastreador de consentimientos
   - `--contracts`: Modo 2 — importar lista de contratos (repositorio o carga), clasificar por nivel y tipo
   - `--report`: Modo 3 — generar reporte de avance
   - `--update`: Modo 4 — actualización manual o parsear documento de avance cargado
   - `--export`: Modo 5 — exportar a CSV o tabla
5. Leer/escribir `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/integration-tracker.yaml`.
6. Después de cualquier escritura: mostrar resumen de cambios y alertar sobre nuevas banderas.

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗` (predeterminado para usuarios in-house), omitir el resto de este párrafo — los skills usan contexto a nivel de práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o indica `practice-level`." Cargar el `matter.md` del asunto activo para contexto y excepciones específicas del asunto. Escribir productos en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` sea `on`.

---

## Propósito

El abogado externo cierra la operación. El equipo jurídico interno hereda el trabajo pendiente. Este skill es la capa de gestión de programa para la integración post-cierre — no la integración de negocio, no los sistemas de TI, no el diseño organizacional de RRHH. El flujo de trabajo jurídico: consentimientos, cesiones de contratos, racionalización de entidades, inscripciones de PI, obligaciones del contrato de compraventa de acciones. Rastrea qué está hecho, qué vence, qué está bloqueado y qué necesita una decisión.

---

## Archivo rastreador

Vive en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/integration-tracker.yaml`. Leer `deal-context.md` para el código de operación, nombre del objetivo, fecha de cierre y líder de la operación. Heredar cualquier elemento post-cierre de `closing-checklist.yaml` si existe.

```yaml
# integration-tracker.yaml

metadata:
  deal_code: "[code]"
  target: "[nombre de la sociedad]"
  close_date: "[AAAA-MM-DD]"
  deal_lead: "[nombre]"
  outside_counsel: "[despacho y abogado responsable]"
  last_updated: "[fecha]"
  last_status_report: "[fecha o null]"

pa_dates:
  required_consents_deadline: "[AAAA-MM-DD — extraer del contrato de compraventa]"
  rep_survival_expires: "[AAAA-MM-DD]"
  escrow_release: "[AAAA-MM-DD o null]"
  earnout_milestones:
    - description: "[hito]"
      measurement_date: "[AAAA-MM-DD]"
      payment_date: "[AAAA-MM-DD]"
      owner: "finance"   # siempre finanzas — jurídico solo rastrea la fecha

workplan:
  day_1:
    target_date: "[close_date + 7 días]"
    items: []
  day_30:
    target_date: "[close_date + 30 días]"
    items: []
  day_90:
    target_date: "[close_date + 90 días]"
    items: []
  day_180:
    target_date: "[close_date + 180 días]"
    items: []

required_consents: []
desired_consents: []

contracts:
  source: "[repository / manual-upload / disclosure-schedule]"
  repository_path: "[ruta o null]"
  last_imported: "[fecha]"
  total: 0
  tier_1: []
  tier_2: []
  tier_3: []
  tier_4: []
```

**Estructura de elemento del plan de trabajo:**
```yaml
- id: "W-001"
  description: "[acción a realizar]"
  phase: "[day_1 / day_30 / day_90 / day_180]"
  owner: "[legal-owns / legal-supports]"
  workstream: "[legal / hr / it / finance / real-estate / other]"
  priority: "[critical / high / medium / low]"
  deadline: "[AAAA-MM-DD o null]"
  deadline_basis: "[pa-obligation / regulatory / best-practice]"
  status: "[not_started / in_progress / complete / blocked / deferred]"
  blocker: "[descripción o null]"
  depends_on: "[id del elemento o null]"
  notes: ""
```

**Estructura de entrada de consentimiento:**
```yaml
- id: "CON-001"
  counterparty: "[nombre]"
  contract_type: "[customer / vendor / lease / IP-license / financial / other]"
  required_consent: true        # true = nombrado en el anexo de Consentimientos Requeridos del contrato
  pa_deadline: "[AAAA-MM-DD]"   # solo para required_consent: true
  status: "[not_started / outreach_sent / in_negotiation / obtained / waived / refused]"
  assigned_to: "[nombre o null]"
  outreach_date: "[fecha o null]"
  obtained_date: "[fecha o null]"
  notes: ""
```

**Estructura de entrada de contrato:**
```yaml
- id: "C-001"
  name: "[nombre del contrato o nombre de archivo]"
  counterparty: "[nombre de la parte]"
  contract_type: "[MSA / SaaS / arrendamiento / IP-license / empleo / NDA / otro]"
  annual_value: "[monto o unknown]"
  assignment_mechanism: "[auto-assign / consent-required / coc-provision / silent]"
  tier: 1   # 1=Consentimiento Requerido, 2=material+consentimiento requerido, 3=cambio de control, 4=cesión automática
  required_consent: false
  pa_deadline: "[AAAA-MM-DD o null]"
  status: "[not_reviewed / no_action / consent_pending / outreach_sent / in_negotiation / consent_obtained / assignment_complete / waived / refused / coc_triggered]"
  assigned_to: "[nombre o null]"
  notes: ""
  last_updated: "[fecha]"
```

---

## Modo 1: Inicializar

```
/corporativo-legal-mexico:integration-management --init [--deal [code]]
```

### Paso 1: Cargar contexto de la operación

Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/deal-context.md`. Si no se encuentra: solicitar código de la operación, sociedad objetivo, fecha de cierre, líder de la operación y abogado externo. Escribir deal-context.md si no existe.

Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/closing-checklist.yaml` si existe. Cualquier elemento marcado como post-cierre se convierte en elemento del plan de trabajo Día 1 o Día 30 (heredar estado del closing-checklist).

### Paso 2: Leer documentos de la operación

**Un contrato de compraventa de acciones completo produce el rastreador más completo.** El anexo de Consentimientos Requeridos y la sección de obligaciones post-cierre del contrato son la fuente autoritativa para fechas límite firmes y obligaciones legales. Pero el skill puede inicializarse útilmente con lo que esté disponible — datos parciales producen un rastreador inicial que el abogado completa, en vez de una página en blanco.

> ¿Qué documentos de la operación tienes disponibles? Comparte lo que exista:
>
> **Ideal:** El contrato de compraventa de acciones (cargar o ruta de documento conectado). Leeré las obligaciones post-cierre, el anexo de Consentimientos Requeridos, los períodos de supervivencia de declaraciones y garantías, los términos del fideicomiso de garantía (escrow) y las disposiciones de earn-out.
>
> **También útil — comparte cualquier combinación de:**
> - Resumen de la operación o term sheet (me da la economía clave y el cronograma)
> - Lista de pendientes de integración o checklist post-cierre del abogado externo
> - Plan de trabajo o rastreador de integración existente (lo importo y continúo desde ahí)
> - Checklist de cierre — si fue generado por el skill de cold-start de F&A, lo heredo automáticamente de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/closing-checklist.yaml`
> - Lista de Consentimientos Requeridos sola (si el contrato lo tiene el abogado externo)
>
> **Si no tienes nada escrito:** Cuéntame la operación en términos simples — quién fue adquirido, cuándo cerró, cuáles son los principales pendientes — y construiré un rastreador inicial basado en el plan de trabajo estándar Día 1/30/90/180 que tú editas.

**Lo que cambia según lo proporcionado:**

| Documento | Lo que obtienes |
|---|---|
| Contrato de compraventa completo | Plan de trabajo completo + Consentimientos Requeridos con fechas límite + fechas del contrato |
| Contrato + lista de contratos | Rastreador completo + lista de cesión de contratos por nivel |
| Resumen de operación / lista de pendientes | Esqueleto de plan de trabajo estándar, Consentimientos Requeridos como marcadores de posición |
| Nada | Andamio de plan de trabajo estándar; el abogado completa consentimientos y listas de contratos |

El rastreador está diseñado para construirse progresivamente — un esqueleto hoy, completado conforme se disponga de más información.

**Del contrato de compraventa extraer:**

*Anexo de Consentimientos Requeridos:*
- Para cada consentimiento: nombre de la contraparte, tipo de contrato y la fecha límite contractual. Establecer como required_consent: true con pa_deadline poblado.

*Obligaciones post-cierre:*
- Mapear cada obligación a un elemento del plan de trabajo. Asignar a la fase correcta según la fecha límite. Etiquetar como pa-obligation en deadline_basis.

*Fechas clave:*
- Fecha límite de Consentimientos Requeridos — extraer del contrato
- Vencimiento de supervivencia de declaraciones y garantías — extraer los períodos específicos de supervivencia del contrato. Las declaraciones generales, fundamentales y fiscales típicamente tienen períodos de supervivencia diferentes; extraer cada uno que el contrato defina y registrarlos por separado. No asumir un período por defecto.
- Fecha(s) de liberación del fideicomiso de garantía (escrow) — extraer del contrato
- Cualquier fecha de medición y pago de earn-out — agregar a pa_dates.earnout_milestones, owner siempre establecido como "finance"

### Paso 3: Construir el plan de trabajo por fases

Generar elementos estándar del plan de trabajo para cada fase. Agregar obligaciones del contrato de compraventa extraídas en el Paso 2. Los elementos heredados del checklist de cierre vienen pre-poblados.

**Día 1 — legal-owns:**
- Cambio de denominación social ante notario público y RPC (si la entidad adquirida será renombrada) [priority: critical]
- Actualización de firmas bancarias — notificar al banco con documentación de cierre [priority: critical]
- Aviso de cambio de accionistas/socios al Registro Público de Comercio [priority: high]
- Ejecución de cesiones de PI clave — si alguna cesión de PI fue diferida del cierre [priority: critical]
- Transferencia de nombres de dominio y cuentas de redes sociales [priority: high]
- Seguro de responsabilidad civil para consejeros y directivos — confirmar que la póliza de cola esté vigente para los consejeros de la entidad adquirida [priority: critical]
- Avisos al Registro Público de Comercio de cambios de control donde sea requerido [priority: high]
- Aviso de cambio de situación fiscal ante el SAT (si aplica) [priority: high]

**Día 1 — legal-supports:**
- Comunicación a empleados y anuncios (RRHH lidera, jurídico revisa) [priority: critical]
- Confirmación de cobertura de prestaciones día 1 (RRHH lidera, jurídico asesora sobre continuidad de cobertura IMSS y términos de prestaciones). Nota: en México, la relación laboral es continua bajo sustitución patronal (Art. 41 LFT) — no hay equivalente a COBRA; la cobertura del IMSS continúa por ley si se cumple con el aviso de sustitución patronal [priority: critical]
- Cartas de comunicación a clientes (el negocio lidera, jurídico revisa por precisión)

**Día 30 — legal-owns:**
- Impulso inicial de Consentimientos Requeridos — contactar a todas las contrapartes, documentar acercamientos [priority: critical]
- Inscripción de cesión de PI ante IMPI (patentes, marcas registradas) [priority: high]
- Registro de cesión de derechos de autor ante INDAUTOR [priority: medium]
- Registro de cesión de marcas ante IMPI [priority: high]
- Revisión de contratos materiales — completar análisis de cesión de contratos nivel 1 y nivel 2 [priority: high]
- Confirmación final de póliza de cola de seguro de responsabilidad civil [priority: high]
- Aviso de sustitución patronal ante IMSS e INFONAVIT (Art. 41 LFT) — obligatorio si hay empleados [priority: critical]

**Día 30 — legal-supports:**
- Revisión de privacidad de migración de datos (TI lidera, jurídico asesora sobre mecanismos de transferencia de datos y cumplimiento de la LGPDPPSP)
- Revisión de contratos de arrendamiento para cláusulas de cesión (instalaciones lidera, jurídico asesora)

**Día 90 — legal-owns:**
- Fecha límite de Consentimientos Requeridos — todos los Consentimientos Requeridos deben estar obtenidos o escalados [priority: critical, deadline: pa_dates.required_consents_deadline]
- Decisión de racionalización de entidades — recomendar mantener separada / fusionar / disolver [priority: high]
- Documentación de continuidad o terminación de plan de prestaciones laborales [priority: high]
- Segundo impulso de consentimientos — consentimientos pendientes restantes [priority: high]
- Resolución de contratos nivel 3 con cláusula de cambio de control [priority: critical]
- Inscripción del beneficiario controlador ante el SAT (Art. 32-B Quáter CFF) si aplica [priority: high]

**Día 90 — legal-supports:**
- Documentación completa de armonización de RRHH (RRHH lidera, jurídico asesora sobre legislación laboral — Ley Federal del Trabajo, condiciones generales de trabajo, derechos adquiridos)

**Día 180 — legal-owns:**
- Protocolización de fusión ante notario público + inscripción en RPC — si la decisión de racionalización es fusionar [priority: high]
- Protocolización de disolución y liquidación ante notario público + inscripción en RPC — si la decisión de racionalización es liquidar [priority: high]
- Novación completa de contratos — contratos que requieren el nombre del adquirente [priority: high]
- Seguimiento de supervivencia de declaraciones y garantías — notar fecha de vencimiento próxima [priority: medium]
- Baja ante el SAT de la entidad disuelta (si aplica) [priority: high]

Mostrar resumen después de generar:

```
Rastreador de integración inicializado — [Código de operación] / [Objetivo]

Fecha de cierre: [fecha]
Fecha límite de Consentimientos Requeridos: [fecha] ([N] días desde hoy)
Vencimiento de supervivencia de declaraciones: [fecha]

Elementos del plan de trabajo: [N] ([N] legal-owns, [N] legal-supports)
Consentimientos Requeridos: [N] (del anexo del contrato)
Consentimientos Deseados: [N] (del due diligence — sin fecha límite contractual)

Cesión de contratos: aún no importada — ejecutar --contracts para poblar

Siguiente paso: ejecutar /corporativo-legal-mexico:integration-management --contracts para
importar la lista de contratos, luego --report para ver tu primer resumen de avance.
```

---

## Modo 2: Cesión de Contratos

```
/corporativo-legal-mexico:integration-management --contracts [--deal [code]]
```

Esta es la inicialización dedicada de cesión de contratos. Separada de la inicialización principal para que pueda ejecutarse de forma independiente y re-ejecutarse cuando la lista de contratos cambie.

### Paso 1: Obtener la lista de contratos

Dos caminos — usar el que aplique:

**Camino A: Repositorio conectado**

> ¿Tu repositorio de contratos está conectado? (Google Drive, Box, SharePoint, o un VDR que siga accesible post-cierre?)
>
> Si sí: dame la ruta de carpeta o nombre de carpeta para los contratos de la sociedad adquirida. Extraeré una lista de lo que hay ahí y leeré cada contrato buscando la cláusula de cesión y la contraparte.

Buscar en el repositorio conectado. Para cada documento encontrado:
- Extraer nombre de archivo y ruta
- Leer el documento — identificar: parte del contrato (nombre de la contraparte), tipo de contrato (del encabezado o materia), texto de la cláusula de cesión, texto de la cláusula de cambio de control si la hay, y valor anual si se indica.

**Camino B: Carga manual de lista**

> Carga una lista de contratos. Puede ser:
> - El anexo de Contratos Materiales de los anexos de revelación del contrato de compraventa
> - Un CSV o Excel exportado de su sistema de gestión de contratos
> - Una lista preparada manualmente
>
> Columnas mínimas requeridas: Nombre del Contrato, Contraparte. Útiles pero opcionales: Tipo de Contrato, Valor Anual, texto de la Cláusula de Cesión.

Leer la lista cargada. Para contratos donde no se proporcionó texto de la cláusula de cesión, establecer assignment_mechanism como "not_reviewed" y marcar para seguimiento.

**Camino C: Anexo de revelación**

Si ni repositorio ni lista están disponibles, leer el anexo de Contratos Materiales de los anexos de revelación del contrato (del contrato cargado en --init). Esto da la lista mínima requerida — partes y tipos de contrato. Las cláusulas de cesión necesitarán revisión manual.

### Paso 2: Determinar mecanismo de cesión

Para cada contrato, clasificar el mecanismo de cesión:

| Mecanismo | Definición | Nivel |
|---|---|---|
| `consent-required` | Cláusula explícita que prohíbe cesión sin consentimiento de la contraparte | 1 o 2 |
| `coc-provision` | Cláusula de cambio de control que otorga a la contraparte derecho de terminación o consentimiento activado por la operación | 3 |
| `auto-assign` | Sin restricción, o permiso explícito para ceder a afiliadas o sucesoras | 4 |
| `silent` | Sin cláusula de cesión — remitirse al derecho aplicable. Investigar la regla supletoria del derecho aplicable para cesión de contratos cuando el contrato es silente y citar la norma aplicable (en México: Arts. 2051-2054 del Código Civil Federal para cesión de derechos; Art. 2051 para cesión de créditos). Marcar para revisión del abogado. | 2 |
| `not_reviewed` | No se pudo leer o localizar la cláusula de cesión | Marcar para revisión manual |

Para contratos señalados en el anexo de Consentimientos Requeridos del contrato de compraventa: anular nivel a 1 independientemente de la clasificación del mecanismo de cesión.

### Paso 3: Asignación de nivel

```
Nivel 1 — Consentimientos Requeridos: [N] contratos
  Nombrados en el anexo del contrato, fecha límite firme [fecha], se debe obtener consentimiento

Nivel 2 — Material, consentimiento requerido: [N] contratos
  Restricción de cesión presente, no en el anexo del contrato
  Cronograma recomendado: obtener dentro del Día 90

Nivel 3 — Cláusulas de cambio de control: [N] contratos ⚠️
  La contraparte tiene derecho de terminación o consentimiento activado por el cierre
  ACCIÓN REQUERIDA: contactar a la contraparte de inmediato — el cambio de control puede haberse activado ya

Nivel 4 — Cesión automática / sin acción: [N] contratos
  Se cede automáticamente o por disposición de afiliada/sucesora
  Solo seguimiento — no se requiere acercamiento

Sin revisar: [N] contratos
  No se pudo determinar el mecanismo de cesión — revisión manual requerida
```

Mostrar nivel 3 por separado y de forma prominente. Una cláusula de cambio de control puede haberse activado en la fecha de cierre — la contraparte puede tener un derecho de terminación que está corriendo en este momento.

### Paso 4: Generar entradas de estado

Para cada contrato, crear una entrada en el rastreador con:
- Todos los campos extraídos (contraparte, tipo, valor, mecanismo, nivel)
- Estado inicial: nivel 4 → `no_action`; nivel 3 → `coc_triggered`; niveles 1/2 → `consent_pending`; not_reviewed → `not_reviewed`
- pa_deadline poblado para nivel 1 del anexo de Consentimientos Requeridos

---

## Modo 3: Reporte de Avance

```
/corporativo-legal-mexico:integration-management --report [--deal [code]]
```

Lee el estado actual del rastreador. Produce:

```
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

> Este reporte de avance se deriva del contrato de compraventa de acciones, hallazgos del due diligence y registros de integración post-cierre. Hereda su estado de privilegio y confidencialidad — la distribución fuera del círculo de secreto profesional puede perder la protección. Confirmar la lista de destinatarios antes de enviar.

AVANCE DE INTEGRACIÓN — [Código de operación] / [Objetivo]
[Fecha] — Día [N] post-cierre

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESUMEN EJECUTIVO
[Párrafo de 2-3 oraciones: avance general, mayor riesgo, logro clave desde el último reporte]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONSENTIMIENTOS REQUERIDOS  [fecha límite: FECHA — N días restantes]
  Obtenidos:         [N] de [total]  ████████░░  [%]
  En negociación:    [N]
  Acercamiento enviado: [N]
  No iniciados:      [N]
  Rechazados:        [N] ⚠️

⚠️ EN RIESGO: [contraparte] — fecha límite en [N] días, sin respuesta al acercamiento
⚠️ RECHAZADO: [contraparte] — obligación contractual no cumplida; escalar a abogado externo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CESIÓN DE CONTRATOS
  Nivel 1 (Consentimientos Requeridos):  [N] completos / [N] en proceso / [N] pendientes
  Nivel 2 (Contratos materiales):        [N] completos / [N] en proceso / [N] pendientes
  Nivel 3 (Cláusulas de cambio de control): [N] resueltos / [N] pendientes ⚠️
  Nivel 4 (Cesión automática):           [N] — sin acción requerida

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLAN DE TRABAJO — LEGAL OWNS
  🔴 VENCIDOS ([N]):
    [elemento] — venció [fecha]

  ⏰ VENCE ESTA SEMANA ([N]):
    [elemento] — vence [fecha]

  ✅ COMPLETADOS DESDE EL ÚLTIMO REPORTE ([N]):
    [elemento] — completado [fecha]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BLOQUEOS Y DECISIONES PENDIENTES
  [elemento] — bloqueado por: [descripción] — responsable: [nombre]
  [elemento] — decisión necesaria: [descripción] — recomendación: [opción]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FECHAS CLAVE PRÓXIMAS
  [fecha] — [hito / fecha límite]
  [fecha] — Vence supervivencia de declaraciones y garantías — confirmar que no haya reclamaciones de indemnización pendientes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Modo 4: Actualizar

```
/corporativo-legal-mexico:integration-management --update [--deal [code]]
```

**Actualización manual:** El abogado le dice a Claude qué cambió.

> "Obtuvimos el consentimiento de Salesforce. Marcarlo como obtenido, asignado a [nombre], fecha de hoy."
> "La decisión de racionalización de entidades es fusionar. Actualizar estado y agregar la protocolización de fusión al Día 180."
> "[Contraparte] rechazó el consentimiento. Marcarlo y anotar que necesitamos al abogado externo sobre si esto activa una reclamación de indemnización bajo el contrato."

Claude actualiza la entrada relevante del rastreador, recalcula cualquier estado derivado (ej., si todos los consentimientos nivel 1 ya fueron obtenidos, marcar la obligación contractual como cumplida) y muestra qué cambió.

**Actualización por carga:** El responsable del flujo de trabajo o el abogado externo envía un documento de avance.

> Carga la actualización de avance de [abogado externo / líder de RRHH / equipo de corp dev]. Lo parsearé y actualizaré el rastreador.

Leer el documento cargado. Emparejar elementos descritos con entradas del rastreador por nombre de contraparte o descripción del elemento del plan de trabajo. Actualizar campos de estado. Marcar cualquier elemento en la actualización que no coincida con una entrada existente del rastreador — pueden ser elementos nuevos para agregar.

Después de cualquier actualización, mostrar:
```
Actualizados [N] elementos.

Cambios:
  CON-003 Salesforce: not_started → obtained
  W-014 Racionalización de entidades: in_progress → complete

Nuevas banderas:
  CON-007 [Contraparte]: refused — obligación contractual puede no estar cumplida. Considerar:
  revisión del abogado externo sobre reclamación de indemnización. ⚠️
```

---

## Modo 5: Exportar

```
/corporativo-legal-mexico:integration-management --export [--format csv|table] [--section all|consents|contracts|workplan]
```

Produce un CSV plano o tabla markdown. Predeterminado: todas las secciones, CSV.

Formato CSV — una fila por elemento, sección indicada por una columna `section`.
Las columnas varían por sección:

*Plan de trabajo:* id, phase, description, owner, workstream, priority, deadline, status, blocker

*Consentimientos:* id, counterparty, contract_type, required_consent, pa_deadline, status, assigned_to, obtained_date, notes

*Contratos:* id, name, counterparty, contract_type, annual_value, assignment_mechanism, tier, required_consent, pa_deadline, status, assigned_to, notes

La exportación es el formato compartible — apta para abogados externos, corp dev, o una actualización de integración al Consejo de Administración.

---

## Lo que este skill no hace

- No gestiona flujos de trabajo de integración de negocio (TI, RRHH, finanzas, inmuebles). Rastrea los puntos de contacto jurídicos en esos flujos y alerta cuando se necesita asesoría jurídica. La responsabilidad permanece con la función de negocio.
- No redacta las cartas de solicitud de consentimiento ni los convenios de novación — esos son producidos por el skill de consentimiento por escrito o por el abogado externo.
- No asesora sobre reclamaciones de indemnización o incumplimiento del contrato de compraventa. Cuando un consentimiento es rechazado o una fecha límite se incumple, marca la situación — el análisis jurídico de las consecuencias es decisión del abogado.
- No rastrea el desempeño de earn-outs. Los hitos y fechas de pago de earn-out aparecen en el rastreador como fechas de referencia con owner establecido como finance. El negocio maneja los números.
- No lee contratos en tiempo real durante la generación de reportes. El estado de los contratos es lo que el abogado ha actualizado en el rastreador. El skill lee el rastreador, no los contratos, al momento del reporte.


## Defensa contra inyección de fórmulas

Antes de escribir cualquier celda en salida de Excel, Sheets o CSV, neutralizar inyección de fórmulas. El texto proveniente de contrapartes (citas de contratos, nombres de partes, datos de agentes registrados, exportaciones de CLM) es controlado por un atacante. Una celda que comience con `=`, `+`, `-`, `@`, `	`, `
`, o `
` será interpretada como una fórmula o romperá la estructura de filas.

- **Prefijo con comilla simple:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (mostrado como texto, no ejecutado)
- **Aplica a toda celda que contenga texto proveniente de un documento, resultado de herramienta, o pegado del usuario.** Los encabezados de columna que tú controlas y los valores calculados que tú produces son seguros.
- **CSV: también escapar comas embebidas, comillas dobles, saltos de línea** (quoting RFC 4180).
- Esto no es opcional. Una hoja de cálculo que tu usuario abre en Excel y que dispara una macro o exfiltra datos vía DDE es un ataque a la cadena de suministro de tu usuario.
