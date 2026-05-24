---
name: notificacion-infraccion
description: >
  Notificación de infracción de PI en línea — cuatro vías: notificación a ISP
  bajo LFDA Art. 231 bis (T-MEC), declaración administrativa ante IMPI,
  mecanismos de plataforma (Mercado Libre, Amazon, Meta), y denuncia penal
  UEIDDAPI. Usar cuando contenido infractor se encuentre en plataformas
  digitales, cuando se reciba una notificación de infracción, o cuando se
  necesite retirar contenido que infringe PI.
argument-hint: "<--enviar | --responder | --plataforma | --penal> [contexto o ruta al aviso recibido]"
---

# /notificacion-infraccion

**México NO tiene un régimen DMCA.** No existe equivalente directo al safe
harbor de 17 U.S.C. § 512 ni un sistema unificado de notice-and-takedown. La
reforma T-MEC de 2020 introdujo un mecanismo limitado de notificación a ISPs
(LFDA Art. 231 bis y ss.) `[model knowledge — verify]`, pero difiere
materialmente del DMCA en alcance, requisitos y consecuencias. Las demás vías
son procedimientos administrativos, mecanismos privados de plataforma, y la
vía penal.

Cuatro modos. Elegir uno:

- `/propiedad-intelectual-legal-mexico:notificacion-infraccion --enviar` —
  preparar una notificación bajo LFDA Art. 231 bis (ISP) o una solicitud de
  retiro ante plataforma.
- `/propiedad-intelectual-legal-mexico:notificacion-infraccion --responder` —
  triar una notificación que recibimos. Opciones: cumplir / contra-notificar /
  negociar / ignorar.
- `/propiedad-intelectual-legal-mexico:notificacion-infraccion --plataforma` —
  preparar una queja ante mecanismo específico de plataforma (Mercado Libre,
  Amazon, Meta, etc.).
- `/propiedad-intelectual-legal-mexico:notificacion-infraccion --penal` —
  preparar elementos para denuncia ante UEIDDAPI (solo para piratería a escala
  comercial o falsificación sistemática).

## Instrucciones

1. **Leer el perfil de práctica.** Cargar
   `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`.
   Si contiene marcadores `[PLACEHOLDER]` o no existe, detenerse y decir: "Este
   plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   `/propiedad-intelectual-legal-mexico:cold-start-interview` — el skill de
   notificación de infracción depende de tu matriz de aprobación y perfil de
   práctica."

2. **Revisar contexto del asunto.** Per `## Espacios de trabajo por asunto`: si
   `Habilitado` es `✗`, omitir. Si está habilitado y no hay asunto activo,
   preguntar: "¿Para qué asunto es esto? Ejecuta
   `/propiedad-intelectual-legal-mexico:matter-workspace switch <slug>` o di
   `nivel-de-práctica`."

3. **Despachar según `$ARGUMENTS`:**
   - `--enviar` → ejecutar modo envío (abajo).
   - `--responder` → ejecutar modo respuesta (abajo).
   - `--plataforma` → ejecutar modo plataforma (abajo).
   - `--penal` → ejecutar modo penal (abajo).
   - Sin flag → preguntar una vez: "¿Estamos enviando una notificación de
     infracción, triando una que recibimos, presentando queja ante una
     plataforma, o preparando una denuncia penal?"

4. **Respetar las puertas.** En `--enviar` y `--penal`, la puerta de
   confirmación se ejecuta antes de que cualquier resultado final se escriba.

5. **Nota jurisdiccional.** Este skill aplica derecho mexicano. Si el ISP, el
   contenido o el infractor se encuentran fuera de jurisdicción mexicana,
   señalar antes de proceder — puede ser necesario un aviso bajo el régimen
   del país donde está el ISP (EU DSA, DMCA 512, UK OSA) además de o en lugar
   del procedimiento mexicano.

6. **Transferir donde corresponda.** `--responder` con recomendación de
   contra-notificación encadena con el proceso de contra-aviso — pero solo
   después de que el memorándum de triaje haya sido revisado y la decisión de
   contra-notificar se haya tomado deliberadamente.

## Ejemplos

