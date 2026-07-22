---
name: clearance
description: >
  Búsqueda de disponibilidad de marca — eliminatoria + verificación de marcas
  similares produciendo una lista de señales, no una opinión de disponibilidad.
  Usa cuando se propone una marca nueva, cuando pregunten si una marca está
  disponible o para correr una búsqueda eliminatoria, o al evaluar riesgo de
  confusión antes de una búsqueda profesional completa. Este skill NUNCA concluye
  que una marca está libre.
argument-hint: "[describe la marca propuesta, productos/servicios y jurisdicciones — o solo la marca y preguntaré]"
---

# /clearance

**Esto es un triaje, no una opinión de disponibilidad.** Una opinión de
disponibilidad de marca requiere una búsqueda profesional completa y el criterio
de un abogado titulado especialista en marcas. Un resultado de "sin conflictos
evidentes" significa que el triaje no encontró nada — no significa que la marca
esté libre. Se han iniciado procedimientos de infracción contra marcas que
pasaron una búsqueda eliminatoria.

## Instrucciones

1. Ejecutar `matter_workspace.py status` y leer `PROFILE`. Si contiene `[PLACEHOLDER]`, detener y dirigir a `/propiedad-intelectual-legal-mexico:cold-start-interview`.
2. Seguir el flujo de trabajo de abajo.
3. Correr la toma de datos (marca, productos/servicios, clases, jurisdicciones, visualización/estilización).
4. Verificación eliminatoria de impedimentos intrínsecos — genéricos, descriptivos, contrarios al orden público, banderas/escudos, denominaciones de origen, nombres sin consentimiento, títulos/personajes con reserva, formas funcionales, falsas indicaciones de procedencia.
5. Probar en runtime una capacidad específica de búsqueda registral de marcas.
   Los conectores incluidos no garantizan esa capacidad. Si no existe una
   herramienta probada, decirlo y proceder solo con datos del usuario y análisis
   estructurado; no reutilizar una herramienta de patentes como si fuera marcas.
6. Recorrer el análisis de similitud conforme al marco mexicano: similitud fonética, gráfica e ideológica, similitud de productos/servicios, canales de comercialización, consumidores relevantes, distintividad de la marca anterior, notoriedad. Señalar cada eje; nunca concluir.
7. Escribir el memorándum de triaje a la carpeta del asunto (si un asunto está activo) o la carpeta de resultados de la práctica. Aplicar el encabezado de confidencialidad conforme al rol.
8. Cerrar con siguientes pasos recomendados y la compuerta de no abogado si el rol es no abogado.

Este skill nunca concluye que una marca está libre. Si hay duda, señalar — el
abogado decide.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:clearance "APEXLEAF para línea de ropa deportiva, lanzamiento México + Madrid"
```

```
/propiedad-intelectual-legal-mexico:clearance
```

(Y el skill preguntará por la marca, productos, clases y jurisdicciones.)

---

## ESTO ES UN PRIMER PASE, NO UNA OPINIÓN DE DISPONIBILIDAD

**Decir esto al inicio de cada resultado. No omitirlo. No suavizarlo.**

> **Esto es un primer pase, no una opinión de disponibilidad.** Una opinión de
> disponibilidad de marca requiere una búsqueda profesional completa (Marcanet,
> MARCia, registros estatales de nombre comercial, fuentes de uso común y no
> registrado, registros internacionales vía OMPI/EUIPO, dominios, redes sociales
> y marcas de diseño/trade dress donde sea relevante) y el criterio de un abogado
> titulado sobre riesgo de confusión, que depende de factores que un triaje
> estructurado no puede evaluar completamente. Un resultado de "sin conflictos
> evidentes" de este skill significa que el triaje no encontró nada — no que la
> marca esté libre. Se han iniciado procedimientos de infracción ante IMPI contra
> marcas que pasaron una búsqueda eliminatoria. Un abogado titulado especialista
> en marcas evalúa antes de que alguien adopte, solicite o invierta en esta marca.

Esta es la guardia más fuerte del plugin. Sub-señalar un conflicto es una puerta
de un solo sentido — un logo en producto, una campaña lanzada, una solicitud
ante IMPI, todo con un problema debajo. Sobre-señalar es una puerta de dos
sentidos — el abogado reduce la lista en revisión. Quedarse del lado de la
puerta de dos sentidos.

---

## Contexto de asunto

**Contexto de asunto.** Usar exclusivamente `DATA_ROOT`. Si los asuntos están habilitados y no hay activo, preguntar si debe cambiarse a uno o trabajar a nivel de práctica. Cargar `DATA_ROOT/matter.md` solo cuando haya slug activo y escribir en `DATA_ROOT/outputs/`. Nunca leer otra carpeta de `matters/`.

---

## Cargar el perfil de práctica primero

Antes de correr la búsqueda de disponibilidad, leer `PROFILE`. Extraer:

- **Rol** de `## Quién usa este plugin` (abogado vs. no abogado cambia el encabezado de confidencialidad y la compuerta de no abogado abajo).
- **Jurisdicciones de registro** y **dónde haces valer derechos** de `## Perfil de práctica de PI` y `## Postura de enforcement` (jurisdicciones por defecto si el usuario no especifica).
- **Integraciones** de `## Integraciones disponibles` (LegalDataHunter / Solve Intelligence — cada una determina qué búsquedas están disponibles, cuál es la alternativa, y qué se atribuye en el resultado).
- **Postura de decisión** de `## Postura de decisión en juicios jurídicos subjetivos` — este skill nunca concluye "no confusamente similar."

