---
description: >
  Analiza una carta invitación o requerimiento del SAT por discrepancias fiscales
  — identifica el período auditado, las diferencias que el SAT detectó, las
  posibles causas, los documentos que desvirtúan la discrepancia, y prepara el
  borrador de respuesta.
---

# Skill: sat-discrepancy (fiscal-legal-mexico)

## Propósito

Una discrepancia detectada por el SAT puede resolverse antes de convertirse en un crédito fiscal — si se responde a tiempo y con la documentación correcta. Este skill extrae los datos clave del documento del SAT, clasifica la discrepancia, identifica las causas más probables y estructura el borrador de respuesta con el fundamento legal correspondiente.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae: RFC del contribuyente, ADSC asignada, historial de cartas invitación y requerimientos previos.

### Paso 1: ⚠️ PLAZO — mostrar primero

Extrae la fecha de vencimiento del documento antes de cualquier otro análisis.

> **⚠️ `[review: caducidad — respuesta vence AAAA-MM-DD]`**
> Plazo: [N días hábiles restantes a partir de hoy ([fecha actual])]
> Tipo de documento: [carta invitación / requerimiento formal]

Si el plazo ya venció: advertir de inmediato y ofrecer análisis de opciones.

### Paso 2: clasificar el documento

Determina el tipo de documento y su consecuencia jurídica:

| Tipo | Obligación de responder | Fundamento | Consecuencia de no responder |
|---|---|---|---|
| Carta invitación | No (recomendable sí) | — | Escalamiento a requerimiento formal o inicio de auditoría |
| Requerimiento formal | Sí, en plazo indicado | Art. 41 CFF [settled — last confirmed 2026-05-24] | Multa y posible determinación presuntiva |
| Oficio de discrepancia (Art. 91 LISR) | Sí | Art. 91 LISR | Determinación de ingreso presuntivo |

### Paso 3: extraer datos del documento

Del texto del documento, extrae y tabula:

| Dato | Valor extraído |
|---|---|
| Número de oficio | |
| Fecha de notificación | |
| Período revisado | |
| Impuesto(s) en discrepancia | ISR / IVA / IEPS / retenciones / nómina |
| Monto de la discrepancia | |
| Fuentes de información usadas por el SAT | DIOT / base CFDI / reportes de terceros / otra |
| Ejercicios incluidos en la revisión | |

**Verificación de caducidad del período:** confirma que el período revisado esté dentro del plazo de 5 años del Art. 67 CFF. Si el SAT está revisando períodos fuera de ese plazo, identificar la excepción aplicable (Art. 67 frac. I CFF — 10 años para ciertos supuestos) o documentar la defensa de caducidad. `[review: caducidad]` [settled — last confirmed 2026-05-24]

### Paso 4: analizar causas de la discrepancia

Para cada discrepancia identificada, analiza las causas más probables:

**Diferencias de temporalidad:**
- Deducción o ingreso reconocido en ejercicio distinto al que el SAT espera (devengado vs. efectivamente pagado).

**CFDIs no conciliados en base SAT:**
- CFDI cancelado pero no sustituido — aparece como ingreso en el sistema SAT sin la nota de crédito correspondiente.
- Error en RFC del receptor — el CFDI no aparece en la cuenta del receptor.
- CFDI en disputa con el receptor.

**Diferencias de clasificación:**
- Gasto deducible clasificado por el SAT como no deducible.
- Ingreso exento mal reportado.

**Ingreso no declarado:**
- Advierte al cliente sobre esta posibilidad y prepara el análisis de impacto si fuera confirmada.

### Paso 5: documentación a reunir

Genera un checklist de evidencia por tipo de discrepancia:

```
CHECKLIST DE EVIDENCIA — [Impuesto] [Período]

Para desvirtuar las discrepancias identificadas:

  [ ] Estados de cuenta bancarios del período — [banco(s)]
  [ ] XMLs de CFDIs emitidos y recibidos del período (descarga masiva SAT)
  [ ] Complementos de pagos (REP) correspondientes
  [ ] Contratos que soporten las operaciones cuestionadas
  [ ] Registros contables (balanza de comprobación, diario, mayor)
  [ ] Declaraciones periódicas del período (ISR / IVA / IEPS)
  [ ] DIOT presentada para el período
  [ ] Correspondencia con el receptor de los CFDIs en disputa (si aplica)
```

### Paso 6: estructura del borrador de respuesta

Genera el esquema de respuesta:

```
[Ciudad], [Fecha]

Administración Desconcentrada de Servicios al Contribuyente [ADSC]
Servicio de Administración Tributaria

Asunto: Atención al oficio número [número] de fecha [fecha]
RFC del contribuyente: [RFC]

[Nombre], en representación de [empresa], comparece para dar respuesta al
oficio citado al rubro, exponiendo:

ANTECEDENTES
[Descripción del oficio y la discrepancia señalada]

HECHOS Y ACLARACIONES
[Para cada discrepancia: explicación, causa real, referencia a documentos que la desvirtúan]

FUNDAMENTO LEGAL
[Art. 67 CFF — caducidad si aplica; disposición que respalda la deducibilidad
o clasificación del ingreso; tesis del TFJA o SCJN si hay jurisprudencia aplicable]
`[model knowledge — verify tesis aplicables]`

PRUEBAS
[Lista numerada de documentos que se acompañan]

Por lo expuesto, solicita [lo que pide: aclaración de la discrepancia / cierre del procedimiento].

[Firma y datos del representante legal]
```

---

**⚠️ Nota del revisor:** Responder a una carta invitación es voluntario pero recomendable — la no respuesta escala el asunto. Sin embargo, la respuesta debe delimitarse cuidadosamente para no confirmar la teoría del SAT ni abrir periodos no incluidos en el oficio. Revisar el alcance de la respuesta con el asesor fiscal antes de enviar. Si el monto de la discrepancia es material, considera iniciar un acuerdo conclusivo PRODECON (`/fiscal-legal-mexico:prodecon-tramite`) como alternativa a la respuesta directa.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
