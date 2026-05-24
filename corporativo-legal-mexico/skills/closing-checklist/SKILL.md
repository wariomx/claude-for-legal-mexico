---
name: closing-checklist
description: >
  Qué falta para cerrar — mantiene el checklist de cierre con estatus, ruta
  crítica y días para el cierre. Se auto-actualiza: ingiere nuevos elementos de
  hallazgos de debida diligencia y construcción de anexos, da seguimiento al
  estatus y resalta lo que está bloqueando. Usar cuando el usuario diga
  "checklist de cierre", "qué falta para cerrar", "estatus del checklist",
  "agregar al checklist", o en un reporte programado de estatus.
argument-hint: "[opcional: ID del elemento + actualización de estatus]"
---

# /closing-checklist

1. Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/closing-checklist.yaml` y utilizar los modos descritos abajo.
2. Si se proporciona una actualización de estatus: Modo 3 (actualizar elemento).
3. En caso contrario, Modo 4: elementos bloqueantes, ruta crítica, días para el cierre.

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omitir el resto de este párrafo — las habilidades usan el contexto a nivel práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y modificaciones. Escribir las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

Las operaciones se cierran cuando el checklist está completo. Todo en la lista, hecho. Nada faltante. Esta habilidad mantiene la lista, ingiere nuevos elementos conforme surgen de la debida diligencia y le dice al equipo qué está bloqueando.

## El checklist

Ubicado en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/deals/[code]/closing-checklist.yaml`. Estructura:

```yaml
deal_code: "Proyecto Halcón"
target_close: [FECHA]
signing_date: [FECHA]
last_updated: [FECHA]

conditions_precedent:
  - id: CS-001
    item: "Resolución favorable de COFECE sobre la notificación de concentración"
    category: "Regulatory"
    responsible: "Abogados del comprador"
    due: 2026-04-15
    status: "Notificación presentada el 2026-03-01, corre el plazo de revisión"
    blocking: true
    source: "Contrato de Compraventa de Acciones §7.1(a)"

  - id: CS-002
    item: "Consentimiento de Acme Corp para cesión del contrato"
    category: "Third-party consents"
    responsible: "Target — Jane Doe"
    due: 2026-04-20
    status: "Solicitud enviada el 2026-03-10, sin respuesta"
    blocking: true
    source: "Anexo 3.12(a)(4); Acme Contrato Marco de Servicios §14.2"

closing_deliverables:
  - id: EC-001
    item: "Constancia de situación fiscal — Target (RPC)"
    category: "Corporate"
    responsible: "Abogados del target"
    due: 2026-04-28
    status: "No iniciado"
    blocking: true
    source: "Contrato de Compraventa de Acciones §2.3(b)(iv)"

  # ... etc
```

## Modos

### Modo 1: Inicializar desde el contrato de compraventa de acciones

Leer el contrato de compraventa de acciones (CCA) firmado (o en versión casi final). Extraer:

- Toda condición suspensiva (la ubicación varía según el contrato — leer los encabezados reales de cada sección)
- Todo entregable de cierre (anexo de entregables de cierre o sección correspondiente)
- Toda obligación de hacer (covenant) con fecha límite previa al cierre

Cada uno se convierte en un elemento del checklist con una cita a la sección del contrato como fuente.

**Investigar las obligaciones antes de llenar elementos regulatorios/de aprobación.** Las autorizaciones antimonopolio, de inversión extranjera y sectoriales (por ejemplo, notificación de concentración a COFECE bajo la LFCE, autorización de la Comisión Nacional de Inversiones Extranjeras bajo la Ley de Inversión Extranjera, reguladores sectoriales como CNBV, CRE o IFT) tienen mecánicas, umbrales y plazos específicos por jurisdicción que cambian. Extraer el nombre de cada condición regulatoria del CCA, luego investigar las mecánicas actualmente vigentes (quién presenta, cuándo, qué detona una revisión de segunda fase, cuál es el plazo de revisión). Citar fuentes primarias y verificar vigencia. No llenar una suposición de tiempos de memoria.

**Condiciones de cierre por efecto material adverso (EMA).** Extraer el término definido del CCA — la redacción del EMA es negociada, no estándar. Investigar la interpretación bajo la ley aplicable del lenguaje específico utilizado (la legislación mexicana no tiene jurisprudencia consolidada sobre cláusulas EMA como en jurisdicciones de common law — analizar la redacción contractual conforme a los principios generales de interpretación de contratos del Código Civil Federal y del Código de Comercio) antes de señalar un evento como posible detonante de EMA.

