---
description: >
  Gestiona el proceso de queja, conciliación y arbitraje ante la CONDUSEF
  por disputas entre asegurados y aseguradoras. Prepara la queja formal,
  la posición de conciliación, la solicitud de arbitraje y los escritos
  de defensa. Aplica la Ley de Protección y Defensa al Usuario de Servicios
  Financieros (LPDUSF) y las reglas de procedimiento CONDUSEF.
argument-hint: "[descripción de la disputa con la aseguradora o acto reclamado]"
---

# Skill: recurso-condusef (seguros-legal-mexico)

## Propósito

Cuando una aseguradora niega, reduce o retarda injustificadamente el pago de un siniestro, o cuando las condiciones contractuales son abusivas, CONDUSEF ofrece un mecanismo gratuito, rápido y accesible para el asegurado. La conciliación CONDUSEF resuelve muchos conflictos de seguros sin necesidad de litigio. Este skill prepara al usuario para todo el proceso: desde la queja inicial hasta el arbitraje.

## Marco legal

| Norma | Relevancia |
|---|---|
| LPDUSF Arts. 1-94 | Marco del proceso de queja, conciliación y arbitraje CONDUSEF |
| LPDUSF Arts. 50-63 | Procedimiento de conciliación y arbitraje |
| LCS Arts. 67-81 | Base de la reclamación al asegurado: obligaciones de la aseguradora |
| LISF Arts. 440-458 | Obligaciones de las aseguradoras frente a los asegurados |
| Reglamento de la LPDUSF | Detalle procedimental `[model knowledge — verify versión vigente]` |
| Reglas de operación CONDUSEF vigentes | Plazos y requisitos actualizados `[verify en condusef.gob.mx]` |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Si está activo el módulo Asegurado-Individual o Asegurado-Corporativo, extraer:
- Aseguradoras con las que opera
- Número(s) de póliza
- Estado de queja CONDUSEF

### Paso 1: captura de hechos de la disputa

Si el usuario no los proporcionó, preguntar:

1. "¿Cuál es el tipo de seguro involucrado? (vida / GMM / auto / daños / RC / otro)"
2. "¿Cuál es la aseguradora y el número de póliza?"
3. "¿Qué acto o conducta de la aseguradora quieres reclamar? (negativa de pago / reducción de indemnización / retardo en el pago / condiciones abusivas / otro)"
4. "¿Cuándo ocurrió el siniestro y cuándo recibiste la negativa o el acto reclamado?"
5. "¿Tienes documentos de soporte? (póliza, carta de negativa, expediente del siniestro, recibos de prima)"
6. "¿Ya presentaste una reclamación directa ante la aseguradora? ¿Cuál fue la respuesta?"
7. "¿Ya tienes una queja ante CONDUSEF en proceso? Si sí, en qué etapa."

### Paso 2: evaluar la viabilidad de la queja CONDUSEF

Verificar:

- [ ] **Plazo de prescripción.** ¿La acción ha prescrito? (LCS Art. 81: 2 años desde el hecho generador; 5 años para vida/muerte). Si está próximo a vencer: `[review: plazo fatal — verificar y actuar de inmediato]`
- [ ] **Competencia CONDUSEF.** CONDUSEF tiene competencia sobre disputas entre usuarios de servicios financieros y entidades supervisadas. Las aseguradoras autorizadas en México están bajo su competencia.
- [ ] **Monto de la disputa.** Para arbitraje CONDUSEF, hay montos máximos que varían por ramo. `[verify topes actuales CONDUSEF por ramo]`
- [ ] **Agotamiento de vía directa.** ¿Se presentó la reclamación directamente ante la UNE de la aseguradora? CONDUSEF puede recibir la queja aunque no se haya agotado la vía directa, pero conviene tenerlo documentado.

### Paso 3: preparar la queja formal ante CONDUSEF

La queja puede presentarse en línea en condusef.gob.mx o en ventanilla. Preparar el escrito:

```
QUEJA ANTE LA COMISIÓN NACIONAL PARA LA PROTECCIÓN Y DEFENSA DE LOS USUARIOS
DE SERVICIOS FINANCIEROS (CONDUSEF)

Lugar y fecha: [ciudad], [fecha]

QUEJOSO: [nombre completo del asegurado/tomador/beneficiario]
Domicilio: [domicilio para oír notificaciones]
Correo electrónico: [para notificaciones electrónicas]

INSTITUCIÓN FINANCIERA RECLAMADA: [nombre de la aseguradora]
Número de autorización CNSF: [número, si conocido]

NÚMERO DE PÓLIZA: [número]
TIPO DE SEGURO: [ramo]
FECHA DEL SINIESTRO: [fecha]

HECHOS:

1. [Hecho 1: descripción clara y cronológica]
2. [Hecho 2]
3. [...]

ACTO RECLAMADO:

[Describir con precisión la conducta de la aseguradora que se reclama:
negativa de pago / reducción de indemnización / retardo en el pago / etc.
Incluir fecha y número del oficio o carta de rechazo si existe.]

FUNDAMENTO DE LA RECLAMACIÓN:

La aseguradora está obligada a [pagar la indemnización / cumplir la cobertura / 
respetar las condiciones de la póliza] conforme a:
- LCS Art. [artículo aplicable]
- Condiciones generales de la póliza, cláusula [cláusula aplicable]
[Citar el texto de la póliza que fundamenta la cobertura reclamada]

PRETENSIÓN:

Solicito a CONDUSEF que:
1. Cite a [nombre de la aseguradora] a una audiencia de conciliación.
2. En caso de no resolverse en conciliación, someta la disputa a arbitraje.
3. [Cualquier medida adicional]

DOCUMENTOS QUE SE ACOMPAÑAN:

1. Copia de la póliza (carátula y condiciones generales)
2. Copia de la carta de negativa / comunicación de la aseguradora
3. Comprobantes de pago de prima (últimos [N] recibos)
4. [Documentación del siniestro: acta, expediente médico, etc.]
5. Identificación oficial del quejoso

Atentamente,
[Nombre y firma del quejoso o representante legal]
[RFC]
```

### Paso 4: preparar posición de conciliación

La audiencia de conciliación es informal. Preparar:

**Resumen de la posición del asegurado:**
- Hecho base: ¿qué pasó?
- Cobertura reclamada: ¿qué ampara la póliza?
- Lo que ofreció la aseguradora (si algo): ¿por qué es insuficiente?
- Lo que se solicita: monto, cumplimiento específico, o ambos

**Argumentos clave:**
1. [Argumento principal de cobertura — el más sólido]
2. [Argumento sobre la validez o alcance de la exclusión invocada por la aseguradora]
3. [Argumento sobre incumplimiento del plazo de pago de la aseguradora, si aplica]

**Posición de negociación:**
- Mínimo aceptable: [monto o condición] `[review: decisión del cliente]`
- Primera oferta propuesta a la aseguradora: [monto o propuesta]

### Paso 5: solicitud de arbitraje (si falla la conciliación)

Si la conciliación no llegó a acuerdo, preparar solicitud de arbitraje:

El arbitraje CONDUSEF puede ser:
- **En amigable composición:** CONDUSEF decide con base en sus propios criterios de equidad (más rápido, menos formal)
- **En estricto derecho:** CONDUSEF resuelve conforme a la LCS y el contrato de póliza (más formal, más robusto)

```
SOLICITUD DE ARBITRAJE ANTE CONDUSEF

[Encabezado igual a la queja]

Con fundamento en los artículos [X] de la LPDUSF, solicito se someta el
presente asunto a arbitraje [en amigable composición / en estricto derecho].

HECHOS (incorporar por referencia o resumir)

PRETENSIÓN ARBITRAL: [monto exacto de la indemnización + intereses moratorios
desde la fecha en que debió pagarse + costos, si aplica]

PRUEBAS QUE SE OFRECEN:
1. Documental: [lista de documentos]
2. Pericial: [si se requiere perito — médico, valuador, etc.]
3. [Otras pruebas]

Atentamente, [nombre y firma]
```

### Paso 6: output final

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [póliza y carta de negativa proporcionadas ✓ | plazos CONDUSEF: model knowledge — verify en condusef.gob.mx]
- Leído: [descripción de insumos]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar topes actuales de CONDUSEF para arbitraje por ramo; confirmar si la prescripción está vigente.

---

**Viabilidad de queja CONDUSEF:** [Procedente / Procedente con observaciones / No procedente — razón]
**Prescripción:** [vigente hasta AAAA-MM-DD] [review: plazo fatal]
**Competencia CONDUSEF:** [confirmada / verificar]

[Borrador de queja del Paso 3]

[Posición de conciliación del Paso 4]

[Si aplica: borrador de solicitud de arbitraje del Paso 5]

**Una pregunta que haría y que no está en mi checklist:** [observación]
```

> **¿Qué siges?**
> 1. **Enviar la queja ahora** — confirma que el borrador es correcto y preséntaloen condusef.gob.mx o en ventanilla; guarda el acuse de recibo.
> 2. **Análisis de cobertura** — `/seguros-legal-mexico:cobertura-analysis` para fortalecer los argumentos de la queja con análisis jurídico detallado.
> 3. **Preparar pruebas periciales** — identifico qué peritaje se necesita (médico, valuador, actuar) y qué debe acreditar.
> 4. **Demanda civil o mercantil** — si CONDUSEF no tiene competencia por el monto o el tipo de disputa, analizo la ruta judicial.
> 5. **Escalar** — si la negativa de la aseguradora afecta a múltiples asegurados, puede justificar una acción colectiva o denuncia a la CNSF.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
