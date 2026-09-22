---
name: revision-arrendamiento
description: >
  Usar cuando el usuario pida revisar, marcar o evaluar un contrato de
  arrendamiento de inmueble — casa-habitación, departamento, local comercial,
  oficina, bodega, nave industrial, terreno o predio agropecuario — bajo el
  código civil de la entidad donde se ubica el inmueble. Disparadores: "revisa
  este arrendamiento", "contrato de renta", "revisa el contrato del local",
  "qué riesgos tiene este arrendamiento", "redlines al arrendamiento",
  "¿puedo firmar este contrato de renta?", o cuando otra skill enrute aquí un
  arrendamiento de inmueble. No usar para arrendamiento financiero (LGTOC) ni
  para arrendamiento de muebles o vehículos.
argument-hint: "[pega el contrato o da la ruta — o ejecuta y pide el documento]"
---

# /revision-arrendamiento

1. Leer el perfil de práctica (Paso 0). Si no existe o tiene `[PLACEHOLDER]`, detener y dirigir a `/civil-legal-mexico:cold-start-interview`. Si el asunto no revela la entidad del inmueble o el lado que se representa, preguntarlo antes de citar.
2. Cargar el contrato (pegado, ruta de archivo o carpeta del asunto activo).
3. Clasificar: destino del inmueble, lado, entidad, ¿es arrendamiento financiero?
4. Recorrer el checklist de 14 temas cláusula a cláusula, con la tabla de reglas irrenunciables como filtro final.
5. Emitir el análisis con el formato de salida estándar.
6. Cerrar con árbol de decisión.

---

## Propósito

El arrendamiento de inmuebles en México es **derecho estatal**. Cada código civil fija sus propios plazos máximos, umbrales de inscripción, derechos de preferencia, avisos de terminación y reglas de orden público, con numeración distinta. Un contrato redactado con machote de otra entidad, o revisado con el Código Civil Federal en la cabeza, produce una revisión que parece correcta y no lo es.

Esta skill recorre el contrato buscando tres cosas: (a) las cláusulas que contradicen una regla **irrenunciable** del código de la entidad y por tanto se tendrán por no puestas; (b) las omisiones que la ley suple con una regla por defecto que quizá no conviene al lado que representas; y (c) las posiciones negociables que vale la pena pelear. Produce señales, no dictamina — el abogado decide qué señal activa una negociación.

La revisión opera sobre lo que está en el documento. No supone intención de las partes ni hechos fuera del contrato salvo que el usuario los proporcione.

---

## Contexto del asunto

Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si está deshabilitado, omitir — las skills usan contexto a nivel práctica. Si está habilitado y no hay asunto activo, preguntar: "¿Para qué asunto es esto?" y cargar `matter.md` (su `## Entidad federativa` prevalece sobre la entidad principal del perfil). Escribir salidas en `~/.claude/plugins/config/claude-for-legal/civil-legal-mexico/matters/<matter-slug>/`. Administrar asuntos con `/civil-legal-mexico:matter-workspace`.

---

## Marco legal aplicable

1. Leer `## Entidades federativas` del perfil de práctica. Determinar la entidad que rige **este** asunto: la **ubicación del inmueble** (no el domicilio de las partes ni el lugar de firma). Si no es evidente en el contrato ni en el perfil, **preguntar antes de citar**. No asumir una entidad por defecto.
2. Citar el **código civil de esa entidad**. El Código Civil Federal solo se cita como referencia supletoria o comparativa, y se dice expresamente que lo es.
3. Si no se tiene a la vista el texto vigente del código estatal, toda cita lleva `[VERIFICAR: <código> art. <n>]`. Nunca trasladar la numeración del CCF ni la de otra entidad a un código estatal: la numeración difiere entre entidades.
4. Materia procesal (vía para desahucio, rescisión, cobro de rentas): la transición al Código Nacional de Procedimientos Civiles y Familiares avanza entidad por entidad. Toda afirmación sobre la vía o los plazos procesales lleva `[VERIFICAR: estatus CNPCF en <entidad>]` salvo que se haya confirmado en esta sesión.

### Entidad verificada: Jalisco

Para inmuebles ubicados en Jalisco, **leer `references/ccj-jalisco-arrendamiento.md` antes de citar**. Contiene los artículos operativos del Título Sexto (arts. 1980-2146) y las disposiciones conexas (1313, 1743, 1792, 1896-1897, 1974-1979), verificados contra la compilación del Congreso del Estado. Las citas tomadas de ahí llevan `[settled — last confirmed 2026-09-22]`; si esa fecha tiene más de seis meses, degradar a `[model knowledge — verify]` y confirmar contra la compilación vigente (LegalDataHunter → OrdenJuridicoEstatal, o el PDF del Congreso).

Los números de artículo que aparecen en el checklist de abajo son **de Jalisco**. Para otra entidad, el tema del checklist se conserva y la cita se sustituye por `[VERIFICAR: <código estatal> — <tema>]`.

### Otras entidades

Sin tabla verificada. Aplicar el checklist completo, citar con `[VERIFICAR]`, y decir en la nota del revisor: "Entidad sin referencia verificada en este plugin; los números de artículo son conocimiento del modelo." Ofrecer en el árbol de decisión buscar el código estatal vía LegalDataHunter si el conector responde.

