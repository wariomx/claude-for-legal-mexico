---
name: triaje-infraccion
description: >
  Triaje de infracción de PI — marcas, derechos de autor, patentes y secretos
  industriales — una lista de factores con la dirección en que cortan, no un
  dictamen. Usar cuando se necesite evaluar si alguien infringe nuestra PI o
  si nosotros podríamos estar infringiendo la de otro, cuando aparece un
  imitador, o cuando se necesita decidir si un asunto vale la pena y por qué
  vía proceder.
argument-hint: "[describir los hechos y el derecho — o solo los hechos y preguntaré]"
---

# /triaje-infraccion

**Esto es un triaje, no un dictamen de infracción o no infracción.**
El análisis de infracción de PI es intensivo en hechos y jurídicamente complejo.
Actuar sobre un triaje — enviar una carta de requerimiento, negarse a cesar,
iniciar una declaración administrativa, o decidir no actuar — sin revisión de
abogado es cómo las empresas terminan del lado equivocado de multas, costas,
responsabilidades por denuncia temeraria y daños agravados.

## Instrucciones

1. Leer
   `PROFILE` resuelto por `matter_workspace.py status`.
   Si contiene `[PLACEHOLDER]`, detenerse y dirigir a
   `/propiedad-intelectual-legal-mexico:cold-start-interview`.
2. Seguir el flujo de trabajo abajo.
3. Preguntar qué derecho está en juego — marca / derecho de autor / patente /
   secreto industrial / mixto. Si mixto, ejecutar cada uno por separado; no
   mezclar.
4. Ejecutar la toma de datos común (postura de parte — titular o acusado,
   jurisdicción, plazos, exhibiciones).
5. Recorrer los factores específicos del modo:
   - **Marca** — análisis de confusión bajo criterios IMPI + dilución (si la
     marca es notoriamente conocida) + competencia desleal.
   - **Derecho de autor** — titularidad + registro INDAUTOR + semejanza
     sustancial + excepciones y limitaciones + derechos morales.
   - **Patente** — mapeo de reivindicaciones (primera pasada); literal +
     equivalentes; infracción indirecta; defensas de nulidad.
   - **Secreto industrial** — existencia del secreto + medidas razonables +
     apropiación indebida.
6. Producir una lista de factores con dirección — qué corta a favor del
   titular, qué a favor del acusado, qué es mixto. Nunca concluir.
7. Identificar las vías de acción disponibles: administrativa (IMPI), civil
   (daños y perjuicios), criminal (UEIDDAPI).
8. Escribir el memorándum de triaje en la carpeta del asunto o en la carpeta
   de resultados de la práctica. Aplicar el encabezado de confidencialidad
   per rol.
9. Cerrar con siguientes pasos recomendados, la puerta de no-abogado si el
   rol es no-abogado, y — si la postura de la práctica soporta la aserción —
   ofrecer redactar la carta de requerimiento vía
   `/propiedad-intelectual-legal-mexico:carta-requerimiento` o la
   notificación de infracción vía
   `/propiedad-intelectual-legal-mexico:notificacion-infraccion`.
   No redactar automáticamente.

