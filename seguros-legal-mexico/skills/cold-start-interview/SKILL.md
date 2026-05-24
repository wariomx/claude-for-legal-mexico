---
description: >
  Entrevista de configuración inicial para el plugin de seguros y fianzas.
  Construye el perfil de práctica calibrado al tipo de entidad (operador,
  asegurado corporativo, asegurado individual, reaseguro, fianzas), activa
  los módulos seleccionados y verifica las integraciones disponibles. Todos
  los skills del plugin dependen de esta configuración.
argument-hint: "[--local] [--redo] [--check-integrations] [--module <módulo>] [--from <paso>]"
---

# Skill: cold-start-interview (seguros-legal-mexico)

## Propósito

Sin configuración, todos los skills de este plugin producen resultados genéricos que no corresponden al tipo de entidad, los ramos de seguro, las aseguradoras, ni la postura de riesgo real del usuario. Esta entrevista tarda entre 10 y 15 minutos y habilita resultados calibrados para el resto del plugin.

## Flags

| Flag | Comportamiento |
|---|---|
| (ninguno) | Ejecutar solo los pasos no configurados |
| `--redo` | Re-ejecutar todos los pasos |
| `--from <N>` | Re-ejecutar desde el paso N o desde el módulo especificado |
| `--check-integrations` | Solo verificar integraciones disponibles, mostrar tabla y detenerse |
| `--local` | Escribir todo a `.claude-legal/seguros-legal-mexico/CLAUDE.md` en el directorio de trabajo actual |
| `--module <slug>` | Agregar o re-configurar un módulo específico sin re-ejecutar la entrevista completa (usar `/seguros-legal-mexico:customize` para edición puntual) |

## Flujo

### Paso 0: verificar estado actual

1. Buscar config activa (local → global). Si existe y no tiene `--redo`, cargarla y mostrar:
   > "Encontré una configuración existente. Módulos activos: [lista]. Para re-ejecutar todo, usa `--redo`. Para agregar un módulo, usa `--module <slug>`."
   Detenerse.
2. Si no existe, continuar.
3. Si `--check-integrations`: saltar a Paso 5, mostrar tabla y detenerse.

### Paso 1: perfil compartido de empresa

Verificar si existe `company-profile.md` en la ruta activa. Si existe, leerlo y mostrar:
> "Encontré el perfil de empresa: [nombre]. Usaré esos datos en la configuración."

Si no existe, recopilar:
- Nombre legal de la entidad
- Industria / sector principal
- Ciudad y estado de operación principal
- Tamaño del equipo legal (número de personas o "solo")
- Ruta de escalamiento (despacho externo / Director Jurídico / nombre)
- Tipo de práctica (despacho solo/pequeño | despacho mediano/grande | in-house | clínica/gobierno)

Escribir `company-profile.md` en la ruta activa.

### Paso 2: tipo de entidad y módulos

Preguntar:

> "¿Qué tipo de entidad o rol describe mejor tu práctica de seguros? (Puedes seleccionar más de uno)"
>
> 1. **Operador** — Aseguradora o afianzadora autorizada por la CNSF (o en proceso de autorización)
> 2. **Asegurado Corporativo** — Empresa que contrata pólizas de seguro para sus operaciones
> 3. **Asegurado Individual** — Persona física con seguros personales
> 4. **Reaseguro** — Cedente o reasegurador en contratos de reaseguro
> 5. **Fianzas** — Afianzadora, tomador o beneficiario de fianzas

Activar los módulos seleccionados. Si el usuario selecciona más de uno, configurar cada uno en orden (Paso 3A-E).

### Paso 3A: módulo Operador (si se seleccionó)

Recopilar:
- Número de autorización CNSF
- Tipo de institución (aseguradora / afianzadora / aseguradora-y-afianzadora / sociedad mutualista)
- Ramos autorizados (vida / daños / accidentes y enfermedades / fianzas; sub-ramos activos)
- Vicepresidencia de supervisión CNSF asignada
- Nombre del Oficial de Cumplimiento
- Nombre del actuario responsable y cédula profesional
- Nombre y firma del auditor externo
- ¿Hay requerimientos CNSF activos? (sí / no; si sí, descripción breve)
- Fecha del último reporte regulatorio enviado a CNSF