---

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa (`.claude-legal/civil-legal-mexico/CLAUDE.md` del proyecto, o `~/.claude/plugins/config/claude-for-legal/civil-legal-mexico/CLAUDE.md`). Extraer:

- Rol del usuario (abogado / no abogado) → decide el encabezado de confidencialidad y el modo de salida
- Entidad(es) federativa(s) de la práctica
- Lado habitual (arrendador / arrendatario / ambos)
- Postura de riesgo y cadena de escalamiento

Si el perfil no existe o contiene `[PLACEHOLDER]`: **detener** y decir: "Este plugin necesita configuración antes de dar resultados útiles. Ejecuta `/civil-legal-mexico:cold-start-interview` — toma entre 8 y 12 minutos y fija la entidad federativa, el lado habitual y el playbook de los que depende esta revisión." No continuar con un perfil genérico: una revisión sin entidad fijada es la que cita el código equivocado con seguridad.

Con el perfil configurado, dos datos siguen dependiendo del asunto y se preguntan si el contrato no los revela: la **entidad del inmueble** (puede diferir de la entidad principal del perfil; la tabla de `## Entidades federativas` dice si hay referencia verificada) y el **lado que se representa** en este contrato (el perfil da el lado habitual, no el de este asunto).

### Paso 1: clasificar

Antes de leer cláusula a cláusula, fijar cuatro datos. Si el contrato no los revela, preguntar.

| Dato | Opciones | Por qué importa |
|---|---|---|
| **Destino** | habitación / comercio / industria / oficina (≈ comercio) / agropecuario / mixto | Cambia el plazo máximo, el umbral de inscripción, la prórroga legal, los topes de renta y el régimen fiscal |
| **Lado** | arrendador / arrendatario / revisión neutral (p. ej., para un fiador) | Invierte la posición recomendada en casi todos los temas |
| **Entidad** | la del inmueble | Fija el código aplicable — ver Marco legal |
| **¿Hay opción de compra? ¿De qué tipo?** | no / civil entre particulares / financiero | Dos figuras distintas. **(a) Arrendamiento financiero:** el arrendador es una arrendadora financiera, SOFOM o entidad regulada, y las rentas amortizan el precio como operación de crédito → **detener**: es LGTOC, no arrendamiento civil. Decirlo y rutear a la skill de revisión de contratos del plugin comercial cuando esté instalado; mientras, `/corporativo-legal-mexico:revision-contratos` (si está instalado) aplica el checklist universal. **(b) Opción de compra entre particulares:** arrendador particular, precio de venta pactado desde el inicio, opción al vencimiento → **continuar** con los 14 temas **y** aplicar el bloque "Opción de compra civil" del tema 3. |

Si el destino es **mixto** (local con vivienda arriba, por ejemplo), aplicar el régimen más protector al arrendatario en los temas donde difieren y marcar `[review]` la elección.

### Paso 2: cargar y dimensionar el contrato

Leer el contrato completo, anexos incluidos (inventario, reglamento del condominio, carta de fiador, póliza jurídica). Si es extenso (más de ~50 páginas con anexos), leer primero: declaraciones, objeto, plazo, renta, garantías, terminación, jurisdicción; luego el resto; y registrar la cobertura en la línea **Leído:** de la nota del revisor.

Si no puedes leer un archivo señalado, decirlo: ruta equivocada, alcance del plugin o formato no legible — y pedir que lo peguen.

### Paso 3: checklist por tema

Para cada tema: qué buscar, por qué importa, posición por lado, y la cita (Jalisco verificada, o `[VERIFICAR]` para otra entidad). Cada hallazgo recibe severidad en la escala canónica 🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo. Ante duda entre dos severidades, redondear arriba y marcar `[review]`.

#### 1. Partes, personalidad y legitimación para arrendar

- **Buscar:** quién firma por el arrendador y con qué título: propietario, copropietario, usufructuario, albacea, tutor, apoderado. Si es apoderado, ¿el poder es para actos de administración o de dominio, y qué límites tiene?
- **Por qué importa:** puede arrendar quien tiene la libre disposición o autorización de éste (Jalisco art. 1983); el apoderado se sujeta a los límites del poder (art. 1984); el **copropietario de bien indiviso necesita el consentimiento de la mayoría de intereses** (art. 1986 fr. II); servidores públicos no pueden arrendar bienes que administran (art. 1986 fr. IV). Un arrendador sin legitimación produce un contrato que el verdadero titular puede desconocer.
- **Arrendatario:** exigir que las declaraciones identifiquen el título de propiedad (escritura, folio real) y el poder con datos de inscripción; pedir copia. **Arrendador:** declarar la legitimación con precisión para blindar la oponibilidad.
- 🔴 si el firmante no acredita título ni poder; 🟠 si hay poder pero sin datos ni límites; 🟡 si falta el folio real.

#### 2. Objeto, destino y uso de suelo