```
/propiedad-intelectual-legal-mexico:notificacion-infraccion --enviar
/propiedad-intelectual-legal-mexico:notificacion-infraccion --responder ~/Descargas/notificacion-recibida.pdf
/propiedad-intelectual-legal-mexico:notificacion-infraccion --plataforma
/propiedad-intelectual-legal-mexico:notificacion-infraccion --penal
/propiedad-intelectual-legal-mexico:notificacion-infraccion
```

## Notas

- La notificación saliente y la contra-notificación NO llevan el encabezado
  de confidencialidad. Los borradores internos, análisis de excepciones y
  memorándums de triaje SÍ lo llevan.
- Los entregables orientados al exterior no son privilegiados — son
  declaraciones en un proceso administrativo o privado.
- Usuarios no-abogados reciben un breve para la conversación con el abogado
  antes de que la puerta se abra — particularmente importante para el modo
  penal.

---

## Propósito

La protección de PI en línea en México opera a través de múltiples vías, cada
una con diferentes requisitos, alcances y consecuencias. No existe un sistema
unificado como el DMCA. Este skill maneja las cuatro vías disponibles con las
salvaguardas que cada una amerita.

> **Entregables externos (modos enviar y plataforma):** la notificación
> saliente va al ISP, a la plataforma, o a la autoridad. NO incluir el
> encabezado `CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO` en el documento
> saliente. Los borradores internos, análisis de excepciones/limitaciones, y
> memorándums de triaje conservan el encabezado per configuración del plugin
> `## Resultados`.

---

## Cargar contexto

- `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md`
  → `## Perfil de práctica de PI` (registros de derechos de autor si existen),
  `## Postura de enforcement` → matriz de aprobación, `## Resultados`
  (encabezado de confidencialidad, rol), `## Quién usa este plugin` (rol —
  abogado vs. no-abogado)
- **Contexto del asunto.** Escribir resultados en la carpeta del asunto activo
  en
  `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/matters/<asunto-slug>/notificacion/<slug>/`
  (o `notificacion/<slug>/` a nivel de práctica). Nunca leer archivos de otro
  asunto a menos que `Contexto cruzado entre asuntos` esté `on`.

---

## VÍA 1: Notificación a ISP — LFDA Art. 231 bis (Reforma T-MEC)

### Contexto legal

La reforma a la LFDA de 2020, derivada del T-MEC (Capítulo 20, Arts. 20.88-
20.89) `[model knowledge — verify]`, introdujo un mecanismo de notificación a
proveedores de servicios de internet (ISPs) para infracciones de derechos de
autor en el entorno digital. Este mecanismo:

- **NO es un DMCA mexicano** — es materialmente más limitado
- **NO crea un safe harbor automático** para los ISPs como el § 512 DMCA
  `[model knowledge — verify]`
- Establece un procedimiento de notificación y contra-notificación
- Se limita a **derechos de autor** — no cubre propiedad industrial (marcas,
  patentes, secretos industriales). Para esos, usar la vía IMPI o plataforma.
- El marco regulatorio secundario puede haber sido emitido o estar pendiente
  `[model knowledge — verify]`

### Modo enviar (`--enviar`) — Notificación al ISP

#### Paso 1: Identificar la obra protegida

> ¿Cuál es la obra protegida?
>
> - **Título / descripción** — ¿qué es la obra (software, imagen, texto,
>   video, audio, música)?
> - **Estatus de registro ante INDAUTOR** — número de registro y fecha (si
>   existe). El registro NO es requisito para actuar en México, pero es
>   prueba útil de titularidad.
> - **Titularidad** — ¿somos el autor, el titular de derechos patrimoniales
>   por transmisión (LFDA Arts. 30-33), o el comitente en obra por encargo
>   (LFDA Arts. 83-84)?
> - **Licencias previas** — ¿hemos licenciado este uso, o un uso más amplio
>   que pudiera cubrirlo?

#### Paso 2: Identificar el material infractor y su ubicación

