---
description: >
  Genera el calendario de plazos fatales del asunto laboral activo — audiencias
  ante el Tribunal Laboral, fechas de la etapa prejudicial del CJFCA, plazos
  de contestación, prescripción, y vencimientos de obligaciones
  IMSS/INFONAVIT/NOM. Produce una lista priorizada con fundamento legal para
  cada fecha.
argument-hint: "[slug del asunto o fecha-clave de inicio]"
---

# /plazo-calendar

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer los módulos activos relevantes: CJFCA, IMSS/INFONAVIT, NOM-035/037, Terminación y Liquidación. Identificar el asunto activo del `matter.md` o preguntar al usuario si no está especificado: "¿Cuál es el asunto? Puedes darme el slug o las fechas clave."

2. **Recopilar fechas base.** Para cada módulo activo, solicitar o extraer:
   - Fecha de notificación de la convocatoria CJFCA (si existe)
   - Fecha del emplazamiento o de la demanda ante el Tribunal Laboral (si existe)
   - Fecha de la terminación del trabajador (para prescripción)
   - Fecha del último pago bimestral IMSS/INFONAVIT
   - Fecha de la última declaración anual de siniestralidad (prima de riesgo)
   - Fechas de vencimiento NOM-035/037 del perfil de práctica
   - Cualquier otro plazo que el usuario indique en el asunto

3. **Regla de días hábiles.** Para todos los cómputos de plazos procesales laborales: `[settled — last confirmed 2026-05-24]`
   - Excluir sábados y domingos.
   - Excluir los días de descanso obligatorio (Art. 74 LFT): 1 enero, primer lunes de febrero, tercer lunes de marzo, 5 febrero, 21 marzo, 1 mayo, 16 de septiembre, 20 de noviembre, 1 de diciembre (transmisión de Ejecutivo Federal cada 6 años), 25 de diciembre. `[model knowledge — verify: verificar el calendario oficial de días inhábiles del Tribunal Laboral competente, pues puede incluir días adicionales por decreto]`
   - El día de la notificación no cuenta; el plazo empieza el día hábil siguiente.

4. **Calcular plazos por etapa.**

   **Etapa prejudicial ante el CJFCA (Arts. 684-A a 684-N LFT):** `[settled — last confirmed 2026-05-24]`
   - Comparecencia inicial: **10 días hábiles** desde la notificación de la convocatoria (Art. 684-C LFT).
     `[review: plazo fatal]` — la incomparecencia injustificada genera presunción contra el patrón y puede resultar en sanción.
   - Duración máxima de la etapa prejudicial: **45 días hábiles** a partir de la primera audiencia, prorrogables por acuerdo (Art. 684-D LFT).
   - Si se llega a acuerdo conciliatorio: registrar la fecha de firma y el plazo de cumplimiento pactado.
   - Si no hay acuerdo: el CJFCA expide la Constancia de No Conciliación; a partir de ahí corre el plazo para presentar la demanda ante el Tribunal Laboral.

   **Etapa procesal ante el Tribunal Laboral:**
   - Contestación de la demanda: **15 días hábiles** a partir del emplazamiento (Art. 873-A LFT). `[settled — last confirmed 2026-05-24]`
     `[review: plazo fatal]` — la falta de contestación oportuna genera que se tengan por confesados los hechos de la demanda.
   - Período de ofrecimiento y desahogo de pruebas: verificar el auto de admisión de pruebas del Tribunal para las fechas específicas; no existe plazo fijo en la ley. `[review]`
   - Alegatos: conforme al auto del Tribunal. `[review]`

   **Prescripción de acciones laborales (Arts. 516-519 LFT):** `[settled — last confirmed 2026-05-24]`
   - Regla general: **1 año** desde que la obligación es exigible (Art. 516 LFT).
   - Acciones de nulidad de rescisión de contrato colectivo: **6 meses** (Art. 519 frac. I LFT).
   - Acciones de huelga: **60 días** (Art. 519 frac. II LFT).
   - Acciones de seguridad social (diferencias IMSS/INFONAVIT): **5 años** (Art. 300 LSS). `[settled — last confirmed 2026-05-24]`
   - Prescripción de la causal de rescisión con causa: **1 mes** desde que el patrón tuvo conocimiento (Art. 517 frac. I LFT). `[settled — last confirmed 2026-05-24]`

   **Obligaciones IMSS/INFONAVIT:**
   - Pago bimestral de cuotas: los bimestres vencen el último día hábil de los meses de febrero, abril, junio, agosto, octubre y diciembre. `[model knowledge — verify: confirmar calendario bimestral vigente en el portal IMSS]`
   - Declaración anual de siniestralidad (prima de riesgo): último día hábil de febrero de cada año. `[model knowledge — verify]`
   - `[review: plazo fatal]` — el entero extemporáneo genera actualización y recargos automáticos (Art. 40-C LSS).

   **Obligaciones NOM-035/037-STPS:**
   - Plazos de implementación: extraer del perfil de práctica. Si están en PLACEHOLDER, avisar al usuario.
   - Periodicidad de aplicación de cuestionarios NOM-035: anual como buena práctica; la norma no fija una frecuencia mínima explícita. `[model knowledge — verify: verificar si la STPS emitió criterios de periodicidad]`