Si `PROFILE` contiene `[PLACEHOLDER]` o `[Tu Empresa]`, mostrar este rebote:

> Noto que no has configurado tu perfil de práctica todavía — es como calibro postura, jurisdicciones y cadena de aprobación a tu práctica.
>
> **Dos opciones:**
> - Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` (2 minutos) para configurar tu perfil, luego corro esto calibrado a TU práctica.
> - Di **"provisional"** y lo corro con valores por defecto genéricos — jurisdicción México, apetito de riesgo medio, rol abogado, sin playbook — y marco cada resultado `[PROVISIONAL — configura tu perfil para resultados calibrados]` para que veas lo que hago antes de comprometerte.

### Modo provisional

Si el usuario dice "provisional," correr la búsqueda normalmente con estos defaults genéricos: apetito de riesgo medio, rol abogado, jurisdicción México (IMPI + uso común), sin playbook (hacer el análisis completo en vez de comparar contra una lista de posiciones). Marcar la nota del revisor y cada bloque de hallazgos con `[PROVISIONAL]`. Al final del resultado, agregar:

> "Esa fue una corrida genérica contra supuestos por defecto. Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` para obtener resultados calibrados a TU práctica — tu playbook, tu jurisdicción, tu apetito de riesgo. 2 minutos."

---

## Toma de datos

Preguntar una vez, en un solo lote (no alargar un trabajo rápido):

> Unas preguntas antes de correr el triaje:
>
> 1. **Marca propuesta.** Escritura exacta, cualquier estilización, y si es marca nominativa, innominada (diseño), mixta o tridimensional.
> 2. **Productos o servicios.** Qué se vende u ofrece realmente bajo esta marca. Un par de oraciones — yo mapeo a clases internacionales.
> 3. **Clases.** Si ya conoces las clases de Niza, listarlas. Si no, describe los productos/servicios y yo sugiero las clases probables y confirmo contigo antes de correr la búsqueda.
> 4. **Jurisdicciones.** ¿Dónde planeas usar, registrar o hacer valer? (México / Madrid / EUIPO / USPTO / países específicos — usaré el default de `Jurisdicciones de registro` de tu perfil de práctica si no dices.)
> 5. **Cómo aparecerá en uso.** ¿Algún tagline, nombre de producto adyacente, trade dress o elemento de diseño que acompañe la marca en el mercado?

Esperar la respuesta. Si la descripción es vaga ("herramienta de IA," "plataforma"), empujar una vez:

> Dame la cosa real que ve el cliente — ¿es una app móvil de consumo, una API empresarial, un producto físico, un servicio profesional? Las clases dependen de esto.

### ¿Marca o aviso comercial?

Si la marca propuesta es claramente un eslogan, frase publicitaria o lema comercial, señalar:

> Lo que describes parece un **eslogan/lema**, no una marca denominativa. En México, los eslóganes se protegen como **avisos comerciales** (no como marcas) — tienen vigencia de 10 años, se tramitan ante IMPI con requisitos similares pero expediente separado. ¿Quieres que corra la búsqueda como aviso comercial, como marca, o ambos?

Si el usuario confirma aviso comercial, ajustar la búsqueda para barrer tanto el registro de marcas como el de avisos comerciales. La declaración de uso real puede alcanzar avisos comerciales conforme al artículo 233 y al régimen transitorio; los otorgados antes del 10 de agosto de 2018 tienen tratamiento distinto. Aplicar `MX-LFPPI-MARK-USE-DECLARATION-001`, no una regla universal sin fecha.

---

## Verificación eliminatoria

