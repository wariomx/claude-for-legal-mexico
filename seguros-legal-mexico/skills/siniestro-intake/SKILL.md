---
description: >
  Triaje de un siniestro nuevo o en curso: identifica la cobertura aplicable,
  calcula y marca los plazos fatales bajo la LCS (Art. 66 aviso de 5 días),
  clasifica la severidad, prepara la carta de aviso a la aseguradora y
  genera la lista de documentos requeridos. Primera acción cuando ocurre
  un siniestro.
argument-hint: "[descripción del siniestro o tipo de seguro afectado]"
---

# Skill: siniestro-intake (seguros-legal-mexico)

## Propósito

Las primeras 24-48 horas después de un siniestro son las más críticas. El Art. 66 LCS exige aviso a la aseguradora dentro de los 5 días hábiles siguientes al conocimiento del siniestro — un retraso sin justificación puede reducir o extinguir el derecho a la indemnización. Este skill actúa como primera respuesta: calcula la fecha límite de aviso, clasifica el siniestro, y prepara la notificación inicial.

## Marco legal crítico

| Norma | Contenido |
|---|---|
| **LCS Art. 66** | **Aviso de siniestro en 5 días hábiles desde el conocimiento** — incumplimiento justifica reducción proporcional o pérdida de cobertura si causó perjuicio a la aseguradora |
| LCS Art. 67 | Obligación del asegurado de aportar los documentos e información que justifiquen el siniestro |
| LCS Art. 68 | La aseguradora no puede rechazar el pago invocando el incumplimiento del asegurado si ella misma lo impidió |
| LCS Art. 72 | Pago de la indemnización — plazo a partir del dictamen de procedencia `[verify plazo CNSF vigente]` |
| **LCS Art. 81** | **Prescripción de 2 años (5 años para vida/muerte)** desde el hecho que da origen a la acción |
| LCS Art. 100 | Infraseguro — reducción proporcional de la indemnización |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer:
- Tipo de entidad (asegurado corporativo / asegurado individual / operador)
- Tipos de seguro activos
- Aseguradoras principales y datos de contacto

### Paso 1: captura de hechos del siniestro

Si el usuario no proporcionó los hechos, preguntar:

1. "¿Cuándo ocurrió el siniestro o cuándo tuviste conocimiento de él? (fecha exacta)"
2. "¿Qué tipo de seguro cubre este riesgo? (vida / GMM / daños / RC / auto / transporte / D&O / ciberseguridad / otro)"
3. "¿Cuál es la aseguradora y el número de póliza?"
4. "Describe brevemente qué pasó (3-5 oraciones)."
5. "¿Ya se dio aviso a la aseguradora? Si sí, ¿cuándo y cómo?"
6. "¿Hay lesionados, fallecidos o terceros afectados?"
7. "¿Hay algún proceso penal, civil o administrativo abierto relacionado?"

### Paso 2: calcular plazos fatales

**Este paso es obligatorio y va al inicio del output.**

Basado en la fecha de conocimiento del siniestro:

```
PLAZOS FATALES — CALCULAR ANTES DE CUALQUIER OTRA ACCIÓN

Fecha de conocimiento del siniestro: [AAAA-MM-DD]

1. AVISO A ASEGURADORA (Art. 66 LCS)
   Plazo: 5 días hábiles
   Fecha límite: [calcular — AAAA-MM-DD] [review: plazo fatal]
   Estado: [Pendiente / Cumplido el AAAA-MM-DD / VENCIDO]

2. PRESCRIPCIÓN DE LA ACCIÓN (Art. 81 LCS)
   Plazo: 2 años desde [fecha del hecho generador]
   (5 años si es seguro de vida / muerte)
   Fecha límite: [calcular — AAAA-MM-DD] [review: plazo fatal]

3. PRESENTACIÓN DE DOCUMENTOS A LA ASEGURADORA
   [verify plazo específico de la póliza]

ADVERTENCIA: si el aviso de Art. 66 LCS está próximo a vencer o ya venció,
esta es la primera acción a resolver.
```

### Paso 3: evaluar cobertura prima facie

Con base en los hechos descritos y la póliza disponible (o el perfil de práctica si no hay póliza):

- [ ] ¿El tipo de riesgo materializado está dentro del objeto del seguro?
- [ ] ¿El siniestro ocurrió durante la vigencia de la póliza?
- [ ] ¿Hay exclusiones visibles que pudieran aplicar? Listar con `[review]`
- [ ] ¿Hay preexistencias relevantes o declaraciones de salud que pudieran impactar? (GMM/vida)
- [ ] ¿El asegurado estaba al corriente en el pago de primas?

Clasificar cobertura prima facie: ✓ Aparentemente cubierto / ⚠️ Cobertura dudosa [review] / ✗ Aparentemente excluido / 🔍 Requiere más información

### Paso 4: clasificar severidad

