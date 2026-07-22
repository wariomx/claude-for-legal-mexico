---
name: revision-clausulas-pi
description: >
  Revisión de cláusulas de PI en un contrato — cesión, titularidad, licencias,
  garantías, indemnizaciones. Usar cuando se revisen términos de PI en contratos
  laborales, de prestación de servicios, de consultoría, de licencia, obra por
  encargo, o cuando se comparta un contrato con disposiciones de PI para
  revisión.
argument-hint: "[ruta del archivo | texto pegado]"
---

# /revision-clausulas-pi

Revisa las cláusulas de propiedad intelectual de un contrato contra el perfil de
práctica en
`PROFILE`, resuelto por `matter_workspace.py status`.
Señala lagunas de cesión, ambigüedad en titularidad, problemas de alcance de
licencia, y deficiencias en garantías/indemnizaciones de PI. Produce un
memorándum con hallazgos por cláusula, priorizados por riesgo, con lenguaje de
marcado de cambios sugerido donde corresponda.

## Instrucciones

1. **Cargar
   `PROFILE` resuelto por `matter_workspace.py status`.**
   Si contiene marcadores `[PLACEHOLDER]`, detenerse y decir: "Ejecuta
   `/propiedad-intelectual-legal-mexico:cold-start-interview` primero — necesito
   conocer tu perfil de práctica antes de revisar cláusulas de PI contra él."

2. **Obtener el contrato:** Desde ruta de archivo o texto pegado. Si no se
   proporciona, preguntar.

3. **Seguir el flujo de trabajo abajo.** En particular:
   - Establecer el tipo de contrato y de qué lado está la empresa para efectos
     de PI (otorgante / receptora / ambas). La pregunta del lado es por
     documento, no una respuesta de configuración única.
   - Ejecutar la verificación de derechos morales PRIMERO — señalar cualquier
     cláusula que pretenda ceder o renunciar derechos morales porque no puede
     producir ese efecto en contra de los arts. 18-21 LFDA. El abogado determina
     nulidad parcial, severabilidad y remedio.
   - Ejecutar la verificación de cesión/transmisión después.
   - Producir hallazgos por cláusula priorizados por riesgo.
   - Verificar consistencia entre cláusulas, no solo cláusula por cláusula.
   - Anotar implicaciones jurisdiccionales (derechos morales, obra por encargo,
     invenciones laborales, licencia implícita).

4. **Producir el memorándum** según la plantilla abajo — encabezado de
   confidencialidad primero, conclusión principal, verificación de derechos
   morales, verificación de cesión, cláusulas por severidad, señales de
   consistencia, nota jurisdiccional, enrutamiento de aprobación.

5. **Respetar la postura de decisión.** Cuando una cláusula pueda leerse para
   asignar PI en cualquier dirección, señalar para revisión del abogado y
   exponer los factores que cortan en ambos sentidos. Nunca decidir
   silenciosamente una pregunta subjetiva de asignación.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:revision-clausulas-pi ~/Documentos/contrato-consultoria.pdf
