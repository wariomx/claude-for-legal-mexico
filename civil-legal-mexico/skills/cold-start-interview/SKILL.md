---
name: cold-start-interview
description: >
  Entrevista de configuración inicial del plugin de derecho civil mexicano.
  Construye el perfil de práctica: tipo de práctica civil, entidades
  federativas donde se ubican los inmuebles y asuntos, lado habitual
  (arrendador / arrendatario), posiciones de playbook de arrendamiento, rol
  del usuario e integraciones disponibles. Usar en instalación nueva, cuando
  un skill se detenga por `[PLACEHOLDER]`, para agregar una entidad federativa
  o un módulo, o para re-verificar conectores.
argument-hint: "[--local] [--redo] [--check-integrations] [--module <módulo>] [--from <paso>]"
---

# /cold-start-interview

## Propósito

El derecho civil es estatal. Sin configuración, los skills de este plugin no saben qué código civil citar, de qué lado negociar ni a quién escalar, y producen resultados genéricos que parecen correctos y no lo son. Esta entrevista tarda entre 8 y 12 minutos y habilita resultados calibrados para el resto del plugin. Es el único skill del plugin que funciona sin configuración previa.

## Flags

| Flag | Comportamiento |
|---|---|
| (ninguno) | Ejecutar solo los pasos no configurados |
| `--redo` | Re-ejecutar todos los pasos |
| `--from <N>` | Re-ejecutar desde el paso N |
| `--check-integrations` | Solo verificar integraciones, mostrar tabla, actualizar `## Integraciones disponibles` y detenerse |
| `--local` | Escribir todo a `.claude-legal/civil-legal-mexico/CLAUDE.md` en el directorio de trabajo actual (aislamiento por cliente) |
| `--module <slug>` | Agregar o re-configurar un módulo sin re-ejecutar la entrevista completa. Módulos disponibles en esta versión: `arrendamiento` |

## Flujo

### Paso 0: verificar estado actual

1. Determinar la ruta activa: con `--local`, `.claude-legal/civil-legal-mexico/CLAUDE.md`; sin él, `~/.claude/plugins/config/claude-for-legal/civil-legal-mexico/CLAUDE.md`.
2. Si existe una configuración sin `[PLACEHOLDER]` y no hay `--redo` ni `--module` ni `--from`, mostrar:
   > "Encontré una configuración existente. Entidad principal: [X]. Módulos activos: [lista]. Para re-ejecutar todo usa `--redo`; para ajustar un campo, `/civil-legal-mexico:customize`; para agregar un módulo, `--module <slug>`."
   y detenerse.
3. Si existe con `<!-- SETUP PAUSED AT: N -->`, ofrecer continuar desde el paso N.
4. Si `--check-integrations`: saltar al Paso 6.
5. Si es primera ejecución tras actualizar el plugin y hay un `CLAUDE.md` configurado en la ruta de caché antigua (`~/.claude/plugins/cache/claude-for-legal/civil-legal-mexico/<versión>/CLAUDE.md`) pero no en la ruta de configuración, copiarlo antes de continuar.

### Paso 1: perfil compartido de la empresa

Verificar si existe `company-profile.md` en la ruta activa (`.claude-legal/company-profile.md` o `~/.claude/plugins/config/claude-for-legal/company-profile.md`). Si existe:
> "Encontré el perfil de empresa: [nombre]. Usaré esos datos."

Si no existe, recopilar y escribirlo:
- Nombre de la entidad o del despacho
- Industria o sector (para despachos: "servicios jurídicos")
- Ciudad y estado de operación principal
- Tamaño del equipo legal (personas, o "solo")
- Ruta de escalamiento (socio responsable / despacho externo / Director Jurídico / notario de confianza)
- Tipo de práctica: despacho solo/pequeño | despacho mediano/grande | jurídico interno | gobierno/asistencia legal/clínica

### Paso 2: perfil civil

Preguntar:

> "¿Qué describe mejor tu práctica civil?"
> 1. **Despacho civilista** — contratos, arrendamientos, inmuebles, familia, sucesiones para clientes
> 2. **Notaría (apoyo jurídico)** — revisión previa a protocolización
> 3. **Jurídico interno con cartera inmobiliaria** — empresa que arrienda o toma en arrendamiento locales, bodegas, oficinas
> 4. **Administrador de inmuebles** — gestiona arrendamientos por cuenta de propietarios
> 5. **Persona física con asesoría** — revisa sus propios contratos con acceso a un abogado

La respuesta fija `**Perfil civil:**` en `## Perfil de la empresa` y orienta el lado habitual del Paso 4.

### Paso 3: entidades federativas

Esta es la sección que todos los skills leen antes de citar. Preguntar:

1. "¿En qué entidad federativa se ubican la mayoría de los inmuebles o asuntos que manejas?" → `**Entidad principal:**`
2. "¿Trabajas asuntos en otras entidades? ¿Cuáles?" → `**Entidades adicionales:**` (o "ninguna")
3. Para cada entidad, llenar la fila de la tabla (la fila de **Jalisco** es fija y se conserva siempre porque es la entidad verificada del plugin; si el usuario no trabaja en Jalisco se conserva igual y se agregan las suyas; la fila `[PLACEHOLDER]` se sustituye o se elimina):
   - **Código civil aplicable:** nombre oficial (p. ej., "Código Civil del Estado de Jalisco"; en Ciudad de México, "Código Civil para el Distrito Federal", hoy aplicable a la CDMX `[VERIFICAR nombre vigente]`).
   - **Referencia verificada en el plugin:** ✓ si existe `skills/<skill>/references/<código>-<entidad>-*.md` en el plugin instalado (en esta versión: solo Jalisco, arrendamiento); ✗ en caso contrario, con la nota "citas con `[VERIFICAR]`".
   - **Código procesal vigente / estatus CNPCF:** preguntar si el usuario lo sabe; si no, escribir `[VERIFICAR]`. No completar de memoria: la incorporación del Código Nacional de Procedimientos Civiles y Familiares avanza por declaratoria estatal y cambia de fecha.
   - **RPP:** nombre del registro público de la propiedad de la entidad.

