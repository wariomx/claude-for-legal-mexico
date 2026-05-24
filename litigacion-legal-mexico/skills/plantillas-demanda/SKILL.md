---
name: plantillas-demanda
description: >
  Genera plantillas de demanda completas para los principales juicios en derecho
  mexicano: ordinario mercantil, ejecutivo mercantil, oral mercantil, ordinario
  civil, hipotecario, requerimiento de pago y terminación de arrendamiento por
  falta de pago. Cada plantilla incluye estructura procesal, artículos clave,
  documentos requeridos y marcadores [RELLENAR] para personalización. Usar cuando
  el usuario quiera iniciar un juicio o necesite la estructura correcta de una
  demanda según la vía procesal.
argument-hint: "[tipo — mercantil-ordinario | ejecutivo-mercantil | oral-mercantil | civil-ordinario | hipotecario | requerimiento-pago | arrendamiento-renta]"
---

# /plantillas-demanda

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → lado, jurisdicciones, estilo de casa.
2. Usar el árbol de selección si el tipo no se especificó explícitamente.
3. Pre-poblar la plantilla con datos del asunto disponibles en el contexto.
4. Marcar `[RELLENAR: ___]` donde falte información del asunto.
5. Marcar `[VERIFICAR: ___]` en cualquier hecho o cita que requiera confirmación contra fuente primaria.
6. Salida: escrito en formato procesal mexicano, en español, con ⚠️ Nota del revisor arriba.

---

# Plantillas de Demanda — Litigación Mexicana

## Árbol de selección de vía procesal

Si el usuario no especificó el tipo, hacer las siguientes preguntas:

1. **¿La relación es mercantil o civil?**
   - Mercantil (compraventa, préstamo, factoraje, contrato de servicios entre comerciantes) → ir a 2
   - Civil (arrendamiento personal, daños extracontractuales, familia) → ir a 4

2. **¿Tienes un título ejecutivo?** (pagaré, cheque, letra de cambio, póliza de crédito, sentencia, convenio judicial, factura aceptada)
   - Sí → **Ejecutivo mercantil**
   - No → ir a 3

3. **¿El monto reclamado es menor o igual al límite del oral mercantil?** `[VERIFICAR: umbral vigente Art. 1390 Bis CCom — verificar contra DOF]`
   - Sí → **Oral mercantil**
   - No → **Ordinario mercantil**

4. **¿Hay hipoteca o gravamen registrado como garantía?**
   - Sí → **Hipotecario**
   - No → ir a 5

5. **¿Es por falta de pago de renta / terminación de arrendamiento?**
   - Sí → **Arrendamiento / renta**
   - No → **Ordinario civil**

6. **¿Solo quieres requerir el pago extrajudicialmente antes de demandar?**
   - Sí → **Requerimiento de pago** (extrajudicial)

---

## A. Juicio Ordinario Mercantil

**Cuándo usar:** Controversias mercantiles (entre comerciantes o de actos de comercio) que no encuadren en ejecutivo mercantil ni en oral mercantil. Es la vía general.

**Artículos clave:** Arts. 1049, 1377–1390 Código de Comercio `[model knowledge — verify]`

**Plazo para contestar:** 15 días hábiles (Art. 1378 CCom) `[model knowledge — verify]`

**Período probatorio:** 40 días (Art. 1383 CCom) `[verified 2026-05-23]`

**Documentos que deben acompañar la demanda:**
- [ ] Poder notarial o carta poder del representante legal
- [ ] Contrato o documento base de la acción
- [ ] Facturas, pedidos, correos u otros documentos que acrediten la relación
- [ ] Copias para el juzgado + copias para emplazar al demandado

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO MERCANTIL EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ACTOR], por mi propio derecho / en mi carácter de [CARGO] de
[PERSONA MORAL], por conducto de [REPRESENTANTE LEGAL] en términos del poder
notarial que se acompaña como Anexo 1, señalando domicilio para oír y recibir
toda clase de notificaciones en [DOMICILIO], y autorizando para tales efectos a
[PERSONAS AUTORIZADAS] (Art. 1069 Código de Comercio), ante Usted respetuosamente
comparezco y expongo:

                              PROEMIO

Que en la vía ORDINARIA MERCANTIL y en ejercicio de las acciones que más adelante
se precisan, vengo a demandar a [NOMBRE DEL DEMANDADO], persona [física/moral],
con domicilio en [DOMICILIO PARA EMPLAZAMIENTO], las siguientes:

                         PRESTACIONES

1. El pago de la cantidad de $[MONTO] ([MONTO CON LETRA] pesos, moneda nacional),
   por concepto de [DESCRIPCIÓN DEL ADEUDO].

2. El pago de intereses moratorios a razón de [TASA]% [mensual/anual] sobre el
   capital insoluto, desde [FECHA DE MORA] y hasta la total liquidación del adeudo,
   conforme a lo pactado en la Cláusula [NÚMERO] del contrato base de la acción /
   a la tasa legal del Art. 362 del Código de Comercio.
   `[RELLENAR: indicar si la tasa es contractual o legal]`

