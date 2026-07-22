---
name: portafolio
description: >
  Gestiona el portafolio de PI — registros, renovaciones, anualidades,
  declaraciones de uso y auditoría. Usa cuando necesites verificar qué vence,
  agregar o actualizar un activo, registrar un pago o trámite, o auditar el
  registro buscando brechas, caducidades y cuestiones de uso real. Recibe
  transferencias de trabajo de trámite y disponibilidad.
argument-hint: "[--reporte [--dias N] | --agregar | --actualizar | --auditar]"
---

# /portafolio

Muestra qué vence, agrega activos, registra trámites y audita el registro.

## Instrucciones

1. **Seguir el flujo de trabajo de abajo** y leer
   `DATA_ROOT/portfolio.json`, después de resolver con `matter_workspace.py status`.

2. **Por defecto (sin args):** equivalente a `--reporte` — mostrar plazos en los
   próximos 90 días agrupados por urgencia (🔴 caducado/gracia, ⏰ vence pronto,
   🟡 próximo, 🌐 gestionado por agente, ❓ desconocido).

3. **`--reporte [--dias N]`:** Modo 2. Cambiar la ventana con `--dias`
   (30 / 60 / 90 / 180 típico). Siempre anteponer el encabezado de
   confidencialidad conforme a CLAUDE.md → Resultados. Siempre cerrar con la
   salvedad de verificación.

4. **`--agregar`:** Modo 3. Guiar interactivamente un nuevo activo — tipo,
   jurisdicción, número, fechas, titular, responsable de negocio. Capturar una
   regla personalizada si la jurisdicción no está incluida.

5. **`--actualizar`:** Modo 4. Registrar que se realizó un trámite o pago,
   importar desde un MCP de gestión personalizado solo si su capacidad fue
   probada, o cambiar el estatus de un activo. Aplicar la compuerta antes de marcar
   cualquier plazo como `tramitado`.

6. **`--auditar`:** Modo 5. Revisión amplia de salud — higiene de plazos,
   brechas de registro, cuestiones de uso real, inconsistencias de titularidad,
   horizonte de expiración, marcas sin vigilancia.

7. **Si el registro está vacío:** ofrecer importar una exportación del usuario.
   Solo ofrecer sincronización si un MCP personalizado de SGPI aparece en
   runtime y una llamada de lectura tuvo éxito en esta ejecución.

8. **Recordatorio de salvaguarda:** Los plazos calculados son solo de referencia.
   Todo resultado cierra con una línea dirigiendo verificación contra
   Marcanet / MARCia / VIDOC / SIGA del IMPI, el portal de INDAUTOR, OMPI, o
   el registro relevante antes de tramitar o pagar. Un plazo registrado pero
   equivocado crea falsa confianza; no permitir que el usuario trate esto como
   el sistema oficial de registro, incluso si fue importado de otro sistema.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:portafolio
