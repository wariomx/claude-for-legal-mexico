---
name: reservas-derechos
description: >
  Reservas de derechos al uso exclusivo ante INDAUTOR — búsqueda de
  disponibilidad, clasificación de categoría, preparación y presentación de
  solicitud, seguimiento de vigencia y renovación. Régimen exclusivamente
  mexicano sin equivalente en derecho estadounidense (LFDA Arts. 173-180).
argument-hint: "[nombre a reservar] [--buscar | --solicitar | --renovar | --revisar]"
---

# /reservas-derechos

Las reservas de derechos al uso exclusivo son un régimen de protección
**exclusivamente mexicano** administrado por INDAUTOR (Instituto Nacional del
Derecho de Autor), regulado por la LFDA Arts. 173-180 y su Reglamento
`[model knowledge — verify]`. No existe equivalente en el derecho
estadounidense ni en la mayoría de las jurisdicciones.

Este régimen protege nombres, títulos y denominaciones que no son susceptibles
de registro de marca ante IMPI pero que requieren protección contra el uso por
terceros.

## Instrucciones

1. **Cargar
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.**
   Si contiene `[PLACEHOLDER]`, detenerse y dirigir a
   `/propiedad-intelectual-legal-mexico:cold-start-interview`.

2. **Despachar según `$ARGUMENTS`:**
   - `--buscar` → ejecutar modo de búsqueda de disponibilidad
   - `--solicitar` → ejecutar modo de preparación de solicitud
   - `--renovar` → ejecutar modo de renovación
   - `--revisar` → ejecutar modo de revisión de cartera de reservas
   - Sin flag → preguntar: "¿Necesitas buscar disponibilidad, preparar una
     solicitud, renovar una reserva existente, o revisar tu cartera de
     reservas?"

3. **Seguir el flujo de trabajo del modo seleccionado abajo.**

4. **Coordinación IMPI.** Una reserva de derechos puede entrar en conflicto con
   una marca registrada — y viceversa. Siempre señalar la necesidad de una
   búsqueda paralela ante IMPI cuando el nombre también podría ser susceptible
   de registro de marca.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:reservas-derechos --buscar "La Gaceta del Jurista"
