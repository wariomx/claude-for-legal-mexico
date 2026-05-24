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
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/portfolio.yaml`.

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
   sincronizar con el sistema de gestión de PI, o cambiar el estatus de un
   activo. Aplicar la compuerta de acción consecuencial antes de marcar
   cualquier plazo como `tramitado`.

6. **`--auditar`:** Modo 5. Revisión amplia de salud — higiene de plazos,
   brechas de registro, cuestiones de uso real, inconsistencias de titularidad,
   horizonte de expiración, marcas sin vigilancia.

7. **Si el registro está vacío y hay un sistema de gestión de PI conectado:**
   Ofrecer Modo 1 — jalar el portafolio del sistema de registro e inicializar.

8. **Recordatorio de salvaguarda:** Los plazos calculados son solo de referencia.
   Todo resultado cierra con una línea dirigiendo verificación contra
   Marcanet / MARCia / VIDOC / SIGA del IMPI, el portal de INDAUTOR, OMPI, o
   el registro relevante antes de tramitar o pagar. Un plazo registrado pero
   equivocado crea falsa confianza; no permitir que el usuario trate esto como
   el sistema de registro a menos que el sistema de gestión de PI esté
   sincronizado vía integración.

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

## Funciona mejor conectado

Este skill rastrea plazos a partir de lo que le informas. Funciona mucho mejor
conectado a:

- **Un sistema de gestión de PI (SGPI) vía MCP** — Anaqua, CPA Global, PatSnap,
  Clarivate IPfolio, Alt Legal, FoundationIP. Un SGPI conectado te da el
  expediente completo, calendarios de anualidades y correspondencia entrante en
  un solo lugar, en vez de que el registro sea lo que el abogado recuerda pegar.
  Pregunta a tu proveedor de SGPI si tienen un conector MCP, o consulta
  `CONNECTORS.md` en la raíz del repositorio para cómo solicitar uno.
- **Herramientas de práctica IMPI** (Marcanet, MARCia, VIDOC, SIGA) — estas NO
  son integraciones MCP del plugin; son herramientas web que el practicante usa
  directamente para verificar estatus, consultar expedientes y confirmar plazos.
  Cuando el skill indica "verificar contra el registro," estas son las
  herramientas donde verificas.
- **Portal de INDAUTOR** — para verificar estatus de registros de obra, reservas
  de derechos al uso exclusivo y contratos de licencia/cesión registrados.

Sin ninguno, pega tu expediente o sube una hoja de cálculo y rastrearé desde ahí.

## Propósito

Un registro de marca que no se renueva a tiempo puede ser cancelado. Una patente
sin pago de anualidad caduca. Una declaración de uso real no presentada a los
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
> nuevamente en abril 2026 `[model knowledge — verify]`. **Siempre confirmar
> plazos calculados contra Marcanet / MARCia / VIDOC / SIGA del IMPI, el portal
> de INDAUTOR, OMPI Madrid Monitor / Patentscope, o el registro nacional
> relevante antes de actuar.** Si usas Anaqua, CPA Global, Clarivate, Alt Legal
> u otro sistema de gestión de PI, su expediente es autoritativo para tus
> activos — usa este rastreador para organizar y surfear sus datos, no para
> reemplazarlos.
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
  LFPPI) — la omisión dentro de esa ventana causa caducidad automática de pleno
  derecho `[verified 2026-05-23]`. El plazo es el tercer aniversario + 3 meses de
  ventana; no exactamente "a los 3 años". Para la renovación decenal, hay un
  periodo de gracia de 6 meses con recargo.
- **Avisos comerciales (IMPI):** Vigencia de 10 años. Renovable cada 10 años.
  Mecánica similar a marcas, incluyendo declaración de uso real dentro de los
  3 meses siguientes al tercer aniversario del otorgamiento (Art. 233 LFPPI)
  `[verified 2026-05-23]`.
- **Patentes (IMPI):** Vigencia de 20 años desde la fecha de presentación de la
  solicitud (no desde otorgamiento). **Anualidades anuales** — no 3 pagos
  puntuales como en EE.UU. (3.5/7.5/11.5 años). La falta de pago de cualquier
  anualidad causa caducidad. No renovable; al vencer los 20 años el invento
  pasa a dominio público. No existe un mecanismo general de "revival" por
  caducidad involuntaria como el "unintentional lapse petition" de USPTO.
- **Modelos de utilidad (IMPI):** Vigencia de 15 años desde la fecha de
  presentación. **Anualidades anuales.** No renovable.
- **Diseños industriales (IMPI):** Vigencia de 25 años desde la fecha de
  presentación. **Pagos por quinquenios** (cada 5 años), no anualidades anuales.
  No renovable.
- **Secretos industriales:** No requieren registro ni renovación ante IMPI. La
  protección dura mientras se mantenga la confidencialidad. No se rastrean en
  este registro por plazos, pero pueden listarse para inventario.
- **Denominaciones de origen e indicaciones geográficas:** Protección indefinida
  mientras subsistan las condiciones. Se autorizan usuarios, no se "renuevan"
  en el sentido de marcas/patentes.

### México — INDAUTOR (Derechos de Autor)

- **Registro de obras:** No requiere mantenimiento. La protección patrimonial
  dura la vida del autor más 100 años (Art. 29 LFDA) `[model knowledge — verify]`.
  Los derechos morales son perpetuos, inalienables e irrenunciables (Art. 19
  LFDA). Sin plazos de renovación.
- **Reservas de derechos al uso exclusivo (INDAUTOR):** Vigencia variable según
  tipo (Arts. 173-180 LFDA) `[model knowledge — verify]`:

  | Tipo de reserva | Vigencia | Renovable |
  |---|---|---|
  | Publicaciones periódicas | 1 año | Sí, indefinidamente |
  | Difusiones periódicas | 1 año | Sí, indefinidamente |
  | Personajes ficticios | 5 años | Sí, indefinidamente |
  | Personajes humanos de caracterización | 5 años | Sí, indefinidamente |
  | Promociones publicitarias | Variable (duración de la promoción) | Según tipo |

  Las reservas son de los activos de PI con vigencia más corta. Un vencimiento
  inadvertido pierde la exclusividad del nombre/título/personaje.

### Internacional (cuando el portafolio incluye activos fuera de México)

- **Marcas Madrid (OMPI):** Vigencia de 10 años renovable en OMPI; las
  designaciones individuales pueden tener requisitos locales adicionales (ej.,
  §71 Declaration en EE.UU. para designaciones Madrid-US).
- **Marcas EUIPO:** Renovación decenal; 6 meses de gracia con recargo.
- **Patentes PCT / fase nacional:** Las anualidades dependen de cada oficina
  nacional. Confirmar por jurisdicción — la EPO tiene anualidades anuales desde
  la presentación; USPTO tiene 3 pagos puntuales.
- **Diseños industriales La Haya:** Renovación quinquenal por periodos de 5 años
  hasta el máximo permitido por cada designación.
- **Copyright US Copyright Office:** Sin mantenimiento para obras creadas 1978 o
  después.
- **Dominios:** Renovación anual o multianual según registrador; típicamente
  30 días de gracia, luego periodo de redención (~30 días con tarifa alta),
  luego liberación.

Si el portafolio incluye activos en jurisdicciones no listadas arriba, capturar
la mecánica de mantenimiento en el bloque `custom_rules` del registro y el
reporte los mostrará como `gestionado_por_agente` — confirmar estatus con el
corresponsal extranjero en vez de calcular una fecha que este skill no entiende.

---

## El registro

Vive en `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/portfolio.yaml`.
Estructura:

```yaml
# Registro de Portafolio de PI
# Generado: [fecha]
# Última actualización: [fecha]
# Advertencia: los plazos calculados son solo de referencia — confirmar con
# IMPI (Marcanet/MARCia/VIDOC/SIGA) / INDAUTOR / OMPI / registro relevante
# o el sistema de gestión de PI antes de actuar.

