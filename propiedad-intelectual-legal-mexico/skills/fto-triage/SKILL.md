---
description: >
  Triaje de libertad de operación (Freedom to Operate) — una primera lectura
  estructurada de patentes y modelos de utilidad potencialmente bloqueantes, no
  un dictamen de FTO. Usa cuando un producto, proceso o característica se está
  evaluando por patentes bloqueantes, cuando preguntan si algo impide un
  lanzamiento, o para construir un primer chart de reivindicaciones contra las
  patentes más plausibles antes de revisión por abogado de patentes.
  Este skill nunca concluye que un producto está libre para lanzar.
---

# /fto-triage

**Esto no es un dictamen de libertad de operación.** Un dictamen formal de FTO
requiere una búsqueda exhaustiva, construcción completa de reivindicaciones, y
análisis elemento por elemento de infracción por un abogado de patentes
calificado. La LFPPI exige analizar los actos concretos, la fracción de
infracción invocada y los remedios disponibles; este skill no presume una
categoría automática de responsabilidad ni un efecto jurídico por conocimiento
previo. Un resultado de "no se encontraron patentes bloqueantes obvias" en este triaje
significa que el triaje no encontró una — no significa que el producto esté
libre.

## Instrucciones

1. Ejecutar `matter_workspace.py status` y leer `PROFILE`. Si
   contiene `[PLACEHOLDER]`, detenerse y dirigir a `/propiedad-intelectual-legal-mexico:cold-start-interview`.
2. Seguir el flujo de trabajo abajo.
3. Ejecutar intake (producto/proceso, detalle técnico, jurisdicciones, patentes
   conocidas, timing).
4. Ejecutar una búsqueda preliminar solo si una herramienta de investigación de
   patentes se descubre y supera una prueba mínima de solo lectura en esta
   ejecución (Solve Intelligence u otro MCP). De lo
   contrario, decirlo en el resultado y proceder con las patentes que el
   usuario haya proporcionado.
5. Para las 2–5 patentes más plausibles, construir un primer chart de
   reivindicaciones contra cada reivindicación independiente — elemento por
   elemento. Lectura literal primero; señalar equivalentes por separado;
   señalar infracción indirecta / dividida.
6. Listar preguntas abiertas que un estudio formal de FTO resolvería
   (ejecutabilidad, historial de trámite, nulidades, disponibilidad de
   licencia, historial de enforcement del titular).
7. Escribir el memorándum de triaje en la carpeta del asunto o carpeta de
   resultados de la práctica. Aplicar el encabezado de confidencialidad
   conforme al rol.
8. Cerrar con siguientes pasos recomendados, una nota de gobernanza sobre las
   patentes identificadas (preservar el análisis, no ocultar ni destruir
   información y obtener revisión jurídica antes de decidir), y la puerta para
   no abogados si el rol es no abogado. No atribuir al conocimiento un efecto
   automático sobre infracción, sanciones o daños sin fuente y análisis del
   caso.

