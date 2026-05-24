---
description: >
  Prepara escritos y estrategia para la etapa prejudicial de conciliación
  obligatoria ante el Centro de Conciliación (CJFCA federal o centro estatal).
  Redacta el escrito de comparecencia, propone una oferta de conciliación con
  argumentos de apertura, y da seguimiento a los plazos de la etapa
  (Art. 684-A a 684-J LFT). Produce el convenio de conciliación si hay
  acuerdo, o el certificado de no conciliación para proceder al Tribunal.
argument-hint: "[slug del asunto | nuevo]"
---

# /cjfca-conciliacion

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer del módulo de Conciliación CJFCA: centro habitual, representante, postura de conciliación, documentos semilla.

2. **Identificar el asunto.** Si el usuario proporciona un slug, leer el `matter.md` correspondiente. Si dice "nuevo", ejecutar primero un intake básico (nombre del trabajador, evento, etapa actual) antes de continuar.

3. **Verificar plazos.** Antes de cualquier trabajo sustantivo, verificar los plazos de la etapa prejudicial:

   - **Plazo de comparecencia:** 10 días hábiles desde la notificación de la convocatoria (Art. 684-C LFT) `[settled — last confirmed 2026-05-24]`
   - **Duración máxima de la etapa:** 45 días hábiles, prorrogables por acuerdo de partes (Art. 684-D LFT) `[settled — last confirmed 2026-05-24]`
   - **Consecuencia de inasistencia injustificada:** el empleador que no comparece sin causa justificada puede ser sancionado y la etapa prejudicial se tiene por agotada en su contra (Art. 684-E LFT) `[settled — last confirmed 2026-05-24]`

   Si algún plazo está en riesgo, marcar 🔴 al inicio del output y escalar antes de continuar.

4. **Redactar el escrito de comparecencia.** Si el usuario pide el escrito o si aún no se ha presentado:

   Estructura del escrito (adaptar al formato semilla si existe en el perfil de práctica):

   ```
   [Ciudad], [fecha]

   CENTRO DE CONCILIACIÓN [FEDERAL / ESTATAL]
   PRESENTE

   [Nombre del representante], en mi carácter de apoderado legal de [nombre del empleador],
   con fundamento en el artículo 684-C de la Ley Federal del Trabajo, comparezco a dar
   respuesta a la convocatoria de fecha [fecha] en el expediente de conciliación número
   [número], promovido por [nombre del trabajador].

   ANTECEDENTES
   [Narración breve y objetiva de los hechos desde la perspectiva del empleador]

   POSTURA DEL EMPLEADOR
   [Postura de fondo: causa de terminación si es con causa, o reconocimiento de terminación
   sin causa con oferta de liquidación si aplica]

   PROPUESTA DE CONCILIACIÓN
   [Oferta económica con desglose de conceptos, o declaración de disposición a negociar]

   A T E N T A M E N T E
   [Firma del representante]
   [Nombre]
   [Cédula profesional]
   ```

   Marcar con `[review]` la sección de postura de fondo — el abogado decide cuánto revelar en la etapa prejudicial.

5. **Calcular la oferta de conciliación.** Si el usuario no tiene un monto definido:
   - Usar los datos del `matter.md` y los cálculos de `/laboral-legal-mexico:liquidacion-calculator` si ya se corrieron.
   - Proponer tres escenarios: (a) oferta base = liquidación legal exacta, (b) oferta con margen = liquidación + 10-20% para evitar juicio, (c) oferta mínima = solo proporcionales. Dejar la elección al abogado — marcar `[review]`.

6. **Redactar el convenio de conciliación (si hay acuerdo).** Si las partes llegaron a un acuerdo:

   Estructura del convenio:
   - Encabezado: fecha, expediente, partes, Centro de Conciliación
   - Antecedentes: relación laboral y causa de terminación
   - Cláusulas: monto acordado con desglose, forma de pago, fechas, documentos a entregar (carta de no adeudo, referencias laborales, documentos del trabajador)
   - Cláusula de finiquito: el trabajador declara recibir a su entera satisfacción y no tener reclamación pendiente
   - Firmas: trabajador, empleador, conciliador del centro
   - Nota obligatoria: el convenio ratificado ante el Centro tiene efecto de cosa juzgada (Art. 33 LFT) `[settled — last confirmed 2026-05-24]`

7. **Emitir certificado de no conciliación (si no hay acuerdo).** Si la etapa prejudicial se agotó sin acuerdo, confirmar que el Centro emitirá el certificado que habilita para presentar demanda ante el Tribunal Laboral. Anotar la fecha de emisión en el `matter.md` y actualizar el `_log.yaml`.

8. **Actualizar el registro del asunto.** Escribir en el `matter.md`:
   - Fecha de comparecencia
   - Oferta presentada y postura del trabajador
   - Resultado: acuerdo / no acuerdo / pendiente
   - Próxima audiencia si aplica

## Salvaguardas

- **No revelar postura de fondo sin validación.** El escrito de comparecencia en la etapa prejudicial es estratégico — el abogado decide qué revelar. La sección de postura siempre lleva `[review]`.
- **No omitir el plazo de comparecencia.** Si el plazo está por vencer, la primera línea del output es una alerta 🔴.
- **No redactar el convenio sin los montos exactos.** Si los montos no están confirmados, dejar `[PLACEHOLDER — verificar con /laboral-legal-mexico:liquidacion-calculator]`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