Este skill nunca concluye. Si hay duda, señalar — el abogado decide.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:triaje-infraccion "un competidor lanzó un producto llamado APEXSEMILLA en clase 9 — tenemos APEXHOJA registrada en clase 9 ante IMPI; ¿confusión probable?"
```

```
/propiedad-intelectual-legal-mexico:triaje-infraccion "ex ingeniero se llevó notas de nuestra arquitectura de modelo a un competidor — ¿posible secreto industrial?"
```

```
/propiedad-intelectual-legal-mexico:triaje-infraccion
```

(Y el skill preguntará qué derecho y los hechos.)

---

## ESTO ES UN TRIAJE, NO UN DICTAMEN

**La salvaguarda más prominente del plugin. Decirlo al inicio de cada resultado.
No omitirlo. No suavizarlo.**

> **Esto es un triaje, no un dictamen de infracción o no infracción.**
> El análisis de infracción es intensivo en hechos y jurídicamente complejo.
> El triaje identifica los factores y señala los más relevantes; no concluye.
> Una conclusión de que algo infringe o no infringe es una opinión jurídica
> que requiere el criterio de un abogado sobre los hechos, el alcance del
> derecho, la ley aplicable de la jurisdicción relevante, y las defensas
> probables. Actuar sobre un triaje — enviar una carta de requerimiento,
> negarse a cesar, iniciar un procedimiento, o decidir no actuar — sin
> revisión de abogado es cómo las empresas terminan del lado equivocado de
> multas, costas y responsabilidades por una aserción improcedente; verificar
> las vías y remedios del texto vigente (LFPPI arts. 386 y 396-397,
> MX-LFPPI-INFRINGEMENT-REMEDIES-001) y otras consecuencias aplicables.

Sub-calificar un conflicto es una puerta de un solo sentido — una carta no
enviada y una marca se vuelve genérica en el mercado; una acción no perseguida
y la prescripción corre; una obra copiada que permanece en línea.
Sobre-calificar es una puerta de dos sentidos — el abogado reduce. Quedarse
del lado de la puerta de dos sentidos.

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el
CLAUDE.md a nivel de práctica. Si `Habilitado` es `✗` (el valor por defecto
para usuarios internos), omitir el resto de este párrafo — los skills usan
contexto a nivel de práctica y la maquinaria de asuntos es invisible. Si está
habilitado y no hay asunto activo, preguntar: "¿Para qué asunto es esto?
Ejecuta `/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` o
di `nivel-de-práctica`." Cargar el `matter.md` del asunto activo. Escribir
resultados en la carpeta del asunto en
`DATA_ROOT/`.
Nunca leer archivos de otro asunto. El campo legado `Contexto entre asuntos`
no anula el hook; para trabajo a nivel de práctica usar el controlador con
`none` y un flujo agregado explícito.

Los triajes de infracción frecuentemente llevan a la redacción de cartas de
requerimiento o enrutamiento de notificación de infracción. Abrir un asunto
si no hay uno activo y la práctica es privada — el triaje, la carta y
cualquier respuesta posterior pertenecen a un mismo workspace.

---

## Cargar el perfil de práctica primero

Leer
`PROFILE`.
Extraer:

- **Rol** de `## Quién usa este plugin`.
- **Postura de enforcement** de `## Postura de enforcement` — la salida del
  triaje debe terminar con una sugerencia de enrutamiento consistente con la
  postura declarada (agresiva / mesurada / conservadora) y el aprobador
  nombrado para el tipo de carta relevante.
- **Registros en / ejecutar donde** de `## Perfil de práctica de PI` — determina
  qué prueba jurisdiccional aplicar por defecto.
- **Integraciones** de `## Integraciones disponibles` — LegalDataHunter,
  Solve Intelligence cada una afecta si el triaje puede citar jurisprudencia,
  resoluciones previas o arte previo.
- **Postura de decisión** de `## Postura de decisión en juicios jurídicos
  subjetivos` — este skill nunca concluye sobre un umbral subjetivo.

Si la configuración tiene `[PLACEHOLDER]`, mostrar este rebote:

> Noto que aún no has configurado tu perfil de práctica — así es como adapto
> postura, jurisdicciones y cadena de aprobación a tu práctica.
>
> **Dos opciones:**
> - Ejecutar `/propiedad-intelectual-legal-mexico:cold-start-interview`
>   (2 minutos) para configurar tu perfil, y luego ejecuto este triaje
>   adaptado a TU práctica.
> - Decir **"provisional"** y ejecuto con valores genéricos por defecto —
>   jurisdicción México, apetito de riesgo medio, rol abogado, sin playbook —
>   y marco cada resultado `[PROVISIONAL — configura tu perfil para resultados
>   adaptados]` para que veas qué hago antes de comprometerte.

### Modo provisional

Si el usuario dice "provisional," ejecutar el triaje normalmente usando estos
valores genéricos: apetito de riesgo medio, rol abogado, jurisdicción México
(IMPI / tribunales federales), sin playbook (hacer el análisis completo en
vez de cruzar contra una lista de posiciones). Marcar la nota del revisor y
cada bloque de hallazgo con `[PROVISIONAL]`. Al final del resultado, agregar:

> "Esa fue una ejecución genérica contra supuestos por defecto. Ejecuta
> `/propiedad-intelectual-legal-mexico:cold-start-interview` para obtener
> resultados calibrados a TU práctica — tu playbook, tu jurisdicción, tu
> apetito de riesgo. 2 minutos."

---

## Selección de modo

Preguntar al inicio, antes de cualquier cosa:

> ¿Qué derecho estamos triando?
>
> 1. **Marca** — confusión, notoriedad marcaria, competencia desleal
> 2. **Derecho de autor** — semejanza sustancial, excepciones y limitaciones,
>    derechos morales
> 3. **Patente** — mapeo de reivindicaciones (primera pasada), literal +
>    equivalentes
> 4. **Secreto industrial** — existencia, medidas razonables, apropiación
>    indebida
> 5. **Mixto / no estoy seguro** — describe los hechos y los clasifico

