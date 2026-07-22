---
name: oss-review
description: >
  Revisión de cumplimiento de licencias de código abierto para una lista de
  dependencias, una biblioteca individual o código de salida. Úsalo al revisar
  un manifiesto, SBOM o repositorio por obligaciones copyleft y compatibilidad
  de licencias, al preguntar si una biblioteca puede liberarse, o al preparar
  código para ser open-source.
argument-hint: "[ruta al manifiesto / SBOM | nombre de paquete | ruta del repo | pegar texto]"
---

# /oss-review

Ejecuta una revisión de cumplimiento de licencias de código abierto contra el
perfil de práctica en
`PROFILE`, resuelto por `matter_workspace.py status`.
Clasifica dependencias por familia de licencia, mapea obligaciones al modelo de
despliegue, señala paquetes con licencia desconocida y paquetes non-OSI que se
presentan como OSS, y recomienda acciones — cumplir, reemplazar, remover, enviar
a revisión jurídica, obtener licencia comercial.

## Instrucciones

1. **Ejecutar `matter_workspace.py status` y cargar `PROFILE`.** Si contiene placeholders, detener y preguntar: "Ejecuta `/propiedad-intelectual-legal-mexico:cold-start-interview` primero — necesito conocer tu perfil de práctica (y tu política de OSS, si la tienes) antes de poder revisar." Si el perfil de práctica apunta a una política de OSS cargada, leerla también — es la fuente de verdad para licencias aceptadas / en revisión / bloqueadas en este equipo.

2. **Establecer el alcance:** una lista de dependencias (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, pom.xml, SBOM), una biblioteca individual, o código propio que el equipo está preparando para liberar como open-source. Si el usuario proporcionó una ruta, inferir del archivo; de lo contrario, preguntar.

3. **Establecer el modelo de despliegue** antes de clasificar obligaciones — SaaS, binario distribuido, solo interno, o embebido/firmware. La misma lista de dependencias genera diferentes obligaciones dependiendo de esto.

4. **Seguir el flujo de trabajo abajo.** En particular:
   - Leer el texto real de la licencia, no solo los metadatos — los archivos LICENSE pueden estar equivocados, los metadatos del administrador de paquetes pueden estar desactualizados.
   - Clasificar cada paquete en permisiva / copyleft débil / copyleft fuerte / dominio público / non-OSI / desconocida.
   - Señalar licencia desconocida como "necesita revisión", no permisiva por defecto.
   - Señalar licencias non-OSI source-available (SSPL, BUSL, Commons Clause, Elastic License, fair-source) — no son código abierto.
   - Para código de salida, verificar que la licencia outbound elegida sea compatible con cada dependencia embebida.

5. **Emitir el memorándum** según la plantilla abajo — encabezado de confidencialidad primero, conclusión principal, señales al inicio del memorándum, bloques por paquete agrupados por severidad, nota jurisdiccional (con sección de derechos morales LFDA), revisión outbound (si aplica), enrutamiento de aprobación.

