---
name: written-consent
description: >
  Redacta resoluciones unánimes fuera de asamblea del Consejo de Administración,
  de un comité o de la Asamblea de Accionistas en formato interno, con búsqueda
  de precedentes en el repositorio de resoluciones. Maneja resoluciones
  múltiples, señalamiento de conflictos de consejeros, requisitos de la LGSM
  (Art. 143 para el Consejo, Art. 178 para la Asamblea), y seguimiento de
  firmantes, con advertencia incorporada de alcance para acciones relevantes de
  única ocasión. Usar cuando el usuario diga "resoluciones fuera de asamblea",
  "resoluciones unánimes", "consentimiento del consejo", "resolución sin sesión",
  "acuerdo fuera de asamblea", o describa una acción que requiera aprobación del
  consejo o de la asamblea sin necesidad de sesión presencial.
argument-hint: "[describe la acción que requiere aprobación del consejo o asamblea]"
---

# /written-consent

1. Carga `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → Board & Secretary (repositorio de resoluciones, lenguaje de resoluciones, entidad de constitución, composición del Consejo).
2. Usa el flujo de trabajo a continuación.
3. Identifica la acción y clasifícala (rutinaria / requiere revisión).
4. Si requiere revisión: muestra la advertencia de abogado externo y confirma antes de proceder.
5. Busca en el repositorio de resoluciones el precedente más cercano. Si no hay repositorio: usa las resoluciones semilla de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`.
6. Redacta la resolución en formato interno usando el precedente como base.
7. Resultado: borrador de resolución + lista de firmantes + avisos de revisión.

---

## Contexto del asunto