Si el usuario elige "no estoy seguro," ayudarle a clasificar. Los mismos hechos
pueden implicar múltiples derechos (ej., el producto de un competidor usa
nuestro logo — marca; y el producto es una copia cercana del nuestro — posible
patente, derecho de autor sobre el empaque, posible imagen comercial; y un
ex-empleado lo lanzó — secreto industrial).

**Si más de un derecho está en juego, ejecutar el triaje para cada uno, por
separado.** No mezclarlos. Cada derecho tiene diferentes factores, diferentes
procedimientos, y diferentes vías de acción.

---

## Toma de datos (común a todos los modos)

> Antes de recorrer factores:
>
> 1. **Postura.** ¿Eres el titular potencial (están tomando lo tuyo) o el
>    acusado potencial (nos están señalando a nosotros)? Los factores son
>    simétricos pero el resultado difiere — un triaje de "me copian" enruta
>    hacia una carta de aserción; un triaje de "podríamos estar expuestos"
>    enruta hacia un memorándum de riesgo.
> 2. **Jurisdicción.** ¿Dónde están los actos de infracción? México (federal
>    vs. estatal), o hay componente internacional. Por defecto México si no se
>    especifica. Señalar si legislación extranjera puede aplicar.
> 3. **Plazos.** ¿Está corriendo algún plazo de prescripción? Señalar plazos
>    relevantes (LFPPI, LFDA, Código de Comercio).
> 4. **¿Qué exhibiciones / pruebas / documentos fuente tienes?** Una captura
>    de pantalla, una URL, una foto de empaque, un extracto de código, un
>    contrato de ex-empleado, un registro de marca.

Esperar la respuesta antes de recorrer factores.

---

## Rutas de acción en México

**Todo modo de triaje debe cerrar con las rutas que realmente podrían aplicar
al derecho y conducta concretos.** No presentar “tres vías” como menú universal
ni como secuencia obligatoria. Identificar los elementos, legitimación,
procedibilidad, prueba, plazo y objetivo de cada ruta antes de sugerirla.

### 1. Vía administrativa — IMPI (declaración administrativa)

- **Fundamento:** LFPPI para propiedad industrial; para infracciones de derecho
  de autor o en materia de comercio, verificar la categoría y autoridad bajo la
  LFDA vigente.
- **Procedimiento:** arts. 328 y siguientes LFPPI; requisitos, pruebas,
  emplazamiento y resolución no se reducen al antiguo rango 334-348
  (**MX-LFPPI-ENFORCEMENT-PROCEDURE-001**).
- **Medidas provisionales:** arts. 344 y siguientes. Identificar la medida
  concreta, apariencia del derecho, fianza/contrafianza y plazo; no prometerla.
- **Inspección:** arts. 354 y siguientes, según proceda.
- **Conducta:** citar la fracción aplicable del art. 386 solo después de
  cotejarla con hechos y texto vigente.
- **Tiempo e impugnación:** obtener estimación y medio de defensa del abogado
  con el expediente actual; no usar duraciones ni cadenas procesales fijas de
  plantilla.

### 2. Indemnización y vía jurisdiccional

- **Fundamento industrial:** arts. 396-410 LFPPI. El art. 396 permite elegir,
  según sus condiciones, entre reclamar ante IMPI una vez concluido el
  procedimiento o acudir directamente a tribunales; no exigir siempre una
  declaración administrativa previa.
- **Competencia:** el art. 407 prevé tribunales federales y, cuando solo se
  afecten intereses particulares, la opción de juzgadores del orden común.
  El abogado debe definir acción, vía procesal y foro.
- **Piso del art. 396:** cuarenta por ciento del **indicador de valor legítimo**
  presentado por la persona titular, desarrollado en el art. 397; no es un
  cuarenta por ciento automático de ventas al público.
- **Derecho de autor:** verificar art. 216 Bis LFDA, causalidad, prueba y vía
  aplicables. No trasladar automáticamente la estructura industrial.
- **Tiempo y medidas:** dependen de vía, foro y hechos; no usar un rango fijo de
  plantilla (**MX-LFPPI-INFRINGEMENT-REMEDIES-001**).

### 3. Vía penal — UEIDDAPI (denuncia ante MP Federal)

- **Fundamento:** delitos enumerados en arts. 402-405 LFPPI o en las
  disposiciones vigentes del CPF sobre derecho de autor, según la conducta.
- **Procedimiento:** Denuncia o querella ante el Ministerio Público Federal
  (UEIDDAPI — Unidad Especializada en Investigación de Delitos contra los
  Derechos de Autor y la Propiedad Industrial)