Este skill nunca concluye que un producto está libre para lanzar. Si hay
incertidumbre, señalar — el abogado de patentes decide.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:fto-triage "un modelo de reconocimiento de voz on-device para wearables, lanzamiento en México primero"
```

```
/propiedad-intelectual-legal-mexico:fto-triage
```

---

## ESTO NO ES UN DICTAMEN DE LIBERTAD DE OPERACIÓN

**La salvaguarda más fuerte del plugin. Decir esto al inicio de cada resultado.
No omitirla. No suavizarla. No dejar que el lector la pase de largo.**

> **Esto no es un dictamen de libertad de operación.** Un dictamen de FTO es un
> juicio profesional jurídico, usualmente por un abogado de patentes calificado,
> basado en una búsqueda exhaustiva, construcción completa de reivindicaciones, y
> un análisis elemento por elemento de infracción contra cada reivindicación de
> cada patente relevante. Este triaje es una primera lectura estructurada de lo
> que podría estar afuera. Un resultado de "no se encontraron patentes
> bloqueantes obvias" significa que el triaje no encontró una — no significa que
> el producto esté libre. Evaluar los actos concretos del artículo 55, las
> limitaciones del artículo 57, la fracción aplicable del artículo 386 y los
> elementos/remedios de la vía elegida; no resumir el régimen como
> “responsabilidad objetiva” ni asignar efectos automáticos al conocimiento sin
> fuente verificada. La decisión de lanzar, fabricar, usar, vender o importar es una
> decisión de negocio informada por un estudio formal de FTO y el juicio del
> abogado — no por este triaje. Un abogado de patentes calificado evalúa antes
> de que alguien se apoye en esto para una decisión de producto.

Sub-señalar una patente bloqueante es una puerta de un solo sentido — un
producto lanzado, una inspección del IMPI un año después, daños y perjuicios
sobre la mesa. Sobre-señalar es una puerta de dos sentidos — el abogado reduce
la lista en una lectura. Mantenerse del lado de la puerta de dos sentidos.
Siempre.

### Una nota sobre conocimiento previo de patentes

Leer este triaje revela patentes que deben evaluarse y conservarse dentro del
flujo jurídico de la organización. No afirmar que ese conocimiento produce por
sí solo dolo, agrava una multa o aumenta daños: la consecuencia depende de la
pretensión, sus elementos, la evidencia y las normas aplicables. El resultado se
marca como confidencial cuando un abogado lo está usando, y el resultado para no
abogados se enmarca como investigación para llevar al abogado. No discutir las
patentes específicas fuera de los canales autorizados ni alterar o destruir el
registro del análisis.

---

## Contexto de asunto

**Contexto de asunto.** Usar exclusivamente el `DATA_ROOT` devuelto por el resolver. Si los asuntos están habilitados y no hay activo, preguntar si debe cambiarse a uno o trabajar a nivel de práctica. Cargar `DATA_ROOT/matter.md` solo cuando `active` tenga slug. Escribir en `DATA_ROOT/outputs/`; nunca construir ni leer otra ruta de `matters/`.

Los asuntos de FTO de patentes son particularmente candidatos comunes para
confidencialidad **reforzada** al abrir el asunto. Respetar la marca de
confidencialidad del asunto en `matter.md`.

---

## Cargar el perfil de práctica primero

Antes de ejecutar el triaje, leer `PROFILE`. Extraer:

- **Rol** de `## Quién usa este plugin` (abogado vs. no abogado cambia el
  encabezado de confidencialidad y la puerta para no abogados abajo).
- **Jurisdicciones de registro** y **postura de enforcement** de `## Perfil de
  práctica de PI` y `## Postura de enforcement` (útil para verificación cruzada
  de portafolio defensivo y para defaults de jurisdicción).
- **Despacho externo de patentes** de `## Perfil de práctica de PI` →
  `Despacho externo / corresponsales` para el paso de enrutamiento.
- **Integraciones** de `## Integraciones disponibles` — específicamente Solve
  Intelligence, o cualquier MCP de investigación de patentes. Determina qué
  búsquedas están disponibles.
- **Postura de decisión** de `## Postura de decisión en juicios jurídicos
  subjetivos` — este skill nunca concluye "no infringe."

Si `PROFILE` contiene `[PLACEHOLDER]`, mostrar este rebote:

> Noto que no has configurado tu perfil de práctica aún — así es como calibro
> postura, jurisdicciones y cadena de aprobación a tu práctica.
>
> **Dos opciones:**
> - Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` (2 minutos) para configurar tu perfil, luego ejecutaré esto calibrado a TU práctica.
> - Di **"provisional"** y lo ejecutaré contra valores genéricos por defecto — jurisdicción México, apetito de riesgo medio, rol de abogado, sin playbook — y marcaré cada resultado con `[PROVISIONAL — configura tu perfil para resultados calibrados]` para que veas lo que hago antes de comprometerte.

### Modo provisional

Si el usuario dice "provisional," ejecutar el triaje de FTO normalmente usando estos valores genéricos por defecto: apetito de riesgo medio, rol de abogado, jurisdicción México, sin playbook (hacer el análisis completo en lugar de comparar contra una lista de posiciones). Marcar la nota del revisor y cada bloque de hallazgos con `[PROVISIONAL]`. Al final del resultado, agregar:

> "Eso fue una ejecución genérica contra supuestos por defecto. Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` para obtener resultados calibrados a TU práctica — tu playbook, tu jurisdicción, tu apetito de riesgo. 2 minutos."

---

## Intake

Preguntar en un solo lote:

