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
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.
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
> multas, costas, responsabilidades por denuncia temeraria (LFPPI Art. 221
> `[model knowledge — verify]`), y daños agravados.

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
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<asunto-slug>/`.
Nunca leer archivos de otro asunto a menos que `Contexto cruzado entre asuntos`
esté `on`.

Los triajes de infracción frecuentemente llevan a la redacción de cartas de
requerimiento o enrutamiento de notificación de infracción. Abrir un asunto
si no hay uno activo y la práctica es privada — el triaje, la carta y
cualquier respuesta posterior pertenecen a un mismo workspace.

---

## Cargar el perfil de práctica primero

Leer
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.
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

## Las tres vías de acción en México

**Todo modo de triaje debe cerrar con las tres vías disponibles según apliquen
al derecho en juego.** El titular de un derecho de PI en México tiene hasta
tres vías de acción `[model knowledge — verify]`:

### 1. Vía administrativa — IMPI (declaración administrativa)

- **Fundamento:** LFPPI para propiedad industrial; LFDA canalizada a través de
  IMPI para ciertas conductas de infracción en materia de derechos de autor
  (Art. 231 LFDA) `[model knowledge — verify]`
- **Procedimiento:** Solicitud de declaración administrativa de infracción ante
  IMPI (Arts. 334-348 LFPPI) `[model knowledge — verify]`
- **Medidas cautelares:** IMPI puede dictar medidas provisionales (aseguramiento
  de mercancía, suspensión de actividades) — Arts. 349-362 LFPPI
  `[model knowledge — verify]`
- **Sanciones:** Multas (hasta 500,000 UMAs), clausura temporal o definitiva,
  decomiso de mercancía infractora `[model knowledge — verify]`
- **Duración estimada:** ~2 años `[model knowledge — verify]`
- **Apelación:** Recurso de reconsideración ante IMPI → TFJA (antes TFJFA) →
  Tribunales Colegiados de Circuito → SCJN (amparo)
- **Ventaja:** No requiere cuantificar daños; IMPI investiga y resuelve.
  Procedimiento más expedito que la vía civil.

### 2. Vía civil — Juicio ordinario mercantil (daños y perjuicios)

- **Fundamento:** LFPPI Arts. 221-222 (daños por infracción de PI industrial);
  LFDA Art. 216 bis (daños por infracción de derechos de autor)
  `[model knowledge — verify]`
- **Procedimiento:** Juicio ordinario mercantil ante Juzgados de Distrito en
  Materia Civil (competencia federal) — Código de Comercio Arts. 1377 y ss.
  `[model knowledge — verify]`
- **Medidas cautelares:** Providencias precautorias bajo Código de Comercio
  Arts. 1168 y ss.
- **Daños:** Daños y perjuicios + ganancia ilícita del infractor. LFPPI Art.
  221: el monto no podrá ser inferior al 40% del precio de venta al público
  de cada producto o servicio que implique infracción
  `[model knowledge — verify]`
- **Duración estimada:** ~2-4 años (primera instancia + apelación)
- **Ventaja:** Indemnización económica directa; medidas cautelares más amplias.

### 3. Vía penal — UEIDDAPI (denuncia ante MP Federal)

- **Fundamento:** LFPPI Art. 402 (delitos en materia de PI industrial);
  CPF Arts. 424-429 (delitos en materia de derechos de autor)
  `[model knowledge — verify]`
- **Procedimiento:** Denuncia o querella ante el Ministerio Público Federal
  (UEIDDAPI — Unidad Especializada en Investigación de Delitos contra los
  Derechos de Autor y la Propiedad Industrial)
- **Sanciones:** Pena privativa de libertad + multa + reparación del daño
- **Requisito previo:** Para PI industrial, generalmente se requiere resolución
  administrativa previa de IMPI declarando la infracción
  `[model knowledge — verify]`
- **Cuándo procede:** Piratería a escala comercial, falsificación sistemática
  de marcas, revelación dolosa de secretos industriales. No es la vía
  ordinaria para disputas comerciales.

> **⚠️ La vía penal es la opción más severa.** Señalar ÚNICAMENTE cuando los
> hechos sugieran dolo, escala comercial significativa, o reincidencia. No
> sugerir como primera opción en disputas comerciales ordinarias. `[review]`

---

## Modo de marca

### Análisis de confusión — criterios IMPI

El análisis de confusión en México no sigue los tests multifactoriales de
circuitos estadounidenses (Polaroid, Sleekcraft, du Pont). El IMPI aplica
criterios propios derivados de la LFPPI y la jurisprudencia mexicana
`[model knowledge — verify]`:

**Tipos de confusión que analiza el IMPI:**
- **Confusión directa** — el consumidor confunde un producto/servicio con otro
- **Confusión indirecta** — el consumidor cree que los productos/servicios
  provienen de la misma fuente o de fuentes relacionadas
- **Riesgo de asociación** — el consumidor asocia las marcas aunque no las
  confunda directamente

**Factores del análisis de confusión (criterios IMPI):**

- **Semejanza de las marcas** — fonética, gráfica, conceptual e impresión
  comercial en conjunto. El IMPI analiza las marcas en su TOTALIDAD, no
  aislando elementos.
- **Semejanza de productos o servicios** — clasificación NIZA, pero también
  análisis de naturaleza, destino y canales de comercialización reales.
- **Grado de atención del consumidor** — consumidor promedio del sector
  relevante (no especializado, a menos que sea un mercado técnico).
- **Canales de comercialización** — dónde y cómo se comercializan.
- **Fuerza de la marca titular** — fantasía / arbitraria / sugestiva /
  descriptiva con secondary meaning / genérica. Las marcas más fuertes
  (fantasía, arbitraria) reciben protección más amplia.
- **Intención** — evidencia de copia deliberada, imitación de imagen
  comercial, marca cercana.
- **Confusión real** — evidencia de consumidores confundidos (encuestas,
  quejas, correos misdirected).
- **Coexistencia previa** — ¿han coexistido en el mercado sin confusión?

### Marca notoriamente conocida

LFPPI Arts. 190-198 `[model knowledge — verify]` — la marca notoriamente
conocida recibe protección ampliada:

- **Protección más allá de los productos/servicios registrados** — puede
  oponerse a marcas en clases diferentes si hay riesgo de confusión o
  aprovechamiento de la reputación.
- **Declaración ante IMPI** — se puede solicitar declaración de notoriedad o
  de marca famosa.
- **Marca famosa** (Art. 190 LFPPI) `[model knowledge — verify]` — un escalón
  arriba de notoriamente conocida; conocida por la mayoría del público
  consumidor. Protección contra dilución.
- **Dilución** — menoscabo del carácter distintivo o de la reputación.
  Tarnishment (desprestigio) y blurring (dilución de distintividad).

Si la marca titular no es claramente notoria o famosa, señalar la protección
ampliada como un argumento débil.

### Competencia desleal

LFPPI Arts. 213 y ss. `[model knowledge — verify]` — infracciones
administrativas que incluyen:

- Uso de una marca confusamente similar a otra registrada
- Imitación de imagen comercial (trade dress)
- Actos de competencia desleal relacionados con PI
- Publicidad engañosa que involucre signos distintivos

Señalar si los hechos configuran competencia desleal además de o en lugar de
infracción marcaria.

### Resultado de modo marca

Tabla de factores; qué corta en cada dirección; una línea de "no es un
dictamen" al cierre. Cerrar con sugerencia de vía de acción contra la postura
de enforcement del perfil de práctica, identificando las tres vías disponibles
y cuál se recomienda para los hechos.

---

## Modo de derecho de autor

### Titularidad

¿El reclamante es el autor o titular de los derechos patrimoniales (o
licenciatario exclusivo con legitimación)? Puntos a señalar:

- **Obra por encargo** — LFDA Arts. 83-84: los derechos patrimoniales
  pertenecen al comitente, PERO los derechos morales siempre pertenecen al
  autor `[model knowledge — verify]`
- **Obra en colaboración** — LFDA Art. 78: los coautores son cotitulares
  `[model knowledge — verify]`
- **Transmisión de derechos patrimoniales** — LFDA Arts. 30-33: debe constar
  por escrito con requisitos específicos
- **Relación laboral** — las obras creadas en el ejercicio de funciones: la
  ley es menos clara que para invenciones; revisar el contrato
  `[model knowledge — verify]`

### Registro INDAUTOR

El registro ante INDAUTOR (Instituto Nacional del Derecho de Autor) NO es
constitutivo — los derechos de autor nacen con la creación de la obra (LFDA
Art. 5) `[model knowledge — verify]`. Sin embargo:

- El registro es declarativo y genera una presunción de titularidad (prueba
  prima facie)
- NO es requisito para iniciar acciones de infracción (a diferencia de EE.UU.
  donde el registro es prerrequisito para demandar)
- El certificado de registro es útil como prueba en procedimientos

Señalar estatus de registro; si no está registrado, NO señalar como barrera
procesal (como sería en EE.UU.) sino como debilidad probatoria.

### Semejanza sustancial

El análisis de semejanza en derecho mexicano `[model knowledge — verify]`:

- **Reproducción total o parcial** — LFDA Art. 229 señala como infracción la
  reproducción sin autorización `[model knowledge — verify]`
- **Semejanza sustancial** — no se requiere copia exacta; la reproducción de
  los elementos originales y protegibles es suficiente
- **Elementos no protegibles** — ideas, procedimientos, métodos de operación,
  conceptos matemáticos, datos, hechos (LFDA Art. 14)
  `[model knowledge — verify]`
- **Expresión original** — lo protegido es la expresión, no la idea

### Excepciones y limitaciones (equivalente funcional de fair use)

México NO tiene una doctrina de fair use como la de 17 U.S.C. § 107. En su
lugar, la LFDA establece excepciones y limitaciones TAXATIVAS (Arts. 147-151)
`[model knowledge — verify]`:

- Cita de obras con fines de crítica, comentario, investigación o enseñanza
  (con atribución y sin exceder lo justificado)
- Reproducción por una sola vez para uso personal y privado (no comercial)
- Reproducción de artículos sobre temas de actualidad
- Reproducción para procedimientos judiciales o administrativos
- Acceso a obras para personas con discapacidad
- Parodia (debatido — no tan claro como en EE.UU.)

**La diferencia clave con EE.UU.:** las excepciones mexicanas son una lista
cerrada, no un test de factores abierto. Si el uso no cae en ninguna excepción
enlistada, no hay defensa equivalente al fair use. Esto hace que el análisis
de defensa sea más binario que en EE.UU.

### Derechos morales en el triaje

Si los hechos involucran violación de derechos morales (falta de atribución,
mutilación de la obra, divulgación no autorizada), señalar como línea separada.
Los derechos morales son perpetuos, inalienables e irrenunciables (LFDA Art.
19). La violación de derechos morales es infracción independiente de la
infracción de derechos patrimoniales.

### Resultado de modo derecho de autor

Factores señalados; balance de excepciones con "el triaje no concluye";
notas de umbral de titularidad / registro / derechos morales. Enrutamiento per
postura, con las tres vías de acción identificadas.

---

## Modo de patente

### Verificación del tipo de patente/registro

**Revisar el número de registro PRIMERO.** En México, IMPI otorga:

- **Patente de invención** — 20 años de vigencia desde la solicitud
  `[model knowledge — verify]`
- **Modelo de utilidad** — 15 años de vigencia desde la solicitud (objetos,
  utensilios, aparatos o herramientas con una configuración o estructura
  diferente que presente función diferente o ventaja de uso práctico)
  `[model knowledge — verify]`
- **Diseño industrial** — 25 años de vigencia desde la solicitud (modelos
  industriales — forma tridimensional; y dibujos industriales — combinaciones
  de colores, líneas, figuras, formas, texturas, para aspecto ornamental)
  `[model knowledge — verify]`

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
  aplicación industrial, materia no patentable (LFPPI Arts. 45-50)
  `[model knowledge — verify]`. Resultados conocidos de procedimientos de
  nulidad ante IMPI. Arte previo conocido. Expediente de trámite.
- **Defensas de agotamiento de derechos** — si el producto fue legítimamente
  puesto en comercio por el titular o con su consentimiento
  `[model knowledge — verify]`
- **Postura de daños** — daños y perjuicios bajo LFPPI Art. 221 (mínimo 40%
  del precio de venta); ganancia ilícita del infractor
  `[model knowledge — verify]`

### Diseño industrial — análisis diferente

- Análisis de impresión visual de conjunto
- Comparación del diseño registrado vs. el producto acusado
- Elementos funcionales vs. ornamentales — los diseños industriales protegen
  la apariencia, no la función
- Arte previo en diseño — el alcance se estrecha en campos saturados

### Resultado de modo patente

Mapeos de reivindicaciones. Señalamientos de elementos. Señalamientos de
defensas. Enrutamiento a abogado de patentes. Las tres vías de acción.

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

Aplicar LFPPI Arts. 163-170 `[model knowledge — verify]` (secretos
industriales). Señalar:

- **No es de conocimiento general** — no disponible para el público ni para
  otros en la industria que puedan obtener valor económico de su divulgación.
- **Valor económico derivado de la secrecía** — valor económico actual o
  potencial, derivado de no ser generalmente conocido.
- **Combinaciones y compilaciones** — una combinación de elementos públicos
  puede constituir un secreto industrial.

### Medidas razonables de protección

LFPPI requiere que el titular haya adoptado "medidas suficientes" para mantener
la secrecía `[model knowledge — verify]`:

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

LFPPI Arts. 211-212 `[model knowledge — verify]` — adquisición por medios
desleales, o divulgación/uso en incumplimiento de un deber de confidencialidad.

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
qué corta en cada dirección. Enrutamiento per postura. Señalar las tres vías
de acción (la vía penal es particularmente relevante en secretos industriales
cuando hay dolo — LFPPI Art. 402 fracción IV `[model knowledge — verify]`).

---

## Contra-infracción (cuando el cliente es el acusado)

Cuando la postura es de **acusado** (nos señalan a nosotros), el triaje invierte
la dirección pero mantiene los mismos factores. Adicionalmente:

### Defensas comunes en derecho mexicano

- **Uso previo de buena fe** — si el acusado usaba el signo antes del registro
  del titular (LFPPI) `[model knowledge — verify]`
- **Nulidad del registro** — el registro del titular es nulo por falta de
  novedad, actividad inventiva, o por haber sido otorgado en contravención
  de la ley
- **Prescripción de la acción** — verificar plazos según la vía
  `[model knowledge — verify]`
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
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`
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
| Administrativa (IMPI) | LFPPI Arts. 334-348 | ~2 años | No requiere cuantificar daños; IMPI investiga | No hay indemnización directa |
| Civil (daños) | LFPPI Art. 221 / LFDA Art. 216 bis | ~2-4 años | Indemnización económica | Carga probatoria sobre el actor |
| Penal (UEIDDAPI) | LFPPI Art. 402 / CPF Arts. 424-429 | Variable | Efecto disuasorio máximo | Solo para conductas dolosas y graves |

**Vía recomendada para estos hechos:** [identificar con fundamento, pero NO
decidir — el abogado aprueba] `[review]`

## Siguientes pasos recomendados

- [opinión formal de abogado / derivar a abogado de PI nombrado en el perfil]
- [preservación de pruebas — si corre un reloj]
- [desarrollo de hechos necesario — ej., logs de acceso, historia de trámite
  ante IMPI, estudios de mercado, prueba pericial]
- [enrutamiento per
  `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`
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
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<asunto-slug>/outputs/triaje-<modo>-<slug-del-sujeto>-AAAA-MM-DD.md`.
De lo contrario escribir a
`~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/outputs/triaje-<modo>-<slug-del-sujeto>-AAAA-MM-DD.md`
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