**La extracción de requisitos de consentimiento de contratos relevantes** depende de las reglas supletorias de la ley aplicable y del lenguaje específico de anti-cesión en cada contrato. Investigar la regla aplicable por contrato (Código Civil Federal arts. 2051-2054 para cesión de derechos; Código de Comercio para contratos mercantiles) en lugar de asumir una regla supletoria genérica.

### Modo 2: Ingerir desde debida diligencia (la parte "auto-actualizable")

El Modo 2 se activa cuando una habilidad upstream produce un hallazgo con una acción previa al cierre. Las habilidades upstream y tipos de salida que este modo ingiere:

- **Hallazgos de `diligence-issue-extraction`** — cualquier hallazgo señalado para una acción de cierre (consentimiento, resolución de asamblea de accionistas, resolución del consejo de administración, trámite regulatorio, liberación, mecánica de fideicomiso de garantía, carta de pago). No solo "consentimientos" — ver la sección de Handoffs de la habilidad de extracción para la lista completa.
- **Elementos de cambio de control / cesión de `material-contract-schedule`** — cláusulas de cambio de control, restricciones de cesión, detonantes de nación más favorecida (NMF) identificados durante la construcción del anexo.
- **Salida de `deal-team-summary`** — el resumen ejecutivo agrega hallazgos de extracción y a veces identifica un elemento de acción de cierre que una lectura mecánica de los memorandos individuales de extracción no detectaría (por ejemplo, una resolución de asamblea para aprobación de indemnizaciones por separación consolidada a través de múltiples contratos laborales, o un paquete compuesto de consentimientos). El Modo 2 lee el último deal-team-summary en la carpeta de la operación y reconcilia sus elementos de acción de cierre contra el checklist. Cualquier elemento señalado por deal-team-summary como requiriendo acción previa al cierre que no esté ya en el checklist se agrega.

El esquema de handoff cubre el rango completo de acciones previas al cierre, no solo consentimientos:

```yaml
handoff:
  # Campos obligatorios
  item: "[Contraparte o acción, una línea]"
  category: "[Third-party consents | Shareholder / board action | Regulatory filing | Release / termination | Escrow / holdback | Closing deliverable]"
  source: "[Nombre del contrato / sección legal / ruta VDR + Bates]"
  blocking: true  # a menos que el contrato tenga un calificador de materialidad
  severity: "[🔴 / 🟠 / 🟡 / 🟢 — heredado del upstream, ver regla de severity-floor en CLAUDE.md]"

  # Campos de consentimiento / acción de tercero
  counterparty: "[ej., Dunmore Holdings, S.A. de C.V.]"
  guarantor: "[ej., Se requiere garantía de la sociedad controladora del comprador, o N/A]"
  conditions: "[cualquier condición sustantiva que la contraparte haya impuesto — ej., 'se requiere garantía sustituta de la controladora del comprador antes de que el consentimiento surta efectos']"
  notice_deadline: "[ej., 30 días previos al cierre, o fecha específica]"

  # Campos de acción corporativa
  approval_body: "[Asamblea de Accionistas | Consejo de Administración | Comité | Regulador]"
  approval_threshold: "[ej., 75% de votos de accionistas en asamblea extraordinaria para aprobación de indemnizaciones]"
  statutory_or_charter_source: "[ej., LGSM Art. 182; Estatutos sociales Cláusula XX]"

  # Tiempos
  estimated_time_to_complete: "[ej., 30 días]"
  must_occur_before: "[ej., closing | signing | fin del período de espera]"
```