> Ejecutaré un triaje de FTO. Algunas preguntas primero:
>
> 1. **Producto, proceso o característica.** ¿Qué se está fabricando, usando,
>    ofreciendo en venta, vendiendo o importando? Describir llanamente — la
>    esencia técnica, no el pitch de marketing.
> 2. **Detalle técnico.** ¿Algún diagrama de arquitectura, especificaciones
>    relevantes a reivindicaciones, una página de producto pública, o un
>    documento de especificación que puedas compartir? (Entre más detalle, más
>    real el triaje.)
> 3. **Jurisdicciones.** ¿Dónde se fabricará, usará, venderá, ofrecerá en venta,
>    importará? (El art. 55 LFPPI enumera actos que la persona titular puede
>    impedir, con reglas distintas para producto y proceso; aplicar
>    MX-LFPPI-PATENT-RIGHTS-001. Por defecto asumiré México si no
>    especificas.)
> 4. **Patentes conocidas.** ¿Hay patentes ya en tu radar — portafolio de un
>    competidor, pool de patentes esenciales a estándar, carta de un NPE, algo
>    que mencionó un ingeniero?
> 5. **Timing.** ¿Qué tan cerca del lanzamiento está esto? Si faltan meses, el
>    triaje es temprano y el diseño alternativo está sobre la mesa. Si ya está
>    en el mercado, estamos en modo de cubrir el riesgo.

Esperar la respuesta. Si la descripción es vaga ("un agente de IA," "una base de datos"), insistir una vez:

> Dame la esencia técnica — ¿qué hace la cosa, cómo lo hace, y cuál es la
> parte que crees que podría ser novedosa? Las reivindicaciones de patente viven
> a ese nivel.

---

## Alcance — patentes de invención y modelos de utilidad

**Este skill analiza patentes de invención y modelos de utilidad.** Ambos tipos
de título otorgan derechos exclusivos ante IMPI pero tienen diferencias
sustanciales:

| Característica | Patente de invención | Modelo de utilidad |
|---|---|---|
| Vigencia | 20 años desde solicitud | 15 años desde solicitud |
| Requisito de actividad inventiva | Pleno | Reducido (menor nivel inventivo) |
| Examen de fondo | Completo | Simplificado |
| Tipos de invención | Productos y procesos | Solo objetos, utensilios, aparatos o herramientas (no procesos) |

**El triaje de FTO debe cubrir AMBOS tipos.** Un modelo de utilidad con
reivindicaciones amplias sobre un utensilio o dispositivo puede ser tan
bloqueante como una patente de invención. No asumir que solo las patentes son
relevantes.

Si una patente en el radar es un **diseño industrial**, señalarlo y enrutar,
no hacer chart:

- **Diseño industrial.** Prueba diferente — novedad y originalidad del aspecto
  ornamental, no análisis funcional de reivindicaciones. Enrutar al skill de
  `/propiedad-intelectual-legal-mexico:triaje-infraccion` en su rama de diseño
  industrial y al abogado de diseño industrial. **Los diseños industriales no
  se analizan en este triaje de FTO** — una sobreposición de diseño industrial
  debe señalarse como un flujo de trabajo separado.

También señalar como bandera cruzada **imagen comercial (trade dress)**: si la
apariencia del producto es el riesgo, los mismos hechos pueden ser una
posible infracción administrativa dentro del catálogo vigente del artículo 386
LFPPI (MX-LFPPI-INFRINGEMENT-REMEDIES-001); verificar la fracción aplicable.
Señalar como vía paralela.

**Variedades vegetales.** Si la invención involucra una variedad vegetal, enrutar
a la Ley Federal de Variedades Vegetales — fuera de alcance de este skill.

---

## Búsqueda

### Capacidad verificada en esta ejecución

Leer el registro de capacidades; `PROFILE` es historial, no prueba. Descubrir la
herramienta y ejecutar una consulta mínima no sensible antes de usarla:

- **Solve Intelligence `verified` ahora:** ejecutar una búsqueda preliminar sobre la
  descripción técnica. Anotar la fecha de la búsqueda, la consulta usada, las
  jurisdicciones cubiertas, y cualquier ventana de fecha (patentes vigentes;
  solicitudes publicadas recientemente).
- **Otro MCP personalizado:** usarlo solo si declara búsqueda de patentes y la
  prueba runtime fue exitosa; registrar herramienta y alcance.