- **Buscar:** descripción del inmueble (superficie, ubicación, colindancias, folio real), instalaciones y accesorios, estado que guarda, inventario anexo; **destino pactado** y cláusula de uso exclusivo; quién obtiene licencia de giro, uso de suelo, protección civil.
- **Por qué importa:** el contenido mínimo del art. 2023 exige descripción detallada, instalaciones, estado, destino y quién paga los servicios públicos; su omisión no invalida pero deja huecos que la ley suple. Recibido sin descripción, **se presume en buen estado** (art. 2018), lo cual perjudica al arrendatario al devolverlo. Usar el bien para destino distinto es causa de rescisión a favor del arrendador (art. 2144 fr. II). Ambas partes deben acatar normas de desarrollo urbano y protección civil, y si eso vuelve oneroso el cumplimiento pueden optar por rescisión o renegociación (art. 2052).
- **Arrendatario:** exigir inventario fotográfico firmado y que el arrendador declare que el uso de suelo permite el giro; condicionar la vigencia a la obtención de licencias. **Arrendador:** cargar al arrendatario licencias de giro y cumplimiento normativo del negocio, conservando para sí la responsabilidad estructural.
- 🟡 por cada fracción del art. 2023 ausente; 🟠 si no hay inventario y el lado representado es el arrendatario; 🟠 si el destino pactado es incompatible con el uso de suelo declarado.

#### 3. Plazo, prórroga y tácita reconducción

- **Buscar:** plazo determinado o indefinido; fecha de inicio (¿coincide con la entrega?); prórrogas pactadas y sus condiciones; cláusula que niegue la tácita reconducción; renuncias a prórroga legal.
- **Por qué importa:** Jalisco fija **máximos por destino** — habitación 15 años (art. 2039), comercio 20 e industria 25 (art. 2045), agropecuario 25 (art. 2054). Sin plazo expreso, el contrato es **por tiempo indefinido** (art. 2034) y termina con aviso indubitable de 3 meses si lo da el arrendador y 1 mes si lo da el arrendatario en predio urbano, 9 meses en rústico — **regla irrenunciable** (art. 2035). El arrendatario cumplido tiene **prórroga legal**: 1 año en habitación (art. 2044), **una cuarta parte del plazo original** en comercio e industria (art. 2051). Si al vencer continúa sin oposición, opera la **tácita reconducción** hasta por un tiempo igual al pactado, con renta actualizada al interés legal, y cualquiera de las partes puede terminarla con el aviso del art. 2035 (art. 2143). Si el contrato incluye muebles (amueblado), su arrendamiento dura lo mismo que el del inmueble salvo pacto (art. 2065). En habitación de valor hasta 10,000 UMA, el plazo mínimo es de un año y **obliga solo al arrendador** (art. 2041 fr. II).
- **Arrendatario:** verificar que el plazo no exceda el máximo (el exceso se reduce o se discute `[review]`); conservar la prórroga legal; pactar renovación con aviso y condiciones claras. **Arrendador:** cláusula expresa de que la entrega al vencimiento es inmediata (art. 2143 bis) y de que la permanencia posterior no constituye nuevo contrato; exigir aviso de no renovación con antelación mayor a la legal solo si lo da el arrendatario (la del arrendador no puede reducirse).
- 🔴 renuncia a la prórroga legal o a los avisos del art. 2035; 🔴 plazo mínimo habitacional impuesto al arrendatario en inmueble hasta 10,000 UMA; 🟠 plazo que excede el máximo legal; 🟡 plazo sin fecha de inicio ligada a la entrega.

**Opción de compra civil (solo si el Paso 1 la detectó).** En Jalisco es un contrato con capítulo propio (arts. 2097-2113). Verificar: plazo **forzoso para ambas partes** (art. 2097; sin término, se entiende un año, art. 2100); **precio de venta o bases para determinarlo** — sin ellos el contrato degrada a arrendamiento simple y el arrendatario no puede exigir la venta (arts. 2101-2102); los siete contenidos obligatorios del art. 2099 (término, precio, plazo de aviso de compra, pago periódico, lugar y plazos, uso, prórroga y sus derechos); notificación del arrendador con **30 días** para ejercer la opción (art. 2103); **escritura pública** en inmuebles (art. 2104); **inscripción en el Registro Público**, que vuelve inoponibles gravámenes y traslaciones posteriores (art. 2105) y cuya omisión da acción de daños al arrendatario (art. 2106); régimen de evicción y defensa de la posesión a cargo del arrendador (arts. 2108-2111). **Arrendatario:** exigir escritura e inscripción, precio cierto, y que los pagos periódicos se imputen al precio si así se negoció. **Arrendador:** aviso de compra con plazo cierto, rescisión judicial por incumplimiento (art. 2112). 🔴 opción de compra de inmueble en contrato privado sin escritura ni inscripción; 🔴 sin precio ni bases cuando representas al arrendatario que cuenta con comprar; 🟠 sin plazo de aviso de compra.

#### 4. Renta, moneda, incrementos y forma de pago