/propiedad-intelectual-legal-mexico:reservas-derechos --solicitar
/propiedad-intelectual-legal-mexico:reservas-derechos --renovar
/propiedad-intelectual-legal-mexico:reservas-derechos --revisar
/propiedad-intelectual-legal-mexico:reservas-derechos "El Capitán Águila"
```

(Si se da un nombre sin flag, el skill preguntará qué modo.)

---

## Contexto legal

### ¿Qué es una reserva de derechos al uso exclusivo?

Es el derecho a usar y explotar de forma exclusiva títulos, nombres y
denominaciones en las categorías que establece la ley. Se tramita ante INDAUTOR
(no ante IMPI). Es independiente del registro de marca — un titular puede
tener ambos, o solo uno, sobre el mismo nombre `[model knowledge — verify]`.

### Categorías (LFDA Art. 173)

La LFDA establece cinco categorías de reserva (Art. 173 LFDA) `[verified 2026-05-23]`:

| Frac. | Categoría (Art. 173 LFDA) | Descripción | Vigencia (Art. 174) | ¿Renovable? |
|---|---|---|---|---|
| I | Títulos de publicaciones periódicas | Revistas, periódicos, boletines, gacetas y cualquier publicación periódica | 1 año | Sí, por periodos iguales |
| II | Difusiones periódicas | Programas de radio, televisión y cualquier difusión periódica | 1 año | Sí, por periodos iguales |
| III | Personajes humanos de caracterización, o ficticios o simbólicos | Personajes de ficción, simbólicos (representativos de marca/empresa/concepto) y personas físicas cuando adoptan una caracterización para uso comercial | 5 años | Sí, por periodos iguales |
| IV | Personas o grupos dedicados a actividades artísticas | Nombres de artistas, intérpretes, ejecutantes, conjuntos musicales, grupos de teatro, danza, circo u otras actividades artísticas | 5 años | Sí, por periodos iguales |
| V | Denominaciones de promociones publicitarias | Nombres de promociones comerciales: ofertas, sorteos, concursos, rifas | Vigencia de la promoción; máximo 1 año | No renovable |

> ⚠️ **La renovación se solicita dentro del mes anterior al vencimiento o hasta un mes después** (con recargo). El margen de maniobra no es de 6 meses. `[verified 2026-05-23]`

### Diferencia con el registro de marca (IMPI)

| Aspecto | Reserva de derechos (INDAUTOR) | Registro de marca (IMPI) |
|---|---|---|
| Autoridad | INDAUTOR | IMPI |
| Marco legal | LFDA Arts. 173-180 | LFPPI |
| Objeto | Títulos, nombres, denominaciones en 5 categorías | Signos distintivos para productos/servicios |
| Vigencia | 1-5 años según categoría | 10 años renovables |
| Alcance | Categoría específica | Clases de productos/servicios (NIZA) |
| Coexistencia | Puede coexistir con marca | Puede coexistir con reserva |
| Conflicto | Puede ser negada por conflicto con marca | Puede ser negada por conflicto con reserva |

### Reglas clave

- **Uso obligatorio** — la reserva debe ser utilizada. El no uso puede
  resultar en la pérdida del derecho al no renovar o en una acción de
  tercero. LFDA establece consecuencias por falta de uso
  `[model knowledge — verify]`
- **No conflicto con marcas registradas** — INDAUTOR puede negar una reserva
  si el nombre entra en conflicto con una marca registrada ante IMPI. La
  coordinación IMPI-INDAUTOR es necesaria.
- **No conflicto con reservas previas** — la misma categoría o categoría
  confundible
- **Requisitos formales** — la solicitud debe contener información específica
  según la categoría
- **Transmisión** — las reservas de derechos son transmisibles. La
  transmisión debe registrarse ante INDAUTOR `[model knowledge — verify]`

---

## Contexto del asunto

Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de
práctica. Si `Habilitado` es `✗`, omitir. Si está habilitado y no hay asunto
activo, preguntar. Escribir resultados en la carpeta del asunto en
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<asunto-slug>/`.

---

## Modo búsqueda (`--buscar`)

### Propósito

Evaluar la disponibilidad de un nombre, título o denominación para reserva de
derechos antes de presentar la solicitud. Una búsqueda previa reduce el riesgo
de rechazo y los costos de re-trámite.

### Flujo de trabajo

#### Paso 1: Clasificar la categoría

> ¿Qué quieres reservar?
>
> 1. **Título de publicación periódica** — revista, periódico, boletín,
>    gaceta, newsletter
> 2. **Nombre de personaje ficticio o simbólico** — personaje de ficción,
>    mascota, personaje representativo
> 3. **Nombre de persona física (uso comercial)** — nombre propio para
>    explotación comercial
> 4. **Nombre de grupo artístico** — banda, grupo musical, compañía de
>    teatro/danza
> 5. **Denominación de promoción publicitaria** — nombre de oferta, sorteo,
>    concurso, rifa

Si el usuario no está seguro de la categoría, ayudar a clasificar con base
en el uso pretendido.

#### Paso 2: Búsqueda en base de datos INDAUTOR

> Para la búsqueda de disponibilidad, necesito:
>
> - **Nombre exacto propuesto** — tal como se quiere reservar
> - **Variantes** — ¿hay variantes del nombre que también quieras verificar?
> - **Categoría** — confirmada en el Paso 1

**Búsqueda recomendada:**
1. Consulta en el sistema de INDAUTOR (si hay integración disponible)
   `[INDAUTOR]`
2. Búsqueda fonética y conceptual de nombres similares en la misma categoría
3. **Búsqueda paralela ante IMPI** — verificar si existe marca registrada
   confundible en clases relevantes

> **⚠️ Coordinación IMPI obligatoria.** Siempre recomendar una búsqueda
> paralela de marca ante IMPI. Un nombre disponible para reserva ante
> INDAUTOR puede tener una marca confundible registrada ante IMPI — y INDAUTOR
> puede negar la reserva por ese conflicto. Y viceversa: una reserva existente
> puede ser obstáculo para un registro de marca posterior.

