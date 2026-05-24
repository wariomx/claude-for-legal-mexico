---
description: >
  Análisis de brecha regulatoria para aseguradoras y afianzadoras supervisadas
  por la CNSF. Evalúa gobierno corporativo, capitalización, Requerimiento de
  Capital de Solvencia (RCS), prevención de lavado de dinero, protección al
  asegurado y cumplimiento de reportes regulatorios bajo la LISF y las
  Disposiciones de Carácter General CNSF. Produce un reporte con hallazgos
  clasificados por severidad, fundamento legal y plazo de remediación.
argument-hint: "[tipo de institución o área de cumplimiento a analizar]"
---

# Skill: cnsf-compliance (seguros-legal-mexico)

## Propósito

La CNSF supervisa aseguradoras y afianzadoras con facultades de inspección ordinaria, especial y permanente (LISF Art. 299 y ss.). Los hallazgos de una visita de inspección derivan en recomendaciones con plazos de atención que, si se incumplen, escalan a medidas cautelares, sanciones administrativas (LISF Art. 459-479) y hasta revocación de la autorización. Este skill mapea el estado de cumplimiento antes de que la CNSF lo haga.

**Nota:** Este skill cubre solo la capa de supervisión CNSF. Las aseguradoras que forman parte de conglomerados financieros supervisados también por CNBV deben complementar con `/regulatorio-legal-mexico:cnbv-compliance`.

## Marco regulatorio

| Norma | Relevancia |
|---|---|
| LISF (Ley de Instituciones de Seguros y de Fianzas) | Marco completo de operación y supervisión |
| Disposiciones de Carácter General CNSF | Regulación secundaria por materia `[verify versión vigente en DOF]` |
| LCS (Ley sobre el Contrato de Seguro) | Régimen del contrato — relación con asegurado |
| LFPIORPI | PLD/FT — obligaciones de entidades del sector financiero |
| LPDUSF | Protección al usuario — CONDUSEF interface |
| Circular S-18.3 y circulares CNSF vigentes | Requisitos actuariales y de capital `[model knowledge — verify vigencia]` |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo Operador:
- Tipo de institución
- Ramos autorizados
- Número de autorización CNSF
- Historial de visitas de inspección

Si el módulo Operador no está activo: "El módulo Operador no está configurado. Ejecutando con parámetros genéricos — para resultados calibrados ejecuta `/seguros-legal-mexico:cold-start-interview --module operador`."

### Paso 1: identificar el alcance del análisis

Si el usuario no especificó las áreas, preguntar:

1. "¿Qué tipo de institución? (aseguradora / afianzadora / aseguradora-y-afianzadora / sociedad mutualista)"
2. "¿La institución tiene autorización CNSF vigente, está en proceso de obtenerla, o quieres evaluar si una actividad requiere autorización?"
3. "¿Qué áreas quieres cubrir? (gobierno corporativo / capital y RCS / PLD/FT / protección al asegurado / reportes regulatorios / todo)"

### Paso 2: área A — gobierno corporativo

**Aseguradoras y afianzadoras (LISF):**

- [ ] Consejo de Administración integrado conforme a LISF Arts. 87-95 (consejeros independientes, funciones, responsabilidades) `[model knowledge — verify artículos exactos LISF]`
- [ ] Comité de Auditoría con consejeros independientes
- [ ] Comité de Inversiones y Financiamiento (si aplica según tamaño)
- [ ] Director General designado según procedimiento LISF
- [ ] Actuario responsable de la institución designado y registrado ante CNSF
- [ ] Auditor externo de estados financieros aprobado por CNSF
- [ ] Manuales de gobierno corporativo aprobados e implementados
- [ ] Política de conflictos de interés operativa

Clasificar cada elemento: ✓ Cumple / ⚠️ Brecha parcial / ✗ No cumple / N/A con severidad 🔴🟠🟡🟢.

### Paso 3: área B — capital y Requerimiento de Capital de Solvencia (RCS)

El RCS es el equivalente mexicano de Solvencia II (EU). Se calcula conforme a las Disposiciones de Carácter General CNSF.

- [ ] Capital mínimo pagado cubierto conforme a LISF `[verify monto mínimo vigente para el tipo de institución y ramos — model knowledge]`
- [ ] RCS calculado y cubierto al 100% `[verify si aplica coeficiente adicional por tamaño]`
- [ ] Fondos propios admisibles suficientes para cubrir el RCS
- [ ] Margen de Solvencia reportado a CNSF dentro de plazo `[verify plazo de reporte trimestral]`
- [ ] Reservas técnicas constituidas (reserva de riesgos en curso, reserva para siniestros pendientes, reserva de previsión) conforme a LISF y circulares CNSF `[verify disposiciones vigentes]`
- [ ] Inversiones que respaldan reservas técnicas dentro de los límites LISF (catálogo de activos admisibles) `[model knowledge — verify catálogo vigente]`
- [ ] Plan de negocio y proyecciones actuariales presentadas a CNSF si se solicitaron