/propiedad-intelectual-legal-mexico:revision-clausulas-pi
```

(Y el skill pedirá el contrato.)

---

## Derechos morales — LFDA arts. 18-21

**La salvaguarda más fuerte de este skill. Verificar ANTES de cualquier otro
análisis. No omitir. No suavizar.**

> Aplicar **MX-LFDA-MORAL-RIGHTS-001**. La persona autora es titular originaria
> y única de los derechos morales (art. 18); el derecho moral se considera
> inalienable, imprescriptible, irrenunciable e inembargable (art. 19). Las
> facultades del art. 21 incluyen:
>
> 1. **Divulgación** — decidir si la obra se da a conocer y en qué forma
> 2. **Paternidad** — ser reconocido como autor
> 3. **Integridad** — oponerse a deformaciones, mutilaciones o modificaciones
> 4. **Retracto** — retirar la obra del comercio
> 5. **Respeto** — exigir respeto a la obra
>
> **Una cláusula no puede lograr la cesión o renuncia de derechos morales en
> contra de esos artículos.** Señalar el lenguaje exacto y proponer una
> reformulación patrimonial. No declarar automáticamente nulo todo el contrato
> ni toda la cláusula: nulidad parcial, severabilidad, ley aplicable y efecto
> requieren revisión jurídica.
>
> **Calificación inicial: 🔴 Bloqueante + `[review]`** cuando la cláusula exige
> una cesión/renuncia; el abogado puede recalibrar después de analizar el texto.

Aplicar esta verificación a CADA cláusula del contrato. Las formas comunes en
que aparecen intentos de cesión/renuncia de derechos morales:

- "El autor cede la totalidad de los derechos de autor" — si no distingue
  patrimoniales de morales, pretende incluir morales → 🔴
- "El contratista renuncia a cualquier derecho moral" → 🔴
- "La empresa será considerada autora de la obra" — en México no existe la
  doctrina de *work made for hire* que convierte al empleador en autor → 🔴
- "El prestador de servicios se obliga a no ejercer sus derechos morales" → 🔴
- "Los derechos de autor corresponderán en su totalidad al cliente" — si no
  excluye expresamente los morales → 🔴
- Cualquier "waiver of moral rights" en contratos redactados en inglés que
  apliquen ley mexicana → 🔴

**Marcado de cambios propuesto para cada hallazgo 🔴 de derechos morales:**

> "REVISAR esta cláusula. Separar derechos patrimoniales de derechos morales;
> limitar la transmisión/licencia a facultades patrimoniales expresas y
> reconocer que los derechos morales se rigen por los artículos 18 a 21 de la
> LFDA. Confirmar por separado forma escrita, temporalidad, remuneración y
> severabilidad conforme a los artículos 30 a 33."

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el
CLAUDE.md a nivel de práctica. Si `Habilitado` es `✗` (el valor por defecto para
usuarios internos), omitir este párrafo — los skills usan contexto a nivel de
práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay
asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta
`/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` o di
`nivel-de-práctica`." Cargar el `matter.md` del asunto activo para contexto y
anulaciones específicas del asunto. Escribir resultados en la carpeta del asunto
en `DATA_ROOT/`.
Nunca leer archivos de otro asunto. El campo legado `Contexto entre asuntos`
no anula el hook; cambiar de asunto solo mediante el controlador.

---

## Propósito

Leer las cláusulas de PI en un contrato y decirle al abogado qué hace cada una,
cómo se desvía del estándar de mercado mexicano o de la posición estándar del
equipo, cuál es el riesgo, y — donde corresponda — el marcado de cambios
específico a proponer. El objetivo es un memorándum sobre el cual el abogado
pueda actuar en una sola pasada.

**Las cláusulas de mayor riesgo en la mayoría de los contratos son titularidad y
transmisión de derechos.** Son difíciles de corregir después. Una falla en
obtener una transmisión limpia de derechos patrimoniales en un contrato de
consultoría o de obra por encargo se descubre en debida diligencia de M&A, en
financiamientos y en litigios, a veces años después de firmado el contrato.
Si la transmisión es débil, faltante, o pretende abarcar derechos morales,
señalarlo al inicio del memorándum — no enterrarlo como un punto más.

## Precondición: cargar el perfil de práctica

**Antes de leer el contrato, leer
`PROFILE`.**
Si falta o contiene marcadores, detenerse y ejecutar
`/propiedad-intelectual-legal-mexico:cold-start-interview`. El perfil de
práctica indica:

- El alcance jurisdiccional — afecta si las cláusulas de derechos morales son
  nulas, cómo funciona la obra por encargo, si hay licencia implícita, qué tan
  amplias pueden ser las licencias
- Quién aprueba desviaciones y en qué nivel de severidad
- El encabezado de confidencialidad a anteponer en los resultados

## Flujo de trabajo

### Paso 1: Orientar

Leer el contrato completo una vez, rápido. Responder:

| Pregunta | Respuesta |
|---|---|
| ¿Qué tipo de contrato es? | Laboral / consultoría o prestación de servicios / obra por encargo (LFDA Arts. 83-84) / licencia de marca / licencia de patente / cesión de derechos / colaboración o JDA / acuerdo de confidencialidad (NDA) con cláusulas de PI / acuerdo de adquisición / otro |
| ¿De qué lado estamos para PI? | Otorgando derechos o recibiéndolos / cediendo PI o adquiriéndola / licenciante o licenciatario |
| ¿Quién es la contraparte? | Nombre, y sofisticación — persona física, startup, empresa grande |
| ¿Hay contraprestación específica por la PI? | Salario, honorarios, regalías, pago inicial, participación, ninguna |
| Ley aplicable y jurisdicción | ¿Qué dice? ¿Y nuestro perfil de práctica señala esa jurisdicción como estándar, escalar, o nunca? |

Si el lado es ambiguo (contrato de colaboración donde ambas partes contribuyen y
ambas reciben derechos, contrato de distribución con PI de flujo), preguntar:

> ¿De qué lado está [empresa] en este contrato para efectos de PI? ¿Otorgando
> derechos, recibiéndolos, o ambos? Si ambos, revisaré cada dirección por
> separado.

### Paso 2: Verificación de derechos morales (PRIORIDAD MÁXIMA)

**Ejecutar ANTES de cualquier otro análisis.** Buscar en TODO el contrato
cualquier cláusula que:

- Pretenda ceder, transferir o transmitir derechos morales
- Pretenda una renuncia de derechos morales
- Limite el ejercicio de derechos morales
- Declare que la empresa es "autora" de la obra (lo que implicaría derechos
  morales)
- Use lenguaje anglosajón como "work made for hire" sin adaptación a derecho
  mexicano
- Ceda "la totalidad de los derechos de autor" sin distinguir patrimoniales
  de morales

Si CUALQUIERA de las anteriores está presente:

```markdown
## 🔴 INCOMPATIBILIDAD — DERECHOS MORALES

