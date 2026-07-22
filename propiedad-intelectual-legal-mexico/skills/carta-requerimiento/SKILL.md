---
description: >
  Redacta una carta de requerimiento (modo envío) o clasifica una recibida
  (modo recepción). Usa cuando se hacen valer derechos de PI contra un
  infractor con una carta calibrada a la postura de enforcement, o cuando una
  carta de requerimiento recibida requiere clasificación en un memorándum de
  opciones con recomendación.
---

# /carta-requerimiento

Dos modos. Elige uno:

- `/propiedad-intelectual-legal-mexico:carta-requerimiento --enviar` — redacta una carta de requerimiento calibrada a tu postura de enforcement. Se ejecuta una puerta de revisión antes de la entrega.
- `/propiedad-intelectual-legal-mexico:carta-requerimiento --recibir` — clasifica una carta de requerimiento que recibiste. Produce un memorándum de opciones con recomendación.

## Instrucciones

1. **Leer el perfil de práctica.** Ejecutar `matter_workspace.py status` y cargar `PROFILE`. Si contiene marcadores `[PLACEHOLDER]` o no existe, detenerse y decir: "Este plugin necesita configuración antes de poder darte un resultado útil. Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` — el skill de carta de requerimiento depende de tu postura de enforcement, matriz de aprobación y mezcla de áreas de práctica, ninguna de las cuales está configurada aún."

2. **Verificar espacios de trabajo por asunto.** Conforme a `## Espacios de trabajo por asunto`: si `Habilitado` es `✗`, omitir — los skills usan contexto a nivel de práctica. Si está habilitado y no hay asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` o di `nivel de práctica`."

3. **Despachar según `$ARGUMENTS`:**
   - Si `--enviar` está presente: ejecutar modo envío (abajo). Recorrer identificar-el-derecho, identificar-la-conducta, identificar-la-relación, identificar-la-demanda, calibrar-a-postura, diligencia-de-contraparte, redactar, y la puerta pre-entrega.
   - Si `--recibir` está presente: ejecutar modo recepción (abajo). Solicitar la carta entrante (ruta o texto pegado), luego evaluar, identificar exposición, presentar opciones, y redactar el memorándum de clasificación.
   - Si ninguna bandera está presente: preguntar una vez — "¿Estamos enviando una carta de requerimiento (estás haciendo valer tus derechos) o clasificando una que recibimos (estás defendiendo)?" — y despachar.

4. **Respetar la puerta.** En modo envío, la puerta de revisión se ejecuta antes de que cualquier borrador final se escriba a disco. No omitirla.

5. **Respetar la matriz de aprobación.** Obtener el aprobador para la fila de carta de requerimiento de `## Postura de enforcement → Aprobación para enviar cartas de requerimiento y acciones`. Obtener escalamientos automáticos. Mostrar ambos en la puerta; no suprimirlos.

6. **Transferir cuando corresponda.** En modo recepción, si la recomendación es responder firmemente, ofrecer encadenar a `/propiedad-intelectual-legal-mexico:carta-requerimiento --enviar` pre-poblado con el contexto de respuesta. Si la recomendación es iniciar un procedimiento administrativo ante IMPI o una acción penal, escalar a despacho externo conforme a la fila de litigio de PI del perfil de práctica — no redactar. Si se requiere clasificación para litigio, enrutar a `/litigacion-legal-mexico:requerimiento-triage`.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:carta-requerimiento --enviar
/propiedad-intelectual-legal-mexico:carta-requerimiento --recibir ~/Downloads/carta-recibida-acme.pdf
/propiedad-intelectual-legal-mexico:carta-requerimiento
```

## Notas

- La carta de requerimiento saliente no lleva el encabezado de confidencialidad. El borrador interno, el memorándum pre-envío y el memorándum de clasificación sí lo llevan.
- Los derechos de PI son territoriales; el borrador asume las jurisdicciones declaradas en el perfil de práctica en `Jurisdicciones de registro:`. Si la conducta o la contraparte está en otra jurisdicción, señalar antes de redactar.
- Cada `[CITE:___]` no está verificado hasta ejecutar una verificación contra fuente primaria. Las etiquetas de atribución de fuente permanecen en el borrador.
- Usuarios no abogados reciben un resumen de una página para la conversación con el abogado antes de que la puerta se libere.

---

## Propósito

Una carta de requerimiento (cease & desist) hace valer un derecho de propiedad intelectual y exige que alguien deje de hacer algo. Es una de las comunicaciones más trascendentes que una práctica de PI envía o recibe. Enviar una es un primer paso hacia un procedimiento formal — el destinatario puede contraatacar con una solicitud de nulidad ante IMPI, una reclamación por afirmaciones abusivas o una demanda reconvencional. Recibirla inicia un reloj y fuerza una decisión. Este skill maneja ambos lados con las salvaguardas que la decisión merece.

Dos modos:

- `--enviar` — estás haciendo valer derechos. Redactar una carta de requerimiento calibrada a la postura, puerta antes de entrega.
- `--recibir` — estás defendiendo. Clasificar la carta entrante, producir un memorándum de opciones, enrutar a creación de asunto si amerita.

Si el usuario no pasa una bandera, preguntar una vez: "¿Estamos enviando una carta de requerimiento (estás haciendo valer tus derechos) o clasificando una que recibimos (estás defendiendo)?"

> **Entregable externo (modo envío):** la carta redactada se envía a la contraparte. NO incluir el encabezado `CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL` en la carta saliente. Borradores internos, memorándums pre-envío y memorándums de clasificación mantienen el encabezado conforme a la configuración del plugin `## Resultados`.

## Supuesto jurisdiccional

Los derechos de PI son territoriales — un registro ante IMPI no viaja. Los derechos de autor son multilaterales por Berna/T-MEC pero el enforcement es específico de cada jurisdicción. Este skill asume la jurisdicción declarada en el asunto o en el perfil de práctica en `Jurisdicciones de registro:`. Si la conducta infractora, la contraparte o el foro está en otra parte, señalarlo — el borrador puede no aplicar tal como está redactado.

