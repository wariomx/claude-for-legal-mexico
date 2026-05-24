---
name: entity-compliance
description: >
  Rastreador de cumplimiento societario — inicializar, reportar vencimientos
  próximos, actualizar estado, ejecutar auditoría de salud, exportar a CSV.
  Mantiene un compliance-tracker.yaml construido a partir de la tabla de
  entidades, calcula fechas de vencimiento de obligaciones por entidad y
  jurisdicción, y muestra lo que vence en los próximos 30/60/90 días. Usar
  cuando el usuario dice "cumplimiento societario", "vencimientos registrales",
  "obligaciones fiscales", "asambleas anuales", "rastreador de entidades",
  "qué obligaciones vencen", "salud corporativa", "constancia de vigencia",
  "entity compliance", "filing deadlines", "annual reports due", "entity
  tracker", "what filings are due", "entity health", o "good standing".
argument-hint: "[--init | --report [--days N] | --update [--from-report] | --sweep | --audit | --export [--format csv|table]]"
---

# /entity-compliance

1. Cargar `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → `## Gestión de Entidades` (tabla de entidades, jurisdicciones, representante legal).
2. Despachar al modo correcto según la bandera:
   - Sin bandera o `--init`: Modo 1 — inicializar rastreador desde tabla de entidades
   - `--report`: Modo 2 — mostrar vencimientos próximos y elementos vencidos
   - `--update`: Modo 3a (manual) o 3b (--from-report carga) — actualizar estado
   - `--sweep`: Modo 3c — recorrer elementos desconocidos/vencidos uno por uno
   - `--audit`: Modo 4 — auditoría de salud completa
   - `--export`: Modo 5 — producir exportación CSV o tabla
3. Leer/escribir `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/entities/compliance-tracker.yaml`.
4. Después de cualquier actualización: mostrar resumen de cambios y siguiente acción.

---

## Propósito

Inscripciones en el Registro Público de Comercio, declaraciones anuales ante el
SAT, obligaciones ante el IMSS e INFONAVIT, asambleas ordinarias anuales,
informes del Comisario — cada entidad tiene su propio calendario de obligaciones
y sus propias consecuencias por incumplimiento. Este skill mantiene un único
rastreador YAML que sabe qué vence, cuándo y para qué entidad. Es ligero por
diseño: el rastreador es un archivo que tú controlas, Claude lo actualiza bajo
tu instrucción, y lo exportas cuando necesitas compartirlo.

## Importante: advertencia sobre fechas de vencimiento

> Las fechas de vencimiento de obligaciones en la tabla de referencia de este
> skill reflejan requisitos públicamente disponibles a la fecha de construcción
> del skill. Los requisitos de presentación y las fechas límite pueden cambiar.
> **Siempre confirmar las fechas con tu notario público, corredor público,
> contador, o directamente con la autoridad competente (SAT, IMSS, RPC) antes
> de confiar en ellas para fines de cumplimiento.** Si cuentas con un despacho
> corporativo externo o un área de legal ops que lleve el expediente registral
> y fiscal, su calendario de cumplimiento es autoritativo para tus entidades
> específicas — usa este rastreador para organizar y visibilizar sus datos, no
> para reemplazarlos.

## Supuesto de jurisdicción