3. El pago de gastos y costas del presente juicio.

4. [PRESTACIÓN ADICIONAL, si aplica]

                             HECHOS

1. Con fecha [FECHA], [ACTOR] y [DEMANDADO] celebraron [TIPO DE CONTRATO],
   mediante el cual [DESCRIPCIÓN BREVE DE LA OBLIGACIÓN PRINCIPAL].
   `[VERIFICAR: fecha y partes contra documento original]`

2. Conforme a la Cláusula [NÚMERO] del contrato, el demandado se obligó a
   [OBLIGACIÓN ESPECÍFICA] a más tardar el [FECHA DE VENCIMIENTO].
   `[VERIFICAR: texto exacto de la cláusula]`

3. A pesar de las gestiones realizadas por [ACTOR], el demandado no ha cumplido
   con su obligación de pago, existiendo a la fecha un saldo insoluto de
   $[MONTO].
   `[VERIFICAR: saldo actual e historial de pagos]`

4. Con fecha [FECHA], [ACTOR] envió requerimiento de pago al demandado mediante
   [MEDIO — correo certificado / acta circunstanciada / notificación personal],
   sin que a la fecha haya obtenido respuesta favorable.
   `[RELLENAR: adjuntar prueba de envío como Anexo _]`

[AGREGAR LOS HECHOS ADICIONALES QUE PROCEDAN, NUMERADOS]

                      FUNDAMENTOS DE DERECHO

Sustantivos: Arts. 371–387 (compraventa mercantil) / Arts. [APLICABLES] del
Código de Comercio; Arts. 1792–1859 del Código Civil Federal (contratos en general,
supletorio). `[VERIFICAR: artículos específicos al tipo de contrato]`

Procesales: Arts. 1049, 1377–1390 del Código de Comercio (juicio ordinario
mercantil); Art. 1069 (autorización de personas); Art. 1083 (competencia
territorial). `[model knowledge — verify]`

                       PRUEBAS QUE SE OFRECEN

I.   DOCUMENTAL PÚBLICA: [DESCRIPCIÓN] que se acompaña como Anexo [NÚMERO].
     Acredita: Hecho [NÚMERO].

II.  DOCUMENTAL PRIVADA: [DESCRIPCIÓN] que se acompaña como Anexo [NÚMERO].
     Acredita: Hecho [NÚMERO].

III. CONFESIONAL a cargo del demandado [NOMBRE], en relación con los hechos
     [NÚMEROS].

IV.  TESTIMONIAL a cargo de [NOMBRE(S)], quienes declararán sobre los hechos
     [NÚMEROS].
     `[RELLENAR: incluir únicamente si hay testigos — eliminar si no aplica]`

V.   PRESUNCIONAL LEGAL Y HUMANA, en todo lo que favorezca a esta parte.

VI.  INSTRUMENTAL DE ACTUACIONES, en todo lo que favorezca a esta parte.

                        PUNTOS PETITORIOS

POR LO ANTERIORMENTE EXPUESTO Y FUNDADO, A USTED C. JUEZ, ATENTAMENTE PIDO
SE SIRVA:

PRIMERO. Tenerme por presentado en tiempo y forma con este escrito inicial de
demanda, en la vía ordinaria mercantil.

SEGUNDO. Admitir la demanda y ordenar el emplazamiento del demandado
[NOMBRE DEL DEMANDADO] en su domicilio señalado.

TERCERO. Tener por ofrecidas las pruebas señaladas en el capítulo respectivo.

CUARTO. En su oportunidad, previos los trámites de ley, dictar sentencia
definitiva en la que se condene al demandado al pago de las prestaciones
reclamadas en el capítulo correspondiente, con los accesorios de ley.

