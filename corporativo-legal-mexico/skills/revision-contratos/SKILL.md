---
name: revision-contratos
description: >
  Revisión cláusula a cláusula de contratos comerciales bajo derecho mexicano —
  contratos de servicios, suministro, distribución, licencias de tecnología,
  NDAs, arrendamiento mercantil, obra y compraventa. Produce un marcado de
  cambios con señales de riesgo, posiciones de negociación y árbol de decisión.
  Usar cuando se diga "revisa este contrato", "marca este acuerdo", "qué riesgos
  tiene este contrato", "redlines", "revisa las cláusulas", o cuando PI o
  litigación enruten aquí para revisión de cláusulas en un contrato más amplio.
argument-hint: "[pega el contrato o proporciona la ruta — o solo ejecuta y pide el documento]"
---

# /revision-contratos

1. Leer `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md`. Si contiene `[PLACEHOLDER]`, detener y dirigir a `/corporativo-legal-mexico:cold-start-interview`.
2. Cargar el contrato (pegado, ruta de archivo, o carpeta de asunto activo).
3. Identificar el tipo de contrato y activar el checklist correspondiente (ver abajo).
4. Recorrer el checklist cláusula a cláusula.
5. Emitir el análisis con el formato de salida estándar.
6. Cerrar con árbol de decisión.

---

## Contexto del asunto

Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗`, omitir — las habilidades usan contexto a nivel práctica. Si está habilitado y no hay asunto activo, preguntar: "¿Para qué asunto es esto?" y cargar `matter.md`. Escribir salidas en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`.

---

## Propósito

Un contrato es solo tan bueno como sus cláusulas. Esta habilidad recorre el
contrato buscando los puntos donde el derecho mexicano impone una restricción
que el redactor quizás no conocía, los puntos donde la ambigüedad crea riesgo
real, y los puntos donde la posición adoptada es negociable y vale la pena
pelear. Produce señales, no dictamina — el abogado decide cuál señal activa una
negociación.

La revisión opera sobre lo que está en el documento. No supone intención de las
partes, no normaliza redacción descuidada, no decide silenciosamente que un
riesgo es "bajo" porque la contraparte es confiable. Las señales son el trabajo;
el criterio es del abogado.

---

## Verificación de alcance y entradas

Antes de comenzar el análisis, confirmar:

1. **Documento:** ¿Ya lo tienes, o hay que pedirlo? Si hay múltiples versiones (redline, clean), ¿cuál se revisa?
2. **Lado:** ¿Representas al que propone el contrato o a quien lo recibe? Esto cambia el encuadre — el que propone defiende sus posiciones, el que recibe señala lo que rechaza.
3. **Propósito de la revisión:** ¿Primera revisión (señalar todo)? ¿Revisión de redlines de contraparte (comparar posiciones)? ¿Verificación de cierre (confirmar que los cambios acordados están bien capturados)?
4. **Jurisdicción operativa:** El checklist asume derecho federal mexicano. Si el contrato tiene elementos extranjeros (partes en el extranjero, ley aplicable extranjera, arbitraje internacional), señalarlo en la nota del revisor.
5. **Cláusulas de PI:** Si el contrato contiene cesión, licencia, obra por encargo o cláusulas de secreto industrial, enrutar esas cláusulas también a través del análisis de PI (ver sección específica abajo).

Si cualquiera de los cinco puntos no está claro, preguntar antes de hacer análisis sustantivo.

---

## Checklist de revisión — categorías universales

Estas categorías aplican a todo tipo de contrato. Las secciones específicas por tipo se activan después (ver "Tipos de contrato" abajo).

### 1. Partes y capacidad

