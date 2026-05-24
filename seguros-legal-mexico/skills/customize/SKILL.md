---
description: >
  Ajusta secciones específicas del perfil de práctica de seguros sin
  re-ejecutar la entrevista completa. Útil para actualizar ramos activos,
  cambiar aseguradoras, agregar siniestros o modificar la postura de
  cobertura sin tocar el resto de la configuración.
argument-hint: "[campo o sección a ajustar]"
---

# Skill: customize (seguros-legal-mexico)

## Propósito

`cold-start-interview` configura todo de una vez. `customize` edita campos puntuales sin riesgo de borrar configuración existente. Para agregar un módulo completo nuevo, usar `cold-start-interview --module <slug>`.

## Flujo

### Paso 0: leer configuración activa

Leer el perfil de práctica en la ruta activa (local → global). Si no existe o tiene `[PLACEHOLDER]`, redirigir:

> "No encontré configuración para este plugin. Ejecuta `/seguros-legal-mexico:cold-start-interview` primero."

### Paso 1: identificar qué ajustar

Si el usuario no especificó qué cambiar, mostrar los campos disponibles agrupados por módulo:

**Módulo Operador**
- Número de autorización CNSF
- Ramos autorizados
- Nombre del Oficial de Cumplimiento
- Requerimientos activos CNSF

**Módulo Asegurado Corporativo**
- Tipos de seguro activos
- Aseguradoras principales
- Suma asegurada total
- Siniestros activos
- Renovaciones próximas
- Postura de cobertura

**Módulo Asegurado Individual**
- Tipos de seguro activos
- Aseguradora(s) y número(s) de póliza
- Siniestro activo
- Situación CONDUSEF

**Módulo Reaseguro**
- Tipos de contratos activos
- Reaseguradores principales
- Límite de retención

**Módulo Fianzas**
- Tipos de fianza
- Fianzas activas relevantes
- Reclamaciones activas

**Configuración general**
- Integraciones (re-verificar)
- Rol del usuario
- Contacto de escalamiento

### Paso 2: recopilar nuevo valor

Para cada campo que el usuario quiera cambiar, preguntar el nuevo valor. Si el campo es una lista (tipos de seguro, aseguradoras), preguntar si reemplaza o agrega.

### Paso 3: escribir cambio

Actualizar SOLO el campo indicado en el `CLAUDE.md` activo. No modificar ninguna otra sección.

Confirmar:

> "Actualizado: [campo] → [nuevo valor]. El resto de la configuración no cambió."

Para re-verificar integraciones: ejecutar Paso 5 de `cold-start-interview` y actualizar la tabla de integraciones.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