6. **Respetar la postura de decisión.** Cuando un análisis de activación copyleft depende de una cuestión controvertida (el "interactúa sobre una red" de AGPL, el "conveying" de GPL-3.0, el alcance de linking de LGPL), señalar para revisión de abogado y exponer los factores que cortan en ambos sentidos. Cualquier cosa señalada como copyleft fuerte o licencia desconocida va a un abogado antes de que la dependencia se distribuya o el código se libere.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:oss-review ~/code/mi-proyecto/package.json
/propiedad-intelectual-legal-mexico:oss-review ~/code/mi-proyecto/requirements.txt
/propiedad-intelectual-legal-mexico:oss-review redis
/propiedad-intelectual-legal-mexico:oss-review ~/code/mi-proyecto  # raíz del repo — escanear todos los manifiestos
```

---

## Funciona mejor conectado

Las solicitudes de revisión OSS usualmente llegan a través de un sistema de tickets. Conectado a Jira, Linear o Asana, este skill puede: monitorear solicitudes OSS entrantes, responder con orientación directamente en el ticket (señalando información incompleta, pidiendo el enlace al repo, devolviendo la clasificación por familia de licencia), y dar seguimiento al estado de revisión entre solicitudes.

Sin conector, pega el ticket o describe la solicitud y la manejaré una a la vez. Consulta `CONNECTORS.md` en la raíz del repo para cómo agregar un conector de ticketing.

## Contexto de asunto

**Contexto de asunto.** Usar exclusivamente `DATA_ROOT`. Si los asuntos están habilitados y no hay activo, preguntar si debe cambiarse a uno o trabajar a nivel de práctica. Cargar `DATA_ROOT/matter.md` solo con slug activo y escribir salidas en `DATA_ROOT/outputs/`. Nunca leer otra carpeta de `matters/`.

---

## Propósito

Decir al usuario qué licencias hay en su árbol de dependencias, qué obligaciones disparan esas licencias dado cómo se desplegará el código, y qué hacer con cada una. El resultado es un memorándum sobre el cual el abogado (o el ingeniero con acceso a asesor jurídico) puede actuar — cumplir, reemplazar, remover, enviar a revisión jurídica, obtener licencia comercial.

**Esta es una clasificación de primer pase.** El análisis copyleft depende del modelo de despliegue, el grado de vinculación (linking), la jurisdicción, y a veces de cuestiones jurídicas que no han sido probadas en tribunales (notablemente el "interactúa sobre una red" de AGPL, la cláusula de patentes de GPL-3.0). Para cualquier cosa que clasifique como copyleft fuerte o licencia desconocida, un abogado evalúa antes de que la dependencia se distribuya o el código se libere. El skill reporta lo que encontró; el abogado decide qué hacer.

## Precondición: cargar el perfil de práctica

**Antes de escanear dependencias, leer `PROFILE`.** Si no existe o todavía contiene placeholders, detener y ejecutar `/propiedad-intelectual-legal-mexico:cold-start-interview`. El perfil de práctica indica:

- Quién es responsable de revisión OSS en este equipo (frecuentemente ingeniería con visto bueno jurídico)
- Enrutamiento de escalamiento para obligaciones copyleft
- El encabezado de confidencialidad a anteponer

Si el perfil de práctica tiene una política de OSS cargada, leerla también — es la fuente de verdad para qué licencias acepta el equipo, cuáles requieren revisión y cuáles están bloqueadas.

## Flujo de trabajo

### Paso 1: ¿Cuál es el alcance?

Preguntar (o inferir de lo que proporcionó el usuario):

> ¿Qué estamos revisando?
>
> 1. **Una lista de dependencias** — `package.json`, `requirements.txt`, `go.mod`, `Gemfile`, `Cargo.toml`, `pom.xml`, un SBOM (SPDX / CycloneDX), un lockfile
> 2. **Una biblioteca individual** — un paquete específico que estás considerando agregar
> 3. **Nuestro propio código** — estamos planeando liberarlo como open-source y necesitamos revisar qué tiene embebido

La ruta de análisis difiere:

- Lista de dependencias → clasificar cada entrada, acumular obligaciones
- Biblioteca individual → clasificar un paquete y recorrer sus dependencias transitivas si están disponibles
- Código de salida → revisar qué hay embebido (directo y transitivo), verificar si la licencia outbound elegida es compatible con todas las licencias embebidas, verificar que los archivos LICENSE / NOTICE sean correctos

### Paso 2: ¿Cuál es el modelo de despliegue?

Esta es la entrada más importante después de la lista de licencias — la misma biblioteca genera obligaciones diferentes dependiendo de cómo se entrega el software. Preguntar:

> ¿Cómo se desplegará esto?
>
> 1. **SaaS / servicio hospedado** — los usuarios acceden por red; nada se envía al usuario
> 2. **Binario distribuido** — enviamos código compilado a usuarios (app de escritorio, app móvil, servidor on-prem, herramienta CLI)
> 3. **Solo interno** — se usa solo dentro de la empresa, no se distribuye externamente
> 4. **Embebido / firmware** — se envía en hardware o como firmware de sistema cerrado

| Despliegue | Licencias que importan materialmente |
|---|---|
| SaaS | AGPL (activación por red), atribución permisiva en cualquier UI, SSPL/BUSL/Elastic si se reutiliza como servicio competidor |
| Binario distribuido | GPL, LGPL, MPL, EPL (todas se activan en distribución), atribución permisiva |
| Solo interno | La mayoría del copyleft no se activa — sin distribución. La atribución permisiva sigue siendo buena higiene. AGPL sí se activa si usuarios fuera de la empresa interactúan por red. |
| Embebido / firmware | GPL es especialmente difícil de cumplir aquí (divulgación de código fuente + build reproducible + información de instalación en algunos casos). Planificar antes de enviar, no después. |

Señalar el modelo de despliegue en el memorándum de salida — la misma lista de dependencias revisada contra "SaaS" vs. "binario distribuido" genera obligaciones diferentes.

### Paso 3: Clasificar cada dependencia

Para cada paquete, determinar la licencia. Leer el texto real de la licencia, no solo los metadatos — los archivos LICENSE pueden estar equivocados (el archivo dice MIT pero los encabezados dicen GPL; el README afirma Apache pero no hay archivo de licencia), y los metadatos del administrador de paquetes pueden estar desactualizados.

Clasificar en:

| Categoría | Ejemplos | Obligaciones clave |
|---|---|---|
| **Permisiva** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Unlicense | Atribución, preservar texto de licencia, Apache-2.0 agrega concesión de patente + requisito de NOTICE |
| **Copyleft débil** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-1.0, EPL-2.0, CDDL | Divulgación de código fuente a nivel de archivo o biblioteca; reglas de linking varían |
| **Copyleft fuerte** | GPL-2.0, GPL-3.0, AGPL-3.0, OSL, EUPL (según versión) | Amplia divulgación de código fuente; AGPL extiende al uso por red |
| **Dominio público / dedicación** | CC0, Unlicense, WTFPL | Típicamente sin obligaciones, pero algunas son controvertidas en jurisdicciones que no reconocen la dedicación al dominio público (ver nota jurisdiccional abajo — México es una de ellas respecto a derechos morales) |
| **Non-OSI source-available** | SSPL, BUSL, Commons Clause, Elastic License, Confluent Community, familia fair-source | No son código abierto — restringen uso comercial, uso como servicio competidor, o ambos. Leer la licencia específica. |
| **Otra / personalizada / desconocida** | específica del proveedor, propietaria, archivo de licencia faltante, conflicto entre archivo y encabezados | Detener — no tratar como permisiva por defecto |

Señalar:

- **Paquetes con licencia dual** — ¿qué licencia estamos usando? La elección puede cambiar las obligaciones.
- **Paquetes obsoletos** — el paquete ya no tiene mantenimiento; ¿existe un reemplazo soportado?
- **Paquetes con dependencia copyleft en su propio árbol** — la licencia de nivel superior es permisiva pero una dependencia transitiva es copyleft.
- **Paquetes que cambiaron licencia recientemente** — Redis, MongoDB, Elastic, HashiCorp — asegurarse de que la versión fijada esté bajo la licencia que se piensa.

### Paso 4: Mapear obligaciones al modelo de despliegue

Para cada dependencia clasificada, declarar qué activa el modelo de despliegue:

```markdown
### [paquete@versión] — [Licencia]