- **Buscar:** monto, periodicidad, día de pago, lugar y medio (transferencia, efectivo), moneda, cláusula de incremento (índice INPC, porcentaje fijo, tope), renta variable sobre ingresos, renta anticipada, intereses moratorios, emisión de recibos o CFDI.
- **Por qué importa:** a falta de pacto, la renta de inmuebles se paga **por meses vencidos** en el lugar de entrega del bien (art. 2007) y **no se debe hasta recibir el bien** (art. 2006). En comercio e industria la renta es **libre** y puede fijarse como porcentaje de ingresos brutos (arts. 2046-2047). En habitación de inmueble hasta 10,000 UMA la renta **no puede exceder 12 % anual del valor fiscal ni 10 % del comercial** — orden público, y los pactos más gravosos son nulos aunque consten en recibos o cartas (arts. 2041-2043). El arrendador **debe entregar recibos**; su entrega presume el contrato y el pago (art. 1995 fr. IX); el arrendatario puede consignar si se los niegan (art. 2005 fr. V). El arrendador puede subir la renta proporcionalmente si hace mejoras o el bien se sujeta a plusvalía o cuotas municipales (art. 2024). **Intereses moratorios:** tope por remisión a mutuo — legal 9 %, moratorio máximo el natural más 50 %, nulo el anatocismo (arts. 1981 Bis, 2005 fr. VIII, 1976-1979). Renta en dólares: aplicar el análisis de moneda del checklist universal de `/corporativo-legal-mexico:revision-contratos` (si está instalado) — obligación en moneda extranjera pagadera en pesos al tipo de cambio del día de pago salvo pacto de pago efectivo en esa moneda `[VERIFICAR: Ley Monetaria art. 8]`.
- **Arrendatario:** día de pago con período de gracia; incremento topado a INPC; moratorios dentro del tope legal; obligación expresa de CFDI. **Arrendador:** renta anticipada explícita en el contrato (art. 1991 la protege frente a nuevo adquirente solo si consta ahí); incremento anual automático; renta variable con auditoría de ingresos.
- 🔴 interés moratorio que rebase el tope legal o pacto de capitalización; 🔴 renta habitacional arriba del tope del art. 2041 en inmueble que califica; 🟠 renta en moneda extranjera sin cláusula de conversión; 🟠 incremento sin índice ni tope; 🟡 sin obligación de recibo/CFDI.

#### 5. Fiscal

- **Buscar:** quién paga predial, IVA sobre renta, retención de ISR e IVA cuando el arrendatario es persona moral, CFDI con complemento, régimen del arrendador (persona física con actividad de arrendamiento, persona moral, fideicomiso).
- **Por qué importa:** el arrendador debe entregar el inmueble **al corriente de contribuciones** previas al contrato (art. 1995 fr. VI). Renta habitacional exenta de IVA; comercial gravada; retenciones cuando paga persona moral `[model knowledge — verify]`. El civilista señala; el detalle es fiscal.
- Marcar `[review]` y rutear a `/fiscal-legal-mexico:cfdi-review` para validar CFDI, retenciones y deducibilidad.
- 🟡 si el contrato calla sobre IVA y retenciones en arrendamiento comercial; 🟠 si carga al arrendatario el predial de ejercicios anteriores.

#### 6. Depósito y garantías

- **Buscar:** depósito en garantía (monto, si genera intereses, plazo y condiciones de devolución, contra qué se aplica); fiador u obligado solidario (¿identifica inmueble libre de gravamen?, ¿renuncia a beneficios de orden y excusión?, ¿su obligación cubre prórrogas y tácita reconducción?); póliza jurídica; fianza de institución; garantía prendaria.
- **Por qué importa:** la garantía es contenido mínimo (art. 2023 fr. VI). El arrendador **debe devolver el saldo** a favor del arrendatario al terminar y, si tiene un derecho que ejercitar, **debe depositarlo judicialmente**, no retenerlo (arts. 1995 fr. VIII, 2002, 2008). El arrendador no puede rehusar un fiador que reúna los requisitos legales (art. 1994). **Las obligaciones de terceros garantes cesan al vencer el plazo determinado, salvo convenio en contrario** (art. 2143 último párrafo): sin pacto expreso, el fiador no cubre la tácita reconducción ni la prórroga.
- **Arrendatario:** depósito de un mes con devolución en plazo cierto (15-30 días) contra acta de entrega; prohibir su aplicación a renta corriente; fiador con obligación acotada al plazo original. **Arrendador:** fiador que renuncie a orden y excusión, identifique inmueble con folio real y **extienda expresamente su obligación a prórrogas, reconducción y renovaciones**; depósito aplicable a daños, servicios y rentas vencidas.
- 🔴 cláusula que autorice al arrendador a quedarse el depósito sin depósito judicial ni rendición de cuentas; 🟠 fiador sin inmueble identificado o sin extensión a prórrogas cuando representas al arrendador; 🟠 depósito sin plazo de devolución cuando representas al arrendatario. Fianza de institución afianzadora → `/seguros-legal-mexico:poliza-review`. Hipoteca u obligado solidario con inmueble → skill de garantías civiles de este plugin cuando exista; mientras, analizar aquí y marcar `[review]`.

#### 7. Conservación, reparaciones, vicios ocultos y mejoras

