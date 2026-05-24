---
name: customize
description: >
  Personalización guiada de tu perfil de práctica corporativa — cambia un
  elemento sin volver a ejecutar toda la entrevista de configuración inicial.
  Ajusta postura de riesgo, contactos de escalamiento, módulos activos (F&A /
  Consejo de Administración / Sociedad Bursátil / Administración de Entidades),
  umbrales de materialidad, formato de anexos de revelaciones, precedentes de
  consentimiento, o rutas de carpetas de asuntos. Úsalo cuando el usuario diga
  "cambia mi [cosa]", "actualiza mi perfil", "edita mi configuración" o
  "personalizar".
argument-hint: "[nombre de sección, o describe lo que quieres cambiar]"
---

# /customize

## Cuándo se ejecuta

El usuario escribió `/corporativo-legal-mexico:customize`. Quiere cambiar algo
en su perfil de práctica — una postura de riesgo, un contacto de escalamiento,
un módulo activo/inactivo, un formato de salida — sin volver a ejecutar toda la
entrevista de configuración inicial y sin editar manualmente el archivo de
configuración.

## Qué hacer

1. **Leer la configuración.** Lee
   `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`
   (y `~/.claude/plugins/config/claude-for-legal/company-profile.md` un nivel
   arriba). Si la configuración del plugin no existe o todavía contiene valores
   `[PLACEHOLDER]`, di:

   > Aún no has ejecutado la configuración inicial. Ejecuta
   > `/corporativo-legal-mexico:cold-start-interview` primero — personalizar es
   > para ajustar un perfil que ya tienes.

2. **Mostrar el mapa de opciones personalizables.** Lista lo que contiene el
   perfil, agrupado, con un resumen de una línea del valor actual:

   - **Empresa / quién eres** — nombre, industria, jurisdicciones, etapa,
     privada vs. emisora en BMV, entorno de práctica *(compartido entre los 12
     plugins — los cambios fluyen a través de `company-profile.md`)*
   - **Módulos activos** — cuáles de F&A, Consejo de Administración y Secretaría
     Corporativa, Sociedad Bursátil, Administración de Entidades están activos.
     Activar o desactivar un módulo cambia qué habilidades solicitan
     configuración.
   - **Postura de riesgo** — conservadora / moderada / agresiva, qué significa
     cada una para la materialidad en debida diligencia y el alcance de los
     anexos de revelaciones
   - **Personas** — equipo de operación, secretario del consejo, responsable de
     administración de entidades, cadena de escalamiento
   - **Módulo de F&A** — umbrales de materialidad (valor de contrato, número de
     empleados, ingresos), plataformas de data room de confianza, nivel de
     confianza en revisión masiva con IA (Luminance / Kira), cadencia de
     informes al equipo de operación
   - **Módulo de Consejo de Administración y Secretaría Corporativa** — formato
     de resoluciones unánimes fuera de asamblea, preferencias de firmantes,
     estructura de comités, requisitos de convocatoria, protocolización
   - **Módulo de Sociedad Bursátil** — calendario de reportes ante CNBV,
     controles de revelación, revisión de reporte anual / trimestral
   - **Módulo de Administración de Entidades** — tabla de entidades, notario
     público / fedatario, entidades de constitución, calendario de obligaciones
     ante el Registro Público de Comercio
   - **Flujo de trabajo** — carpetas de asuntos (deal rooms), ubicación de
     checklist de cierre, cadencia de monitoreo del data room
   - **Integraciones** — Box / Intralinks / Datasite / Notario público / Slack,
     estado y alternativas

3. **Preguntar qué quieren cambiar.**

   > ¿Qué te gustaría ajustar? Elige una sección o describe el cambio con tus
   > propias palabras.

4. **Hacer el cambio.** Muestra el valor actual, solicita el nuevo valor,
   explica qué cambia en los procesos posteriores, confirma y escríbelo en la
   configuración.

   Ejemplos:
   - *Umbral de materialidad $250K → $500K:*
     "`/corporativo-legal-mexico:diligence-issue-extraction` y
     `/corporativo-legal-mexico:material-contract-schedule` ahora usarán $500K
     como punto de corte. Los hallazgos existentes permanecen como se
     registraron; vuelve a ejecutar si quieres que se aplique el nuevo umbral
     retroactivamente."
   - *Activar el módulo de Sociedad Bursátil:* "Te pediré el calendario de
     reportes ante CNBV y los controles de revelación la próxima vez que
     ejecutes algo en esa área."
   - *Confianza en revisión masiva con IA de "revisar cada fila" a "verificar
     10% por muestreo":* "`/corporativo-legal-mexico:ai-tool-handoff` revisará
     una muestra del 10% en vez de cada extracción."

5. **Para cambios en el perfil compartido** (nombre de la empresa, industria,
   jurisdicciones, entorno de práctica, etapa): escribe en
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` y nota:

   > Este cambio afecta a los 12 plugins — cualquier plugin que lea tu
   > cobertura jurisdiccional ahora verá [nuevo valor].

6. **Cerrar.**

   > Listo. Tu próxima salida reflejará el cambio. ¿Algo más? Puedes ejecutar
   > `/corporativo-legal-mexico:customize` en cualquier momento.

## Salvaguardas

- **Nunca eliminar una sección.** Si el usuario quiere "quitar" algo, establece
  el valor como `[No configurado]` y explica qué significa eso para el
  comportamiento del plugin.
- **Señalar inconsistencias internas.** Si el cambio haría que el perfil fuera
  inconsistente (p. ej., módulo de Sociedad Bursátil desactivado + "abogado de
  valores ante CNBV" en escalamiento; o postura de riesgo agresiva + umbral de
  materialidad de $25K), señala la tensión.
- **Señalar degradación de salvaguardas.** Las etiquetas `[review]`, las
  etiquetas de atribución de fuentes en documentos recuperados y las etiquetas
  `[verify]` en autoridades citadas son elementos estructurales — explica la
  compensación antes de eliminarlas.
- **Un cambio a la vez.** No volver a hacer toda la entrevista.