> ¿Dónde está el material infractor?
>
> - **Plataforma / ISP** — YouTube, Facebook/Instagram/Meta, TikTok, un web
>   host, un ISP mexicano, etc.
> - **URL(s)** — enlaces permanentes específicos al material infractor.
> - **Descripción** — ¿qué es el material infractor y cómo infringe
>   (copia verbatim, sustancialmente similar, derivado)?
> - **Capturas de pantalla / evidencia** — preservadas con fecha, hora y
>   URL visible. Considerar acta de fe de hechos ante notario público
>   `[model knowledge — verify]` para preservar evidencia con valor
>   probatorio reforzado.

#### Paso 3: Análisis de excepciones y limitaciones

A diferencia del fair use de EE.UU. (test de 4 factores abierto), México tiene
excepciones y limitaciones TAXATIVAS (LFDA Arts. 147-151)
`[model knowledge — verify]`:

> Antes de preparar la notificación, revisar si alguna excepción o limitación
> aplica al uso:
>
> 1. ¿Es cita con fines de crítica, comentario, investigación o enseñanza?
> 2. ¿Es reproducción por una sola vez para uso personal y privado?
> 3. ¿Es reproducción de artículos sobre temas de actualidad?
> 4. ¿Cae en alguna otra excepción de LFDA Arts. 147-151?
>
> Si alguna excepción claramente aplica, **no preparar la notificación**.
> Detener y enrutar a revisión de abogado: "Una excepción de la LFDA parece
> aplicable a este uso. Enviar una notificación de infracción sobre un uso
> lícito genera exposición por notificación temeraria y daño a la reputación."
>
> Si la aplicación es debatible, señalar: "La excepción de [Art. X] podría
> aplicar. El análisis requiere criterio de abogado antes de proceder."
> `[review]`

#### Paso 4: Creencia de buena fe

Confirmar que el notificante:

- Ha confirmado que la obra es suya (o tiene legitimación para actuar)
- Ha confirmado que el uso no está autorizado (no hay licencia previa, no hay
  transmisión de derechos, no hay consentimiento)
- Ha revisado excepciones y limitaciones (Paso 3)
- Ha revisado directamente el contenido acusado (no solo un reporte sobre él)

#### Paso 5: Preparar la notificación

Elementos de la notificación bajo LFDA Art. 231 bis `[model knowledge — verify]`:

1. **Identificación del notificante** — nombre, domicilio, datos de contacto,
   carácter con que actúa (titular, representante legal, apoderado)
2. **Identificación de la obra protegida** — título, descripción, registro
   INDAUTOR si existe
3. **Identificación del material infractor** — URLs, descripción de la
   infracción
4. **Declaración de titularidad o legitimación** — fundamento de la
   titularidad sobre los derechos
5. **Declaración de buena fe** — declaración bajo protesta de decir verdad
   de que el uso no está autorizado
6. **Firma** del titular o representante legal

> **⚠️ Bajo protesta de decir verdad.** La declaración de buena fe en la
> notificación es una declaración bajo protesta de decir verdad. Una
> declaración falsa puede generar responsabilidad civil y, en su caso,
> penal (falsa declaración). `[model knowledge — verify]`

#### Paso 6: Puerta de confirmación antes del envío

```
┌──────────────────────────────────────────────────────────────┐
│  ANTES DE QUE ESTA NOTIFICACIÓN SE ENVÍE                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Una notificación de infracción bajo LFDA Art. 231 bis       │
│  contiene una declaración bajo protesta de decir verdad.     │
│  Enviarla no es un trámite administrativo rutinario — es     │
│  una declaración con consecuencias jurídicas.                │
│                                                              │
│  • Una notificación sobre uso lícito (excepciones de LFDA    │
│    Arts. 147-151) genera exposición por notificación         │
│    temeraria y potencial responsabilidad civil.              │
│                                                              │
│  • La declaración de titularidad debe ser verificable.       │
│    Reclamar derechos sobre una obra ajena es temerario.      │
│                                                              │
│  Confirmar antes de que la notificación salga:               │
│                                                              │
│    1. Eres titular de los derechos de autor, o tienes        │
│       legitimación para actuar (transmisión de derechos      │
│       patrimoniales o poder legal).                          │
│    2. El uso no está autorizado — verificaste licencias,     │
│       transmisiones y consentimientos previos.               │
│    3. Revisaste excepciones y limitaciones (Paso 3);         │
│       tu conclusión está en el registro.                     │
│    4. Quien tiene autoridad para firmar aprueba el envío.    │
│                                                              │
│  Aprobador per perfil de práctica: [aprobador de la          │
│  matriz de enforcement]                                      │
│                                                              │
│  Escalamientos automáticos que aplican: [listar los del      │
│  perfil de práctica que este asunto dispara]                 │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Si el usuario es no-abogado (per `## Quién usa este plugin`), agregar:

> Una notificación de infracción contiene una declaración bajo protesta de
> decir verdad. ¿Lo has revisado con un abogado? Si no, aquí hay un breve
> para llevar a la consulta: [generar resumen corto: obra, titularidad, uso
> acusado, análisis de excepciones, firmante, ISP/plataforma]. Un par de
> horas de abogado ahora es materialmente más barato que una responsabilidad
> por notificación temeraria.
>
> Si necesitas encontrar un abogado: Colegio de Abogados de tu localidad,
> AMPPI (Asociación Mexicana para la Protección de la Propiedad Intelectual),
> ANADE (Asociación Nacional de Abogados de Empresa).

No escribir el resultado final sin interacción explícita con la puerta.

#### Paso 7: Resultado

**Primario:** `<carpeta-asunto>/notificacion/<slug>/notificacion-v<N>.md` — el
contenido de la notificación, listo para enviar al ISP.

**En chat:** mostrar la notificación como texto plano para revisión antes de
escribir. Iterar antes de comprometer a disco.

**Nota de cierre para el revisor** (solo en la previsualización en chat):

> Este es un borrador de notificación para revisión del abogado, no una
> notificación lista para enviar. Un abogado titulado revisa, edita y asume
> responsabilidad profesional antes del envío.

### Contra-notificación bajo LFDA Art. 231 bis

Si hemos recibido una notificación y nuestro contenido fue retirado, el
proceso de contra-notificación `[model knowledge — verify]`:

- Confirmar que el retiro fue por notificación bajo LFDA Art. 231 bis (no
  por acción directa de la plataforma por TOS)
- Creencia de buena fe de que el material fue retirado por error o
  identificación equivocada
- Elementos de la contra-notificación: identificación, material retirado,
  declaración bajo protesta de decir verdad, firma
- **Consecuencias:** El ISP debe restaurar el contenido dentro del plazo
  legal, a menos que el notificante original inicie un procedimiento
  `[model knowledge — verify]`

---

## VÍA 2: Declaración administrativa ante IMPI

### Cuándo usar esta vía

Para infracción de **propiedad industrial** en plataformas digitales:
- Uso no autorizado de marca registrada
- Venta de productos falsificados
- Imitación de imagen comercial (trade dress)
- Uso de denominación de origen o indicación geográfica sin autorización

La LFDA Art. 231 bis solo cubre derechos de autor. Para marcas, patentes y
otros derechos de propiedad industrial, la vía es IMPI.

### Procedimiento

1. **Solicitud de declaración administrativa de infracción** ante IMPI
   (LFPPI Arts. 334-348) `[model knowledge — verify]`
2. **Medidas provisionales** — IMPI puede ordenar:
   - Suspensión de la comercialización
   - Retiro de productos del mercado
   - Aseguramiento de mercancía infractora
   - Bloqueo de acceso a contenido infractor en línea
     `[model knowledge — verify]`
3. **Inspección** — IMPI puede realizar visitas de inspección, incluyendo
   inspección de establecimientos virtuales `[model knowledge — verify]`
4. **Resolución** — IMPI declara si existe o no infracción y, en su caso,
   impone sanciones

### Elementos de la solicitud

- Identificación del solicitante y acreditación de legitimación
- Registro(s) de marca, patente u otro derecho ante IMPI
- Descripción de los actos de infracción
- Pruebas (capturas de pantalla con acta de fe de hechos ante notario,
  compras de control, printouts certificados)
- Solicitud específica (suspensión, retiro, multa, clausura)

### Ventaja sobre la vía ISP