#### Paso 3: Resultado de búsqueda

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Reporte de Búsqueda — Reserva de Derechos al Uso Exclusivo

**Fecha:** [AAAA-MM-DD]
**Nombre buscado:** [nombre]
**Categoría:** [I-V]

## Resultados en INDAUTOR

| Nombre encontrado | Categoría | Titular | Vigencia | Estatus |
|---|---|---|---|---|
| [nombre similar o idéntico] | [cat.] | [titular] | [fecha] | [vigente/vencida] |

## Resultados en IMPI (marcas confundibles)

| Marca | Clase(s) NIZA | Titular | Registro | Estatus |
|---|---|---|---|---|
| [marca similar] | [clase] | [titular] | [número] | [vigente/vencida] |

## Evaluación de disponibilidad

**Disponibilidad estimada:** [Alta / Media / Baja / No disponible]

**Riesgos identificados:**
- [Reserva confundible existente — riesgo de rechazo]
- [Marca confundible registrada ante IMPI — riesgo de oposición]
- [Nombre genérico o descriptivo — riesgo de rechazo por falta de
  distintividad]

**Recomendación:** [Proceder con solicitud / Modificar el nombre / No
proceder] `[review]`

## Verificación de citas

[Etiquetas de fuente para cada resultado: `[INDAUTOR]`, `[IMPI]`,
`[model knowledge — verify]`, `[user provided]`]
```

Escribir resultado a
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/outputs/reserva-busqueda-<slug>-AAAA-MM-DD.md`
(o en carpeta del asunto si aplica).

---

## Modo solicitud (`--solicitar`)

### Propósito

Preparar y documentar una solicitud de reserva de derechos al uso exclusivo
ante INDAUTOR.

### Flujo de trabajo

#### Paso 1: Confirmar categoría y búsqueda previa

- ¿Se hizo búsqueda de disponibilidad? Si no, recomendar ejecutar `--buscar`
  primero.
- Confirmar categoría (I-V).
- Confirmar que no hay conflictos identificados que impidan la solicitud.

#### Paso 2: Recopilar información según categoría

**Para TODAS las categorías:**
- Nombre/título/denominación exacto a reservar
- Datos del solicitante (persona física o moral): nombre, domicilio,
  nacionalidad, RFC (si aplica)
- Datos del representante legal (si aplica): nombre, datos del poder
- Categoría seleccionada

**Información adicional por categoría:**

| Categoría | Información específica requerida |
|---|---|
| I — Publicación periódica | Género de la publicación (informativo, cultural, científico, etc.), periodicidad (diaria, semanal, mensual, etc.), idioma, editor responsable |
| II — Personaje ficticio/simbólico | Descripción del personaje, características físicas y psicológicas, contexto de uso (serie, película, publicidad, etc.), si es ficticio o simbólico |
| III — Persona física | Nombre completo de la persona, uso comercial pretendido (distinto a actividad profesional), consentimiento de la persona (si es diferente al solicitante) |
| IV — Grupo artístico | Género artístico (musical, teatral, danza, etc.), integrantes, representante del grupo |
| V — Promoción publicitaria | Descripción de la promoción, fecha de inicio y término, mecánica, bases de participación |

`[model knowledge — verify]` — los requisitos exactos pueden diferir del
Reglamento de la LFDA vigente. Verificar contra fuente primaria.

#### Paso 3: Preparar borrador de solicitud

Producir un borrador de la solicitud con todos los campos requeridos, listo
para revisión del abogado antes de presentación ante INDAUTOR.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Solicitud de Reserva de Derechos al Uso Exclusivo

**Fecha de preparación:** [AAAA-MM-DD]
**Categoría:** [I-V] — [descripción]
**Nombre/título/denominación:** [exacto]

## Datos del solicitante

[Nombre, domicilio, nacionalidad, RFC, representante legal]