QUINTO. Condenar al demandado al pago de gastos y costas del presente juicio.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ACTOR / REPRESENTANTE LEGAL]
Cédula Profesional: [NÚMERO]
```

---

## B. Juicio Ejecutivo Mercantil

**Cuándo usar:** Cuando se tiene un título ejecutivo (Art. 1391 CCom). El juicio inicia con embargo y el deudor tiene plazo reducido para oponerse.

**Artículos clave:** Arts. 1391–1414 Código de Comercio `[model knowledge — verify]`

**Títulos ejecutivos (Art. 1391 CCom):** `[VERIFICAR: lista vigente]`
- Sentencia ejecutoriada y la arbitral
- Escritura pública
- Póliza de corredor
- Títulos de crédito (pagaré, cheque, letra de cambio) — endosados al actor o a su favor
- Facturas aceptadas
- Convenios celebrados en el juzgado

**Plazo para contestar:** 8 días hábiles (Art. 1396 CCom) `[verified 2026-05-23]`

**Documentos requeridos:**
- [ ] Título ejecutivo original (pagaré, cheque, letra, etc.)
- [ ] Poder notarial del representante legal
- [ ] En caso de endoso: cadena de endosos completa

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO MERCANTIL EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ACTOR], señalando domicilio en [DOMICILIO], autorizando a
[PERSONAS AUTORIZADAS] (Art. 1069 CCom), ante Usted comparezco y expongo:

                              PROEMIO

Que en la vía EJECUTIVA MERCANTIL, vengo a demandar en juicio ejecutivo a
[NOMBRE DEL DEUDOR], con domicilio en [DOMICILIO], las siguientes:

                         PRESTACIONES

1. El pago de la cantidad de $[MONTO] ([MONTO CON LETRA] pesos), importe del
   título ejecutivo que se acompaña.

2. El pago de intereses moratorios a razón de [TASA]% [mensual/anual] desde
   [FECHA DE VENCIMIENTO] hasta su total liquidación.
   `[RELLENAR: tasa pactada en el título o tasa legal Art. 362 CCom]`

3. El pago de gastos y costas judiciales.

                             HECHOS

1. Con fecha [FECHA], [DEUDOR] suscribió a favor de [ACREEDOR] un [TIPO DE
   TÍTULO — pagaré/cheque/letra] por la cantidad de $[MONTO], con vencimiento
   el [FECHA DE VENCIMIENTO].
   `[VERIFICAR: datos exactos del título]`

2. A la fecha de presentación de esta demanda, el título no ha sido pagado ni
   en todo ni en parte.

3. El título que se acompaña como Anexo 1 constituye título ejecutivo en términos
   del Art. 1391, fracción [NÚMERO], del Código de Comercio.
   `[VERIFICAR: fracción aplicable del Art. 1391]`

                      FUNDAMENTOS DE DERECHO

Sustantivos: Arts. [APLICABLES] de la Ley General de Títulos y Operaciones de
Crédito (LGTOC); Arts. 1391–1414 del Código de Comercio.

Procesales: Arts. 1391–1414 del Código de Comercio (juicio ejecutivo mercantil).

                  SOLICITUD DE MANDAMIENTO EJECUTIVO

Con fundamento en el Art. 1392 del Código de Comercio, solicito a Usted se
sirva librar mandamiento ejecutivo de embargo en bienes del demandado
suficientes para garantizar la suerte principal más intereses y costas,
designando como depositario a [NOMBRE DEL DEPOSITARIO PROPUESTO].

Bienes a embargar: [DESCRIPCIÓN DE BIENES CONOCIDOS O SOLICITAR EMBARGO
GENÉRICO].
`[RELLENAR: identificar bienes conocidos — cuentas bancarias, inmuebles, vehículos]`

                       PRUEBAS QUE SE OFRECEN

I.   DOCUMENTAL PÚBLICA / PRIVADA: [TÍTULO EJECUTIVO] que se acompaña como
     Anexo 1. Acredita: todos los hechos.

II.  PRESUNCIONAL LEGAL Y HUMANA en todo lo que favorezca a esta parte.

III. INSTRUMENTAL DE ACTUACIONES en todo lo que favorezca a esta parte.

                        PUNTOS PETITORIOS

PRIMERO. Tenerme por presentado en la vía ejecutiva mercantil.

SEGUNDO. Librar mandamiento ejecutivo de embargo en contra del demandado
[NOMBRE] sobre bienes suficientes para cubrir la suerte principal, intereses
y costas.

TERCERO. Emplazar al demandado para que dentro del término de 8 días hábiles
(Art. 1396 CCom) oponga excepciones o pague.

CUARTO. En su oportunidad, dictar sentencia de remate en los términos del
Art. 1407 del Código de Comercio, condenando al demandado al pago de las
prestaciones reclamadas. `[verified 2026-05-23]`

QUINTO. Condenar al demandado al pago de gastos y costas.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ACTOR / REPRESENTANTE LEGAL]
```

---

## C. Juicio Oral Mercantil

**Cuándo usar:** Controversias mercantiles cuya cuantía no exceda el límite establecido por el Consejo de la Judicatura Federal para el juicio oral mercantil. `[VERIFICAR: umbral vigente Art. 1390 Bis CCom — actualizado periódicamente, consultar DOF]`

**Artículos clave:** Arts. 1390 Bis al 1390 Bis 49, Código de Comercio `[model knowledge — verify]`

**Audiencias:**
- Audiencia preliminar: dentro de los 10 días siguientes al cierre del período de contestación (Art. 1390 Bis 20 CCom) `[verified 2026-05-23]`
- Audiencia de juicio oral: se desahogan pruebas y se formulan alegatos
- Sentencia: dentro de los 10 días siguientes a la audiencia de juicio

**Documentos requeridos:**
- [ ] Poder notarial
- [ ] Documentos base de la acción (contrato, facturas, correos)
- [ ] Toda la prueba debe ofrecerse con la demanda

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO MERCANTIL EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ACTOR], señalando domicilio en [DOMICILIO], autorizando a
[PERSONAS AUTORIZADAS], ante Usted comparezco y expongo:

                              PROEMIO