- **Buscar:** reparto de reparaciones (mayores / menores / "todas a cargo del arrendatario"); plazo del arrendador para reparar; derecho a reducir renta o rescindir por falta de reparación; obligación de avisar; régimen de mejoras (autorización, quién paga, destino al término, derecho de retirarlas).
- **Por qué importa:** el arrendador conserva y hace las **reparaciones necesarias** no imputables al arrendatario (art. 1995 fr. II); el arrendatario hace las de **poca cuantía** que exige el uso (art. 2019) y debe **avisar** la necesidad de reparar bajo pena de daños (art. 1997). Si el arrendador no repara, el arrendatario elige rescindir o pedir al juez que lo constriña (art. 1998); si pierde el uso por reparaciones más de un mes, puede no pagar, reducir o rescindir (art. 2020). El arrendador responde de **vicios ocultos** anteriores y aun sobrevenidos sin culpa del arrendatario (arts. 1995 fr. V, 2001). El arrendatario **no puede variar la forma** del bien sin consentimiento expreso (art. 2016). **Mejoras:** el arrendador las paga si las autorizó y se obligó, si son útiles y el contrato se rescinde por su culpa, o en plazo indeterminado si concluye antes de que el arrendatario se compense (art. 2003); en esos dos últimos casos el reembolso procede **aunque se haya pactado que las mejoras quedan a beneficio del bien** (art. 2004). Responsabilidad por incendio del arrendatario salvo caso fortuito o vicio (art. 2015); en industria peligrosa **debe asegurar la finca** (art. 2031).
- **Arrendatario:** cláusula de "todas las reparaciones a cargo del arrendatario" limitada a menores; plazo del arrendador para reparar con derecho a hacerlas y compensar; mejoras útiles reembolsables o retirables. **Arrendador:** consentimiento escrito para obras; mejoras a beneficio del inmueble sin reembolso salvo art. 2004; seguro de contenidos y RC a cargo del arrendatario.
- 🟠 reparaciones estructurales o de vicios ocultos cargadas al arrendatario; 🟠 mejoras sin regla de destino ni autorización; 🟡 sin plazo para reparar; 🟢 falta de cláusula de seguro en giro no peligroso.

#### 8. Subarrendamiento, cesión y traspaso

- **Buscar:** prohibición absoluta, autorización general o consentimiento caso por caso; cesión del contrato; traspaso del negocio (comercio e industria); cambio de control del arrendatario persona moral.
- **Por qué importa:** sin consentimiento **no puede subarrendar ni ceder**; si lo hace, responde solidariamente con el subarrendatario y es causa de rescisión (arts. 2137, 2144 fr. III). Con autorización general responde como si él siguiera en el uso (art. 2138); con aprobación expresa del subarriendo concreto, el subarrendatario queda **subrogado** (art. 2139). En comercio e industria, **si se pacta**, el arrendatario puede **traspasar** el negocio sin oposición y cobrar por ello; queda **obligado solidario** del nuevo ocupante en todos los traspasos subsecuentes, y el plazo del nuevo es el original (arts. 2048-2050).
- **Arrendatario (comercial):** pactar el derecho de traspaso del art. 2048 y la posibilidad de subarrendar parcialmente a filiales. **Arrendador:** consentimiento previo y escrito caso por caso; cambio de control equiparado a cesión; solidaridad expresa.
- 🟠 traspaso pactado sin solidaridad expresa cuando representas al arrendador; 🟠 prohibición absoluta de subarriendo o cesión a filiales cuando representas a un arrendatario corporativo; 🟡 silencio sobre cambio de control.

#### 9. Derecho de preferencia y derecho del tanto

- **Buscar:** cláusula de preferencia para renovar; renuncia a la preferencia; cláusula de derecho del tanto en venta; procedimiento de aviso y plazos.
- **Por qué importa:** en Jalisco el arrendatario tiene **preferencia para el nuevo arrendamiento** solo si el contrato **duró más de tres años**, está al corriente y no se retrasó dos meses (art. 2025); el arrendador debe avisar las nuevas condiciones **al menos diez días antes** del vencimiento y el arrendatario responde en **cinco días** (art. 2027); la violación no anula el nuevo arrendamiento pero genera **daños mínimos del 10 % de la renta bruta anual** (art. 2028). El **derecho del tanto en venta NO es general**: solo lo tiene el arrendatario que hizo **mejoras de importancia con autorización** del arrendador, con el procedimiento de los arts. 1896-1897 (aviso fehaciente, quince días) (art. 2026). No trasladar aquí la regla de CDMX o del CCF. **Prórroga legal vs. preferencia:** son dos derechos distintos y el código no articula su secuencia. La prórroga (arts. 2044, 2051) extiende el **mismo** contrato a favor del arrendatario cumplido; la preferencia (arts. 2025-2028) opera sobre el **nuevo** arrendamiento en igualdad de condiciones. Postura prudente al revisar: el aviso del art. 2027 debe darse antes de que venza el plazo o su prórroga, y el arrendador que quiere recuperar el inmueble debe contar con que el arrendatario cumplido puede primero exigir la prórroga y después invocar la preferencia. Marcar `[review]` la interpretación en cualquier calendario de salida.
- **Arrendatario:** pactar preferencia para renovar desde el primer contrato (la legal exige tres años) y derecho del tanto convencional sin condicionarlo a mejoras. **Arrendador:** limitar la preferencia a la legal y documentar el aviso del art. 2027 en el calendario.
- 🟡 renuncia genérica a la preferencia `[review: renunciabilidad del art. 2025 no está declarada irrenunciable, pero el art. 2028 sanciona su violación]`; 🟢 ausencia de derecho del tanto convencional (no es defecto, es posición).

#### 10. Enajenación del inmueble e inscripción en el Registro Público