**Cláusula [X]** pretende [ceder/renunciar/limitar] derechos morales del autor.

**Fundamento:** La persona autora es titular originaria y única (art. 18) y el
derecho moral es inalienable, imprescriptible, irrenunciable e inembargable
(art. 19; MX-LFDA-MORAL-RIGHTS-001). La cláusula no puede efectuar la
cesión/renuncia pretendida. `[review]` para efecto, nulidad parcial y
severabilidad; no extender la conclusión automáticamente al contrato completo.

**Riesgo:** La cláusula es inoponible. La empresa que confía en ella
descubrirá que no tiene el control que pensaba cuando el autor ejerza sus
derechos morales — particularmente divulgación, paternidad e integridad.
Esto se manifiesta en disputas sobre crédito autoral, en oposiciones a
modificaciones de la obra, y en retracto.

**Marcado de cambios propuesto:**
> "REVISAR [cláusula]. Sustituir con: 'La transmisión de derechos
> patrimoniales sobre la obra se regirá por los artículos 30 a 33 de la
> LFDA. Se reconoce que los derechos morales del autor son perpetuos,
> inalienables e irrenunciables conforme al artículo 19 de la misma ley.'"

**Escalamiento:** `[review]` — Abogado debe confirmar eliminación/reformulación
antes de firma.
```

### Paso 3: Verificación de transmisión de derechos patrimoniales

Si el contrato es un contrato de obra por encargo, de prestación de servicios,
laboral, o cualquier otro donde la empresa debería recibir derechos
patrimoniales — verificar el lenguaje de transmisión.

**Marco legal para transmisión (LFDA arts. 30-33):**

La regla verificada es que la transmisión patrimonial y la licencia exclusiva
deben constar por escrito o son nulas de pleno derecho
(`MX-LFDA-PATRIMONIAL-TRANSFER-FORM-001`). Revisar el texto vigente de los arts.
30-33 para onerosidad/remuneración, temporalidad y excepciones antes de proponer
duración. Como precisión contractual, describir derechos, modalidades,
territorio, plazo y contraprestación; no presentar esa lista como requisitos de
validez idénticos ni inventar un territorio supletorio sin fuente.

**Clasificar antes de aplicar una regla:**

- **Obra por encargo (art. 83; MX-LFDA-COMMISSIONED-WORK-001):** salvo pacto en
  contrario, quien comisiona goza de los derechos patrimoniales y facultades
  enumeradas; la persona participante conserva el derecho de mención y el
  contrato debe ser claro y preciso.
- **Obra laboral (art. 84; MX-LFDA-EMPLOYMENT-WORK-001):** con contrato
  individual escrito y sin pacto contrario, los patrimoniales se dividen por
  partes iguales; sin contrato escrito corresponden al empleado.
- En ambos, separar el análisis de facultades patrimoniales del régimen de
  derechos morales de los arts. 18-21.

**Invenciones laborales (LFT Art. 163):**
(**MX-LFT-EMPLOYEE-INVENTIONS-001**)
- La persona inventora tiene derecho a que su nombre figure como autora.
- Si se dedica, por cuenta del patrón, a investigación o perfeccionamiento de
  procedimientos, la propiedad y explotación de la patente corresponden al
  patrón; revisar posible compensación complementaria por desproporción.
- En cualquier otro caso, la propiedad corresponde a quien realizó la
  invención y el patrón tiene, en igualdad de circunstancias, derecho preferente
  al uso exclusivo o adquisición.
- No convertir uso de equipo/recursos en una tercera categoría ni asumir que
  “en ejercicio de funciones” basta sin analizar el supuesto completo.

Buscar:

- **Transmisión expresa y específica** de derechos patrimoniales — no genérica.
  "Se transmiten todos los derechos" sin especificar cuáles es insuficiente
  bajo Arts. 30-33 LFDA.
- **Modalidades de explotación** — ¿están definidas?
- **Plazo** — ¿está definido? Si falta, la ley suple 5 años.
- **Territorio** — ¿está definido? Si falta, se entiende México.
- **Comisión u obra laboral** — ¿los hechos activan el art. 83 o el 84 y cumple
  el documento con la regla correspondiente?
- **Cláusula de invenciones laborales** — si es contrato laboral, ¿se ajusta
  al Art. 163 LFT?
- **PI preexistente excluida** — ¿qué excluye la contraparte de la transmisión?
  ¿Es la lista específica o abierta?
- **Cláusula de asistencia futura** — ¿la contraparte se obliga a firmar lo
  necesario para perfeccionar la transmisión?

Si cualquiera de los anteriores falta o es débil, señalar al inicio del
memorándum con severidad 🔴 o 🟠 y un marcado de cambios específico.

```markdown
## ⚠️ DEFICIENCIA EN TRANSMISIÓN DE DERECHOS