- **No es universal:** el art. 402 no criminaliza toda infracción industrial.
  Verificar fracción, dolo/fin exigido, querella u oficio y, cuando corresponda,
  el dictamen técnico limitado del art. 405. No sustituirlo por una supuesta
  resolución administrativa previa general.
- **Cuándo considerar:** solo si los hechos satisfacen un tipo penal concreto;
  no usar la vía penal como amenaza genérica
  (**MX-LFPPI-CRIMINAL-OFFENSES-001**).

> **⚠️ La vía penal es la opción más severa.** Señalar ÚNICAMENTE cuando los
> hechos sugieran dolo, escala comercial significativa, o reincidencia. No
> sugerir como primera opción en disputas comerciales ordinarias. `[review]`

---

## Modo de marca

### Análisis de confusión — criterios IMPI

El análisis de confusión en México no sigue los tests multifactoriales de
circuitos estadounidenses (Polaroid, Sleekcraft, du Pont). El IMPI aplica
la LFPPI y los criterios mexicanos que resulten aplicables. Citar la fracción
exacta del art. 173 o 386 y recuperar cualquier tesis antes de atribuirle un
"test" obligatorio (`MX-LFPPI-MARK-REFUSALS-001`).

**Tipos de confusión que analiza el IMPI:**
- **Confusión directa** — el consumidor confunde un producto/servicio con otro
- **Confusión indirecta** — el consumidor cree que los productos/servicios
  provienen de la misma fuente o de fuentes relacionadas
- **Riesgo de asociación** — el consumidor asocia las marcas aunque no las
  confunda directamente

**Ejes de comparación y evidencia — no presentarlos como lista legal cerrada:**

- **Semejanza de las marcas** — fonética, gráfica, conceptual e impresión
  comercial en conjunto. El IMPI analiza las marcas en su TOTALIDAD, no
  aislando elementos.
- **Semejanza de productos o servicios** — clasificación NIZA, pero también
  análisis de naturaleza, destino y canales de comercialización reales.
- **Grado de atención del consumidor** — consumidor promedio del sector
  relevante (no especializado, a menos que sea un mercado técnico).
- **Canales de comercialización** — dónde y cómo se comercializan.
- **Distintividad y alcance demostrado** de la marca anterior; no importar una
  taxonomía estadounidense como si fuera texto de la LFPPI.
- **Intención y confusión observada** — tratarlas como evidencia contextual,
  no como requisitos universales ni factores obligatorios sin criterio citado.
- **Coexistencia previa** — ¿han coexistido en el mercado sin confusión?

### Marca notoriamente conocida o famosa

Para el impedimento de registro, las fracciones XVI y XVII del art. 173 pueden
alcanzar cualquier producto o servicio; en notoriedad se exige además uno de
los efectos enumerados en la fracción XVI. Separar notoriedad de fama y no
traducir automáticamente categorías de *tarnishment/blurring*. Para una
declaratoria ante IMPI, recuperar y citar el procedimiento vigente antes de
describir requisitos (`MX-LFPPI-MARK-REFUSALS-001`).

Si la marca titular no es claramente notoria o famosa, señalar la protección
ampliada como un argumento débil.

### Competencia desleal

LFPPI art. 386 contiene supuestos distintos. Identificar la fracción e inciso y
mapear cada elemento a hechos; no usar "competencia desleal", *trade dress* o
"publicidad engañosa" como tipos genéricos. Para confusión sobre patrocinio de
eventos masivos, aplicar `MX-LFPPI-EVENT-SPONSORSHIP-001`.

### Resultado de modo marca

Tabla de factores; qué corta en cada dirección; una línea de "no es un
dictamen" al cierre. Cerrar con sugerencia de vía de acción contra la postura
de enforcement del perfil de práctica, identificando solo las rutas que
realmente procedan y cuál se recomienda para los hechos.

---

## Modo de derecho de autor

### Titularidad

¿El reclamante es el autor o titular de los derechos patrimoniales (o
licenciatario exclusivo con legitimación)? Puntos a señalar:

- **Obra por encargo** — art. 83: salvo pacto contrario, el comitente goza de
  los patrimoniales/facultades enumeradas; revisar derecho de mención
  (MX-LFDA-COMMISSIONED-WORK-001)
- **Obra en colaboración** — recuperar el texto vigente y el acuerdo entre
  participantes antes de caracterizar cotitularidad o facultades `[verify]`
- **Transmisión de derechos patrimoniales** — LFDA Arts. 30-33: debe constar
  por escrito con requisitos específicos
