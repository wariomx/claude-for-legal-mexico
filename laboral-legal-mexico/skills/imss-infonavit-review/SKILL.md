---
description: >
  Revisa el cumplimiento de obligaciones ante el IMSS e INFONAVIT — verifica
  el Salario Base de Cotización (SBC), detecta diferencias por omisión o
  subdeclaración, revisa el cálculo de la prima de riesgo (IMSS) y los
  créditos de vivienda (INFONAVIT), y prepara la postura ante una auditoría
  o visita de verificación.
argument-hint: "[RFC del patrón o slug del período a revisar]"
---

# /imss-infonavit-review

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer del módulo IMSS/INFONAVIT: registro patronal IMSS, registro patronal INFONAVIT, clase y prima de riesgo actuales, responsable de gestión, última auditoría registrada.

2. **Recopilar datos del período.** Solicitar o extraer del `matter.md` activo:
   - RFC y razón social del patrón
   - Número(s) de registro patronal IMSS
   - Número de registro patronal INFONAVIT
   - Nómina del período a revisar (bimestre/mes — pegar o adjuntar)
   - Clase de Riesgo asignada por el IMSS (I a V)
   - Dictamen IMSS previo, si existe
   - Lista de altas y bajas del período (avisos de alta/baja SUA o IDSE)

3. **Verificar el Salario Base de Cotización (SBC) por trabajador.** Artículo 27 LSS. `[settled — last confirmed 2026-05-24]`

   **Integran el SBC** (se deben incluir):
   - Salario ordinario (cuota diaria)
   - Gratificaciones y primas
   - Comisiones
   - Despensa en efectivo o vales que excedan el 40% del salario mínimo
   - Ayuda de transporte en efectivo que exceda el límite legal
   - Habitación y alimentación que el patrón proporcione

   **No integran el SBC** (Art. 27 fracs. I-IX LSS — exenciones) `[settled — last confirmed 2026-05-24]`:
   - Instrumentos de trabajo (herramientas, uniformes, equipo)
   - Ahorro cuando el patrón cotiza igual que el trabajador y los fondos son inembargables
   - Aportaciones adicionales al fondo de retiro (AFORE voluntario)
   - PTU
   - Alimentación y habitación cuando se descuente al trabajador el 20% del salario mínimo por cada concepto
   - Despensa hasta el 40% del salario mínimo
   - Premios por asistencia y puntualidad que no excedan el 10% del salario

   Para cada trabajador: calcular el SBC declarado vs. el SBC que resulta de los conceptos de nómina. Marcar discrepancias.

4. **Verificar topes del SBC.** `[settled — last confirmed 2026-05-24]`
   - **Mínimo:** salario mínimo general vigente (CONASAMI) `[model knowledge — verify]`
   - **Máximo:** 25 Unidades de Medida y Actualización (UMA) diarias `[model knowledge — verify: verificar UMA vigente en inegi.org.mx]`

5. **Calcular cuotas IMSS y aportaciones INFONAVIT.** Aplicar las tasas sobre el SBC de cada trabajador:

   | Rama del seguro | Cuota patronal | Cuota obrera | Base |
   |---|---|---|---|
   | Enfermedad y Maternidad — cuota fija (Art. 106 frac. I LSS) | 20.40% del salario mínimo | — | Por trabajador/día |
   | Enfermedad y Maternidad — cuota adicional (Art. 106 frac. II LSS) | 1.10% | 0.40% | Sobre excedente del salario mínimo |
   | Enfermedad y Maternidad — prestaciones en especie pensionados (Art. 25 Ley del IMSS) | 1.05% | 0.375% | SBC |
   | Invalidez y Vida (Art. 147 LSS) | 1.75% | 0.625% | SBC |
   | Guarderías y Prestaciones Sociales (Art. 211 LSS) | 1.00% | — | SBC |
   | Retiro, Cesantía en Edad Avanzada y Vejez — RCIV (Arts. 168-169 LSS) | 3.150% retiro + 3.150% cesantía/vejez | 1.125% cesantía/vejez | SBC |
   | INFONAVIT (Art. 29 Ley del INFONAVIT) | 5.00% | — | SBC |
   | Riesgos de Trabajo (Art. 73 LSS) | Prima según Clase de Riesgo | — | SBC |

   `[model knowledge — verify: verificar tasas vigentes en el DOF y en la Ley del IMSS antes de confiar en este cuadro]`

   Mostrar el cálculo trabajador por trabajador. Sumar totales patronales y obreros por concepto.

