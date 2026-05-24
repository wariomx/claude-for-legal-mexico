---
description: >
  Verifica el cumplimiento de un CFDI 4.0 — detecta errores en campos
  obligatorios, valida el complemento de nómina o el complemento de pagos según
  aplique, identifica inconsistencias entre RFC emisor/receptor y el SAT, y
  genera un reporte de errores con acción correctiva.
---

# Skill: cfdi-review (fiscal-legal-mexico)

## Propósito

Un CFDI con errores en campos obligatorios puede ser rechazado como deducción por el SAT incluso si la operación es legítima. Este skill hace la verificación preliminar antes de que el CFDI llegue al auditor: detecta errores de forma, valida los complementos más frecuentes y genera un reporte de hallazgos con la corrección específica para cada uno.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae del módulo SAT-Cumplimiento:
- PAC habitual
- Versión CFDI en uso (debe ser 4.0)
- Tipos de comprobantes frecuentes

Si el módulo no está activo: continúa con parámetros genéricos pero advierte que los resultados serán menos calibrados.

### Paso 1: recibir el CFDI

Acepta el CFDI en cualquiera de estos formatos:
- XML pegado directamente en el chat
- Ruta de archivo (lee el contenido)
- Descripción de campos clave (modo manual si no hay XML disponible)

Si se proporcionan múltiples CFDIs: advierte el total y procesa uno a uno, numerándolos.

### Paso 2: verificar campos obligatorios CFDI 4.0

Revisa los campos requeridos conforme al Art. 29-A CFF + Anexo 20 SAT CFDI 4.0 [settled — last confirmed 2026-05-24]:

| Campo | Regla | Acción si falla |
|---|---|---|
| Version | Debe ser "4.0" | Cancelar y re-emitir |
| Serie / Folio | Secuencial, único por emisor | Verificar numeración |
| Fecha | Dentro del plazo de timbrado | Cancelar si expiró |
| RFC Emisor | 12-13 dígitos, registrado en SAT | Verificar en portal SAT |
| Nombre / RazonSocial Emisor | Coincide exactamente con SAT `[review]` | Cancelar y re-emitir |
| RegimenFiscal Emisor | Valor del catálogo SAT | Corregir clave |
| RFC Receptor | 12-13 dígitos, registrado en SAT | Verificar en portal SAT |
| Nombre / RazonSocial Receptor | Coincide exactamente con SAT [settled — last confirmed 2026-05-24] | Cancelar y re-emitir |
| DomicilioFiscalReceptor | CP del domicilio fiscal del receptor en SAT [settled — last confirmed 2026-05-24] | Corregir o cancelar |
| RegimenFiscalReceptor | Valor del catálogo SAT correspondiente al receptor | Verificar con receptor |
| UsoCFDI | Permitido para el régimen del receptor [settled — last confirmed 2026-05-24] | Corregir clave |
| Sello digital / CSD | Vigente a la fecha del CFDI | Renovar CSD si expiró |
| SubTotal / Total | Cuadra con conceptos | Revisar cálculo |
| MetodoPago / FormaPago | Consistentes entre sí y con la operación | Corregir |

### Paso 3: verificar por tipo de complemento

**Si es Complemento de Pagos (REP):**
- Verifica que el CFDI de ingreso relacionado exista y coincida en monto e importes parciales.
- Verifica tipo de cambio si el pago es en moneda extranjera `[review]`.
- Verifica que la forma de pago corresponda al método real de pago.

**Si es Complemento Nómina:**
- Verifica tipo de percepción/deducción contra catálogo SAT.
- Verifica número de seguridad social IMSS del trabajador.
- Verifica CURP del trabajador.
- Verifica que el período de pago corresponda al período declarado en nómina.

**Si es Carta Porte:**
- Verifica versión vigente del Complemento Carta Porte `[model knowledge — verify versión y requisitos actuales]`.
- Verifica operador, vehículo y ubicaciones de origen/destino.

### Paso 4: reporte de hallazgos

```
REPORTE DE REVISIÓN CFDI 4.0
CFDI: [Serie-Folio] | Emisor: [RFC] | Fecha: [fecha]
────────────────────────────────────────────────────

HALLAZGOS

| # | Campo | Valor actual | Valor requerido | Severidad | Acción correctiva |
|---|---|---|---|---|---|
| 1 | [campo] | [valor] | [requerido] | 🔴 / 🟠 / 🟡 | [acción] |

RESUMEN
  Total de hallazgos: [N]  🔴 Bloqueantes: [N]  🟠 Altos: [N]  🟡 Medios: [N]
  Recomendación: [Cancelar y re-emitir / Corregir antes de deducir / Sin hallazgos]
```

**Caducidad:** corregir un error en el CFDI no extiende el plazo de deducción del gasto subyacente. La deducibilidad se rige por el ejercicio fiscal en que ocurrió la operación — `[review: caducidad]` aplica al año fiscal correspondiente.

### Paso 5: árbol de decisión

> **¿Qué sigue?**
> 1. **Cancelar y re-emitir** — te ayudo a redactar la instrucción al PAC con los campos corregidos.
> 2. **Verificar en portal SAT** — accede a verificacfdi.facturaelectronica.sat.gob.mx para validación oficial.
> 3. **Revisar más CFDIs** — pega el siguiente XML para continuar.
> 4. **Generar reporte de lote** — si tienes más de 10 CFDIs, organizo el reporte como dashboard `[review]`.

---

**⚠️ Nota del revisor:** Esta revisión es preliminar. La validación oficial y definitiva debe hacerse a través del portal de verificación del SAT (verificacfdi.facturaelectronica.sat.gob.mx). El Anexo 20 y los catálogos SAT se actualizan periódicamente — verificar la versión vigente de los catálogos antes de corregir `[model knowledge — verify]`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