```

```
/propiedad-intelectual-legal-mexico:portafolio --reporte --dias 180
```

```
/propiedad-intelectual-legal-mexico:portafolio --agregar
```

```
/propiedad-intelectual-legal-mexico:portafolio --actualizar
```

```
/propiedad-intelectual-legal-mexico:portafolio --auditar
```

---

## Fuentes de datos y capacidad real

Este skill rastrea plazos a partir de datos proporcionados. Consultar
`${CLAUDE_PLUGIN_ROOT}/references/connector-capabilities.json` antes de prometer
una importación:

- **SGPI:** Anaqua, CPA Global, PatSnap, Clarivate IPfolio, Alt Legal y
  FoundationIP **no vienen conectados**. Usar exportación o MCP personalizado.
  No afirmar sincronización hasta descubrir una herramienta de lectura y
  probarla; registrar proveedor, herramienta y hora de la prueba.
- **Herramientas de práctica IMPI** (Marcanet, MARCia, VIDOC, SIGA) — estas NO
  son integraciones MCP del plugin; son herramientas web que el practicante usa
  directamente para verificar estatus, consultar expedientes y confirmar plazos.
  Cuando el skill indica "verificar contra el registro," estas son las
  herramientas donde verificas.
- **Portal de INDAUTOR** — para verificar estatus de registros de obra, reservas
  de derechos al uso exclusivo y contratos de licencia/cesión registrados.

Sin ninguno, pega tu expediente o sube una hoja de cálculo y rastrearé desde ahí.

## Propósito

Un registro de marca que no se renueva conforme a la ley puede caducar. Una patente
sin pago de anualidad puede caducar conforme al expediente y reglas aplicables. Una declaración de uso real no presentada a los
3 años del otorgamiento causa caducidad de la marca. Una reserva de derechos que
vence se pierde. Todo esto es evitable, y todo depende de una cosa: que el plazo
correcto esté en el calendario de alguien, vinculado al número de registro
correcto, en la jurisdicción correcta.

Este skill mantiene ese calendario.

## Importante: salvedad de plazos de referencia

> Las reglas de plazos que aplica este skill reflejan los requisitos públicamente
> disponibles a la fecha de construcción del skill. Los requisitos de IMPI e
> INDAUTOR, periodos de gracia, estructuras de tarifas y calendarios de
> mantenimiento cambian — la LFPPI fue reformada sustancialmente en 2020 y
> nuevamente en abril de 2026 (fuentes `MX-LFPPI-CONSOLIDATED-2026-04-03` y
> `MX-LFPPI-REFORM-2026-04-03`). **Siempre confirmar
> plazos calculados contra Marcanet / MARCia / VIDOC / SIGA del IMPI, el portal
> de INDAUTOR, OMPI Madrid Monitor / Patentscope, o el registro nacional
> relevante antes de actuar.** Si la práctica designa otro sistema como fuente
> de registro, documentar esa decisión y conciliar manualmente o mediante un MCP
> personalizado verificado; no asumir que está disponible por aparecer en el
> perfil.
>
> Un plazo registrado pero equivocado es peor que uno no registrado: crea falsa
> confianza. Los resultados de "ningún plazo próximo" especialmente merecen una
> segunda revisión antes de confiar en ellos.

## Reglas de jurisdicción y tipo

La mecánica de mantenimiento varía por jurisdicción y tipo de activo:

### México — IMPI (Propiedad Industrial)

- **Marcas (IMPI):** Vigencia de 10 años desde la fecha de otorgamiento del
  registro. Renovable cada 10 años. **Declaración de uso real obligatoria dentro
  de los 3 meses siguientes al tercer aniversario del otorgamiento** (Art. 233
  LFPPI) — la omisión dentro de esa ventana causa caducidad de pleno derecho.
  Antes de aplicar, verificar el régimen transitorio por fecha de otorgamiento
  (MX-LFPPI-MARK-USE-DECLARATION-001). Para la renovación, aplicar la ventana
  de 6 meses anteriores y 6 posteriores del art. 237
  (MX-LFPPI-MARK-RENEWAL-001).
- **Avisos comerciales (IMPI):** Vigencia de 10 años. Renovable cada 10 años.
  Mecánica similar a marcas, incluyendo declaración de uso real dentro de los
  3 meses siguientes al tercer aniversario del otorgamiento (Art. 233 LFPPI)
  (`MX-LFPPI-MARK-USE-DECLARATION-001`; comprobar transición).
- **Patentes (IMPI):** Vigencia de 20 años desde la fecha de presentación de la
  solicitud reconocida (no desde otorgamiento), sujeta al pago de anualidades
  (`MX-LFPPI-PATENT-TERM-001`). La tarifa y el expediente pueden organizar el
  pago individual o por quinquenios; no calcular aquí la fecha ni importar el
  calendario estadounidense. No renovable al terminar su vigencia legal.
- **Modelos de utilidad (IMPI):** Vigencia de 15 años desde la fecha de
  presentación y sujeto al pago de anualidades
  (`MX-LFPPI-UTILITY-MODEL-TERM-001`). Confirmar mecánica y pago en expediente
  y tarifa vigente; no renovable al terminar su vigencia legal.
- **Diseños industriales (IMPI):** Vigencia inicial de 5 años desde la fecha de
  presentación, **renovable por periodos sucesivos de 5 años hasta un máximo de
  25 años** (arts. 78-79; MX-LFPPI-DESIGN-TERM-001). No describirlo como un
  derecho único de 25 años ni como “no renovable”.
- **Secretos industriales:** No requieren registro ni renovación ante IMPI. La
  protección dura mientras se mantenga la confidencialidad. No se rastrean en
  este registro por plazos, pero pueden listarse para inventario.
- **Denominaciones de origen e indicaciones geográficas:** Protección indefinida
  mientras subsistan las condiciones. Se autorizan usuarios, no se "renuevan"
  en el sentido de marcas/patentes.

### México — INDAUTOR (Derechos de Autor)

- **Registro de obras:** No requiere mantenimiento. La regla de vida de la
  persona autora más 100 años tiene supuestos distintos para coautoría y obras
  de la fracción II (art. 29; `MX-LFDA-PATRIMONIAL-TERM-001`).
  Los derechos morales son perpetuos, inalienables e irrenunciables (Art. 19
  LFDA). Sin plazos de renovación.
- **Reservas de derechos al uso exclusivo (INDAUTOR):** seis categorías y
  vigencia conforme a los arts. 173 y 189-191 LFDA:

  | Tipo de reserva | Vigencia | Renovable |
  |---|---|---|
  | Publicaciones periódicas | 1 año | Sí, indefinidamente |
  | Difusiones periódicas | 1 año | Sí, indefinidamente |
  | Personajes humanos de caracterización, ficticios o simbólicos | 5 años | Sí, por periodos iguales |
  | Personas o grupos artísticos | 5 años | Sí, por periodos iguales |
  | Eventos artísticos y culturales | 1 año | Sí, por periodos iguales |
  | Promociones publicitarias | 5 años | No |

  Las reservas son de los activos de PI con vigencia más corta. Un vencimiento
  inadvertido puede perder la exclusividad. La ventana de solicitud va de un
  mes antes a un mes después del vencimiento; no usar la ventana marcaria de 6
  meses (MX-LFDA-RESERVA-RENEWAL-001).

### Activos fuera de México

El motor de reglas de este plugin no calcula plazos extranjeros ni de nombres
de dominio. Pueden inventariarse, pero sus `deadline_events` quedan vacíos y el
activo se marca `agent_managed: true` hasta que un agente de la jurisdicción o
el registrador aporte el evento documentado. No crear `custom_rules` locales ni
reutilizar una regla mexicana por analogía: este vigilante solo verifica IDs del
registro canónico México.

---

## El registro

Vive en `DATA_ROOT/portfolio.json` y debe ser JSON válido conforme a
`schemas/portfolio.schema.json`. No escribir comentarios ni sintaxis YAML.
Estructura:

```json
{
  "metadata": {
    "schema_version": "2.0.0",
    "empresa": "[Razón social]",
    "generado": "[AAAA-MM-DD]",
    "ultima_actualizacion": "[AAAA-MM-DD]",
    "ultima_auditoria": null,
    "sistema_fuente": "manual",
    "fuente_detalle": null,
    "fuente_verificada_en": null
  },
  "custom_rules": [],
  "assets": [
    {
      "id": "MCA-MX-001",
      "type": "marca",
      "jurisdiction": "MX-IMPI",
      "mark_or_title": "[Marca o denominación]",
      "owner": "[Titular registral]",
      "status": "registrada",
      "application_number": null,
      "registration_number": "[Número]",
      "classes": ["9", "42"],
      "filing_date": null,
      "registration_date": "[AAAA-MM-DD]",
      "deadline_events": [
        {
          "event_id": "MCA-MX-001-uso-3",
          "rule_id": "MX-LFPPI-MARK-USE-DECLARATION-001",
          "action": "Presentar declaración de uso real ante IMPI",
          "due_date": "[AAAA-MM-DD]",
          "grace_end": null,
          "status": "pending",
          "source": {
            "kind": "official_certificate",
            "reference": "[Certificado, expediente, URL o archivo]",
            "captured_at": "[AAAA-MM-DDTHH:MM:SSZ]"
          },
          "human_verified": false,
          "verified_by": null,
          "verified_against_registry_at": null,
          "calculation_trace": "[Fecha base + regla + transición/calendario revisados]"
        }
      ],
      "uso_real": null,
      "agent_managed": false,
      "docket_id": null,
      "outside_counsel": null,
      "business_owner": null,
      "notes": ""
    }
  ]
}
```

El ejemplo muestra la forma, no hechos predeterminados. Reemplazar todos los
corchetes antes de guardar. Si falta una fecha necesaria, **no crear** el
`deadline_event`: dejar `deadline_events` vacío y explicar la brecha en
`notes`. Repetir la misma estructura para `patente`, `modelo_utilidad`,
`diseno_industrial`, `aviso_comercial`, `derecho_autor`, `reserva_derechos` o
`dominio`; los eventos mexicanos deben usar el `rule_id` verificado aplicable.

Valores persistidos para `deadline_events.status`: `pending`, `pendiente`,
`scheduled`, `programado`, `tramitado`, `completed`, `paid`, `filed`, `closed`.
Urgencia (`next_30_days`, `grace`, `overdue`, etc.)
no se almacena: `renewal_watch.py` la recalcula determinísticamente desde
`--as-of`. Un evento legado `next_deadlines` se muestra como desconocido hasta
que se añadan `rule_id`, fuente, traza y verificación.

---

## Modo 1: Inicializar

Se ejecuta cuando no existe registro, o con `--reconstruir`.

### Paso 1: Determinar la fuente

Leer `PROFILE` y el registro de capacidades:
- **MCP personalizado de SGPI verificado ahora:** importar con la herramienta
  de solo lectura probada; conservar IDs y procedencia. La fuente de registro es
  la que la práctica haya designado, no automáticamente el MCP.
- **Sin sistema de PI, pero hoja de cálculo / exportación disponible:** pedir al usuario que la comparta. Importar lo presente; marcar cualquier activo sin fecha de registro u otorgamiento como `desconocido` para cálculo de plazos.
- **Nada a la mano:** guiar los activos interactivamente — tipo, jurisdicción, número, fechas clave, titular.

### Paso 2: Para cada activo, documentar eventos de plazo

Usar exclusivamente reglas vigentes de `references/verified-rules.json`.
Poblar `deadline_events` solo cuando existan: `rule_id`, fecha base documentada,
fuente, fecha de captura y `calculation_trace`. Un cálculo aritmético crea un
candidato con `human_verified: false`; solo cambia a `true` después de cotejar
el expediente/registro oficial y guardar `verified_by` y
`verified_against_registry_at`.

**Atención especial a la declaración de uso real (Art. 233 LFPPI):** Para toda
marca registrada ante IMPI, revisar fecha de otorgamiento y transición. La
ausencia de evidencia de presentación se marca `unknown/review_required`, **no
`caducado`**: no confundir falta en el registro local con falta real ante IMPI.

**Para activos que el skill no puede calendarizar con confianza:**
- Jurisdicción desconocida → agregar un stub bajo `custom_rules` y marcar el
  activo `agent_managed: true` con un TODO para confirmar con el corresponsal.
- Fechas faltantes necesarias para cálculo (sin fecha de otorgamiento para marca,
  sin fecha de solicitud para patente) → dejar `deadline_events` vacío con nota
  en `notes`, y listar el activo como `desconocido` en el resumen de
  inicialización.

### Paso 3: Escribir el registro

Generar `DATA_ROOT/portfolio.json`. Mostrar resumen:

```
Registro de portafolio inicializado.

