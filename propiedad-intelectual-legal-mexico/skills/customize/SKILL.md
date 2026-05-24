---
name: customize
description: >
  Personalización guiada de tu perfil de práctica de propiedad intelectual —
  cambia un elemento sin volver a ejecutar toda la entrevista de configuración
  inicial. Ajusta postura de riesgo, contactos de escalamiento, alcance de
  portafolio, estrategia de protección de marca, postura de enforcement,
  umbrales de búsqueda de anterioridades, reglas de revisión OSS, o rutas de
  carpetas de asuntos. Úsalo cuando el usuario diga "cambia mi [cosa]",
  "actualiza mi perfil", "edita mi configuración" o "personalizar".
argument-hint: "[nombre de sección, o describe lo que quieres cambiar]"
---

# /customize

## Cuándo se ejecuta

El usuario escribió `/propiedad-intelectual-legal-mexico:customize`. Quiere
cambiar algo en su perfil de práctica de PI — una postura de riesgo, un contacto
de escalamiento, una posición de portafolio, una táctica de enforcement — sin
volver a ejecutar toda la entrevista de configuración inicial y sin editar
manualmente el archivo de configuración.

## Qué hacer

1. **Leer la configuración.** Lee
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`
   (y `~/.claude/plugins/config/claude-for-legal/company-profile.md` un nivel
   arriba). Si la configuración del plugin no existe o todavía contiene valores
   `[PLACEHOLDER]`, di:

   > Aún no has ejecutado la configuración inicial. Ejecuta
   > `/propiedad-intelectual-legal-mexico:cold-start-interview` primero —
   > personalizar es para ajustar un perfil que ya tienes.

2. **Mostrar el mapa de opciones personalizables.** Lista lo que contiene el
   perfil, agrupado, con un resumen de una línea del valor actual:

   - **Empresa / quién eres** — nombre, industria, jurisdicciones, etapa,
     entorno de práctica *(compartido entre los 12 plugins — los cambios fluyen
     a través de `company-profile.md`)*
   - **Perfil de práctica de PI** — qué tipos de PI están en alcance (marca,
     patente, derecho de autor, secreto industrial, diseño industrial, modelo
     de utilidad), orientación de práctica (trámite ante IMPI/INDAUTOR /
     transacciones / enforcement / portafolio in-house)
   - **Postura de riesgo** — conservadora / moderada / agresiva, qué significa
     cada una para umbrales de búsqueda de anterioridades, opiniones de FTO y
     escalamiento de cartas de requerimiento
   - **Personas** — abogado de PI, despachos externos por tipo de PI, cadena de
     escalamiento de enforcement, comité de invenciones
   - **Portafolio** — familias de patentes, clases de marca, marcas clave,
     países de registro, servicios de vigilancia, registros ante IMPI/INDAUTOR
   - **Protección de marca** — postura de enforcement en retiro de productos de
     marketplace, cibersquatters, parodia / uso justo
   - **Postura de enforcement** — cuándo enviar carta de requerimiento vs. carta
     de saneamiento vs. declaración administrativa ante IMPI; disparadores de
     escalamiento por tipo de infracción
   - **Búsqueda de anterioridades y FTO** — proveedores de búsqueda
     (LegalDataHunter, Solve Intelligence), umbrales de confianza, formato de
     dictamen de FTO
   - **Revisión OSS** — políticas por nivel de licencia, licencias bloqueantes,
     cadencia de revisión de nuevas dependencias
   - **Derechos de autor** — registro ante INDAUTOR, reservas de derechos,
     obra por encargo (LFDA Arts. 83-84), derechos morales (LFDA Art. 19)
   - **Flujo de trabajo** — carpetas de asuntos (IDs de asunto, IDs de familia),
     alimentación de expedientes, formato de admisión de invenciones
   - **Integraciones** — sistema de gestión de PI / conectores a IMPI/INDAUTOR /
     LegalDataHunter / Solve Intelligence / Slack / almacenamiento de
     documentos, estado y alternativas

3. **Preguntar qué quieren cambiar.**

   > ¿Qué te gustaría ajustar? Elige una sección o describe el cambio con tus
   > propias palabras.

4. **Hacer el cambio.** Muestra el valor actual, solicita el nuevo valor, explica
   qué cambia en los procesos posteriores, confirma y escríbelo en la
   configuración.

   Ejemplos:
   - *Agregar una nueva clase de marca en vigilancia:*
     "`/propiedad-intelectual-legal-mexico:portafolio` incluirá la clase XX en
     los reportes de vigilancia y
     `/propiedad-intelectual-legal-mexico:triaje-infraccion` enrutará hallazgos
     de clase XX en consecuencia."
   - *Postura de enforcement agresiva → moderada:*
     "`/propiedad-intelectual-legal-mexico:carta-requerimiento` ofrecerá
     borradores de carta de saneamiento como primera opción en casos ambiguos
     en vez de ir directo a carta de requerimiento formal."
   - *Nueva licencia bloqueante en OSS:*
     "`/propiedad-intelectual-legal-mexico:oss-review` rechazará revisiones que
     incluyan esta licencia en vez de solo advertir."
   - *Actualizar formato de dictamen de FTO:*
     "`/propiedad-intelectual-legal-mexico:fto-triage` usará el nuevo formato
     para dictámenes."

5. **Para cambios en el perfil compartido** (nombre de la empresa, industria,
   jurisdicciones, entorno de práctica, etapa): escribe en
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` y nota:

   > Este cambio afecta a los 12 plugins — cualquier plugin que lea tu
   > cobertura jurisdiccional ahora verá [nuevo valor].

6. **Cerrar.**

   > Listo. Tu próxima salida reflejará el cambio. ¿Algo más? Puedes ejecutar
   > `/propiedad-intelectual-legal-mexico:customize` en cualquier momento.

## Salvaguardas

- **Nunca eliminar una sección.** Si el usuario quiere "quitar" un tipo de PI
  del alcance, establece el valor como `[No se maneja actualmente]` y explica
  qué cambia en el comportamiento del plugin.
- **Señalar inconsistencias internas.** Si el cambio haría que el perfil fuera
  inconsistente (p. ej., marca fuera de alcance + servicio de vigilancia de
  marca configurado; o postura de enforcement agresiva + "todas las cartas de
  requerimiento van a despacho externo"), señala la tensión.
- **Señalar degradación de salvaguardas.** Las etiquetas `[review]`, las
  etiquetas de atribución de fuentes y las etiquetas `[verify]` en autoridades
  citadas son elementos estructurales — no eliminar. La confianza en umbrales
  de búsqueda de anterioridades es estructural en
  `/propiedad-intelectual-legal-mexico:clearance` — no suprimir.
- **Un cambio a la vez.** No volver a hacer toda la entrevista.
