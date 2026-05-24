---
description: >
  Prepara el expediente de registro o modificación de un producto de seguro
  ante la CNSF. Genera la lista de documentos requeridos, revisa la nota
  técnica y las condiciones generales contra los requisitos regulatorios,
  identifica deficiencias antes de presentar el trámite, y produce el
  índice del expediente listo para entrega.
argument-hint: "[ramo de seguro y tipo de trámite: registro nuevo / modificación / renovación de condiciones]"
---

# Skill: producto-filing (seguros-legal-mexico)

## Propósito

El registro de condiciones generales y notas técnicas ante la CNSF es un requisito previo para comercializar cualquier producto de seguro en México. Un expediente incompleto o con deficiencias técnicas genera observaciones CNSF que retrasan el lanzamiento del producto y, en el peor caso, operación sin registro que puede derivar en sanciones. Este skill audita el expediente antes de presentarlo para reducir al mínimo las observaciones.

## Marco regulatorio

| Norma | Relevancia |
|---|---|
| LISF Arts. 200-230 | Registro de productos: condiciones generales, notas técnicas, tarifas `[model knowledge — verify artículos exactos]` |
| Disposiciones de Carácter General CNSF — Productos | Requisitos específicos por ramo `[verify versión vigente DOF]` |
| LCS | Las condiciones generales no pueden contravenir la LCS |
| Reglas CNSF del Sistema de Depósito de Información (SDI) | Plataforma de presentación de trámites `[verify requisitos técnicos actuales]` |
| Circulares CNSF por ramo | Requisitos adicionales por tipo de producto `[model knowledge — verify circulares vigentes]` |

## Tipos de trámite

| Trámite | Descripción |
|---|---|
| Registro de condiciones generales nuevas | Primer registro del producto |
| Modificación de condiciones generales | Cambios a un producto ya registrado |
| Renovación o revalidación | Si las condiciones tienen vigencia limitada `[verify si aplica al ramo]` |
| Registro de nota técnica | Componente actuarial del producto |
| Aviso de comercialización | Si el ramo solo requiere aviso, no aprobación previa `[verify por ramo]` |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo Operador:
- Tipo de institución
- Ramos autorizados (el producto debe estar dentro del ramo autorizado)
- Actuario responsable

Si el módulo Operador no está activo, advertir y continuar.

### Paso 1: identificar el producto y el trámite

Si el usuario no especificó, preguntar:

1. "¿Cuál es el ramo de seguro? (vida / daños / accidentes y enfermedades / salud / auto / transporte / RC / GMM / D&O / otro)"
2. "¿Qué tipo de trámite? (registro nuevo / modificación / aviso)"
3. "¿Tienes los borradores de condiciones generales y nota técnica? Proporciona los documentos."
4. "¿Cuáles son las características principales del producto? (suma asegurada, vigencia, primas, poblaciones objetivo)"
5. "¿Es un producto para personas físicas, morales, o ambas?"
6. "¿El producto incluye componentes de ahorro, inversión o excedentes? (relevante para vida)"

### Paso 2: verificar que el producto esté dentro del ramo autorizado

- [ ] La aseguradora tiene autorización CNSF para el ramo al que corresponde el producto
- [ ] El objeto del seguro es consistente con la descripción del ramo autorizado
- [ ] Si el producto combina coberturas de dos ramos (vida + accidentes), verificar que la aseguradora tenga ambas autorizaciones

`[review: verificar el texto exacto de la autorización CNSF de la institución]`

### Paso 3: revisión de condiciones generales

#### 3A. Requisitos formales mínimos (LCS + Disposiciones CNSF)

- [ ] Identificación de la aseguradora (nombre, número de autorización, datos de contacto)
- [ ] Definición clara del objeto del seguro / cobertura grant
- [ ] Suma asegurada o forma de determinarla
- [ ] Prima, forma y plazo de pago (incluyendo período de gracia)
- [ ] Vigencia de la póliza y condiciones de renovación
- [ ] Definición de términos técnicos usados en la póliza
- [ ] Sección de exclusiones: clara, taxativa y conforme a la LCS
- [ ] Obligaciones del asegurado: declaración de riesgo, aviso de siniestro (plazo mínimo LCS Art. 66: 5 días hábiles), documentación
- [ ] Proceso de reclamación: cómo presentar el siniestro, documentos requeridos, plazos de la aseguradora
- [ ] Datos de la UNE (Unidad Especializada de Atención a Usuarios) de CONDUSEF
- [ ] Instancias de atención: UNE interna → CONDUSEF → vía judicial
- [ ] Si aplica: cláusula de subrogación (seguros de daños, LCS Art. 111)
- [ ] Si aplica: tabla de beneficios y condiciones de pago (seguros de personas)

#### 3B. Consistencia con la LCS

