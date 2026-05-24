---
description: >
  Revisa una póliza de seguro conforme a la LCS (Ley sobre el Contrato de
  Seguro) y las condiciones generales del ramo. Verifica la carátula,
  condiciones generales, condiciones particulares y endosos; identifica
  exclusiones, cláusulas potencialmente inválidas, obligaciones del
  asegurado y plazos críticos. Produce un reporte de hallazgos con
  severidad y árbol de decisión.
argument-hint: "[ramo de seguro o nombre de la póliza a revisar]"
---

# Skill: poliza-review (seguros-legal-mexico)

## Propósito

Una póliza de seguro es un contrato de adhesión regulado principalmente por la LCS. Muchas condiciones generales incluyen cláusulas que restringen coberturas más allá de lo que la LCS permite, o que imponen cargas al asegurado que la ley no autoriza. Este skill mapea la póliza contra la LCS y detecta estas brechas antes de que surja un siniestro.

## Marco legal aplicable

| Norma | Relevancia |
|---|---|
| LCS Arts. 1-192 | Ley sobre el Contrato de Seguro — marco general |
| LCS Art. 25 | Póliza como documento probatorio del contrato |
| LCS Arts. 31-35 | Declaraciones del asegurado y consecuencias de inexactitud |
| LCS Arts. 52-66 | Obligaciones del asegurado: mantenimiento del riesgo, aviso de siniestro |
| LCS Art. 66 | **Plazo fatal: aviso de siniestro en 5 días hábiles** |
| LCS Arts. 67-72 | Evaluación, liquidación y pago del siniestro |
| LCS Art. 81 | **Prescripción: 2 años (5 años para vida/muerte)** |
| LCS Arts. 100-109 | Seguro de daños — subrogación, infraseguro, valor de reposición |
| LCS Arts. 151-191 | Seguro de personas (vida, salud, accidentes) |
| LISF Arts. 200-230 | Condiciones generales — requisitos mínimos por ramo `[model knowledge — verify]` |
| Disposiciones CNSF | Condiciones generales registradas por ramo `[model knowledge — verify]` |

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer:
- Tipo de entidad (operador / asegurado corporativo / asegurado individual)
- Ramos activos

Si el módulo seguros no está configurado: ejecutar con parámetros genéricos y advertir.

### Paso 1: identificar el documento

Si el usuario no proporcionó la póliza, solicitar:
1. "¿Qué ramo de seguro cubre esta póliza? (vida / daños / responsabilidad civil / GMM / auto / transporte / D&O / ciberseguridad / fianzas / otro)"
2. "¿Tienes el documento de la póliza (carátula + condiciones generales + condiciones particulares + endosos)? Puedes pegarlo o indicar la ruta."
3. "¿Cuál es el propósito de la revisión? (compra / renovación / siniestro activo / auditoría de cobertura / litigio)"

### Paso 2: revisar la carátula

Verificar que la carátula contenga los elementos mínimos conforme a la LCS:

- [ ] Nombre y domicilio del asegurador
- [ ] Nombre y domicilio del contratante / tomador
- [ ] Nombre del asegurado (si difiere del contratante)
- [ ] Nombre del beneficiario (para seguros de personas)
- [ ] Objeto del seguro / bien o persona asegurada
- [ ] Suma asegurada o forma de determinarla
- [ ] Prima y forma de pago
- [ ] Vigencia (inicio y fin, hora de inicio)
- [ ] Número de póliza y endosos incorporados
- [ ] Firma del asegurador

Clasificar cada elemento: ✓ Presente / ⚠️ Parcial / ✗ Ausente / N/A

### Paso 3: revisar condiciones generales

Para cada sección de condiciones generales:

#### 3A. Cobertura (objeto del seguro)

- [ ] La cobertura es determinable o determinada conforme al Art. 7 LCS `[review]`
- [ ] El riesgo cubierto no es ilícito ni contrario al orden público (Arts. 2 y 3 LCS)
- [ ] Los sub-límites y deducibles están expresamente definidos

#### 3B. Exclusiones

Para cada exclusión identificada:
- Citar el texto de la exclusión
- Verificar que sea una exclusión válida bajo la LCS (no una exclusión encubierta que anule la cobertura principal)
- Verificar que esté redactada en lenguaje claro (las exclusiones ambiguas se interpretan contra el asegurador — Art. 162 del Código de Comercio, integrado a la LCS por práctica judicial)
- Clasificar: ✓ Válida y clara / ⚠️ Ambigua [review] / ✗ Potencialmente inválida bajo LCS