Que en la vía ORAL MERCANTIL, con fundamento en los Arts. 1390 Bis y siguientes
del Código de Comercio, vengo a demandar a [NOMBRE DEL DEMANDADO], con
domicilio en [DOMICILIO], las siguientes:

                         PRESTACIONES

1. El pago de $[MONTO] ([MONTO CON LETRA] pesos) por concepto de [DESCRIPCIÓN].

2. Intereses moratorios a razón de [TASA]% desde [FECHA] hasta la liquidación.

3. Gastos y costas.

                             HECHOS

[NARRACIÓN BREVE — el juicio oral mercantil privilegia la concisión; los hechos
se amplían en audiencia]

1. [HECHO 1]
   `[VERIFICAR: documento que lo acredita]`

2. [HECHO 2]

3. [HECHO 3 — incumplimiento específico]

                      FUNDAMENTOS DE DERECHO

Arts. 1390 Bis–1390 Bis 49 del Código de Comercio; Arts. [SUSTANTIVOS
APLICABLES] del Código de Comercio / CCF (supletorio).

                       PRUEBAS QUE SE OFRECEN

IMPORTANTE: En el juicio oral mercantil TODA la prueba se ofrece con la demanda.
No se admiten pruebas que no se hayan ofrecido en este escrito inicial.

I.   DOCUMENTAL: [DESCRIPCIÓN] — Anexo [NÚMERO]. Acredita: Hecho [NÚMERO].

II.  PERICIAL en materia de [MATERIA], a cargo del perito que se designará en
     audiencia.
     `[RELLENAR: incluir solo si es necesario; en juicio oral la pericial se
     simplifica]`

III. TESTIMONIAL a cargo de [NOMBRES], quienes comparecerán a audiencia.

IV.  PRESUNCIONAL LEGAL Y HUMANA e INSTRUMENTAL DE ACTUACIONES.

                        PUNTOS PETITORIOS

PRIMERO. Tenerme por presentado en la vía oral mercantil.

SEGUNDO. Admitir la demanda y señalar fecha y hora para la audiencia preliminar
dentro de los 10 días siguientes al cierre del período de contestación
(Art. 1390 Bis 20 CCom).

TERCERO. Emplazar al demandado para que conteste en el plazo de ley.

CUARTO. En su oportunidad, dictar sentencia condenando al demandado al pago
de las prestaciones reclamadas.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ACTOR / REPRESENTANTE LEGAL]
```

---

## D. Juicio Ordinario Civil

**Cuándo usar:** Controversias civiles (no mercantiles) — responsabilidad civil, cumplimiento de contrato civil, daños y perjuicios — que no sean hipotecarias ni arrendamiento.

**Código procesal aplicable:** Código Nacional de Procedimientos Civiles y Familiares (CNPCF) en estados donde esté vigente; código procesal estatal donde no lo esté. `[VERIFICAR: vigencia del CNPCF en el estado del foro]`

**Artículos clave:** Arts. 225–265 CNPCF (demanda y contestación); Arts. 1159–1168 CCF (prescripción) `[model knowledge — verify]`

**Plazo para contestar:** 15 días hábiles para la vía ordinaria civil (Art. 241 CNPCF) `[verified 2026-05-23]`

**Documentos requeridos:**
- [ ] Poder notarial o carta poder con firma de dos testigos
- [ ] Contrato o documento base
- [ ] Pruebas documentales que respalden los hechos

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO CIVIL EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ACTOR], señalando domicilio en [DOMICILIO], autorizando a
[PERSONAS AUTORIZADAS], ante Usted comparezco y expongo:

                              PROEMIO

Que en la vía ORDINARIA CIVIL, con fundamento en los artículos que más
adelante se señalan, vengo a demandar a [NOMBRE DEL DEMANDADO], con domicilio
en [DOMICILIO], las siguientes:

                         PRESTACIONES

1. El cumplimiento forzoso del contrato de [TIPO] celebrado con fecha [FECHA]
   / el pago de la cantidad de $[MONTO] por concepto de [DESCRIPCIÓN].

2. El pago de daños y perjuicios ocasionados por el incumplimiento, en cantidad
   no menor a $[MONTO ESTIMADO], o la que resulte probada en autos.
   `[RELLENAR: liquidar con precisión si es posible]`

3. El pago de intereses legales desde [FECHA] a razón de la tasa del Art. 2395
   del Código Civil Federal / del código civil estatal aplicable.
   `[VERIFICAR: tasa de interés legal civil en la entidad]`

4. El pago de gastos y costas.

                             HECHOS

1. [HECHO 1 — relación jurídica y su origen]
   `[VERIFICAR: documento y fecha]`

2. [HECHO 2 — obligación específica]

3. [HECHO 3 — incumplimiento y sus consecuencias]

4. [HECHO 4 — gestiones previas / requerimiento]

                      FUNDAMENTOS DE DERECHO

Sustantivos: Arts. [APLICABLES] del Código Civil Federal / [CÓDIGO CIVIL
ESTATAL]; Arts. 1949 (rescisión), 2104–2118 (daños y perjuicios) CCF.
`[VERIFICAR: artículos específicos al tipo de acción]`

Procesales: Arts. 225–265 del Código Nacional de Procedimientos Civiles y
Familiares / [CÓDIGO PROCESAL ESTATAL APLICABLE].

                       PRUEBAS QUE SE OFRECEN

I.   DOCUMENTAL PÚBLICA: [DESCRIPCIÓN] — Anexo [NÚMERO].
II.  DOCUMENTAL PRIVADA: [DESCRIPCIÓN] — Anexo [NÚMERO].
III. CONFESIONAL a cargo del demandado.
IV.  TESTIMONIAL a cargo de [NOMBRES].
V.   PERICIAL en materia de [MATERIA].
     `[RELLENAR: incluir solo si aplica]`
VI.  PRESUNCIONAL LEGAL Y HUMANA e INSTRUMENTAL DE ACTUACIONES.

                        PUNTOS PETITORIOS

PRIMERO. Tenerme por presentado en la vía ordinaria civil.

SEGUNDO. Admitir la demanda y ordenar el emplazamiento del demandado.

TERCERO. En su oportunidad, dictar sentencia condenando al demandado al pago
de las prestaciones reclamadas.

CUARTO. Condenar al demandado al pago de gastos y costas.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ACTOR / REPRESENTANTE LEGAL]
```