## Información específica de la categoría

[Campos per categoría del Paso 2]

## Documentación a adjuntar

- [ ] Formato oficial de INDAUTOR (verificar formato vigente)
- [ ] Comprobante de pago de derechos
- [ ] Poder notarial o carta poder (si actúa representante)
- [ ] [Documentos adicionales según categoría]

## Notas para el abogado

- **Búsqueda previa:** [realizada / no realizada — resultado]
- **Conflictos potenciales:** [reservas o marcas confundibles identificadas]
- **Coordinación IMPI:** [¿se recomienda tramitar marca en paralelo?]
- **Vigencia esperada:** [según categoría]
- **Fecha de renovación proyectada:** [calcular según vigencia]

## Costos estimados

- Derechos de solicitud ante INDAUTOR: [consultar tasa vigente]
  `[model knowledge — verify]`
- Honorarios profesionales: [según acuerdo]
```

**Nota de cierre:**

> Este es un borrador de solicitud para revisión del abogado. Verificar
> los requisitos formales vigentes de INDAUTOR antes de presentar — los
> formatos y requisitos pueden cambiar. No presentar sin revisión profesional.

---

## Modo renovación (`--renovar`)

### Propósito

Gestionar la renovación de reservas de derechos existentes antes de su
vencimiento.

### Flujo de trabajo

#### Paso 1: Identificar la reserva a renovar

> ¿Cuál reserva necesitas renovar?
>
> - **Número de reserva** — expediente ante INDAUTOR
> - **Nombre/título reservado**
> - **Categoría**
> - **Fecha de vencimiento**
> - **Titular actual**

#### Paso 2: Verificar renovabilidad

- **Categoría V (promociones publicitarias) NO es renovable**
  `[model knowledge — verify]`. Si es categoría V, informar que se necesita
  una nueva solicitud para una nueva promoción.
- Verificar si la reserva ha sido utilizada — el no uso puede ser obstáculo
  para la renovación `[model knowledge — verify]`
- Verificar si hay cambios en titularidad que requieran trámite previo de
  transmisión

#### Paso 3: Plazo de renovación

- La renovación debe solicitarse dentro del plazo establecido por la ley
  (generalmente dentro de los últimos 6 meses de vigencia o dentro de los
  6 meses posteriores al vencimiento, con recargos)
  `[model knowledge — verify]`
- **⚠️ Verificar plazos exactos contra la LFDA y su Reglamento** — los plazos
  arriba son heurísticos

#### Paso 4: Preparar solicitud de renovación

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Solicitud de Renovación — Reserva de Derechos al Uso Exclusivo

**Reserva número:** [número de expediente]
**Nombre/título:** [nombre reservado]
**Categoría:** [I-V]
**Titular:** [nombre del titular]
**Vencimiento actual:** [fecha]
**Nuevo vencimiento si se renueva:** [fecha calculada]

## Documentación para renovación

- [ ] Formato oficial de renovación de INDAUTOR
- [ ] Comprobante de pago de derechos de renovación
- [ ] Prueba de uso (si es requerida)
- [ ] Poder notarial o carta poder (si aplica)

## Alerta de calendario

- **Fecha límite para renovar sin recargos:** [fecha]
- **Fecha límite absoluta:** [fecha]
- **Recordatorio sugerido:** [30 días antes del plazo sin recargos]
```

---

## Modo revisión de cartera (`--revisar`)

### Propósito

Revisar el estado de todas las reservas de derechos del cliente para
identificar vencimientos próximos, oportunidades de protección adicional
(coordinación con marca IMPI), y riesgos.

### Flujo de trabajo

#### Paso 1: Cargar la cartera