- **Denominación completa y tipo de persona jurídica.** Una SA de CV y una S de RL de CV tienen regímenes de responsabilidad distintos. Verificar que la denominación en el contrato coincide con el acta constitutiva / RFC. Una denominación abreviada o incorrecta puede crear ambigüedad sobre quién firmó.
- **Representación legal.** ¿El firmante tiene poder suficiente? Para contratos que superen el objeto social o los límites del poder general para actos de administración, se requiere poder especial (Art. 2554 CCF). Verificar: (a) que el poder existe, (b) que está vigente (poderes notariales pueden ser revocados), (c) que su alcance cubre este acto específico. Marcar si no se ha exhibido el poder. `[review]`
- **RFC de las partes.** Contratos mercantiles que generan obligaciones fiscales requieren que las partes puedan emitir o recibir CFDI. Sin RFC válido, el impacto fiscal es del pagador.
- **Domicilio fiscal vs. domicilio convencional para notificaciones.** Son distintos. Confirmar que ambos están capturados.

### 2. Objeto

- **Claridad y completitud del objeto.** El objeto mal definido es la causa más frecuente de litigio contractual mercantil. El objeto debe ser: posible (Art. 1827 CCF), lícito (Art. 1828 CCF), y determinado o determinable (Art. 1825 CCF). Si el objeto es determinable, la fórmula de determinación debe ser objetiva.
- **NOM y normas técnicas.** Si el contrato involucra bienes o servicios regulados (alimentos, construcción, dispositivos médicos, equipos eléctricos), verificar que el objeto referencia el cumplimiento de las NOMs aplicables. Un contrato de suministro de bienes regulados sin cláusula de NOM pone el riesgo de incumplimiento normativo en el comprador.
- **Entregables y criterios de aceptación.** Sin criterios de aceptación explícitos, el prestador del servicio controla cuándo "termina" y el cliente no tiene base para rechazar. `[review]`

### 3. Precio y condiciones de pago

- **Moneda.** Contratos pactados en dólares entre personas en México: la obligación es válida pero el pago puede hacerse en pesos al tipo de cambio del día del pago (Ley Monetaria de los Estados Unidos Mexicanos, Art. 8). Si las partes quieren pago en USD efectivamente, la cláusula debe especificarlo con lenguaje de "dólares de los Estados Unidos de América de curso legal, efectivamente y en esa moneda". Sin esa precisión, la contraparte puede pagar en pesos. `[review]`
- **IVA.** Verificar si el precio es "más IVA" o "incluye IVA". La omisión crea litigio. IVA 16% general; 8% en zona fronteriza norte; 0% en exportaciones. Si el precio es a exportación, confirmar que califica como exportación de servicios bajo LIVA.
- **Retención ISR por servicios profesionales.** Si el prestador es persona física con actividad empresarial o honorarios, el pagador debe retener 10% de ISR (Art. 106 LISR). La cláusula de precio debe aclarar quién absorbe la retención o si el precio es "neto de retenciones".
- **CFDI.** Los contratos que generan obligaciones de facturación deben especificar el RFC, régimen fiscal, uso del CFDI y método de pago (PUE/PPD). Sin esto, el pagador puede no poder deducir el gasto.
- **Condiciones de pago y mora.** Verificar: plazo de pago (días naturales vs. hábiles), base del cómputo (factura, entrega, aceptación), intereses moratorios (si no están pactados aplica TIIE + 2 pp por defecto en mercantil bajo Art. 362 Código de Comercio), y forma de pago (transferencia, cheque — los cheques tienen sus propias contingencias).
- **Ajustes de precio.** Cláusulas de ajuste por inflación (INPC), tipo de cambio, o costos de insumos — verificar que el índice y la fórmula son objetivos y auditables.

### 4. Vigencia y terminación

