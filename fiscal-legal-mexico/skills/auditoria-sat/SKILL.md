---
description: >
  Prepara la estrategia y documentación para una auditoría del SAT — visita
  domiciliaria (Art. 44 CFF), revisión de gabinete (Art. 48 CFF), o revisión
  electrónica (Art. 53-B CFF). Identifica plazos del procedimiento, derechos del
  contribuyente, documentación a presentar, y argumentos para minimizar la
  determinación.
---

# Skill: auditoria-sat (fiscal-legal-mexico)

## Propósito

Una auditoría del SAT mal gestionada puede convertir una discrepancia menor en un crédito fiscal con recargos y multas. Este skill identifica el tipo de auditoría, mapea los plazos procedimentales críticos, lista los derechos del contribuyente y genera el checklist de documentación y la estrategia de defensa, incluyendo la ruta al acuerdo conclusivo PRODECON cuando convenga.

## Flujo

### Paso 0: leer configuración

Lee el perfil de práctica en la ruta activa. Extrae del módulo Auditoría SAT: tipo de revisión activa, período revisado, impuestos bajo revisión, fase actual, representante legal designado y postura de defensa previa.

### Paso 1: ⚠️ PLAZOS — mostrar primero

Antes de cualquier análisis de fondo, extrae e identifica las fechas clave:

> **⚠️ `[review: caducidad — determina vence AAAA-MM-DD]`**
> Tipo de auditoría: [visita domiciliaria / gabinete / electrónica / dictamen]
> Fecha de inicio de la auditoría: [fecha]
> Plazo máximo del procedimiento: [fecha límite — Art. 46-A CFF para visita domiciliaria] `[review]`
> Próximo plazo procesal activo: [nombre del plazo y fecha de vencimiento]
> `[review: caducidad — el período revisado [ejercicio] debe estar dentro del plazo de 5 años del Art. 67 CFF]`

### Paso 2: identificar tipo de auditoría

**Visita domiciliaria (Arts. 43-46 CFF):**
- Los auditores visitan el domicilio fiscal del contribuyente.
- El oficio de orden debe identificar: contribuyente, período, impuestos, número de auditores designados [settled — last confirmed 2026-05-24].
- El contribuyente tiene derecho a designar representante y testigos.
- Duración máxima: 12 meses (Art. 46-A CFF) [settled — last confirmed 2026-05-24]; ampliable a 18 meses en ciertos supuestos `[model knowledge — verify condiciones de prórroga vigentes]`.
- Etapas: inicio → actas parciales → última acta parcial (20 días hábiles para observaciones) → acta final → PAHC → crédito fiscal.

**Revisión de gabinete (Arts. 48-50 CFF):**
- El SAT solicita documentos para revisión en sus oficinas.
- Plazo para presentar información: 15 días hábiles (extensible a 30 días) [settled — last confirmed 2026-05-24].
- No hay visita al domicilio; el contribuyente entrega expediente.

**Revisión electrónica (Art. 53-B CFF):**
- Procedimiento íntegramente electrónico vía Buzón Tributario.
- El SAT emite una precliquidación; el contribuyente tiene 15 días hábiles para aceptarla o desvirtuar [settled — last confirmed 2026-05-24].
- Respuesta dentro de los 15 días hábiles siguientes a la precliquidación.

**Revisión de dictamen (Art. 52-A CFF):**
- Inicia con el Contador Público Registrado (CPR) que firmó el dictamen.
- El SAT requiere primero al CPR antes de revisar al contribuyente.

### Paso 3: derechos del contribuyente

Durante cualquier auditoría, el contribuyente tiene derecho a:

| Derecho | Referencia | Acción a tomar |
|---|---|---|
| Designar representante legal | Art. 46 CFF frac. IV | Presentar poder notarial al inicio |
| Presentar declaraciones complementarias durante la auditoría | Art. 32 CFF | Suspende caducidad para ese período `[review]` |
| Solicitar plazo adicional para reunir documentos | Art. 53-B CFF (electrónica) | Solicitar formalmente por Buzón Tributario |
| Formular observaciones a la última acta parcial | Art. 46 CFF frac. IV, 20 días hábiles | `[review]` Contar desde el día siguiente al acta |
| Aportar pruebas tras el acta final | Art. 46-A CFF, 20 días hábiles [settled — last confirmed 2026-05-24] | Reunir documentación clave |
| Acudir a PRODECON para acuerdo conclusivo | Arts. 69-C a 69-H CFF | Solo mientras la auditoría está en curso |
| Impugnar el crédito ante TFJA | Art. 13 LFPCA | 30 días hábiles desde notificación del crédito |

### Paso 4: checklist de documentación

Genera el checklist según el tipo de auditoría y los impuestos revisados:

```
CHECKLIST DE DOCUMENTACIÓN — Auditoría [tipo]
Período revisado: [ejercicio(s)] | Impuestos: [ISR / IVA / IEPS / otro]

Documentación corporativa y contable:
  [ ] Acta constitutiva y estatutos vigentes
  [ ] Poder notarial del representante legal ante el SAT
  [ ] Libros contables del período (diario, mayor, balanza de comprobación)
  [ ] Declaraciones anuales y mensuales del período
  [ ] Declaraciones informativas (DIOT, DIM, otras)

Documentación de operaciones:
  [ ] XMLs de CFDIs emitidos y recibidos (descarga masiva SAT)
  [ ] Complementos de pagos (REP) del período
  [ ] Estados de cuenta bancarios y conciliaciones
  [ ] Contratos de las operaciones relevantes
  [ ] Expediente de precios de transferencia si hay partes relacionadas

Documentación de deducciones específicas bajo revisión:
  [ ] [Listar por tipo de deducción cuestionada] `[review]`
```

### Paso 5: estrategia de defensa

Analiza las siguientes líneas de defensa y evalúa cuáles aplican al caso concreto:

- **Vicios formales del oficio de auditoría:** ¿el oficio identifica correctamente al contribuyente, período, impuestos y auditores? Cualquier omisión puede ser causal de nulidad lisa y llana.
- **Caducidad del período revisado:** verificar que el ejercicio auditado esté dentro del plazo del Art. 67 CFF. `[review: caducidad]`
- **Documentación que desvirtúa las observaciones:** identificar las actas parciales con observaciones y reunir evidencia contundente para cada punto.
- **Interpretación jurídica alternativa:** tesis del TFJA o SCJN que respalden la posición del contribuyente `[model knowledge — verify tesis aplicables]`.
- **Declaraciones complementarias:** evaluar si corregir antes del acta final reduce el monto a impugnar.
- **Acuerdo conclusivo PRODECON:** si la disputa es sobre hechos o interpretación jurídica — no solo sobre montos — considera iniciar acuerdo conclusivo para obtener la reducción del 100% de multas y suspender el plazo de la auditoría. Ejecuta `/fiscal-legal-mexico:prodecon-tramite` para el análisis detallado.

---

**⚠️ Nota del revisor:** Los mecanismos de suspensión del plazo de auditoría del Art. 46-A CFF son complejos e interactúan con las reglas de caducidad del Art. 67 CFF. Si el monto de la determinación esperada es material, retener asesor especializado en litigación fiscal antes de comprometer una postura de defensa. Este skill genera el mapa estratégico; la ejecución procesal requiere criterio especializado.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