- **Relación laboral** — art. 84: con contrato individual escrito, reparto igual
  por defecto salvo pacto contrario; sin contrato escrito, patrimoniales del
  empleado (MX-LFDA-EMPLOYMENT-WORK-001)

### Registro INDAUTOR

No importar el prerrequisito registral estadounidense. Conforme a los arts. 5 y
168, la protección no requiere registro, mientras la inscripción genera una
presunción salvo prueba en contrario y deja a salvo derechos de terceros. La
regla procesal de la vía, titularidad, legitimación y prueba aún requieren
análisis. Señalar qué certificado o cadena existe y qué falta
(`MX-LFDA-REGISTRATION-EFFECT-001`).

### Semejanza sustancial

No importar "substantial similarity" como test mexicano sin una fuente. Mapear
qué acto exclusivo y qué infracción concreta se alegan; comparar solo expresión
protegible y separar ideas, procedimientos, métodos, datos y demás materia del
art. 14. Recuperar la fracción aplicable del art. 229 y cualquier criterio
judicial antes de concluir `[verify]`.

### Excepciones y limitaciones (equivalente funcional de fair use)

No aplicar directamente 17 U.S.C. § 107. Clasificar el uso bajo la excepción o
limitación concreta de la LFDA vigente y sus condiciones; recuperar el texto de
los arts. 147-151 antes de usar cualquiera de estas posibilidades `[verify]`:

- Cita de obras con fines de crítica, comentario, investigación o enseñanza
  (con atribución y sin exceder lo justificado)
- Reproducción por una sola vez para uso personal y privado (no comercial)
- Reproducción de artículos sobre temas de actualidad
- Reproducción para procedimientos judiciales o administrativos
- Acceso a obras para personas con discapacidad
- Parodia (debatido — no tan claro como en EE.UU.)

No declarar que la lista vuelve el resultado automáticamente binario: revisar
texto, tratados, derechos fundamentales y precedentes realmente aplicables con
abogado de autor.

### Derechos morales en el triaje

Si los hechos involucran violación de derechos morales (falta de atribución,
mutilación de la obra, divulgación no autorizada), señalar como línea separada.
Los derechos morales son perpetuos, inalienables e irrenunciables (LFDA Art.
19). Analizar su eventual violación en una línea separada de los derechos
patrimoniales y verificar la infracción, acción y remedio concretos; no asumir
que toda afectación produce automáticamente una causa independiente.

### Resultado de modo derecho de autor

Factores señalados; balance de excepciones con "el triaje no concluye";
notas de umbral de titularidad / registro / derechos morales. Enrutamiento per
postura, con las rutas aplicables identificadas.

---

## Modo de patente

### Verificación del tipo de patente/registro

**Revisar el número de registro PRIMERO.** En México, IMPI otorga:

- **Patente de invención** — 20 años improrrogables desde la fecha de
  presentación reconocida, sujeta a anualidades
  (`MX-LFPPI-PATENT-TERM-001`)
- **Modelo de utilidad** — 15 años de vigencia desde la solicitud (objetos,
  utensilios, aparatos o herramientas con una configuración o estructura
  diferente que presente función diferente o ventaja de uso práctico)
  (`MX-LFPPI-UTILITY-MODEL-TERM-001`)
- **Diseño industrial** — vigencia inicial de 5 años desde la presentación,
  renovable por periodos sucesivos de 5 años hasta un máximo de 25 años
  (LFPPI arts. 78-79; regla `MX-LFPPI-DESIGN-TERM-001`) (modelos
  industriales — forma tridimensional; y dibujos industriales — combinaciones
  de colores, líneas, figuras, formas, texturas, para aspecto ornamental)

El análisis de infracción difiere por tipo. No aplicar el análisis de
reivindicaciones de patente de invención a un diseño industrial — los diseños
industriales se evalúan por impresión visual de conjunto, no por elementos
reivindicados.

### Flujo de trabajo para patente de invención / modelo de utilidad

- Producto / proceso / método acusado — descrito en detalle técnico.
- Patente(s) identificada(s).
- Mapeo de reivindicaciones para cada reivindicación independiente: mapeo
  elemento por elemento al producto acusado.
- Infracción literal primero. Equivalentes como señalamiento.
- Infracción indirecta (contribución, inducción) como señalamientos.
- **Defensas de nulidad a considerar** — novedad, actividad inventiva,
  aplicación industrial, materia no considerada invención o exclusiones
  (LFPPI arts. 45-52 y causal vigente del art. 154;
  `MX-LFPPI-PATENTABILITY-001`). Resultados conocidos de procedimientos de
  nulidad ante IMPI. Arte previo conocido. Expediente de trámite.