- [ ] El plazo de aviso de siniestro no es menor al mínimo legal de 5 días hábiles (LCS Art. 66) `[review: si la póliza fija plazo menor, es una condición nula]`
- [ ] El plazo de prescripción no reduce el mínimo legal (2 años / 5 años para vida) `[review: si reduce, la cláusula puede ser nula]`
- [ ] Las exclusiones no eliminan la esencia de la cobertura `[review: posible condición abusiva]`
- [ ] Los efectos de la declaración inexacta del asegurado son consistentes con los Arts. 31-35 LCS
- [ ] No hay cláusulas que inviertan la carga de la prueba del siniestro de manera injustificada

#### 3C. Consistencia con las Disposiciones CNSF para el ramo

`[model knowledge — verify para el ramo específico; las disposiciones por ramo pueden tener requisitos adicionales]`

- [ ] Las condiciones generales siguen la estructura exigida por las Disposiciones para el ramo
- [ ] El lenguaje cumple con los estándares de claridad exigidos por CNSF y CONDUSEF
- [ ] Las cláusulas de renovación y cancelación son conformes a los requisitos del ramo

### Paso 4: revisión de la nota técnica (NT)

La nota técnica es el documento actuarial que justifica las tarifas y reservas del producto. Debe ser elaborada y firmada por el actuario responsable.

- [ ] Firmada y sellada por el actuario responsable con cédula profesional
- [ ] Metodología de cálculo de la prima: base estadística, supuestos de mortalidad/morbilidad/frecuencia/severidad
- [ ] Bases técnicas: tablas utilizadas (identificar si son tablas CNSF oficiales o tablas propias con justificación)
- [ ] Tarifa: prima neta + cargos (gastos de adquisición, administración, utilidad) = prima comercial
- [ ] Reservas técnicas que generará el producto: metodología de cálculo
- [ ] Periodo de suficiencia de la tarifa: ¿cada cuándo se revisa?
- [ ] Si el producto tiene componente de ahorro / inversión: proyecciones de rendimiento y supuestos `[review: supervisión actuarial más estricta]`

`[review: la revisión de la NT requiere el actuario — este skill identifica deficiencias formales; la validación actuarial es responsabilidad del actuario]`

### Paso 5: lista de documentos del expediente

Producir el índice del expediente a presentar ante CNSF:

**Documentos generales (todos los trámites):**
- [ ] Solicitud de registro en el formato CNSF correspondiente
- [ ] Condiciones generales (original firmado por el Director General)
- [ ] Nota técnica (firmada por actuario responsable)
- [ ] Tarifas (documento separado o incluido en NT, según el ramo)
- [ ] Modelo de carátula / póliza
- [ ] Modelo de solicitud de seguro (si aplica)
- [ ] Poder notarial del representante legal que firma la solicitud
- [ ] Copia del número de autorización CNSF vigente

**Documentos adicionales según ramo:**

*Vida / ahorro / inversión:*
- [ ] Tabla de valores garantizados (si aplica)
- [ ] Proyecciones ilustrativas de rendimiento con supuestos
- [ ] Formulario de declaración de estado de salud (si aplica)

*GMM / gastos médicos:*
- [ ] Catálogo de hospitales y médicos (si la aseguradora opera red cerrada)
- [ ] Procedimiento de preautorización de servicios médicos
- [ ] Condiciones de cobertura para preexistencias

*Daños / auto:*
- [ ] Si tiene servicio de asistencia: descripción del servicio y proveedor

*Transporte:*
- [ ] Si cubre transporte internacional: referencia al Convenio de transporte aplicable

**Si es modificación:**
- [ ] Cuadro comparativo entre las condiciones vigentes y las nuevas
- [ ] Justificación de los cambios

### Paso 6: producir reporte de auditoría previa

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [condiciones generales y NT proporcionadas ✓ | Disposiciones CNSF por ramo: model knowledge — verify versión vigente]
- Leído: [descripción de documentos revisados]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar los requisitos actuales en el Sistema de Depósito de Información (SDI) de CNSF; las disposiciones por ramo se actualizan periódicamente.

---

**Auditoría Pre-Filing — [nombre del producto] — [ramo] — [fecha]**

**Trámite:** [registro nuevo / modificación / aviso]
**Estado general del expediente:** [Listo para presentar / Requiere correcciones — N observaciones]

**Observaciones en condiciones generales:**
[Tabla de hallazgos del Paso 3]

**Observaciones en nota técnica:**
[Hallazgos del Paso 4]

**Documentos faltantes:**
[Lista de documentos del Paso 5 marcados como faltantes]

**Una pregunta que haría y que no está en mi checklist:** [observación]
```

> **¿Qué siges?**
> 1. **Corregir las observaciones** — identifico los cambios específicos que deben hacerse en condiciones generales y NT antes de presentar.
> 2. **Preparar solicitud formal** — elaboro el escrito de presentación para el trámite ante CNSF.
> 3. **Revisar condiciones generales en detalle** — `/seguros-legal-mexico:poliza-review` con las condiciones del producto para análisis más profundo de exclusiones y cláusulas.
> 4. **Responder observaciones CNSF** — si CNSF ya emitió observaciones al trámite, preparo la respuesta con las correcciones.
> 5. **Análisis de cumplimiento operativo** — `/seguros-legal-mexico:cnsf-compliance` para verificar que la institución puede operar el nuevo producto.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