- **Ninguno de los anteriores:** decirlo explícitamente. No inferir patentes
  del conocimiento del modelo y presentarlas como resultados de búsqueda.

### Alternativa cuando no hay base de datos de patentes conectada

Escribir esta declaración exacta en el resultado:

> **No se ejecutó búsqueda en base de datos de patentes.** Este triaje no
> consultó Solve Intelligence Patents, SIGA (IMPI), Espacenet, Google Patents,
> PatSnap, ni ningún otro corpus de patentes. Se requiere una búsqueda
> estructurada en las jurisdicciones en alcance antes de confiar en este triaje
> para cualquier decisión de lanzamiento. El análisis abajo se limita a patentes
> y solicitudes que el usuario nombró o que surgieron en la conversación.

Luego proceder. El trabajo de chart de reivindicaciones abajo sigue siendo
valioso — solo etiquetar el alcance honestamente.

### Señales complementarias (no sustituyen búsqueda)

Si están disponibles y el usuario lo permite, barrer señales no-patente que
indiquen una preocupación de patentes:

- **Solicitudes de patente de competidores** alrededor del área de producto.
- **NPEs conocidos atacando** la clase tecnológica.
- **Declaraciones de patentes esenciales a estándar** (IEEE, ETSI, 3GPP) si el
  producto toca un estándar relevante.
- **Litigio reportado** en el espacio tecnológico (procedimientos ante IMPI,
  juicios civiles/mercantiles, recursos ante TFJA).

Cada señal es una razón para buscar más fuerte, no un hit de patente. Marcarlas
como señales en el resultado, no como patentes identificadas.

---

## Para cada patente relevante encontrada o proporcionada

Capturar:

- **Número de patente/modelo de utilidad** (con número de solicitud si es
  diferente) y **jurisdicción**
- **Título**
- **Titular (cesionario) e inventores**
- **Fecha de prioridad y fecha de otorgamiento**
- **Fecha de expiración** (conforme a SIGA/IMPI — verificar pago de anualidades
  y cualquier extensión)
- **Estatus de anualidades / vigencia** — verificar en el expediente oficial el
  pago exigible, el periodo aplicable y cualquier gracia, rehabilitación,
  resolución o litigio. Una ausencia de pago aparente o una fuente secundaria
  no bastan para declarar la caducidad ni para descartar la patente como barrera
- **Tipo** — patente de invención o modelo de utilidad
- **Conteo de reivindicaciones — independientes y dependientes**
- **Reivindicaciones independientes como fueron otorgadas** (y cualquier
  reivindicación relevante modificada de procedimientos post-otorgamiento)
- **Procedimientos relacionados** — declaraciones administrativas de nulidad
  ante IMPI, recursos ante TFJA, litigio, procedimientos en otras
  jurisdicciones
- **Aspectos destacados del expediente** — limitaciones durante el trámite,
  modificaciones que estrecharon las reivindicaciones, declaraciones sobre el
  alcance

**No suplementar silenciosamente.** Si una búsqueda arroja una patente,
atribuir el resultado. Si el usuario mencionó una patente, decirlo. Nunca
inventar un número de patente, nunca "llenar" un elemento de reivindicación
que el expediente no soporta, nunca imaginar una fecha de expiración. Si el
estatus de anualidades no está disponible, escribir "estatus de anualidades no
verificado del resultado de búsqueda — confirmar en SIGA/IMPI antes de confiar
en el estatus de vigencia."

---

## Chart de reivindicaciones — primera pasada

Este es el núcleo del triaje. Elegir las patentes con la lectura más plausible
sobre el producto — usualmente las 2–5 con el mapeo técnico más cercano — y
recorrer cada reivindicación independiente elemento por elemento.

**Para cada patente seleccionada, escribir un chart de reivindicaciones por
cada reivindicación independiente:**

| Elemento de reivindicación | ¿El producto practica esto? | Base |
|---|---|---|
| "Un [frase de preámbulo]" | [sí / no / posiblemente / depende de construcción] | [una oración — qué del producto mapea; qué no; qué es ambiguo] |
| "que comprende [elemento 1]" | [sí / no / posiblemente] | [mapeo o brecha] |
| "en donde [elemento 2]" | [sí / no / posiblemente] | [mapeo o brecha] |
| [continuar por cada elemento] | | |

**Reglas para el chart:**