- **Buscar:** cláusula de subsistencia ante venta; obligación de notificar al arrendatario el cambio de arrendador; obligación de inscribir y quién paga; declaración de gravámenes o hipoteca sobre el inmueble.
- **Por qué importa:** si cambia el titular, **el arrendamiento subsiste** (art. 1989) y el arrendatario paga al nuevo arrendador desde la notificación judicial, notarial o con acuse firmado (arts. 1990-1991). La **inscripción es obligatoria** arriba del umbral por destino: habitación > 5 años (art. 2039), comercio e industria > 8 años (art. 2045), agropecuario > 10 años (arts. 2055-2056, imputable al arrendador); si debe inscribirse, entre dos arrendamientos **solo vale el inscrito** (art. 2021). En venta judicial subsiste salvo celebrado dentro de los 60 días previos al secuestro o después de registrada la hipoteca que da lugar a la subasta (art. 2146).
- **Arrendatario:** exigir inscripción cuando el plazo lo requiera o cuando haya hipoteca previa (art. 2146 lo expone), a costa del arrendador o compartida; cláusula de notificación de venta. **Arrendador:** inscribir si el plazo lo exige (es obligación, no opción) y pactar el reparto de derechos registrales.
- 🔴 plazo arriba del umbral **sin** previsión de inscripción; 🟠 hipoteca previa declarada sin inscripción del arrendamiento cuando representas al arrendatario; 🟡 sin cláusula de notificación de cambio de arrendador.

#### 11. Terminación, rescisión, pena convencional y entrega

- **Buscar:** causales de rescisión pactadas vs. legales; plazo de cura; pena convencional por terminación anticipada o por mora en la entrega; renuncia a la rescisión por caso fortuito; procedimiento de entrega (acta, inventario, servicios pagados); pacto comisorio; cláusula de terminación anticipada del arrendatario.
- **Por qué importa:** causales legales del arrendador (art. 2144: falta de pago, uso distinto, subarriendo sin permiso, daños graves, variar la forma, servicios impagos más de dos meses) y del arrendatario (art. 2145: falta de conservación, pérdida total o parcial, reparación mayor a un mes, vicios ocultos, servicios impagos a cargo del arrendador). Rescisión por caso fortuito que impida el uso más de un mes: **irrenunciable** (arts. 2012-2013). Si la única causal es falta de pago y el arrendatario exhibe el pago antes de sentencia, **el juez debe sobreseer**: orden público, irrenunciable (art. 1792). Devolución anticipada en plazo fijo: se debe la totalidad del precio (art. 2010 frs. I y III) — de ahí que la pena por terminación anticipada deba negociarse. **Pena convencional: no puede exceder la obligación principal** (art. 1313), se reduce proporcionalmente al cumplimiento parcial (arts. 1314-1315) y no se acumula con el cumplimiento salvo pena por retardo (art. 1316). Al terminar, se debe renta hasta entregar en las condiciones en que se recibió (art. 2009) y el arrendatario entrega constancias de no adeudo de servicios (art. 2005 fr. VII). Abandono más dos meses de impago permite la entrega con certificación judicial (art. 2142). Cada parte devuelve de inmediato el saldo a favor de la otra (art. 2008). Rentas vencidas **prescriben en dos años** escalonadamente (art. 1743). Muerte de cualquiera de las partes **no rescinde** salvo pacto (art. 1988).
- **Arrendatario:** derecho de salida anticipada con aviso y pena de uno a tres meses de renta; plazo de cura de 10-15 días antes de rescindir por impago; acta de entrega con plazo para que el arrendador objete. **Arrendador:** pena por salida anticipada dentro del tope del art. 1313; rescisión por impago de una sola mensualidad con plazo de cura corto; entrega inmediata al vencimiento (art. 2143 bis) con pena diaria por retardo.
- 🔴 renuncia a los arts. 2012-2013 o al 1792; 🔴 pena convencional que exceda la obligación principal (p. ej., totalidad de rentas restantes más pena adicional); 🟠 sin plazo de cura cuando representas al arrendatario; 🟠 pacto de que la muerte del arrendatario termina el contrato en habitación `[review]`; 🟡 sin procedimiento de entrega.

#### 12. Declaración de uso lícito y extinción de dominio

- **Buscar:** declaración del arrendatario de que destinará el inmueble a fines lícitos y de que los recursos con que paga son de procedencia lícita; obligación de informar hechos ilícitos; derecho del arrendador a rescindir por uso ilícito; deslinde del arrendador para acreditar buena fe.
- **Por qué importa:** el Código Civil de Jalisco no regula la extinción de dominio; la fuente es la Ley Nacional de Extinción de Dominio, donde el propietario que **acredite buena fe** (desconocimiento del uso ilícito y actos razonables para impedirlo) puede oponerla `[VERIFICAR: LNED, requisitos de buena fe del tercero]`. El contrato es la prueba principal de esa buena fe. Cultivos ilícitos en predio agropecuario están expresamente prohibidos (art. 2054).
- **Arrendador:** declaración de uso lícito, obligación de permitir inspecciones razonables, rescisión inmediata por uso ilícito, obligación del arrendatario de reportar. **Arrendatario:** aceptar la declaración; acotar las inspecciones con aviso previo.
- 🟠 ausencia total de declaración de uso lícito cuando representas al arrendador; 🟢 cuando representas al arrendatario.

#### 13. Jurisdicción, ley aplicable y medios alternativos