**Contexto del asunto.** Revisa `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omite el resto de este párrafo — las habilidades usan el contexto a nivel de práctica y el sistema de asuntos es invisible. Si está habilitado y no hay un asunto activo, pregunta: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Carga el `matter.md` del asunto activo para contexto y sobreescrituras específicas del asunto. Escribe los resultados en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leas archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

La mayoría de las aprobaciones rutinarias del Consejo de Administración o de la Asamblea de Accionistas no necesitan una sesión presencial. Nombramientos de funcionarios, otorgamiento de poderes, autorizaciones bancarias, aprobaciones de contratos que superan el umbral de los funcionarios, arreglos intercompañía — estos pueden resolverse mediante resoluciones unánimes fuera de asamblea. Esta habilidad las redacta rápidamente en tu formato interno, encuentra la resolución previa más cercana a lo que necesitas, y señala las acciones donde debes obtener la revisión de un abogado externo antes de que alguien firme.

**Marco legal mexicano:** En México, las resoluciones fuera de asamblea se rigen por dos disposiciones distintas de la LGSM:

- **Art. 143 LGSM — Consejo de Administración:** Permite que el Consejo tome resoluciones fuera de sesión "en los términos que establezcan los estatutos." Los estatutos sociales deben prever expresamente esta posibilidad; si son silentes, las resoluciones del Consejo deben tomarse en sesión.
- **Art. 178 LGSM — Asamblea de Accionistas:** Las resoluciones tomadas fuera de asamblea requieren el consentimiento UNÁNIME de TODOS los accionistas que representen la totalidad del capital social. Esto es más restrictivo que el equivalente estadounidense (unanimous written consent) — no admite excepciones ni umbrales menores.

Esta habilidad produce ambos tipos de resoluciones. Identifica cuál aplica según el órgano que resuelve (Consejo o Asamblea) y aplica los requisitos correspondientes.

## Advertencia de alcance — leer antes de redactar

> **Esta habilidad está diseñada para resoluciones del día a día con precedentes directos en tu repositorio o documentos semilla.** Acciones rutinarias — nombramientos de funcionarios, otorgamiento de poderes, autorizaciones anuales, aprobaciones estándar de contratos — son el caso de uso adecuado. La habilidad encuentra una resolución previa que coincida cercanamente, la adapta a la acción actual y produce un borrador limpio.
>
> **Para acciones relevantes de única ocasión, la revisión de abogado externo es prudente independientemente de lo que produzca esta habilidad.** Esto incluye: operaciones de M&A (compraventa de acciones, compraventa de activos, fusiones, inversiones), rondas de financiamiento, emisiones de capital a nuevos inversionistas, disposiciones de cambio de control, disolución o liquidación, operaciones inmobiliarias relevantes, reformas a los estatutos sociales o al acta constitutiva, y cualquier acción que será objeto de escrutinio en un proceso posterior de due diligence.
>
> La habilidad señalará automáticamente cuando la acción parezca ser relevante de única ocasión. Ese señalamiento no es un bloqueo — puedes proceder. Es un aviso para reflexionar sobre si un borrador adaptado de precedente es suficiente para esta acción en particular.

---

## Acción relevante + urgencia = detente

Una resolución fuera de asamblea para una acción relevante de única ocasión (M&A, financiamiento, disolución, cambio en estructura de capital, designación de consejeros vinculada a un financiamiento o M&A) que el usuario quiere firmada HOY — "envía para firma electrónica esta tarde", "la junta es en una hora", "se firma esta noche", "necesitamos esto antes de la apertura del mercado" — pasa por revisión de abogado externo. No porque la habilidad no pueda redactarla — sino porque una resolución incorrecta en una acción relevante es una puerta sin retorno, y la presión de urgencia es exactamente cuando ocurren los errores.

Disparador (ambos deben ser verdaderos):

1. La acción está en la categoría de **Requiere revisión — acción relevante de única ocasión** más abajo (M&A, financiamiento, disolución, cambio de estructura de capital, disposición de cambio de control, designación de consejeros vinculada a un financiamiento o M&A, operación inmobiliaria relevante, cualquier acción que aparecerá como anexo de aprobación del consejo en un futuro data room de financiamiento o M&A).
2. La solicitud del usuario contiene una señal de irreversibilidad — "enviar para firma electrónica", "firmar hoy", "el consejo firma esta tarde/noche", "necesitamos esto antes de [apertura de mercado / cierre / la sesión de las X]", cualquier frase que comprometa la resolución a firma en el mismo turno.

Cuando ambos sean verdaderos, muestra esto y detente:

> ⛔ **Acción relevante + firma el mismo día — no marcaré esto como listo para firmar.**
>
> Esta es [tipo de acción], que es una puerta sin retorno. Has pedido que se firme hoy. Esa combinación es exactamente cuando los errores en una resolución del consejo o la asamblea se vuelven más difíciles de revertir.
>
> Redactaré el borrador — con gusto — pero no lo marcaré como listo para firmar sin que un abogado externo lo revise. Si ya hay abogado externo involucrado en esta operación, entrégale este borrador. Si no, para esto es exactamente el abogado externo. Contacta a la Barra Mexicana de Abogados, al Colegio de Abogados local o a la Dirección General de Profesiones (SEP) para un servicio de referencia que pueda encontrar uno el mismo día si es necesario.
>
> Dos opciones:
>
> 1. **Yo redacto, el abogado externo revisa, luego las firmas** — la ruta normal para una acción corporativa relevante. Dime que redacte y lo haré.
> 2. **El abogado externo ya está en esta operación y autorizó la vía del borrador** — dime quién revisó y cuándo. Procederé e incluiré una nota de que el abogado externo tiene el borrador.
>
> No redactaré en formato "listo para enviar" bajo presión de firma el mismo día sin una de esas dos opciones. Esto no es un retraso — es la única forma en que una resolución de acción relevante firmada el mismo día es defendible si alguien revisa el expediente después.

No procedas al Paso 1 ni a ninguna redacción bajo esta compuerta sin una respuesta explícita eligiendo la opción 1 o la opción 2. Una resolución rutinaria sin disparador de acción relevante, o una resolución de acción relevante sin la solicitud de firma el mismo día, sigue el flujo normal a continuación — el señalamiento de "Revisión de abogado externo recomendada" en la categoría de acción relevante de única ocasión sigue aplicándose pero no genera un bloqueo total.

---

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → `## Board & Secretary`:
  - Ubicación del repositorio de resoluciones
  - Lenguaje interno de resoluciones
  - Entidad de constitución (para requisitos de la LGSM y estatutos sociales)
  - Composición del Consejo de Administración (para lista de firmantes), incluyendo Comisario
  - Resoluciones fuera de asamblea — alcance y cualquier límite

