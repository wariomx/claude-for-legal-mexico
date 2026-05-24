---
description: >
  Calcula la liquidación constitucional e indemnización legal de un trabajador
  bajo la LFT. Produce una tabla detallada con todos los conceptos: 3 meses
  de salario (Art. 50 frac. II LFT), 20 días por año (Art. 50 frac. II LFT),
  prima de antigüedad (Art. 162 LFT), partes proporcionales de aguinaldo
  (Art. 87 LFT), vacaciones (Art. 76 LFT), prima vacacional (Art. 80 LFT)
  y PTU (Art. 117-131 LFT). También cubre el cálculo de salarios vencidos
  para demandas de reinstalación (Art. 48 LFT).
argument-hint: "[nombre del trabajador o slug del asunto]"
---

# /liquidacion-calculator

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer parámetros del módulo de Terminación y Liquidación: salario base de cálculo (ordinario o integrado), componentes variables incluidos, documentos semilla.

2. **Recopilar datos del trabajador.** Extraer del `matter.md` activo o preguntar al usuario:
   - **Fecha de ingreso** — el cálculo de antigüedad empieza aquí
   - **Fecha de terminación** — o "hoy" si no se ha terminado todavía
   - **Salario diario ordinario** — el pagado en la nómina regular
   - **Componentes variables** que integran el salario: comisiones, bonos, despensa, ayuda de transporte, habitación, etc. (Art. 84 LFT) `[settled — last confirmed 2026-05-24]`
   - **Parte proporcional de aguinaldo en el salario diario integrado** — ¿cuántos días de aguinaldo por año?
   - **Días de vacaciones correspondientes al último período** (tabla Art. 76 LFT) `[settled — last confirmed 2026-05-24]`
   - **PTU generada y no pagada** (si la aplica)
   - **Tipo de terminación:** sin causa (liquidación constitucional) / con causa justificada / rescisión por trabajador

3. **Calcular el salario diario integrado (SDI).** Fórmula base (Art. 84 LFT):

   ```
   SDI = Salario diario ordinario
       + (Aguinaldo anual / 365)
       + (Prima vacacional / 365)
       + (Otros componentes variables anualizados / 365)
   ```

   Mostrar el cálculo paso a paso. Marcar cada componente con su fuente: `[user provided]` o `[model knowledge — verify]` si es un componente inferido.

   **Nota sobre el tope del SDI para prima de antigüedad:** la prima de antigüedad se calcula sobre el SDI, pero tiene como tope el doble del salario mínimo general (Art. 162 frac. III LFT). `[settled — last confirmed 2026-05-24]` Aplicar el tope si el SDI lo supera.

4. **Calcular antigüedad.** Años, meses y días completos desde la fecha de ingreso hasta la fecha de terminación. Para fracciones de año, calcular la parte proporcional correspondiente.

5. **Tabla de conceptos de liquidación.** Para terminación **sin causa** o por causa no justificada:

   | Concepto | Base | Factor | Días/Monto | Importe |
   |---|---|---|---|---|
   | 3 meses de salario (Art. 50 frac. II LFT) | SDI | 90 días | 90 | $[X] |
   | 20 días por año (Art. 50 frac. II LFT) | SDI | 20 × [años] | [días] | $[X] |
   | Prima de antigüedad (Art. 162 LFT) | SDI* | 12 × [años] | [días] | $[X] |
   | Aguinaldo proporcional (Art. 87 LFT) | Salario diario | [días/365 × días aguinaldo] | [días] | $[X] |
   | Vacaciones proporcionales (Art. 76 LFT) | Salario diario | [días según tabla] | [días] | $[X] |
   | Prima vacacional proporcional (Art. 80 LFT) | Vacaciones | 25% | [monto] | $[X] |
   | PTU pendiente | [dato del usuario] | | | $[X] |
   | **TOTAL** | | | | **$[X]** |

   *SDI con tope de 2 × salario mínimo para prima de antigüedad.

6. **Para terminaciones con causa justificada:** calcular solo partes proporcionales (aguinaldo, vacaciones, prima vacacional, PTU) y prima de antigüedad si aplica. No incluir los 3 meses ni los 20 días por año.

7. **Para cálculo de salarios vencidos (demanda de reinstalación, Art. 48 LFT):** calcular desde la fecha de terminación hasta la fecha estimada de resolución. Advertir: "Los salarios vencidos en México corren desde la terminación hasta la reinstalación o el pago, pero la ley establece un tope de 12 meses de salarios vencidos después de la reforma 2019 (Art. 48 párrafo segundo LFT). `[settled — last confirmed 2026-05-24]` Verificar si aplica el tope al monto calculado." Marcar `[review]` para que el abogado confirme.

8. **Nota de vigencia del salario mínimo.** El salario mínimo general se actualiza anualmente (CONASAMI). Anotar: "Se usa el salario mínimo general vigente a la fecha de terminación. `[model knowledge — verify]` Verificar el monto actual en conasami.gob.mx antes de confiar en el tope de prima de antigüedad."

9. **Resumen ejecutivo.** Antes de la tabla detallada, una línea de totales:

   > **Liquidación estimada: $[total] MXN** — 3 meses ($X) + 20 días/año ($X) + prima ($X) + proporcionales ($X). SDI: $[SDI]/día · Antigüedad: [N] años [M] meses.

10. **Árbol de decisión.** Cerrar con:

    > **¿Qué sigue?**
    > 1. **Preparar el convenio de terminación** — `/laboral-legal-mexico:escrito-laboral --tipo convenio-terminacion` usando estos montos
    > 2. **Verificar el riesgo de la terminación primero** — `/laboral-legal-mexico:termination-risk`
    > 3. **Preparar la conciliación CJFCA** — `/laboral-legal-mexico:cjfca-conciliacion` con estos montos como base de oferta
    > 4. **Exportar a Excel** — te genero un archivo Excel con la tabla de cálculo para revisión del área de nóminas

## Salvaguardas

- **No redondear silenciosamente.** Mostrar cada operación aritmética. Si hay un componente que no se puede calcular por falta de datos, dejar la celda vacía y explicar qué falta.
- **No asumir componentes del salario integrado** que el usuario no confirmó — los componentes variables cambian por empresa. Preguntar si no están en el perfil de práctica.
- **No usar salario mínimo sin verificar.** El monto del salario mínimo general es `[model knowledge — verify]` — siempre señalar que se debe confirmar en conasami.gob.mx.
- **Marcar la tabla completa como borrador.** El encabezado de la tabla lleva: "⚠️ Borrador — verificar SDI y componentes con el área de nóminas antes de firmar el convenio."

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
