---
name: board-minutes
description: >
  Redacta actas de sesión del Consejo de Administración o de comités en el
  formato interno de la empresa. Detecta automáticamente sesiones próximas del
  consejo y comités desde el calendario, solicita el orden del día y materiales
  de lectura previa, y produce un borrador completo en el formato aprendido de
  las actas semilla. También maneja resoluciones unánimes fuera de asamblea.
  Disparadores: "acta del consejo", "redactar acta", "sesión del consejo
  próxima", "acta de comité", "resoluciones fuera de asamblea", o detección
  en calendario de un evento próximo del consejo o comité.
---

# Actas de Sesión del Consejo de Administración

## Contexto del asunto

**Contexto del asunto.** Revisa `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel de práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omite el resto de este párrafo — las habilidades usan el contexto a nivel de práctica y el sistema de asuntos es invisible. Si está habilitado y no hay un asunto activo, pregunta: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Carga el `matter.md` del asunto activo para contexto y sobreescrituras específicas del asunto. Escribe los resultados en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leas archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

Las actas de sesión del Consejo de Administración son un registro legal. Deben ser precisas, completas y en un formato que resista cualquier escrutinio — ya sea una revisión de due diligence para un financiamiento, una investigación regulatoria o un data room de M&A. Esta habilidad las redacta en tu formato interno para que dediques tu tiempo a revisar y corregir, no a formatear y retranscribir.

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → sección `## Board & Secretary`:
  - Formato de actas (narrativa extensa / actas de acuerdos / híbrido)
  - Plantilla de actas extraída de documentos semilla (estructura, lenguaje de resoluciones, formato de encabezado)
  - Composición del Consejo de Administración y comités (incluido el Comisario, órgano de vigilancia obligatorio conforme a los Arts. 164-171 LGSM)
  - Resoluciones unánimes fuera de asamblea — para qué se usan y cualquier límite
- Si `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` no tiene formato de actas: ejecuta cold-start primero. No procedas con un formato genérico.

---

## Paso 1: Identificar la sesión

### Detección por calendario

Si el conector de calendario está autorizado, busca eventos próximos que coincidan con palabras clave del consejo y comités:

**Términos de búsqueda:** "Consejo de Administración", "Sesión del Consejo", "Comité de Auditoría y Prácticas Societarias", "Comité de Compensaciones", "Comité de Nominaciones", "Comité Especial", "Asamblea General de Accionistas", "Consejo de Administración — [Empresa]"

**Ventana de tiempo:** Buscar 30 días hacia adelante. Si no se encuentra una sesión próxima, buscar 14 días hacia atrás (las actas frecuentemente se redactan después de la sesión).

Presenta lo que encuentres:

> Encontré las siguientes sesiones del consejo o comités en tu calendario:
>
> 1. **[Nombre de la sesión]** — [Fecha], [Hora], [Lugar/Virtual]
> 2. **[Nombre de la sesión]** — [Fecha], [Hora], [Lugar/Virtual]
>
> ¿Para cuál de estas son las actas? ¿O es una sesión diferente que no aparece aquí?

Si el conector de calendario no está autorizado o no devuelve resultados: pregunta directamente — qué sesión, qué fecha, qué tipo (Consejo de Administración pleno / qué comité / Asamblea General).

### Metadatos de la sesión a confirmar

Una vez identificada la sesión, confirma o completa:

- **Tipo de sesión:** Consejo de Administración pleno / [Nombre del comité] / Asamblea General Ordinaria / Asamblea General Extraordinaria
- **Fecha y hora**
- **Lugar o plataforma** (domicilio social / dirección física / Zoom / Teams / telefónica)
- **Convocatoria:** ¿Se realizó la convocatoria conforme a los estatutos sociales y la LGSM (Arts. 186-188)? (Sí / Se renunció a la convocatoria — la renuncia debe constar por escrito) Nota: Para SA, la convocatoria de primera convocatoria debe publicarse en el DOF o periódico oficial del domicilio de la sociedad.

---

## Paso 2: Asistencia

Solicita la lista de asistentes, u ofrece obtenerla de la invitación del calendario si el conector está autorizado.