---

## E. Juicio Especial Hipotecario

**Cuándo usar:** Ejecución de hipoteca o garantía real registrada en el Registro Público de la Propiedad. El acreedor hipotecario ejercita sus derechos ante incumplimiento del deudor.

**Código procesal:** Código procesal del estado donde esté ubicado el inmueble, o CNPCF donde esté vigente. `[VERIFICAR: código aplicable en el estado del inmueble]`

**Requisitos previos obligatorios:**
- La hipoteca debe estar inscrita en el Registro Público de la Propiedad `[VERIFICAR: folio real]`
- El crédito garantizado debe ser exigible (vencido y no pagado)
- Algunos estados requieren requerimiento previo notarial `[VERIFICAR: requisito en el estado]`

**Documentos requeridos:**
- [ ] Escritura pública constitutiva de la hipoteca
- [ ] Certificado de gravámenes (Registro Público de la Propiedad) — reciente
- [ ] Estado de cuenta certificado del adeudo
- [ ] Avalúo del inmueble (requerido por algunos juzgados)
- [ ] Poder notarial

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO CIVIL / ESPECIALIZADO EN EJECUCIÓN DE GARANTÍAS
EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ACREEDOR HIPOTECARIO], señalando domicilio en [DOMICILIO],
autorizando a [PERSONAS AUTORIZADAS], ante Usted comparezco y expongo:

                              PROEMIO

Que en la vía ESPECIAL HIPOTECARIA, con fundamento en los artículos que más
adelante se señalan, vengo a demandar a [NOMBRE DEL DEUDOR HIPOTECARIO],
con domicilio en [DOMICILIO], como deudor hipotecario, y en su caso a
[NOMBRE DEL TERCER POSEEDOR] como tercer poseedor del inmueble gravado,
las siguientes:

                         PRESTACIONES

1. El pago de la cantidad de $[MONTO] ([MONTO CON LETRA] pesos), importe del
   crédito hipotecario insoluto a la fecha de presentación de esta demanda,
   según estado de cuenta que se acompaña como Anexo [NÚMERO].
   `[VERIFICAR: saldo certificado]`

2. El pago de intereses ordinarios y moratorios devengados y por devengarse
   hasta la total liquidación, a las tasas pactadas en la Cláusula [NÚMERO]
   de la escritura de hipoteca.

3. En caso de incumplimiento del pago: el remate en subasta pública del inmueble
   hipotecado, ubicado en [DOMICILIO DEL INMUEBLE], inscrito en el Registro
   Público de la Propiedad con folio real [NÚMERO].
   `[VERIFICAR: folio real vigente]`

4. Gastos y costas del presente juicio, incluyendo honorarios de perito
   valuador.

                             HECHOS

1. Mediante escritura pública número [NÚMERO], de fecha [FECHA], otorgada
   ante el Notario Público [NÚMERO] de [CIUDAD], Lic. [NOMBRE], [DEUDOR]
   constituyó hipoteca sobre el inmueble identificado en la prestación 3 a
   favor de [ACREEDOR] para garantizar el pago del crédito por $[MONTO
   ORIGINAL].
   `[VERIFICAR: número de escritura, fecha, notario]`

2. Dicha hipoteca quedó inscrita en el Registro Público de la Propiedad
   del Estado de [ESTADO], bajo el folio real [NÚMERO], con fecha [FECHA
   DE INSCRIPCIÓN].
   `[VERIFICAR: datos de inscripción contra certificado de gravámenes]`