- **Cada elemento importa.** Una reivindicación se infringe solo si el producto
  acusado practica cada elemento de al menos una reivindicación (regla de todos
  los elementos). Faltar un elemento literalmente significa no infracción
  literal sobre esa reivindicación. No omitir ninguno.
- **Equivalentes son una pregunta separada, no una regla asumida.** Primero
  hacer chart literal. Para cualquier elemento con “no”, señalar que un abogado
  debe verificar si el expediente, criterio vigente y vía mexicana admiten una
  lectura no literal. No importar automáticamente las pruebas estadounidenses
  de diferencias insustanciales o función-medio-resultado.
- **La construcción de reivindicaciones es trabajo del abogado.** Donde un
  término pueda construirse de manera estrecha o amplia y la respuesta cambie
  la lectura de infracción, señalar el término y anotar ambas construcciones.
  No elegir una silenciosamente ni importar el procedimiento de un *Markman
  hearing* estadounidense; identificar el foro mexicano y su regla vigente.
- **Infracción indirecta (inducida, contribución) e infracción dividida** son
  solo señales. No intentar un análisis completo; anotar que pueden aplicar y
  requieren abogado de patentes.

> **Los sistemas de patentes difieren por jurisdicción.** El chart de
> reivindicaciones mexicano (regla de todos los elementos, equivalentes,
> análisis de LFPPI) no se transfiere directamente a otros sistemas:
> - **EE.UU.:** Markman hearing, Phillips claim construction, doctrine of
>   equivalents con prosecution history estoppel, §284 treble damages.
> - **Europa (UPC):** Procedimiento UPC desde 2023, protocolo sobre
>   interpretación del Art. 69 EPC.
> - **China:** Modelos de utilidad, examen CNIPA, diferente construcción de
>   reivindicaciones.
>
> Cuando hay jurisdicciones fuera de México en alcance: "Este análisis usa el
> marco de infracción mexicano bajo la LFPPI. Un producto fabricado en China y
> vendido en la UE necesita análisis CNIPA y EP, no un chart mexicano. Puedo
> señalar los temas que un análisis mexicano expone, pero las decisiones de
> infracción y validez requieren revisión específica de [jurisdicción]."

**Postura de decisión:** conforme al perfil de práctica, este skill nunca
concluye "no infringe." Las opciones:

- "El producto practica cada elemento de la Reivindicación X como está escrita;
  revisión de abogado requerida antes de proceder."
- "Uno o más elementos no están claramente presentes; revisión de abogado
  requerida para evaluar infracción literal y equivalentes."
- "La construcción de reivindicaciones es determinante en el elemento [Y];
  construcción por abogado requerida antes de proceder."

---

## Exclusiones de patentabilidad — relevancia para FTO

Las reglas de materia no considerada invención y exclusiones bajo LFPPI arts.
47-49 (MX-LFPPI-PATENTABILITY-001)
son relevantes para el triaje de FTO no porque el producto sea patentable, sino
porque una patente bloqueante podría ser atacada por nulidad si sus
reivindicaciones caen en una exclusión. Señalar como pregunta abierta si una
reivindicación de la patente bloqueante parece recitar materia excluida:

- Programas de computación reclamados como tales o en sí mismos (art. 47,
  fr. V y párrafo final LFPPI)
- Métodos de negocios
- Métodos terapéuticos, quirúrgicos o de diagnóstico
- Descubrimientos, teorías científicas, métodos matemáticos
- Esquemas, planes, reglas y métodos para realizar actos mentales
- Juegos
- Materia biológica como se encuentra en la naturaleza

**Esto no es un análisis de nulidad.** La pregunta abierta es: "¿podría esta
reivindicación ser vulnerable a una declaración administrativa de nulidad ante
IMPI por recitar materia excluida? — el abogado de patentes decide."

---

## Modelos de utilidad — consideraciones especiales para FTO

Los modelos de utilidad tienen un **umbral de actividad inventiva más bajo** y
un alcance de protección diferente:

- Solo protegen objetos, utensilios, aparatos o herramientas — no procesos.
- Un modelo de utilidad con reivindicaciones amplias puede ser más fácil de
  evadir que una patente de invención, pero también puede ser más fácil de
  obtener para un competidor.
- Los modelos de utilidad son particularmente comunes en México para innovaciones
  incrementales en manufactura, herramientas, y dispositivos mecánicos.