metadata:
  empresa: "[Razón Social]"
  generado: "[fecha]"
  ultima_actualizacion: "[fecha]"
  ultima_auditoria: "[fecha o null]"
  sistema_fuente: "[Anaqua / CPA Global / manual / ninguno]"

custom_rules:   # jurisdicciones no incluidas capturadas manualmente
  []

assets:
  - id: "MCA-MX-001"
    type: "marca"                               # marca / patente / modelo_utilidad / diseno_industrial / aviso_comercial / derecho_autor / reserva_derechos / dominio
    jurisdiction: "MX-IMPI"
    mark_or_title: "[Marca o denominación]"
    owner: "[Titular registral — razón social]"
    status: "registrada"                        # en_tramite / registrada / caducada / abandonada / cancelada / nula
    application_number: "[número o null]"
    registration_number: "[número o null]"
    classes: ["9", "42"]                        # Clasificación de Niza para marcas; CIP para patentes; null para otros
    filing_date: "[AAAA-MM-DD o null]"
    registration_date: "[AAAA-MM-DD o null]"
    grant_date: "[AAAA-MM-DD o null]"           # patentes / modelos / diseños
    priority_date: "[AAAA-MM-DD o null]"
    next_deadlines:                             # calculados; se refrescan en --reporte y --auditar
      - type: "Declaración de uso real (Art. 233 LFPPI)"
        due_date: "[AAAA-MM-DD]"
        grace_end: null                         # La declaración de uso NO tiene periodo de gracia
        basis: "3 años desde otorgamiento del registro"
        action: "Presentar declaración de uso real ante IMPI con pruebas de uso efectivo"
        status: "proximo"                       # proximo / vence_pronto / vencido / gracia / caducado / tramitado
      - type: "Renovación decenal"
        due_date: "[AAAA-MM-DD]"
        grace_end: "[AAAA-MM-DD o null]"        # 6 meses con recargo
        basis: "10 años desde otorgamiento"
        action: "Presentar solicitud de renovación ante IMPI"
        status: "proximo"
    uso_real: true                              # solo marcas/avisos — alimenta análisis de declaración de uso
    agent_managed: false                        # true para corresponsal extranjero / despacho externo gestionado
    local_agent: null
    docket_id: "[ID de sistema de gestión o null]"
    outside_counsel: "[despacho o null]"
    business_owner: "[correo o equipo]"
    notes: ""

  - id: "PAT-MX-001"
    type: "patente"
    jurisdiction: "MX-IMPI"
    mark_or_title: "[Título de la invención]"
    owner: "[Titular]"
    status: "otorgada"
    application_number: "[número]"
    registration_number: "[número de patente]"
    filing_date: "[AAAA-MM-DD]"
    grant_date: "[AAAA-MM-DD]"
    priority_date: "[AAAA-MM-DD o null]"
    expiration_date: "[AAAA-MM-DD]"             # 20 años desde fecha de solicitud
    next_deadlines:
      - type: "Anualidad [año N]"
        due_date: "[AAAA-MM-DD]"
        grace_end: "[AAAA-MM-DD o null]"
        basis: "Anualidad anual desde solicitud"
        action: "Pagar anualidad ante IMPI"
        status: "proximo"
    claims_count: 20
    entity_size: null                           # México no tiene tarifa diferenciada por tamaño de entidad como USPTO
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""

  - id: "RES-MX-001"
    type: "reserva_derechos"
    jurisdiction: "MX-INDAUTOR"
    mark_or_title: "[Título o nombre reservado]"
    owner: "[Titular]"
    status: "vigente"
    application_number: "[número o null]"
    registration_number: "[número de certificado]"
    category: "personaje_ficticio"              # publicacion_periodica / difusion_periodica / personaje_ficticio / personaje_humano / promocion_publicitaria
    filing_date: "[AAAA-MM-DD]"
    registration_date: "[AAAA-MM-DD]"
    expiration_date: "[AAAA-MM-DD]"             # 1-5 años según tipo
    next_deadlines:
      - type: "Renovación de reserva"
        due_date: "[AAAA-MM-DD]"
        grace_end: "[AAAA-MM-DD o null]"
        basis: "Vencimiento de vigencia según tipo de reserva"
        action: "Presentar solicitud de renovación ante INDAUTOR"
        status: "proximo"
    docket_id: null
    outside_counsel: null
    business_owner: null
    notes: ""
