---
name: valuacion-acciones
description: Valúa series de acciones A, B y C de una SA de CV para operaciones de M&A conforme a LGSM y LISR. Aplica DCF, múltiplos de mercado, valor contable ajustado y valor de liquidación; entrega cuadro comparativo por serie con advertencias legales.
argument-hint: "[--modulo dcf|multiplos|contable|liquidacion]"
---

## Propósito y marco legal

Este skill guía al asesor de M&A en la valuación de series estatutarias de acciones (A, B, C) de una *Sociedad Anónima de Capital Variable* mexicana en operaciones de compra o venta. Aplica cuatro metodologías — DCF, múltiplos de mercado, valor contable ajustado y valor de liquidación — y entrega un cuadro comparativo consolidado por serie en español.

**Legislación aplicable:**
- LGSM Arts. 112-114 — derechos de las series de acciones (ordinarias, preferentes, de goce)
- LGSM Art. 113 — dividendo preferente acumulativo
- LGSM Art. 206 — derecho de separación del accionista disidente (base de valuación para el precio de reembolso)
- LGSM Arts. 232-249 — disolución y liquidación; orden de prelación en la distribución
- LISR Art. 22 — costo promedio por acción (piso fiscal en transmisión de acciones)
- Ley Federal de Competencia Económica Art. 86 — umbrales de notificación previa ante COFECE

---

## ADVERTENCIA DE ALCANCE

Este skill produce un **análisis de valuación de referencia**, no una opinión de perito. NO:

- Sustituye la opinión de perito valuador externo inscrito ante el IMCP (*Instituto Mexicano de Contadores Públicos*), que ciertos estatutos y el Art. 22 LISR requieren para efectos fiscales
- Calcula impuestos de la transacción (ISR por enajenación de acciones — remitir al plugin fiscal)
- Valúa acciones cotizadas en BMV o BIVA
- Emite carta de fairness opinion al Consejo de Administración
- Determina si la operación requiere notificación previa a COFECE (señala el umbral; el abogado decide)

---

## Fase 0 — Gatekeeping

Antes de correr cualquier módulo, confirmar que el usuario cuenta con los tres siguientes elementos. Si falta alguno, **detener y listar lo que hace falta**:

1. **Estatutos sociales o *acta constitutiva*** con la definición de las Series A, B, C y sus derechos (voto, dividendos, preferencia de liquidación, restricciones de transferencia)
2. **Estados financieros** — auditados o management accounts de al menos 3 ejercicios fiscales completos
3. **Tipo de operación declarado** — paquete de control (>50%) vs. paquete minoritario

Si se proporciona el argumento `--modulo`, omitir el flujo completo y ejecutar únicamente el módulo indicado. De cualquier forma, ejecutar el gatekeeping primero.

---

## Paso 0 — Mapeo de derechos por serie

Antes de cualquier valuación, extraer de los estatutos (o preguntar al usuario) los derechos económicos de cada serie y construir esta tabla:

| Derecho | Serie A | Serie B | Serie C |
|---------|---------|---------|---------|
| Voto | pleno / limitado / sin voto | — | — |
| Dividendo preferente | % anual / no aplica | — | — |
| Acumulativo | sí / no | — | — |
| Preferencia de liquidación | sí / no / monto fijo | — | — |
| Restricción de transferencia | ROFR / ROFO / lock-up / ninguna | — | — |
| Derecho de conversión | sí / no | — | — |

Esta tabla es el insumo de todos los módulos. Incluirla en el output final.

**Puntos legales clave a señalar aquí:**
- Si la Serie B tiene dividendo preferente acumulativo conforme al Art. 113 LGSM, ese monto acumulado es senior a cualquier distribución ordinaria y debe pagarse antes de que fluya valor alguno a la Serie A o C.
- Si alguna serie no tiene derecho a voto (*acciones sin derecho a voto*), el Art. 113 LGSM exige que esa serie reciba su dividendo preferente antes de declarar dividendo alguno sobre las acciones con voto.
- Si las restricciones de transferencia incluyen una *cláusula de exclusión de extranjeros*, señalarlo al equipo de estructuración del comprador.

---

## Módulo 1 — DCF (Flujos de Caja Descontados)

**Datos a solicitar:**

- Proyecciones de EBITDA para los años 1-5 (modelo del usuario o a construir en conjunto)
- WACC, o sus componentes:
  - Tasa libre de riesgo: rendimiento vigente de CETES a 364 días o Bonos M a 10 años `[verificar contra Banco de México]`
  - Prima de riesgo de mercado: referencia 5.0%–6.5% para México `[model knowledge — verify]`
  - Beta: beta de empresa pública comparable o estimado; SA de CV es empresa privada
  - Estructura de capital D/E
- Tasa de crecimiento terminal (g): referencia — objetivo de inflación de mediano plazo del Banco de México `[verificar]`
- Deuda neta a la fecha de valuación (deuda financiera menos efectivo y equivalentes)