Antes de cualquier búsqueda en bases de datos, correr los problemas intrínsecos
que matan una marca independientemente de registros previos. Para cada uno,
evaluar directamente y señalar. No racionalizar un problema evidente.

| Impedimento | Qué significa | Señalar cuando |
|---|---|---|
| **Genérico** | El término ES la categoría (ej., "Jabón" para jabón) | La marca nombra lo que es el producto |
| **Descriptivo sin distintividad adquirida** | Describe directamente una característica, función, cualidad o ingrediente | El consumidor lee la marca y sabe qué hace el producto sin imaginación — y no hay evidencia de distintividad adquirida (secondary meaning) |
| **Forma funcional o usual** | Forma tridimensional esencial para el uso, determinada por la naturaleza del producto o que le da ventaja funcional | Marca tridimensional — recuperar y aplicar la fracción exacta del art. 173 antes de concluir `[verify]` |
| **Contrario al orden público o buenas costumbres** | La marca contiene elementos ofensivos, violentos, discriminatorios | La marca sería rechazada por razones de moralidad pública |
| **Banderas, escudos, emblemas oficiales sin autorización** | Signos oficiales de México o de cualquier Estado, escudos municipales, emblemas de organizaciones internacionales | La marca contiene o imita un signo oficial; recuperar la fracción, excepción y autorización aplicables `[verify]` |
| **Denominación de origen / indicación geográfica protegida** | Nombres protegidos e indicaciones geográficas reconocidas por IMPI | El signo es idéntico o semejante en grado de confusión y los productos/servicios solicitados son idénticos o similares a los vinculados o protegidos; aplicar art. 173, fr. XI, no un bloqueo automático en todas las clases (`MX-LFPPI-MARK-REFUSALS-001`) |
| **Nombre de persona viva sin consentimiento** | No se puede registrar el nombre, seudónimo o imagen de una persona sin su consentimiento | La marca es o incluye el nombre o imagen de una persona identificable viva |
| **Título/nombre relacionado con obra o reserva (INDAUTOR)** | Posible cruce LFDA-LFPPI | Recuperar la fracción vigente y comprobar la reserva/titularidad; no tratar toda coincidencia como impedimento `[verify]` |
| **Falsa indicación de procedencia** | La marca sugiere un origen geográfico que los productos no tienen | La marca indica un lugar de origen y los productos no provienen de ahí, y el origen sería material para el consumidor |
| **Marca notoria o famosa** | Marcas con protección ampliada bajo los supuestos expresos del art. 173 | Para cualquier producto o servicio: en notoriedad, verificar además confusión/asociación, aprovechamiento, desprestigio o dilución de la fr. XVI; en fama, aplicar fr. XVII (`MX-LFPPI-MARK-REFUSALS-001`) |

**Nota sobre impedimentos intrínsecos en México vs. EE.UU.** Los impedimentos
intrínsecos mexicanos se fundamentan en la LFPPI (no en el §2 del Lanham Act).
Diferencias clave:

- México protege **denominaciones de origen/indicaciones geográficas** mediante
  la fr. XI, pero el texto vigente vincula el impedimento a productos o
  servicios idénticos o similares; no describirlo como absoluto en todas las
  clases.
- México tiene el impedimento de **títulos de obras y personajes amparados por reserva de derechos** (cruce LFDA-LFPPI sin equivalente directo en EE.UU.).
- La reforma 2026 añadió al art. 386, fr. II, inc. e), un supuesto de confusión
  sobre patrocinio oficial de eventos masivos. Es un análisis de infracción y
  competencia desleal, **no** un impedimento autónomo de registro ni una regla
  general de “anti-ambush marketing” (`MX-LFPPI-EVENT-SPONSORSHIP-001`).
- México NO tiene los impedimentos de "primarily merely a surname" ni "false connection" como categorías independientes de la ley estadounidense. Los nombres de personas se tratan bajo la fracción específica de la LFPPI que requiere consentimiento.

Las fracciones del artículo 173 deben cotejarse con el texto vigente al emitir
un dictamen. Usar `MX-LFPPI-MARK-REFUSALS-001` como punto de partida, pero citar
la fracción exacta y su fuente primaria en el entregable.

**Resultado:** para cada categoría de impedimento, "sin problema identificado" o
una señal específica con razón de una línea. No producir una tabla en blanco de
aprobaciones.

---

## Búsqueda de marcas similares

El propósito aquí es **encontrar marcas previas potencialmente confusamente
similares**, no decidir si la confusión es probable. Eso es criterio del abogado.

### Qué capacidad está verificada ahora

Leer el registro de capacidades y tratar `PROFILE` solo como historial. Antes de
usar un conector, ejecutar una prueba mínima de solo lectura en esta sesión:

- **Si una herramienta expone explícitamente búsqueda de registro de marcas y
  la prueba tuvo éxito:** correr una
  búsqueda preliminar en las clases y jurisdicciones relevantes. Atribuir cada
  resultado a su fuente. Anotar la fecha de la búsqueda y el alcance (cuáles
  registros, cuáles clases, exacta vs. difusa, búsqueda de diseño o no).
- **Si LegalDataHunter u otro conector jurídico fue probado:** puede buscar
  jurisprudencia/documentos; no presentarlo como búsqueda del registro de
  marcas salvo que esa capacidad concreta se verificó. Barrer por disputas
  que involucren la marca o una variante cercana. Misma regla de atribución.
- **Si no hay capacidad registral verificada:** decirlo, explícitamente, en el
  resultado. No inferir resultados de conocimiento del modelo y presentarlos
  como hallazgos de búsqueda.

### Alternativa cuando no hay acceso a bases de datos

Escribir, en el resultado, esta declaración exacta:

> **No se corrió búsqueda en bases de datos.** Este triaje no consultó Marcanet,
> MARCia, Solve Intelligence, LegalDataHunter, registros estatales de nombre
> comercial, Madrid/OMPI, INDAUTOR (reservas de derechos), NIC México (dominios
> .mx), ni fuentes de uso común / marcas no registradas. Una búsqueda
> eliminatoria o completa en esas bases de datos es obligatoria antes de
> cualquier conclusión sobre disponibilidad. El triaje abajo se limita al
> análisis de impedimentos intrínsecos y factores de similitud estructurados
> contra marcas que el usuario haya identificado o que surjan en la conversación.

Luego proceder — las verificaciones intrínsecas y el análisis de similitud
siguen siendo útiles, solo etiquetados honestamente.

### Para cada marca similar encontrada (o proporcionada)

Capturar:

- **Marca** (caracteres exactos, cualquier estilización)
- **Fuente** (número de registro IMPI, designación Madrid, registro estatal,
  cita de resolución, dominio, red social — lo que aplique)
- **Clases / descripción de productos-servicios** del registro
- **Titular**
- **Estatus** (registrada / en trámite / caducada / cancelada / nula — una marca
  caducada o cancelada no es impedimento directo pero puede ser relevante para
  notoriedad y derechos del predecesor)
- **Fecha de primer uso si está disponible**

**No suplementar en silencio.** Si citas un número de registro IMPI, provino de
la búsqueda que corriste; si describes una marca que el usuario mencionó, decirlo.
Nunca inventar un registro y nunca "completar" un dato que el expediente no
respalda. Si la búsqueda no devolvió una fecha de primer uso, escribir "fecha de
primer uso no disponible en el resultado de búsqueda" — no adivinar.

### Barrido de familias adyacentes (obligatorio antes de concluir)

Una búsqueda de disponibilidad que solo verifica coincidencias exactas y
casi-exactas pierde las marcas que un competidor adoptó *porque* la tuya estaba
tomada. Antes de concluir, identificar 3–5 familias de palabras adyacentes que
el practicante también debería barrer, y pedir al usuario que confirme o agregue
a la lista.

Las familias adyacentes son sustitutos convencionalmente aceptados en la
categoría que un competidor razonable consideraría cuando la marca directa no
está disponible. Para una marca como `NEXUS HOME` en el espacio de hogares
inteligentes, las familias adyacentes incluyen como mínimo:

- **Sinónimos de categoría** para NEXUS: `HUB`, `NEST`, `CORE`, `LINK`,
  `CONNECT`, `BRIDGE`, `CENTRAL`, `GATEWAY`.
- **Nombres tipo asistente** en la misma categoría de producto: `ALEXA`, `ECHO`,
  `SIRI`, `GOOGLE HOME`, `CORTANA`, `HOMEY`, `HOMEBASE`.
- **Variantes HOME / CASA / HOGAR / SMART**: `SMART HOME`, `HOUSEHOLD`,
  `HOUSE`, `ABODE`, `CASA`, `DOM`, `HOGAR`.
- **Gemelos fonéticos** de la raíz: `NEXIS`, `NEKSUS`, `NEXXUS`, `NECTIS`,
  `KNOXUS` (según cómo se posicione la palabra en el mercado).

El skill debe producir un bloque de familias adyacentes en la sección de
Marcas Similares con una solicitud de confirmación:

> **Familias adyacentes a barrer (por favor confirmar o agregar):**
>
> - [familia 1 — ej., HUB / NEST / LINK / CONNECT / BRIDGE / GATEWAY]
> - [familia 2 — ej., nombres tipo asistente]
> - [familia 3 — ej., HOME / CASA / HOGAR / SMART variants]
> - [familia 4 — gemelos fonéticos de la raíz]
>
> Una búsqueda de disponibilidad que solo verifica coincidencias exactas y
> casi-exactas pierde las marcas que un competidor adoptó porque la tuya estaba
> tomada. Confirmar que esta lista está completa para la categoría antes de
> continuar.

> **Equivalentes de traducción español↔inglés (OBLIGATORIO cuando México está en
> alcance).** El barrido solo en un idioma pierde la fuente más común de conflictos
> transfronterizos en México. Agregar:
> - **Equivalentes de traducción.** La marca traducida al otro idioma (español→inglés y viceversa). El criterio del IMPI y la jurisprudencia consideran la traducción como la misma marca para efectos de confusión.
> - **Transliteración.** La marca escrita en el otro alfabeto si aplica (marcas en chino/japonés/coreano/árabe para productos importados a México).
> - **Variaciones fonéticas entre idiomas.** Marcas registradas en español que suenan como la marca propuesta en inglés, y viceversa.
>
> Si no puedes realizar el análisis inter-idiomas, decirlo: "Análisis fonético y de equivalentes de traducción español↔inglés no realizado — esta es la fuente más común de conflictos transfronterizos en México. Una búsqueda de disponibilidad completa debe incluirlo."

Si el practicante tiene una herramienta de búsqueda de marcas conectada,
re-correr el barrido contra cada familia adyacente confirmada (exacta + fonética
+ equivalente de traducción donde aplique) y agregar los resultados a la tabla
de Marcas Similares con la fuente `Familia adyacente` anotada. Si no hay
conector disponible, decirlo, y listar las familias como entrada explícita para
el siguiente paso de búsqueda profesional completa — no saltar el barrido en
silencio.

### Búsqueda cruzada INDAUTOR

**Obligatoria cuando la marca propuesta podría coincidir con un título de obra o nombre de personaje.** Verificar si existe una reserva de derechos al uso exclusivo vigente ante INDAUTOR que cubra el nombre propuesto. Si LegalDataHunter está conectado, barrer. Si no, señalar explícitamente: "No se verificaron reservas de derechos vigentes ante INDAUTOR — verificar en el portal de INDAUTOR antes de adoptar."

### Búsqueda de dominios

Verificar disponibilidad de dominios `.mx` y `.com.mx` relevantes vía NIC México. Un dominio existente con el nombre propuesto no es impedimento registral pero informa la estrategia de adopción y puede indicar uso previo por un tercero.

---

## Análisis de similitud — marco mexicano

> **El marco de confusión es específico de cada jurisdicción.** México, EE.UU. y la UE evalúan el riesgo de confusión de forma diferente. No aplicar el marco equivocado.
>
> - **México (IMPI / LFPPI):** Comparar similitud fonética, gráfica e ideológica,
>   productos/servicios y contexto pertinente como ejes de investigación. No
>   presentarlos como test cerrado u obligatorio hasta recuperar el criterio
>   mexicano aplicable; no importar factores estadounidenses `[verify]`.
> - **EE.UU. (circuitos federales):** Tests multi-factor (*du Pont*, *Polaroid*, *Sleekcraft*) — fuerza de la marca, similitud (sight/sound/meaning), proximidad de productos, canales, sofisticación del comprador, confusión actual, intención.
> - **UE (Art. 8(1)(b) RMUE):** Apreciación global — todos los factores relevantes evaluados holísticamente a través de los ojos del consumidor medio. Mayor peso a similitud fonética; equivalentes de traducción como estándar; "riesgo de asociación" más allá de confusión de origen.
> - **Otras jurisdicciones:** Si la toma de datos incluye una jurisdicción sin marco arriba, decir: "No tengo el marco de confusión de [jurisdicción]. Aplicar el criterio mexicano daría una respuesta incorrecta que parece correcta. Opciones: (a) busco el estándar aplicable, (b) lo enrutas a un especialista en [jurisdicción], (c) noto que esta jurisdicción está fuera de alcance." Nunca aplicar silenciosamente doctrina mexicana.

### Ejes del análisis de similitud mexicano

Para cada eje, producir una **señal**, no un veredicto. Cada eje debe decir qué
apunta en cada dirección y dónde está la incertidumbre:

- **Similitud fonética.** ¿Cómo suenan las marcas al pronunciarlas? Estructura
  silábica, acento, sonidos dominantes y de cierre. Considerar pronunciación en
  español Y en inglés si el mercado relevante incluye consumidores bilingües.