Cuando el triaje identifica un modelo de utilidad como potencialmente
bloqueante, señalar:
1. Las reivindicaciones están limitadas a objetos/dispositivos, no a procesos.
2. La nulidad puede ser más viable dado el umbral inventivo más bajo.
3. Vigencia de 15 años desde solicitud (diferente a los 20 de patente de
   invención).

---

## Preguntas abiertas

Cada patente o modelo de utilidad expuesto en el triaje debe producir una lista
de preguntas abiertas que un estudio formal de FTO respondería. Ejemplos:

- ¿La patente es ejecutable — el titular está correctamente registrado ante IMPI,
  algún defecto de titularidad, alguna cesión no registrada?
- ¿Qué declaró el solicitante sobre el término [X] durante el trámite ante IMPI,
  y limita eso la reivindicación?
- ¿Ha sido esta reivindicación objeto de una declaración administrativa de
  nulidad ante IMPI — qué dijo el IMPI sobre el alcance o la validez?
- ¿Hay una licencia disponible (pool de estándares, marcado de patente,
  compromiso de no aserción)?
- ¿Cuál es el historial real de enforcement de este titular ante IMPI o
  tribunales?
- ¿El modelo de utilidad tiene un alcance que realmente cubra el producto, o
  las reivindicaciones están limitadas a un dispositivo diferente?

Listarlas llanamente.

---

## Siguientes pasos recomendados

Clasificar por lo que encontró el triaje:

- **Si cada elemento de una reivindicación independiente mapea al producto
  (lectura literal):** *Detenerse y consultar al abogado de patentes.* Las
  opciones típicamente incluyen dictamen formal de FTO, diseño alternativo,
  licencia, impugnar validez (declaración administrativa de nulidad ante IMPI),
  o (rara vez) proceder asumiendo el riesgo. La elección es una decisión de
  negocio informada por el abogado.
- **Si elementos cortan en ambas direcciones o la construcción de
  reivindicaciones es determinante:** Estudio formal de FTO por abogado de
  patentes calificado. No lanzar basándose en este triaje.
- **Si la patente aparece caduca, abandonada o no ejecutable:** El abogado
  confirma el estatus de vigencia — el triaje no lo hace.
- **Si no se identificaron patentes en la búsqueda pero no se tenía acceso a
  base de datos:** La búsqueda formal es el siguiente paso, no una decisión de
  lanzamiento.
- **Siempre:** documentar qué patente identificó el triaje, de qué fuente
  provino, quién debe revisarla y qué decisión queda pendiente. No afirmar que
  el solo conocimiento configura dolo o agrava automáticamente sanciones o
  daños. El abogado debe determinar cualquier consecuencia jurídica y
  documentar el camino a seguir.

**Nota sobre remedios:** aplicar `MX-LFPPI-INFRINGEMENT-REMEDIES-001` a la vía
concreta y no importar categorías de daños estadounidenses. El art. 396 LFPPI
no establece un multiplicador por conocimiento previo. El art. 402 tampoco
convierte la infracción de patente en delito genérico: solo considerar vía penal
si los hechos satisfacen un tipo enumerado, previa revisión de
`MX-LFPPI-CRIMINAL-OFFENSES-001`.

---

## Formato de resultado

Anteponer el encabezado de confidencialidad de `PROFILE` → `## Resultados`. Marcar el documento como confidencial si el rol es abogado; ver la puerta para no abogados abajo si no.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD]

# Triaje de FTO — Primera Pasada (NO ES UN DICTAMEN)

**Esto no es un dictamen de libertad de operación.** Un dictamen formal de FTO
requiere una búsqueda exhaustiva, construcción completa de reivindicaciones, y
análisis elemento por elemento de infracción por un abogado de patentes
calificado. Deben analizarse los actos del artículo 55, sus limitaciones, la
fracción aplicable del artículo 386 y los remedios de la vía elegida; no se
presume responsabilidad ni un efecto jurídico automático por conocimiento
previo. Un resultado de "no se encontraron patentes
bloqueantes obvias" significa que el triaje no encontró una — no que el producto
esté libre. Un abogado de patentes calificado evalúa antes de que alguien se
apoye en esto para una decisión de producto.

**Resultado del triaje:** [VERDE / AMARILLO / ROJO — una oración por qué]

## Sujeto