> Este rastreador calcula fechas de vencimiento contra la jurisdicción de constitución e inscripción registrada por entidad. Las reglas de presentación, mecánicas de fechas límite y estructuras de derechos varían materialmente por jurisdicción. En México, las sociedades se constituyen bajo ley federal (LGSM), pero el Registro Público de Comercio es operado por cada entidad federativa — los derechos registrales y tiempos de inscripción pueden variar. Si la operación real de la entidad difiere de lo registrado en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` (subsidiarias internacionales no reveladas, entidades disueltas, entidades extranjeras con operaciones en México), los resultados pueden no aplicar tal como están escritos — confirmar con el notario público, corredor público, o abogado corporativo para esa jurisdicción.

## Diferenciación por tipo de entidad

> El calendario de obligaciones depende del **tipo de entidad**, no solo de la jurisdicción. Tratar una "sociedad mexicana" como un solo grupo es un error común y con consecuencias — las SA de CV, S de RL de CV y SAS tienen obligaciones diferentes, órganos de gobierno distintos y consecuencias diferentes por incumplimiento. Confirmar el tipo de entidad de la tabla de entidades antes de calcular o reportar una fecha de vencimiento, y nunca copiar una obligación de un tipo de entidad a otro.
>
> **SA de CV — Sociedad Anónima de Capital Variable:**
>
> - **Asamblea General Ordinaria anual:** Obligatoria dentro de los 4 meses siguientes al cierre del ejercicio fiscal (Art. 181 LGSM). Para ejercicios que cierran el 31 de diciembre, la fecha límite es el 30 de abril. La asamblea debe aprobar el informe del Consejo de Administración o Administrador Único, los estados financieros, y la aplicación de resultados. [verificar vigente]
> - **Comisario:** Obligatorio (Arts. 164-171 LGSM). El Comisario debe presentar su informe a la asamblea ordinaria anual. La omisión del informe del Comisario puede acarrear responsabilidad para los administradores. [verificar vigente]
> - **Declaración Anual ISR:** Persona moral — vence el 31 de marzo del año siguiente al ejercicio fiscal (Art. 76, fracción V, LISR). [verificar vigente]
> - **Inscripciones en el RPC:** Cualquier modificación estatutaria (aumento/disminución de capital, cambio de denominación, cambio de domicilio, cambio de administradores) debe protocolizarse ante notario público e inscribirse en el Registro Público de Comercio.
> - **Identidad del beneficiario controlador:** Obligación de mantener información actualizada ante el SAT (Art. 32-B Quáter CFF). [verificar vigente]
>
> **S de RL de CV — Sociedad de Responsabilidad Limitada de Capital Variable:**
>
> - **Asamblea de Socios anual:** Obligatoria, con requisitos similares a la SA. Las partes sociales no se representan por títulos de acciones.
> - **Sin Comisario obligatorio:** A menos que el contrato social lo establezca, no se requiere Comisario. El órgano de vigilancia puede sustituirse por otros mecanismos.
> - **Declaración Anual ISR:** Misma fecha límite que la SA — 31 de marzo.
> - **Modificaciones estatutarias:** Requieren protocolización ante notario e inscripción en RPC, igual que la SA.
> - **Cesión de partes sociales:** Requiere consentimiento de socios que representen la mayoría del capital social, salvo pacto distinto (Art. 65 LGSM). [verificar vigente]
>
> **SAS — Sociedad por Acciones Simplificada:**
>
> - **Constitución electrónica:** Se constituye vía el portal de la Secretaría de Economía, sin intervención de notario público. [verificar vigente]
> - **Límite de ingresos:** Si los ingresos anuales superan 5 millones de UDIs, debe transformarse en otro tipo societario. [verificar vigente — el umbral puede haber sido modificado]
> - **Accionista único permitido:** Puede tener un solo accionista.
> - **Sin Comisario obligatorio.**
> - **Declaración Anual ISR:** Misma fecha límite — 31 de marzo.
> - **Publicación de estados financieros:** Obligación de publicar en el sistema electrónico de la SE.
>
> Si la tabla de entidades registra una entidad mexicana sin tipo, marcarla como `type_unknown` y solicitar al usuario que confirme antes de calcular cualquier obligación.
>
> **Para entidades extranjeras con operaciones en México:** La inscripción como sociedad extranjera (Arts. 250-251 LGSM) ante el RPC es obligatoria para ejercer comercio habitual en México. Estas entidades están sujetas a las leyes mexicanas en lo que se refiere a sus operaciones en territorio nacional. Confirmar el régimen específico de obligaciones con el abogado corporativo.

---

## Archivo rastreador

Vive en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/entities/compliance-tracker.yaml`. Estructura:

```yaml
# Rastreador de Cumplimiento Societario
# Generado: [fecha]
# Última actualización: [fecha]
# Aviso: las fechas de vencimiento son solo de referencia — confirmar con notario público, contador, o autoridad competente

metadata:
  company: "[Nombre de la Empresa]"
  generated: "[fecha]"
  last_updated: "[fecha]"
  last_audit: "[fecha o null]"

custom_jurisdictions:   # agregados manualmente — jurisdicciones internacionales no en tabla de referencia
  []                    # se puebla cuando se encuentra una nueva jurisdicción

entities:
  - name: "[Nombre de la Entidad]"
    type: "[SA de CV / S de RL de CV / SAS / SA / SC / S en C / AC / otro]"
    state_of_formation: "[entidad federativa donde se inscribió en el RPC]"
    formation_date: "[fecha o null]"
    status: "[active / dormant / dissolving]"
    notario_publico: "[nombre del notario o corredor público de cabecera / no aplica]"
    representante_legal: "[nombre]"
    domicilio_social: "[dirección registrada]"
    notes: ""

    obligaciones:
      - type: "[Asamblea General Ordinaria / Declaración Anual ISR / Informe del Comisario / Inscripción RPC / Alta SAT / Registro IMSS / Beneficiario Controlador / otro]"
        due_date: "[AAAA-MM-DD]"
        due_basis: "[fixed date / anniversary month / statutory period / otro]"
        last_filed: "[fecha o null]"
        last_fee: "[monto o null]"
        status: "[current / due_soon / overdue / unknown]"
        authority: "[SAT / RPC / IMSS / INFONAVIT / SE / SRE / otro]"
        confirmed_compliance: "[fecha o null]"
        notes: ""

    jurisdictions_intl:
      - country: "[país]"
        registration_type: "[subsidiary / branch / representative office]"
        local_agent: "[nombre o null]"
        agent_managed: false
        filings:
          - type: "[tipo de obligación]"
            due_date: "[AAAA-MM-DD]"
            due_basis: "[fixed date / anniversary month / otro]"
            last_filed: "[fecha o null]"
            status: "[current / due_soon / overdue / unknown]"
            notes: ""
```

Valores de estado:
- `current` — cumplido para el período actual, nada vence dentro de 90 días
- `due_soon` — vence dentro de 90 días
- `overdue` — pasó la fecha de vencimiento sin fecha de cumplimiento registrada
- `unknown` — sin información; necesita confirmación manual

---

## Modo 1: Inicializar

Se ejecuta cuando no existe rastreador, o con `--rebuild` para regenerar desde cero.

### Paso 1: Cargar tabla de entidades

Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → `## Gestión de Entidades` → Tabla de entidades. Si la tabla de entidades está poblada (desde carga de organigrama en el cold-start), usarla directamente. Si no, solicitar al usuario que ejecute el módulo de cold-start o proporcione la lista de entidades.

### Paso 2: Para cada entidad, confirmar las obligaciones de cumplimiento

Para cada entidad, confirmar el calendario actual de obligaciones con el notario público, contador, o abogado corporativo. Los requisitos legales pueden cambiar (reformas fiscales, nuevas obligaciones de transparencia, cambios en umbrales). No confiar en un calendario anterior. El rastreador registra las fechas que se confirmen; actualizarlas cuando el área fiscal o el despacho externo envíe recordatorios.

Para cada entidad en la tabla:

1. Preguntar al usuario si tiene un reporte de cumplimiento actual de su despacho corporativo o contador — esa es la fuente más autoritativa.
2. Si no, preguntar qué sabe el usuario (tipo de obligación, base de fecha de vencimiento, fecha de último cumplimiento, monto típico). Registrar lo que proporcione.
3. Para cualquier cosa que el usuario no sepa, marcar la entrada como `unknown` — no poblar fechas de un calendario anterior. El siguiente paso del usuario es confirmar con su notario público, contador, o la autoridad competente.

**Obligaciones estándar por tipo de entidad (México):**

Para entidades mexicanas, generar las siguientes obligaciones según el tipo:

*Todas las sociedades mercantiles (SA de CV, S de RL de CV, SAS):*
- Declaración Anual ISR — vence 31 de marzo [authority: SAT]
- Declaraciones mensuales provisionales ISR — vencen día 17 del mes siguiente [authority: SAT]
- Declaraciones mensuales IVA — vencen día 17 del mes siguiente [authority: SAT]
- Asamblea General Ordinaria anual — dentro de 4 meses del cierre del ejercicio fiscal (Art. 181 LGSM) [authority: LGSM]
- Identidad del beneficiario controlador — mantener actualizado (Art. 32-B Quáter CFF) [authority: SAT]
- Avisos al RFC por cambios (domicilio, representante legal, socios/accionistas) [authority: SAT]

*Solo SA de CV:*
- Informe del Comisario — debe presentarse en la asamblea ordinaria anual (Arts. 164-171 LGSM) [authority: LGSM]