**Derecho aplicable principal:**
- **Propiedad industrial** — catálogo de infracciones del art. 386 LFPPI; verificar la fracción, procedimiento y medida aplicables en el texto vigente antes de citar (MX-LFPPI-INFRINGEMENT-REMEDIES-001)
- **Derechos de autor** — LFDA arts. 229-230 (infracciones en materia de derechos de autor), arts. 231-236 (infracciones en materia de comercio y sanciones), y arts. 213-217 Bis (vías jurisdiccionales y mecanismos alternativos), según corresponda
- **Vía penal** — LFPPI arts. 402-405 (delitos contra la propiedad industrial), CPF arts. 424-429 (delitos en materia de derechos de autor) — denuncia o querella ante el Ministerio Público Federal y, según el canal institucional vigente, UEIDDAPI (Unidad Especializada en Investigación de Delitos contra los Derechos de Autor y la Propiedad Industrial)
- **Daños civiles** — CCF Arts. 1910-1934 (responsabilidad civil extracontractual), Art. 1916 (daño moral)

`[model knowledge — research lead only]` — no usar hasta verificar artículos específicos contra la versión vigente de cada ley.

## Cargar contexto

- `PROFILE` → `## Postura de enforcement` (postura, detonantes de carta de requerimiento, criterios de carta amigable, matriz de aprobación, escalamientos automáticos), `## Perfil de práctica de PI` (mezcla de áreas, jurisdicciones de registro, despacho externo), `## Resultados` (encabezado de confidencialidad, rol), `## Quién usa este plugin` (rol — abogado vs. no abogado)
- Cualquier plantilla de carta de requerimiento o playbook de enforcement referenciada en los documentos semilla del perfil de práctica — leerla, seguir su estructura
- **Contexto de asunto.** Usar exclusivamente `DATA_ROOT`. Si los asuntos están habilitados y no hay activo, preguntar si debe cambiarse a uno o trabajar a nivel de práctica. Cargar `DATA_ROOT/matter.md` solo con slug activo y escribir resultados en `DATA_ROOT/outputs/`. Nunca leer otra carpeta de `matters/`.

## Modo envío — redacción de la carta de requerimiento

### Paso 1: Identificar el derecho

Preguntar, en un lote:

> ¿Qué derecho de PI estamos haciendo valer?
>
> - **Marca** — ¿está registrada ante IMPI? Número de registro, clase(s) Niza, fecha de otorgamiento. ¿Registro internacional vía Protocolo de Madrid? ¿O marca usada sin registro (fecha de primer uso, alcance geográfico, notoriedad)?
> - **Patente / modelo de utilidad** — ¿está otorgada? Número de patente/registro ante IMPI, título, reivindicaciones principales.
> - **Diseño industrial** — número de registro ante IMPI, descripción, fecha de otorgamiento.
> - **Derecho de autor** — ¿está registrado ante INDAUTOR? Título, número de registro, fecha. ¿O no registrado? (Nota: el registro ante INDAUTOR es declarativo, no constitutivo — los derechos nacen con la creación de la obra, pero el registro facilita la prueba.)
> - **Secreto industrial** — ¿se tienen documentadas las medidas de protección conforme a la LFPPI? (Sin registro, pero se requiere demostrar que se tomaron medidas razonables.)
> - **Varios** — identificar cada uno.

Registrar cada derecho. Derechos registrados se citan por número. Para marcas
usadas sin registro, no inventar exclusividad registral: documentar uso anterior
y analizar el art. 175, una causal de nulidad del art. 258 o, si se alega
notoriedad/fama, los arts. 190 y siguientes, según los hechos y tras verificación.
Derechos de autor no registrados se señalan: "El registro ante INDAUTOR es
declarativo; los derechos surgen con la creación. Sin embargo, el registro
facilita significativamente la prueba de titularidad en procedimiento —
`[review]` evaluar si conviene registrar antes de enviar la carta."

### Paso 2: Identificar la conducta

> Describe la conducta infractora con hechos específicos, no adjetivos:
>
> - **Quién** lo hace — razón social, persona física, nombre comercial, perfil de plataforma.
> - **Qué** — la marca acusada, la copia acusada, el producto acusado, el proceso acusado. Adjuntar o describir muestras.
> - **Dónde** — URL, listado de marketplace, tienda física, redes sociales, establecimiento comercial.
> - **Desde cuándo** — fecha de primera observación, fecha del uso más antiguo documentable.
> - **Evidencia** — capturas de pantalla (con certificación notarial de fe de hechos si las tienes), notas de compra, reportes de servicio de vigilancia, reportes de confusión de clientes, actas de inspección ocular.

Los hechos van en específico. "Usted comercializó el producto X en [URL] ostentando la marca [Y] desde [fecha]" supera a "Usted ha infringido nuestros derechos." Los adjetivos delatan un expediente delgado.

**Fe de hechos notarial.** En México, la evidencia digital tiene mayor valor probatorio cuando se ha levantado **fe de hechos** por notario público (constancia notarial de lo que aparece en un sitio web, red social o marketplace en una fecha determinada). Si el usuario no tiene fe de hechos pero la conducta es relevante, recomendar obtenerla ANTES de enviar la carta — fortalece la posición en un eventual procedimiento ante IMPI o judicial.

### Paso 3: Identificar la relación

> ¿Cuál es la relación entre nosotros y el destinatario?
>
> - **Competidor** (directo o adyacente) — postura estándar aplica
> - **Distribuidor / socio comercial** — el tono se ajusta; considerar la ruta de carta amigable
> - **Ex licenciatario / ex empleado / ex socio** — disposiciones contractuales probablemente aplican; citarlas. Verificar cláusulas de no competencia y confidencialidad.
> - **Desconocido / infractor casual** — postura estándar
> - **Cliente o socio actual** — escalamiento automático conforme al perfil de práctica; señalar antes de redactar
> - **Infractor en comercio informal / tianguis / mercado** — verificar si la conducta satisface un tipo concreto (por ejemplo, LFPPI art. 404 para ciertos objetos con marca falsificada); no recomendar vía penal solo por el lugar. Evaluar medidas IMPI por separado.