**Clasificación:** [Permisiva / Copyleft débil / Copyleft fuerte / Dominio público / Non-OSI / Desconocida]

**Obligaciones para nuestro despliegue ([SaaS / binario / interno / embebido]):**

- [ ] [Obligación específica — p. ej., "Incluir atribución en un archivo NOTICES enviado con la app"]
- [ ] [p. ej., "Si modificamos y distribuimos, publicar código fuente de nuestras modificaciones"]
- [ ] [p. ej., "Activación por red de AGPL — si usuarios acceden nuestra versión modificada por red, el código fuente debe ofrecerse"]

**Riesgo:** 🔴 Bloqueante | 🟠 Alto | 🟡 Medio | 🟢 Bajo

**Recomendación:** [Cumplir obligaciones | Reemplazar con [alternativa] | Remover | Revisión de abogado antes de distribuir | Obtener licencia comercial de [proveedor]]
```

> **¿Cómo se consume la dependencia copyleft?** La relación de vinculación (linking) determina si el copyleft realmente se activa. Preguntar o determinar:
> - **Vinculación estática / compilación conjunta:** Las obras se combinan en un solo binario. Señal fuerte de que el copyleft se activa (LGPL "work based on the Library," GPL obra derivada).
> - **Vinculación dinámica / biblioteca compartida:** Las obras permanecen separables en tiempo de ejecución. LGPL lo permite explícitamente ("work that uses the Library"). La posición de GPL es controvertida (FSF dice obra derivada, otros discrepan).
> - **Inclusión de encabezados / funciones inline:** Puede crear obra derivada dependiendo de cuánto se incluye.
> - **Subproceso / IPC:** Procesos separados comunicándose por interfaces bien definidas. Generalmente no es obra derivada.
> - **Llamada API por red:** Para la mayoría de las licencias, no. Para **AGPL**, la cláusula de interacción por red significa que servir el software por red ES distribución. En una arquitectura de microservicios, un componente AGPL detrás de una API sí se activa.
> - **Copyleft a nivel de archivo (MPL):** Solo los archivos modificados llevan copyleft, no toda la obra. Verificar si se modificaron archivos copyleft.
>
> **La calificación de severidad depende de esto.** "LGPL — copyleft débil, reglas de linking varían" sin el análisis de linking es la respuesta que mete al ingeniero en problemas. LGPL vinculada estáticamente en un producto propietario es 🔴 Bloqueante. LGPL vinculada dinámicamente es 🟢 Bajo. Misma licencia, calificación opuesta.

**Calibración de severidad:**

| Nivel | Significa |
|---|---|
| 🔴 Bloqueante | Copyleft fuerte en un despliegue que lo activa (p. ej., GPL en binario distribuido, AGPL en SaaS). Licencia non-OSI que el modelo de negocio realmente conflicta (p. ej., SSPL mientras se construye un servicio gestionado). Licencia no determinable y el paquete es de carga. |
| 🟠 Alto | Copyleft débil con obligaciones para las que el equipo no está preparado (divulgación a nivel de archivo, requisitos de NOTICE). Licencia dual donde la licencia elegida es ambigua. El archivo de licencia dice una cosa, los encabezados dicen otra. |
| 🟡 Medio | Permisiva con requisitos de atribución que no se han integrado al build (archivo NOTICES faltante, LICENSE faltante en distribución). Copyleft transitivo en una posición que puede o no activarse, dependiendo de cómo se consume la biblioteca. |
| 🟢 Bajo | Permisiva con obligaciones ya satisfechas. Copyleft en un modelo de despliegue que no lo activa (p. ej., biblioteca GPL usada solo internamente, sin redistribución). |

### Paso 5: Señalar modos de falla

Llamar la atención sobre cualquiera de los siguientes en una sección al inicio del memorándum:

- **Licencia desconocida** — clasificar como "necesita revisión", no permisiva. Una dependencia sin clasificar debe detener una decisión de distribución, no pasar inadvertida.
- **El archivo de licencia conflicta con los encabezados de archivos** — leer ambos y reportar el conflicto.
- **Combinaciones incompatibles** — GPL-2.0 only + Apache-2.0 históricamente una incompatibilidad conocida; revisar combinaciones MPL / EPL / GPL cuidadosamente.
- **Licencias non-OSI presentándose como código abierto** — SSPL, BUSL, Commons Clause, Elastic License, Confluent Community. Leer la licencia; no confiar en la insignia de "open source" de GitHub.
- **Cambios de licencia** — si una versión anterior era permisiva y la versión actual es source-available, la versión fijada importa.

### Paso 6: Revisión outbound (si se revisa código propio antes de liberar como open-source)

Si el usuario está preparando código para liberar como open-source:

- Confirmar que la licencia outbound elegida es compatible con la licencia de cada dependencia embebida (p. ej., no se puede liberar bajo MIT si se tiene código GPL embebido — la obra combinada debe ser GPL)
- Confirmar que el archivo LICENSE está presente y es correcto
- Confirmar que el archivo NOTICE está presente y lista las atribuciones requeridas (Apache-2.0 y otras)
- Confirmar que los textos de licencia de terceros están incluidos donde se requiere
- Confirmar que no hay código propietario o confidencial, ni datos de clientes, ni credenciales embebidas en el historial del repo
- Confirmar política de marca para cualquier nombre de proyecto (separada de la licencia de derechos de autor)
- **Verificar titularidad de derechos patrimoniales** — ver sección de obra por encargo LFDA abajo

### Paso 7: Ensamblar el memorándum

Anteponer el encabezado de confidencialidad de `PROFILE` → `## Resultados` (varía por rol del usuario — ver `## Quién usa este plugin`).