3. El deudor incumplió con el pago de [N] mensualidades / el pago total a
   su vencimiento, generando un saldo insoluto de $[MONTO] según el estado
   de cuenta certificado (Anexo [NÚMERO]).

4. [REQUERIMIENTO PREVIO — si aplica en el estado]:
   Con fecha [FECHA], se realizó requerimiento notarial de pago al deudor,
   sin que haya satisfecho el adeudo.
   `[VERIFICAR: si el estado exige requerimiento previo]`

                      FUNDAMENTOS DE DERECHO

Sustantivos: Arts. 2893–2943 del Código Civil Federal (hipoteca);
Arts. [APLICABLES] del Código Civil del Estado de [ESTADO].
`[VERIFICAR: artículos del código civil estatal]`

Procesales: Arts. [JUICIO ESPECIAL HIPOTECARIO] del [CÓDIGO PROCESAL APLICABLE].
`[VERIFICAR: artículos específicos del código procesal del estado]`

Registral: Arts. [APLICABLES] de la Ley del Registro Público de la Propiedad
del Estado de [ESTADO].

                       PRUEBAS QUE SE OFRECEN

I.   DOCUMENTAL PÚBLICA: Escritura de hipoteca — Anexo 1.
II.  DOCUMENTAL PÚBLICA: Certificado de gravámenes — Anexo 2.
III. DOCUMENTAL PRIVADA / PÚBLICA: Estado de cuenta certificado — Anexo 3.
IV.  PERICIAL en materia de valuación inmobiliaria.
     `[RELLENAR: algunos juzgados aceptan avalúo de corredor público]`
V.   PRESUNCIONAL LEGAL Y HUMANA e INSTRUMENTAL DE ACTUACIONES.

                        PUNTOS PETITORIOS

PRIMERO. Tenerme por presentado en la vía especial hipotecaria.

SEGUNDO. Admitir la demanda y ordenar el emplazamiento del deudor y, en su
caso, del tercer poseedor.

TERCERO. En su oportunidad, previo el requerimiento de pago al deudor conforme
al procedimiento del juicio especial hipotecario, y en caso de incumplimiento,
ordenar el remate en pública subasta del inmueble hipotecado para con su
producto cubrir el adeudo, intereses y costas.

CUARTO. Condenar al demandado al pago de gastos y costas.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ACREEDOR / REPRESENTANTE LEGAL]
```

---

## F. Requerimiento de Pago (Extrajudicial)

**Cuándo usar:** Antes de iniciar juicio — para constituir en mora al deudor, interrumpir la prescripción (Art. 1041 CCom / Art. 1168 CCF) e intentar el cobro extrajudicial. También como requisito previo en algunos procedimientos.

**Efectos jurídicos:**
- Constituye en mora al deudor (Art. 2080 CCF / Art. 85 CCom) `[verified 2026-05-23]`
- Interrumpe la prescripción de la acción (Art. 1041 CCom / Art. 1168 CCF) `[model knowledge — verify]`
- En materia laboral: no sustituye la conciliación prejudicial obligatoria ante el CFCRL

**Formalidades recomendadas:**
- Correo certificado con acuse de recibo (valor probatorio básico)
- Acta circunstanciada ante notario público (mayor valor probatorio)
- Notificación personal con testigos

---

```
[CIUDAD], [FECHA]

[NOMBRE DEL DEUDOR]
[DOMICILIO DEL DEUDOR]

ASUNTO: REQUERIMIENTO FORMAL DE PAGO

Estimado(a) [NOMBRE]:

Por medio del presente conducto, en representación de [NOMBRE DEL ACREEDOR]
/ por mi propio derecho, le hago saber lo siguiente:

I. ANTECEDENTES

Con fecha [FECHA], usted contrajo una obligación de pago a favor de
[ACREEDOR] por la cantidad de $[MONTO] ([MONTO CON LETRA] pesos), derivada
de [DESCRIPCIÓN — contrato de fecha ___, factura número ___, pagaré de fecha
___, etc.].
`[VERIFICAR: descripción exacta del documento fuente]`

II. ADEUDO ACTUAL

A la fecha del presente requerimiento, el adeudo a su cargo asciende a las
siguientes cantidades:

- Suerte principal: $[MONTO PRINCIPAL]
- Intereses devengados al [FECHA]: $[MONTO INTERESES]
- Total: $[MONTO TOTAL]

`[VERIFICAR: saldo e intereses calculados correctamente]`

III. REQUERIMIENTO

Por medio del presente documento, REQUIERO FORMALMENTE a usted para que en
un plazo no mayor a [N — generalmente 5, 10 o 15] días hábiles contados a
partir de la recepción del presente, proceda a realizar el pago de la
cantidad de $[MONTO TOTAL] a favor de [ACREEDOR], mediante [MEDIO DE PAGO
— transferencia a cuenta ___, cheque de caja a nombre de ___, etc.].

IV. CONSECUENCIAS DEL INCUMPLIMIENTO