**Proceso:**

1. Calcular el flujo libre a la firma (FCFF) para cada año proyectado:
   `FCFF = EBIT × (1 − tasa ISR) + D&A − CapEx − ΔCTNO`
2. Descontar cada FCFF al WACC
3. Calcular el valor terminal con el Modelo de Crecimiento de Gordon:
   `VT = FCFFn+1 / (WACC − g)`
4. Descontar el valor terminal a valor presente
5. Sumar → Valor de Empresa (EV)
6. Restar deuda neta → Valor del capital social (total)
7. Distribuir el valor del capital social entre las series conforme al orden de prelación de liquidación del Paso 0:
   - Pagar primero los montos de preferencia de liquidación a las series senior
   - Distribuir el remanente pro-rata entre las series ordinarias

**Ajustes (aplicar y revelar):**

| Ajuste | Cuándo aplicar | Rango de referencia |
|--------|---------------|---------------------|
| Descuento por falta de control (DLOC) | Paquete minoritario (<50%) | 15%–35% |
| Descuento por falta de comerciabilidad (DLOM) | Siempre (SA de CV es privada, sin mercado líquido) | 10%–30% |

**Tabla de sensibilidad (3×3):**

Producir una tabla con WACC ± 100 puntos base en un eje y g ± 50 puntos base en el otro, mostrando el valor por acción resultante para cada serie.

---

## Módulo 2 — Múltiplos de mercado

**Datos a solicitar:**

- Industria / subsector de la empresa
- Comparables propuestos por el usuario (empresas cotizadas o transacciones cerradas) o inferidos del sector
- EBITDA, Ingresos y Utilidad Neta de los últimos doce meses (LTM)

**Múltiplos a aplicar:**

| Múltiplo | Uso principal |
|----------|---------------|
| EV/EBITDA | Métrica principal en M&A México |
| EV/Ingresos | Cuando el EBITDA es negativo o distorsionado |
| P/U (Precio/Utilidad) | Complementario |

**Proceso:**

1. Aplicar cada múltiplo a la métrica LTM de la empresa → EV implícito por múltiplo
2. Reportar el rango (mínimo, mediana, máximo entre los comparables)
3. Restar deuda neta → Valor del capital social implícito
4. Aplicar DLOC y DLOM (mismos rangos que el Módulo 1; revelar y justificar)
5. Distribuir entre series conforme al orden de prelación del Paso 0

**Nota sobre comparables:** Los múltiplos de empresas públicas deben ajustarse por diferencias de tamaño, crecimiento y riesgo de mercado entre el universo de comparables y la empresa objetivo. Revelar cualquier ajuste realizado.

---

## Módulo 3 — Valor contable ajustado

**Datos a solicitar:**

- Balance general auditado más reciente
- Ajustes a valor de mercado por clase de activo, si están disponibles (avalúo de inmuebles, maquinaria, intangibles); si no están disponibles, señalarlo y usar valores contables con la etiqueta `[verificar — avalúos no proporcionados]`

**Proceso:**

1. Partir del patrimonio neto contable
2. Sumar/restar ajustes a valor de mercado por clase de activo:
   - Inmuebles: valor de avalúo menos valor en libros
   - Maquinaria y equipo: costo de reposición depreciado menos valor en libros
   - Intangibles identificados (marcas, patentes): valor razonable estimado
   - ISR diferido sobre ajustes positivos (deducir)
3. Patrimonio neto ajustado = base de distribución
4. Distribuir entre series conforme al orden de prelación del Paso 0

**Referencia fiscal — LISR Art. 22:**

> 🟠 El valor contable ajustado por acción establece la referencia fiscal mínima para efectos del Art. 22 LISR. Si el precio pactado es inferior al costo promedio por acción del vendedor (*costo promedio por acción*), el vendedor podría reconocer una pérdida fiscal sujeta a limitaciones específicas. Señalar para el plugin fiscal.

---

## Módulo 4 — Valor de liquidación

**Datos a solicitar:**

- Mismo balance que el Módulo 3
- Costos estimados de liquidación:
  - Honorarios notariales y derechos de inscripción ante el RPC
  - Costos de declaratoria de cumplimiento ante el SAT
  - Liquidación laboral (IMSS/INFONAVIT, indemnización conforme al Art. 50 LFT)
  - Honorarios profesionales del proceso de liquidación
- Tiempo estimado de realización de activos (incide en el haircut por venta forzada)

**Proceso:**

1. Aplicar haircut de venta forzada a cada clase de activo (rangos típicos: inmuebles 70%–85%, maquinaria 50%–70%, cuentas por cobrar 60%–90% del valor nominal)
2. Sumar los valores de realización de activos
3. Restar: pasivos totales + costos de liquidación
4. Resultado: *haber social* disponible
5. Distribuir conforme a los Arts. 232-249 LGSM y la prelación estatutaria:
   - Las series con preferencia de liquidación reciben primero su monto preferente
   - El remanente del *haber social* se distribuye pro-rata entre las series ordinarias