```

Valores de estatus para `next_deadlines`:
- `proximo` — más de 90 días
- `vence_pronto` — vence dentro de 90 días, no se ha tramitado
- `vencido` — pasó la fecha límite principal, dentro del periodo de gracia (si hay)
- `gracia` — en el periodo de gracia (marca explícita — conlleva recargo)
- `caducado` — pasó el periodo de gracia sin acción; activo efectivamente perdido salvo recurso
- `tramitado` — acción completada en este ciclo

---

## Modo 1: Inicializar

Se ejecuta cuando no existe registro, o con `--reconstruir`.

### Paso 1: Determinar la fuente

Leer `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`:
- **Sistema de gestión de PI conectado** (Anaqua, CPA Global, etc.): jalar el portafolio vía su integración. El sistema de PI es la fuente autoritativa; este registro lo espeja y no agrega plazos que el sistema no tenga.
- **Sin sistema de PI, pero hoja de cálculo / exportación disponible:** pedir al usuario que la comparta. Importar lo presente; marcar cualquier activo sin fecha de registro u otorgamiento como `desconocido` para cálculo de plazos.
- **Nada a la mano:** guiar los activos interactivamente — tipo, jurisdicción, número, fechas clave, titular.

### Paso 2: Para cada activo, calcular plazos

Aplicar las reglas al inicio de este archivo. Poblar `next_deadlines` con los
dos o tres plazos más próximos — plazos lejanos (renovaciones decenales décadas
en el futuro) se calculan bajo demanda durante reportes en vez de almacenarse
especulativamente.

**Atención especial a la declaración de uso real (Art. 233 LFPPI):** Para toda
marca y aviso comercial registrado ante IMPI, calcular si la declaración de uso
a los 3 años del otorgamiento ya fue presentada o si está pendiente. Si la marca
tiene más de 3 años y no hay registro de declaración de uso, marcar como
🔴 `caducado` hasta que el usuario confirme que fue presentada.

**Para activos que el skill no puede calendarizar con confianza:**
- Jurisdicción desconocida → agregar un stub bajo `custom_rules` y marcar el
  activo `agent_managed: true` con un TODO para confirmar con el corresponsal.
- Fechas faltantes necesarias para cálculo (sin fecha de otorgamiento para marca,
  sin fecha de solicitud para patente) → dejar `next_deadlines` vacío con nota
  en `notes`, y listar el activo como `desconocido` en el resumen de
  inicialización.

### Paso 3: Escribir el registro

Generar `portfolio.yaml` en la ruta de config. Mostrar resumen:

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

Plazos calculados: [N]
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

Ventana por defecto: 90 días. Refrescar plazos calculados para cada activo antes
de producir el reporte — no confiar solo en fechas almacenadas.

Resultado (anteponer encabezado de confidencialidad conforme a `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md` → Resultados):

```
REPORTE DE PLAZOS DEL PORTAFOLIO DE PI — [fecha]
[Razón social] — ventana: próximos [N] días