- **Similitud gráfica.** ¿Cómo se ven al compararlas visualmente? Longitud de
  la palabra, letras compartidas, disposición visual, elementos de diseño (si
  aplica). Para marcas mixtas o innominadas: composición visual, colores,
  elementos figurativos.
- **Similitud ideológica (conceptual).** ¿Evocan la misma idea, concepto o
  imagen mental? Significado de las palabras, asociaciones conceptuales,
  impresión comercial. Incluye equivalentes de traducción entre idiomas.
- **Similitud de productos/servicios.** No si los productos son idénticos —
  sino si el consumidor esperaría que provienen de la misma fuente. Misma
  clase de Niza no significa automáticamente similitud; clases diferentes no
  significa automáticamente disimilitud.
- **Canales de comercialización y consumidor relevante.** ¿Se venden en los
  mismos establecimientos? ¿A través de los mismos medios? ¿Al mismo perfil
  de consumidor? Un consumidor especializado (industrial, profesional) tiene
  mayor grado de atención que un consumidor general.
- **Distintividad de la marca anterior.** ¿Es la marca anterior arbitraria,
  fantasiosa, sugestiva o descriptiva con distintividad adquirida? Mayor
  distintividad = mayor protección = mayor riesgo de confusión.
- **Notoriedad / renombre.** ¿La marca anterior ha sido declarada notoria o
  famosa por IMPI? Las fracciones XVI y XVII del artículo 173 pueden operar
  para cualquier producto o servicio; en notoriedad, comprobar además al menos
  uno de los efectos enumerados por la fracción XVI. No resumir el análisis por
  clase de Niza. `MX-LFPPI-MARK-REFUSALS-001`

Conforme a la postura de decisión en `PROFILE`:

- **Nunca concluir "no confusamente similar."**
- Si hay duda, escribir: "Marcas similares encontradas — evaluación de confusión
  requerida antes de adopción." O: "Los ejes apuntan en ambas direcciones;
  criterio de abogado requerido."
- Solo hay espacio para "no se encontraron marcas similares en las bases de
  datos consultadas" si se corrió una búsqueda real; ver la alternativa de
  sin-búsqueda arriba en caso contrario.

---

## Siguientes pasos recomendados

Cada resultado de disponibilidad cierra con siguientes pasos concretos,
agrupados por lo que el triaje encontró:

- **Si se encontraron impedimentos eliminatorios:** reformular la marca, o
  aceptar el impedimento descriptivo y planear para distintividad adquirida a
  lo largo del tiempo; enrutar a revisión de abogado antes de adoptar.
- **Si se encontraron marcas similares en las bases de datos consultadas:**
  revisión de abogado obligatoria antes de adoptar, solicitar o comercializar.
  Frecuentemente el siguiente paso es una búsqueda profesional completa para
  encontrar todo lo que el triaje perdió.
- **Si no se encontraron marcas similares pero no se corrió búsqueda en bases
  de datos:** búsqueda completa obligatoria antes de adopción. Nombrar las bases
  de datos que necesitan consultarse.
- **Si se encontraron marcas similares y la marca anterior es débil, antigua, en
  clase diferente, o caducada:** señalar para revisión de abogado — el triaje no
  hará esta determinación.
- **Siempre:** opinión de disponibilidad completa por un abogado titulado
  especialista en marcas, escalada al tamaño de la inversión que llevará la
  marca. Una marca que vas a poner en una línea de productos y una campaña
  nacional tiene más peso que una marca para un evento único.

**Enrutamiento a otros skills (cuando aplique):**

- Conflicto encontrado, el abogado quiere defender → `/propiedad-intelectual-legal-mexico:triaje-infraccion`
- Se abre camino de solicitud → `/propiedad-intelectual-legal-mexico:portafolio --agregar`
- Titular de marca anterior parece ser infractor de la tuya → `/propiedad-intelectual-legal-mexico:carta-requerimiento`
- Reserva de derechos necesaria en vez de (o además de) marca → `/propiedad-intelectual-legal-mexico:reservas-derechos`
- Cláusula de PI en contrato más amplio → `/corporativo-legal-mexico:revision-contratos` (si instalado)

---

## Formato del resultado

Anteponer el encabezado de confidencialidad de `PROFILE` → `## Resultados`.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

⚠️ Nota del revisor
- **Fuentes:** [Conector de investigación: LegalDataHunter ✓ verificado | Solve Intelligence ✓ | no conectado — citas de conocimiento del modelo, verificar antes de confiar]
- **Leído:** [N/A — búsqueda de disponibilidad]
- **Marcado para tu criterio:** [N elementos marcados `[review]` en línea | ninguno]
- **Vigencia:** [se buscaron novedades desde [fecha] — nada encontrado | no fue posible buscar, verificar contra LFPPI vigente]
- **Antes de confiar:** [las 1-2 cosas que el revisor debe hacer]