*Solo SAS:*
- Publicación de estados financieros en sistema electrónico de la SE [authority: SE]

*Si tiene empleados (cualquier tipo):*
- Registro patronal IMSS — alta y avisos de modificación [authority: IMSS]
- Aportaciones INFONAVIT — bimestrales [authority: INFONAVIT]
- Participación de los Trabajadores en las Utilidades (PTU) — reparto dentro de 60 días siguientes a fecha de presentación de Declaración Anual [authority: LFT/SAT]
- Declaración informativa de sueldos y salarios — anual [authority: SAT]

*Si tiene inscripciones en el RPC:*
- Avisos de modificaciones estatutarias (cambios de capital, domicilio, administradores, denominación) [authority: RPC]

**Capturar detalles en el rastreador para jurisdicciones internacionales:**

> No tengo los requisitos de presentación para [Jurisdicción] en la tabla de referencia. Déjame capturarlos para que podamos rastrear esto en adelante.
>
> Para [Entidad] en [Jurisdicción]:
> 1. ¿Qué tipo de obligación se requiere? (Reporte anual, declaración fiscal, confirmación de registro, u otra?)
> 2. ¿Cuándo vence? (Fecha fija como el 1 de mayo, mes aniversario, u otro?)
> 3. ¿Cuál es el costo típico? (Aproximado está bien — o "desconocido".)
> 4. ¿Quién es tu agente o representante local allá?

Almacenar la respuesta en un bloque `custom_jurisdictions` en el rastreador:

```yaml
custom_jurisdictions:
  - jurisdiction: "[País]"
    jurisdiction_type: "[US state / Canada province / EU member state / LatAm / otro]"
    filings:
      - type: "[tipo de obligación]"
        due_basis: "[fixed: MM-DD / anniversary month / otra descripción]"
        typical_fee: "[monto o unknown]"
        notes: "[cualquier otra información relevante — ej., agente local requerido, presentación en idioma local]"
    added_by: "manual"
    added_date: "[fecha]"
```

Esta definición personalizada se aplica entonces a todas las entidades en esa jurisdicción. Las ejecuciones futuras de `--init` y las adiciones de entidades la usarán automáticamente.

**Jurisdicciones internacionales específicamente:**

Las obligaciones internacionales varían enormemente por jurisdicción. Siempre seguir el flujo de definición personalizada arriba — confirmar el tipo de obligación, cadencia y costo con el agente local o el abogado en esa jurisdicción antes de poblar el rastreador.

Para entidades internacionales, también preguntar:
- ¿Hay un agente local o representante de oficina registrada manejando el cumplimiento? Si sí, anotar el nombre del agente — el rastreador puede alertar cuándo dar seguimiento con ellos en vez de calcular fechas de vencimiento independientemente.
- ¿La entidad está obligada a presentar reportes a nivel grupo en esa jurisdicción (ej., reporte país por país, registros de beneficiarios finales, informes de sustancia económica)?

Marcar entidades internacionales con agente local como `agent_managed: true` en el rastreador. El modo de reporte las listará por separado con una nota para confirmar estado con el agente local en vez de mostrar una fecha de vencimiento calculada.

Para obligaciones basadas en aniversario: calcular desde la formation_date en el rastreador. Si formation_date es null: establecer estado como `unknown` y marcar para confirmación.

### Paso 3: Escribir el rastreador

Generar `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/entities/compliance-tracker.yaml` con todas las entidades y sus obligaciones de cumplimiento calculadas. Establecer estado inicial:
- `current` si last_filed está dentro del período de cumplimiento actual
- `due_soon` si vence dentro de 90 días y no hay last_filed para el período actual
- `overdue` si la fecha de vencimiento pasó y no hay last_filed para el período actual
- `unknown` si formation_date falta o la jurisdicción no está en la tabla de referencia

Mostrar un resumen después de generar:

```
Rastreador de cumplimiento societario inicializado.

Entidades: [N]
Total jurisdicciones: [N]
Obligaciones rastreadas: [N]

Resumen de estado:
  ✅ Al corriente:  [N]
  ⏰ Próximo a vencer: [N] (próximos 90 días)
  🔴 Vencido:       [N]
  ❓ Desconocido:   [N] (confirmar con notario público, contador, o autoridad)

Ejecutar /corporativo-legal-mexico:entity-compliance --report para ver qué vence.
```

