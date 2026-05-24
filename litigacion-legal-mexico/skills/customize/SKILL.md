---
name: customize
description: >
  Personalización guiada de tu perfil de práctica litigiosa — cambia un
  elemento sin repetir toda la entrevista de configuración inicial. Ajusta
  rol de práctica, lado (actor / demandado / mixto), calibración de riesgo,
  panorama, estilo de casa, contactos de escalamiento, vocabulario de
  severidad o rutas de espacios de trabajo por asunto. Úsalo cuando el
  usuario dice "cambia mi [cosa]", "actualiza mi perfil", "edita mi
  configuración" o "personalizar".
argument-hint: "[nombre de sección, o describe lo que quieres cambiar]"
---

# /customize

## Cuándo se ejecuta

El usuario escribió `/litigacion-legal-mexico:customize`. Quiere cambiar algo
en su perfil de litigación — una calibración de riesgo, una regla de estilo,
un contacto de escalamiento, una nota de panorama — sin repetir toda la
entrevista de configuración inicial y sin editar YAML a mano.

## Qué hacer

1. **Leer la configuración.** Leer
   `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md`
   (y `~/.claude/plugins/config/claude-for-legal/company-profile.md` un nivel
   arriba). Si la configuración del plugin no existe o todavía contiene
   valores `[PLACEHOLDER]`, decir:

   > Aún no has corrido la configuración inicial. Ejecuta `/litigacion-legal-mexico:cold-start-interview`
   > primero — customize es para ajustar un perfil que ya tienes.

2. **Mostrar el mapa personalizable.** Listar lo que hay en el perfil, agrupado,
   con un resumen de una línea del valor actual:

   - **Empresa / quién eres** — nombre, industria, jurisdicciones, etapa, contexto
     de práctica *(compartido entre los 12 plugins — los cambios fluyen a través
     de `company-profile.md`)*
   - **Rol de práctica** — jurídico interno / asociado de despacho / independiente / clínica u otro
   - **Lado** — actor / demandado / mixto, y cualquier matiz de postura (defensa
     en acciones colectivas, defensa ante reguladores, actor mercantil, etc.)
   - **Calibración de riesgo** — qué cuenta como alto / medio / bajo riesgo en una
     demanda, requerimiento o asunto nuevo; umbrales de escalamiento
   - **Panorama** — adversarios recurrentes, foros favorables y desfavorables,
     jueces a conocer, relaciones permanentes con despachos externos
   - **Estilo de casa** — estilo de escritos, formato de declaraciones, plantilla
     de carta de demanda, estructura de preparación de pruebas, plantilla de
     retención documental
   - **Mapa de vocabulario de severidad** — cómo traduces las etiquetas de severidad
     entre resultados internos, para el cliente y ante tribunales
   - **Personas** — responsables de asuntos, equipo jurídico interno, despacho
     externo por tipo de asunto, cadena de escalamiento
   - **Flujo de trabajo** — espacios de trabajo por asunto, bitácora del portafolio,
     cadencia de estatus con despacho externo, cadencia de renovación de
     retención documental
   - **Integraciones** — almacenamiento de documentos / presentación electrónica /
     calendario / estado de Slack, respaldos

3. **Preguntar qué quiere cambiar.**

   > ¿Qué deseas ajustar? Elige una sección, o describe el cambio en tus
   > propias palabras.

4. **Hacer el cambio.** Mostrar el valor actual, pedir el nuevo valor, explicar
   qué cambia aguas abajo, confirmar, escribir en la configuración.

   Ejemplos:
   - *Lado mixto → solo demandado:* "`/litigacion-legal-mexico:matter-intake` dejará de hacer
     las preguntas del lado actor. `/litigacion-legal-mexico:demand-draft` seguirá funcionando
     para demandas pre-judiciales del lado demandado pero el marco inicial será diferente."
   - *Calibración de riesgo — endurecer el umbral de alto riesgo:* "Más demandas
     y requerimientos entrantes pasarán por `/litigacion-legal-mexico:matter-briefing` y
     `/litigacion-legal-mexico:oc-status`."
   - *Nuevo despacho externo permanente para asuntos de PI:* "`/litigacion-legal-mexico:oc-status`
     incluirá a este despacho en los barridos semanales para asuntos etiquetados como PI."

5. **Para cambios en el perfil compartido** (nombre de empresa, industria,
   jurisdicciones, contexto de práctica, etapa): escribir en
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` y notar:

   > Este cambio afecta los 12 plugins — cualquier plugin que lea tu
   > perímetro jurisdiccional ahora ve [nuevo valor].

6. **Cerrar.**

   > Listo. Tu próximo resultado reflejará el cambio. ¿Algo más? Puedes
   > ejecutar `/litigacion-legal-mexico:customize` en cualquier momento.

## Salvaguardas

- **Nunca borrar una sección.** Si el usuario quiere "eliminar" un tipo de
  asunto del alcance, ofrecer marcarlo como `[No se maneja actualmente]` y
  explicar qué cambia en la ruta de admisión.
- **Señalar inconsistencias internas.** Si el cambio haría el perfil
  inconsistente (p. ej., lado solo-actor + cartera de despacho externo solo-demandado;
  o portafolio de "alto volumen" + sin espacios de trabajo por asunto configurados),
  señalar la tensión.
- **Señalar degradación de salvaguardas.** La compuerta de conciliación/mediación
  y secreto profesional en `/litigacion-legal-mexico:demand-draft`, el encabezado de
  privilegio en los resultados de asuntos, las etiquetas de atribución de fuentes
  y las etiquetas `[verificar]` en autoridades citadas son elementos de carga —
  no eliminar. La etiqueta `[revisar]` y el marco de "no presentar sin revisión
  de abogado" son elementos de carga.
- **Un cambio a la vez.** No repetir toda la entrevista.