- **Producto / proceso / característica:** [descripción, esencia técnica]
- **Detalle técnico en que se basó:** [qué se revisó — spec, diagrama, página
  pública, código, descripción del ingeniero]
- **Jurisdicciones en alcance:** [fabricar / usar / vender / ofrecer / importar
  — conforme a los derechos conferidos y conductas concretas verificadas]
- **Timing:** [pre-lanzamiento / cerca de lanzamiento / ya en mercado]

## Alcance de la búsqueda

- **Bases de datos consultadas:** [Solve Intelligence / Google Patents /
  Espacenet / PatSnap / SIGA (IMPI) — o "no se ejecutó búsqueda en base de
  datos"]
- **Consulta / enfoque:** [texto de consulta, clases tecnológicas, palabras
  clave, clasificaciones]
- **Fecha / ventana de fecha:** [fecha de búsqueda; patentes vigentes +
  solicitudes publicadas desde AAAA-MM-DD]
- **Jurisdicciones cubiertas por la búsqueda:** [lista]
- **Qué no se buscó:** [barridos de titular específico, declaraciones de
  patentes esenciales, portafolios de NPE, diseños industriales, equivalentes
  extranjeros — según aplique]

*Si no se ejecutó búsqueda en base de datos:* **No se ejecutó búsqueda en
base de datos de patentes.** Este triaje no consultó Solve Intelligence
Patents, SIGA (IMPI), Espacenet, Google Patents, PatSnap, ni ningún otro
corpus de patentes. Se requiere una búsqueda estructurada en las jurisdicciones
en alcance antes de confiar en este triaje para cualquier decisión de
lanzamiento.

## Patentes y modelos de utilidad identificados

| Título | Jurisdicción | Tipo | Titular | Prioridad / Otorgamiento | Expiración | ¿Vigente? | Fuente |
|---|---|---|---|---|---|---|---|
| [número] | [MX/US/EP/...] | [patente/MU] | [titular] | [fechas] | [fecha] | [sí/no/sin verificar] | [enlace a resultado de búsqueda o "proporcionado por usuario"] |

## Charts de reivindicaciones — primera pasada

### [Número de patente/MU] — Reivindicación independiente [N]

> "[Texto exacto de la Reivindicación N]"

| Elemento | ¿Practicado por el producto? | Base |
|---|---|---|
| [elemento 1] | [sí/no/posiblemente] | [mapeo o brecha] |
| [elemento 2] | [sí/no/posiblemente] | [mapeo o brecha] |

**Lectura literal:** [cada elemento mapea / uno o más elementos no mapean
claramente / la construcción de reivindicaciones es determinante en el elemento
[Y]]

**Equivalentes (solo señal):** [lectura por equivalentes plausible en el
elemento [Y] — construcción por abogado requerida / no plausible sobre los
elementos expuestos / desarrollo jurisprudencial limitado en México — señalar
para abogado]

**Infracción indirecta / dividida (solo señal):** [anotar si alguna lectura
depende de teorías de infracción indirecta o dividida — análisis por abogado
requerido]

*(Repetir para cada reivindicación independiente de cada patente seleccionada.)*

## Preguntas abiertas

- [pregunta 1]
- [pregunta 2]

## Señales (no patentes confirmadas)

- [solicitudes de competidores / actividad de NPE / declaraciones de patentes
  esenciales / litigio en el espacio tecnológico — cada una es razón para
  buscar más fuerte, no una patente identificada]

## Siguientes pasos recomendados

- [estudio formal de FTO por abogado de patentes — recomendación de primera
  línea salvo que la búsqueda no encontró nada y ya se ejecutó búsqueda
  exhaustiva]
- [opciones de diseño alternativo si se encontró lectura literal]
- [licencia / nulidad ante IMPI / análisis de riesgo según instruya el
  abogado]
- [enrutamiento conforme a
  `PROFILE`
  — despacho externo de patentes nombrado en el perfil de práctica]

## Nota de gobernanza de patentes identificadas

Este triaje identifica patentes específicas. Registrar la fuente y fecha,
preservar el análisis y obtener revisión jurídica antes de una decisión. No
afirmar que el conocimiento, por sí solo, configura dolo o agrava sanciones o
daños. El abogado de patentes determina las consecuencias aplicables y
documenta el camino a seguir; la decisión de lanzar, diseñar una alternativa o
licenciar se informa con un dictamen formal de FTO y el juicio del abogado, no
con este triaje.

## Verificación de citas

Cada número de patente, cita de reivindicación, fecha y hecho del expediente
en este memorándum debe verificarse contra la fuente autoritativa (SIGA/IMPI,
PatentCenter de USPTO, registro de EPO, equivalente nacional) antes de confiar
en ello. Las citas de reivindicaciones son el sitio de error más común — una
sola palabra cambia el análisis. No citar un resultado que no puedas abrir.
```

---

## Puerta para no abogados

Antes de emitir el resultado, leer `## Quién usa este plugin`. Si el Rol es No abogado:

> Este resultado es un triaje de investigación, no asesoría legal. Lanzar,
> continuar vendiendo, o invertir en este producto basándose solo en este triaje
> puede exponer a una reclamación si un derecho vigente cubre actos concretos
> del producto. Este resultado no establece infracción ni calcula sanciones o
> daños. Un abogado de patentes necesita evaluar antes de que avances.
>
> Aquí hay un resumen para llevar a un abogado — recortará el tiempo que toma
> la conversación:
>
> [Generar un resumen de 1 página: la descripción del producto, las
> jurisdicciones en alcance, la búsqueda ejecutada (y lo que no se buscó), las
> patentes expuestas y las lecturas del chart de primera pasada, las preguntas
> abiertas, y las tres preguntas para hacerle al abogado.]
>
> Si necesitas encontrar apoyo calificado en México, busca una persona abogada
> con cédula y experiencia técnica/PI para el dictamen y cualquier litigio.
> Para representación administrativa, verificar poder, personalidad y
> requisitos del trámite concreto; no asumir una categoría o registro oficial
> de "agente de propiedad industrial" sin fuente vigente.
> El Colegio de Abogados de tu entidad federativa, la Barra Mexicana Colegio
> de Abogados, o la AMPPI (Asociación Mexicana para la Protección de la
> Propiedad Intelectual) mantienen directorios de especialistas.

Entregar el memorándum de triaje completo junto con el resumen. No retener el
análisis. Señalar que el triaje mismo es un documento de investigación
confidencial y no debe reenviarse a terceros fuera de la cadena jurídica.

---

## Ubicación del resultado

Si los espacios de trabajo por asunto están habilitados y un asunto está activo, escribir el resultado en
`DATA_ROOT/outputs/fto-triage-<slug-sujeto>-AAAA-MM-DD.md`.
De lo contrario, escribir en
`DATA_ROOT/outputs/fto-triage-<slug-sujeto>-AAAA-MM-DD.md`
y mostrar la ruta.

Agregar una entrada de una línea al `history.md` del asunto si hay un asunto activo.

---

## Cerrar con el árbol de decisión de siguientes pasos

Cerrar con el árbol de decisión de siguientes pasos conforme a CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más hechos, observar y esperar, algo diferente) son un punto de partida, no un candado. El árbol es el resultado; el abogado elige.