- **Buscar:** cláusula de sumisión a tribunales (¿de la entidad del inmueble?); renuncia al fuero del domicilio; cláusula arbitral o de mediación ante centro de justicia alternativa; ley aplicable distinta a la del inmueble; domicilios convencionales para notificaciones.
- **Por qué importa:** la ley que rige el inmueble es la de su ubicación; una sumisión a tribunales de otra entidad es válida pero complica ejecución y desahucio `[review]`. La vía procesal para rescisión, desahucio y cobro depende de si en la entidad ya rige el CNPCF o el código procesal local — `[VERIFICAR: estatus CNPCF en <entidad>]`. Cláusula arbitral en arrendamiento habitacional con parte no comerciante: ejecutabilidad y proporcionalidad `[review]`. Mediación previa obligatoria: verificar que no bloquee medidas urgentes.
- **Ambos lados:** tribunales de la ubicación del inmueble; domicilios convencionales completos; correo electrónico para avisos solo como complemento del aviso indubitable, no como sustituto.
- 🟠 sumisión a tribunales de otra entidad o ley extranjera; 🟡 avisos solo por correo electrónico cuando la ley exige forma indubitable; 🟡 arbitraje en habitación.

#### 14. Datos personales del arrendatario y del fiador

- **Buscar:** qué datos recaba el arrendador (INE, comprobantes de ingresos, buró de crédito, datos del fiador), si hay aviso de privacidad, si se comparten con póliza jurídica o administradora.
- **Por qué importa:** el arrendador que recaba datos personales es responsable bajo la LFPDPPP y debe poner a disposición un aviso de privacidad; el fiador es titular de datos aunque no sea parte principal.
- Señalar y rutear a `/privacidad-legal-mexico:aviso-privacidad`. 🟡 si no hay aviso y hay recolección extensa; 🟢 en lo demás.

### Paso 4: filtro de reglas irrenunciables (Jalisco)

Después del checklist, pasar el contrato por esta tabla. **Toda cláusula que pretenda renunciar, reducir o condicionar una de estas reglas es 🔴 Bloqueante** con la cita, y la posición recomendada es "se tendrá por no puesta; eliminarla evita un litigio que se pierde". Para otra entidad, la tabla se conserva como lista de temas a `[VERIFICAR]`.

| Regla irrenunciable | Jalisco | Efecto de la cláusula contraria |
|---|---|---|
| Avisos de terminación del indefinido (3 meses arrendador / 1 mes arrendatario urbano; 9 rústico) | arts. 2035, 2143 | Nula; rige el plazo legal |
| Rescisión o reducción por caso fortuito que impida el uso más de un mes | arts. 2012-2013 | Nula |
| Obras de habitabilidad ordenadas por autoridad y daños por omitirlas | art. 2040 | Nula |
| Topes de renta y plazo mínimo en habitación hasta 10,000 UMA | arts. 2041-2043 | Nula de pleno derecho, incluso en recibos o cartas; posible responsabilidad penal |
| Sobreseimiento por exhibir el pago cuando la única causal es impago | art. 1792 | Nula |
| Tope de interés moratorio y prohibición de anatocismo | arts. 1981 Bis, 1976-1979 | Se tiene por no puesto; nulidad |
| Pena convencional que exceda la obligación principal | art. 1313 | Reducción judicial |
| Reembolso de mejoras en los casos del art. 2003 frs. II-III aunque se pacte lo contrario | art. 2004 | La cláusula no impide el reembolso |

### Paso 5: consolidar y emitir

Ordenar hallazgos por severidad descendente. Verificar que cada hallazgo tenga: cláusula, texto citado, señal, problema en una línea, posición recomendada y cita etiquetada. Verificar que ninguna cita de Jalisco salga de la tabla de referencia sin etiqueta `[settled — last confirmed 2026-09-22]`, y que ninguna cita de otra entidad salga sin `[VERIFICAR]`.

---

## Formato de salida

Emitir el análisis en este orden:

```
⚠️ Nota del revisor
- Fuentes: [Jalisco: references/ccj-jalisco-arrendamiento.md, verificado 2026-09-22 | otra entidad: conocimiento del modelo, verificar | LegalDataHunter ✓/✗]
- Leído: [contrato completo N páginas + anexos: inventario, carta fiador | páginas 1-X de Y]
- Marcado para tu criterio: [N elementos [review]]
- Vigencia: [compilación del Congreso con decretos hasta 30196/LXIV/26 | estatus CNPCF en la entidad no verificado]
- Antes de confiar: [las 1-2 cosas que el revisor debe hacer]

---

CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO [o encabezado según rol en el perfil]

# Revisión de Contrato de Arrendamiento — [inmueble / partes]
**Partes:** [arrendador] / [arrendatario]   **Fecha:** [...]   **Lado que representa:** [...]
**Entidad:** [...]   **Destino:** [habitación / comercio / industria / agropecuario]   **Plazo:** [...]   **Renta:** [...]

## Señales de alto impacto 🔴 [N]
[Solo Bloqueante/Alto que requieren negociación o acción antes de firmar — reglas irrenunciables violadas primero]

## Resumen ejecutivo
[5-8 líneas: qué hace el contrato, cuál es el riesgo principal para el lado representado, cuál es la posición general]

## Análisis por cláusula

### [Número de cláusula] — [Nombre]
> **Texto:** "[cita textual relevante]"

**Señal:** [🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Sin señal]
**Problema:** [Una línea]
**Fundamento:** [Código Civil de <entidad> art. N — etiqueta de fuente]
**Posición recomendada:** [Qué pedir o proponer, desde el lado representado]
[review] si requiere criterio del abogado

## Omisiones que la ley suple
[Temas del checklist sin cláusula: qué regla por defecto aplica y si conviene al lado representado]

## Cláusulas sin señal
[Lista de cláusulas revisadas sin observaciones]

## Resumen de señales
| # | Cláusula | Tema | Severidad | Problema en una línea | Fundamento |
|---|---|---|---|---|---|
| 1 | § [X] — [Nombre] | [tema 1-14] | 🔴 | [Descripción breve] | art. N |

## Calendario derivado del contrato
| Evento | Fecha o plazo | Fundamento |
|---|---|---|
| Aviso de nuevas condiciones para preferencia | ≥ 10 días antes del vencimiento | art. 2027 |
| Aviso de no renovación / terminación | [según contrato y art. 2035] | |
| Devolución del depósito | [plazo pactado] | |
| Prescripción de rentas más antiguas | 2 años desde cada vencimiento | art. 1743 |

**Una pregunta que haría y que no está en mi checklist:** [observación de segundo orden — omitir si no hay una genuina]
```

