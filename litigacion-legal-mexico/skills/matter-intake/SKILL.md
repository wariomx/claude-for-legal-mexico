---
name: matter-intake
description: Ingreso de un nuevo asunto — preguntas uniformes que cubren identificación, conflictos de interés, origen, triaje de riesgo, materialidad, despacho externo, responsables internos, retención legal y fechas clave; escribe matter.md y history.md y agrega una fila estructurada a _log.yaml. Usar cuando el usuario dice "nuevo asunto", "ingresar este asunto", o quiere incorporar un nuevo asunto al portafolio.
argument-hint: "[nombre opcional del asunto]"
---

# /matter-intake

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → calibración de riesgo (para triaje), panorama (para contexto, método de conflictos), partes interesadas (para saber a quién involucrar).
2. Seguir el flujo de trabajo y la referencia que se describen abajo.
3. Ejecutar el ingreso uniforme: identificación, verificación de conflictos, origen, triaje de riesgo, materialidad, despacho externo, responsables internos, retención legal, fechas clave, postura inicial.
4. Generar slug a partir del nombre del asunto (minúsculas, guiones, año).
5. Crear `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md` — ingreso narrativo completo.
6. Crear `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md` — inicializado con el ingreso como primera entrada.
7. Agregar fila estructurada a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`.
8. Confirmar con el usuario: "Esta es la fila que escribiré — ¿algún cambio?"

---

# Ingreso de asunto

## Propósito

Todo nuevo asunto pasa por el mismo ingreso para que el portafolio sea comparable. Las filas uniformes en `_log.yaml` permiten que el skill de estatus consolide. La narrativa en `matter.md` captura lo que la fila no puede. El archivo de historial inicializado aquí se convierte en el registro de eventos.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` — calibración de riesgo (umbrales de triaje, materialidad, escalera de convenio), panorama (partes interesadas, banco de despachos externos).
- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` — para confirmar unicidad del slug.

## El ingreso

### 1. Identificación

- Nombre del asunto (como se referencia comúnmente, ej., "Acme c. Nosotros 2026")
- Contraparte
- Tipo de asunto: `mercantil | laboral | pi | regulatorio | investigacion | administrativo | amparo | otro`
- Nuestro rol: `actor | demandado | reclamante | enjuiciado | investigado`
  - Si el `## Lado` del perfil de práctica es `actor`, `defensa`, o una variante "ambos — por defecto X", pre-llenar el rol desde ese valor por defecto y confirmar. Si `## Lado` es `varía por asunto`, preguntar directamente. Nunca asumir silenciosamente una postura que el perfil de práctica no haya establecido.
  - El rol impulsa los skills aguas abajo: asuntos con postura de actor dirigen el triaje de riesgo al valor del caso / económica de contingencia; asuntos con postura de defensa dirigen a exposición / provisiones / cobertura de seguro.
- Jurisdicción (juzgado, foro arbitral o autoridad regulatoria)

### 2. Verificación de conflictos de interés

Antes de continuar, ejecutar el paso de conflictos conforme a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → Verificación de conflictos.

- **Estado:** `cleared | pending | not-run | waived`
- **Método:** coincidir con lo que declara `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` (`corporate-legal | outside-counsel | system-check | informal | other`). Si el método declarado es `informal`, decirlo — el registro aún captura que una verificación basada en el criterio del abogado fue la base.
- **Liberado por:** nombre / equipo / despacho
- **Fecha de liberación:** AAAA-MM-DD
- **Verificado contra:** lista breve de los nombres/entidades específicos verificados (contraparte, afiliados conocidos, abogados adversos si se conocen, testigos clave). Poco está bien; "no" no lo está.
- **Notas:** cualquier cosa señalada pero liberada (ej., "García en nuestro Consejo fue consejero independiente de la contraparte 2019–2021 — liberado por no superposición con este asunto").

Comportamiento por estado:

- `cleared` → proceder.
- `pending` → proceder con el ingreso; señalar prominentemente en `matter.md` y en la fila del log que los conflictos están pendientes; mostrar de nuevo en cada `/litigacion-legal-mexico:matter-update` y en `/litigacion-legal-mexico:portfolio-status` hasta que se resuelva.
- `waived` → raro; requiere una justificación de dispensa de conflicto (redactar la dispensa está fuera de este skill — capturar que existe una, quién la firmó y dónde se encuentra).
- `not-run` → **DETENER. Este es un filtro obligatorio.** El skill no creará `matter.md`, `history.md`, ni una entrada en `_log.yaml` hasta que la postura de conflictos esté resuelta. Tres caminos aceptables:

  **Camino 1 — Ejecutar conflictos ahora.** Pausar este ingreso. Verificar conforme a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` Verificación de conflictos. Regresar con `status: cleared` o `status: waived` con justificación.

  **Camino 2 — Marcar como pendiente con responsable + fecha límite.** Permitido solo cuando `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` Verificación de conflictos declara que el ingreso en paralelo es aceptable. Capturar: quién está ejecutando los conflictos, cuándo se espera que regresen, qué entidades están verificando. El ingreso procede; la fila del asunto lleva `conflicts.status: pending`; `/litigacion-legal-mexico:portfolio-status` lo señala en cada ejecución; `/litigacion-legal-mexico:matter-update` vuelve a preguntar hasta que se resuelva.

  **Camino 3 — Bypass con justificación documentada.** Solo si el usuario reconoce explícitamente el bypass. Registrar en `conflicts.override`:

  ```yaml
  conflicts:
    status: not-run               # preservado tal cual
    override:
      by: [nombre del usuario]
      date: [AAAA-MM-DD]
      rationale: [por qué se omitió la verificación de conflictos — registro permanente; no expira automáticamente]
  ```

  Este campo es visible en cada `/litigacion-legal-mexico:portfolio-status`, cada `/litigacion-legal-mexico:matter-briefing`, y cada `/litigacion-legal-mexico:matter-update` hasta que se elimine. Nunca es eliminado por el skill — solo por edición explícita del usuario a `_log.yaml` después de que los conflictos se verifiquen efectivamente.

  **No proceder silenciosamente.** "Lo haré después" no es una respuesta aceptable. Uno de los Caminos 1/2/3 debe elegirse, y la elección se captura en el registro.

Este paso no se trata de que el skill decida si existe un conflicto — ese es el criterio del usuario/despacho. Se trata de asegurar que la verificación se realizó y el registro lo refleja.

### 3. Origen

¿Cómo llegó este asunto?
- `carta-requerimiento | demanda-notificada | requerimiento-judicial | consulta-regulatoria | reporte-interno | amenaza-previa`
- *Oportunidad de documento semilla:* "Si tienes el documento iniciador (demanda, requerimiento, oficio), adjúntalo o comparte la ruta. Afinará el ingreso."

### 4. Triaje de riesgo — contra la calibración de la casa

- Severidad: alta | media | baja (referencia las bandas de severidad de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`)
- Probabilidad: alta | media | baja (referencia las bandas de probabilidad de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`)
- Calificación de riesgo resultante (según la matriz): alta | media | baja | crítica
- Rango de exposición por daños (mejor estimación)
- Exposición no monetaria (¿medida cautelar? ¿convenio regulatorio? ¿publicidad? ¿precedente?)

Si la calibración de riesgo en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` es escasa, no fabricar precisión. Usar la intuición del usuario y anotar la escasez.

### 5. Materialidad

Contra los umbrales de la casa en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`:
- `provisionado | revelado | monitoreado | ninguno`
- Si `provisionado`: monto de la provisión y si finanzas ha sido notificado
- Si `revelado`: ubicación de la presentación y nota al pie

### 6. Despacho externo

- Despacho
- Socio líder
- **Correo del socio líder** (usado por `/litigacion-legal-mexico:oc-status` para redactar solicitudes de estatus)
- Estado de la carta compromiso: `signed | pending | none`
- Autorización de presupuesto: monto y aprobador
- *Oportunidad de documento semilla:* "Ruta de la carta compromiso, si está firmada."

Si el riesgo es medio o mayor y no hay despacho externo asignado — señalarlo.

### 7. Responsables internos

Desde `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` panorama — ¿qué partes interesadas internas están involucradas?
- Líder de negocio
- Contacto de RH (si es laboral)
- Contacto de comunicación (si hay riesgo reputacional)
- CISO (si involucra datos o ciberseguridad)
- Otro

### 8. Retención legal

- ¿Emitida? Si sí: fecha, alcance, custodios (lista de nombres).
- Próxima fecha de renovación (por defecto: seis meses desde la emisión; ajustar por asunto).
- Si no y se trata de litigio activo o razonablemente anticipado: señalar urgentemente; ofrecer ejecutar `/litigacion-legal-mexico:legal-hold [slug] --issue` después de que el ingreso se complete.
- *Oportunidad de documento semilla:* "Aviso de retención, si fue emitido."

### 9. Fechas clave

- Plazo de respuesta (contestación de demanda, objeción, oposición)
- Próxima audiencia / conferencia
- Plazo de prescripción (si aplica)
- Plazos regulatorios

### 10. Postura inicial

Un párrafo de teoría:
- ¿Cuál es nuestra versión?
- ¿Cuál es la de ellos?
- ¿Cuál es el hecho decisivo?
- Postura inicial: `litigar | convenir | investigar | esperar`

## Escritura de los resultados

### Slug

Minúsculas, guiones, año al final. Ejemplos: `acme-c-nosotros-2026`, `laboral-garcia-2026`, `cofece-investigacion-2026`.

Confirmar que el slug sea único en `_log.yaml` antes de escribir.

### `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/matter.md`

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según config del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

# [Nombre del asunto]

**Slug:** [slug]
**Abierto:** [AAAA-MM-DD]
**Nuestro rol:** [actor/demandado/etc.]
**Estado:** [estado]

---

## Identificación

[contraparte, jurisdicción, tipo de asunto, origen]

## Conflictos de interés

**Estado:** [cleared / pending / not-run / waived]
**Método:** [corporate-legal / outside-counsel / system-check / informal / other]
**Liberado por:** [nombre]
**Fecha de liberación:** [AAAA-MM-DD]
**Verificado contra:** [entidades verificadas]
**Notas:** [señalamientos liberados, referencia de dispensa si aplica]

## Triaje de riesgo

**Severidad:** [banda] — [por qué, con referencia a las definiciones de severidad de la casa]
**Probabilidad:** [banda] — [por qué]
**Calificación de riesgo:** [alta/media/baja/crítica]
**Exposición:** [rango en pesos + no monetaria]

## Materialidad

[provisionado/revelado/monitoreado/ninguno — con monto de provisión, ubicación de revelación, o razonamiento si "ninguno"]

## Despacho externo

[despacho, líder, estado de carta compromiso, presupuesto]

## Responsables internos

[partes interesadas y por qué cada una está involucrada]

## Retención legal

[estado, fecha, alcance]

## Fechas clave

[lista]

## Teoría inicial

[un párrafo: nuestra versión, su versión, hecho decisivo, postura inicial] `[SME VERIFY — la teoría al ingreso es una hipótesis de trabajo; confirmar con despacho externo antes de cualquier escrito o comunicación material que asuma este encuadre]`

## Preguntas abiertas

[cualquier cosa aún no conocida que importe — ej., "cobertura de seguro pendiente de confirmar", "no está claro si tenemos póliza para X"]

---

## Documentos semilla

| Documento | Ruta / referencia |
|---|---|
| [ej., demanda] | [ruta o "aún no compartido"] |
```

### `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/[slug]/history.md`

Inicializar el archivo de historial con el ingreso como entrada cero:

```markdown
# Historial: [Nombre del asunto]

Registro de eventos de solo agregar. El más reciente arriba.

---

## [AAAA-MM-DD] — Asunto abierto

[Origen, quién lo trajo, resumen del triaje inicial, despacho externo asignado, retención legal emitida sí/no.]
```

### Agregar a `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml`

Agregar una fila según el esquema. Ejemplo:

```yaml
- id: acme-c-nosotros-2026
  name: "Acme Corp c. La Empresa"
  type: mercantil
  role: demandado
  counterparty: "Acme Corp"
  jurisdiction: "Juzgado 3° Civil, CDMX"
  # status se deriva de source:
  #   source: amenaza-previa | carta-requerimiento        → status: amenazado
  #   source: demanda-notificada | requerimiento-judicial | consulta-regulatoria → status: activo
  #   source: reporte-interno                              → status: amenazado (default) o activo si un proceso formal ha iniciado
  status: activo
  stage: etapa de demanda/contestación
  source: demanda-notificada
  outside_counsel:
    firm: "Basham, Ringe y Correa"
    lead: "J. Reyes"
    email: "jreyes@basham.example.com"
    engagement: signed
  conflicts:
    status: cleared
    method: corporate-legal
    cleared_by: "K. Patel"
    cleared_date: 2026-04-20
    override:                   # se llena solo en bypass de Camino 3
      by: null
      date: null
      rationale: null
  risk: alta
  materiality: provisionado
  exposure_range: "$2M–$5M MXN"
  internal_owners:
    business_lead: "Ana López"
    hr_partner: null
    comms_contact: null
  legal_hold:
    issued: true
    issued_date: 2026-02-15
    scope: "Dirección comercial 2023–2026"
    custodians: ["Ana López", "R. Chen", "T. Patel"]
    last_refresh: 2026-02-15
    next_refresh: 2026-08-15
    released: null
  related_matters: []
  opened: 2026-04-20
  next_deadline: 2026-05-15
  last_updated: 2026-04-20
  path: matters/acme-c-nosotros-2026/
```

## Confirmar antes de escribir

Mostrar al usuario la fila y el contenido de matter.md:

> Esto es lo que escribiré. Señala cualquier cosa incorrecta o insuficiente antes de que lo registre.

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, observar y esperar, algo diferente) son un punto de partida, no una restricción. El árbol es el resultado; el abogado elige.

## Lo que este skill no hace

- **Ejecutar la verificación de conflictos por sí mismo.** Registra el resultado, el estado, el método, y las entidades verificadas. La verificación real ocurre en cualquier sistema (o criterio) que declare el perfil de práctica de la casa. Si el usuario dice "liberado," el skill lo toma a valor nominal y captura los metadatos.
- Decidir la teoría inicial. Captura lo que dice el usuario; no inventa una.
- Emitir la retención legal. La señala si falta. El usuario la emite.
