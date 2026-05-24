---
name: customize
description: >
  Personalización guiada de tu perfil de práctica de privacidad — cambia un
  elemento sin volver a ejecutar toda la entrevista de configuración inicial.
  Ajusta tipo de responsable, módulos activos (Avisos de Privacidad / ARCO /
  Transferencias Internacionales / EIPD / Vulneraciones / Procedimientos INAI),
  ventanilla ARCO, tipos de datos tratados, proveedores en nube, protocolo de
  vulneraciones, o rutas de carpetas de asuntos. Úsalo cuando el usuario diga
  "cambia mi [cosa]", "actualiza mi perfil", "edita mi configuración" o
  "personalizar".
argument-hint: "[nombre de sección, o describe lo que quieres cambiar]"
---

# /customize

## Cuándo se ejecuta

El usuario escribió `/privacidad-legal-mexico:customize`. Quiere cambiar algo en
su perfil de práctica — un módulo activo/inactivo, la ventanilla ARCO, los tipos
de datos tratados, un nuevo proveedor en nube — sin volver a ejecutar toda la
entrevista de configuración inicial y sin editar manualmente el archivo de
configuración.

## Qué hacer

1. **Leer la configuración.** Lee
   `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`
   (y `~/.claude/plugins/config/claude-for-legal/company-profile.md` un nivel
   arriba). Si la configuración del plugin no existe o todavía contiene valores
   `[PLACEHOLDER]`, di:

   > Aún no has ejecutado la configuración inicial. Ejecuta
   > `/privacidad-legal-mexico:cold-start-interview` primero — personalizar es
   > para ajustar un perfil que ya tienes.

2. **Mostrar el mapa de opciones personalizables.** Lista lo que contiene el
   perfil, agrupado, con un resumen de una línea del valor actual:

   - **Empresa / quién eres** — nombre, industria, jurisdicciones, tipo de práctica
     *(compartido entre los plugins — los cambios fluyen a través de `company-profile.md`)*
   - **Tipo de responsable** — sector privado (LFPDPPP) o sector público (LGPDPPSP).
     Cambiar esto modifica los módulos disponibles y la ley aplicable en cada skill.
   - **Módulos activos** — cuáles de Avisos de Privacidad, ARCO, Transferencias
     Internacionales, EIPD, Vulneraciones, Procedimientos INAI están activos.
     Activar o desactivar un módulo cambia qué secciones del perfil existen y qué
     preguntas hacen los skills.
   - **Perfil de datos** — tipos de datos personales tratados, si hay datos sensibles,
     si hay menores. Cambiar esto afecta los checklists de `/privacidad-legal-mexico:aviso-privacidad`
     y `/privacidad-legal-mexico:gap-analysis`.
   - **Módulo ARCO** — ventanilla de recepción (correo, portal, físico), responsable
     de atención, mecanismo de verificación de identidad, volumen histórico.
   - **Módulo Avisos de Privacidad** — tipos de aviso en uso, repositorio de avisos
     vigentes, fecha de última revisión.
   - **Módulo Transferencias Internacionales** — destinos habituales, mecanismo legal
     usado, estado de los DPAs con encargados.
   - **Módulo EIPD** — umbral para EIPD, última EIPD realizada.
   - **Módulo Vulneraciones** — responsable de activar protocolo, criterio de
     "vulneración significativa", última prueba de respuesta a incidentes.
   - **Módulo Procedimientos INAI** — procedimientos activos, despacho externo.
   - **Documentos semilla** — avisos vigentes, plantilla ARCO, DPA modelo, política
     interna, plantilla de notificación de vulneración.
   - **Integraciones** — LegalDataHunter, INAI portal, Google Drive / SharePoint / Box,
     Slack — estado y alternativas.

3. **Preguntar qué quieren cambiar.**

   > ¿Qué te gustaría ajustar? Elige una sección o describe el cambio con tus
   > propias palabras.

4. **Hacer el cambio.** Muestra el valor actual, solicita el nuevo valor,
   explica qué cambia en los procesos posteriores, confirma y escríbelo en la
   configuración.

   Ejemplos:
   - *Agregar módulo EIPD:* "Voy a agregar la sección EIPD a tu perfil. Te haré
     tres preguntas rápidas: ¿para qué tipo de proyectos realizas EIPDs, cuál es
     tu umbral formal, y cuándo fue la última? Puedes responderlas ahora o dejarlas
     como placeholders y llenarlas después."
   - *Cambiar ventanilla ARCO:* "`/privacidad-legal-mexico:arco-response` ahora
     usará [nuevo correo] como la ventanilla de recepción. El plazo de 20 días
     hábiles sigue corriendo desde la recepción por cualquier canal — asegúrate
     de que [nuevo correo] tenga configurado un acuse de recibo automático con
     fecha y hora."
   - *Agregar nuevo proveedor en nube:* "Voy a agregar [proveedor] a tu lista de
     encargados con transferencia internacional. ¿Tienen un DPA firmado? ¿Bajo qué
     mecanismo legal se realiza la transferencia (consentimiento / cláusulas
     contractuales / otro)?"

5. **Para cambios en el perfil compartido** (nombre de la empresa, industria,
   jurisdicciones, tipo de práctica): escribe en
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` y nota:

   > Este cambio afecta a todos los plugins — cualquier plugin que lea tu
   > perfil de empresa ahora verá [nuevo valor].

6. **Cerrar.**

   > Listo. Tu próxima salida reflejará el cambio. ¿Algo más? Puedes ejecutar
   > `/privacidad-legal-mexico:customize` en cualquier momento.

## Salvaguardas

- **Nunca eliminar una sección.** Si el usuario quiere "quitar" algo, establece
  el valor como `[No configurado]` y explica qué significa eso para el
  comportamiento del plugin.
- **Señalar inconsistencias internas.** Si el cambio haría que el perfil fuera
  inconsistente (ej., módulo de Transferencias Internacionales desactivado + un
  DPA firmado en Documentos semilla; o tipo de responsable "sector público" con
  módulo PPD de sector privado activo), señala la tensión.
- **Señalar implicaciones jurídicas del cambio.** Si el usuario quiere cambiar
  el tipo de responsable de privado a público, advertir: "Cambiar el tipo de
  responsable cambia la ley aplicable de la LFPDPPP a la LGPDPPSP. Los plazos,
  los derechos de los titulares y los procedimientos ante el INAI son diferentes
  en cada régimen. Si la organización realmente opera en ambos sectores, es mejor
  tener perfiles separados por entidad. ¿Confirmas el cambio?"
- **Señalar degradación de salvaguardas.** Las etiquetas `[review]` y
  `[model knowledge — verify]` son elementos estructurales — explica la
  compensación antes de eliminarlas.
- **Un cambio a la vez.** No volver a hacer toda la entrevista.