### Bloqueo total por falta de precedente

Si (a) no hay repositorio de resoluciones configurado en `## Board & Secretary` → Consents repository, Y (b) no se ha proporcionado ningún documento semilla de resolución a esta habilidad (ni subido en esta sesión ni referenciado en la sección `## Board & Secretary` → Consent format con lenguaje extraído de resoluciones/considerandos/autorizaciones de un documento semilla específico), **DETENTE antes de redactar**. No procedas al Paso 1 de recopilación, no redactes desde una plantilla genérica, no "comiences" con un formato de relleno.

Muestra exactamente este bloque y espera una respuesta:

> **No hay precedente disponible — detengo antes de redactar.**
>
> No tengo un precedente que coincida. Una resolución fuera de asamblea redactada sin tu formato interno requerirá más correcciones de las que ahorra — el lenguaje de resoluciones, la profundidad de los considerandos, el texto de autorización y las convenciones del bloque de firmas contienen decisiones específicas del formato interno que el revisor reescribirá desde cero si parto de una plantilla genérica.
>
> Dos opciones para desbloquear:
>
> 1. **Pega o sube una resolución previa** (cualquier resolución unánime fuera de asamblea reciente de esta empresa en cualquier categoría — extraeré el formato, no el contenido), O
> 2. **Dime "redacta desde una plantilla genérica de todas formas — yo ajustaré las formalidades"** — solo elige esta opción si sabes que reelaborarás el lenguaje de resoluciones, el estilo de considerandos y el bloque de autorización a mano antes de circularlo. Dilo explícitamente; no lo inferiré.
>
> ¿Qué prefieres hacer?

NO procedas sin una respuesta explícita eligiendo una de esas dos opciones. Los intentos de redacción sin precedente son el resultado con mayor proporción de retrabajo-a-valor que esta habilidad puede producir — el bloqueo total es intencional.

---

## Paso 1: Identificar la acción

Pregunta al usuario qué acción necesita aprobar el Consejo o la Asamblea. Recopila:

- **¿Qué órgano resuelve?** Consejo de Administración / Comité / Asamblea General de Accionistas (Ordinaria o Extraordinaria). Esto determina si aplica el Art. 143 LGSM (Consejo) o el Art. 178 LGSM (Asamblea).
- **¿Qué se está aprobando?** (Una oración.)
- **¿Algún detalle de soporte?** Por ejemplo: el nombre del funcionario que se nombra, el monto y precio de la emisión de acciones, la contraparte y valor del contrato.
- **Fecha de efectividad:** ¿Hoy, o una fecha específica?
- **Firmantes:** ¿Todo el Consejo, o un comité específico? ¿O todos los accionistas? Si el `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` indica en el alcance de resoluciones fuera de asamblea que ciertas acciones requieren sesión presencial en lugar de resolución fuera de asamblea, señálalo ahora.
- **¿Algún conflicto de interés de consejero/accionista?** ¿Algún consejero o accionista tiene un interés material en la acción que se aprueba? Si es así: señálalo. El consejero con conflicto podría aún poder firmar dependiendo de los estatutos sociales y la naturaleza del conflicto, pero la resolución debe revelarlo y el usuario debe confirmar.

### Clasificación de la acción

Clasifica la acción antes de buscar precedente:

**Rutinaria — probable precedente directo:**
- Nombramiento o remoción de funcionarios (Director General, directores de área)
- Otorgamiento, modificación o revocación de poderes
- Autorización o actualización de firmas bancarias
- Aprobación de un contrato por debajo del umbral de materialidad
- Resoluciones de autorización anual (asuntos fiscales, planes de prestaciones, etc.)
- Préstamo o contrato de servicios intercompañía en términos de mercado
- Cambio de domicilio social (dentro de la misma entidad federativa)

**Requiere revisión — acción relevante de única ocasión, abogado externo prudente:**
- Operación de M&A (adquisición, fusión, compraventa de activos o acciones, inversión)
- Nueva ronda de financiamiento o línea de crédito
- Emisión de acciones a un nuevo inversionista
- Disposición o activación de cambio de control
- Aprobación de un acuerdo que por sí mismo requiere aprobación del Consejo o la Asamblea conforme al acta constitutiva, los estatutos sociales o los convenios entre accionistas
- Disolución, liquidación o concurso mercantil
- Operación inmobiliaria relevante
- Reformas a los estatutos sociales o al acta constitutiva (requiere Asamblea Extraordinaria y protocolización)
- Cualquier acción que aparecerá como anexo de aprobación del consejo en un futuro data room de financiamiento o M&A

Si la acción está en la categoría de requiere revisión, muestra esto antes de redactar:

> ⚠️ **Revisión de abogado externo recomendada.** Esto parece ser [tipo de acción], que es una acción corporativa relevante donde un borrador adaptado de precedente podría no ser suficiente. Considera que un abogado externo lo revise antes de circularlo. ¿Quieres que proceda con un borrador de todas formas?

---

## Paso 2: Buscar precedente

### Si el repositorio de resoluciones está conectado

Busca en el repositorio la resolución previa más cercana. Estrategia de búsqueda:

1. Busca por palabra clave del tipo de acción (p. ej., "nombramiento de funcionario", "otorgamiento de poderes", "autorización bancaria", "emisión de acciones")
2. Devuelve la resolución más reciente que coincida, o pregunta al usuario si hay varios resultados cercanos:

> Encontré [N] resoluciones previas que se parecen a esta:
>
> 1. [Título / descripción de la resolución] — [Fecha]
> 2. [Título / descripción de la resolución] — [Fecha]
>
> ¿Cuál es la más cercana a lo que necesitas? ¿O debo usar la más reciente?

3. Lee la resolución seleccionada. Extrae: lenguaje de resoluciones, estructura de considerandos, lenguaje de autorización, cualquier condición o salvedad específica.
4. Registra cualquier diferencia entre la acción previa y la actual que necesitará actualizarse en el borrador.

### Si no hay repositorio (solo documentos semilla)

Extrae el formato de las resoluciones semilla en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Nota que no hay búsqueda de precedentes disponible — el borrador seguirá el formato interno pero sin coincidencia sustantiva de precedente. Señálalo al usuario:

> No hay repositorio de resoluciones conectado, así que estoy trabajando desde tus documentos semilla para el formato. Para este tipo de acción específicamente, podrías querer verificar si tienes una resolución previa para usar como punto de partida sustantivo.

---

## Paso 3: Redactar la resolución

Usa el formato interno. La estructura a continuación es el estándar — adáptala para coincidir con el precedente o formato semilla exactamente.