# Búsqueda de Disponibilidad de Marca — Primer Pase (NO ES UNA OPINIÓN)

**Esto es un primer pase, no una opinión de disponibilidad.** Una opinión de
disponibilidad requiere una búsqueda profesional completa y criterio de un
abogado titulado. Un resultado de "sin conflictos evidentes" aquí significa que
el triaje no encontró nada — no que la marca esté libre. Un abogado titulado
especialista en marcas evalúa antes de que alguien adopte, solicite o invierta
en esta marca.

**Resultado del triaje:** [🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo — una oración de por qué]

## Marca propuesta

- **Marca:** [texto exacto, estilización anotada]
- **Tipo de marca:** [nominativa / innominada / mixta / tridimensional]
- **Productos / servicios:** [descripción]
- **Clases:** [números de clase de Niza con descripciones de una línea]
- **Jurisdicciones:** [México / Madrid / EUIPO / USPTO / países específicos]
- **Marco de análisis aplicado:** [Similitud fonética/gráfica/ideológica — marco IMPI/LFPPI, con razón de por qué es el correcto]

## Impedimentos eliminatorios

| Impedimento | Señal | Nota |
|---|---|---|
| Genérico / descriptivo / forma funcional / contrario al orden público / banderas y escudos / denominación de origen / nombre sin consentimiento / reserva de derechos / falsa procedencia / marca notoria-famosa / anti-ambush | [ninguna / señalada] | [una línea si señalada] |

## Búsqueda de marcas similares

**Fuentes consultadas:** [registros y bases de datos consultadas, con fechas — o "no se corrió búsqueda en bases de datos; ver nota de alcance abajo."]
**Alcance:** [clases, jurisdicciones, exacta-vs-difusa, búsqueda de diseño o no]

**Familias adyacentes barridas (confirmadas con el usuario):**
- [familia 1 — ej., HUB / NEST / LINK / CONNECT / BRIDGE / GATEWAY]
- [familia 2 — ej., nombres tipo asistente]
- [familia 3 — ej., CASA / HOGAR / HOME / SMART variantes]
- [familia 4 — gemelos fonéticos de la raíz]
- [familia 5 — equivalentes de traducción español↔inglés]

*Una búsqueda de disponibilidad que solo verifica coincidencias exactas y
casi-exactas pierde las marcas que un competidor adoptó porque la tuya estaba
tomada. Si alguna familia no fue barrida (sin conector, sin tiempo), se lista
explícitamente como entrada para la búsqueda profesional completa — no se salta
en silencio.*

| Marca | Fuente | Clases / P&S | Titular | Estatus | Primer uso | Nota |
|---|---|---|---|---|---|---|
| [exacta] | [no. registro / cita / URL] | [lista de clases] | [titular del registro] | [registrada/en trámite/caducada/cancelada/nula] | [fecha o "no disponible"] | [por qué importa — coincidencia exacta / familia adyacente / traducción] |

*Si no se corrió búsqueda:* **No se corrió búsqueda en bases de datos.** Este
triaje no consultó Marcanet, MARCia, Solve Intelligence, LegalDataHunter,
registros de nombre comercial, Madrid/OMPI, INDAUTOR (reservas), NIC México
(dominios .mx), ni fuentes de uso común / marcas no registradas. Una búsqueda
eliminatoria o completa en esas bases de datos es obligatoria antes de cualquier
conclusión sobre disponibilidad.

## Análisis de similitud — señales para revisión de abogado

Para cada eje del marco aplicado, una señal de una línea indicando qué apunta en
cada dirección.

| Eje | Señal | Dirección |
|---|---|---|
| Similitud fonética | [nota] | [apunta a conflicto / apunta contra / mixta] |
| Similitud gráfica | [nota] | [dirección] |
| Similitud ideológica (conceptual) | [nota] | [dirección] |
| Similitud de productos/servicios | [nota] | [dirección] |
| Canales de comercialización / consumidor relevante | [nota] | [dirección] |
| Distintividad de la marca anterior | [nota] | [dirección] |
| Notoriedad / renombre | [nota o "sin evidencia de declaración de notoriedad"] | [dirección] |

**Conclusión sobre confusión:** *Este skill no concluye.* Alguna de:
- "Marcas similares encontradas; evaluación de confusión por abogado requerida antes de adopción."
- "No se encontraron marcas similares en las bases de datos consultadas; búsqueda completa requerida antes de adopción."
- "Los ejes apuntan en ambas direcciones; criterio de abogado requerido."