- **Fecha de inicio.** ¿Firma, entrega del anticipo, o condición suspensiva? Si hay condición suspensiva, ¿quién la verifica y cómo?
- **Plazo definido vs. indefinido.** Contratos de plazo indefinido en servicios habituales dan al proveedor palanca de salida unilateral (aviso + plazo). Contratos de plazo definido vinculan — pero requieren pactar qué pasa al vencimiento (terminación automática, renovación automática, renegociación).
- **Renovación automática.** Si la hay, ¿en qué términos y con qué aviso de no renovación? La renovación automática sin aviso previo requerido puede atrapar a una parte en condiciones que ya no reflejan el mercado. Verificar que el plazo de aviso es operacionalmente viable.
- **Rescisión por causa (Art. 1949 CCF).** El incumplimiento grave permite a la parte afectada elegir entre cumplimiento forzado o rescisión, más daños en ambos casos. La cláusula debe definir qué constituye incumplimiento esencial (para evitar litigio sobre si un retraso de 3 días activa la rescisión), el proceso de notificación y el plazo de cura.
- **Terminación sin causa.** ¿La permite el contrato? Si sí: aviso requerido (verificar que sea razonable, no arbitrariamente corto), pago de terminación si aplica. Si el contrato es de prestación de servicios de largo plazo sin terminación sin causa, puede ser un contrato de facto de duración indefinida.
- **Consecuencias de la terminación.** Obligaciones de devolución de materiales/información, certificación de destrucción de datos, actas de entrega-recepción, pagos proporcionales por servicios parcialmente prestados.

### 5. Penalidades convencionales

- **Cláusula penal (Arts. 1840-1843 CCF).** La cláusula penal es el sustituto convenido de los daños y perjuicios. Verificar: (a) que la pena no es superior al valor de la obligación principal (Art. 1843 CCF — si lo es, es reducible judicialmente), (b) que la pena y los daños son mutuamente excluyentes o acumulables según lo pactado, (c) que el cómputo es claro (base, porcentaje, tope, periodicidad). Una cláusula penal mal redactada puede resultar en que la pena sea menor que los daños reales — o en que el acreedor no pueda cobrar nada porque no probó el daño. `[review]`
- **Penas de demora vs. penas de incumplimiento total.** Son categorías distintas; deben estar separadas en el texto.

### 6. Responsabilidad y limitaciones

- **Límite de responsabilidad.** Verificar que el techo es suficiente para cubrirte en el peor caso razonable, y que los conceptos excluidos del techo (dolo, fraude, daños a terceros) no dejan la limitación sin efecto en la práctica. `[review]`
- **Exclusión de daños consecuentes.** En derecho mexicano los "daños consecuentes" no tienen una categoría autónoma como en common law, pero la exclusión de "lucro cesante, pérdida de negocio, pérdida de reputación, o cualquier daño indirecto" tiene el mismo efecto. Verificar que la exclusión no sea tan amplia que también excluya los daños directos.
- **Daño emergente vs. lucro cesante.** Art. 2108-2110 CCF. En derecho mexicano ambos son recuperables; una cláusula que excluya el lucro cesante debe ser expresa. `[review]`
- **Seguro.** Si el contrato requiere seguro, verificar que la póliza requerida sea obtenible en el mercado mexicano a un costo razonable, que el asegurado y el beneficiario estén correctamente identificados, y que el requisito de mantener seguro durante la vigencia del contrato no se extienda indefinidamente post-terminación.

### 7. Propiedad intelectual

> **Si el contrato contiene cualquier cláusula de PI — cesión, licencia, obra por encargo, secreto industrial, non-compete tecnológico — aplicar también el análisis completo de `/propiedad-intelectual-legal-mexico:revision-clausulas-pi`. Esta sección es un triaje rápido, no la revisión completa de PI.**