Activos: [N]
  Marcas:             [N]   ([N registradas] / [N en trámite])
  Avisos comerciales: [N]   ([N vigentes])
  Patentes:           [N]   ([N otorgadas] / [N en trámite])
  Modelos de utilidad:[N]   ([N otorgados] / [N en trámite])
  Diseños industriales:[N]  ([N registrados] / [N en trámite])
  Derechos de autor:  [N]
  Reservas de derechos:[N]  ([N vigentes] / [N por vencer])
  Dominios:           [N]

Eventos con procedencia completa: [N]
Eventos que requieren verificación humana/registral: [N]
Gestionados por agente / jurisdicción TBC: [N] — confirmar con corresponsales
Desconocidos (datos clave faltantes): [N] — llenar antes de confiar en reportes

⚠️ Declaraciones de uso real (Art. 233): [N] marcas requieren verificación de
   estatus de declaración de uso — omisión = caducidad automática.

Ejecuta /propiedad-intelectual-legal-mexico:portafolio --reporte para ver qué vence.
```

---

## Modo 2: Reporte

```
/propiedad-intelectual-legal-mexico:portafolio --reporte [--dias 30|60|90|180]
```

Ventana por defecto: 90 días. Ejecutar el clasificador determinístico:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/renewal_watch.py" --resolve --days <N> --format markdown
```