Si hay más de ~10 hallazgos, ofrecer el dashboard conforme al perfil de práctica (no construirlo sin que lo pidan).

> **¿Qué sigue? Elige una opción y te ayudo a desarrollarla:**
> 1. **Redactar el marcado de cambios** — produzco la versión con cambios propuestos cláusula a cláusula desde el lado que representas, con nota explicativa por cambio.
> 2. **Carta a la contraparte** — redacto la comunicación con los puntos a negociar, ordenados por prioridad.
> 3. **Obtener más información** — antes de cerrar necesitaría: [folio real y gravámenes del inmueble / poder del firmante / valor comercial o fiscal para el art. 2041 / uso de suelo]. Las redacto como solicitud al cliente o la contraparte.
> 4. **Buscar el código estatal** — si el inmueble no está en Jalisco y LegalDataHunter responde, busco el título de arrendamiento del código de la entidad y re-cito con etiqueta de fuente.
> 5. **Escalar** — nota breve al [aprobador según perfil] con los 🔴 y la decisión que se necesita.
> 6. **Algo diferente** — dime qué harías con esto.

---

## Ruteo

| Situación | Destino |
|---|---|
| El incumplimiento **ya ocurrió** (rentas vencidas, negativa a desocupar) y hay que demandar | `/litigacion-legal-mexico:plantillas-demanda arrendamiento-renta` |
| Es arrendamiento **financiero** (LGTOC: arrendadora financiera, rentas que amortizan el precio) | Skill de revisión de contratos del plugin comercial cuando esté instalado; mientras, `/corporativo-legal-mexico:revision-contratos` para el checklist universal |
| Opción de compra **entre particulares** | Se queda aquí: bloque "Opción de compra civil" del tema 3 |
| Renta en moneda extranjera, pena convencional compleja, cláusulas universales (confidencialidad, fuerza mayor, notificaciones) | Checklist universal de `/corporativo-legal-mexico:revision-contratos` (si está instalado) |
| CFDI, IVA, retenciones, deducibilidad | `/fiscal-legal-mexico:cfdi-review` |
| Fianza emitida por institución afianzadora o póliza jurídica con aseguradora | `/seguros-legal-mexico:poliza-review` |
| Aviso de privacidad para datos del arrendatario y fiador | `/privacidad-legal-mexico:aviso-privacidad` |
| Hipoteca, prenda, obligado solidario con inmueble | Skill de garantías civiles de este plugin cuando exista; mientras, analizar en el tema 6 y marcar `[review]` |
| Inmueble ejidal o comunal, o arrendador extranjero en zona restringida | Detener el análisis civil ordinario, advertir régimen agrario o de inversión extranjera `[VERIFICAR]`, y rutear a especialista |
| Pregunta doctrinal sobre arrendamiento sin contrato que revisar | Responder directamente con el marco legal de esta skill; no forzar el formato de revisión |

---

## Errores que esta skill existe para evitar

| Error | Corrección |
|---|---|
| Citar numeración del CCF o de CDMX como si fuera de Jalisco | Solo `references/ccj-jalisco-arrendamiento.md` para Jalisco; `[VERIFICAR]` para todo lo demás |
| Tratar el derecho del tanto como derecho general del arrendatario | En Jalisco es condicional a mejoras autorizadas (art. 2026) |
| Decir "conviene inscribir" cuando el plazo rebasa el umbral | Arriba del umbral la inscripción es obligatoria y el no inscrito pierde frente al inscrito (arts. 2021, 2039, 2045, 2055) |
| Asumir que el fiador cubre la tácita reconducción | Cesa al vencer el plazo salvo pacto expreso (art. 2143) |
| Aplicar la misma prórroga legal a todo destino | Habitación 1 año; comercio e industria ¼ del plazo (arts. 2044, 2051) |
| Calificar como "aconsejable" la eliminación de una renuncia a regla irrenunciable | Es 🔴: la cláusula se tendrá por no puesta y su sola presencia es un litigio perdido |
| Continuar la revisión de un arrendamiento financiero con este checklist | Detener y rutear: es LGTOC |
| Tratar toda opción de compra como arrendamiento financiero | Entre particulares es civil y tiene capítulo propio en Jalisco (arts. 2097-2113): exige escritura pública e inscripción |

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