- **Agotamiento o limitación aplicable** — identificar la disposición vigente y
  sus hechos; no trasladar automáticamente una regla extranjera `[verify]`
- **Postura de daños** — indemnización bajo LFPPI arts. 396-397 (el art. 396
  contiene el piso del 40% sobre el indicador de valor legítimo; no tratarlo
  como 40% automático de ventas sin construir el indicador). La vía elegida,
  legitimación, causalidad, indicador y prueba requieren revisión jurídica.

### Diseño industrial — análisis diferente

- Análisis de impresión visual de conjunto
- Comparación del diseño registrado vs. el producto acusado
- Elementos funcionales vs. ornamentales — los diseños industriales protegen
  la apariencia, no la función
- Arte previo en diseño — el alcance se estrecha en campos saturados

### Resultado de modo patente

Mapeos de reivindicaciones. Señalamientos de elementos. Señalamientos de
defensas. Enrutamiento a abogado de patentes. Las rutas de acción aplicables.

### Transferencia a claim chart completo

Para un mapeo detallado elemento por elemento adecuado para contestaciones de
infracción o nulidad, ejecutar
`/litigacion-legal-mexico:claim-chart`. El mapeo de este triaje es una primera
pasada para identificar los mapeos más fuertes y más débiles; el claim chart de
litigación construye el cuadro completo con citas puntuales, señalamientos de
construcción de reivindicaciones, reivindicaciones dependientes, y el flujo de
verificación que las contestaciones requieren.

---

## Modo de secreto industrial

### ¿Era un secreto?

Aplicar LFPPI arts. 163-169 (`MX-LFPPI-TRADE-SECRETS-001`) (secretos
industriales). Señalar:

- **No es de conocimiento general** — no disponible para el público ni para
  otros en la industria que puedan obtener valor económico de su divulgación.
- **Valor económico derivado de la secrecía** — valor económico actual o
  potencial, derivado de no ser generalmente conocido.
- **Combinaciones y compilaciones** — una combinación de elementos públicos
  puede constituir un secreto industrial.

### Medidas razonables de protección

El art. 163 exige medios o sistemas suficientes para preservar la
confidencialidad y acceso restringido (`MX-LFPPI-TRADE-SECRETS-001`):

- Convenios de confidencialidad con empleados, contratistas, contrapartes.
  ¿Alcance, firmados, ejecutados?
- Controles de acceso — técnicos (acceso por rol), físicos (puertas, gafetes),
  organizacionales (necesidad de conocer).
- Marcado — leyendas de confidencialidad en documentos, código, datos.
- Entrevistas de salida / devolución de materiales al terminar la relación.
- Política de secretos industriales / capacitación.

Señalar qué está en su lugar y qué falta. "Razonable" / "suficiente" es
específico a los hechos; el triaje no decide si las medidas fueron suficientes
— las lista.

### Apropiación indebida

LFPPI arts. 163-169 (**MX-LFPPI-TRADE-SECRETS-001**) — distinguir la definición
de apropiación indebida, sus exclusiones y los deberes de confidencialidad; la
infracción administrativa o delito requieren fundamento específico adicional.

- **Patrón de ex-empleado:** nuevo empleador, trabajo similar, timing de
  salida, documentos llevados (¿y devueltos?), logs de acceso, canales de
  reclutamiento, convenios de confidencialidad y de asignación de invenciones.
- **Divulgación inadvertida:** ¿La divulgación fue hecha por persona con
  deber de confidencialidad? ¿El receptor sabía o debía saber del
  incumplimiento?
- **Ingeniería inversa** — es una defensa si los medios fueron lícitos.
  Señalar si la ingeniería inversa es plausible en los hechos.

### Resultado de modo secreto industrial

Tres grupos de señalamientos — secrecía, medidas, apropiación — cada uno con
qué corta en cada dirección. Enrutamiento conforme a postura. Mostrar solo las
rutas sustentadas. Para vía penal verificar qué fracción III-VI del art. 402
corresponde a los hechos y los elementos subjetivos/procedibilidad; no asumir
que toda apropiación administrativa es delito.

---

## Contra-infracción (cuando el cliente es el acusado)

Cuando la postura es de **acusado** (nos señalan a nosotros), el triaje invierte
la dirección pero mantiene los mismos factores. Adicionalmente:

### Defensas comunes en derecho mexicano

- **Uso previo de buena fe** — verificar disposición, fechas, territorio y
  alcance antes de invocarlo `[verify]`
- **Nulidad del registro** — el registro del titular es nulo por falta de
  novedad, actividad inventiva, o por haber sido otorgado en contravención
  de la ley