No recalcular fechas dentro del prompt. El programa valida `rule_id`, vigencia
de regla, fuente, revisión humana y antigüedad de cotejo; clasifica respecto de
`as_of` y expone datos legados/desconocidos.

Resultado (anteponer encabezado de confidencialidad conforme a `PROFILE` → Resultados):

```
REPORTE DE PLAZOS DEL PORTAFOLIO DE PI — [fecha]
[Razón social] — ventana: próximos [N] días

🔴 VENCIDOS / EN GRACIA — CANDIDATOS ([N])
  [ID Activo] / [Jurisdicción] / [Tipo] / [Marca o título]
    [Acción] — fecha original [fecha], gracia termina [fecha]
    Estatus temporal: [gracia / vencido] | Verificación: [verified / review_required]

⚠️ DECLARACIONES DE USO REAL PENDIENTES ([N])
  [ID Activo] / MX-IMPI / Marca / [Marca]
    Declaración de uso real (Art. 233 LFPPI) — vence [fecha]
    ⚠️ Sin periodo de gracia — omisión = caducidad automática

⏰ VENCE DENTRO DE [N] DÍAS ([N])
  [ID Activo] / [Jurisdicción] / [Tipo] / [Marca o título]
    [Acción] — vence [fecha]
    Regla: [rule_id] | Fuente: [reference] | Traza: [calculation_trace]
    [Agente: despacho / expediente: id — si presente]

🟡 PRÓXIMOS (más allá de 30 días, dentro de [N] días)
  [lista]

🌐 GESTIONADO POR AGENTE ([N])
  [ID Activo] / [Jurisdicción] — gestionado por [corresponsal]; confirmar directamente
  [ID Activo] / [Jurisdicción] — sin corresponsal registrado; agregar con --actualizar

❓ DESCONOCIDO ([N])
  [ID Activo] — falta [campo]; no se puede calcular plazo
  Confirmar con [sistema de gestión / Marcanet / MARCia / INDAUTOR / registro relevante] antes de confiar en este reporte.

RESUMEN
  Total activos rastreados: [N]
  Plazos en ventana: [N]
  Última auditoría: [fecha]
```