---

## Modo 2: Reporte

Muestra vencimientos próximos y marca elementos vencidos. Predeterminado: próximos 90 días.

```
/corporativo-legal-mexico:entity-compliance --report [--days 30|60|90|180]
```

Formato de salida:

```
REPORTE DE CUMPLIMIENTO SOCIETARIO — [fecha]
[Nombre de la Empresa]

🔴 VENCIDOS ([N]):
  [Entidad] / [Obligación] / [Autoridad] — venció [fecha]

⏰ VENCE DENTRO DE [N] DÍAS ([N]):
  [Entidad] / [Obligación] / [Autoridad] — vence [fecha]  [notario/contador responsable]
  [Entidad] / [Obligación] / [Autoridad] — vence [fecha]

✅ CUMPLIDO RECIENTEMENTE ([N] en últimos 90 días):
  [Entidad] / [Obligación] / [Autoridad] — cumplido [fecha]

❓ ESTADO DESCONOCIDO ([N]):
  [Entidad] / [Obligación] / [Autoridad] — sin información; confirmar con notario público, contador, o autoridad

🌐 GESTIONADO POR AGENTE ([N]):
  [Entidad] / [País] / [Obligación] — gestionado por [agente local]; confirmar estado directamente
  [Entidad] / [País] — sin agente local registrado; agregar uno con --update

SITUACIÓN FISCAL Y REGISTRAL:
  Última confirmación: [fecha]
  Entidades con constancia de situación fiscal vigente: [N] de [total]
  Entidades sin confirmación en últimos 12 meses: [lista]
```

Si el rastreador cubre más de ~10 entidades, o cada vez que el usuario lo pida: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Adaptar la oferta para este output — conteos por estado de cumplimiento (vencido / próximo a vencer / cumplido / desconocido), conteos por situación fiscal, y una tabla ordenable de entidades con obligación, autoridad y próxima fecha de vencimiento.

---

## Modo 3: Actualizar

Actualiza una o más entidades en el rastreador. Tres sub-modos:

### Validación de acción con consecuencias (presentar declaración / inscripción)

**Antes de dirigir o confirmar una presentación:** Leer `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si el Rol es **No abogado**:

> Presentar una declaración fiscal, inscribir una modificación estatutaria, o realizar un trámite ante una autoridad gubernamental (SAT, RPC, IMSS, IMPI) tiene consecuencias legales — es una manifestación formal de la entidad, lleva costos y derechos, y las presentaciones omitidas o incorrectas pueden causar multas, recargos, pérdida de la constancia de situación fiscal, o incluso la cancelación del RFC. ¿Has revisado esto con un abogado titulado (o con tu contador o notario público) antes de proceder? Si sí, proceder a registrar la presentación. Si no, aquí hay un resumen para llevarles:
>
> - Entidad, obligación, autoridad y fecha de vencimiento
> - Lo que dice el rastreador sobre la última presentación (fecha, monto, información de administradores reportada)
> - Preguntas abiertas (¿la información de administradores sigue vigente? ¿cambió el domicilio social? ¿hubo modificaciones estatutarias?)
> - Lo que puede salir mal (información de administradores desactualizada, vencimiento de plazo que genera multas o recargos, error en el cálculo de derechos, cancelación del RFC por incumplimiento reiterado)
> - Qué preguntar al abogado (¿realmente se necesita esta presentación este año? ¿hay modificaciones al acta constitutiva pendientes? ¿quién debe firmar? ¿se requiere protocolización ante notario?)
>
> Si necesitas encontrar un abogado: contactar a la Barra Mexicana de Abogados, el Colegio de Abogados local, o la Dirección General de Profesiones (SEP) para una referencia. Para asuntos que requieren protocolización, consultar con un notario público o corredor público competente.

No registrar una nueva fecha de `last_filed` sin un sí explícito pasando esta validación. Las lecturas del rastreador, reportes de vencimiento y salida de "qué vence pronto" no requieren la validación.

### 3a: Actualización manual

```
/corporativo-legal-mexico:entity-compliance --update
```

El abogado le dice a Claude qué se cumplió:
> "Se presentó la Declaración Anual ISR de [Entidad] el 28 de marzo. El pago fue de $45,000."

Claude actualiza:
- `last_filed` → fecha del 28 de marzo
- `last_fee` → $45,000
- `status` → `current`
- `last_updated` en metadata

### 3b: Carga de reporte del despacho o contador

```
/corporativo-legal-mexico:entity-compliance --update --from-report
```

El usuario carga un reporte de cumplimiento del despacho corporativo, contador, o notario público (PDF, CSV o Excel). Claude lo lee y actualiza las entidades coincidentes:

Del reporte, extraer para cada entidad:
- Tipo de obligación y fecha de vencimiento
- Fecha de último cumplimiento (si está presente)
- Estado de situación fiscal y fecha de confirmación
- Cualquier bandera o advertencia del despacho o contador

Emparejar entidades del reporte con entidades del rastreador por nombre (marcar coincidencias cercanas para confirmación — "Corporativo Acme SA de CV" vs. "Acme SA de CV" probablemente son la misma entidad).

Después de procesar:
```
Actualizadas [N] entidades desde el reporte.

