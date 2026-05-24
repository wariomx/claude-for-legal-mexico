---
description: >
  Revisa contratos de reaseguro — proporcional (cuota parte, excedente) y
  no proporcional (exceso de pérdida, stop loss). Evalúa la retención,
  los límites de cobertura, las exclusiones, las cláusulas financieras,
  los requisitos de reporte y las cláusulas de arbitraje. Aplica tanto
  para cedentes (aseguradoras) como para reaseguradores.
argument-hint: "[tipo de contrato de reaseguro o cláusula a revisar]"
---

# Skill: reaseguro-review (seguros-legal-mexico)

## Propósito

Los contratos de reaseguro son acuerdos entre profesionales de la industria aseguradora que no están directamente regulados por la LCS (que regula el seguro directo con el asegurado). Sin embargo, deben cumplir con las Disposiciones de Carácter General de la CNSF en materia de reaseguro y con los requisitos de registro de reaseguradores extranjeros. Este skill revisa los términos comerciales y jurídicos del contrato de reaseguro desde la perspectiva del cedente o del reasegurador.

## Marco regulatorio

| Norma | Relevancia |
|---|---|
| LISF Arts. 96-113 | Reaseguro y reafianzamiento — marco general `[model knowledge — verify artículos exactos]` |
| Disposiciones CNSF — Reaseguro | Registro de reaseguradores extranjeros, límites de retención, reportes `[verify versión vigente DOF]` |
| Principios IAIS | Prácticas internacionales de reaseguro (referencia; no vinculantes en México) |
| Ley de Arbitraje (CCo Arts. 1415-1463) | Si el contrato remite a arbitraje comercial |

**Nota sobre el derecho aplicable.** Los contratos de reaseguro frecuentemente designan como derecho aplicable el derecho inglés o neoyorquino y como foro el arbitraje CIC, Lloyd's, o AAA. Este skill analiza el contrato desde el derecho mexicano y señala cuándo el derecho extranjero o el arbitraje internacional imponen marcos distintos. `[review: derecho aplicable designado en el contrato]`

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo Reaseguro:
- Rol (cedente / reasegurador / intermediario)
- Tipos de contratos activos
- Reaseguradores principales

### Paso 1: identificar el contrato y su tipo

Si el usuario no proporcionó el contrato, solicitar:

1. "¿Tienes el contrato de reaseguro o las condiciones principales (slip)? Proporciona el documento."
2. "¿Es un contrato proporcional (cuota parte / excedente) o no proporcional (XL / stop loss)?"
3. "¿Es un contrato automático (de cartera) o facultativo (riesgo individual)?"
4. "¿Cuál es el ramo? (vida / daños / responsabilidad civil / transporte / otro)"
5. "¿Cuál es el propósito de la revisión? (negociación inicial / renovación / disputa / cumplimiento CNSF)"

### Paso 2: estructura del contrato proporcional

**Si es cuota parte (quota share):**
- [ ] Porcentaje de cesión claramente definido
- [ ] Participación del reasegurador en primas, siniestros y gastos alineada con el porcentaje de cesión
- [ ] Límite de suma asegurada por riesgo individual
- [ ] Comisión de reaseguro y comisión de participación en utilidades (profit commission): fórmula y bases de cálculo
- [ ] Retención del cedente claramente definida
- [ ] ¿El cedente retiene al menos el mínimo establecido por las Disposiciones CNSF? `[verify mínimo de retención]`

**Si es excedente (surplus):**
- [ ] Líneas del cedente y de la tabla (number of lines)
- [ ] Suma asegurada máxima por riesgo admitida a reaseguro
- [ ] Riegos que no aplican a la tabla (exclusiones de la tabla)
- [ ] Comisiones y participación en utilidades

### Paso 3: estructura del contrato no proporcional

**Si es exceso de pérdida (XL / excess of loss):**
- [ ] Retención del cedente (prioridad) claramente definida
- [ ] Límite de cobertura del reasegurador (capa) con expresión del XS
- [ ] ¿Es por riesgo, por ocurrencia o por año de cartera?
- [ ] Retención de segunda pérdida / restauraciones (reinstatements): número y costo
- [ ] Prima de reaseguro: tasa, base, ajuste mínimo/máximo
- [ ] Cláusula de pérdida máxima probable (PML) si aplica

**Si es stop loss:**
- [ ] Umbral de pérdida (como % del ratio combinado o monto absoluto)
- [ ] Límite de cobertura del reasegurador
- [ ] Período de referencia y base de medición

### Paso 4: cláusulas generales críticas

Para todos los tipos de contrato:

#### 4A. Exclusiones