| Severidad | Criterios |
|---|---|
| 🔴 Bloqueante | Aviso Art. 66 LCS vence en ≤ 24h, o siniestro con fallecidos o lesionados graves, o suma asegurada total comprometida |
| 🟠 Alto | Aviso Art. 66 LCS vence en ≤ 3 días, o cobertura dudosa por exclusión relevante, o terceros afectados |
| 🟡 Medio | Aviso dentro de plazo con tiempo suficiente, cobertura aparente, documentación incompleta |
| 🟢 Bajo | Siniestro rutinario, aviso en plazo, cobertura clara, monto bajo |

### Paso 5: preparar carta de aviso a la aseguradora

Si el aviso aún no se ha dado, preparar borrador:

```
[Ciudad], [fecha]

[Nombre de la aseguradora]
[Dirección / canal de notificación según póliza]

Póliza No.: [número]
Asegurado: [nombre]
Ramo: [tipo de seguro]

Estimados señores:

Por medio del presente, de conformidad con el artículo 66 de la Ley sobre el
Contrato de Seguro, hacemos del conocimiento de ustedes que el día [fecha]
ocurrió el siguiente siniestro: [descripción concisa de los hechos].

[Si hay terceros afectados: Hacemos constar que resultaron afectados:
[descripción].]

Queda formalmente abierto el presente aviso de siniestro bajo los términos
de la póliza referida. Quedamos a su disposición para proporcionar la
información y documentación adicional que requieran.

Atentamente,
[Nombre del asegurado / representante legal]
[Cargo]
[Datos de contacto]
```

**Enviar por el medio que deje constancia fehaciente de recepción** (correo electrónico con acuse, mensajería certificada, o el canal específico que indique la póliza). Guardar el acuse. `[review: plazo fatal]`

### Paso 6: lista de documentos para la reclamación

Según el ramo de seguro, proporcionar la lista de documentos que típicamente requiere la aseguradora:

**General (todos los ramos):**
- Póliza original o número de póliza
- Identificación oficial del asegurado
- Carta de aviso (este documento)
- Descripción detallada de los hechos (declaración escrita)

**Daños a bienes:**
- Acta de hechos / acta levantada ante autoridad (si aplica)
- Inventario de bienes dañados o perdidos
- Facturas o documentación que acredite el valor de los bienes
- Presupuestos de reparación o reposición
- Fotografías del siniestro y los daños

**Responsabilidad civil:**
- Acta de hechos / acta levantada ante autoridad
- Datos del tercero afectado
- Reclamación o demanda del tercero (si ya existe)
- Testimonio de testigos (si aplica)

**GMM / gastos médicos:**
- Expediente médico del evento
- Facturas hospitalarias y médicas
- Diagnóstico médico
- Recetas y comprobantes de medicamentos

**Vida / muerte:**
- Acta de defunción
- Certificado médico de causa de muerte
- Documentos de identidad del beneficiario
- Documentación de parentesco o beneficiario designado

**Auto:**
- Acta ante el Ministerio Público o autoridad de tránsito
- Fotos del vehículo
- Datos de terceros involucrados
- Licencia de conducir vigente

**D&O / RC profesional:**
- Reclamación o demanda recibida
- Actos o decisiones que originaron la reclamación
- Comunicaciones relevantes

`[review]` Verificar la lista específica de documentos en las condiciones generales y condiciones particulares de la póliza, ya que pueden variar.

### Paso 7: output final

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [póliza proporcionada ✓ | sin póliza — análisis sobre perfil de práctica]
- Leído: [descripción de hechos del siniestro]
- Marcado para tu criterio: [N elementos [review: plazo fatal]]
- Antes de confiar: verificar fecha exacta de conocimiento del siniestro para el cálculo del plazo Art. 66 LCS.

---

PLAZOS FATALES
[tabla del Paso 2]

COBERTURA PRIMA FACIE: [clasificación]
SEVERIDAD: [nivel con justificación]

BORRADOR DE AVISO A ASEGURADORA
[carta del Paso 5]

DOCUMENTOS A PREPARAR
[lista del Paso 6]

Una pregunta que haría y que no está en mi checklist: [observación]
```

> **¿Qué sigue?**
> 1. **Enviar el aviso ahora** — confirma que el borrador es correcto y envíalo; guarda el acuse.
> 2. **Análisis de cobertura** — `/seguros-legal-mexico:cobertura-analysis` con los hechos y la póliza para evaluar a fondo si la reclamación procede.
> 3. **Revisar la póliza** — `/seguros-legal-mexico:poliza-review` para identificar exclusiones y cláusulas relevantes antes de negociar con la aseguradora.
> 4. **Preparar queja CONDUSEF** — si la aseguradora ya negó o retardó injustificadamente, `/seguros-legal-mexico:recurso-condusef`.
> 5. **Escalar** — redacto nota para el Director Jurídico con los hechos, cobertura prima facie y fecha límite de aviso.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