Este memorándum y cualquier lista de dependencias revisada pueden ser confidenciales o privilegiados, o ambos. El resultado hereda ese estatus de la fuente. Distribuir solo dentro del círculo de confidencialidad; retirar el encabezado de confidencialidad antes de cualquier entrega externa (incluyendo antes de adjuntar el memorándum a un ticket de ingeniería fuera del círculo de confidencialidad).

> **Sin suplemento silencioso.** Si una consulta de investigación a la herramienta de investigación jurídica configurada devuelve pocos o ningún resultado para una regla que el memorándum necesita (ejecutabilidad del activador por red de AGPL en una jurisdicción dada, alcance de la concesión de patentes de GPL-3.0, texto de licencia más reciente de un paquete relicenciado recientemente), reportar lo encontrado y detenerse. NO llenar la laguna con búsqueda web o conocimiento del modelo sin preguntar. Decir: "La búsqueda devolvió [N] resultados de [herramienta]. La cobertura parece escasa para [regla / licencia / jurisdicción]. Opciones: (1) ampliar la consulta de búsqueda, (2) probar otra herramienta de investigación, (3) buscar en la web — los resultados se etiquetarán `[web search — verify]` y deben verificarse contra una fuente primaria antes de confiar, o (4) marcar como no verificado y detener. ¿Cuál prefieres?" Un abogado decide si aceptar fuentes de menor confianza.
>
> **Atribución de fuentes.** Donde el memorándum cite un texto de licencia, una decisión judicial interpretando una licencia, u orientación de un administrador (FSF, OSI, SPDX, SFLC), etiquetar la cita: `[OSI]`, `[SPDX]`, `[FSF]`, `[SFC/SFLC]`, `[LegalDataHunter]`, `[Solve Intelligence]`, `[SCJN IUS]`, `[DOF]`, `[IMPI]`, `[INDAUTOR]`, o el nombre de la herramienta MCP para citas recuperadas de un conector; `[web search — verify]` para resultados aún no primarios; `[model knowledge — research lead only]` para una pista que no puede sustentar el resultado; `[user provided]` para texto leído directamente del repo. Nunca quitar ni colapsar las etiquetas.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — según configuración del plugin ## Resultados]