```
RESOLUCIONES UNÁNIMES FUERA DE [SESIÓN DEL CONSEJO DE ADMINISTRACIÓN / ASAMBLEA]
DE [NOMBRE DE LA EMPRESA], S.A. DE C.V.

[Fecha]

Los suscritos, quienes constituyen [la totalidad de los miembros del
Consejo de Administración / la totalidad de los accionistas que representan
el 100% del capital social] de [Nombre de la Empresa], S.A. de C.V. (la
"Sociedad"), sociedad mercantil constituida conforme a las leyes de los
Estados Unidos Mexicanos, adoptan las siguientes resoluciones por unanimidad
fuera de [sesión / asamblea], de conformidad con [el artículo 143 de la Ley
General de Sociedades Mercantiles y los estatutos sociales de la Sociedad /
el artículo 178 de la Ley General de Sociedades Mercantiles], en sustitución
de una [sesión del Consejo / Asamblea General de Accionistas]:

[ENCABEZADO DEL ASUNTO / ACCIÓN — si son resoluciones múltiples]

CONSIDERANDO QUE, [antecedente — una o dos oraciones exponiendo los hechos
relevantes y por qué se solicita al órgano que actúe]; y

CONSIDERANDO QUE, [considerando adicional si es necesario]; y

POR LO TANTO, SE RESUELVE, QUE [la acción específica que se aprueba,
en lenguaje preciso — nombrar personas, indicar montos, hacer referencia
al acuerdo o instrumento específico cuando aplique];

SE RESUELVE ADEMÁS, QUE [cualquier resolución relacionada o de implementación
— p. ej., los funcionarios específicos autorizados para firmar documentos,
la autoridad otorgada, el otorgamiento de poderes necesarios];

SE RESUELVE ADEMÁS, QUE los funcionarios de la Sociedad quedan, y cada uno
de ellos queda, autorizado e instruido para, en nombre y representación de
la Sociedad, realizar todas las acciones y otorgar, suscribir y entregar
todos los documentos, instrumentos, certificados y acuerdos que dichos
funcionarios consideren necesarios o convenientes para llevar a cabo el
objeto y propósito de las resoluciones anteriores; y

SE RESUELVE ADEMÁS, QUE cualesquier acciones previamente realizadas por
cualquier funcionario de la Sociedad en relación con lo anterior se ratifican,
confirman y aprueban en todos sus aspectos.

[Repetir bloque CONSIDERANDO / SE RESUELVE para cada acción adicional si la
resolución es múltiple]

Las presentes resoluciones podrán firmarse en uno o más ejemplares, cada uno
de los cuales se considerará un original y todos en conjunto constituirán un
solo instrumento. Las firmas electrónicas, en términos de la Ley de Firma
Electrónica Avanzada y demás legislación aplicable, tendrán la misma validez
que las firmas autógrafas para todos los efectos legales.

[BLOQUES DE FIRMA — uno por cada firmante requerido]

_______________________________
[Nombre del Consejero / Accionista]
[Cargo, si aplica]
Fecha: _______________

[Repetir para cada consejero / accionista / miembro del comité]
```

### Notas de redacción de resoluciones

- **Sé preciso.** Las resoluciones vagas generan problemas en due diligence. "Se aprobó la operación" no es útil. "Se aprobó el Contrato de Compraventa de Acciones de fecha [fecha] entre [Comprador] y [la Sociedad], sustancialmente en la forma que se adjunta como Anexo A" sí lo es.
- **Nombra a los firmantes autorizados.** No digas solo "los funcionarios" si un funcionario específico necesita autoridad para algo específico. Nómbralos. Indica los poderes que se otorgan o que ya tienen.
- **Referencia anexos.** Si se está aprobando un documento, adjúntalo como anexo y refiérelo en la resolución. La resolución es tan útil como su especificidad.
- **Coincide con el lenguaje interno exactamente.** "SE RESUELVE, QUE" vs. "SE ACUERDA, QUE" vs. "POR LO TANTO SE RESUELVE" — usa lo que sea que esté en el precedente o documentos semilla. No cambies de formato dentro de una misma resolución.

---

## Paso 4: Confirmar los requisitos legales conforme a la LGSM y los estatutos sociales

Revisa la información de la entidad en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Investiga los requisitos para resoluciones fuera de asamblea antes de finalizar el borrador:

**Para resoluciones del Consejo de Administración (Art. 143 LGSM):**
- ¿Los estatutos sociales prevén expresamente la posibilidad de tomar resoluciones fuera de sesión? Si no lo prevén, la resolución debe tomarse en sesión presencial.
- ¿Qué requisitos establecen los estatutos sociales? (unanimidad, mayoría calificada, forma de firma, plazos)
- ¿Existe alguna restricción en los estatutos sobre qué asuntos pueden resolverse fuera de sesión?

**Para resoluciones de la Asamblea de Accionistas (Art. 178 LGSM):**
- Se requiere el consentimiento UNÁNIME de TODOS los accionistas que representen la TOTALIDAD del capital social. No hay excepción a este requisito.
- ¿Los estatutos sociales establecen requisitos adicionales?
- Nota: La resolución debe registrarse en el Libro de Actas de Asambleas de Accionistas.

**Requisitos generales:**
- ¿Qué forma de firma es válida? (firma autógrafa, firma electrónica avanzada conforme a la Ley de Firma Electrónica Avanzada, ejemplares)
- ¿El acta constitutiva o los estatutos sociales sobreescriben alguna regla predeterminada — p. ej., un umbral de firma más alto, una ventana de notificación diferente, una restricción sobre qué acciones pueden tomarse por resolución fuera de asamblea?

**Protocolización:** Determina si la resolución debe protocolizarse ante Notario Público e inscribirse en el Registro Público de Comercio. Esto es obligatorio cuando la resolución implique:
- Reformas a los estatutos sociales o al acta constitutiva
- Aumento o disminución del capital social
- Fusión, escisión o transformación de la sociedad
- Disolución y liquidación
- Otros actos que conforme a la LGSM deban constar en escritura pública

Cita las disposiciones legales específicas y cualquier cláusula del acta constitutiva o estatutos sociales en que te apoyes. Verifica vigencia — la LGSM y la legislación mercantil se reforman periódicamente. Señala incertidumbre para verificación del abogado en lugar de afirmar una regla que no has confirmado.

Si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` registra una posición interna sobre cualquiera de estas cuestiones, aplícala y anota el fundamento legal en que se apoya. Agrega un bloque breve de "Requisitos legales LGSM" al resultado resumiendo lo que confirmaste (o señalaste) para que el usuario no se quede con dudas.

---

## Paso 4.5: Compuerta de acción consecuente (ejecutar resolución)

**Antes de proceder al resultado:** Lee `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si el Rol es **No abogado**:

> Ejecutar una resolución fuera de asamblea tiene consecuencias legales — vincula a la sociedad y se convierte en un registro corporativo. ¿Has revisado esto con un abogado? Si sí, procede. Si no, aquí hay un resumen para llevarles:
>
> - Cuál es la acción (la resolución)
> - Qué encontró el análisis (requisitos de la LGSM, umbral de firmas, cualquier conflicto señalado, necesidad de protocolización)
> - Preguntas abiertas (cualquier punto señalado para verificación del abogado arriba)
> - Qué podría salir mal (resolución inválida, incumplimiento de deberes fiduciarios, defecto en las firmas, conflicto no manejado adecuadamente, falta de protocolización cuando es requerida)
> - Qué preguntar al abogado (¿es este el vehículo adecuado?; ¿faltan considerandos?; ¿los estatutos sociales permiten resolución fuera de asamblea para esta acción?; ¿se requiere protocolización?)
>
> Si necesitas encontrar un abogado titulado: contacta a la Barra Mexicana de Abogados, al Colegio de Abogados local o a la Dirección General de Profesiones (SEP) para un servicio de referencia profesional.

No produzcas el borrador definitivo listo para firma pasada esta compuerta sin un sí explícito. Investigación, extracción de formato y un borrador marcado como BORRADOR para revisión del abogado están bien.

---

## Paso 5: Resultado

Produce:

1. **El borrador de la resolución** — completo, listo para revisar y circular. La resolución fuera de asamblea ejecutada en sí misma es un registro corporativo, no privilegiado; no apliques el encabezado de producto de trabajo a la resolución tal como se circula. Las notas de redacción, el seguimiento de firmantes y el análisis a continuación son producto de trabajo — antepón el encabezado de producto de trabajo de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` `## Resultados` (difiere según el rol del usuario — ver `## Quién usa este plugin`):

   ```
   [ENCABEZADO DE PRODUCTO DE TRABAJO — según ## Resultados del plugin — difiere por rol; ver `## Quién usa este plugin`]
   ```

2. **Lista de firmantes:**
```
[ENCABEZADO DE PRODUCTO DE TRABAJO — según ## Resultados del plugin — difiere por rol; ver `## Quién usa este plugin`]

LISTA DE FIRMANTES — [Acción] — [Fecha]

Firmantes requeridos ([unanimidad conforme al Art. 178 LGSM para Asamblea /
conforme a estatutos sociales para Consejo]):
□ [Nombre del Consejero / Accionista 1]
□ [Nombre del Consejero / Accionista 2]
□ [Nombre del Consejero / Accionista 3]
[etc. — tomado de la composición del Consejo o lista de accionistas en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`]

Revelación de conflictos:
[Ninguno / [Nombre del Consejero/Accionista] tiene un interés declarado — confirmar si la recusación o revelación es apropiada]

Requisitos legales LGSM: [regla confirmada para el tipo de sociedad y órgano que resuelve / confirmar]
Protocolización requerida: [Sí — indicar motivo / No / Verificar con abogado]
```

3. **Avisos de revisión:**
```
[ENCABEZADO DE PRODUCTO DE TRABAJO — según ## Resultados del plugin — difiere por rol; ver `## Quién usa este plugin`]

ANTES DE CIRCULAR — verificar:
□ El lenguaje de las resoluciones describe precisamente la acción (sin aprobaciones vagas)
□ Fecha de efectividad correcta
□ Todos los anexos requeridos adjuntos y referenciados
□ Firmantes autorizados nombrados correctamente
□ Cualquier conflicto de consejero/accionista revelado o resuelto
□ Para acciones relevantes: abogado externo ha revisado
□ Requisitos de protocolización verificados (si aplica, ¿se ha programado cita con Notario Público?)
□ ¿Se registrará en el Libro de Actas correspondiente?
□ ¿El órgano que resuelve es el correcto conforme a la LGSM y los estatutos sociales?
```

4. **Nota final sobre el borrador — agregar antes de circulación.** Anteponer al borrador de la resolución como una nota previa a la ejecución separada, y eliminar antes de que la resolución se firme:

> Este es un borrador para revisión del abogado, no una resolución ejecutada. Ejecutarla vincula a la sociedad y se convierte en un registro corporativo — un abogado titulado la revisa, edita según sea necesario y asume responsabilidad profesional antes de que se envíe para firma. No circule para firma sin revisión previa.

---

## Lo que esta habilidad no hace

- No determina si una acción legalmente requiere aprobación del Consejo o de la Asamblea — ese juicio corresponde al abogado.
- No asesora sobre deberes fiduciarios de los consejeros ni sobre la resolución de conflictos de interés — señala conflictos, el abogado los maneja.
- No sustituye la revisión de abogado externo para operaciones relevantes — la advertencia de alcance es genuina, no formularia.
- No circula la resolución — el resultado es para que el abogado revise y envíe mediante su propio proceso.
- No da seguimiento a las firmas devueltas — la lista de firmantes es un punto de partida; el seguimiento de firmas es manual o se maneja mediante tu proceso de gestión documental.
- No determina si la resolución requiere protocolización ante Notario Público — esa determinación la hace el abogado conforme a la LGSM y los estatutos sociales.
- No verifica si los estatutos sociales permiten resoluciones fuera de sesión para el Consejo (Art. 143 LGSM) — el abogado debe confirmar que los estatutos contemplan esta posibilidad.