- **Derechos morales — regla dura.** Cualquier cláusula que pretenda "ceder", "renunciar", "waiver" o "transferir" derechos morales es **nula de pleno derecho** bajo LFDA Art. 19. Los derechos morales son perpetuos, inalienables e irrenunciables. Si la cláusula dice "todos los derechos incluyendo derechos morales" o "waiver de derechos morales" → señal 🔴 Bloqueante automática. `[review]`
- **Obra por encargo (LFDA Arts. 83-84).** Si el contrato involucra creación de obras (software, diseño, redacción), verificar que hay una cláusula de obra por encargo que transfiere los derechos patrimoniales al comitente. Sin ella, el autor retiene los derechos patrimoniales aunque sea empleado o contratista.
- **Titularidad de mejoras.** Si el contratista desarrolla mejoras a tecnología del contratante: ¿quién las posee? Si el contratante desarrolla mejoras a tecnología del contratista: ¿concesión de licencia de regreso? `[review]`
- **Secretos industriales (LFPPI Arts. 163-172).** Si el contrato involucra acceso a secretos industriales, verificar: identificación razonable de los secretos (no puede ser todo lo que la empresa sabe), obligación de confidencialidad y su plazo post-contrato, medidas de seguridad razonables.

### 8. Confidencialidad

- **Definición de información confidencial.** ¿Es tan amplia que incluye información pública? ¿Tan estrecha que excluye lo que realmente importa? El estándar práctico: información marcada como confidencial + información que por su naturaleza es confidencial. Sin marcado automático post-término, la parte que recibe información después de que expire el plazo de marcado puede quedar sin obligación.
- **Excepciones estándar.** Información ya pública, información conocida antes de la divulgación, información desarrollada independientemente, divulgación requerida por ley. Verificar que las cuatro estén.
- **Plazo post-contrato.** ¿Cuánto tiempo sobrevive la obligación de confidencialidad? Plazo indefinido es rara vez necesario (y difícil de ejecutar); plazo de 2-5 años post-terminación es el estándar de mercado para información no técnica. Secretos industriales: plazo indefinido mientras mantengan su carácter de secreto.
- **Remedio por violación.** Los daños por violación de confidencialidad son difíciles de cuantificar. Una cláusula penal específica para violaciones de confidencialidad (independiente de la cláusula penal general) más la posibilidad de medidas cautelares es la posición que debe negociar quien comparte.

### 9. Datos personales

- **¿El contrato involucra tratamiento de datos personales?** Si el contratista accederá a datos personales del contratante (empleados, clientes, usuarios), el contratante es el responsable y el contratista es el encargado bajo LGPDPPSP Arts. 36-37.
- **Cláusula de encargado.** Verificar que el contrato incluye: (a) instrucciones de tratamiento (propósito, categorías de datos, medidas de seguridad), (b) prohibición de uso para fines propios del encargado, (c) obligación de devolver o destruir al término, (d) prohibición de subcontratar sin autorización, (e) auditoría. Sin esta cláusula, el responsable incumple LGPDPPSP y es responsable ante INAI.
- **Transferencia internacional.** Si los servidores del contratista están fuera de México, hay una transferencia internacional de datos. Verificar el mecanismo de legitimación (cláusulas contractuales estándar, consentimiento del titular, o excepción aplicable). `[review]`

### 10. Fuerza mayor

- **Definición.** ¿Incluye actos del Estado (regulación que impide la prestación), desastres naturales, pandemia, huelgas legales? ¿Excluye riesgos que la parte debió prever o mitigar? Una cláusula de fuerza mayor que abarca "cualquier circunstancia fuera del control de las partes" puede usarse como escape de cualquier incumplimiento.
- **Obligaciones durante el evento.** Aviso inmediato (¿cuántas horas?), documentación, mitigación, comunicación periódica de estatus.
- **Derechos de terminación.** Si el evento se extiende más de X días, ¿puede la parte afectada terminar sin penalidad? ¿Ambas partes o solo una?

### 11. No competencia y no solicitud

- **Límites legales en México.** El Art. 5 fr. I LFT prohíbe contratos que impliquen renuncia al derecho de ejercer una profesión o industria lícita. Una cláusula de no competencia post-contrato excesivamente amplia (por tiempo, geografía o actividad) puede ser nula. El criterio práctico: alcance razonable, compensación por la restricción, tiempo definido (no más de 2 años post-término como regla general). `[review]`
- **No solicitud de empleados.** Más ejecutable que el no competencia. Verificar que sea recíproco o que el alcance esté justificado. Una cláusula unilateral de no solicitud que solo ata al contratista puede ser desequilibrada.