Cerrar el reporte con la línea de salvedad: *"Calculado desde el registro de portafolio. Verificar cada plazo contra IMPI (Marcanet/MARCia/VIDOC/SIGA) / INDAUTOR / OMPI / registro relevante antes de tramitar o pagar."*

Si el reporte lista más de ~10 activos, o cuando el usuario lo pida: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Adaptar la oferta a este resultado — conteos por estatus de registro (vigente / en gracia / caducado / en trámite), una línea de tiempo de plazos, y una tabla ordenable del portafolio con jurisdicción, tipo y fecha de próxima acción.

---

## Modo 3: Agregar

```
/propiedad-intelectual-legal-mexico:portafolio --agregar
```

Agregar interactivamente un solo activo. Preguntar por:
1. Tipo (marca / patente / modelo de utilidad / diseño industrial / aviso
   comercial / derecho de autor / reserva de derechos / dominio)
2. Jurisdicción (MX-IMPI / MX-INDAUTOR / Madrid / PCT / EUIPO / USPTO /
   nacional específico)
3. Marca o denominación / título de la invención / nombre reservado
4. Titular (titular registral — importa para renovaciones y cesiones)
5. Fechas clave (según tipo: solicitud, otorgamiento, registro, prioridad,
   expiración)
6. Número(s) de expediente y registro
7. Clases / cuenta de reivindicaciones / categoría de reserva
8. Fuente — ¿se rastrea en el sistema de gestión bajo un ID de expediente?
9. Despacho externo / corresponsal, si aplica
10. Responsable de negocio (a quién le importa este activo — línea de producto,
    director de marca)