**Cláusula [X]** transmite derechos patrimoniales, pero: [problema específico —
ej., "no especifica los derechos patrimoniales transmitidos, lo cual no cumple
con el artículo 30 de la LFDA," o "no establece plazo, por lo que la
transmisión se entenderá por 5 años conforme al artículo 33 de la LFDA," o
"es contrato de obra por encargo sin especificar contraprestación"].

**Riesgo:** Este tipo de deficiencia se descubre en debida diligencia años
después. La contraparte (o un sucesor) puede tener derechos residuales sobre
la obra que la empresa pensaba que le pertenecían.

**Marcado de cambios propuesto:**
> "[lenguaje de reemplazo específico]"

**Escalamiento:** Per
`PROFILE`,
las deficiencias de transmisión escalan a [aprobador].
```

### Paso 4: Revisión cláusula por cláusula

Para cada cláusula relevante de PI, producir un bloque. Las cláusulas a buscar:

- **Cesión/transmisión de derechos patrimoniales** — quién es titular de los
  derechos patrimoniales sobre lo creado bajo el contrato
- **Comisión / obra laboral** — clasificar y revisar art. 83 o 84 por separado
- **Titularidad de entregables** — distinta de la transmisión; suele declarar
  el producto del encargo
- **Mejoras y obras derivadas** — quién es titular de mejoras a PI
  preexistente, quién de obras derivadas
- **PI de fondo vs. PI de primer plano** — ¿el contrato define PI
  preexistente y PI nuevamente creada por separado?
- **Licencias de uso de marca** — alcance, exclusividad, territorio, campo de
  uso, sublicenciabilidad, plazo, causales de terminación, regalías, control
  de calidad del licenciante
- **Licencias de patente** — alcance, campo de uso, territorio,
  sublicenciabilidad, mejoras, regalías
- **Licencias de software** — alcance, restricciones de uso, código fuente vs.
  objeto, actualizaciones, soporte
- **Garantías de PI** — no infracción de derechos de terceros, autoridad para
  otorgar, obra original
- **Indemnizaciones de PI** — alcance, límite, procedimiento, exclusiones
  (modificaciones del usuario, combinaciones, uso no autorizado)
- **Derechos morales** — ya cubierto en Paso 2, verificar que no reaparezcan
- **Representaciones sobre software libre/código abierto** — qué OSS está o
  no incorporado en los entregables
- **Uso de marcas** — cualquier concesión o restricción sobre uso de las
  marcas de la otra parte; lineamientos de marca
- **Secreto industrial** — tratamiento de información confidencial como secreto
  industrial, medidas razonables de protección, devolución o destrucción,
  obligaciones post-terminación (LFPPI arts. 163-169;
  MX-LFPPI-TRADE-SECRETS-001)
- **Cláusula de invenciones laborales** — si es contrato laboral, conformidad
  con Art. 163 LFT

Para cada cláusula presente, producir:

```markdown
### [Cláusula X.X]: [Nombre de la cláusula]