## Siguientes pasos recomendados

- [siguiente paso específico 1 — ej., "Búsqueda profesional completa en Marcanet, MARCia, registros de nombre comercial, INDAUTOR (reservas), NIC México, y Madrid Monitor antes de adopción"]
- [siguiente paso específico 2 — ej., "Evaluar rediseño de la marca `APEXLEAF` en Clase 25 si la intención es continuar"]
- [siguiente paso específico 3 — ej., "Reformular la marca — la forma actual es descriptiva y requerirá distintividad adquirida"]
- [enrutamiento conforme a `PROFILE` — abogado de marcas o despacho externo nombrado en el perfil de práctica]

## Verificación de citas

Cada resolución, número de registro, disposición legal y resultado de base de
datos en este memorándum debe verificarse contra la fuente autoritativa antes de
confiar en él. Los números de registro, designaciones de clase y fechas de
primer uso son los sitios más comunes de error. No citar un resultado que no
puedas abrir.
```

---

## Compuerta de no abogado

Antes de emitir el resultado, leer `## Quién usa este plugin`. Si el Rol es No abogado:

> Este resultado es un triaje de investigación, no asesoría legal. Adoptar,
> solicitar o invertir en esta marca basándose solo en este triaje tiene
> consecuencias jurídicas — incluyendo ser demandado por infracción sobre una
> marca que "pasó" esta verificación. Un abogado titulado especialista en marcas
> necesita evaluar antes de avanzar.
>
> Aquí tienes un resumen para llevar a un abogado — reducirá el tiempo que toma
> la conversación:
>
> [Generar resumen de 1 página: la marca propuesta, los productos/servicios y
> clases, los impedimentos eliminatorios (si los hay), las marcas similares
> encontradas (si las hay), qué se buscó y qué no, y las tres preguntas para
> hacer al abogado.]
>
> Si necesitas encontrar un abogado titulado con cédula profesional
> especializado en propiedad intelectual: la Barra Mexicana Colegio de
> Abogados, AMPPI (Asociación Mexicana para la Protección de la Propiedad
> Intelectual), AIPPI México, o ANADE (Asociación Nacional de Abogados de
> Empresa) pueden ser puntos de partida solo después de verificar sus
> directorios y datos actuales.

Entregar el memorándum de triaje completo junto con el resumen. No retener el
análisis.

---

## Ubicación del resultado

Si los espacios de trabajo por asunto están habilitados y hay un asunto activo,
escribir el resultado en
`DATA_ROOT/outputs/clearance-<marca-slug>-AAAA-MM-DD.md`.
De lo contrario escribir en
`DATA_ROOT/outputs/clearance-<marca-slug>-AAAA-MM-DD.md`
y mostrar la ruta al usuario.

Agregar una entrada de una línea al `history.md` del asunto si hay un asunto
activo.

---

## Cierre con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más información, observar y esperar, algo diferente) son un punto de partida, no una camisa de fuerza. El árbol es el resultado; el abogado elige.

## Lo que este skill NO hace

- **Concluir que una marca está libre.** Nunca. La guardia más fuerte del plugin.
- **Sustituir una búsqueda en Marcanet, MARCia, registros de nombre comercial,
  INDAUTOR, NIC México, Madrid/OMPI, o fuentes de uso común / marcas no
  registradas.**
- **Presentar una solicitud de marca ante IMPI.** La solicitud es tarea del
  abogado; este skill informa la decisión de solicitar.
- **Evaluar trade dress, dilución de marca o reclamaciones de marca famosa**
  más allá de una señal preliminar. La protección ampliada de marcas notorias y
  famosas requiere un análisis de renombre que este skill no intenta.
- **Abordar impedimentos específicos de jurisdicción extranjera** (ej.,
  estándares de similitud fonética en Japón, doctrina de equivalentes de
  traducción en la UE) más allá de señalar que se requiere análisis extranjero
  cuando una jurisdicción fuera de México está en alcance.
- **Citar resultados a clientes, contrapartes o medios.** Esto es investigación
  interna. Protegida por secreto profesional si aplica el encabezado del inicio.

---

## Tono

Concreto, directo, honesto sobre el alcance. El abogado que lee este resultado
debe saber en diez segundos qué encontró el triaje, qué no encontró, y qué
tiene que pasar antes de que alguien adopte la marca. Sin prosa evasiva. La
guardia al inicio y la línea de "este skill no concluye" sobre confusión hacen
el trabajo de delimitar el alcance.