**Consejeros presentes:**
- Toma como punto de partida la composición del Consejo en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`
- Pregunta quiénes estuvieron presentes, quiénes ausentes, y si algún consejero ausente tuvo aviso previo

**Comisario:**
- ¿Estuvo presente el Comisario (órgano de vigilancia)? Su presencia puede ser requerida conforme a los Arts. 164-171 LGSM. Registrar su asistencia o ausencia.

**Directivos presentes:**
- ¿Quiénes de la administración asistieron? (Director General, Director de Finanzas, Director de Operaciones, etc.)
- Nota: los directivos se enlistan por separado de los consejeros

**Invitados:**
- ¿Asistió abogado externo? (Nombre y despacho)
- ¿Auditores externos, asesores financieros u otros asesores?
- ¿Algún invitado que asistió solo para puntos específicos del orden del día? (Registrar su asistencia como limitada a ese punto)

**Presidente:**
- ¿Quién presidió la sesión?
- ¿Quién fungió como Secretario del Consejo?

**Quórum:**

- Verifica el acta constitutiva y los estatutos sociales para el requisito de quórum. Conforme a la LGSM:
  - Asamblea General Ordinaria, primera convocatoria: 50% del capital social (Art. 189 LGSM)
  - Asamblea General Ordinaria, segunda convocatoria: cualquier número de accionistas (Art. 191 LGSM)
  - Asamblea General Extraordinaria, primera convocatoria: 75% del capital social (Art. 190 LGSM)
  - Asamblea General Extraordinaria, segunda convocatoria: 50% del capital social (Art. 191 LGSM)
  - Sesiones del Consejo de Administración: conforme a los estatutos sociales; si son silentes, mayoría de consejeros (Art. 143 LGSM)
- Registra lo confirmado (fuente y cita exacta) en las notas de redacción.
- Confirma que hubo quórum. Si no: detente y señálalo antes de redactar. No produzcas actas que impliquen que se celebró válidamente una sesión. Somete la cuestión al abogado externo — la vía de remediación (ratificación, nueva sesión, resoluciones fuera de asamblea, otra) depende de la LGSM, los estatutos sociales y la naturaleza de la acción.

---

## Paso 3: Materiales

Solicita los materiales de la sesión. Estos son la fuente para los puntos del orden del día y cualquier resolución.

> ¿Puedes compartir el orden del día y los materiales de lectura previa para esta sesión? Incluso un orden del día aproximado es suficiente para estructurar las actas. Si hubo presentaciones o materiales de la administración, súbelos también — los usaré para completar los resúmenes de cada punto.
>
> Si los materiales no se distribuyeron con anticipación, dime los puntos del orden del día y redactaré marcadores de posición para cada uno.

**Del orden del día y los materiales, extrae:**
- Puntos del orden del día en orden
- Cualquier resolución propuesta (busca lenguaje de aprobación: "aprobar", "autorizar", "ratificar", "adoptar", "designar", "nombrar")
- Cualquier anexo referenciado (presentaciones de la administración, estados financieros, dictámenes legales, avalúos)
- Cualquier votación esperada

**Si no hay materiales:** Solicita los puntos del orden del día verbalmente y procede con marcadores de posición para el contenido de la discusión.

---

## Paso 4: Redactar las actas

Usa el formato interno de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. No uses un formato genérico. Las actas semilla son la plantilla — replica la estructura, el encabezado, el lenguaje de resoluciones, el nivel de detalle de la discusión.

### Estructura estándar (adaptar al formato interno)

**Bloque de encabezado:**
```
ACTA DE LA SESIÓN DEL CONSEJO DE ADMINISTRACIÓN
[O: ACTA DE LA SESIÓN DEL [NOMBRE DEL COMITÉ]]
[O: ACTA DE LA ASAMBLEA GENERAL [ORDINARIA / EXTRAORDINARIA] DE ACCIONISTAS]
DE [NOMBRE DE LA EMPRESA], S.A. DE C.V.