---

## Output consolidado

Entregar el análisis completo en español con la siguiente estructura:

### Encabezado

```
VALUACIÓN DE ACCIONES — ANÁLISIS DE REFERENCIA
Empresa: [nombre]
Fecha de valuación: [fecha]
Tipo de operación: [control / minoritario]
Metodologías aplicadas: [DCF / Múltiplos / Valor contable / Liquidación]
```

Anteponer el encabezado de confidencialidad del perfil de práctica (`## Resultados` en CLAUDE.md). Si no hay perfil configurado, usar:
`CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL`

### Tabla de derechos por serie

Incluir la tabla del Paso 0, completamente poblada.

### Cuadro comparativo consolidado

| Metodología | Serie A ($/acción) | Serie B ($/acción) | Serie C ($/acción) |
|-------------|-------------------|-------------------|-------------------|
| DCF | rango mín–máx | — | — |
| Múltiplos de mercado | rango mín–máx | — | — |
| Valor contable ajustado | valor puntual | — | — |
| Valor de liquidación | valor puntual | — | — |
| **Rango de referencia** | **mín — máx** | **mín — máx** | **mín — máx** |

Poblar celdas únicamente para los módulos que se ejecutaron. Marcar cualquier celda con datos incompletos con `[datos incompletos — ver nota del revisor]`.

### Tabla de sensibilidad DCF

Incluir la cuadrícula 3×3 si se ejecutó el Módulo 1.

### Advertencias legales

Señalar las que apliquen, usando la escala canónica de severidad:

> 🔴 **Derecho de separación — LGSM Art. 206:** Hay accionistas minoritarios. Si la operación implica una modificación estatutaria que afecte derechos fundamentales de los socios (cambio de objeto, fusión, transformación, traslado de domicilio al extranjero), los disidentes pueden ejercer su derecho de separación. El precio de reembolso se determina conforme a los estatutos o, en su defecto, por perito valuador. `[review — confirmar si la operación activa Art. 206]`

> 🟠 **COFECE — notificación previa:** Verificar si la operación supera los umbrales de concentración de la Ley Federal de Competencia Económica Art. 86 (umbral de valor de operación y umbral de participación de mercado). La notificación previa es obligatoria y su omisión es sancionable. `[review — verificar umbrales con datos actualizados]` `[model knowledge — verificar umbrales contra reglas vigentes de COFECE]`

> 🟠 **Fiscal — LISR Art. 22:** El precio pactado por acción debe compararse con el costo promedio por acción del vendedor. Si hay pérdida fiscal, confirmar limitaciones de deducción. Remitir al plugin fiscal para análisis ISR. `[review]`

> 🟡 **Dividendo preferente acumulado:** Si la Serie B acumula dividendo preferente no pagado, ese monto es senior a cualquier distribución ordinaria y reduce el valor disponible para las Series A y C. Confirmar monto acumulado con el *libro de actas* y los estados financieros. `[review — verificar monto acumulado]`

### Aviso legal

> *Este análisis es de referencia y no constituye una opinión de valuación formal. La valuación definitiva para efectos legales, fiscales o de terceros requiere perito valuador externo inscrito ante el IMCP. Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*

---

## Formato de nota del revisor

Colocar el siguiente bloque encima del encabezado de confidencialidad:

> **⚠️ Nota del revisor**
> - **Fuentes:** [modelo + datos proporcionados por el usuario | conectores verificados si disponibles]
> - **Módulos ejecutados:** [DCF / Múltiplos / Contable / Liquidación — indicar cuáles]
> - **Datos incompletos:** [lista de datos faltantes que afectan la precisión, o "ninguno"]
> - **Marcado para tu criterio:** [N elementos `[review]` en línea]
> - **Antes de confiar:** verificar datos de mercado usados (tasa libre de riesgo, múltiplos comparables), confirmar que el acta constitutiva revisada es la versión vigente con todas sus reformas, y remitir al perito valuador si el análisis se usará ante terceros o autoridades

---

## Árbol de decisión

Cerrar con:

> **¿Qué sigue? Elige una opción:**
> 1. **Profundizar un módulo** — puedo extender el DCF con más escenarios, construir la tabla de comparables detallada, o refinar el valor contable con ajustes adicionales.
> 2. **Redactar la sección de valuación para el SPA** — produciré las cláusulas de precio, ajuste de precio (*working capital peg*, deuda neta) y *earn-out* si aplica.
> 3. **Análisis fiscal de la transacción** — invocar el plugin fiscal para calcular el ISR del vendedor conforme al Art. 22 LISR y la retención del comprador.
> 4. **Memo al Comité de Inversión / Consejo** — redactaré un memorándum ejecutivo con el rango de referencia y la recomendación para el órgano aprobador.
> 5. **Algo diferente** — dime qué necesitas.