Esto cambia el tono, el aprobador, y si se redacta en absoluto sin escalamiento.

### Paso 4: Identificar la demanda

> ¿Qué quiere el cliente realmente?
>
> - **Cesar** — cesar el uso infractor
> - **Informar** — reportar ventas, ingresos, volúmenes (para base de cálculo de daños)
> - **Destruir** — destruir o retirar inventario infractor
> - **Indemnizar** — pago por daños y perjuicios (CCF Arts. 1910-1934)
> - **Transferir / ceder** — transferir dominio, entregar cuenta, ceder marca o derecho
> - **Corrección pública** — retiro, aclaración o publicación solo si existe base
>   legal/procesal verificada o acuerdo de la contraparte; no presumir
>   publicación de sentencia a costa del infractor
> - **Confirmar por escrito** — compromiso de cumplimiento con fecha límite
> - **Conciliar** — abrir una vía de mediación/conciliación para resolver sin procedimiento

Elegir los remedios reales. La demanda debe ser proporcional al daño — una demanda excesiva puede ser usada en contra del remitente como indicio de mala fe si el asunto llega a procedimiento.

**Medidas provisionales como vía paralela.** Si la infracción es urgente
(productos en mercado, evento inminente), señalar la posibilidad de solicitar
**medidas provisionales ante IMPI** bajo los arts. 344 y siguientes
(MX-LFPPI-ENFORCEMENT-PROCEDURE-001). Verificar medida concreta,
fianza/contrafianza, temporalidad, prueba y responsabilidad por afectación antes
de recomendarla. La carta no sustituye ni suspende este análisis.

**Ruta de retiro en marketplace (infracción en comercio electrónico).** Si la conducta acusada está en un marketplace, señalar la vía de protección de marca de la plataforma como camino paralelo más rápido y barato:

- **Mercado Libre Brand Protection** (programa de protección de marcas — reporte de infracción de marca y producto apócrifo)
- **Amazon Brand Registry** (retiro de marca y producto falsificado)
- **Etsy / eBay VeRO / Alibaba IPP** (programas de protección de PI internacionales)
- **TikTok Shop / Shopify** (reportes de infracción de PI)

Un retiro en marketplace frecuentemente se resuelve en días; una carta de requerimiento da al infractor tiempo de vender el inventario mientras negocia. Las dos vías no son mutuamente excluyentes — recomendar ambas cuando la conducta es en marketplace, con la carta de requerimiento cubriendo la conducta fuera de plataforma (sitio web propio, venta mayorista, redes sociales, comercio físico) que el reporte de plataforma no alcanza. Anotar en el memorándum pre-envío si la vía paralela ha sido presentada, está en cola, o fue declinada (y por qué).

**Opción de carta amigable.** En México es común enviar primero una **carta amigable** antes de la carta de requerimiento formal. La carta amigable:
- Tono conciliatorio, no adversarial
- Identifica el derecho y la conducta, pero sin lenguaje de amenaza
- Invita a resolver de buena fe antes de recurrir a vías formales
- No incluye plazo perentorio ni consecuencias legales explícitas
- Útil para: infractores de buena fe aparente, relaciones comerciales que se quieren preservar, primera infracción menor

Leer `Cuándo enviamos carta amigable primero` del perfil de práctica. Si los hechos sugieren una carta amigable en lugar de carta de requerimiento, señalarlo: "Conforme a tu postura de enforcement, este patrón coincide con [carta amigable]. ¿Prefieres la carta amigable o la carta de requerimiento formal?"

### Paso 5: Calibrar a la postura

Leer `## Postura de enforcement` → `Postura por defecto:` y aplicar:

- **Agresiva** — carta firme, plazo corto (7-14 días), lenguaje explícito de consecuencias (procedimiento ante IMPI, medidas provisionales, denuncia penal ante UEIDDAPI, demanda civil de daños y perjuicios), sin suavización
- **Mesurada** — firme pero profesional, plazo estándar (15-30 días), consecuencias señaladas sin dramatismo, apertura a diálogo si responden
- **Conservadora** — encuadre de carta amigable, plazo largo o sin plazo duro, apertura de "nos gustaría dialogar", lenguaje de consecuencias atenuado o ausente

También leer `Cuándo enviamos carta de requerimiento`, `Cuándo enviamos carta amigable primero`, y `Cuándo vamos directo a IMPI`. Si los hechos sugieren que esto debe ser carta amigable, acción directa ante IMPI, o denuncia penal conforme al perfil de práctica, señalarlo antes de redactar.

Sobrescrituras a nivel de asunto en `matter.md` prevalecen sobre el valor por defecto de la práctica.

### Paso 5.5: Diligencia de contraparte — PRECONDICIÓN OBLIGATORIA

**Antes de redactar, ejecutar la diligencia de contraparte y presentar los resultados al usuario.** Esto no es condicional en "si la contraparte parece grande." Toda carta de requerimiento conlleva riesgo de contraataque (nulidad, contrarreclamación, exposición mediática) calibrado a *quién* es el destinatario. El skill no redacta una carta hasta que el usuario ha visto la diligencia y confirmado que desea proceder.

Recopilar y presentar — en un bloque, para aprobación del usuario — lo siguiente:

- **Persona jurídica** — razón social exacta, entidad federativa de constitución, representante legal, cualquier nombre comercial. Registros en Marcanet/SIGA (IMPI); INDAUTOR para derechos de autor; Registro Público de Comercio; BMV si es pública. Señalar `[review]` si la fuente no está confirmada.
- **Tamaño y recursos** — número aproximado de empleados, rango de ingresos si es público, financiamiento si es startup, empresa matriz si es subsidiaria. Fuentes públicas (LinkedIn, prensa, Crunchbase, BMV/CNBV). Señalar honestamente si el tamaño no puede determinarse.
- **Portafolio de PI** — ¿tienen marcas, patentes o derechos de autor registrados en clases adyacentes? Una contraparte con su propio portafolio de PI es más probable que (a) entienda la postura, (b) contra-aserción, y (c) inicie procedimiento de nulidad. Búsqueda rápida en Marcanet/SIGA.
- **Historial de litigio** — búsqueda rápida de procedimientos previos ante IMPI, INDAUTOR, o tribunales como demandante o demandado. Un litigante habitual o contraparte dispuesta a pelear cambia el cálculo.
- **Asesor jurídico** — ¿tienen despacho externo de PI conocido? Despacho, socio responsable si es identificable de expedientes previos.
- **Riesgo de contraataque** — dado tamaño, portafolio de PI, historial de litigio, asesor y foro: ¿es probable que esta contraparte responda con (a) solicitud de nulidad de marca/patente ante IMPI, (b) una reclamación por afirmaciones falsas o abusivas bajo la norma realmente aplicable, (c) demanda reconvencional, o (d) campaña mediática? No citar calumnia federal: `MX-CPF-CALUMNY-REPEAL-001` confirma que el art. 251 CPF no la regula y los arts. 356-359 están derogados. Señalar alto / medio / bajo con razón de una oración.
- **Riesgo de relación** — ¿somos clientes de ellos, compartimos inversionistas, son un potencial adquirente o socio? Confirmación de "no es cliente" obtenida del perfil de práctica; cualquier otra cosa señalada.

Presentar esto como un memorándum corto en chat ANTES del borrador:

```
## Diligencia de contraparte — [Nombre de la Entidad]

- **Entidad:** [razón social, entidad federativa de constitución, empresa matriz en su caso]
- **Tamaño:** [rango de empleados, rango de ingresos, etapa de financiamiento] — [fuente, `[review]` donde aplique]
- **Portafolio de PI:** [marcas / patentes / derechos de autor registrados en clases adyacentes — o "no se encontraron"]
- **Historial de procedimientos:** [procedimientos previos ante IMPI/tribunales como demandante o demandado — o "no se encontraron en revisión rápida"]
- **Asesor jurídico:** [despacho externo de PI conocido — o "no identificado"]
- **Riesgo de contraataque:** [alto / medio / bajo — razonamiento]
- **Riesgo de relación:** [cualquier sobreposición como cliente / inversionista / socio / adquirente — o "no identificado"]

**Escalamientos automáticos que esto detona** (conforme al perfil de práctica `## Postura de enforcement` → Escalamientos automáticos):
- [listar cada detonante que esta diligencia expone]