**Qué dice:** [resumen en lenguaje llano, una o dos oraciones]

**Qué es estándar de mercado (para este tipo de contrato, este lado, esta
jurisdicción):** [referencia breve]

**Riesgo:** 🔴 Bloqueante | 🟠 Alto | 🟡 Medio | 🟢 Bajo

**Por qué importa:** [una o dos oraciones — qué sale mal para el negocio si
se queda como está]

**Marcado de cambios propuesto (si es necesario):**
> "[lenguaje de reemplazo específico]"

**Decisión pendiente:** [Si es incierto si la cláusula logra la asignación de
PI pretendida, señalar para revisión del abogado y exponer los factores que
cortan en ambos sentidos. No decidir silenciosamente una pregunta subjetiva de
asignación.] `[review]`
```

**Calibración de severidad:**

| Nivel | Significado |
|---|---|
| 🔴 Bloqueante | No firmar sin corregir. Cualquier intento de ceder/renunciar derechos morales. Deficiencia en transmisión de derechos patrimoniales en documento que debería tenerla. Licencia ilimitada donde se pretendía una limitada. Concesión exclusiva donde se pretendía no exclusiva. Comisión u obra laboral que contradice la regla aplicable del art. 83 o 84. |
| 🟠 Alto | Insistir fuertemente; escalar si no ceden. Alcance ambiguo de transmisión. Transmisión que no cumple con todos los requisitos de Arts. 30-33 LFDA (faltan derechos específicos, modalidades, plazo o territorio). Indemnización estrecha. Invención laboral no conforme a Art. 163 LFT. |
| 🟡 Medio | Pedir en primera ronda; aceptar si es el último punto abierto. Lenguaje impreciso pero cosmético, periodos de vigencia más cortos que el estándar. |
| 🟢 Bajo | Anotarlo, no gastar capital. Una desviación estilística que no cambia la asignación. |

### Paso 5: Consistencia entre cláusulas

Las cláusulas de PI fallan como sistema. Verificar:

- **¿La licencia otorgada coincide con el alcance de lo licenciado?** (Una
  licencia de "uso" es más estrecha que una de "uso, modificación y creación
  de obras derivadas.")
- **¿Las garantías cubren todo lo que cubre la licencia?** (Una garantía de
  no infracción limitada a patentes, en una licencia que también cubre
  derechos de autor y secretos industriales, deja lagunas.)
- **¿La indemnización cubre lo que promete la garantía?** (Una garantía sin
  indemnización es una promesa sin remedio.)
- **¿La terminación recupera la licencia?** (¿O una licencia pagada sobrevive
  la terminación? Cualquiera es defendible — la pregunta es si coincide con
  la intención.)
- **¿Es consistente la asignación de PI entre este contrato y cualquier SOW,
  orden de trabajo, o addendum relacionado?** Señalar conflictos.
- **¿La cláusula de secreto industrial es consistente con la cláusula de
  confidencialidad?** (A veces el NDA protege cierta información pero la
  cláusula de PI la obliga a compartirla.)

### Paso 6: Nota jurisdiccional

Las reglas de PI son jurisdiccionalmente específicas en formas que cambian el
resultado. Señalar si el contrato implica alguno de estos:

- **Derechos morales** — en México son perpetuos, inalienables e
  sujetos a los arts. 18-21 LFDA. Si el contrato aplica ley extranjera pero
  involucra autores mexicanos o se ejecuta en México, los derechos morales
  bajo ley mexicana pueden ser un piso que la ley extranjera no desplaza.
  `[review]`
- **Obra por encargo** — el art. 83 (comisión) y el art. 84 (relación laboral)
  son reglas distintas. La doctrina mexicana difiere
  fundamentalmente de la estadounidense (*work made for hire*, 17 U.S.C.
  § 101). Bajo art. 83, salvo pacto en contrario, el comitente goza de los
  derechos patrimoniales y facultades que la norma enumera; bajo art. 84, un
  contrato individual laboral escrito divide por defecto los patrimoniales en
  partes iguales salvo pacto contrario, y sin contrato escrito corresponden al
  empleado. En EE.UU., el *work for hire*
  convierte al empleador en AUTOR. Un contrato que use lenguaje de *work for
  hire* bajo ley mexicana tiene un problema fundamental de compatibilidad.
- **Transmisión de derechos patrimoniales** — la transmisión y la licencia
  exclusiva requieren forma escrita; de lo contrario son nulas de pleno
  derecho conforme al art. 30. Recuperar arts. 31-33 para las demás condiciones
  (`MX-LFDA-PATRIMONIAL-TRANSFER-FORM-001`).
- **Invenciones laborales** — Art. 163 LFT establece un régimen diferente
  al de EE.UU. La fr. II atribuye al patrón cuando la persona trabajadora se
  dedica, **por cuenta del patrón**, a investigación o perfeccionamiento; la fr. III
  atribuye los demás casos a las personas inventoras y concede al patrón un
  derecho preferente. Aplicar MX-LFT-EMPLOYEE-INVENTIONS-001.
- **Registros y licencias de PI industrial** — no usar una regla única. Para
  transmisión o gravamen de patente, registro o solicitud, el art. 137 exige
  inscripción para producir efectos en perjuicio de terceros
  (MX-LFPPI-ASSIGNMENT-REGISTRATION-001). Analizar licencias de patente y marca
  bajo sus disposiciones específicas y el objetivo de la inscripción; no
  afirmar automáticamente que toda licencia no inscrita carece de efectos.

Declarar qué ley rige el contrato, y si el perfil de práctica señala esa
jurisdicción como estándar, escalar, o nunca.

## Granularidad del marcado de cambios

**Editar con la menor granularidad posible.** Un marcado de cambios es un
artefacto de negociación, no una reescritura. La sustitución total de cláusula
señala "descartamos tu redacción" — es agresivo, obliga a la contraparte a
releer toda la cláusula, y descarta las partes que estaban bien. Los cambios
quirúrgicos — eliminar una palabra, insertar una frase, reestructurar un
inciso — señalan "tenemos pedidos específicos" y son más rápidos de leer,
entender y aceptar.

Valor por defecto: la edición más pequeña que logra la posición del playbook:
- Reemplazar una **palabra** antes que una frase.
- Reemplazar una **frase** antes que una oración.
- Reestructurar un **inciso** antes que reemplazar la oración.
- Reemplazar una **oración** antes que reemplazar la cláusula.
- Solo reemplazar una **cláusula completa** cuando la versión de la contraparte
  está tan lejos de tu posición que ediciones quirúrgicas serían más difíciles
  de leer — y cuando lo hagas, decirlo en el transmittal: "Reemplazamos la
  cláusula §X.X en lugar de marcarla porque los cambios eran extensos.
  Podemos explicar el detalle."

Ante la duda, más pequeño.

### Paso 7: Ensamblar el memorándum

Anteponer el encabezado de confidencialidad de
`PROFILE`
→ `## Resultados`.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — per plugin config ## Resultados]