🔴 CADUCADOS / EN GRACIA ([N])
  [ID Activo] / [Jurisdicción] / [Tipo] / [Marca o título]
    [Acción] — fecha original [fecha], gracia termina [fecha]
    Estatus: [gracia / caducado]

⚠️ DECLARACIONES DE USO REAL PENDIENTES ([N])
  [ID Activo] / MX-IMPI / Marca / [Marca]
    Declaración de uso real (Art. 233 LFPPI) — vence [fecha]
    ⚠️ Sin periodo de gracia — omisión = caducidad automática

⏰ VENCE DENTRO DE [N] DÍAS ([N])
  [ID Activo] / [Jurisdicción] / [Tipo] / [Marca o título]
    [Acción] — vence [fecha]
    Base: [ej., "anualidad año 5 desde solicitud"]
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
- Agregar a `assets:` en `portfolio.yaml`.

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
`## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`. Si el Rol es **No abogado**:

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
correspondiente: `status: tramitado`, `fecha_tramite`, y calcular el siguiente
plazo en su ciclo de vida (para la declaración de uso, el siguiente es la
renovación decenal).

**Desde sincronización con sistema de gestión:** Si Anaqua / CPA Global / similar
está conectado, jalar el último expediente y conciliar. Señalar discrepancias
entre el registro y el sistema de gestión — el sistema de gestión prevalece;
actualizar el registro para coincidir y mostrar cualquier cosa que el registro
tenía y el sistema no.

**Cambio de estatus:** "Marca MCA-MX-004 como abandonada." Actualizar `status`,
limpiar `next_deadlines`, anotar fecha de abandono.

**Registro de cesión / cambio de titularidad:** "La marca MCA-MX-002 fue cedida
a [nuevo titular] con fecha [fecha]." Actualizar `owner`, anotar fecha de
inscripción de la cesión ante IMPI si aplica. Verificar que la cesión esté
inscrita ante el registro correspondiente — una cesión no inscrita ante IMPI es
inoponible a terceros (Art. 143 LFPPI) `[model knowledge — verify]`.

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
- ¿Hay activos sin `next_deadlines` calculados? Datos faltantes o jurisdicción
  desconocida.

**Declaraciones de uso real (Art. 233 LFPPI)**
- ¿Hay marcas con más de 3 años desde otorgamiento sin registro de declaración
  de uso? **Esta es la verificación más crítica.** Listar cada una como
  🔴 hasta que el usuario confirme que fue presentada.
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
  la marca necesita auditoría de uso antes de presentar o evaluar si procede
  solicitar prórroga por falta de uso.

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
  movimiento, multimedia) introducidos por la reforma? `[model knowledge — verify]`
- ¿Hay solicitudes provisionales de patente que requieran seguimiento bajo el
  nuevo mecanismo? `[model knowledge — verify]`

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
- **No verifica plazos contra IMPI, INDAUTOR, OMPI ni ningún otro registro.**
  Los calcula a partir de las fechas que le proporcionas. El registro es una
  copia de trabajo; el registro oficial es la fuente de verdad.
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