Después de captura:
- Calcular próximos plazos conforme a las reglas al inicio de este archivo.
- **Para marcas y avisos comerciales:** verificar si la declaración de uso real
  a los 3 años ya venció o está pendiente. Si el activo tiene más de 3 años
  desde otorgamiento y no se indica que fue presentada, preguntar
  explícitamente.
- Si las reglas de la jurisdicción no están incluidas, iniciar el flujo de
  captura de `custom_rules` (ver abajo).
- Agregar a `assets` en `portfolio.json`.

### Captura de reglas personalizadas

Cuando una jurisdicción no está en la lista incluida:

> No tengo las reglas de mantenimiento para [Jurisdicción] / [Tipo de activo].
> Voy a capturarlas para rastrear este activo correctamente.
>
> 1. ¿Qué eventos de mantenimiento aplican? (¿Renovación cada N años?
>    ¿Anualidades anuales? ¿Declaraciones de uso? ¿Quinquenios? ¿Algo más?)
> 2. ¿Qué detona la fecha límite — fecha de solicitud, de otorgamiento, de
>    registro, de entrada a fase nacional, aniversario de qué?
> 3. ¿Hay periodo de gracia? ¿Con qué costo?
> 4. ¿Hay un corresponsal o agente local gestionando esto?

Almacenar bajo `custom_rules:` y aplicar a futuros activos en esa jurisdicción.

---

## Modo 4: Actualizar

```
/propiedad-intelectual-legal-mexico:portafolio --actualizar
```

### Compuerta de acción consecuencial

**Antes de registrar que se realizó un trámite o pago:** Leer
`## Quién usa este plugin` en `PROFILE`. Si el Rol es **No abogado**:

> Registrar una declaración de uso real, una renovación de marca, un pago de
> anualidad de patente, una renovación de reserva de derechos, o un quinquenio
> de diseño industrial como "tramitado" tiene consecuencias. Si el registro es
> erróneo — plazo incumplido, pruebas de uso insuficientes, pago incorrecto —
> el plazo no se mueve y el activo puede caducar. ¿Has confirmado este trámite
> con el abogado o corresponsal que realmente lo presentó (o con
> Marcanet/MARCia/VIDOC del IMPI o el portal de INDAUTOR)? Si sí, proceder.
> Si no:
>
> - No registrar como tramitado todavía.
> - Esto es lo que debes llevar al abogado: ID del activo, jurisdicción, tipo
>   de plazo, qué muestra el sistema de gestión, qué crees que se presentó y
>   cuándo, y la fuente de esa creencia.
>
> Si necesitas encontrar un abogado titulado con cédula profesional
> especializado en PI: la Barra Mexicana Colegio de Abogados, AMPPI
> (Asociación Mexicana para la Protección de la Propiedad Intelectual), AIPPI
> México, o ANADE (Asociación Nacional de Abogados de Empresa) son buenos
> puntos de partida.

No marcar el estatus de un plazo como `tramitado` pasando esta compuerta sin un
sí explícito. Refrescar estatus, generar reportes y mostrar plazos próximos no
requieren la compuerta.

### Sub-modos

**Actualización manual:** "Presentamos la declaración de uso real para
MCA-MX-001 el 4 de marzo, con pruebas de uso adjuntas." Actualizar el plazo
correspondiente: `status: tramitado`, `fecha_tramite` y evidencia. Crear el
siguiente evento como candidato separado solo con regla, fecha base, fuente y
traza; no inferir que IMPI aceptó el trámite.

**Desde MCP personalizado de gestión:** Solo si la herramienta de lectura fue
descubierta y probada en esta ejecución, importar y conciliar. Mostrar
discrepancias; no sobrescribir automáticamente. Pedir confirmación y aplicar la
fuente de registro configurada por la práctica. Si no hay prueba exitosa, usar
`configured_unverified`/`unsupported` y caer a exportación manual.