6. **Prima de riesgo de trabajo.** La prima se determina mediante la fórmula SATIC (Art. 72 LSS y Reglamento de la LSS). `[settled — last confirmed 2026-05-24]`
   - Verificar que la Clase de Riesgo declarada (I-V) corresponde a la actividad económica del patrón (Catálogo de Actividades del IMSS).
   - Si el patrón lleva más de un año en operación: verificar que presentó la Declaración Anual de Siniestralidad (CLEM/SRT) en febrero de cada año. `[review: plazo fatal — la declaración vence el último día hábil de febrero; el incumplimiento genera recálculo de prima por el IMSS]`
   - Comparar la prima vigente con la que resultaría de los siniestros reportados.

7. **Avisos de alta, baja y modificación de salario.** Verificar que cada movimiento en nómina tiene el aviso correspondiente:
   - Alta (Art. 15 frac. I LSS): debe presentarse antes del inicio de labores o el mismo día. `[settled — last confirmed 2026-05-24]`
   - Baja: dentro de los 5 días hábiles siguientes a la separación. `[settled — last confirmed 2026-05-24]`
   - Modificación de SBC: dentro de los 5 días hábiles del cambio. `[settled — last confirmed 2026-05-24]`
   - Trabajadores sin aviso de alta o con aviso extemporáneo = diferencia potencial a pagar.

8. **Créditos INFONAVIT activos.** Para trabajadores con crédito INFONAVIT activo:
   - Verificar que el descuento de nómina corresponde al Factor de Descuento notificado por INFONAVIT.
   - Verificar que el entero se realizó en el bimestre correcto.
   - Detectar trabajadores con crédito que no aparecen en los enteros bimestrales.
   - `[review]` — los créditos INFONAVIT en VSM (veces salario mínimo) se reconvierten anualmente; verificar la tabla de factores vigente en el portal INFONAVIT.

9. **Tabla de resultados por trabajador.**

   | CURP / NSS | Nombre | SBC declarado | SBC calculado | Diferencia | Alta/Baja correcto | Crédito INFONAVIT | Flag |
   |---|---|---|---|---|---|---|---|
   | [CURP] | [Nombre] | $[X] | $[X] | $[±X] | ✓/✗ | ✓/✗/N/A | 🔴/🟢 |

   Leyenda de flags: 🔴 diferencia o incumplimiento detectado · 🟢 sin diferencia

10. **Resumen de exposición.** Tras la tabla:
    - Total de diferencias por subdeclaración de SBC
    - Trabajadores sin aviso oportuno
    - Monto estimado de actualización y recargos `[model knowledge — verify: la tasa de actualización y recargos IMSS se fija anualmente; verificar Art. 40-C LSS y tabla vigente]`
    - `[review: plazo fatal]` — las diferencias determinadas por el IMSS pueden impugnarse mediante recurso de inconformidad dentro de **15 días hábiles** siguientes a la notificación (Art. 294 LSS). El plazo de prescripción para diferencias no determinadas es de **5 años** (Art. 300 LSS). `[settled — last confirmed 2026-05-24]`

11. **Árbol de decisión.**

    > **¿Qué sigue?**
    > 1. **Preparar correcciones** — generaré el listado de avisos de modificación de SBC a presentar en IDSE
    > 2. **Estimar actualización y recargos** — calculamos la deuda actualizada para decidir si autocorregir o esperar auditoría
    > 3. **Preparar postura de auditoría** — redacto los argumentos de defensa para cada diferencia detectada
    > 4. **Revisar prima de riesgo** — `/laboral-legal-mexico:nom-compliance` para verificar el historial de siniestralidad que alimenta la SATIC
    > 5. **Escalar** — redacto nota de escalamiento al responsable de nóminas y al área jurídica

## Salvaguardas

- **No calcular montos de multas IMSS como definitivos.** Las multas dependen de la reincidencia y el criterio del auditor. Indicar rango y remitir a `[model knowledge — verify]`.
- **No marcar como cumplido** ningún aviso sin que el usuario confirme el acuse de recibo del IMSS/INFONAVIT (número de folio o comprobante SUA/IDSE).
- **No asumir que el SBC de nómina es el SBC correcto.** El nómina puede subdeclarar sistemáticamente; la comparación es el trabajo del skill, no el punto de partida.

---

*Nota del revisor: este análisis es preliminar. La determinación formal de diferencias y la resolución de un procedimiento de auditoría requieren la intervención de un contador autorizado o un abogado con experiencia en seguridad social. Las tasas y montos de UMA deben verificarse contra fuentes primarias (DOF, INEGI, portal IMSS) antes de confiar en los totales calculados.*

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