Leer
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/portfolio.yaml`
— filtrar por tipo `reserva-derechos`. Si no hay datos en el portfolio,
preguntar al usuario por la lista de reservas vigentes.

#### Paso 2: Producir reporte de cartera

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Revisión de Cartera — Reservas de Derechos al Uso Exclusivo

**Fecha de revisión:** [AAAA-MM-DD]
**Total de reservas vigentes:** [N]

## Resumen de estatus

| Estatus | Cantidad |
|---|---|
| Vigentes (sin acción necesaria) | [N] |
| Vencimiento próximo (< 6 meses) | [N] |
| Vencidas (en periodo de gracia) | [N] |
| Vencidas (fuera de periodo de gracia) | [N] |

## Detalle por reserva

| # | Nombre | Categoría | Expediente | Vencimiento | Estatus | Acción |
|---|---|---|---|---|---|---|
| 1 | [nombre] | [cat.] | [exp.] | [fecha] | [vigente/próximo/vencido] | [renovar/buscar marca/ninguna] |

## Alertas

### 🔴 Acción urgente
- [Reservas vencidas o por vencer en < 30 días]

### 🟠 Acción próxima
- [Reservas por vencer en 30-90 días]

### 🟡 Planificación
- [Reservas por vencer en 90-180 días]
- [Reservas sin marca IMPI correspondiente — evaluar registro de marca
  en paralelo]

## Coordinación IMPI

[Lista de reservas que podrían beneficiarse de un registro de marca en
paralelo, con recomendación para cada una]

## Recomendaciones

1. [Renovaciones prioritarias]
2. [Registros de marca sugeridos]
3. [Reservas a abandonar (si corresponde)]
```

---

## Puerta de no-abogado

Antes de emitir cualquier resultado sustantivo, leer `## Quién usa este plugin`.
Si el Rol es No-abogado:

> Las reservas de derechos al uso exclusivo son un trámite ante INDAUTOR con
> requisitos formales específicos. Si bien este skill te ayuda a preparar la
> documentación, la presentación y seguimiento del trámite requiere
> acompañamiento de un abogado especializado en propiedad intelectual,
> particularmente para: (a) evaluar si la reserva es la protección adecuada
> o si se necesita también un registro de marca, (b) verificar conflictos
> con derechos previos, (c) cumplir con los requisitos formales vigentes
> de INDAUTOR.
>
> Referencia: AMPPI, ANADE, Colegio de Abogados local, o despachos
> especializados en derecho de autor y PI.

---

## Lo que este skill NO hace

- **Presentar la solicitud.** Solo preparación. El usuario o su abogado
  presenta ante INDAUTOR.
- **Garantizar disponibilidad.** La búsqueda es orientativa. INDAUTOR
  realiza su propia evaluación y puede encontrar conflictos no detectados.
- **Sustituir la búsqueda de marca ante IMPI.** La coordinación INDAUTOR-IMPI
  es necesaria; este skill señala la necesidad pero no ejecuta la búsqueda de
  marca (usar `/propiedad-intelectual-legal-mexico:clearance` para búsqueda
  de marca).
- **Decidir si la reserva es la protección adecuada.** En muchos casos, una
  marca registrada ante IMPI da protección más amplia y durable que una
  reserva. El abogado evalúa la estrategia óptima.
- **Calcular plazos exactos.** Los plazos indicados son heurísticos basados
  en `[model knowledge — verify]`. Verificar contra la LFDA y su Reglamento
  vigentes.

---

## Cierre con el árbol de decisión de siguientes pasos

Cerrar con el árbol de decisión de siguientes pasos per CLAUDE.md
`## Resultados`. Personalizar las opciones a lo que este skill produjo.
Opciones típicas:

> **¿Qué sigue? Elige una opción y te ayudo a desarrollarla:**
> 1. **Presentar la solicitud** — Revisaré que el borrador esté completo y
>    te daré la lista de documentos a reunir para presentar ante INDAUTOR.
> 2. **Buscar marca en paralelo** — Ejecutaré
>    `/propiedad-intelectual-legal-mexico:clearance` para verificar
>    disponibilidad del nombre como marca ante IMPI.
> 3. **Renovar otra reserva** — Si tienes más reservas por renovar, las
>    proceso en serie.
> 4. **Revisar la cartera completa** — Produciré un reporte de todas las
>    reservas vigentes con alertas de vencimiento.
> 5. **Algo diferente** — dime qué necesitas.
