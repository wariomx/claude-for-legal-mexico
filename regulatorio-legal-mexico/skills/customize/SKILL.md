---
description: >
  Personaliza la configuración del plugin regulatorio-legal-mexico. Muestra un
  mapa de las opciones configurables — reguladores activos, palabras clave del
  DOF, umbrales de alerta, postura de cumplimiento, integraciones — y aplica un
  cambio a la vez con confirmación del usuario. Para cambios en el perfil
  compartido de la empresa (nombre, industria, postura de riesgo) escribe en
  company-profile.md para que el cambio se propague a todos los plugins.
argument-hint: "[sección a personalizar]"
---

# Skill: customize (regulatorio-legal-mexico)

## Propósito

Actualizar la configuración existente de regulatorio-legal-mexico sin re-ejecutar la entrevista completa. Este skill expone las palancas de configuración disponibles, pregunta cuál cambiar, y aplica el cambio con confirmación antes de escribir.

## Flujo

### Paso 1: verificar que existe configuración

Leer la configuración activa:
- LOCAL: `.claude-legal/regulatorio-legal-mexico/CLAUDE.md` (si existe)
- GLOBAL: `~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/CLAUDE.md`

Si no existe configuración o aún tiene `[PLACEHOLDER]`: "Primero ejecuta `/regulatorio-legal-mexico:cold-start-interview` — no hay configuración que personalizar todavía."

Leer también:
- `~/.claude/plugins/config/claude-for-legal/company-profile.md` (o local)

### Paso 2: mostrar mapa de opciones configurables

```
Configuración actual de regulatorio-legal-mexico
================================================

PERFIL DE LA EMPRESA (en company-profile.md — cambios se propagan a todos los plugins)
  [ ] Nombre de la entidad
  [ ] Industria / sector
  [ ] Tamaño del equipo legal
  [ ] Postura de riesgo regulatorio

MÓDULOS ACTIVOS
  [ ] Activar / desactivar módulo (DOF / COFECE / CNBV / COFEPRIS / IFT / CRE / CONAMER)

MÓDULO DOF
  [ ] Sectores monitoreados
  [ ] Cadencia de revisión (diaria / semanal / ad-hoc)
  [ ] Palabras clave de alerta
  [ ] Destinatarios del digest
  [ ] Umbral de relevancia

MÓDULO COFECE
  [ ] Sectores de exposición
  [ ] Umbral de notificación de concentraciones
  [ ] Contacto especialista COFECE

MÓDULO CNBV
  [ ] Tipo de entidad regulada
  [ ] Vicepresidencia de supervisión
  [ ] Calendario de reportes regulatorios

MÓDULO COFEPRIS
  [ ] Tipo de productos regulados
  [ ] Responsable Sanitario
  [ ] NOMs aplicables

MÓDULO IFT
  [ ] Tipo de concesión
  [ ] Servicios concesionados
  [ ] Obligaciones de cobertura

MÓDULO CRE
  [ ] Tipo de permiso CRE
  [ ] Vigencia del permiso
  [ ] Obligaciones de reporte

MÓDULO CONAMER
  [ ] Sectores de participación
  [ ] Postura de participación en consultas

INTEGRACIONES
  [ ] Estado de DOF connector
  [ ] Estado de Slack
  [ ] Estado de almacenamiento de documentos
  [ ] Estado de correo

¿Qué quieres cambiar? (escribe el número o nombre de la sección)
```

### Paso 3: hacer un cambio a la vez

Por cada cambio que el usuario pida:

1. Mostrar el valor actual.
2. Preguntar el nuevo valor.
3. Confirmar: "¿Confirmas cambiar [campo] de '[valor actual]' a '[nuevo valor]'? (sí / no)"
4. Aplicar el cambio en el archivo de configuración.
5. Preguntar: "¿Hay algo más que quieras cambiar?"

### Paso 4: cambios en perfil de empresa

Si el usuario cambia algo en la sección de perfil de la empresa:

1. Aplicar el cambio en `company-profile.md` (ruta activa).
2. Informar: "Actualicé company-profile.md — este cambio se propagará a todos los plugins que leen el perfil compartido (corporativo-legal-mexico, litigacion-legal-mexico, propiedad-intelectual-legal-mexico, etc.)."

### Paso 5: salvaguardas

- **Nunca eliminar secciones completas** — si el usuario quiere desactivar un módulo, preguntar si quiere eliminarlo o solo marcarlo como inactivo.
- **Señalar inconsistencias** — si el nuevo valor contradice otra configuración existente (ej: cambiar el tipo de entidad CNBV a "banco" cuando el módulo CONAMER indica solo participación como privado no regulado), señalarlo antes de aplicar.
- **Señalar degradación de salvaguardas** — si el cambio solicitado debilitaría una salvaguarda del CLAUDE.md (ej: eliminar el umbral de escalamiento), advertir antes de aplicar.

### Paso 6: confirmar resultado

Mostrar un resumen de los cambios aplicados:

```
Cambios aplicados:
  ✓ [campo] → [nuevo valor] (en [archivo])

Ningún skill requiere reinicio — los cambios aplican en la siguiente invocación.
```

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
