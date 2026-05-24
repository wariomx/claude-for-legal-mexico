---
name: claim-chart
description: >
  Construye o revisa un cuadro de elementos — un cuadro de reivindicaciones
  de patente (infracción, invalidez o revisión) o un cuadro de elementos
  civiles/mercantiles para cualquier causa de acción o excepción — con cada
  celda citada puntualmente y la detección de lagunas probatorias como
  producto prioritario. Úselo cuando el usuario pida un cuadro de
  reivindicaciones, cuadro de elementos, cuadro de pruebas, cuadro de
  contenciones de infracción o invalidez, mapeo elemento por elemento, o
  pregunte "¿qué nos falta para acreditar [acción]?".
argument-hint: '[--patente | --civil-mercantil] [--infraccion | --invalidez | --revision] [--reivindicacion <n>] [--accion <nombre>] [--asunto <slug>]'
---

# /claim-chart

1. Cargar `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → rol, encabezado de producto de trabajo, postura de decisión, almacenamiento de documentos.
2. Si los espacios de trabajo de asuntos están habilitados, confirmar o seleccionar el asunto activo; cargar `matter.md` (parte, jurisdicción, fase, teoría del caso, escritos).
3. Seguir el flujo de trabajo y la referencia a continuación.
4. Selección de modo:
   - `--patente` → cuadro de reivindicaciones de patente. Requiere número de patente y al menos una reivindicación ejercitada. Sub-modos: `--infraccion`, `--invalidez`, `--revision`.
   - `--civil-mercantil` → cuadro de elementos civiles/mercantiles. Requiere la causa de acción (o excepción) y la parte.
   - Sin bandera → preguntar al usuario cuál.
5. Para modo civil-mercantil: consultar `references/element-templates.md` en el directorio de esta habilidad para la lista base de elementos. Confirmar con el usuario la ley sustantiva o el código procesal aplicable antes de mapear.
6. Para modo patente: parsear las reivindicaciones ejercitadas en elementos, señalar términos en disputa para interpretación, aplicar cualquier resolución de interpretación del IMPI o tribunal.
7. Mapear elementos contra el objetivo (producto acusado / arte previo / acervo probatorio / cuadro bajo revisión). Cada celda con cita puntual. Aplicar la neutralización de prefijo apóstrofo antes de escribir cualquier valor de celda que inicie con `=`, `+`, `-`, `@`, tabulación o retorno de carro.
8. Producir la lista de lagunas (civil-mercantil) o la lista de necesita-prueba (patente) — el producto prioritario.
9. Escribir markdown, CSV (valores + archivo compañero `_sources`), y Excel o Sheets según preferencia del usuario. Encabezado de producto de trabajo en cada salida.
10. Escribir en la carpeta `claim-charts/` del asunto si hay un asunto activo; de lo contrario, en la carpeta `claim-charts/` a nivel de práctica. Agregar una entrada de una línea a `history.md` si hay un asunto activo.
11. Devolver un resumen: reivindicación(es), objetivo(s), jurisdicción, fase, conteo de elementos por estado, la lista de lagunas, rutas de archivos, y el recordatorio de que cada celda es una pista.

---

# Cuadro de Elementos / Reivindicaciones

## Restricciones de uso de documentos obtenidos en juicio

Antes de trabajar con un conjunto de documentos de litigio, pregunte: "¿Alguno de estos documentos fue obtenido como prueba dentro de un procedimiento judicial o arbitral?"

- **México:** Los documentos que forman parte del expediente judicial tienen carácter público conforme a la legislación de transparencia, salvo las excepciones previstas (datos personales, secretos industriales, seguridad nacional). Sin embargo, documentos obtenidos bajo convenios de confidencialidad, medidas cautelares o acuerdos de protección de información dentro del procedimiento están sujetos a restricciones de uso. Verifique el acuerdo específico y los autos del juez.
- **Arbitraje:** Las reglas de arbitraje (CCI, CAM, CANACO) y la cláusula arbitral suelen imponer confidencialidad sobre los documentos del procedimiento. El uso fuera del arbitraje puede constituir incumplimiento del acuerdo arbitral.

Confirme: "El uso de estos documentos está dentro del procedimiento en que fueron obtenidos, o tengo autorización para usarlos fuera de ese contexto." Si no se confirma, señale: "Los documentos del expediente o del arbitraje pueden tener restricciones de uso. Confirme que este uso está permitido antes de continuar."

## UN CUADRO ES UN BORRADOR, NO UNA RESOLUCIÓN NI UN ESCRITO

**Coloque esto al inicio de cada salida. No lo omita. No lo suavice.**

> Este cuadro es un borrador para análisis y verificación del abogado, no un escrito judicial presentado, una sentencia, una opinión legal, ni un dictamen. Cada mapeo es una pista que el abogado debe verificar contra la fuente. Los elementos listados provienen de la ley sustantiva, el código procesal y las plantillas base — la **autoridad controlante** en la jurisdicción del usuario (código procesal federal o estatal, legislación sustantiva vigente, jurisprudencia obligatoria) puede diferir y siempre prevalece. La detección de lagunas es un punto de partida para la etapa probatoria o un escrito; no es una conclusión sobre el fondo.
>
> Sub-señalar una laguna es una puerta de un solo sentido — una demanda presentada sin sustento en un elemento, una contestación sin pruebas para un elemento controvertido, o un caso que llega a sentencia sin prueba de daños. Sobre-señalar es una puerta de dos sentidos — el abogado depura las señales en la revisión. La configuración por defecto favorece la puerta de dos sentidos.

---

## Contexto del asunto

Revise `## Matter workspaces` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗` (valor predeterminado para usuarios de jurídico interno), omita el resto de este párrafo — las habilidades usan el contexto a nivel de práctica y el mecanismo de asuntos es invisible. Si está habilitado y no hay un asunto activo, pregunte: "¿Para qué asunto es esto? Ejecute `/litigacion-legal-mexico:matter-workspace switch <slug>` o diga `nivel-práctica`." Cargue el `matter.md` del asunto activo — especialmente la teoría del caso, la demanda (para los elementos efectivamente alegados), la jurisdicción, cualquier resolución de interpretación de reivindicaciones (modo patente), y la fase del procedimiento. Escriba las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/<matter-slug>/claim-charts/`. Nunca lea archivos de otro asunto a menos que `Cross-matter context` esté `on`.