### 12. Resolución de controversias

- **Jurisdicción pactada.** En contratos mercantiles, las partes pueden pactar fuero (Art. 23 CFPC). Verificar que el fuero pactado sea operativamente conveniente (ciudad donde una de las partes tiene operaciones) y que las partes renuncien expresamente al fuero de su domicilio.
- **Arbitraje.** Si hay cláusula arbitral: (a) especificar las reglas (CAM, CANACO, ICC, UNCITRAL), (b) sede (ciudad mexicana o extranjera — impacta el régimen de reconocimiento del laudo), (c) idioma, (d) número de árbitros, (e) ley aplicable al fondo. Una cláusula arbitral que solo dice "cualquier controversia se resolverá por arbitraje" es patológica — no designa institución ni reglas y puede resultar en que no haya arbitraje ejecutable. `[review]`
- **Escalamiento previo al litigio.** ¿Se requiere negociación directa y/o mediación antes del arbitraje/litigio? Si sí: plazos definidos (no "plazo razonable"), qué ocurre si no hay respuesta (derecho a proceder directamente). Una cláusula de escalamiento sin plazos puede congelar la acción de una parte indefinidamente.

### 13. Ley aplicable y disposiciones generales

- **Ley aplicable.** Para contratos con elementos extranjeros, verificar que la elección de ley aplicable es válida bajo el sistema mexicano (CPEUM Art. 121; Código de Comercio para mercantil). Una elección de ley extranjera en un contrato enteramente ejecutado en México puede no ser respetada por tribunales mexicanos. `[review]`
- **Integridad del acuerdo (merger clause).** ¿Existe? ¿Excluye específicamente representaciones previas, correos, y negociaciones? Sin merger clause, cualquier representación previa puede alegarse como parte del contrato.
- **Modificaciones.** ¿Requieren escrito firmado por ambas partes? Las modificaciones verbales a contratos escritos son difíciles de probar pero no son inválidas bajo derecho mexicano (no hay Statute of Frauds de common law). La cláusula debe ser específica.
- **Divisibilidad.** Si una cláusula es nula, ¿el contrato sobrevive? Recomendada; sin ella, la nulidad de una cláusula puede arrastrar al contrato completo bajo Art. 2226 CCF.
- **Notificaciones.** Dirección, correo electrónico, momento en que surte efectos (depósito, recepción). Correo electrónico como medio válido de notificación debe pactarse expresamente.
- **Cesión.** ¿Puede una parte ceder sus derechos sin consentimiento de la otra? La cesión de posición contractual (Art. 2051 CCF) requiere consentimiento; la cesión de crédito (Arts. 2029-2050 CCF) no. Verificar que la cláusula cubre ambas.

---

## Tipos de contrato — secciones adicionales

Activar la sección adicional según el tipo identificado. No requerir que el usuario lo clasifique — inferir del objeto.

### Contrato de servicios profesionales

- ¿Existe la distinción prestador de servicios / empleado? Elementos de subordinación (horario fijo, herramientas del contratante, lugar fijo) en un contrato de servicios crean riesgo de relación laboral encubierta (Art. 20 LFT). `[review]`
- ¿Niveles de servicio (SLA) y remedios por incumplimiento de SLA?
- ¿Quién provee las herramientas e insumos? Si el contratante los provee, aumenta el riesgo de subordinación.
- ¿Subcontratación permitida? Si sí: ¿notificación previa o consentimiento? ¿Responsabilidad solidaria del contratista por el subcontratista?

### Contrato de suministro / compraventa mercantil

- ¿Existe tabla de precios con proceso de actualización?
- ¿Cantidades mínimas comprometidas vs. proyecciones no vinculantes?
- ¿Incoterms correctamente incorporados (si aplica)?
- ¿Transferencia de riesgo y propiedad: cuándo y dónde?
- ¿Proceso de rechazo de mercancía defectuosa (plazo de inspección, notificación de vicios)?
- ¿Garantía de producto? LFTC y NOM pueden imponer garantías mínimas. `[verify — model knowledge]`

