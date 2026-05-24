---
name: customize
description: >
  Personalización guiada de tu perfil de práctica de gobernanza de IA — cambia
  un elemento sin volver a ejecutar toda la entrevista de configuración inicial.
  Ajusta postura de riesgo, nexo europeo, responsables internos, umbrales de
  triaje, herramientas de IA permitidas/prohibidas, proveedores en el inventario,
  o rutas de documentos semilla. Úsalo cuando el usuario diga "cambia mi
  [cosa]", "actualiza mi perfil", "edita mi configuración" o "personalizar".
argument-hint: "[nombre de sección, o describe lo que quieres cambiar]"
---

# /customize

## Cuándo se ejecuta

El usuario escribió `/ia-governanza-legal-mexico:customize`. Quiere cambiar algo en su perfil de práctica — una postura de riesgo, un responsable interno, una herramienta en el inventario, el nexo europeo — sin volver a ejecutar toda la entrevista de configuración inicial y sin editar manualmente el archivo de configuración.

## Qué hacer

1. **Leer la configuración.** Lee `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md` (y `~/.claude/plugins/config/claude-for-legal/company-profile.md` un nivel arriba). Si la configuración del plugin no existe o todavía contiene valores `[PLACEHOLDER]`, di:

   > Aún no has ejecutado la configuración inicial. Ejecuta `/ia-governanza-legal-mexico:cold-start-interview` primero — personalizar es para ajustar un perfil que ya tienes.

2. **Mostrar el mapa de opciones personalizables.** Lista lo que contiene el perfil, agrupado, con un resumen de una línea del valor actual:

   - **Empresa / quién eres** — nombre, industria, jurisdicciones, etapa, entorno de práctica *(compartido entre los plugins — los cambios fluyen a través de `company-profile.md`)*
   - **Nexo europeo** — si aplica el EU AI Act, naturaleza del nexo (clientes / empleados / contratos / filial / proveedor)
   - **Inventario de sistemas de IA** — sistemas activos, clasificaciones de riesgo, responsables internos
   - **Política de IA** — herramientas permitidas/prohibidas, proceso de aprobación de nuevos casos de uso, alcance de la política
   - **Contratos con proveedores** — tabla de proveedores, cláusulas de training-on-data, propiedad de outputs
   - **Evaluaciones de impacto** — umbral para EIPD-IA, EIPDs realizadas
   - **Documentos semilla** — rutas de política, contratos ejemplo, registros
   - **Espacios de trabajo por asunto** — habilitado/deshabilitado (solo para despachos con múltiples clientes)
   - **Integraciones** — LegalDataHunter, Drive/SharePoint/Box, Slack, estado y alternativas

3. **Preguntar qué quieren cambiar.**

   > ¿Qué te gustaría ajustar? Elige una sección o describe el cambio con tus propias palabras.

4. **Hacer el cambio.** Muestra el valor actual, solicita el nuevo valor, explica qué cambia en los procesos posteriores, confirma y escríbelo en la configuración.

   Ejemplos:
   - *Nexo europeo cambia de "No" a "Sí (clientes en España):*
     "`/ia-governanza-legal-mexico:eu-ai-act-exposure` ahora ejecutará el análisis completo de obligaciones del EU AI Act. `/ia-governanza-legal-mexico:use-case-triage` clasificará tus sistemas conforme a la pirámide de riesgo del EU AI Act."
   - *Agregar un nuevo sistema de IA al inventario:*
     "Lo agregaré al registro de casos de uso. ¿Quieres clasificarlo ahora con `/ia-governanza-legal-mexico:use-case-triage`?"
   - *Actualizar cláusula de training-on-data de un proveedor de "Sí" a "Opt-out":*
     "Actualizaré la tabla de proveedores. El skill de revisión de contratos usará este valor actualizado en futuras revisiones."

5. **Para cambios en el perfil compartido** (nombre de la empresa, industria, jurisdicciones, entorno de práctica): escribe en `~/.claude/plugins/config/claude-for-legal/company-profile.md` y nota:

   > Este cambio afecta a todos los plugins — cualquier plugin que lea tu cobertura jurisdiccional ahora verá [nuevo valor].

6. **Cerrar.**

   > Listo. Tu próxima salida reflejará el cambio. ¿Algo más? Puedes ejecutar `/ia-governanza-legal-mexico:customize` en cualquier momento.

## Salvaguardas

- **Nunca eliminar una sección.** Si el usuario quiere "quitar" algo, establece el valor como `[No configurado]` y explica qué significa eso para el comportamiento del plugin.
- **Señalar inconsistencias internas.** Si el cambio haría que el perfil fuera inconsistente (ej., nexo europeo = "No" + sistema clasificado como "alto riesgo EU AI Act" en el inventario; o herramienta permitida en la política + proveedor con training-on-data sin opt-out en la tabla de contratos), señala la tensión.
- **Señalar degradación de salvaguardas.** Las etiquetas `[review]`, las etiquetas de atribución de fuentes y las etiquetas `[verify]` en autoridades citadas son elementos estructurales — explica la compensación antes de eliminarlas.
- **Un cambio a la vez.** No volver a hacer toda la entrevista.