---

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` → rol, encabezado de producto de trabajo, postura de decisión, almacenamiento de documentos, estructura de teoría del caso
- `matter.md` del asunto activo — acciones, excepciones, parte, jurisdicción, fase, teoría
- Para modo civil-mercantil: la demanda o reconvención (para las acciones efectivamente ejercitadas), la contestación (para las excepciones efectivamente opuestas), la ley sustantiva aplicable, el código procesal. También el acervo probatorio — testimoniales, confesionales, documentos aportados, dictámenes periciales.
- Para modo patente: la patente, las reivindicaciones ejercitadas, la descripción, el historial de trámite ante IMPI si está disponible, el material del producto acusado o la referencia de arte previo, cualquier resolución de interpretación de reivindicaciones.

Si el `CLAUDE.md` tiene marcadores `[PLACEHOLDER]`, muestre este rebote:

> Noto que aún no ha configurado su perfil de práctica — así es como adapto la calibración de riesgo, el panorama y el estilo a su práctica.
>
> **Dos opciones:**
> - Ejecute `/litigacion-legal-mexico:cold-start-interview` (2 minutos) para configurar su perfil, y luego ejecutaré esto adaptado a SU práctica.
> - Diga **"provisional"** y lo ejecutaré con valores genéricos predeterminados — jurisdicción CDMX, apetito de riesgo medio, rol de abogado, sin playbook — y marcaré cada salida con `[PROVISIONAL — configure su perfil para resultados personalizados]` para que vea qué hago antes de comprometerse.

### Modo provisional

Si el usuario dice "provisional," construya el cuadro normalmente usando estos valores genéricos: apetito de riesgo medio, rol de abogado, jurisdicción CDMX/federal, sin playbook a nivel de práctica (trabaje con los escritos del asunto y los elementos de las acciones ejercitadas). Marque la nota del revisor y cada fila del cuadro con `[PROVISIONAL]`. Al final de la salida, agregue:

> "Esa fue una ejecución genérica con supuestos predeterminados. Ejecute `/litigacion-legal-mexico:cold-start-interview` para obtener resultados calibrados a SU práctica — su calibración de riesgo, su panorama, su estilo. 2 minutos."

**Puerta de conflictos — inderogable.** Antes de construir un cuadro de elementos, verifique `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/_log.yaml` para el slug del asunto. Si el asunto no está en `_log.yaml`, rehúse y redirija:

> "No veo [slug del asunto] en el registro de asuntos. Ejecute `/litigacion-legal-mexico:matter-intake` primero para que se corra la verificación de conflictos y se configure el espacio de trabajo. No construiré un cuadro de elementos sobre un asunto que no haya sido registrado — la verificación de conflictos es la puerta."

No proceda sobre un asunto no registrado. El intake ejecuta conflictos y escribe la fila de `_log.yaml` que esta habilidad lee.

---

## Selección de modo

Pregunte al inicio, antes de cualquier otra cosa:

> ¿Qué tipo de cuadro?
>
> 1. **Cuadro de reivindicaciones de patente** — mapeo elemento por elemento de las limitaciones de reivindicación contra un producto acusado (`--infraccion`), arte previo (`--invalidez`), o el cuadro de otra parte (`--revision`). Para contenciones de patente, solicitudes de nulidad ante el IMPI, análisis FTO.
> 2. **Cuadro de elementos civil/mercantil** — elementos de una causa de acción (o excepción) mapeados contra las pruebas. Para revisión de fundabilidad de demandas, planeación de la etapa probatoria, preparación de escritos de alegatos, esquema de orden de prueba en audiencia.
>
> Además (común a ambos):
>
> - **Parte.** ¿Actor o demandado? (En modo civil-mercantil esto invierte la carga probatoria; en modo patente cambia el enfoque infracción/invalidez.)
> - **Jurisdicción / foro.** Entidad federativa, fuero (federal o local), materia (civil, mercantil, laboral). Los elementos y la legislación procesal varían por jurisdicción y materia.
> - **Fase.** Pre-demanda, demanda/contestación, etapa probatoria, alegatos, sentencia, recurso (apelación/amparo). El cuadro es el mismo; el enfoque de la salida cambia.
> - **¿Cuadro existente?** Si `--revision`, cárguelo.

---

# MODO 1 — Cuadro de reivindicaciones de patente

## Sub-modos

- `--infraccion` — elementos de reivindicación vs. producto acusado (escritos de contención de infracción, respuesta a declaración administrativa del IMPI)
- `--invalidez` — elementos de reivindicación vs. arte previo (solicitud de declaración administrativa de nulidad ante IMPI, defensas basadas en falta de novedad o actividad inventiva)
- `--revision` — auditar un cuadro que alguien más produjo

## Ingesta adicional en modo patente

- **Número de patente y reivindicaciones ejercitadas.** Cuáles independientes, cuáles dependientes. (No cuadre reivindicaciones no ejercitadas a menos que se lo pidan.)
- **Fecha de prioridad.** Establece la barra de novedad y la fecha de corte para arte previo (LFPPI Art. 42 — novedad: la invención no debe estar comprendida en el estado de la técnica).
- **Interpretación de reivindicaciones existente.** Resoluciones del IMPI sobre alcance de la patente, interpretaciones propuestas en escritos, sentencias previas sobre el alcance de reivindicaciones similares.

## Vía procesal: IMPI vs. tribunal civil

En México existen dos vías para la defensa de derechos de patente — es fundamental distinguirlas al inicio:

| | Vía administrativa (IMPI) | Vía civil (tribunal federal) |
|---|---|---|
| **Acción** | Declaración administrativa de infracción (LFPPI Arts. 386–388) o de nulidad (LFPPI Arts. 125–131) | Acción civil de daños y perjuicios |
| **Sanciones** | Multas administrativas, clausura temporal, embargo precautorio de mercancía (Art. 389 LFPPI) | Indemnización por daños y perjuicios |
| **Requisito** | Patente vigente y registro ante IMPI | Declaración administrativa previa de infracción (como regla general) |
| **Recurso** | Juicio de nulidad ante TFJA → amparo | Apelación → amparo |

Pregunte al usuario: "¿En qué vía está o planea estar — administrativa ante el IMPI, civil ante tribunal federal, o ambas?" El cuadro se adapta a la vía.

## Flujo de trabajo en modo patente

### Paso 1: Parsear las reivindicaciones

Parsee las reivindicaciones independientes ejercitadas en elementos numerados. Maneje:

- **Preámbulo.** Note si es limitativo o meramente introductorio. Si la resolución del IMPI o el tribunal no lo ha resuelto, señale `preámbulo-limitativo: sin resolver`.
- **Frase de transición.** "Que comprende" (abierta) / "que consiste en" (cerrada) / "que consiste esencialmente en" (semi-abierta). Afecta si elementos adicionales no recitados impiden la infracción.
- **Elementos** separados por comas / punto y coma, numerados `[1a]`, `[1b]`, `[1c]`. Mantenga la numeración estable — es la columna vertebral del cuadro.
- **Reivindicaciones funcionales** — todo "medio para [función]" o término funcional no estructural. El alcance se limita a la estructura descrita en la especificación más equivalentes. Cite la estructura correspondiente por columna/línea de la descripción. Si la especificación no describe estructura, señale `indefinido-funcional`.
- **Grupos Markush, reivindicaciones Jepson, producto-por-proceso, dependencias de orden en reivindicaciones de método** — señale con nota sobre reglas de interpretación especiales.
- **Reivindicaciones dependientes** — referencie la reivindicación padre; cuadre solo las limitaciones adicionales. **Ejecute, no indique.** Si las reivindicaciones ejercitadas incluyen dependientes, produzca las filas reales de limitación adicional para cada dependiente en el Paso 4 — no emita una nota de que los dependientes "deben cuadrarse."
- **Modelo de utilidad.** Si el título es un modelo de utilidad (no una patente de invención), anote: plazo de vigencia de 15 años, se requiere solo novedad y aplicación industrial (no actividad inventiva — LFPPI Arts. 60–67). El umbral de invalidez es diferente al de patentes de invención.

Muestre el parseo al usuario. Confirme antes de mapear. Un parseo incorrecto contamina cada fila posterior.

### Paso 2: Revisión de interpretación de reivindicaciones

Señale términos en disputa:

- Términos acuñados o definidos en la descripción
- Términos con historial de trámite (enmiendas, argumentos, renuncias ante el IMPI durante la concesión)
- Lenguaje funcional ("configurado para", "adaptado para", "capaz de")
- Términos relativos ("sustancialmente", "aproximadamente") — riesgo de imprecisión
- Materia excluida — LFPPI Art. 4: descubrimientos, teorías científicas, métodos matemáticos, programas de cómputo, métodos de diagnóstico/terapéuticos/quirúrgicos, materia biológica como se encuentra en la naturaleza, entre otros. Si las reivindicaciones tocan materia excluida, señale riesgo de invalidez.

Para cada término señalado, indique la(s) interpretación(es) bajo la(s) cual(es) el mapeo funciona y la(s) interpretación(es) bajo la(s) cual(es) falla. Si existe resolución del IMPI o sentencia sobre el alcance, aplíquela. Si hay escritos pendientes, cuadre bajo la interpretación de cada parte.

### Paso 3: Mapear

Para cada elemento, para cada objetivo:

1. **Encontrar pruebas.** Producto acusado: documentación, manuales, fichas técnicas, código fuente, desmontajes, testimoniales, dictámenes periciales. Arte previo: columna/línea para patentes mexicanas o internacionales, párrafo para solicitudes publicadas, página/figura para documentos no patentarios. Para arte previo, señale si la referencia califica como estado de la técnica (LFPPI Art. 42 — publicaciones anteriores a la fecha de prioridad o presentación). Si el estatus de arte previo no es obvio, marque `estado-arte-previo: necesita-prueba`.
2. **Cite textualmente.** Carácter por carácter. Sin paráfrasis. Corte en límites de oración y marque la elisión.
3. **Caracterice el mapeo.**

   | Mapeo | Significado | Dónde |
   |---|---|---|
   | `literal` | El lenguaje de la reivindicación se lee en la característica acusada / la divulgación del arte previo | Ambos |
   | `literal-depende-interpretacion` | Literal bajo X; falla bajo Y | Ambos |
   | `anticipacion` | Cada elemento en una sola referencia, dispuesto conforme a la reivindicación | Solo invalidez |
   | `obviedad-combinacion` | Una referencia secundaria suple el elemento faltante; se requiere motivación para combinar (LFPPI Art. 42, fracción IV — actividad inventiva) | Solo invalidez |
   | `parcial` | Parte del elemento está presente | Ambos |
   | `no-encontrado` | Elemento no presente | Ambos |
   | `necesita-prueba` | No se puede determinar con el material disponible | Ambos |
   | `depende-interpretacion` | Depende de cómo se interprete un término en disputa | Ambos |

4. **Estado por celda.** `mapeado` / `parcial` / `no-encontrado` / `necesita-prueba` / `depende-interpretacion` / `anticipacion` / `obviedad-combinacion`.
5. **Señale preguntas abiertas.** "Esto mapea si [X]. Se necesita [desmontaje / código fuente / testimonial / peritaje] para confirmar."

**Sin suplemento silencioso.** Documentación escasa significa `necesita-prueba`, no extrapolación de productos similares.

### Paso 4: Reivindicaciones dependientes — ejecute, no indique

Para cada reivindicación dependiente ejercitada, produzca una fila (o conjunto de filas) real cuadrando la(s) limitación(es) adicional(es) contra el objetivo. Se anota la dependencia del padre, y la infracción/invalidez del dependiente requiere la del padre. **Produzca las filas, no una nota indicando que deben producirse.**

Si el usuario proporcionó una lista de reivindicaciones ejercitadas que incluye dependientes, la salida del cuadro DEBE contener filas para cada una. Si el usuario dio solo la independiente y dijo "cuadre las independientes por ahora," bien — entonces la salida no cuadra dependientes, pero señala las omitidas explícitamente ("Reivindicaciones dependientes ejercitadas [X, Y, Z] no cuadradas en esta ejecución — solicite: reejecutar con `--incluir-dependientes` o pegue el texto de la reivindicación dependiente"). No omita dependientes silenciosamente.

Formato de fila de reivindicación dependiente:

```markdown
| [#] | Elemento (textual) | Característica acusada (o divulgación de arte previo) | Prueba (cita puntual) | Mapeo | Estado | Verificado |
|---|---|---|---|---|---|---|
| 2 [adic.] | "en donde la espiga se extiende a un ángulo de 15° a 30° del eje del cuerpo" | Ángulo de espiga de 18° del producto X per [FT-X-2026-03 Fig. 4 + §2.3] | [FT-X-2026-03 §2.3] "ángulo de espiga 18° ±2°" | literal-depende-interpretacion | mapeado | ☐ |
```

### Paso 5: Infracción indirecta y sanciones (solo infracción)

Señale, no opine:

- **Infracción administrativa (LFPPI Arts. 213–215)** — identificar la fracción específica del Art. 213 aplicable. Verificar si la conducta encuadra en alguna de las hipótesis (uso de marca o patente sin consentimiento, producción, importación, etc.)
- **Sanciones administrativas (LFPPI Arts. 388–392)** — multas de hasta 500,000 UMAs, clausura temporal, decomiso de mercancía infractora
- **Delitos en materia de propiedad industrial (LFPPI Arts. 402–406)** — se persiguen por querella; requieren intencionalidad
- **Responsabilidad de proveedores y distribuidores** — ¿hay infracciones en la cadena de distribución?

### Paso 6: Umbrales de invalidez (solo invalidez)

Nulidad de patente ante el IMPI — dos fundamentos principales:

**Falta de novedad (LFPPI Art. 42, fracciones I–III):** Cada elemento en una sola referencia del estado de la técnica. Una referencia parcial que no cubre todos los elementos no destruye novedad — es material para actividad inventiva.

**Falta de actividad inventiva (LFPPI Art. 42, fracción IV):** Referencia primaria + referencia(s) secundaria(s) + motivación para combinar. El estándar es: "la invención no deriva de manera evidente del estado de la técnica para una persona versada en la materia." Señale:
- Enseñanza, sugerencia o motivación explícita para combinar
- Motivación por necesidad del mercado o del diseño
- Expectativa razonable de éxito
- **Indicios secundarios** — éxito comercial, necesidad prolongada no satisfecha, fracaso de otros, reconocimiento de la industria

También señale:
- **Materia excluida (LFPPI Art. 4)** — si las reivindicaciones cubren materia que no puede ser objeto de patente
- **Insuficiencia de la descripción (LFPPI Art. 47)** — la descripción debe ser suficientemente clara y completa para que una persona versada en la materia pueda reproducir la invención
- **Reivindicaciones más amplias que la descripción** — las reivindicaciones deben estar sustentadas en la descripción (LFPPI Art. 48)
- **Inejecutabilidad** — vicios en el trámite de concesión (declaraciones falsas, omisión de arte previo conocido)

Señale: "La nulidad de una patente mexicana se resuelve ante el IMPI mediante declaración administrativa de nulidad (LFPPI Arts. 125–131). El estándar no es de prueba reforzada como en otros sistemas — basta prueba suficiente para desvirtuar la presunción de validez del título."

### Paso 7 (sub-modo revisión): Auditoría

Para cada fila: ¿está sustentado el mapeo? ¿Es precisa la cita puntual? ¿Se contabiliza completamente el elemento? ¿Cuál es el mejor contraargumento? ¿Cuál es la oportunidad de réplica? Emita veredictos por fila (`sustentado` / `débil` / `no sustentado`) y las vulnerabilidades del cuadro.

## Salvaguardas del modo patente (adicionales a las salvaguardas compartidas)

- **Escritos y contenciones.** Las contenciones de infracción e invalidez requieren fundamentación seria. Un cuadro de esta habilidad es un borrador, no un escrito presentado al IMPI ni al tribunal.
- **Candor en la interpretación.** Cada fila que depende de interpretación indica la interpretación asumida y aquella bajo la cual el mapeo falla.
- **Infracción indirecta es separada.** No combine responsabilidad de proveedores/distribuidores en las filas de infracción directa.
- **Modelo de utilidad vs. patente de invención.** Anote la diferencia en umbral de invalidez (el modelo de utilidad no requiere actividad inventiva).

---

# MODO 2 — Cuadro de elementos civil/mercantil

Mapee los elementos de una causa de acción (o excepción) contra las pruebas. Los productos decisivos son (a) un cuadro que dice qué prueba va con qué elemento y (b) una lista de lagunas que le dice al abogado qué falta.

## Flujo de trabajo

### Paso 1: Identificar la(s) acción(es)

- ¿Qué causa de acción? (¿O excepción?) Si hay múltiples pretensiones, cuadre cada una por separado.
- ¿Qué parte? ¿Actor o demandado? En el perfil de práctica, lea `## Side` para el valor predeterminado — `actor` mapea la carga de la prueba (acreditando los elementos); `demandado` mapea lagunas y excepciones (desvirtuando o eludiendo los elementos). Confirme que la postura corresponde a este asunto antes de iniciar.
- ¿Qué jurisdicción? Entidad federativa, fuero, materia. **Los elementos y la legislación procesal varían por jurisdicción y materia.** La biblioteca de plantillas es una línea base; la ley sustantiva y el código procesal aplicables prevalecen.
- ¿Qué escrito? Cargue la demanda / reconvención / contestación para que el cuadro refleje las acciones efectivamente ejercitadas, no una versión genérica.

### Paso 2: Cargar los elementos

Tres rutas:

**(a) Biblioteca de plantillas.** Consulte `references/element-templates.md` (en el directorio de esta habilidad). Elementos base para causas de acción y excepciones comunes del derecho mexicano, con citas a la legislación sustantiva y una nota jurisdiccional. Seleccione la plantilla que corresponda a la acción ejercitada.

**(b) Personalizado.** El usuario define los elementos, o pega un artículo de ley, una tesis de jurisprudencia, o una pretensión de la demanda para parsear. Parsee en elementos numerados.

**(c) Excepciones y defensas.** También soporta mapeo de excepciones — prescripción, caducidad, cosa juzgada, falta de legitimación, excepción de contrato no cumplido, nulidad, etc. Las excepciones tienen sus propios elementos que el demandado debe probar (o, para algunas, que el actor debe desvirtuar una vez opuestas).

**Formulaciones específicas por materia — señale proactivamente.** Si el perfil de práctica o el `matter.md` del asunto identifican la materia como **mercantil, laboral o amparo**, señale proactivamente la formulación específica junto con la línea base — no pregunte "¿la legislación de su materia agrega o modifica algún elemento?" primero. La habilidad debe ofrecer la formulación y dejar que el usuario elija.

Divergencias a señalar sin que se lo pidan (no exhaustivo — agregue a esta lista conforme surjan patrones):

| Causa de acción / excepción | Línea base (CCF) | Formulación por materia |
|---|---|---|
| Incumplimiento contractual | 5 elementos (contrato, cumplimiento, incumplimiento, daño, nexo causal — CCF Arts. 1949, 2104) | **Mercantil:** Prevalece lo pactado (Art. 78 C. Com.); mora opera al día siguiente del vencimiento pactado sin requerimiento (Art. 85 frac. I C. Com.); cuando no hay fecha pactada sí se requiere requerimiento judicial o extrajudicial (Art. 85 frac. II C. Com.); convencionalidad de intereses con reglas propias. `[verified 2026-05-23]` |
| Incumplimiento contractual — bienes muebles | Elementos civiles generales | **Si es compraventa mercantil (C. Com. Arts. 371–387):** reglas especiales sobre entrega, vicios ocultos: 30 días desde recepción para reclamar vicios internos; 5 días para defectos de calidad o cantidad visibles (Art. 383 C. Com.). ⚠️ El plazo de 6 meses corresponde a compraventa civil (CCF), NO a compraventa mercantil. `[verified 2026-05-23]` |
| Separación del trabajo (despido) | Elementos LFT Arts. 46–48 | **Laboral:** Carga de la prueba invertida (el patrón prueba la causa justificada — Art. 784 LFT). Requisito de agotar conciliación previa (Art. 684-B LFT). Prescripción: 2 meses desde la separación — aplica tanto a despido justificado como injustificado (Art. 518 LFT). `[verified 2026-05-23]` |
| Responsabilidad civil | 4 elementos (hecho ilícito, culpa, daño, nexo causal — CCF Art. 1910) | **CDMX:** Aplica CCF directamente. **Entidades federativas:** Verifique código civil local — algunas entidades tienen regulación adicional en materia de daño moral o responsabilidad objetiva. |
| Rescisión | CCF Art. 1949 | **Laboral (rescisión patronal):** catálogo cerrado de causales (Art. 47 LFT); aviso obligatorio al trabajador en el momento mismo del despido; si rehúsa recibirlo, comunicar al Tribunal dentro de 5 días hábiles; la falta de aviso crea presunción iuris tantum de separación injustificada — admite prueba en contrario (no es invalidación absoluta). `[verified 2026-05-23]` |

Cuando la formulación por materia difiera materialmente de la línea base, el cuadro abre con una nota de una línea:

> **Nota jurisdiccional:** Me indicó que este es un asunto [mercantil/laboral/civil federal/etc.] en [jurisdicción]. Así difiere la formulación aplicable de la línea base: [divergencia]. El cuadro a continuación usa la formulación de [materia/jurisdicción]. Si es incorrecto, indíquelo y recargo.

Confirme la lista de elementos con el usuario antes de mapear. Si la materia o jurisdicción del usuario no es una de las señaladas proactivamente, pregunte: "¿La legislación aplicable en su jurisdicción agrega, elimina o reformula alguno de estos elementos?" Si sí, use su versión.

### Paso 3: Mapear

Para cada elemento:

- **Prueba que sustenta** — ¿qué acredita este elemento? Cite la fuente con cita puntual.
  - Testimonial — `[Testimonial García, audiencia 15-mar-2026, min. 42:15–43:07]`
  - Confesional — `[Confesional del demandado, pos. 5–7, audiencia 20-mar-2026]`
  - Documental pública — `[Escritura 12,345 / Not. 89 CDMX, foja 3]`
  - Documental privada — `[Contrato MSA § 4.2, Anexo 3-A]`
  - Pericial — `[Dictamen Perito Ing. López, p. 18, conclusión tercera]`
  - Inspección judicial — `[Acta de inspección judicial, foja 245 del expediente]`
  - Instrumental de actuaciones — `[Fojas 12-15 del expediente]`
  - Presuncional — para elementos que se acreditan por presunción legal o humana
  - Ley / jurisprudencia — para elementos puramente jurídicos
- **Cita textual** cuando la prueba es testimonial o documental. Sin paráfrasis.
- **Prueba que contradice** — ¿qué va en contra? Cítela. Esta es la vulnerabilidad de la fila.
- **Fortaleza** — `fuerte` / `moderada` / `débil` / `ninguna`. Manténgalo simple. Calificaciones excesivamente calibradas son ruido; `débil` y `ninguna` son las filas que importan.
- **Estado por celda** — `acreditado` / `parcial` / `controvertido` / `laguna` / `necesita-prueba`.

### Paso 4: Detección de lagunas — el producto decisivo

Después de mapear, produzca una lista de lagunas. Este es el propósito del cuadro.

> **Elementos con prueba escasa o inexistente:** [lista]
>
> - Si es actor: estas lagunas debilitan la fundabilidad de su demanda, su posición probatoria en audiencia, o su caso en sentencia. Ciérrelas antes del siguiente escrito o audiencia.
> - Si es demandado: estos son sus objetivos de defensa — los elementos que el actor debe probar y donde su acervo probatorio es insuficiente.
> - Si está en etapa previa a pruebas: estas son sus prioridades probatorias — las testimoniales, confesionales, periciales y documentales que convierten una laguna en `acreditado` o confirman `ninguna`.

La detección de lagunas no es una conclusión sobre el fondo. Es un mapa de dónde el caso está ligero.

### Paso 5: Enfoque según la fase procesal

Pregunte la fase. Mismo cuadro; diferente enfoque en la salida:

- **Pre-demanda / demanda.** ¿La demanda contiene los hechos y fundamentos de derecho suficientes conforme al código procesal aplicable (CNPCF Arts. 247–248 para civil/familiar; C. Com. Art. 1061 para mercantil; LFT Art. 872 para laboral)? ¿Cumple los requisitos formales? ¿Hay algún elemento alegado sin sustento fáctico que lo haga vulnerable a excepción de oscuridad o imprecisión de la demanda?
- **Etapa probatoria.** Para cada elemento en `laguna` o `necesita-prueba`, ¿qué prueba se necesita? ¿Qué testigos, qué documentos, qué periciales, qué confesionales? Prepare el escrito de ofrecimiento de pruebas.
- **Alegatos.** Para cada elemento, ¿está acreditado en el expediente? Un elemento `acreditado` sin prueba contradictoria es argumento fuerte en alegatos; un elemento `controvertido` requiere análisis de la valoración probatoria que el juez hará.
- **Sentencia / recurso.** ¿La sentencia abordó cada elemento? ¿Hay algún elemento no valorado que constituya agravio para apelación o concepto de violación para amparo?

### Paso 6 (sub-modo revisión): Auditoría

Para el escrito de la contraparte, una resolución, o un borrador de abogado externo: para cada elemento, ¿la prueba citada realmente lo acredita? ¿Dónde está escaso su cuadro? ¿Cuál es su mejor contraargumento?

## Salvaguardas del modo civil-mercantil (adicionales a las salvaguardas compartidas)

- **Jurisdicción.** La lista de elementos es una línea base. Siempre confirme la ley sustantiva y el código procesal aplicables. Registre la fuente en la hoja `_elements`.
- **Acciones ejercitadas únicamente.** Cuadre lo que efectivamente se demandó. No agregue una acción que la demanda no ejercita solo porque los hechos podrían sustentarla — ese es un análisis diferente.
- **Excepciones.** Al mapear excepciones, note si la carga corresponde al demandado (la mayoría) o si al oponerla se traslada carga al actor.
- **"Laguna" ≠ "caso perdido."** Una laguna es una pista. Una prueba adicional, una testimonial, un peritaje puede cerrarla. El cuadro muestra dónde excavar.

---

# Chasis compartido (ambos modos)

## Salida

Anteponga el encabezado de producto de trabajo de `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` `## Outputs`.

### Tabla markdown (siempre)

Una tabla por acción / excepción / reivindicación-de-patente por objetivo.

**Ejemplo modo patente:**

```markdown
| [#] | Elemento (textual) | Característica acusada | Prueba (cita puntual) | Mapeo | Estado | Verificado |
|---|---|---|---|---|---|---|
| 1a | "un procesador configurado para..." | SoC según ficha técnica | [Ficha técnica p. 7] "..." | literal-depende-interpretacion | mapeado | ☐ |
| 1b | "medio para [función]" (funcional) | [equivalente alegado] | [fuente, archivo.c:124] "..." | necesita-prueba | necesita-prueba | ☐ |
```

**Ejemplo modo civil-mercantil:**

```markdown
| [#] | Elemento | Prueba que sustenta (cita puntual) | Prueba que contradice | Fortaleza | Estado | Verificado |
|---|---|---|---|---|---|---|
| 1 | Existencia del contrato | [Anexo 3, MSA § 1; Testimonial García 22:4–14] | ninguna | fuerte | acreditado | ☐ |
| 2 | Cumplimiento del actor | [Dictamen Perito López ¶¶ 4–9] | [Confesional del demandado, pos. 5: "nunca entregaron la fase 2"] | moderada | controvertido | ☐ |
| 3 | Incumplimiento del demandado | — | [Confesional pos. 5] | ninguna | laguna | ☐ |
| 4 | Nexo causal | — | — | ninguna | necesita-prueba | ☐ |
| 5 | Daños y perjuicios | [Pericial contable p. 18 — $2.4M lucro cesante] | [Pericial de la contraparte p. 6 — cuestiona metodología] | moderada | controvertido | ☐ |
```

Continúe con:
- **Excepciones / umbrales** (modo patente: señales de invalidez / infracción indirecta; modo civil-mercantil: excepciones oponibles, análisis de requisitos formales de la demanda)
- **Lista de lagunas** (modo civil-mercantil) / **lista de necesita-prueba** (modo patente) — **el producto prioritario**
- **Qué va a favor y qué en contra — resumen** — elementos más fuertes, elementos más débiles
- **Línea de conclusión** — *"Esta habilidad no concluye."* Elementos mapeados/acreditados: [lista]. Elementos que necesitan prueba / en estado de laguna: [lista]. Elementos que dependen de interpretación (patente) / controvertidos (civil-mercantil): [lista]. Se requiere el criterio del abogado.
- **Verificación de citas** — cada cita puntual, caso, columna/línea, minuto de audiencia, foja debe verificarse contra la fuente.

### CSV (siempre)

Dos archivos por cuadro:
- `[slug-cuadro].csv` — valores
- `[slug-cuadro]_sources.csv` — citas textuales, citas puntuales, notas

**Seguridad de celdas CSV / hoja de cálculo.** Antes de escribir cualquier valor de celda, revise el primer carácter. Si es `=`, `+`, `-`, `@`, tabulación (`\t`), o retorno de carro (`\r`), anteponga un apóstrofo simple (`'`) para neutralizar la interpretación de fórmulas de Excel/Sheets. Las pruebas textuales de fuentes adversarias (escritos de la contraparte, manuales de producto, documentos de terceros, arte previo, transcripciones de audiencia, documentos del expediente) pueden contener cadenas que una hoja de cálculo ejecutará como fórmulas (`=HYPERLINK(...)`, `=cmd|...!A1`, `+WEBSERVICE(...)`), convirtiendo el cuadro en un vector de exfiltración de datos o ejecución remota cuando un abogado lo abre. El entrecomillado RFC 4180 por sí solo no lo impide — el `=` inicial aún se interpreta. Aplique el prefijo apóstrofo en CSV, XLSX y Sheets. Registre las celdas donde se aplicó para que el revisor pueda ver qué citas fueron neutralizadas.

### Hoja de cálculo (Excel o Sheets)

Pregunte en cuál trabaja el equipo. Use el patrón de la habilidad `tabular-review` de `corporativo-legal-mexico` — mismo modelo de citas a nivel de celda, misma codificación de colores por estado, misma columna `Verificado`, misma hoja de esquema:

- Una fila por elemento (o elemento × objetivo si se comparan múltiples objetivos)
- Cada columna de prueba pareada con una columna oculta de fuente que contiene la cita textual y la cita puntual; comentarios de celda (Excel) o notas (Sheets) muestran la cita al pasar el cursor
- Codificación de colores por estado:
  - *Patente:* blanco = `mapeado`, amarillo = `depende-interpretacion` / `parcial`, naranja = `necesita-prueba`, rojo = `no-encontrado`
  - *Civil-mercantil:* blanco = `acreditado`, amarillo = `parcial` / `controvertido`, naranja = `necesita-prueba`, rojo = `laguna`
- Columna `Verificado` por columna de prueba, en blanco por defecto — el revisor la marca
- Hoja `_elements` documentando la fuente de los elementos: ley sustantiva (artículo, fracción, inciso), código procesal, jurisprudencia (Época, Registro, Instancia, Materia, Tesis), o parseo de reivindicación. Esto es lo que hace auditable el cuadro — un lector puede ver de dónde vinieron los elementos.
- Hoja `_lagunas` listando cada fila en `laguna`, `necesita-prueba` o `necesita-prueba` con lo que falta
- Solo para modo patente: hoja `_parseo-reivindicacion` (descomposición de elementos), hoja `_interpretaciones` (términos en disputa e interpretaciones asumidas)

Aplique la neutralización de prefijo apóstrofo a cada celda escrita en la hoja de cálculo.

Anteponga el encabezado de producto de trabajo como la fila superior. Junto a él, incluya:

> Este cuadro se deriva de documentos fuente que pueden estar sujetos a secreto profesional, confidencialidad, o ambos. Hereda el estatus de los documentos fuente — su distribución fuera del círculo profesional puede comprometer la confidencialidad. Almacene con los archivos confidenciales del asunto y tome decisiones de distribución deliberadamente. Nada en este cuadro ha sido presentado ante autoridad alguna; es un borrador para revisión del abogado.

### Nombre de archivo y ubicación

- Infracción de patente: `cuadro-infraccion-[num-patente]-reiv[#]-[objetivo]-AAAA-MM-DD.{md,csv,xlsx}`
- Invalidez de patente: `cuadro-invalidez-[num-patente]-reiv[#]-[ref]-AAAA-MM-DD.{md,csv,xlsx}`
- Civil-mercantil: `cuadro-elementos-[slug-accion]-[parte]-AAAA-MM-DD.{md,csv,xlsx}`
- Revisión: `revision-cuadro-[tema]-AAAA-MM-DD.{md,csv,xlsx}`

Si los espacios de trabajo de asuntos están habilitados y hay un asunto activo: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/matters/<matter-slug>/claim-charts/`. De lo contrario: `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/claim-charts/`. Muestre la ruta. Agregue una entrada de una línea al `history.md` del asunto.

## Resumen de lectura

Después de escribir el cuadro, dé un resumen de una pantalla:

- Acción(es) / excepción(es) / reivindicación(es), objetivo(s), jurisdicción, fase
- Elementos cuadrados · acreditados/mapeados · parciales · controvertidos · laguna / necesita-prueba · no-encontrados
- La lista de lagunas (civil-mercantil) o la lista de necesita-prueba (patente) — **esta es la lista prioritaria**
- Dónde están los archivos de salida
- Recordatorio: cada celda es una pista. El cuadro es un borrador, no un escrito / dictamen / sentencia.

## Puerta de no-abogado

Si `## Who's using this` Rol es No-abogado:

> Este cuadro es un borrador de investigación, no un escrito judicial. Presentar escritos, firmar demandas, o basarse en esto para una opinión sobre el fondo tiene consecuencias procesales y sustantivas. Un abogado con cédula profesional y habilitación en la jurisdicción relevante debe revisar antes de que esto se use para cualquier propósito legal.
>
> Aquí tiene un resumen de una página para llevar a un abogado:
>
> [Genere: acción / patente, parte, jurisdicción, fase, elementos, conteos de acreditado / laguna / necesita-prueba, las tres preguntas abiertas más relevantes.]

Entregue el cuadro junto con el resumen.

## Salvaguardas compartidas — lista de verificación

- **Verificación de citas.** Cada cita puntual (columna/línea, página, minuto de audiencia, foja, párrafo) es una afirmación sobre la fuente. El abogado verifica. La habilidad no fabrica citas — si una cita no puede producirse, la celda es `necesita-prueba` o `laguna`.
- **Atribución de fuente.** Cada cita textual tiene su fuente en el CSV compañero y la columna oculta de fuente de la hoja de cálculo. Una cita sin fuente no es prueba.
- **Sin suplemento silencioso.** Prueba escasa significa `necesita-prueba` / `laguna`, no "extrapolar." No llene desde búsqueda web, conocimiento de entrenamiento, o "cómo suelen resolverse estos casos" para cerrar una laguna.
- **Verificación de espacio de trabajo.** Confirme el asunto activo antes de escribir. Nunca escriba el cuadro del asunto A en la carpeta del asunto B.
- **Postura de decisión.** Cuando haya duda de si un elemento está acreditado, señale; no decida. `parcial` le dice al abogado qué parte falta.
- **Inyección de fórmulas.** Cada celda escrita a CSV / XLSX / Sheets se verifica para `=`, `+`, `-`, `@`, `\t`, `\r` iniciales y se prefija con `'`. Predeterminado: neutralizar-y-escribir.
- **Elementos son específicos por jurisdicción y materia.** La biblioteca de plantillas es una línea base. La ley sustantiva y el código procesal aplicables prevalecen.
- **Un cuadro no es un escrito, un dictamen, ni una sentencia.** Cada salida es un borrador.
- **Secreto profesional.** Toda la salida está sujeta al deber de secreto profesional del abogado. No comparta fuera del círculo profesional sin autorización expresa.

---

## Relación con otras habilidades

- `propiedad-intelectual-legal-mexico:triaje-infraccion` (modo patente) — la primera revisión rápida. Esta habilidad es el cuadro completo que sigue.
- `propiedad-intelectual-legal-mexico:fto-triage` — el FTO usa la misma mecánica desde la postura del potencialmente acusado. Si evalúa su propio producto vs. una patente de tercero, redirija a FTO y use el formato de esta habilidad.
- `corporativo-legal-mexico:tabular-review` — el patrón subyacente de citas a nivel de celda y estado de verificación. Un cuadro de elementos es una revisión tabular especializada.
- `litigacion-legal-mexico:chronology` — la cronología es la línea de tiempo; el cuadro de elementos es la matriz de prueba. Una entrada de cronología frecuentemente se convierte en la cita de prueba de una celda.
- `litigacion-legal-mexico:preparacion-pruebas` — una celda en `necesita-prueba` frecuentemente se convierte en un tema de testimonial o pericial. Después de una audiencia, la nueva prueba llena celdas.
- `litigacion-legal-mexico:redaccion-escritos` — la sección de hechos de un escrito de alegatos frecuentemente se construye directamente de las filas acreditadas del cuadro de elementos.

---

## Cierre con el árbol de decisión de siguientes pasos

Cierre con el árbol de decisión de siguientes pasos conforme al CLAUDE.md `## Outputs`. Personalice las opciones a lo que esta habilidad acaba de producir — las cinco ramas predeterminadas (redactar el X, escalar, obtener más hechos, vigilar y esperar, algo más) son un punto de partida, no un candado. El árbol es la salida; el abogado elige.

## Lo que esta habilidad NO hace

- **No concluye.** Ni infracción, ni no-infracción, ni responsabilidad, ni no-responsabilidad. Jamás.
- **No decide la interpretación de reivindicaciones** (patente) ni **los elementos controlantes** (civil-mercantil). Señala términos en disputa / elementos base y cuadra bajo supuestos declarados.
- **No acredita el estándar de prueba para invalidez** ni **la carga probatoria en sentencia**. Produce un borrador prima facie para revisión del abogado.
- **No sustituye el análisis pericial.** Revisión de código fuente, desmontajes, peritos técnicos, peritos en daños son productos de trabajo separados a los que este cuadro redirige, no reemplaza.
- **No presenta, firma ni promueve nada.** Cada salida es un borrador. Un abogado presenta y firma.
- **No extrapola.** Si la prueba no está ahí, la celda es `necesita-prueba` / `laguna` — nunca una suposición.