### Contrato de distribución

- ¿Exclusividad geográfica claramente definida (territorio, canales)?
- ¿Mínimos de compra vinculantes o de buena fe?
- ¿Derechos del distribuidor sobre la marca del fabricante (¿licencia expresa o implícita?)?
- ¿Consecuencias de no renovar al distribuidor? En distribución de largo plazo, México no tiene una ley de franquicia o de distribución que obligue a indemnizar al distribuidor, pero la doctrina de responsabilidad civil puede aplicar si la terminación fue abusiva. `[review — model knowledge]`
- ¿Obligaciones post-término (no competencia, devolución de materiales, transición de clientes)?

### Contrato de licencia de tecnología (software / IP)

- ¿Licencia de uso o cesión? La cesión transfiere el derecho; la licencia lo otorga. La diferencia en los efectos ante terceros es significativa.
- ¿Alcance de la licencia: comercial / no comercial, sublicenciable, modificable?
- ¿Código fuente en escrow? Si el licenciante desaparece, ¿puede el licenciatario mantener el software?
- ¿Actualizaciones y mantenimiento incluidos o separados? ¿Por cuánto tiempo?
- ¿Métricas de licenciamiento (por usuario, por núcleo, por transacción) y auditoría de cumplimiento?
- ¿Garantía de no infracción de PI de terceros e indemnización si resulta que el software infringe?

### NDA / Acuerdo de confidencialidad independiente

- ¿Unilateral o bilateral? Si unilateral, ¿claramente especificado quién divulga y quién recibe?
- ¿Propósito específico (negociación de una operación, evaluación técnica)? Sin propósito específico, el NDA puede usarse para justificar cualquier divulgación.
- ¿Plazo de vigencia razonable? NDAs "perpetuos" son difíciles de ejecutar en práctica. `[review]`

### Contrato de arrendamiento mercantil

- ¿Renta en pesos o dólares? (Aplicar análisis de moneda de la sección 3.)
- ¿Depósito: monto, condiciones de devolución, plazo de devolución?
- ¿Mejoras al local: ¿quién las hace, quién paga, qué pasa al término?
- ¿Derecho de tanteo / preferencia para renovar?
- ¿Quién paga predial, cuotas de mantenimiento, servicios?

---

## Formato de salida

Emitir el análisis en este orden:

```
⚠️ Nota del revisor
[Fuentes, lectura, señales marcadas, antes de confiar]

---

CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO [o encabezado según rol]

# Revisión de Contrato — [Nombre/Tipo]
**Partes:** [A] / [B]   **Fecha:** [...]   **Lado que representa:** [...]   **Propósito de revisión:** [...]

## Señales de alto impacto 🔴 [N]
[Solo las señales Bloqueante/Alto que requieren negociación o acción antes de firmar]

## Resumen ejecutivo
[5-8 líneas: qué hace el contrato, cuál es el riesgo principal, cuál es la posición general]

## Análisis por cláusula
[Para cada cláusula o sección: descripción de lo que dice, señal de riesgo si aplica,
posición de negociación recomendada. Formato:]

### [Número de cláusula] — [Nombre]
> **Texto:** "[cita textual relevante]"

**Señal:** [🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Sin señal]
**Problema:** [Una línea]
**Posición recomendada:** [Qué pedir o proponer]
[review] si requiere criterio del abogado
[model knowledge — verify] si la proposición jurídica necesita verificación

## Cláusulas sin señal
[Lista de cláusulas revisadas sin observaciones — para que el abogado sepa que se revisaron]

## Resumen de señales
| # | Cláusula | Severidad | Problema en una línea |
|---|---|---|---|
| 1 | § [X] — [Nombre] | 🔴 | [Descripción breve] |
```

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