- Aplica a propiedad industrial (marcas, patentes), no solo derechos de autor
- IMPI tiene facultades de investigación y sanción
- Puede ordenar medidas provisionales con efectos reales
- No depende de la voluntad del ISP o la plataforma

---

## VÍA 3: Mecanismos de plataforma (`--plataforma`)

### Contexto

Las principales plataformas de comercio electrónico y redes sociales que operan
en México tienen sus propios mecanismos de protección de PI. Estos son remedios
de **derecho privado** basados en los términos de servicio de la plataforma —
no son procedimientos legales y sus decisiones no tienen fuerza de cosa juzgada.

### Principales plataformas y sus mecanismos

#### Mercado Libre — Brand Protection Program

- **URL de reporte:** Portal de Brand Protection de Mercado Libre
- **Requisitos:** Registro de marca, prueba de titularidad, identificación de
  las publicaciones infractoras
- **Tipos de infracción cubiertos:** Productos falsificados, uso no autorizado
  de marca, violación de derechos de autor
- **Plazo de respuesta:** Generalmente 48-72 horas para primera revisión
  `[model knowledge — verify]`
- **Proceso de apelación:** El vendedor puede apelar el retiro

#### Amazon México — Brand Registry / Report Infringement

- **URL de reporte:** Amazon Brand Registry (requiere marca registrada ante
  IMPI)
- **Requisitos:** Registro de marca ante IMPI, enrollment en Brand Registry,
  identificación de los ASINs infractores
- **Tipos de infracción cubiertos:** Falsificación, infracción de marca,
  violación de derechos de autor, violación de patente
- **Proceso:** Report a Violation tool dentro de Brand Registry
- **Nota:** Amazon puede requerir test purchases o declaración bajo protesta

#### Meta (Facebook / Instagram) — IP Reporting

- **URL de reporte:** Formulario de reporte de PI de Meta
  (facebook.com/help/intellectual_property)
- **Requisitos:** Identificación del titular, descripción de los derechos,
  identificación del contenido infractor
- **Tipos de infracción cubiertos:** Marca, derechos de autor, falsificación
- **Nota:** Para Marketplace (comercio electrónico), el proceso es similar al
  de las publicaciones pero con opciones adicionales de reporte de
  falsificación

#### Google / YouTube

- **URL de reporte:** YouTube Copyright Complaint (para DA);
  Trademark Complaint Form (para marcas)
- **Nota:** YouTube tiene un proceso de contra-notificación similar al DMCA
  por sus TOS, independientemente de que opere en México

#### TikTok

- **URL de reporte:** Formulario de reporte de PI de TikTok
- **Tipos de infracción cubiertos:** Marca, derechos de autor

### Flujo de trabajo para modo plataforma

1. **Identificar la plataforma** — ¿dónde está el contenido infractor?
2. **Identificar el tipo de derecho** — marca, derecho de autor, patente,
   imagen comercial
3. **Verificar requisitos de la plataforma** — ¿requiere registro de marca
   (Amazon Brand Registry, Mercado Libre BPP)? ¿Requiere prueba de compra?
4. **Preparar la documentación:**
   - Certificado de registro ante IMPI o INDAUTOR
   - Capturas de pantalla del contenido infractor con fecha y URL
   - Poder legal o carta de autorización si actúa un representante
   - Descripción clara de la infracción
5. **Completar el formulario** — el skill prepara el contenido; el usuario
   lo envía a través del portal de la plataforma.

### Limitaciones de la vía de plataforma

- Las decisiones son de la plataforma, no de autoridad; no tienen fuerza
  legal vinculante
- Cada plataforma tiene sus propias reglas y umbrales
- El vendedor/infractor puede apelar y la plataforma puede restaurar el
  contenido
- No sustituye la vía legal (IMPI, civil, penal) para protección definitiva
- **Complementaria, no sustitutiva** — usar como primera línea de defensa
  rápida mientras se evalúa la vía legal apropiada

---

## VÍA 4: Denuncia penal — UEIDDAPI (`--penal`)

### ⚠️ PUERTA SEVERA — SOLO PARA CONDUCTAS GRAVES