Preservar cada campo que la habilidad upstream haya llenado. Un "consentimiento de Dunmore requerido, con condición de garantía sustituta y aviso de 30 días" debe aparecer en el checklist con los tres elementos (consentimiento, garantía, aviso), no colapsar a "consentimiento de Dunmore para cambio de control." Cuando la habilidad upstream proporcione una severidad, mantenerla — ver la regla de cross-skill severity floor en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`.

Agregar al checklist. Deduplicar por (contraparte + tipo de acción), no por el nombre libre del elemento — un consentimiento de Dunmore y una liberación de Dunmore son elementos distintos aunque ambos nombren a Dunmore. Al deduplicar, fusionar campos en lugar de sobrescribir: si un handoff llenó `guarantor` y un handoff posterior llenó `notice_deadline`, la fila del checklist lleva ambos.

### Modo 3: Actualización de estatus

El usuario (o el agente dataroom-watcher) proporciona una actualización de estatus. Encontrar el elemento, actualizar estatus y fecha de última actualización.

```
/corporativo-legal-mexico:closing-checklist
CS-002: Acme respondió, formato de consentimiento adjunto, necesita contrafirma
```

### Modo 4: Qué está bloqueando

```markdown
[ENCABEZADO DE PRODUCTO DE TRABAJO — según configuración del plugin ## Resultados — varía por rol; ver `## Quién usa este plugin`]

> Este reporte de estatus se deriva del contrato de compraventa de acciones, hallazgos de debida diligencia y registros internos de la operación. Hereda su estatus de confidencialidad y secreto profesional — la distribución fuera del círculo de confidencialidad (contraparte, equipos de negocio más amplios) puede comprometer dicha protección. Confirmar la lista de distribución antes de enviar.

## Estatus del Checklist de Cierre — [Código de operación] — [fecha]

**Cierre previsto:** [fecha] ([N] días restantes)
**Elementos:** [N] total — [N] completados, [N] en progreso, [N] no iniciados

### 🔴 Bloqueantes y en riesgo

| ID | Elemento | Vencimiento | Estatus | Días restantes |
|---|---|---|---|---|
| [CS-XXX] | [elemento] | [fecha] | [estatus] | **[N]** |

### 🟡 Bloqueantes, en tiempo

[misma tabla]

### ✅ Completados

[N] elementos — [lista colapsada]

### No bloqueantes (post-cierre, informativos)

[N] elementos

---

**Ruta crítica:** [El o los elementos que, si se retrasan, empujan la fecha de cierre]
```

## Análisis de ruta crítica

No todos los elementos bloqueantes son iguales. Un consentimiento que tarda 30 días en obtenerse está en la ruta crítica. Una constancia de situación fiscal que tarda 2 días no lo está, aunque ambos sean bloqueantes.

Para cada elemento bloqueante, estimar el tiempo para completar. Los elementos donde `(fecha de vencimiento - hoy) < tiempo estimado` están en riesgo. Esos van al inicio de cada reporte de estatus.

Si el checklist tiene más de ~10 elementos, o en cualquier momento que el usuario lo solicite: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Adaptar la oferta para esta salida — conteos por estatus (completado / en progreso / no iniciado / en riesgo), una vista de ruta crítica agrupada por área de trabajo, y una tabla ordenable con elemento, responsable, fecha de vencimiento y días restantes.

## Integración: agente dataroom-watcher

El agente revisa el checklist diariamente, obtiene cualquier actualización de estatus de correo/Slack si están conectados, y publica el reporte de "qué está bloqueando" en el canal del equipo de la operación. El Modo 4 es la salida del agente.

## Puerta de acción consecuente (certificar cierre)

**Antes de producir una certificación de "listo para cerrar / todas las condiciones suspensivas cumplidas" o un memorándum de cierre:** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si el Rol es **No abogado**:

> Certificar que las condiciones de cierre han sido cumplidas (o producir un memorándum de cierre que lo afirme) tiene consecuencias legales — es la señal que detona el flujo de fondos y las obligaciones post-cierre. ¿Has revisado esto con un abogado? Si sí, proceder. Si no, aquí hay un resumen para llevarle:
>
> - La lista completa de condiciones suspensivas con estatus (qué está hecho, qué está en progreso, qué no se ha iniciado)
> - Cualquier elemento donde la evidencia de cumplimiento sea débil o falte
> - Cualquier dispensa (waiver) o carta complementaria necesaria para elementos que no se completarán a tiempo
> - Preguntas abiertas (consentimientos de contrapartes pendientes, cualquier riesgo de EMA/bring-down)
> - Qué preguntar al abogado (¿está esto listo para declarar cerrado?; ¿se está pasando por alto alguna condición que no debería?; ¿qué necesita ir en un anexo de excepciones?)
>
> Si necesitas encontrar un abogado titulado: contacta a la Barra Mexicana de Abogados, el Colegio de Abogados de tu localidad, o la Dirección General de Profesiones (SEP) para referencia de profesionistas.

No producir una certificación final de "listo para cerrar" sin un sí explícito después de esta puerta. El seguimiento de estatus y los reportes de "qué está bloqueando" no requieren la puerta.

---

## Lo que esta habilidad no hace

- No obtiene consentimientos, presenta trámites ni redacta documentos. Da seguimiento a que necesitan ocurrir.
- No decide qué está bloqueando — el contrato de compraventa de acciones decide eso. Esta habilidad lee el contrato.
- No cierra la operación. Te dice cuándo puedes hacerlo.