De no recibir el pago íntegro dentro del plazo señalado, [ACREEDOR] se
reserva el derecho de ejercer las acciones legales conducentes, incluyendo
[ACCIÓN ESPECÍFICA — juicio ejecutivo mercantil / ordinario civil /
arbitraje], con la consecuente condena en costas y honorarios a su cargo.

Asimismo, le informamos que el presente requerimiento interrumpe el cómputo
del plazo de prescripción de la acción y constituye a usted en mora respecto
de las obligaciones descritas.

Atentamente,

_______________________________
[NOMBRE DEL ACREEDOR / REPRESENTANTE LEGAL]
[CARGO]
[DATOS DE CONTACTO]

---
[Para el caso de notificación personal:]
RAZÓN DE NOTIFICACIÓN: En [CIUDAD], siendo las [HORA] horas del día [FECHA],
el suscrito [NOMBRE DEL NOTIFICADOR] hizo entrega personal del presente
documento a [NOMBRE DE QUIEN RECIBE], quien dijo ser [DESCRIPCIÓN], en el
domicilio ubicado en [DOMICILIO], quien firmó de recibido. `[RELLENAR]`
```

---

## G. Terminación de Arrendamiento por Falta de Pago (Desahucio)

**Cuándo usar:** Cuando el arrendatario ha dejado de pagar la renta y el arrendador quiere recuperar el inmueble y cobrar las rentas vencidas.

**Marco legal:** Arts. 2398–2490 del Código Civil Federal (arrendamiento); código civil estatal aplicable; Arts. [DESAHUCIO] del código procesal del estado. `[VERIFICAR: legislación específica del estado — algunos estados tienen procedimiento especial de desahucio o de arrendamiento]`

**Acciones ejercitables:**
1. Terminación del contrato de arrendamiento por falta de pago
2. Desocupación y entrega del inmueble
3. Cobro de rentas vencidas y pendientes hasta la entrega efectiva
4. Daños al inmueble, si aplica

**Documentos requeridos:**
- [ ] Contrato de arrendamiento (original o copia certificada)
- [ ] Comprobante de propiedad del arrendador
- [ ] Evidencia de falta de pago (estado de cuenta, comunicaciones con el arrendatario)
- [ ] Poder notarial del representante, si aplica

**Plazo de prescripción:** 1 año para acciones derivadas del contrato de arrendamiento en algunos códigos civiles estatales. `[VERIFICAR: plazo específico del estado]`

---

```
[CIUDAD], [FECHA]

C. JUEZ [NÚMERO] DE LO CIVIL EN TURNO
[CIRCUITO / PARTIDO JUDICIAL]
P R E S E N T E

[NOMBRE DEL ARRENDADOR], señalando domicilio en [DOMICILIO], autorizando a
[PERSONAS AUTORIZADAS], ante Usted comparezco y expongo:

                              PROEMIO

Que en la vía [ORDINARIA CIVIL / ESPECIAL DE ARRENDAMIENTO — según el estado]
`[VERIFICAR: vía procesal aplicable en el estado]`, vengo a demandar a
[NOMBRE DEL ARRENDATARIO], con domicilio en [DOMICILIO / DOMICILIO DEL
INMUEBLE ARRENDADO], las siguientes:

                         PRESTACIONES

1. La terminación del contrato de arrendamiento de fecha [FECHA] respecto del
   inmueble ubicado en [DOMICILIO COMPLETO DEL INMUEBLE], por incumplimiento
   en el pago de rentas.

2. La desocupación y entrega del inmueble arrendado al actor, libre de personas
   y bienes, en el estado en que fue recibido conforme al inventario de entrega.

3. El pago de las rentas vencidas y no pagadas correspondientes a los meses de
   [MESES], por un total de $[MONTO].

4. El pago de las rentas que se sigan causando desde la presentación de esta
   demanda y hasta la entrega efectiva del inmueble, a razón de $[RENTA MENSUAL]
   por mes o la parte proporcional.

5. El pago de los daños causados al inmueble que se acrediten durante el
   procedimiento.
   `[RELLENAR: incluir solo si hay daños documentados]`

6. El pago de gastos y costas del presente juicio.

                             HECHOS

1. El actor es legítimo propietario del inmueble ubicado en [DOMICILIO
   COMPLETO], según escritura pública número [NÚMERO], otorgada ante el
   Notario [NÚMERO] de [CIUDAD], inscrita en el Registro Público de la
   Propiedad con folio [NÚMERO].
   `[VERIFICAR: datos de propiedad]`

2. Con fecha [FECHA INICIO ARRENDAMIENTO], el actor celebró contrato de
   arrendamiento con el demandado sobre dicho inmueble, pactando una renta
   mensual de $[RENTA] pagadera los [DÍAS — primeros cinco días] de cada mes.
   `[VERIFICAR: condiciones del contrato]`