5. **Tabla de plazos ordenada por fecha.**

   | Fecha | Plazo / Hito | Fundamento legal | Prioridad | Estado |
   |---|---|---|---|---|
   | AAAA-MM-DD | [descripción del plazo] | [artículo] | 🔴/🟠/🟡/🟢 | Pendiente / Completado |

   Ordenar de más próximo a más lejano. Si dos plazos caen el mismo día, listar primero el de mayor prioridad.

   **Criterio de prioridad:**
   - 🔴 **Urgente** — vence en 5 días hábiles o menos; o es un plazo cuya omisión genera consecuencias procesales irreversibles
   - 🟠 **Alto** — vence en 6 a 15 días hábiles
   - 🟡 **Medio** — vence en 16 a 30 días hábiles
   - 🟢 **Seguimiento** — vence en más de 30 días hábiles

6. **Advertencia de verificación obligatoria.** Al inicio de la tabla insertar:

   > `[review: plazo fatal]` — **Todas las fechas de esta tabla son calculadas a partir de los datos que proporcionaste.** El plazo definitivo es el que consta en la notificación oficial del Tribunal Laboral, del CJFCA, o de la autoridad administrativa (IMSS, INFONAVIT, STPS). Las resoluciones y autos pueden modificar, ampliar o acortar los plazos legales. Verificar contra el expediente físico o electrónico antes de confiar en esta tabla.

7. **Resumen de próximos 10 días hábiles.** Antes de la tabla completa, producir un bloque de atención inmediata:

   > **Próximos 10 días hábiles — atención inmediata:**
   > [Listar solo los plazos 🔴 y 🟠 con fecha, descripción breve y artículo]
   > Si no hay plazos en este rango: "Sin vencimientos urgentes en los próximos 10 días hábiles."

8. **Árbol de decisión.**

   > **¿Qué sigue?**
   > 1. **Preparar escrito para el plazo más próximo** — `/laboral-legal-mexico:escrito-laboral` con el tipo de escrito correspondiente
   > 2. **Preparar postura CJFCA** — `/laboral-legal-mexico:cjfca-conciliacion`
   > 3. **Verificar cálculo de liquidación** — `/laboral-legal-mexico:liquidacion-calculator` si hay un plazo de prescripción próximo
   > 4. **Exportar el calendario** — te genero un archivo con la tabla para compartir con el equipo o agregarla al expediente
   > 5. **Agregar un plazo que no está aquí** — dime la fecha y el fundamento y lo incorporo

## Salvaguardas

- **No asumir que los días inhábiles son solo los del Art. 74 LFT.** Los Tribunales Laborales y el CJFCA pueden tener días inhábiles adicionales por decreto o acuerdo de pleno. Siempre indicar que el usuario debe verificar el calendario del Tribunal específico.
- **No calcular plazos sin fecha base confirmada.** Si el usuario no proporciona la fecha de notificación, no estimar; preguntar. Una fecha de notificación asumida puede producir un plazo fatal calculado incorrectamente.
- **No marcar un plazo como "Completado" sin confirmación del usuario.** El skill no tiene acceso al expediente; el estado lo actualiza el abogado.

---

*Nota del revisor: el cálculo de plazos es un punto de partida, no el plazo definitivo. El único plazo jurídicamente vinculante es el que consta en la notificación o auto emitido por el Tribunal Laboral, el CJFCA o la autoridad administrativa competente. Verificar siempre contra el expediente original antes de actuar sobre las fechas de esta tabla.*

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