### Paso 3B: módulo Asegurado Corporativo (si se seleccionó)

Recopilar:
- Tipos de seguro activos (lista: RC / daños / transporte / D&O / ciberseguridad / vida grupo / GMM / otro)
- Aseguradoras principales (nombres)
- ¿Hay corredor o agente? (nombre)
- Suma asegurada total aproximada (orden de magnitud)
- ¿Hay siniestros activos? (número; si sí, descripción breve del más relevante)
- ¿Hay renovaciones en los próximos 90 días?
- Postura de cobertura (conservadora / moderada / autoseguro parcial)

### Paso 3C: módulo Asegurado Individual (si se seleccionó)

Recopilar:
- Tipos de seguro activos (vida / GMM / auto / hogar / RC personal / otro)
- Aseguradora(s) y número(s) de póliza (puede ser "por agregar")
- ¿Hay un siniestro activo? Descripción breve si aplica
- Situación CONDUSEF actual (sin queja / queja en proceso / arbitraje / litigio)

### Paso 3D: módulo Reaseguro (si se seleccionó)

Recopilar:
- Rol (cedente / reasegurador / intermediario)
- Tipos de contratos activos (proporcional: cuota parte / excedente; no proporcional: XL / stop loss)
- Reaseguradores principales (nombres y jurisdicciones)
- ¿Tiene registro CNSF como reasegurador extranjero? (número o "no aplica")
- Límite de retención neta por riesgo (monto o "por configurar")

### Paso 3E: módulo Fianzas (si se seleccionó)

Recopilar:
- Rol (afianzadora / tomador / beneficiario)
- Tipos de fianza (fidelidad / judicial / administrativa / de crédito / garantía)
- ¿Tiene autorización CNSF para operar fianzas? (número o "no aplica")
- Fianzas activas de mayor exposición (descripción breve)
- ¿Hay reclamaciones activas? (número)

### Paso 4: quién usa el plugin

Preguntar:
- **Rol del usuario:** Abogado titulado / profesional jurídico | No abogado con acceso a asesor legal | No abogado sin acceso a asesor legal
- **Si no es abogado:** nombre del contacto legal de referencia

### Paso 5: verificar integraciones

Verificar disponibilidad de:
- **DOF** (Diario Oficial de la Federación) — conector MCP o búsqueda web
- **CNSF** (portal cnsf.gob.mx) — acceso directo o manual
- **SCJN IUS / Semanario Judicial** — conector MCP
- **Almacenamiento** (Google Drive / SharePoint / Box / local)
- **Slack** (para alertas)
- **Email** (para notificaciones)

Mostrar tabla:

| Integración | Estado | Nota |
|---|---|---|
| DOF | ✓ / ✗ | [cómo está disponible] |
| CNSF | ✓ / ✗ | [manual o automático] |
| SCJN IUS / Semanario | ✓ / ✗ | [cómo está disponible] |
| Almacenamiento | ✓ / ✗ | [ruta o sistema] |
| Slack | ✓ / ✗ | [canal] |
| Email | ✓ / ✗ | [dirección] |

### Paso 6: escribir configuración

Construir el `CLAUDE.md` de seguros-legal-mexico con los módulos activos. Los módulos no seleccionados se omiten completamente.

Escribir en la ruta activa:
- `--local`: `.claude-legal/seguros-legal-mexico/CLAUDE.md`
- default: `~/.claude/plugins/config/claude-for-legal/seguros-legal-mexico/CLAUDE.md`

Crear directorios padre según sea necesario.

### Paso 7: confirmación

Mostrar resumen de lo configurado:

```
Configuración de seguros-legal-mexico completada.

Módulos activos: [lista]
Skills disponibles:
  /seguros-legal-mexico:poliza-review
  /seguros-legal-mexico:siniestro-intake
  /seguros-legal-mexico:cobertura-analysis
  [skills según módulos activos]

Integraciones: [resumen]

Siguiente paso recomendado:
  [skill más relevante según el módulo activo]
```

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