- **Prescripción/caducidad procesal** — identificar vía y disposición; no usar
  un plazo genérico `[verify]`
- **Agotamiento de derechos** — el producto fue legítimamente puesto en
  comercio
- **Excepciones y limitaciones** — LFDA Arts. 147-151 para derechos de autor
- **Genericidad o descriptividad** — la marca se ha vuelto genérica o es
  meramente descriptiva
- **Licencia o autorización** — existencia de licencia previa

### Resultado de contra-infracción

Factores que cortan a favor de la defensa, factores que cortan en contra.
Memorándum de riesgo con recomendaciones de respuesta. Si es procedente,
sugerir presentar solicitud de declaración administrativa de nulidad como
contra-ataque.

---

## Formato de resultado (todos los modos)

Anteponer el encabezado de confidencialidad de
`PROFILE`
`## Resultados`.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Triaje de Infracción — [Marca | Derecho de Autor | Patente | Secreto
Industrial] (NO ES UN DICTAMEN)

**Esto es un triaje, no un dictamen de infracción o no infracción.** El triaje
identifica factores y señala los más relevantes; no concluye. Una conclusión
requiere el criterio de un abogado sobre los hechos, el alcance del derecho,
la jurisdicción y las defensas. Actuar sobre un triaje sin revisión de abogado
es cómo las empresas terminan del lado equivocado de multas, costas y daños
agravados.

**Resultado del triaje:** [VERDE / AMARILLO / ROJO — una oración de por qué]

## Postura y alcance

- **Postura de parte:** [titular / acusado]
- **Derecho en juego:** [marca / derecho de autor / patente / secreto industrial]
- **Jurisdicción:** [México — federal / estatal / internacional]
- **Marco legal aplicado:** [citar la prueba y la ley aplicable]
- **Prescripción / plazos:** [estatus del reloj]
- **Exhibiciones / pruebas revisadas:** [lista]

## Análisis de factores

[Tabla de factores específica del modo — factores de confusión / factores de
semejanza / mapeo de reivindicaciones / elementos de secreto industrial. Cada
factor tiene un señalamiento y una dirección. Esto es una lista de factores,
no un veredicto.]

## Defensas y umbrales

[Específico del modo: notoriedad marcaria / excepciones de LFDA / nulidad /
agotamiento de derechos / prescripción / ingeniería inversa / consentimiento /
licencia. Señalar cada uno.]

## Qué corta en qué dirección — resumen

| Factor | Señalamiento | Dirección (titular / acusado / mixto) |
|---|---|---|
| [factor 1] | [nota] | [dirección] |

**Conclusión:** *Este skill no concluye.* Criterio de abogado requerido antes
de actuar. Los factores que cortan [dirección] son [resumen breve]; los factores
que cortan [dirección] son [resumen breve].

## Vías de acción disponibles

| Vía | Fundamento | Plazo estimado | Ventaja | Desventaja |
|---|---|---|---|---|
| Administrativa (IMPI) | LFPPI arts. 328 y ss.; medida arts. 344 y ss.; conducta art. 386 | `[verify]` | Investigación, medidas y sanción según procedencia | Requiere fracción, prueba, garantías y estrategia procesal |
| Indemnización / vía jurisdiccional según el caso | LFPPI arts. 396-410 / LFDA art. 216 Bis | `[verify]` | Reparación económica | Verificar vía, foro, legitimación, causalidad, indicador y prueba |
| Penal (UEIDDAPI) | Tipo concreto de LFPPI arts. 402-405 / CPF vigente | `[verify]` | Persecución de conductas tipificadas | No aplica a toda infracción; verificar procedibilidad y elementos |

**Vía recomendada para estos hechos:** [identificar con fundamento, pero NO
decidir — el abogado aprueba] `[review]`

## Siguientes pasos recomendados

- [opinión formal de abogado / derivar a abogado de PI nombrado en el perfil]
- [preservación de pruebas — si corre un reloj]
- [desarrollo de hechos necesario — ej., logs de acceso, historia de trámite
  ante IMPI, estudios de mercado, prueba pericial]
- [enrutamiento per
  `PROFILE`
  `## Postura de enforcement`, si la postura es de aserción]

## Verificación de citas

Toda ley, tesis, jurisprudencia, número de registro, cita de reivindicación y
exhibición citada aquí debe ser verificada contra la fuente autoritativa antes
de confiar en ella. Las pruebas jurisdiccionales varían y cambian con el
tiempo — confirmar la autoridad vigente y aplicable.
```

---

## Puerta de no-abogado

Antes de emitir el resultado, leer `## Quién usa este plugin`. Si el Rol es
No-abogado:

> Este resultado es un triaje de investigación, no asesoría legal. Enviar una
> carta de requerimiento, decidir no cesar, iniciar un procedimiento
> administrativo, o confiar en "es una excepción permitida" basándose
> únicamente en este triaje tiene consecuencias legales — incluyendo
> responsabilidad por denuncia temeraria, exposición por competencia desleal,
> y costas procesales. Un abogado necesita evaluar antes de que actúes.
>
> Aquí hay un breve para llevar a un abogado:
>
> [Generar un resumen de 1 página: el derecho en juego, la postura, los
> hechos y pruebas, los factores señalados, las defensas señaladas, las
> vías de acción disponibles, y las tres preguntas que hacerle al abogado.]
>
> Si necesitas encontrar un abogado titulado y autorizado en tu jurisdicción:
> el directorio del Colegio de Abogados de tu localidad, la Barra Mexicana de
> Abogados (BMA), la Asociación Nacional de Abogados de Empresa (ANADE), o
> AMPPI (Asociación Mexicana para la Protección de la Propiedad Intelectual)
> para asuntos de PI.

Entregar el triaje junto con el breve.

---

## Ubicación del resultado

Si los espacios de trabajo por asunto están habilitados y hay un asunto activo,
escribir a
`DATA_ROOT/outputs/triaje-<modo>-<slug-del-sujeto>-AAAA-MM-DD.md`.
De lo contrario escribir a
`DATA_ROOT/outputs/triaje-<modo>-<slug-del-sujeto>-AAAA-MM-DD.md`
y mostrar la ruta.

Agregar una entrada de una línea al `history.md` del asunto si hay un asunto
activo.

---

## Transferencia a skills de enforcement

Si el resultado del triaje apunta hacia una aserción y la postura del perfil de
práctica lo soporta, ofrecer:

> ¿Quieres que redacte una carta de requerimiento sobre esto? Ejecuta
> `/propiedad-intelectual-legal-mexico:carta-requerimiento`. Usaré la lista de
> factores de este triaje como base fáctica y aplicaré la cadena de aprobación
> de tu perfil de práctica — la carta no sale sin que el aprobador la autorice.

O, si el modo es derecho de autor y el acusado es contenido alojado en línea:

> ¿Quieres que prepare una notificación de infracción? Ejecuta
> `/propiedad-intelectual-legal-mexico:notificacion-infraccion`.

O, si se necesita mapeo detallado de reivindicaciones para litigio:

> ¿Quieres un claim chart detallado para contestaciones? Ejecuta
> `/litigacion-legal-mexico:claim-chart`. Este triaje es una primera pasada;
> el claim chart de litigación construye el cuadro completo con citas
> puntuales y el flujo de verificación.

No redactar la carta automáticamente desde el triaje. La decisión de actuar es
del aprobador, no del triaje.

---

## Cierre con el árbol de decisión de siguientes pasos

Cerrar con el árbol de decisión de siguientes pasos per CLAUDE.md
`## Resultados`. Personalizar las opciones a lo que este skill produjo — las
cinco ramas por defecto (redactar el X, escalar, obtener más información,
observar y esperar, algo diferente) son un punto de partida, no un candado. El
árbol es el resultado; el abogado elige.

## Lo que este skill NO hace

- **Concluir infracción o no infracción.** Nunca. La salvaguarda más prominente.
- **Sustituir prueba pericial, estudios de mercado, o construcción de
  reivindicaciones.**
- **Evaluar defensas específicas de jurisdicción fuera del alcance del triaje.**
  Si los hechos cruzan fronteras, señalar que se requiere análisis de derecho
  extranjero.
- **Decidir excepciones y limitaciones como cuestión de derecho.** Las
  excepciones de la LFDA son taxativas y su aplicación requiere criterio del
  abogado.
- **Redactar la carta de requerimiento, notificación o demanda.** Esos son
  skills separados
  (`/propiedad-intelectual-legal-mexico:carta-requerimiento`,
  `/propiedad-intelectual-legal-mexico:notificacion-infraccion`) controlados
  por la cadena de aprobación del perfil de práctica.
- **Citar resultados a contrapartes.** Protegido si aplica el encabezado.

---

## Tono

Factor por factor, señalamiento por señalamiento. Sin prosa hedging. La
salvaguarda al inicio hace el trabajo de alcance; el análisis hace el análisis.
Un abogado debería terminar de leer el resultado sabiendo exactamente qué
factores están señalados, qué defensas aplican, qué vías de acción están
disponibles, y qué necesita hacer para actuar o abstenerse.