# Revisión OSS: [Proyecto / Lista de Dependencias / Paquete]

**Revisado:** [fecha]
**Alcance:** [Lista de dependencias / Biblioteca individual / Código de salida]
**Modelo de despliegue:** [SaaS / Binario / Interno / Embebido]

---

## Conclusión principal

[Dos oraciones. ¿Se puede distribuir? ¿Qué tiene que pasar primero?]

**Paquetes revisados:** [N]
**Por clasificación:** [N permisivas, N copyleft débil, N copyleft fuerte, N dominio público, N non-OSI, N desconocidas]
**Hallazgos:** [N]🔴 [N]🟠 [N]🟡 [N]🟢

**Aprobación necesaria de:** [nombre, según perfil de práctica]

---

## Señales al inicio del memorándum

[Lista de licencia desconocida, lista de conflictos de licencia, lista de non-OSI presentándose como OSS, combinaciones incompatibles]

---

## Por paquete

[Bloques del Paso 4, agrupados por severidad]

---

## Nota jurisdiccional — México

La ejecutabilidad de licencias OSS varía — el activador por red de AGPL no ha sido ampliamente probado en tribunales; la cláusula de patentes de GPL-3.0 se lee diferente bajo diferentes regímenes de patentes; las dedicaciones al dominio público no son universalmente reconocidas. Declarar la elección de ley aplicable para cualquier distribución aguas abajo (p. ej., contratos con proveedores que incorporan el código) y señalar jurisdicciones que el perfil de práctica marca como escalamiento.