Marcar exclusiones que restrinjan coberturas por encima de lo que la LCS permite como `[review: posible cláusula abusiva]`.

#### 3C. Obligaciones del asegurado

- [ ] Obligaciones de mantenimiento del riesgo razonables y conformes a los Arts. 52-55 LCS
- [ ] Plazo de aviso de siniestro: ¿corresponde al mínimo legal de 5 días hábiles del Art. 66 LCS? Si la póliza fija un plazo menor, marcar `[review: plazo más restrictivo que LCS Art. 66]`
- [ ] Documentación requerida para reclamar: ¿es proporcional al tipo de siniestro?
- [ ] ¿Hay cláusulas de colaboración en la investigación del siniestro? Verificar que no transfieran carga probatoria al asegurado más allá de lo razonable `[review]`

#### 3D. Procedimiento de reclamación y pago

- [ ] Plazo para que la aseguradora emita dictamen de procedencia `[verify plazo regulatorio CNSF vigente]`
- [ ] Plazo de pago una vez procedente la reclamación `[verify plazo legal vigente]`
- [ ] Mecanismo de controversias: ¿remite a CONDUSEF / arbitraje / judicial?

#### 3E. Subrogación (seguros de daños)

- [ ] Cláusula de subrogación conforme al Art. 111 LCS
- [ ] Excepciones a la subrogación (parientes del asegurado — Art. 112 LCS)
- [ ] ¿Hay cláusula de renuncia a subrogación? Verificar su alcance

### Paso 4: revisar endosos

Para cada endoso:
- Identificar si amplía, restringe o modifica la cobertura base
- Verificar que el endoso esté claramente incorporado a la carátula
- Para endosos restrictivos: verificar validez bajo LCS `[review]`
- Para endosos de exclusión de subrogación / waiver of subrogation: verificar si es conforme `[review]`

### Paso 5: consolidar hallazgos

Producir tabla de hallazgos:

```
| # | Sección | Texto | Estado | Severidad | Fundamento LCS | Acción recomendada |
|---|---|---|---|---|---|---|
| 1 | Exclusiones | "..." | ⚠️ Ambigua | 🟠 Alto | Art. 162 CCom | Negociar redacción |
...
```

Ordenar por severidad descendente (🔴 primero). Escala canónica: 🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo.

### Paso 6: producir reporte

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [CNSF verificado ✓ | model knowledge — verify para umbrales específicos]
- Leído: [secciones revisadas de la póliza]
- Marcado para tu criterio: [N elementos [review]]
- Antes de confiar: verificar condiciones generales registradas ante CNSF para este ramo; las pólizas deben corresponder a las condiciones aprobadas.

---

**Revisión de Póliza — [ramo] — [asegurador] — [fecha]**

**Resumen ejecutivo:** [N hallazgos — X bloqueantes 🔴, Y altos 🟠, Z medios 🟡, W bajos 🟢]

**Ramo:** [nombre]
**Vigencia:** [fechas]
**Suma asegurada:** [monto o N/A]
**Prima anual:** [monto o N/A]

[Tabla de hallazgos del Paso 5]

**Plazos críticos identificados:**
- Aviso de siniestro: [plazo de la póliza vs. mínimo LCS Art. 66] `[review: plazo fatal]`
- Prescripción aplicable: [2 años / 5 años según ramo — LCS Art. 81] `[review: plazo fatal]`

**Una pregunta que haría y que no está en mi checklist:** [observación de segundo orden]
```

> **¿Qué sigue?**
> 1. **Negociar modificaciones** — identifico los 3 cambios de mayor impacto para negociar con la aseguradora antes de renovar.
> 2. **Analizar cobertura para un siniestro específico** — `/seguros-legal-mexico:cobertura-analysis` con los hechos del siniestro y esta póliza.
> 3. **Comparar con condiciones generales CNSF** — verifico si las condiciones de la póliza corresponden a las condiciones generales aprobadas para este ramo.
> 4. **Escalar a especialista** — redacto una nota para el Director Jurídico o despacho externo con los hallazgos críticos.
> 5. **Revisar otro documento** — endoso, condiciones particulares o póliza relacionada.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