**Confirmar antes de que redacte:**
- ¿Deseas proceder con una carta de requerimiento contra esta contraparte, dada la diligencia anterior?
- ¿Alguno de los escalamientos automáticos es aplicable? Si sí, el aprobador nombrado en el perfil aprueba antes de la redacción, no después.
```

**No proceder al Paso 6 (Redactar) hasta que el usuario haya interactuado con el bloque de diligencia.** Un "ok" en blanco es peor que ninguna confirmación — insistir: "Antes de que redacte — ¿algo en la diligencia que cambie el cálculo? Tamaño, procedimientos previos, su asesor, relación."

Si la diligencia expone algo en la lista de escalamientos automáticos del perfil de práctica (cliente, contraparte con más recursos, asunto de patentes, potencial mediático, etc.), enrutar al aprobador nombrado conforme al perfil — no redactar en nombre del revisor hasta que el aprobador haya aprobado proceder.

Si elementos críticos de diligencia no pueden ser respondidos (ej., la entidad no puede ser confirmada, el tamaño es desconocido), decirlo y señalar: "No puedo confirmar [entidad / tamaño / asesor] de las fuentes disponibles. ¿Tienes esta información, o debemos pausar hasta que un paralegal o el despacho externo la confirme?"

### Paso 6: Redactar

Estructura del borrador:

1. **Membrete y fecha** — membrete del remitente
2. **Bloque de destinatario** — razón social, domicilio, a la atención de
3. **Línea de referencia** — concisa, no revela estrategia privilegiada. `Re: Uso no autorizado de la marca [MARCA] (Reg. IMPI No. [•])`
4. **Apertura** — identificar al remitente, el derecho, el registro (en su caso), y el hecho de la carta
5. **El derecho** — marca: número de registro, clase(s), fecha de otorgamiento, estatus de renovación; patente: número, título, reivindicaciones principales; derecho de autor: número de registro INDAUTOR, título, año, descripción de la obra; secreto industrial: descripción de las medidas de protección
6. **La conducta infractora** — específica: quién, qué, dónde, cuándo, evidencia
7. **La base jurídica** — `[CITE: LFPPI Art. 386 Fr. [•] / LFDA Art. 229 o 231 Fr. [•] / CCF Art. 1910]` según aplique y solo tras verificar texto vigente
8. **La demanda** — numerada, específica, proporcionada
9. **El plazo** — fecha de calendario, método de confirmación
10. **Consecuencias del incumplimiento** — calibradas a la postura. Las vías disponibles:
    - Procedimiento de declaración administrativa de infracción ante IMPI
    - Solicitud de medidas provisionales (arts. 344 y siguientes LFPPI; verificar requisitos)
    - Denuncia penal ante UEIDDAPI solo si los hechos satisfacen una fracción concreta de los arts. 402-405 LFPPI
    - Reclamación de daños ante IMPI después del procedimiento o acción directa
      ante tribunal, según los arts. 396-410 LFPPI y la legislación procesal
      aplicable; no asumir un único tipo de juicio
11. **Demanda de preservación de evidencia** — documentos, comunicaciones, registros contables, inventario relacionado con la conducta acusada
12. **Reserva de derechos** — "sin que la presente constituya renuncia a acción alguna, civil, administrativa o penal, que en derecho corresponda"
13. **Bloque de firma** — aprobador conforme al perfil de práctica

**Reglas de redacción:**

- **Especificidad sobre adjetivos.** Fechas, URLs, números de registro, muestras. Los adjetivos son la marca de un expediente delgado.
- **Sin aserciones excesivas.** Si la marca está registrada en una clase y el uso acusado es en otra clase, decirlo — no pretender que el registro cubre ambas. Una carta excesiva puede aumentar exposición procesal, reputacional o a contrarreclamaciones; identificar la causa, foro y norma realmente aplicables antes de afirmar costas, daño moral u otra responsabilidad.
- **Citas como placeholders salvo que estén verificadas.** `[CITE: LFPPI Art. 386 Fr. [•]]` permanece como placeholder hasta verificar la fracción contra fuente primaria. Etiquetar cada cita con fuente e ID de regla cuando exista. Nunca retirar las etiquetas.
- **El lenguaje de consecuencias coincide con la postura.** Agresiva → remedios específicos amenazados (procedimiento ante IMPI, medidas provisionales, denuncia penal, daños y perjuicios). Mesurada → "nos reservamos todas las acciones que en derecho correspondan." Conservadora → "nos gustaría dialogar antes de considerar otras medidas."
- **Ganchos jurisdiccionales** — si hay componente internacional (contraparte
  extranjera, productos importados), señalar jurisdicción, régimen aduanero o
  medida fronteriza realmente aplicable y necesidad de corresponsal. No citar
  los arts. 371-381 como bloque aduanero: pertenecen al procedimiento de
  declaración administrativa vigente.
- **Idioma.** La carta se redacta en **español** por defecto (destinatarios y tribunales mexicanos lo esperan). Si la contraparte es extranjera, ofrecer versión bilingüe o en inglés, pero señalar que la versión en español es la que tiene valor probatorio en México.

### Paso 7: La puerta de revisión antes de entrega

Antes de presentar el borrador en chat o escribir el .docx, mostrar esta puerta textualmente. **El usuario debe interactuar con ella** — un reconocimiento en blanco es peor que ninguna puerta.

```
┌─────────────────────────────────────────────────────────────┐
│  ANTES DE QUE ESTE BORRADOR SALGA A CUALQUIER PARTE         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Este es un borrador para revisión de abogado — no una      │
│  carta para enviar. Enviar una carta de requerimiento es    │
│  una aserción de derechos con consecuencias reales:         │
│                                                             │
│  • Puede detonar una solicitud de nulidad de marca/patente  │
│    ante IMPI por parte de la contraparte. Una contraparte   │
│    con recursos puede usar la carta como invitación para    │
│    iniciar un procedimiento en su propio terreno.           │
│                                                             │
│  • Aserciones excesivas o de mala fe pueden ser usadas en   │
│    contra del remitente o detonar contrarreclamaciones.     │
│    El CPF 251 no regula calumnia y los antiguos tipos       │
│    federales de los arts. 356-359 están derogados.          │
│                                                             │
│  • Inicia una disputa que puede no resolverse barato.       │
│                                                             │
│  Confirmar antes de que salga la carta:                     │
│                                                             │
│    1. Los derechos hechos valer son válidos — registrados    │
│       (verificados en Marcanet/SIGA, no asumidos) o         │
│       sólidamente acreditados con evidencia de uso.         │
│    2. La pretensión es sostenible — un practicante           │
│       razonable la haría sobre estos hechos.                │
│    3. La demanda es proporcionada — estamos pidiendo el     │
│       remedio que la conducta amerita, no todo.             │
│    4. Quien tiene autoridad para iniciar una pelea ha       │
│       aprobado.                                             │
│    5. La diligencia de contraparte (Paso 5.5) fue           │
│       presentada y confirmada — entidad, tamaño,            │
│       portafolio de PI, procedimientos previos, asesor,     │
│       riesgo de contraataque, y riesgo de relación.         │
│       No es condicional. Es obligatoria.                    │
│                                                             │
│  Aprobador conforme a tu perfil de práctica:                │
│  [nombre/rol de Postura de enforcement → Aprobación →       │
│   fila de carta de requerimiento]                           │
│                                                             │
│  Escalamientos automáticos que aplican aquí: [listar los    │
│  del perfil que este asunto detona — cliente, contraparte   │
│  con más recursos, patente, potencial mediático, etc. —     │
│  expuestos en el Paso 5.5]                                  │
│                                                             │
│  Estatus de vía paralela (marketplace): [presentado /       │
│  en cola / declinado — del Paso 4. "No aplicable" si la    │
│  conducta no es en marketplace.]                            │
│                                                             │
│  Carta amigable previa: [sí, enviada el [fecha] /          │
│  no — se va directamente con requerimiento / no aplica      │
│  conforme a postura de enforcement]                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Si el usuario es no abogado (conforme a `## Quién usa este plugin`), agregar:

> Enviar una carta de requerimiento tiene consecuencias legales que van más allá de la respuesta del destinatario — es una aserción afirmativa de derechos que puede ser usada en tu contra. ¿Has revisado esto con un abogado? Si no, aquí hay un resumen para llevar a la conversación: [generar un resumen de 1 página: partes, derechos hechos valer, conducta infractora, demanda, postura, riesgos señalados arriba, qué podría salir mal, preguntas específicas para el abogado].
>
> Si necesitas encontrar un abogado titulado en tu jurisdicción: consulta
> directorios profesionales vigentes. Para representación ante IMPI, verificar
> poder, personalidad y requisitos del trámite; no asumir una categoría oficial
> de "agente de propiedad industrial registrado". Para litigio, confirmar
> habilitación profesional y reglas del foro.

No escribir el .docx ni marcar el borrador como listo sin interacción explícita con la puerta.

### Paso 8: Resultado

**Primario:** `<carpeta-asunto>/carta-requerimiento/<slug>/borrador-v<N>.docx` (o `carta-requerimiento/<slug>/borrador-v<N>.docx` a nivel de práctica). Formato de carta conforme a la estructura del borrador arriba. Retirar el encabezado de confidencialidad de la carta saliente.