### Derechos morales y código abierto en México (LFDA Art. 19)

Aplicar MX-LFDA-MORAL-RIGHTS-001: la persona autora es titular originaria y
única (art. 18), y el derecho moral es inalienable, imprescriptible,
irrenunciable e inembargable (art. 19). El software está protegido en términos
de la LFDA, pero cada consecuencia contractual requiere hechos sobre autoría,
ley aplicable y cadena de titularidad.

**1. Reconocimiento de autoría (art. 21, fr. II LFDA).** Recuperar el texto
vigente al aplicarlo y leerlo con `MX-LFDA-MORAL-RIGHTS-001`. Para código
abierto esto exige separar la obligación contractual de atribución, autoría de
cada contribución, ley aplicable y el derecho moral potencialmente invocado:

- Las cláusulas de atribución en licencias permisivas crean obligaciones
  contractuales; no afirmar automáticamente una segunda infracción moral sin
  identificar persona autora, contribución, atribución exigible y ley aplicable.
- Una omisión en NOTICE puede ser incumplimiento de licencia. Evaluar por
  separado si también afecta un derecho moral concreto.
- Un CLA que pretenda una renuncia total no puede efectuar la renuncia de
  derechos morales prohibida por la LFDA. Marcar el texto exacto; el efecto y
  severabilidad requieren revisión jurídica.

**2. Derecho de integridad (Art. 21, fracc. III LFDA).** El autor puede oponerse a modificaciones que perjudiquen su honor o reputación. En el contexto OSS:

- En la práctica, las licencias OSS que permiten modificaciones (casi todas) coexisten con el derecho de integridad porque las modificaciones de código rara vez perjudican el honor o la reputación del autor.
- Sin embargo, el riesgo existe en casos extremos: p. ej., modificar el código de un autor mexicano para que realice funciones maliciosas, ilegales o contrarias a la ética, manteniendo la atribución al autor original, podría activar el derecho de integridad. `[review]`

**3. Dedicaciones al dominio público.** Instrumentos como CC0 no pueden lograr
una renuncia de derechos morales contraria a la LFDA. No afirmar sin análisis
que la dedicación patrimonial sea plenamente efectiva en México: revisar forma,
temporalidad, remuneración, ley aplicable y licencia de respaldo.

**4. Consecuencia práctica para este escaneo:**

- Si una persona contribuidora puede invocar LFDA, abrir una revisión de autoría,
  ley aplicable y derecho moral; la nacionalidad por sí sola no resuelve el caso.
- Verificar NOTICE/AUTHORS contra la licencia y la cadena de contribución; no
  inventar una obligación formal idéntica para todo paquete únicamente a partir
  del art. 21.
- Señalar cualquier CLA que pretenda obtener renuncia total de derechos — es inaplicable para la porción de derechos morales con autores mexicanos.

### Obra por encargo y obra laboral — reglas distintas (LFDA arts. 83-84)

Cuando una empresa mexicana libera como open-source código desarrollado por sus empleados o contratistas, la titularidad de derechos patrimoniales depende de la existencia de un contrato escrito:

- **Art. 83 LFDA — comisión:** salvo pacto en contrario, quien comisiona la obra
  goza de los derechos patrimoniales y facultades enumeradas; la persona que
  participa conserva el derecho de mención y los términos deben ser claros y
  precisos (MX-LFDA-COMMISSIONED-WORK-001).
- **Art. 84 LFDA — relación laboral:** con contrato individual escrito y sin
  pacto contrario, los derechos patrimoniales se dividen por partes iguales;
  sin contrato escrito corresponden al empleado
  (MX-LFDA-EMPLOYMENT-WORK-001).
- La autorización para publicar bajo una licencia OSS exige revisar quién posee
  qué facultades patrimoniales; no inferirlas de la etiqueta “empleado” o
  “contratista”.

**Implicación práctica para revisión outbound:**

- Clasificar primero comisión (art. 83) versus relación laboral (art. 84) y
  revisar el contrato aplicable de cada contribuyente.
- En relación laboral sin contrato individual escrito, el art. 84 atribuye los
  patrimoniales al empleado. Con contrato escrito pero sin pacto contrario, el
  punto de partida es división por partes iguales, no propiedad total patronal.
- La atribución en NOTICE/AUTHORS no es cortesía — es el reconocimiento del derecho moral de paternidad que persiste legalmente.

---

## Revisión outbound (si aplica)

[Del Paso 6]

---

## Enrutamiento de aprobación

[Del perfil de práctica — quién aprueba, qué dispara escalamiento automático]
```

## Postura de decisión

Cuando una licencia no puede clasificarse con confianza, señalarla como **"necesita revisión"** — no llamarla permisiva. Sub-clasificar el riesgo de licencia es una puerta de un solo sentido: una decisión de distribución hecha sobre una suposición de permisiva-por-defecto se convierte en una obligación de divulgación de código fuente o una medida cautelar meses después. Sobre-señalar es una puerta de dos sentidos — el abogado reduce la lista en revisión.

Del mismo modo, cuando el análisis de activación copyleft depende de una cuestión controvertida (el "interactúa sobre una red" de AGPL, el "conveying" de GPL-3.0, el alcance de linking de LGPL), señalar para revisión de abogado y exponer los factores que cortan en ambos sentidos.

## Verificaciones de calidad antes de entregar

- [ ] Se cargó el perfil de práctica y la política de OSS (si existe)
- [ ] Se estableció el modelo de despliegue antes de clasificar obligaciones
- [ ] Cada dependencia tiene una clasificación, incluyendo transitivas donde estén disponibles
- [ ] Paquetes con licencia desconocida están señalados, no defaulteados a permisiva
- [ ] Se leyó el texto de la licencia (no solo metadatos) para cualquier hallazgo copyleft o non-OSI
- [ ] Etiquetas de fuente aplicadas a citas; sin etiquetas `verify` eliminadas
- [ ] Aprobador nombrado según perfil de práctica
- [ ] Resultado marcado con el encabezado de confidencialidad
- [ ] Sección de derechos morales LFDA incluida en nota jurisdiccional
- [ ] Para revisión outbound: verificación de titularidad de derechos patrimoniales (obra por encargo) incluida

## Cerrar con el árbol de decisión de siguientes pasos

Terminar con el árbol de decisión de siguientes pasos según CLAUDE.md `## Resultados`. Personalizar las opciones a lo que este skill acaba de producir — las cinco ramas por defecto (redactar el X, escalar, obtener más información, observar y esperar, algo diferente) son un punto de partida, no una restricción. El árbol es el resultado; el abogado elige.

Si el escaneo encontró más de ~10 paquetes, o en cualquier momento que el usuario pregunte: ofrecer el dashboard (ver CLAUDE.md `## Resultados → Oferta de dashboard para resultados con muchos datos`). Dar forma a la oferta según lo que sea útil aquí — conteos por familia de licencia (permisiva / copyleft débil / copyleft fuerte / AGPL / propietaria / desconocida), distribución de riesgo, y una tabla de hallazgos con severidad y versión de paquete.