[Fecha]
[Domicilio social / Lugar / Sesión por medios electrónicos]
```

**Apertura:**
- Se reunió el Consejo de Administración [o el Comité / la Asamblea General] de [Empresa], S.A. de C.V., en [lugar], siendo las [hora]
- Convocatoria: [se realizó conforme a los Arts. 186-188 LGSM y los estatutos sociales / se renunció a la convocatoria — adjuntar constancia como anexo si aplica]
- Se verificó el quórum: [N de M consejeros/accionistas presentes, representando el X% del capital social]
- Presidente de la sesión: [nombre]
- Secretario del Consejo: [nombre]

**Asistentes:**
- Consejeros presentes: [lista]
- Consejeros ausentes: [lista, si aplica]
- Comisario: [nombre — presente/ausente]
- También presentes: [directivos, abogados externos, invitados — con cargos]

**Actas previas:**
Lenguaje estándar: aprobación de las actas de la sesión anterior. Toma la fecha de la sesión anterior de la sección de calendario del consejo en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` si está disponible; de lo contrario, deja como [FECHA DE LA SESIÓN ANTERIOR].

**Puntos del orden del día — una sección por punto:**

```
[TÍTULO DEL PUNTO DEL ORDEN DEL DÍA]

[Nombre del presidente/presentador] [presentó / informó sobre / dirigió la discusión sobre] [tema].

[Resumen de la discusión — ver notas de redacción más abajo]

[Si sigue una resolución:]
Después de deliberar, [por unanimidad de votos / por mayoría de votos con N votos a favor, N en contra y N abstenciones], se adoptó la siguiente resolución:

SE RESUELVE, QUE [texto de la resolución en el lenguaje interno de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`].

[O: SE ACUERDA, QUE ...]
```

**Cierre:**
Lenguaje estándar: no habiendo más asuntos que tratar, se levantó la sesión siendo las [hora] del día [fecha], firmándose la presente acta para constancia.

**Bloque de firmas:**
Firma del Secretario del Consejo y del Presidente del Consejo. El formato puede incluir también al Comisario según los estatutos sociales.

---

### Notas de redacción

**Resúmenes de discusión:** La parte más difícil de las actas es decidir cuánta discusión capturar. Sigue el formato interno de los documentos semilla exactamente:

- *Narrativa extensa:* Resume el fondo de la discusión — qué preguntas se plantearon, qué información se presentó, qué factores consideró el Consejo. No cites a individuos a menos que la atribución específica sea legalmente relevante.
- *Actas de acuerdos:* Registra solo lo que se presentó y qué acción se tomó. Sin contenido de discusión más allá de "el Consejo deliberó sobre el asunto."
- *Híbrido:* Narrativa completa para puntos relevantes (adquisiciones, estados financieros, aprobaciones significativas), solo acuerdos para puntos de rutina.

Cuando se proporcionaron materiales: extrae contenido resumido de las presentaciones y materiales de la administración. El Consejo "recibió y revisó" una presentación — resume lo que cubrió.

Cuando no hay materiales: inserta `[MARCADOR — resumir discusión aquí]` y señálalo claramente. No fabrique contenido de discusión.

**Resoluciones:** Usa el lenguaje exacto de resoluciones de las actas semilla — "SE RESUELVE, QUE" vs. "SE ACUERDA, QUE" vs. "POR LO TANTO SE RESUELVE". El lenguaje es estilo interno, no son intercambiables.

**Protocolización:** Cuando las resoluciones impliquen reformas a los estatutos sociales, aumento o disminución de capital, fusión, escisión, disolución u otros actos que conforme a la LGSM deban constar en escritura pública, incluye una nota indicando que el acta debe protocolizarse ante Notario Público e inscribirse en el Registro Público de Comercio.

**Referencias a anexos:** Numera los anexos en el orden en que aparecen (Anexo A, B, C). Anexos comunes: presentación de la administración, estados financieros, informes de valuación, opiniones legales, constancias de renuncia a la convocatoria, acreditación de quórum.

---

## Paso 4.5: Compuerta de acción consecuente (adoptar actas)

**Antes de adoptar las actas como definitivas:** Lee `## Quién usa este plugin` en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si el Rol es **No abogado**:

> Adoptar las actas las convierte en el registro oficial de lo que el Consejo decidió — son la prueba primaria de autorización para las acciones tomadas en la sesión. ¿Has revisado esto con un abogado? Si sí, procede. Si no, aquí hay un resumen para llevarles:
>
> - Qué se decidió (resoluciones, votaciones, quiénes estuvieron presentes)
> - Qué captura el borrador y qué es todavía un marcador de posición
> - Preguntas abiertas (cualquier señalamiento sobre asistencia, quórum o conflictos)
> - Qué podría salir mal (resoluciones mal redactadas, omisión de declaraciones, defectos de quórum, filtración de información privilegiada en los resúmenes de discusión, falta de protocolización cuando es requerida)
> - Qué preguntar al abogado (¿es adecuada la profundidad de la discusión para la práctica de este Consejo?; ¿las notas de sesión ejecutiva están debidamente separadas?; ¿algún punto requiere mayor documentación o protocolización?)
>
> Si necesitas encontrar un abogado titulado: contacta a la Barra Mexicana de Abogados, al Colegio de Abogados local o a la Dirección General de Profesiones (SEP) para un servicio de referencia profesional.

No produzcas la versión definitiva lista para adopción pasada esta compuerta sin un sí explícito. Un borrador marcado como BORRADOR para revisión del abogado está bien.

---

## Paso 5: Resultado y avisos de revisión

Produce el borrador completo. Las actas en sí son un registro corporativo, no privilegiado; no apliques el encabezado de producto de trabajo a las actas tal como se circulan. Las notas de redacción, los marcadores de posición y la lista de verificación de revisión a continuación son producto de trabajo — antepón el encabezado de producto de trabajo de `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` `## Resultados` (difiere según el rol del usuario — ver `## Quién usa este plugin`):

```
[ENCABEZADO DE PRODUCTO DE TRABAJO — según ## Resultados del plugin — difiere por rol; ver `## Quién usa este plugin`]
```

Después del borrador, agrega una lista de verificación de revisión:

```
[ENCABEZADO DE PRODUCTO DE TRABAJO — según ## Resultados del plugin — difiere por rol; ver `## Quién usa este plugin`]

LISTA DE VERIFICACIÓN DE REVISIÓN — favor de verificar antes de circular:

□ Todos los consejeros confirmados como presentes/ausentes (verificar contra la asistencia real)
□ Presencia del Comisario registrada correctamente
□ Quórum confirmado correctamente (conforme a LGSM y estatutos sociales)
□ Lenguaje de las resoluciones coincide con lo que realmente se aprobó (verificar redacción cuidadosamente)
□ Votaciones registradas correctamente — ¿alguna abstención o voto disidente a registrar?
□ Anexos numerados y referenciados correctamente
□ ¿Se celebró alguna sesión ejecutiva? (Agregar nota separada de sesión ejecutiva si aplica)
□ ¿Se reveló algún conflicto de interés? (Registrar recusación del consejero si aplica)
□ Hora de cierre de la sesión por completar
□ ¿Requiere protocolización ante Notario Público? (Verificar si los acuerdos lo requieren conforme a la LGSM)
□ ¿Se debe inscribir en el Libro de Actas de la sociedad?
□ ¿Revisado por abogado externo? (Si lo requiere su proceso)
```

Señala cualquier sección donde el contenido sea un marcador de posición y necesite la revisión del abogado antes de que las actas sean precisas.

Agrega como nota final previa a la adopción en el borrador, que se elimina antes de la adopción:

> Este es un borrador para revisión del abogado, no son actas adoptadas. Las actas adoptadas son el registro oficial de la acción del Consejo y tienen consecuencias legales — un abogado titulado las revisa, edita y asume responsabilidad profesional antes de la adopción. No adopte este borrador sin revisión.

---

## Resoluciones fuera de asamblea

Para redactar resoluciones unánimes fuera de asamblea (en lugar de una sesión presencial), usa `/corporativo-legal-mexico:written-consent`. Esa habilidad maneja la búsqueda de precedentes, la confirmación de requisitos legales conforme a la LGSM, y la advertencia de alcance para acciones relevantes de única ocasión.

---

## Lo que esta habilidad no hace

- No asiste a la sesión ni captura discusión en tiempo real — redacta a partir de materiales e información proporcionada por el abogado.
- No determina si una resolución es legalmente válida o suficiente — redacta en formato interno; el juicio legal sobre la suficiencia corresponde al abogado.
- No finaliza las actas — el borrador requiere revisión del abogado antes de su circulación.
- No distribuye las actas — el resultado es para que el abogado revise, edite y circule mediante su propio proceso.
- No verifica si el acta requiere protocolización ante Notario Público — esa determinación corresponde al abogado conforme a la LGSM y los estatutos sociales.