Decir explícitamente: "Cuando un asunto no indique la entidad, los skills te la preguntarán; no asumen la principal."

### Paso 4: módulo Arrendamiento

En esta versión es el único módulo. Recopilar:

- **Lado habitual:** arrendador / arrendatario / ambos según el asunto / administrador de inmuebles (por cuenta del arrendador)
- **Destinos frecuentes:** habitación / comercio / industria / oficina / agropecuario (varios permitidos)
- **Volumen:** contratos por mes aproximados, u "ocasional"
- **Machote de casa:** ruta del contrato modelo del despacho, o "ninguno" (si hay ruta, leerlo y confirmar que se pudo abrir)
- **Posiciones de playbook** (cada una con una respuesta corta o "sin posición fija"):
  - Depósito en garantía: meses de renta y plazo de devolución que el despacho acepta
  - Incremento anual: INPC / porcentaje fijo / tope
  - Fiador u obligado solidario: siempre / solo comercial / según monto; ¿se exige extensión expresa a prórrogas y tácita reconducción?
  - Pena por terminación anticipada: meses de renta aceptables, por lado
  - Inscripción en RPP: siempre arriba del umbral legal / solo si el cliente lo pide
- **Umbral de escalamiento:** renta mensual o plazo a partir del cual el asunto se escala al socio o Director Jurídico

Preguntar si quiere activar el registro de arrendamientos (vencimientos, ventanas de preferencia, incrementos) en `arrendamientos/registro.yaml` dentro de la ruta de configuración. Si sí, crear el archivo vacío con encabezado.

### Paso 5: quién usa el plugin

- **Rol:** Abogado titulado / profesional jurídico | No abogado con acceso a asesor legal | No abogado sin acceso a asesor legal
- **Si no es abogado:** nombre o equipo del contacto legal de referencia

Explicar en una línea que esto decide el encabezado de confidencialidad y el modo de salida en lenguaje llano.

### Paso 6: verificar integraciones

Probar que cada conector **responde**, no solo que está configurado:

| Integración | Prueba |
|---|---|
| LegalDataHunter | Una búsqueda real: "Código Civil del Estado de [entidad principal] arrendamiento". Si devuelve resultados → ✓. Si el MCP no existe o falla → ✗ con la causa (sin API key / sin conexión / error del servidor). Para configurar la clave: `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico`. |
| CJJ (Poder Judicial de Jalisco) | Solo si Jalisco está entre las entidades. Delegar a `/conectores-legal-mexico:setup-cjj --check-integrations`. |
| Registro Público de la Propiedad | No hay MCP; registrar "portal estatal, consulta manual" y la URL del portal de la entidad principal si el usuario la conoce. |
| Almacenamiento (Google Drive / SharePoint / Box / iManage) | Listar un directorio raíz. |
| Slack | Listar canales. Si hay agentes o alertas futuras, preguntar el canal. |

Mostrar la tabla y escribirla en `## Integraciones disponibles`. Con `--check-integrations`, actualizar solo esa sección y detenerse.

### Paso 7: espacios de trabajo por asunto

Si el tipo de práctica (Paso 1) es despacho o notaría: preguntar "¿Quieres aislar el contexto por cliente o asunto? (recomendado con más de un cliente)". Si sí, `**Habilitado:** ✓` en `## Espacios de trabajo por asunto` y explicar `/civil-legal-mexico:matter-workspace new <slug>`. Si es jurídico interno, administrador o persona física: dejar `✗` sin preguntar.

### Paso 8: escribir configuración

Construir el `CLAUDE.md` del plugin a partir de la plantilla que se distribuye con el plugin, sustituyendo cada `[PLACEHOLDER]` por lo recopilado. Los módulos no activos se omiten por completo. Escribir en la ruta activa creando los directorios padre. Con `--local`, recordar al usuario que `.claude-legal/` debe estar en `.gitignore`.

Si la entrevista se interrumpe, escribir lo recopilado hasta ese punto con `<!-- SETUP PAUSED AT: N -->` al inicio para poder reanudar.

### Paso 9: confirmación

```
Configuración de civil-legal-mexico completada.

Perfil civil: [X]
Entidad principal: [X] — referencia verificada: [✓ arrendamiento / ✗]
Entidades adicionales: [lista]
Lado habitual: [X]
Módulos activos: Arrendamiento
Integraciones: [resumen]

Skills disponibles:
  /civil-legal-mexico:revision-arrendamiento — revisar un contrato de arrendamiento de inmueble
  /civil-legal-mexico:customize — ajustar un campo del perfil
  /civil-legal-mexico:matter-workspace — asuntos por cliente (si está habilitado)

Siguiente paso recomendado:
  /civil-legal-mexico:revision-arrendamiento — pega el contrato o da la ruta.
```

Si la entidad principal no tiene referencia verificada, agregar: "Tu entidad principal no tiene tabla de artículos verificada en esta versión. Los skills citarán con `[VERIFICAR]`; conecta LegalDataHunter para recuperar el código estatal en cada revisión."

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
