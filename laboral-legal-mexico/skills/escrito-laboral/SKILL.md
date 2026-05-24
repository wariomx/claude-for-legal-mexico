---
description: >
  Redacta escritos procesales laborales en español para el Tribunal Laboral:
  contestación de demanda, excepción de incompetencia, ofrecimiento de pruebas,
  alegatos, convenio de terminación, carta de rescisión (Art. 47 LFT),
  convenio de conciliación CJFCA, y promociones de trámite. Produce el escrito
  listo para revisión del abogado, con etiquetas [review] en los párrafos
  que requieren criterio jurídico y [VERIFY] en afirmaciones de hecho.
argument-hint: "[tipo: contestacion | excepcion | pruebas | alegatos | convenio-terminacion | carta-rescision | convenio-cjfca | promocion]"
---

# /escrito-laboral

## Instrucciones

1. **Verificar configuración.** Leer el perfil de práctica activo. Extraer documentos semilla disponibles, lenguaje de resolución preferido y formato de escritos anteriores.

2. **Identificar el tipo de escrito.** Si el argumento no lo especifica, preguntar qué escrito se necesita. Opciones principales:

   - **Contestación de demanda** — respuesta a la demanda inicial del trabajador ante el Tribunal Laboral
   - **Excepción de incompetencia** — cuando el Tribunal no tiene competencia por territorio o materia
   - **Ofrecimiento de pruebas** — lista y cédulas de prueba del empleador
   - **Alegatos** — argumento final de cierre antes de la sentencia
   - **Convenio de terminación** — para firmar ante el Tribunal (Art. 33 LFT) o ante el CJFCA
   - **Carta de rescisión** — aviso formal de terminación con causa (Art. 47 LFT)
   - **Convenio de conciliación CJFCA** — acuerdo en etapa prejudicial
   - **Promoción de trámite** — cualquier otro escrito procesal

3. **Verificar plazos antes de redactar.** Dependiendo del tipo de escrito:

   | Escrito | Plazo | Fundamento |
   |---|---|---|
   | Contestación de demanda | 15 días hábiles desde el emplazamiento (Art. 873-A LFT) | `[settled — last confirmed 2026-05-24]` |
   | Ofrecimiento de pruebas | En la audiencia o en los plazos que fije el Tribunal | `[model knowledge — verify]` |
   | Carta de rescisión | Dentro de 1 mes de conocer la causa (Art. 517 frac. I LFT) | `[settled — last confirmed 2026-05-24]` |
   | Comparecencia CJFCA | 10 días hábiles desde la notificación (Art. 684-C LFT) | `[settled — last confirmed 2026-05-24]` |

   Si un plazo está en riesgo, marcar 🔴 al inicio del output.

4. **Recopilar hechos del asunto.** Extraer del `matter.md` activo o preguntar:
   - Número de expediente (Tribunal Laboral o CJFCA)
   - Partes: nombre completo del trabajador demandante, nombre del empleador demandado
   - Representante del empleador: nombre, cédula profesional, poder notarial
   - Hechos principales de la relación laboral
   - Pretensiones del trabajador (si hay demanda)
   - Hechos y documentos que el empleador puede acreditar

5. **Redactar el escrito.** Estructura general para escritos ante el Tribunal Laboral:

   ```
   [Ciudad], [fecha]

   C. JUEZ DEL TRIBUNAL LABORAL [NÚMERO] [ESTADO]
   EXPEDIENTE NÚMERO: [número]
   PRESENTE

   [Nombre del representante], con cédula profesional [número], en mi carácter de apoderado
   legal de [nombre del empleador], con domicilio para oír y recibir notificaciones en
   [domicilio], comparezco y respetuosamente expongo:

   [SECCIÓN PRINCIPAL — varía por tipo de escrito]

   Por lo anterior, a Usted C. Juez, atentamente solicito:
   [PUNTOS PETITORIOS]

   A T E N T A M E N T E
   [Firma del apoderado]
   [Nombre]
   [Cédula profesional]
   ```

   **Para contestación de demanda:**
   - Excepción general de falsedad de los hechos que no se admitan expresamente
   - Respuesta hecho por hecho a los hechos de la demanda
   - Excepciones y defensas (prescripción, incompetencia, falta de legitimación, etc.)
   - Reconocimiento de hechos que no son controvertidos

   **Para carta de rescisión (Art. 47 LFT):**
   - Fecha y lugar
   - Nombre completo del trabajador
   - Causa(s) de rescisión con referencia a la fracción exacta del Art. 47 LFT
   - Descripción de los hechos que motivan la rescisión
   - Fecha en que surte efectos
   - Firma del representante del empleador
   - Acuse de recibo (si se entrega físicamente)
   - **Nota obligatoria:** "La carta de rescisión debe entregarse al trabajador personalmente o a través del Tribunal Laboral. La entrega mediante el Tribunal requiere promoción específica y es recomendable cuando hay riesgo de que el trabajador niegue haberla recibido. `[review]`"

   **Para convenio de terminación ante el Tribunal (Art. 33 LFT):**
   - Encabezado con número de expediente
   - Antecedentes de la relación laboral
   - Declaración de voluntad de ambas partes de terminar la relación
   - Cláusulas: monto acordado, desglose de conceptos, forma y fecha de pago
   - Cláusula de finiquito total y renuncia a reclamaciones futuras
   - Nota: el convenio requiere ratificación ante el Tribunal para tener efecto de cosa juzgada (Art. 33 párrafo segundo LFT) `[settled — last confirmed 2026-05-24]`

6. **Etiquetas en el escrito.**
   - `[review]` — párrafos que el abogado debe revisar o decidir (postura estratégica, admisiones)
   - `[VERIFY: hecho específico]` — afirmaciones de hecho que el abogado debe confirmar contra los documentos del asunto
   - `[UNCERTAIN: punto procesal]` — puntos donde la práctica local del juzgado puede diferir del texto legal

7. **Nota del revisor al inicio.** Antes del escrito:

   > **⚠️ Nota del revisor**
   > - **Fuentes:** [conocimiento del modelo — verificar contra expediente y ley procesal]
   > - **Leído:** [matter.md del asunto / solo hechos proporcionados por el usuario]
   > - **Marcado para criterio:** [N elementos marcados `[review]`]
   > - **Antes de firmar:** verificar número de expediente, nombre completo de las partes, poder notarial vigente, y plazo procesal

8. **Árbol de decisión.** Cerrar con:

   > **¿Qué sigue?**
   > 1. **Revisar el escrito** — los elementos marcados `[review]` requieren tu criterio antes de presentar
   > 2. **Preparar el ofrecimiento de pruebas** — `/laboral-legal-mexico:escrito-laboral --tipo pruebas`
   > 3. **Actualizar el registro del asunto** — actualizaré el `matter.md` con la fecha de presentación y el escrito

## Salvaguardas

- **No firmar por el abogado.** El escrito es un borrador — marcar claramente "BORRADOR — pendiente de revisión y firma del abogado" en el encabezado.
- **No afirmar hechos que el usuario no confirmó.** Usar `[VERIFY: ...]` para cualquier hecho que se infirió del `matter.md` pero que el abogado debe confirmar.
- **No omitir los puntos petitorios.** Un escrito sin petición clara es una promoción deficiente — siempre incluir la sección "Por lo anterior, solicita:" con puntos numerados.
- **No usar lenguaje de otro sistema jurídico.** El escrito va dirigido al Tribunal Laboral mexicano — no usar "therefore", "whereas", "hereinafter" ni términos del common law. Usar el vocabulario del procedimiento laboral mexicano.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
