---
description: >
  Gestiona trámites ante la Comisión Federal para la Protección contra Riesgos
  Sanitarios (COFEPRIS): registro sanitario, renovación, modificación,
  transferencia de titular, aviso de funcionamiento, licencia sanitaria, y
  certificados BPF. Verifica requisitos actuales, genera checklist de
  documentación, calcula plazos de resolución implícita (afirmativa ficta) y
  produce el escrito de solicitud listo para revisión. Aplica a medicamentos,
  dispositivos médicos, alimentos, suplementos alimenticios, cosméticos,
  plaguicidas y establecimientos sujetos a regulación sanitaria.
argument-hint: "[tipo de trámite] [tipo de producto o establecimiento]"
---

# Skill: cofepris-tramite (regulatorio-legal-mexico)

## Propósito

COFEPRIS tiene plazos de resolución que pueden extenderse meses si la solicitud llega incompleta. Este skill construye el expediente correcto desde el primer intento: verifica los requisitos actuales, genera el checklist de documentación completo, calcula los plazos aplicables (incluyendo la afirmativa ficta del Art. 17-D LGS) y produce el escrito de solicitud en el formato que espera el regulador.

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer del módulo COFEPRIS:
- Tipo de productos regulados
- Responsable Sanitario designado
- Registros sanitarios activos
- NOMs aplicables

Si el módulo COFEPRIS no está activo: ejecutar el triaje con parámetros genéricos pero advertir que los resultados serán menos calibrados.

### Paso 1: identificar el trámite

Si no está claro en el contexto, preguntar:

1. "¿Qué tipo de trámite necesitas gestionar?"
   - Registro sanitario (nuevo)
   - Renovación de registro sanitario
   - Modificación al registro sanitario
   - Transferencia de titular de registro sanitario
   - Aviso de funcionamiento de establecimiento
   - Licencia sanitaria
   - Certificado de Buenas Prácticas de Fabricación (BPF)
   - Certificado de libre venta / exportación
   - Autorización de publicidad / etiquetado
   - Otro (especificar)

2. "¿A qué categoría de producto o establecimiento corresponde?"
   - Medicamentos alopáticos
   - Medicamentos homeopáticos / herbolarios
   - Dispositivos médicos (Clase I / II / III)
   - Alimentos y bebidas no alcohólicas
   - Alimentos y bebidas alcohólicas
   - Suplementos alimenticios
   - Cosméticos
   - Plaguicidas y nutrientes vegetales
   - Materia prima para uso en alimentos
   - Establecimiento (laboratorio / planta de fabricación / importador / distribuidor)

### Paso 2: verificar requisitos vigentes

**Ejecutar búsqueda web** para confirmar los requisitos actuales del trámite en el sistema VUCE (Ventanilla Única de Comercio Exterior) o en el portal COFEPRIS. Los requisitos cambian con frecuencia — no confiar en listas estáticas.

Si no se puede hacer búsqueda web: "Los requisitos de COFEPRIS cambian con frecuencia. La información que tengo es de conocimiento del modelo `[model knowledge — verify]`. Verificar contra el portal COFEPRIS (https://www.gob.mx/cofepris) antes de preparar el expediente."

Fuentes de requisitos:
- Portal COFEPRIS: https://www.gob.mx/cofepris
- VUCE: https://www.ventanillaunica.gob.mx
- Cofemer/CONAMER (para MIR de NOM): https://www.conamer.gob.mx

### Paso 3: generar checklist de documentación

Para cada trámite, producir un checklist estructurado:

```
CHECKLIST DE DOCUMENTACIÓN — [Tipo de trámite]
[Tipo de producto] — COFEPRIS

Documentos del solicitante / titular:
  [ ] [Documento 1] — [especificación, formato, vigencia] `[verify vigencia]`
  [ ] [Documento 2]
  ...

Documentos técnicos del producto:
  [ ] [Documento técnico 1] — [especificación] `[verify]`
  [ ] [Documento técnico 2]
  ...

Documentos del establecimiento:
  [ ] [Documento 1]
  ...

Documentos de apoyo:
  [ ] [Documento 1]
  ...

NOTAS CRÍTICAS:
  ⚠️ [Cualquier requisito no obvio, cambio reciente o trámite previo necesario] `[review]`
```

Marcar con `[review]` los requisitos donde la información podría estar desactualizada o donde el criterio del profesional sanitario es necesario.

### Paso 4: calcular plazos

**Plazo de resolución ordinario:** depende del tipo de trámite y categoría del producto `[verify contra Ley General de Salud y Reglamento aplicable]`.

**Afirmativa ficta (Art. 17-D Ley General de Salud):** cuando la autoridad sanitaria no resuelve dentro del plazo legal, la respuesta se considera afirmativa. Calcular la fecha de vencimiento del plazo a partir de la fecha de presentación del expediente completo.

**Ojo:** la afirmativa ficta NO aplica a todos los trámites sanitarios — algunos quedan expresamente excluidos por la LGS o sus reglamentos. Identificar si el trámite específico es susceptible de afirmativa ficta. `[review]`

**Resolución anticipada:** COFEPRIS opera un sistema de "fast track" para medicamentos en situaciones especiales. Verificar si el trámite califica.

### Paso 5: producir el escrito de solicitud

```
[Ciudad], [Fecha]

C. Comisionada Federal para la Protección contra Riesgos Sanitarios
Av. Marina Nacional No. 60, Col. Tacuba, Alcaldía Miguel Hidalgo
C.P. 11410, Ciudad de México

ASUNTO: Solicitud de [tipo de trámite] — [nombre del producto / establecimiento]

[Nombre del solicitante], [cargo], en representación de [nombre de la empresa], con domicilio en [domicilio], comparece respetuosamente ante Usted para solicitar [tipo de trámite] respecto de [descripción del producto / establecimiento], con base en los siguientes:

ANTECEDENTES
[Descripción breve del producto, su uso, datos de registro previo si aplica]

FUNDAMENTO LEGAL
[Arts. de la Ley General de Salud, Reglamento aplicable, NOM aplicable] `[model knowledge — verify]`

SOLICITUD
Por lo anteriormente expuesto, solicito a Usted se sirva autorizar [lo que se pide].

Se adjunta al presente escrito la siguiente documentación:
[Lista numerada de documentos del checklist que el usuario ha confirmado tener]

Protesto lo necesario.

[Nombre del Responsable Sanitario o representante legal]
[Cédula profesional del Responsable Sanitario]
[Domicilio para oír y recibir notificaciones]
```

Marcar con `[VERIFY: …]` cualquier artículo legal citado para que el revisor confirme el texto vigente antes de enviar.

### Paso 6: árbol de decisión

> **¿Qué sigue?**
> 1. **Completar el expediente** — reviso el checklist contigo e identifico qué documentos faltan.
> 2. **Preparar respuesta a prevención COFEPRIS** — si ya recibirte una prevención (requerimiento de información adicional), `/regulatorio-legal-mexico:respuesta-regulador` prepara la respuesta.
> 3. **Calcular afirmativa ficta** — te doy la fecha exacta en que el silencio de COFEPRIS se convierte en resolución afirmativa y cómo documentarlo `[review]`.
> 4. **Escalar** — redacto nota de escalamiento al Director Jurídico o despacho externo con los hechos clave del trámite.
> 5. **Archivar** — guardo el checklist y el escrito en la carpeta del asunto para cuando esté listo para presentar.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