Emparejadas: [N]
Sin emparejar (en reporte, no en rastreador): [lista — puede necesitar agregar a la tabla de entidades]
Sin reporte (en rastreador, sin actualización): [lista — estado sin cambio]
```

### 3c: Recorrido masivo de estado

```
/corporativo-legal-mexico:entity-compliance --sweep
```

Recorre cada entidad con estado `unknown` o `overdue` y solicita información actual una por una:

> [Entidad] / [Obligación] / [Autoridad] — actualmente muestra estado [status].
> ¿Se cumplió esta obligación? Si sí, ¿cuándo y cuál fue el costo?

Actualiza el rastreador después de cada confirmación. Produce un resumen de completado.

---

## Modo 4: Auditoría de salud

```
/corporativo-legal-mexico:entity-compliance --audit
```

Revisión más amplia que solo el estado de cumplimiento. Identifica:

**Cumplimiento de obligaciones:**
- Elementos vencidos (del modo de reporte)
- Elementos con estado desconocido

**Salud de la entidad:**
- Entidades marcadas como `dormant` — marcar para revisión: ¿deberían disolverse? Mantener entidades inactivas cuesta dinero (derechos registrales, honorarios de notario, obligaciones fiscales recurrentes ante el SAT) y genera obligaciones de cumplimiento continuas.
- Entidades con formation_date mayor a 5 años y estado `dormant` — marcar como candidatos a disolución y liquidación.
- Entidades sin formation_date — marcar como brecha de datos.

**Brechas en situación fiscal y registral:**
- Entidades sin fecha de `confirmed_compliance` — se desconoce si están al corriente; riesgo si una operación requiere una constancia de situación fiscal con urgencia.
- Entidades con `confirmed_compliance` mayor a 12 meses — información obsoleta; vale la pena actualizar, especialmente si se anticipa una F&A o financiamiento.

**Brechas en obligaciones como sociedad extranjera:**
- Si la empresa tiene subsidiarias internacionales o entidades extranjeras operando en México: ¿están inscritas como sociedad extranjera ante el RPC (Arts. 250-251 LGSM)? Esto requiere que el abogado confirme la operación habitual de comercio en México — Claude puede plantear la pregunta pero no puede determinar la presencia operativa de forma independiente.
- Para entidades mexicanas que operan en el extranjero: ¿cumplen con las obligaciones de registro en las jurisdicciones donde operan?

**Brechas en Comisario (solo SA de CV):**
- Entidades de tipo SA de CV sin informe del Comisario registrado para el último ejercicio — marcar como incumplimiento potencial (Arts. 164-171 LGSM).
- ¿El Comisario está vigente? ¿Se ha designado uno para el ejercicio actual?

**Brechas en convenios intercompañía:**
- De `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`: si los convenios intercompañía están marcados como parciales o no, marcar qué relaciones entre entidades probablemente necesitan convenios (servicios matriz-subsidiaria, licencias de PI, préstamos intercompañía).

**Brechas en beneficiario controlador:**
- ¿Todas las entidades tienen actualizada la información del beneficiario controlador ante el SAT (Art. 32-B Quáter CFF)?

Formato de salida:

```
AUDITORÍA DE SALUD CORPORATIVA — [fecha]

CUMPLIMIENTO DE OBLIGACIONES
  Vencidos: [N]
  Estado desconocido: [N]
  Acción: ejecutar --sweep para confirmar elementos desconocidos