# Revisión de Cláusulas de PI: [Contraparte] [Tipo de Contrato]

**Revisado:** [fecha]
**Nuestro lado para PI:** [Otorgando / Recibiendo / Ambos]
**Ley aplicable:** [jurisdicción]

---

## Conclusión principal

[Dos oraciones. ¿La asignación de PI puede mantenerse? ¿Qué tiene que cambiar
primero?]

**Hallazgos:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Aprobación necesaria de:** [nombre, per perfil de práctica]

---

## Verificación de derechos morales

[✅ Limpio — ninguna cláusula pretende afectar derechos morales |
🔴 INCOMPATIBILIDAD DETECTADA — revisar efecto y severabilidad]

---

## Verificación de transmisión de derechos patrimoniales

[✅ Transmisión cumple LFDA Arts. 30-33 | ⚠️ Deficiencia presente — ver arriba]

---

## Cláusulas por severidad

[Todos los bloques de cláusulas del Paso 4, agrupados Bloqueante → Bajo]

---

## Consistencia entre cláusulas

[Señales del Paso 5]

---

## Nota jurisdiccional

[Señales del Paso 6]

---

## Enrutamiento de aprobación

[Desde el perfil de práctica — quién aprueba, qué dispara escalamiento
automático]
```

## Tipos comunes de cláusulas de PI en contratos mexicanos

Para referencia rápida — los tipos de cláusula que aparecen frecuentemente en la
práctica mexicana de PI:

| Tipo de cláusula | Marco legal | Puntos clave de revisión |
|---|---|---|
| Cesión de derechos patrimoniales | LFDA arts. 30-33 | Forma escrita como regla verificada; además delimitar derechos, modalidades, remuneración, plazo y territorio y cotejar condiciones legales |
| Licencia de uso de marca | LFPPI | Recuperar regla de licencia/inscripción aplicable; además revisar control de calidad, exclusividad y territorio |
| Licencia de patente | LFPPI | Recuperar regla de licencia/inscripción aplicable; además revisar campo de uso, mejoras y sublicencia |
| Obra por encargo | LFDA art. 83 | Pacto contrario, claridad/precisión, facultades del comitente y derecho de mención |
| Obra laboral | LFDA art. 84 | Contrato individual escrito, pacto contrario, división igual por defecto o titularidad del empleado si falta escrito |
| Invenciones laborales | LFT art. 163 | Reconocimiento de inventor; supuesto preciso de investigación/perfeccionamiento por cuenta del patrón; compensación por desproporción; regla residual y derecho preferente |
| Secreto industrial | LFPPI arts. 163-169 | Control legal, medidas suficientes, apropiación indebida/exclusiones, confidencialidad; separar infracción y delito específicos |
| Cláusula de no competencia (PI) | Variable | En México los pactos de no competencia laborales tienen limitaciones; revisar caso por caso `[review]` |

## Postura de decisión

Cuando una cláusula pueda leerse para asignar PI en cualquier dirección, o
cuando no esté claro si las palabras elegidas por el redactor logran la
intención declarada, **señalar para revisión del abogado y exponer los factores
que cortan en ambos sentidos**. No decidir silenciosamente una pregunta
subjetiva de asignación. Una asignación de PI no resuelta que se firma es una
puerta de un solo sentido — el error se descubre en debida diligencia,
financiamiento o litigio. Señalar una cláusula ambigua que resulta estar bien
es una puerta de dos sentidos.

## Verificaciones de calidad antes de entregar

- [ ] Perfil de práctica cargado y la nota jurisdiccional refleja lo que contiene
- [ ] Derechos morales verificados PRIMERO — todo intento de cesión/renuncia
      marcado 🔴
- [ ] Transmisión de derechos patrimoniales verificada contra LFDA Arts. 30-33
- [ ] Comisión (art. 83) versus obra laboral (art. 84) clasificada y verificada
- [ ] Invenciones laborales verificadas contra LFT Art. 163 (si aplica)
- [ ] Cada hallazgo 🔴 y 🟠 tiene lenguaje de reemplazo específico
- [ ] Consistencia entre cláusulas verificada, no solo cláusula por cláusula
- [ ] Etiquetas de fuente aplicadas a citas; no se eliminaron etiquetas `verify`
- [ ] Aprobador nombrado per perfil de práctica, no "escalar a jurídico"
- [ ] Resultado marcado con el encabezado de confidencialidad

## Cierre con el árbol de decisión de siguientes pasos

Cerrar con el árbol de decisión de siguientes pasos per CLAUDE.md `## Resultados`.
Personalizar las opciones a lo que este skill produjo — las cinco ramas por
defecto (redactar el X, escalar, obtener más información, observar y esperar,
algo diferente) son un punto de partida, no un candado. El árbol es el
resultado; el abogado elige.