**Cambio de estatus:** "Marca MCA-MX-004 como abandonada." Actualizar `status`,
cerrar (no borrar) `deadline_events` pendientes y anotar fuente/fecha de abandono.

**Registro de cesión / cambio de titularidad:** "La marca MCA-MX-002 fue cedida
a [nuevo titular] con fecha [fecha]." Actualizar `owner`, anotar fecha de
inscripción de la cesión ante IMPI si aplica. Verificar que la cesión esté
inscrita ante el registro correspondiente — para patente, registro o solicitud,
el art. 137 exige inscripción para que la transmisión o gravamen produzca
efectos en perjuicio de terceros
(MX-LFPPI-ASSIGNMENT-REGISTRATION-001).

---

## Modo 5: Auditoría

```
/propiedad-intelectual-legal-mexico:portafolio --auditar
```

Revisión amplia de salud más allá de los plazos del mes:

**Higiene de plazos**
- ¿Hay plazos en estatus `gracia` actualmente? (En curso pero con recargo.)
- ¿Hay activos `caducados` que no están marcados `abandonada` o `cancelada`?
  Evaluar si hay recurso o actualizar estatus.
- ¿Hay activos sin `deadline_events` con procedencia? Datos faltantes o jurisdicción
  desconocida.

**Declaraciones de uso real (Art. 233 LFPPI)**
- ¿Hay marcas con más de 3 años desde otorgamiento sin evidencia local de
  declaración de uso? **Esta es la verificación más crítica.** Listar como
  `review_required`; no declarar caducidad sin cotejo registral y transición.
- ¿Hay marcas próximas al plazo de 3 años (dentro de 6 meses)? Listar como
  ⏰ con recordatorio de reunir pruebas de uso real.

**Brechas de registro**
- ¿Solicitudes de marca presentadas hace más de 18 meses todavía `en_tramite`?
  Marcar para verificación de estatus ante IMPI — puede necesitar respuesta a
  requerimiento.
- ¿Solicitudes de patente presentadas hace más de 4 años todavía `en_tramite`?
  Marcar para verificación de examen.
- ¿Reservas de derechos presentadas hace más del plazo normal de resolución?
  Marcar para verificación ante INDAUTOR.

**Uso real (solo marcas)**
- ¿Se acerca la declaración de uso (Art. 233) en una marca señalada
  `uso_real: false` o incierto? La declaración requiere uso real efectivo;
  la marca necesita auditoría de uso y revisión urgente por abogado antes de
  presentar. No asumir que existe una prórroga por falta de uso.

**Higiene de titularidad**
- ¿Hay activos donde el `titular` no es una entidad activa según el registro
  (si está disponible)? Marcar — puede necesitar inscripción de cesión.
- ¿Inconsistencias de nombre de titular entre activos (misma entidad, diferentes
  cadenas de texto)? Mostrar para limpieza.
- ¿Cambios recientes de razón social sin actualización en IMPI? Las fusiones y
  transformaciones de sociedades requieren inscripción ante IMPI.

**Horizonte de expiración**
- ¿Patentes o modelos de utilidad expirando en los próximos 24 meses? Aunque
  no haya plazo de mantenimiento pendiente, el negocio puede querer saberlo —
  planeación de producto, estrategia de continuación, ventana de licenciamiento.

**Activos sin vigilancia**
- ¿Marcas registradas que no están en la lista de vigilancia en CLAUDE.md →
  Protección de marca? Marcar como brecha para que el abogado decida si agregar.

**Reforma LFPPI 2026**
- ¿Hay activos que podrían beneficiarse de los nuevos tipos de marca (posición,
  movimiento, multimedia) introducidos por la reforma?
  (`MX-LFPPI-NONTRADITIONAL-MARKS-001`)
- ¿Hay solicitudes provisionales de patente que requieran seguimiento bajo el
  nuevo mecanismo? (`MX-LFPPI-PROVISIONAL-PATENT-001`; verificar transición y
  requisitos reglamentarios)

Formato de salida:

```
AUDITORÍA DEL PORTAFOLIO DE PI — [fecha]

HIGIENE DE PLAZOS
  En gracia: [N] — actuar ahora evita caducidad
  Caducados (no marcados abandonados): [N] — confirmar estatus
  Sin cálculo de próximo plazo: [N] — llenar datos o marcar como gestionado por agente

⚠️ DECLARACIONES DE USO REAL (Art. 233 LFPPI)
  Vencidas sin confirmación de presentación: [N] — 🔴 VERIFICAR INMEDIATAMENTE
  Próximas a vencer (6 meses): [N] — ⏰ reunir pruebas de uso

BRECHAS DE REGISTRO
  Solicitudes de marca en trámite >18 meses: [lista]
  Solicitudes de patente en trámite >4 años: [lista]
  Reservas de derechos sin resolución: [lista]

USO REAL (MARCAS)
  Declaración próxima en marcas con uso incierto: [lista]

TITULARIDAD
  Activos con titular no reconocido: [N]
  Inconsistencias de nombre de titular: [lista]

HORIZONTE DE EXPIRACIÓN (24 meses)
  Patentes/modelos expirando: [lista]

VIGILANCIA DE MARCA
  Marcas registradas no vigiladas: [lista]

REFORMA LFPPI 2026
  Oportunidades de nuevos tipos de marca: [lista o ninguna]

ACCIONES RECOMENDADAS
  1. [máxima prioridad]
  2. [etc.]
```

---

## Integración: agente vigilante-renovaciones

El agente `vigilante-renovaciones` en este plugin ejecuta este skill en
calendario (semanal por defecto) y publica el reporte de Modo 2 al canal
configurado en CLAUDE.md → Alertas de renovación. Si aparecen elementos 🔴
(gracia / caducado) o ⚠️ (declaración de uso pendiente), el agente los publica
inmediatamente sin importar el calendario.

## Transferencias

- **Recibe:** nuevos registros de activos desde skills de trámite (cuando se
  presenta una solicitud o una marca se registra), desde skills de disponibilidad
  (cuando se adopta una marca y se programa la solicitud), desde inscripciones
  de cesión, y desde `/propiedad-intelectual-legal-mexico:reservas-derechos`
  (cuando se obtiene una reserva).
- **Envía:** alertas de "presentar declaración de uso ahora" / "pagar anualidad
  ahora" / "renovar reserva ahora" al abogado — este skill no presenta nada;
  informa al abogado del plazo y qué preparar.

## Lo que este skill NO hace

- **No presenta nada.** Toda acción que muestra es para que el abogado o
  corresponsal la ejecute.
- **No convierte aritmética en certeza jurídica.** Clasifica eventos documentados
  y expone su procedencia. La fecha solo aparece `verified` si una persona la
  cotejó contra el registro dentro de la ventana configurada; el registro
  oficial y expediente siguen siendo fuente de verdad.
- **No decide si renovar.** La renovación es una decisión de negocio — ¿la marca
  sigue en uso?, ¿la patente sigue siendo valiosa?, ¿la reserva sigue siendo
  relevante? Este skill muestra el plazo y el costo; el negocio y el abogado
  deciden.
- **No reemplaza un sistema de gestión de PI para portafolios de cientos de
  activos.** Anaqua, CPA Global, Clarivate, Alt Legal y sistemas similares
  tienen feeds directos de registros, automatización de plazos y servicios de
  pago de anualidades. Este skill es mejor para portafolios más pequeños, o
  como capa ligera que muestra lo que indica el sistema de registro.
- **No lee registros oficiales para verificar estatus.** Una declaración de uso
  mostrada como "tramitada" aquí significa que alguien se lo informó — no que
  IMPI la aceptó. Confirmar aceptación vía Marcanet/MARCia/VIDOC o el sistema
  de gestión de PI.
- **No calcula tarifas oficiales.** Las tarifas de IMPI e INDAUTOR se actualizan
  anualmente en el DOF. Consultar las tarifas vigentes antes de pagar.

---

## Cierre con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más información, observar y esperar, algo diferente) son un punto de partida, no una camisa de fuerza. El árbol es el resultado; el abogado elige.