ENTIDADES INACTIVAS ([N])
  [Lista de entidades inactivas con antigüedad y costo anual de mantenimiento si se conoce]
  Candidatos a disolución (>5 años inactivas): [lista]

SITUACIÓN FISCAL Y REGISTRAL
  Sin registro: [N] entidades
  Obsoleto (>12 meses): [N] entidades
  Considerar actualizar antes de: [cualquier operación próxima o renovaciones de contratos si se conocen]

COMISARIO (solo SA de CV)
  Sin informe del Comisario registrado: [N] entidades
  Comisario sin designar para ejercicio actual: [N] entidades

BENEFICIARIO CONTROLADOR
  Sin información actualizada ante SAT: [N] entidades
  Acción: actualizar información del beneficiario controlador

BRECHAS POTENCIALES
  Sociedades extranjeras: [plantear pregunta — confirmar operaciones habituales de comercio en:]
    [lista de jurisdicciones del alcance en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` donde no hay inscripción]
  Convenios intercompañía: [estado de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`]

ACCIONES RECOMENDADAS
  1. [Acción de mayor prioridad]
  2. [etc.]
```

---

## Modo 5: Exportar

```
/corporativo-legal-mexico:entity-compliance --export [--format csv|table]
```

Produce una exportación plana apta para compartir con finanzas, legal ops, o el despacho corporativo externo. Predeterminado: CSV.

Columnas CSV:
`Nombre Entidad, Tipo Entidad, Entidad Federativa de Constitución, Fecha Constitución, Estado, Notario Público, Representante Legal, Obligación, Fecha Vencimiento, Último Cumplimiento, Último Costo, Autoridad, Cumplimiento Confirmado, Notas`

Una fila por obligación. Múltiples filas por entidad (una por obligación).

Si `--format table`: producir una tabla markdown apta para pegar en un reporte o mensaje de Slack, mostrando solo los próximos 90 días de obligaciones.

---

## Lo que este skill no hace

- No presenta nada ante ninguna autoridad. El producto es un rastreador y una lista de pendientes; las presentaciones las realiza el abogado, el contador, el notario público, o el despacho externo.
- No obtiene constancias de situación fiscal ni constancias de vigencia. Rastrea cuándo se confirmaron por última vez; obtenerlas es manual o vía el despacho corporativo.
- No determina si se requiere inscripción como sociedad extranjera en una jurisdicción dada. Ese análisis depende de hechos sobre la actividad comercial habitual que el abogado debe confirmar.
- No reemplaza un despacho corporativo o un área de legal ops para empresas con estructuras multi-entidad complejas. Los despachos especializados tienen equipos dedicados de cumplimiento y relaciones directas con las autoridades. Este skill es más apto para organizaciones más pequeñas sin soporte de despacho, o como una capa ligera sobre los datos del despacho para organizaciones que sí tienen soporte.
- No protocoliza actos ante notario. Cualquier modificación estatutaria, fusión, escisión o disolución requiere intervención de notario público o corredor público — este skill rastrea los pendientes, no los ejecuta.
- La tabla de referencia de fechas de vencimiento de obligaciones no constituye asesoría legal y puede no reflejar los requisitos actuales. Confirmar todas las fechas antes de confiar en ellas.


## Defensa contra inyección de fórmulas

Antes de escribir cualquier celda en salida de Excel, Sheets o CSV, neutralizar inyección de fórmulas. El texto proveniente de contrapartes (citas de contratos, nombres de partes, datos de agentes registrados, exportaciones de CLM) es controlado por un atacante. Una celda que comience con `=`, `+`, `-`, `@`, `	`, `
`, o `
` será interpretada como una fórmula o romperá la estructura de filas.

- **Prefijo con comilla simple:** `'=SUM(A1:A10)` → `=SUM(A1:A10)` (mostrado como texto, no ejecutado)
- **Aplica a toda celda que contenga texto proveniente de un documento, resultado de herramienta, o pegado del usuario.** Los encabezados de columna que tú controlas y los valores calculados que tú produces son seguros.
- **CSV: también escapar comas embebidas, comillas dobles, saltos de línea** (quoting RFC 4180).
- Esto no es opcional. Una hoja de cálculo que tu usuario abre en Excel y que dispara una macro o exfiltra datos vía DDE es un ataque a la cadena de suministro de tu usuario.