**En chat:** mostrar el borrador como texto plano para revisión antes de escribir el .docx. Iterar antes de comprometer a disco.

**Nota de cierre para el revisor** (adjunta a la vista previa en chat solamente, retirada del .docx):

> Este es un borrador de carta de requerimiento para revisión de abogado, no una carta lista para enviar. Enviarla es una aserción de derechos con las consecuencias descritas en la puerta pre-entrega. Un abogado titulado revisa, edita y asume responsabilidad profesional antes de enviar. No enviar este borrador sin revisión.

**Verificación de citas.** Cada `[CITE:___]` y cada cita proveniente de plantilla o autoridad proporcionada no está verificada hasta ser cotejada contra la fuente primaria. Antes de enviar, verificar cada cita en la versión vigente de la LFPPI, LFDA, CCF, o la ley aplicable. Citas fabricadas o incorrectas en cartas de aserción son exposición de responsabilidad profesional. Preservar las etiquetas de atribución de fuente — `[LegalDataHunter]`, `[SCJN IUS]`, `[DOF]`, `[IMPI]`, `[user provided]`, `[model knowledge — research lead only]`; esta última nunca llega a una carta saliente.

**Sin suplemento silencioso.** Si una herramienta de investigación configurada devuelve pocos o ningún resultado para una autoridad que el borrador necesita, reportar lo encontrado y detenerse. NO rellenar con búsqueda web o conocimiento del modelo sin preguntar. Presentar opciones — ampliar la consulta, probar otra herramienta, aceptar búsqueda web con etiquetas, dejar el placeholder — y dejar que el usuario decida.

**Checklist post-envío.** Después de que el borrador sea aprobado, escribir `<carpeta-asunto>/carta-requerimiento/<slug>/checklist.md` con: lectura final por aprobador, todos los `[verify]` resueltos, todas las `[CITE]` llenadas y verificadas, marcas de confidencialidad retiradas de la carta saliente, aprobador firmó, método de entrega ejecutado (mensajería con acuse de recibo / correo electrónico certificado / notificación notarial), comprobante de entrega retenido, fecha de cumplimiento calendarizada, plan de escalamiento si no hay respuesta (IMPI / penal / civil), asunto creado en `matters/` si no lo estaba.

## Modo recepción — clasificación de carta de requerimiento recibida

### Paso 1: Leer la carta

Extraer:

- **Remitente** — entidad, firmante, despacho externo si lo hay
- **Destinatario** — cuál de nuestras entidades/personas
- **Método y fecha de entrega**
- **Derecho alegado** — marca (¿número de registro? ¿jurisdicción?), patente (¿otorgada? ¿número?), derecho de autor (¿registrado? ¿título?), diseño industrial, secreto industrial
- **Conducta alegada** — su versión de lo que estamos haciendo
- **Base jurídica** — artículos, disposiciones contractuales, teorías citadas
- **Demanda** — qué quieren; ¿se establece plazo?
- **Amenazas** — qué dicen que harán (IMPI, penal, civil, medidas provisionales)
- **Tono** — firme / suave / incendiario; firma de despacho generalmente señala seriedad

### Paso 2: Evaluar la aserción

No es una opinión jurídica — es una lectura estructurada:

- **Validez de los derechos.** ¿Los registros alegados son reales y están vigentes? (Verificar en Marcanet/SIGA para marcas, SIGA para patentes, INDAUTOR para derechos de autor — señalar cualquiera que parezca caducado o no vigente, incluyendo falta de declaración de uso real a los 3 años para marcas.) Para derechos no registrados, ¿qué evidencia citan realmente?
- **Plausibilidad de confusión / similitud / infracción.** Sobre los hechos alegados, ¿es una pretensión sostenible o es un estiramiento? Para marcas, comparar signos y productos/servicios y citar la fracción/criterio mexicano realmente recuperado; no importar una lista estadounidense. Para autor, identificar acto exclusivo, expresión protegible y fracción concreta. Señalar dónde la pretensión parece más débil.
- **Exceso.** ¿Están demandando más de lo que la conducta amerita? (¿Quieren la marca transferida cuando el registro cubriría a lo sumo un cambio de etiquetado? ¿Quieren todas las ventas cuando solo un canal tocó el derecho?) Demandas excesivas debilitan la palanca y fortalecen una defensa de mala fe o abuso de derecho.
- **Timing.** Prescripción, caducidad, vigencia del registro, oportunidad de los actos reclamados — señalar cualquier tema de fechas en la cara de la carta.
- **Foro.** ¿Dónde actuarían? IMPI (administrativo), tribunales civiles/mercantiles (daños), UEIDDAPI (penal). ¿Hay oportunidad de acción preventiva para nosotros?

### Paso 3: Evaluar nuestra exposición

- **¿Estamos realmente infringiendo?** Mirada honesta. ¿Qué muestra el registro?
- **¿Podríamos dejar de hacerlo fácilmente?** Costo de cumplimiento vs. costo de pelear.
- **¿El remitente es un reclamante real o un oportunista?** ¿Demandante habitual? ¿Dispuesto a pelear? ¿Campaña reciente de cartas de requerimiento contra uso comparable? Verificar expedientes públicos ante IMPI si el tiempo lo permite.
- **¿Qué está en juego más allá de esta disputa?** Valor de marca, relaciones con clientes, precedente para futuras cartas recibidas.

### Paso 4: Opciones

Presentar 5-6 opciones con tradeoffs:

**A — Cumplir rápidamente**
- Cuándo: la pretensión es sostenible, el cumplimiento es barato, y la pelea no vale la pena
- Tradeoff: establece una concesión que pueden señalar después; puede alentar aserciones futuras
- Siguiente paso: confirmar cumplimiento por escrito (restringido), no conceder teoría más amplia