3. A partir del mes de [MES Y AÑO], el arrendatario dejó de pagar la renta
   convenida, acumulando un adeudo de [N] mensualidades por un total de
   $[MONTO TOTAL VENCIDO].

4. Con fecha [FECHA], el actor requirió al arrendatario el pago de las rentas
   vencidas mediante [CORREO CERTIFICADO / ACTA NOTARIAL / COMUNICACIÓN
   ESCRITA], sin que a la fecha haya realizado pago alguno.
   `[VERIFICAR: acreditar el requerimiento — adjuntar como Anexo]`

5. En consecuencia, se actualiza la causal de terminación del arrendamiento
   por falta de pago prevista en el Art. [NÚMERO] del [CÓDIGO CIVIL APLICABLE].
   `[VERIFICAR: artículo específico del código civil del estado]`

                      FUNDAMENTOS DE DERECHO

Sustantivos: Arts. 2398–2490 del Código Civil Federal / Arts. [APLICABLES]
del Código Civil del Estado de [ESTADO] (arrendamiento); Art. [TERMINACIÓN
POR FALTA DE PAGO] del código civil aplicable.

Procesales: Arts. [DESAHUCIO / ORDINARIO CIVIL] del [CÓDIGO PROCESAL
APLICABLE].
`[VERIFICAR: vía procesal y artículos en el estado del foro]`

                       PRUEBAS QUE SE OFRECEN

I.   DOCUMENTAL PÚBLICA: Escritura de propiedad del actor — Anexo 1.

II.  DOCUMENTAL PRIVADA: Contrato de arrendamiento — Anexo 2.

III. DOCUMENTAL PRIVADA: Evidencia de falta de pago (estados de cuenta /
     correos / comunicaciones) — Anexo 3.

IV.  DOCUMENTAL PÚBLICA / PRIVADA: Requerimiento de pago notarial /
     certificado — Anexo 4.

V.   INSPECCIÓN JUDICIAL al inmueble arrendado para acreditar su estado
     actual.
     `[RELLENAR: incluir si hay daños que documentar]`

VI.  TESTIMONIAL a cargo de [NOMBRES], quienes declararán sobre los hechos
     [NÚMEROS].
     `[RELLENAR: testigos de la falta de pago o del estado del inmueble]`

VII. PRESUNCIONAL LEGAL Y HUMANA e INSTRUMENTAL DE ACTUACIONES.

                        PUNTOS PETITORIOS

PRIMERO. Tenerme por presentado en la vía [ORDINARIA CIVIL / ESPECIAL] con
la presente demanda de terminación de arrendamiento.

SEGUNDO. Admitir la demanda y ordenar el emplazamiento del demandado
[NOMBRE].

TERCERO. En su oportunidad, dictar sentencia definitiva en la que se declare:
   a) Terminado el contrato de arrendamiento de fecha [FECHA];
   b) La obligación del demandado de desocupar y entregar el inmueble al
      actor, libre de personas y bienes, dentro del plazo que fije el
      juzgador;
   c) La condena al pago de rentas vencidas por $[MONTO] y las que se
      sigan causando hasta la entrega efectiva del inmueble.

CUARTO. Condenar al demandado al pago de gastos y costas.

PROTESTO LO NECESARIO

[CIUDAD], [FECHA]

_______________________________
[NOMBRE DEL ARRENDADOR / REPRESENTANTE LEGAL]
```

---

## Reglas de uso de estas plantillas

1. **Verificar la vía antes de presentar.** Una demanda presentada en la vía incorrecta puede resultar en desechamiento o reconversión del procedimiento. Si hay duda entre vía ejecutiva y ordinaria, preferir ordinaria (más segura) salvo que el título sea indudable.

2. **Completar todos los marcadores antes de presentar.** Cada `[RELLENAR]` y `[VERIFICAR]` es un elemento que el abogado debe resolver. No presentar un escrito con marcadores pendientes.

3. **Verificar prescripción antes de demandar.** Las acciones prescriben. Verificar el plazo aplicable contra los hechos del caso antes de redactar. `[Ver § Prescripción en el skill redaccion-escritos]`

4. **Adjuntar pruebas con la demanda en oral mercantil.** En el juicio oral, toda la prueba documental se ofrece con la demanda. Una documental no ofrecida en este momento no podrá ofrecerse después.

5. **Confirmar vigencia del CNPCF en el estado.** La implementación del CNPCF es progresiva. Verificar si el juzgado del foro ya opera bajo el CNPCF antes de fundamentar en él.

6. **Citas legales.** Las citas de artículos en estas plantillas están marcadas según su nivel de confianza: `[verified YYYY-MM-DD]` para artículos confirmados contra fuente primaria, `[model knowledge — verify]` para artículos no verificados en esta sesión. Verificar todos los artículos contra el texto vigente antes de presentar.

7. **Para redacción completa del escrito** — con argumentación, manejo de hechos como advocacy, fundamentos de tesis jurisprudenciales — usar `/litigacion-legal-mexico:redaccion-escritos` después de usar esta plantilla como esqueleto.