- [ ] Lista de exclusiones estándar (guerra, nuklear, NCBR, terrorismo)
- [ ] Exclusiones específicas del contrato
- [ ] ¿Hay exclusiones que dejen al cedente sin cobertura para riesgos que tiene en su cartera? `[review]`
- [ ] Cláusula de cambio de condiciones del seguro directo: ¿requiere aprobación del reasegurador para cambios en condiciones?

#### 4B. Cláusulas financieras

- [ ] Depósito de primas o fondo de retención (funds withheld): monto, interés, liberación
- [ ] Carta de crédito o depósito como garantía del reasegurador extranjero
- [ ] ¿El reasegurador extranjero está registrado ante la CNSF? `[verify requisito de registro]`
- [ ] Cláusula de offset (compensación de créditos entre cedente y reasegurador): ¿es conforme con la ley aplicable?
- [ ] Moneda del contrato y cláusula de tipo de cambio

#### 4C. Cláusulas de reporte y siniestros

- [ ] Plazos de reporte de siniestros al reasegurador `[review: plazo fatal operacional]`
- [ ] Umbral de aviso de siniestros relevantes (loss advices)
- [ ] Derecho del reasegurador a participar en la defensa o la negociación del siniestro
- [ ] Cláusula de seguimiento (follow the settlement / follow the fortunes): alcance y límites
- [ ] Cláusula de ex gratia: ¿queda cubierto el pago gracioso del cedente?

#### 4D. Resolución de controversias

- [ ] Foro: ¿arbitraje o judicial?
- [ ] Si arbitraje: institución (CIC / AAA / LCIA / ad hoc), sede, número de árbitros, derecho aplicable
- [ ] Cláusula de mediación previa
- [ ] Derecho aplicable: ¿derecho mexicano o extranjero? Si es extranjero, identificar las áreas donde difiere materialmente `[review: derecho aplicable]`

#### 4E. Vigencia y terminación

- [ ] Plazo del contrato y condiciones de renovación automática
- [ ] Cláusulas de cancelación (notice period, run-off vs. cut-off)
- [ ] ¿Hay cláusulas de cancelación por deterioro crediticio del cedente o del reasegurador?
- [ ] Tratamiento de siniestros en desarrollo a la fecha de terminación (IBNR run-off)

### Paso 5: registro CNSF del reasegurador extranjero

Si el reasegurador es extranjero:

- [ ] ¿Está registrado en el padrón de reaseguradores extranjeros de la CNSF? `[verify padrón vigente en cnsf.gob.mx]`
- [ ] Si no está registrado: ¿puede la aseguradora cedente operar con él? `[review: verificar requisito de registro — puede limitar la deducibilidad o la validez de la cesión]`
- [ ] Calificación crediticia del reasegurador conforme a las exigencias CNSF `[verify calificación mínima requerida]`

### Paso 6: consolidar hallazgos

```
| # | Sección | Cláusula | Estado | Severidad | Acción |
|---|---|---|---|---|---|
| 1 | Exclusiones | Cláusula [X] | ⚠️ Deja sin cobertura riesgo activo | 🔴 | Negociar redacción |
...
```

### Paso 7: producir reporte

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [contrato proporcionado ✓ | Disposiciones CNSF: model knowledge — verify]
- Leído: [secciones revisadas]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar padrón de reaseguradores extranjeros CNSF; verificar retención mínima requerida; confirmar derecho aplicable del contrato para cláusulas de derecho extranjero.

---

**Revisión de Contrato de Reaseguro — [tipo] — [reasegurador] — [fecha]**

**Tipo de contrato:** [cuota parte / excedente / XL / stop loss / facultativo]
**Ramo:** [ramo]
**Cedente / Reasegurador:** [nombre(s)]
**Vigencia:** [fechas]
**Derecho aplicable:** [mexicano / extranjero — identificado]

[Tabla de hallazgos del Paso 6]

**Una pregunta que haría y que no está en mi checklist:** [observación]
```

> **¿Qué siges?**
> 1. **Redactar contrapropuesta** — identifico los 3-5 puntos prioritarios para negociar y preparo el lenguaje de contrapropuesta.
> 2. **Análisis de solvencia** — `/seguros-legal-mexico:solvencia-rcs` para evaluar si el programa de reaseguro cubre adecuadamente el RCS.
> 3. **Verificar registro CNSF** — busco al reasegurador en el padrón CNSF y evalúo las consecuencias de operar con uno no registrado.
> 4. **Disputa de siniestro de reaseguro** — si hay un siniestro en disputa con el reasegurador, analizo la posición bajo el contrato y la estrategia procesal.
> 5. **Escalar** — redacto nota para el Director Técnico o despacho con los hallazgos críticos.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