> **La denuncia penal es la opción más severa del sistema.** Este modo solo
> debe usarse cuando los hechos evidencien:
>
> - **Piratería a escala comercial** — reproducción y distribución masiva de
>   obras protegidas con fin de lucro (CPF Art. 424 bis)
>   `[model knowledge — verify]`
> - **Falsificación sistemática de marcas** — producción y comercialización
>   de productos con marcas falsificadas (LFPPI Art. 402)
>   `[model knowledge — verify]`
> - **Revelación dolosa de secretos industriales** — con ánimo de causar daño
>   o beneficio propio (LFPPI Art. 402 fracción IV)
>   `[model knowledge — verify]`
> - **Reincidencia** — el infractor ya fue sancionado administrativamente y
>   continúa la conducta
>
> Para disputas comerciales ordinarias, la vía administrativa (IMPI) o civil
> es la apropiada. La vía penal es desproporcionada para infractores
> ocasionales o de bajo impacto.

### Procedimiento

1. **Denuncia o querella ante el MP Federal (UEIDDAPI)**
   - UEIDDAPI: Unidad Especializada en Investigación de Delitos contra los
     Derechos de Autor y la Propiedad Industrial, de la Fiscalía General de
     la República
   - Para PI industrial: generalmente se requiere resolución administrativa
     previa de IMPI declarando la infracción `[model knowledge — verify]`
   - Para derechos de autor: la querella puede presentarse directamente

2. **Tipos penales principales:**
   - **CPF Arts. 424-429** — delitos contra los derechos de autor
     `[model knowledge — verify]`:
     - Art. 424: producción, reproducción, almacenamiento, transporte,
       distribución o venta de obras protegidas sin autorización
     - Art. 424 bis: reproducción con fin de especulación comercial
     - Art. 424 ter: fabricación con fin de lucro de dispositivos para
       descifrar señales encriptadas
   - **LFPPI Art. 402** — delitos en materia de propiedad industrial
     `[model knowledge — verify]`:
     - Falsificación de marcas
     - Producción o comercialización de productos con marcas falsificadas
     - Revelación de secretos industriales
     - Uso de denominación de origen sin autorización

3. **Sanciones:** Pena privativa de libertad (2-10 años según el tipo penal)
   + multa + reparación del daño `[model knowledge — verify]`

4. **Documentación necesaria:**
   - Registro de los derechos (certificado IMPI o INDAUTOR)
   - Evidencia de la conducta infractora (acta de fe de hechos ante notario,
     compras de control, peritajes)
   - Cuantificación del daño o perjuicio
   - Resolución administrativa previa de IMPI (si aplica)
   - Identificación del probable responsable (si se conoce)

### Puerta de confirmación para modo penal