**B — Conciliar / mediar**
- Cuándo: hay un punto medio de negocio (licencia, coexistencia, plazo para rebranding) que lo resuelve
- Tradeoff: compromete tiempo; en México la mediación no tiene la protección automática de FRE 408 — lo dicho en mediación puede no estar protegido contra divulgación salvo acuerdo expreso de confidencialidad `[review]`
- Siguiente paso: carta de acuse y evaluación de negociación, conciliación o
  mecanismo alterno realmente disponible. No remitir a un supuesto centro de
  mediación del IMPI sin verificar autoridad, competencia y canal vigente.

**C — Responder firmemente (rechazar)**
- Cuándo: su pretensión es débil, excesiva, o fácticamente incorrecta; queremos cerrar esto sin procedimiento
- Tradeoff: fija una posición; si la pretensión es de hecho sostenible, nuestra respuesta se convierte en un exhibido
- Siguiente paso: redactar carta de respuesta — considerar ejecutar `/propiedad-intelectual-legal-mexico:carta-requerimiento --enviar` reencuadrado como carta de respuesta

**D — Ignorar (y preservar)**
- Cuándo: la pretensión es frívola, el remitente no tiene capacidad aparente para proceder, el plazo no tiene consecuencia jurídica
- Tradeoff: el silencio puede ser usado como aquiescencia en algunos contextos; deber de preservación de documentos aplica independientemente; riesgo de que sigan con procedimiento formal
- Siguiente paso: activar preservación de documentos; registrar la demanda; continuar

**E — Actuar preventivamente ante IMPI**
- Cuándo: enfrentamos incertidumbre de negocio real, su pretensión es débil, y nos beneficia tomar la iniciativa
- Tradeoff: pasamos a la ofensiva; se requiere presupuesto y aprobación de la dirección
- Opciones: solicitud de nulidad de marca/patente ante IMPI; solicitud de
  declaración de caducidad de marca por no uso bajo el art. 260, fr. II, si los
  hechos y prueba lo permiten (MX-LFPPI-MARK-NULLITY-LAPSE-001)
- Siguiente paso: escalar a despacho externo conforme al perfil de práctica, no redactar

**F — Solicitar cancelación / nulidad de su registro**
- Cuándo: sus derechos mismos son vulnerables y queremos retirar el instrumento del juego
- Para marcas: distinguir nulidad del art. 258, caducidad por no uso del art.
  260, fr. II, y cancelación por genericidad del art. 261; no llamarlas todas
  “cancelación” (MX-LFPPI-MARK-NULLITY-LAPSE-001)
- Para patentes: nulidad por falta de novedad, actividad inventiva, divulgación suficiente o materia/exclusiones bajo los arts. 47-49 LFPPI, según los hechos y el art. 154 vigente
- Tradeoff: lento (~2 años ante IMPI), costoso, público; separado de la disputa en sí
- Siguiente paso: escalar a despacho externo

Recomendar una con dos oraciones de razonamiento. Ser específico sobre por qué.

### Paso 5: Clasificación de plazos

- Su plazo declarado — anotarlo, pero no nos obliga jurídicamente (salvo disposición específica que le dé fuerza).
- Nuestro plazo interno de decisión — típicamente su plazo menos tiempo suficiente para redactar, revisar y aprobar una respuesta. Calendarizarlo.
- Plazos legales — identificar el plazo de la acción, caducidad del registro y
  plazo procesal específicos desde la fuente vigente; no usar los arts. 215-216
  LFPPI como regla genérica de prescripción marcaria.

Ignorar completamente un plazo declarado es una elección, no un default. Anotar que el procedimiento formal generalmente sigue al silencio, no a la fecha del plazo.

### Paso 6: Redactar el memorándum de clasificación

Resultado: `<carpeta-asunto>/carta-requerimiento/entrante/<slug>/clasificacion.md` (o a nivel de práctica si espacios de trabajo por asunto están desactivados).

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — conforme a la configuración del plugin ## Resultados — difiere por rol; ver `## Quién usa este plugin`]

[BLOQUE DE HERENCIA DE CONFIDENCIALIDAD — elegir por rol; ver guía debajo de la plantilla]

# Carta de requerimiento recibida — Clasificación

> **LECTURA PARA CLASIFICACIÓN, NO OPINIÓN.** Este es un escaneo de entrada y análisis de opciones — no un dictamen jurídico de mérito. La evaluación abajo es una lectura estructurada para apoyar la decisión del abogado sobre enrutamiento y respuesta. Cada ley, artículo o tesis citada está señalada para verificación por especialista; cada decisión de mérito es del abogado, no de este skill.

**Slug:** [slug]
**Recibida:** [AAAA-MM-DD]
**Recibida por:** [entidad / persona]
**Archivo entrante:** [ruta]

## La aserción

**Remitente:** [entidad, firmante, despacho]
**Derecho alegado:** [marca / patente / derecho de autor / diseño industrial / secreto industrial — con detalles, números de registro, jurisdicciones]
**Conducta alegada:** [su versión, un párrafo]
**Demanda:** [lista — peticiones específicas]
**Su plazo declarado:** [fecha]
**Tono:** [firme / suave / incendiario]

## Validez de los derechos

[Registros como se alegan — `[review]` verificar contra Marcanet/SIGA/INDAUTOR; derechos no registrados evaluados contra la evidencia citada]

## Base jurídica citada

[Cada cita etiquetada en línea con `[review: aplicabilidad / vigencia / jurisdicción]` y fuente primaria o recuperada `[LegalDataHunter / DOF / user provided]`. Una pista del modelo no se incluye como cita.]

## Evaluación de plausibilidad

- **Confusión / similitud / infracción sobre los hechos:** [lectura]
- **Exceso:** [lectura]
- **Temas de temporalidad (prescripción, caducidad, vigencia del registro):** [lectura]
- **Foro:** [su foro probable; oportunidad de acción preventiva para nosotros]

## Nuestra exposición

- **¿Realmente estamos infringiendo?** [mirada honesta]
- **Costo de cumplimiento vs. costo de pelear:** [lectura]
- **Credibilidad del remitente:** [oportunista / reclamante real / demandante habitual — con evidencia de expedientes públicos si está disponible]
- **Riesgos colaterales:** [marca, clientes, precedente]