Nota: el análisis de capital y RCS requiere los estados financieros y el reporte actuarial de la institución. Si no se proporcionaron, señalar que esta área quedó pendiente. `[review: solicitar estados financieros y reporte RCS]`

### Paso 4: área C — prevención de lavado de dinero y financiamiento al terrorismo (PLD/FT)

Marco: LFPIORPI + Disposiciones de Carácter General de la CNSF en materia de PLD/FT `[verify versión vigente]`.

- [ ] Oficial de Cumplimiento designado y registrado ante la UIF
- [ ] Manual de PLD/FT aprobado por el Consejo o equivalente
- [ ] Políticas KYC: Due Diligence Simplificada, Estándar y Reforzada por tipo de asegurado/tomador
- [ ] Monitoreo de operaciones con umbrales configurados
- [ ] Reportes de operaciones inusuales (ROI) y reportes en efectivo enviados a UIF dentro de plazo
- [ ] Capacitación anual del personal en PLD
- [ ] Evaluación de riesgos de PLD/FT documentada

Las brechas en PLD son sistémicamente más graves porque pueden generar responsabilidad penal para el Oficial de Cumplimiento. Clasificar brechas en PLD mínimo 🟠 Alto salvo evidencia contraria. `[review]`

### Paso 5: área D — protección al asegurado (CONDUSEF)

- [ ] UNE (Unidad Especializada de Atención a Usuarios) designada y registrada ante CONDUSEF
- [ ] Contrato de adhesión (pólizas) registrado ante CONDUSEF si aplica al tipo de seguro `[verify qué ramos requieren registro obligatorio]`
- [ ] Tiempo de respuesta a reclamaciones de asegurados dentro del plazo LPDUSF `[verify plazo vigente]`
- [ ] Comunicaciones al asegurado en lenguaje simple
- [ ] Proceso de reclamación documentado y accesible al asegurado
- [ ] Estadísticas de quejas reportadas a CONDUSEF en los plazos establecidos

### Paso 6: área E — reportes regulatorios CNSF

- [ ] Reporte de solvencia enviado en plazo `[verify frecuencia y plazo de reporte]`
- [ ] Estados financieros dictaminados presentados a CNSF dentro del plazo anual
- [ ] Nota técnica de cada producto registrado actualizada
- [ ] Reporte de inversiones presentado en plazo
- [ ] Reporte de reaseguro cedido en plazo
- [ ] Reporte de reclamaciones y siniestros en plazo
- [ ] Aviso de cualquier cambio en gobierno corporativo o accionariado relevante notificado a CNSF

### Paso 7: consolidar hallazgos

Producir tabla:

```
| # | Área | Requisito | Estado | Severidad | Plazo estimado de remediación | Fundamento legal |
|---|---|---|---|---|---|---|
| 1 | Capital/RCS | RCS cubierto al 100% | ✗ No cumple | 🔴 | Inmediato | LISF Art. [x] |
...
```

Ordenar por severidad descendente.

### Paso 8: producir reporte

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [model knowledge — verify | CNSF portal para disposiciones vigentes]
- Leído: [descripción de insumos]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar montos de capital mínimo y umbrales RCS contra Disposiciones de Carácter General CNSF vigentes; las áreas de capital y PLD requieren documentación interna que este análisis no tuvo.

---

**Análisis de Brecha CNSF — [institución] — [fecha]**

**Resumen ejecutivo:** [N hallazgos — X bloqueantes 🔴, Y altos 🟠, Z medios 🟡, W bajos 🟢]

**Tipo de institución:** [aseguradora / afianzadora / otra]
**Ramos:** [lista]
**Áreas cubiertas:** [lista]
**Áreas no cubiertas (insumos faltantes):** [lista]

[Tabla de hallazgos del Paso 7]

**Prioridad de remediación:**
1. [Hallazgo 🔴 más urgente]
2. [Siguiente hallazgo crítico]

**Una pregunta que haría y que no está en mi checklist:** [observación de segundo orden]
```

> **¿Qué siges?**
> 1. **Plan de remediación** — para cada hallazgo 🔴 y 🟠, preparo un plan de acción con responsable, fecha límite y evidencia de cumplimiento requerida.
> 2. **Análisis de RCS** — `/seguros-legal-mexico:solvencia-rcs` con los estados financieros para análisis detallado de capital.
> 3. **Responder requerimiento CNSF** — si hay visita de inspección activa, preparo la respuesta formal.
> 4. **Dashboard de cumplimiento** — construyo una vista interactiva con hallazgos, estados y fechas para el Comité de Auditoría.
> 5. **Escalar** — redacto nota para el Director Jurídico o despacho externo con hallazgos críticos.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