```
┌──────────────────────────────────────────────────────────────┐
│  ANTES DE PREPARAR ESTA DENUNCIA PENAL                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Una denuncia penal ante UEIDDAPI inicia un procedimiento    │
│  penal con todas sus consecuencias. No es una herramienta    │
│  de presión comercial — es el sistema de justicia penal.     │
│                                                              │
│  • Una denuncia temeraria o infundada puede generar          │
│    responsabilidad por denuncia calumniosa (CPF Art. 356).   │
│                                                              │
│  • El procedimiento penal es público y puede afectar la      │
│    reputación de ambas partes.                               │
│                                                              │
│  • La denuncia penal no es la vía ordinaria para disputas    │
│    comerciales — la vía administrativa (IMPI) o civil es     │
│    la primera opción en la mayoría de los casos.             │
│                                                              │
│  Confirmar antes de preparar la denuncia:                    │
│                                                              │
│    1. Los hechos evidencian dolo o escala comercial           │
│       significativa — no es una disputa comercial ordinaria.  │
│    2. Se cuenta con resolución administrativa previa de      │
│       IMPI (si se requiere para el tipo penal).              │
│    3. La evidencia está preservada con valor probatorio      │
│       (acta de fe de hechos ante notario, compras de         │
│       control, peritajes).                                   │
│    4. El abogado penalista ha sido consultado o se           │
│       consultará antes del ejercicio de la acción penal.     │
│    5. La decisión ha sido aprobada al nivel correspondiente  │
│       de la cadena de aprobación.                            │
│                                                              │
│  Aprobador per perfil de práctica: [aprobador —              │
│  generalmente Director Jurídico o superior para acciones     │
│  penales]                                                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Si el usuario es no-abogado:

> Una denuncia penal inicia un procedimiento ante el sistema de justicia
> penal. ¿Lo has revisado con un abogado penalista? Este paso REQUIERE
> asesoría profesional — no es algo que deba hacerse sin representación
> legal. Breve para la consulta: [generar resumen]. Referencia: AMPPI, BMA,
> Colegio de Abogados, despachos penalistas especializados en PI.

---

## Modo responder (`--responder`) — Triaje de notificación recibida

Tu contenido fue retirado o recibiste una notificación de infracción.

### Paso 1: Leer la notificación recibida

Extraer:

- **Remitente** — entidad, firmante, domicilio, correo
- **Vía utilizada** — notificación ISP (LFDA Art. 231 bis), resolución IMPI,
  mecanismo de plataforma, o carta de requerimiento directa
- **ISP/plataforma** — quién te notificó
- **Obra/derecho reclamado** — qué dicen que es suyo
- **Tu contenido acusado de infringir** — URL(s) o identificadores
- **Fecha de notificación / retiro**
- **Si la notificación cumple los requisitos formales** — señalar elementos
  faltantes; una notificación defectuosa debilita la posición del notificante

### Paso 2: Evaluar

- **¿Tenemos licencia?** Negociada, implícita, previa transmisión, relación
  laboral o de obra por encargo.
- **¿Aplica alguna excepción o limitación?** LFDA Arts. 147-151. Evaluar
  honestamente — es para nosotros, no para la respuesta.
- **¿La notificación es defectuosa?** ¿Falta algún elemento requerido?
  ¿Firmada por alguien sin legitimación aparente?
- **¿El ISP/plataforma cumplió correctamente con el procedimiento?** ¿Nos
  dieron aviso y oportunidad de responder?
- **¿El notificante es reincidente?** ¿Patrón de notificaciones abusivas en
  esta plataforma?

### Paso 3: Opciones

Presentar 4 opciones con ventajas/desventajas:

**A — Cumplir (dejar que el retiro se mantenga)**
- Cuándo: tienen razón, o la pelea no vale la pena
- Desventaja: contenido permanece abajo; puede afectar SEO, cuentas con
  políticas de strikes, ingresos
- Siguiente paso: registrar el evento, confirmar plazos, seguir adelante

**B — Contra-notificar**
- Cuándo: creencia de buena fe de que el material fue identificado
  erróneamente o retirado por error — frecuentemente cuando el uso está
  licenciado, cae en una excepción, o el notificante no es titular
- Desventaja: según la vía, el notificante puede iniciar un procedimiento
  formal
- Siguiente paso: preparar contra-notificación per LFDA Art. 231 bis (si
  la notificación fue por esa vía) o apelación ante la plataforma

**C — Negociar directamente con el notificante**
- Cuándo: hay espacio para resolución comercial (licencia, crédito, retiro
  de una porción menor)
- Desventaja: el contenido sigue abajo durante la conversación
- Siguiente paso: carta de contacto al notificante; no enviar
  contra-notificación mientras haya negociaciones activas

**D — Ignorar y dejar que se mantenga; actuar por otra vía**
- Cuándo: el daño es pequeño, no queremos entrar en un proceso, y
  preferimos tratar con el notificante por separado
- Desventaja: contenido permanece abajo; si la notificación fue temeraria,
  podemos tener acción contra el notificante pero eso es otra pelea

Recomendar una con dos oraciones de fundamento.

### Paso 4: Escribir memorándum de triaje

Resultado: `<carpeta-asunto>/notificacion/entrante/<slug>/triaje.md`.

```markdown
[ENCABEZADO DE CONFIDENCIALIDAD — per plugin config ## Resultados]

> **Herencia de confidencialidad.** Este triaje registra nuestra primera
> evaluación de una notificación adversa. Es material de análisis jurídico
> interno. No reenviar fuera del círculo de confidencialidad ni adjuntar a
> contra-notificaciones sin depurar.

# Notificación de Infracción Recibida — Triaje

> **LECTURA DE TRIAJE, NO OPINIÓN.** Análisis estructurado de la notificación,
> no opinión jurídica de fondo. Cada autoridad señalada para verificación por
> especialista; cada decisión de mérito corresponde al abogado.

**Slug:** [slug]
**Recibida:** [AAAA-MM-DD]
**Plataforma/ISP:** [plataforma]
**Archivo de entrada:** [ruta]

## La notificación

**Remitente:** [entidad, firmante, abogado si existe]
**Obra/derecho reclamado:** [título, descripción, registro si proporcionado]
**Nuestro contenido acusado:** [URLs / identificadores]
**Fecha de retiro:** [AAAA-MM-DD]
**Vía utilizada:** [LFDA Art. 231 bis / IMPI / plataforma / carta directa]
**Notificación cumple requisitos formales:** [sí / no — listar elementos
faltantes]

## Evaluación

**Verificación de licencia/autorización:** [lectura]
**Análisis de excepciones y limitaciones (LFDA Arts. 147-151):** [lectura —
cada excepción + conclusión; `[SME VERIFY]`]
**Defectos de la notificación:** [lista o ninguno]
**Cumplimiento del ISP/plataforma con el procedimiento:** [nos dieron aviso y
oportunidad]
**Credibilidad del notificante:** [legítimo / reincidente / patrón abusivo]

## Opciones

### A. Cumplir
### B. Contra-notificar
### C. Negociar con el notificante
### D. Ignorar

**Recomendación:** [A/B/C/D] — [dos oraciones por qué] — `[SME VERIFY:
abogado debe confirmar antes de ejecutar]`

## Plazos

- **Ventana de contra-notificación:** [según la vía y la plataforma]
- **Plazos contractuales con la plataforma:** [revisar]

## Acciones inmediatas

- [ ] Preservación de evidencia emitida — [sí/no]
- [ ] Impacto de negocio evaluado (ingresos, strikes, SEO) — [sí/no]
- [ ] Asunto creado en registro — [sí/no/pendiente]
- [ ] Abogado asignado — [quién]
```

Cerrar la presentación en chat con:

> Este es un memorándum de triaje, no asesoría. Las evaluaciones arriba son
> una primera lectura de las cuatro esquinas de la notificación. Un abogado
> evalúa antes de contra-notificar o decidir no responder.

---

## Postura de decisión

Per `## Postura de decisión en juicios jurídicos subjetivos` en el perfil de
práctica: cuando haya incertidumbre sobre si aplica una excepción, si somos
titulares, si los derechos son nuestros, si una excepción derrota la
reclamación del lado receptor — no decidir silenciosamente. Las excepciones
y limitaciones de la LFDA son el caso paradigmático de decisión incierta.
Señalar para revisión del abogado; exponer los factores. Enviar una
notificación o una contra-notificación basándose en un supuesto es una
puerta de un solo sentido.

## Lo que este skill NO hace

- **Enviar la notificación.** Solo redacción. El usuario envía a través del
  canal designado del ISP o plataforma.
- **Elegir el portal de la plataforma por el usuario.** Anota cuál vía se
  espera; no auto-envía.
- **Decidir excepciones y limitaciones.** Recorre la lista taxativa; señala.
  Un abogado decide si proceder.
- **Validar la reclamación del remitente en el lado receptor.** Lectura
  estructurada; cada autoridad señalada para verificación por especialista.
- **Saltarse la puerta.** La puerta se ejecuta cada vez en modos `--enviar`
  y `--penal`.
- **Inventar citas.** Cualquier cita incluida se etiqueta por fuente y se
  señala para verificación; sin suplemento silencioso.
- **Manejar regímenes de otros países.** LFDA/LFPPI son derecho mexicano.
  Para EU DSA, DMCA 512, UK OSA, y otros regímenes — señalar y derivar.

---

## Cierre con el árbol de decisión de siguientes pasos

Cerrar con el árbol de decisión per CLAUDE.md `## Resultados`. Personalizar
las opciones a lo que este skill produjo. El árbol es el resultado; el
abogado elige.