**Calificación de clasificación:** [sustancial / debatible / débil / frívola] — *lectura estructurada para enrutamiento, no un dictamen de mérito; `[review]`*

## Opciones

### A. Cumplir rápidamente
[Razonamiento, tradeoffs, siguiente paso]

### B. Conciliar / mediar
[Razonamiento, tradeoffs, siguiente paso]

### C. Responder firmemente
[Razonamiento, tradeoffs, siguiente paso]

### D. Ignorar + preservar
[Razonamiento, tradeoffs, siguiente paso]

### E. Actuar preventivamente ante IMPI
[Razonamiento, tradeoffs, siguiente paso]

### F. Solicitar cancelación / nulidad
[Razonamiento, tradeoffs, siguiente paso]

**Recomendación:** [A/B/C/D/E/F] — [dos oraciones por qué] — `[review: abogado debe confirmar antes de ejecutar]`

## Plazos

- **Su plazo declarado:** [fecha]
- **Nuestro plazo interno de decisión:** [fecha]
- **Plazos legales de la pretensión subyacente:** [prescripción, caducidad, procesales — con fechas]

## Acciones inmediatas

- [ ] Preservación de documentos activada — [sí/no]
- [ ] Asunto creado en registro — [sí/no/por determinar]
- [ ] Abogado asignado — [quién]
- [ ] Seguro tendido — [sí/no/N-A]
- [ ] Escalamiento interno — [a quién/cuándo]
```

**Bloque de herencia de confidencialidad — elegir por rol.** Leer `## Quién usa este plugin` (Rol) en la configuración del plugin. Esta clasificación registra una primera lectura de mérito sobre una aserción adversa; si realmente está protegida depende de quién la preparó. Insertar exactamente uno de los siguientes:

- **Rol = Abogado titulado / profesional jurídico:**
  > **Herencia de confidencialidad.** Esta clasificación registra nuestra primera lectura de mérito y postura de respuesta ante una aserción adversa. Es material protegido por el secreto profesional (Art. 36 Ley Reglamentaria del Art. 5° Constitucional). No reenviar, adjuntar a una reclamación de seguro sin depurar, ni compartir con la contraparte. Almacenar con material privilegiado del asunto conforme a las convenciones internas de confidencialidad.

- **Rol = No abogado (cualquier tipo):**
  > **CONFIDENCIAL — NO PRIVILEGIADO.** Este documento no está protegido por el secreto profesional hasta que sea revisado por un abogado titulado. Tratarlo como confidencial; no reenviarlo a nadie fuera de la cadena de revisión jurídica; llevarlo al abogado y permitir que el abogado lo marque. Reenviarlo como "privilegiado" antes de que un abogado lo revise no lo convierte en privilegiado y puede perjudicar si el asunto se vuelve contencioso.

Cerrar la presentación en chat con esta salvaguarda textualmente:

> Este es un memorándum de clasificación, no asesoría. La evaluación de fortaleza arriba es una primera lectura basada solo en la carta — no toma en cuenta hechos que no me has dicho, registros que no puedo verificar, ni temas jurisdiccionales. Un abogado evalúa antes de que respondas, decidas ignorar, o te comprometas con un camino.

Si el usuario es no abogado, agregar el párrafo de "encontrar un abogado" del modo envío.

### Paso 7: Transferir

Basado en la recomendación y confirmación del usuario:

- Responder firmemente → transferir a `/propiedad-intelectual-legal-mexico:carta-requerimiento --enviar` con contexto pre-poblado como carta de respuesta (esto detona la puerta del modo envío nuevamente).
- Conciliar → iniciar una carta de acuse / vía de conciliación en el asunto.
- Actuar preventivamente o solicitar cancelación/nulidad → escalar a despacho externo conforme a la fila de litigio de PI del perfil de práctica; no redactar. Si se requiere clasificación para litigio, enrutar a `/litigacion-legal-mexico:requerimiento-triage`.
- Creación de asunto → si no hay uno y el asunto es material, ofrecer `/propiedad-intelectual-legal-mexico:matter-workspace new <slug>` pre-poblado.
- Cumplir / ignorar → registrar la decisión en el historial del asunto; activar o confirmar la preservación de documentos; cerrar el registro de clasificación.
- Vía penal → si se considera denuncia ante UEIDDAPI, escalar a despacho externo de PI penal; no redactar la denuncia.

## Postura de decisión

Conforme a `## Postura de decisión en juicios jurídicos subjetivos` en el perfil de práctica: cuando sea incierto si hay infracción, si una marca es confusamente similar, si una obra es sustancialmente similar, si una pretensión es sostenible, o si enviar es seguro — no decidir silenciosamente que está bien. Señalar para revisión del abogado, exponer los factores que cortan en ambas direcciones, anotar la incertidumbre. Enviar una carta de requerimiento sobre una suposición es una puerta de un solo sentido; exponer la duda es una puerta de dos sentidos.

## Qué este skill NO hace

- **Enviar la carta.** Solo redacción. El usuario envía, después de aprobación.
- **Investigar citas.** Los placeholders permanecen como placeholders salvo que el usuario proporcione autoridades o una herramienta de investigación conectada las devuelva. Inventar citas es exposición de responsabilidad profesional.
- **Saltarse la puerta.** La puerta del modo envío se ejecuta cada vez.
- **Decidir mérito definitivamente en el lado de recepción.** La calificación es una lectura estructurada para enrutamiento; un dictamen formal de mérito corresponde al abogado.
- **Validar la ley citada por el remitente.** Señala para el usuario; no declara autónomamente que una pretensión es válida o inválida.
- **Tomar la decisión de creación de asunto.** Expone la recomendación; el usuario decide.
- **Iniciar procedimientos penales.** La denuncia ante UEIDDAPI requiere redacción especializada por abogado penalista de PI; este skill no redacta denuncias penales.