## Qué este skill NO hace

- **Emitir un dictamen de FTO.** Nunca. La salvaguarda más fuerte del plugin.
- **Construir reivindicaciones.** Donde la construcción es determinante, señala
  el término y ambas construcciones plausibles. No elige una.
- **Adjudicar validez.** Puede anotar procedimientos conocidos ante IMPI; no
  opina sobre novedad, actividad inventiva, reglas de los arts. 47-49 LFPPI, o
  suficiencia de descripción.
- **Redactar reivindicaciones de patente.** Este plugin no va ahí; enrutar al
  abogado de trámite de patentes.
- **Evaluar exposición de daños.** La cuantificación de daños es trabajo de
  especialista.
- **Manejar análisis de secreto industrial o marca** — usar
  `/propiedad-intelectual-legal-mexico:triaje-infraccion` con el modo
  correspondiente.
- **Citar resultados a contrapartes o audiencias no confidenciales.** Este es
  un documento de investigación confidencial.

---

## Tono

Técnicamente preciso. Elemento por elemento. Cada señal es específica a un
elemento de reivindicación o una patente conocida. Sin prosa evasiva en el
cuerpo — las salvaguardas al inicio y al final hacen el trabajo de alcance, y
el análisis hace el análisis. El lector debe salir sabiendo qué miró el triaje,
qué no miró, y cuál es el siguiente paso.
