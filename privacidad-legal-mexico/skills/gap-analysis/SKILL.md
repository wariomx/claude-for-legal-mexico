---
description: >
  Diagnóstico de cumplimiento LGPDPPSP/LFPDPPP — checklist de obligaciones del
  responsable, identificación de brechas por severidad, y plan de remediación
  priorizado. Produce tabla de hallazgos con severidad 🔴/🟠/🟡/🟢.
argument-hint: "[--sector tecnologia|salud|fintech|educacion|retail|otro]"
---

# /gap-analysis

## Cuándo se ejecuta

El usuario quiere un diagnóstico estructurado de cumplimiento de la LFPDPPP (sector privado) o LGPDPPSP (sector público), con un mapa de brechas por severidad y un plan de remediación priorizado.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público) — determina la ley aplicable
- Tipos de datos personales tratados (especialmente si hay sensibles o de menores)
- Módulos activos — revisar solo los módulos configurados
- Sector o industria (si se proporcionó `--sector`, usar ese; si no, leer del perfil de práctica)

Si el perfil no existe o contiene `[PLACEHOLDER]`, detenerse: "Ejecuta `/privacidad-legal-mexico:cold-start-interview` primero."

### 2. Determinar el alcance

Si `--sector` no fue especificado y el perfil no lo indica, preguntar:
> ¿En qué sector opera la organización? Esto calibra las obligaciones sectoriales adicionales que el diagnóstico debe verificar (fintech → CNBV / Ley Fintech, salud → NOM-004-SSA3 / COFEPRIS, educación → datos de menores, retail → datos de clientes a escala). O di "general" para el marco base sin capas sectoriales.

### 3. Ejecutar el checklist por dominio

Para cada dominio, calificar el nivel de cumplimiento y producir la tabla de hallazgos.

**Escala de severidad:**
- 🔴 Bloqueante: brecha que expone al responsable a sanción inmediata o procedimiento ante el INAI. Requiere remediación antes de continuar el tratamiento afectado.
- 🟠 Alto: brecha significativa que crea riesgo de infracción en una inspección o procedimiento. Remediación urgente en las próximas 4 semanas.
- 🟡 Medio: brecha que debería corregirse pero no expone a sanción inmediata. Remediación en los próximos 3 meses.
- 🟢 Bajo: oportunidad de mejora o buena práctica no obligatoria. Incorporar en la siguiente revisión del ciclo.

---

#### Dominio 1: Aviso de privacidad

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 1.1 | Aviso de privacidad integral publicado y accesible | Arts. 15-16 LFPDPPP | [✓/✗/Parcial] | | |
| 1.2 | El aviso contiene identidad y domicilio del responsable | Art. 15 Fr. I | [✓/✗/Parcial] | | |
| 1.3 | El aviso distingue finalidades primarias y secundarias | Art. 15 Fr. II | [✓/✗/Parcial] | | |
| 1.4 | El aviso indica mecanismos para ejercer ARCO | Art. 15 Fr. III | [✓/✗/Parcial] | | |
| 1.5 | El aviso informa sobre transferencias y sus finalidades | Art. 15 Fr. IV | [✓/✗/Parcial] | | |
| 1.6 | Para datos sensibles: el aviso recaba consentimiento expreso y por escrito | Arts. 8 y 9 LFPDPPP | [✓/✗/N/A] | | |
| 1.7 | Para datos de menores: el aviso recaba consentimiento de padre/tutor | | [✓/✗/N/A] | | |
| 1.8 | Existe mecanismo para notificar cambios al aviso | Art. 17 LFPDPPP | [✓/✗/Parcial] | | |
| 1.9 | El aviso está actualizado (refleja el tratamiento real actual) | | [✓/✗/Incierto] | | |

#### Dominio 2: ARCO

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 2.1 | Existe ventanilla de ARCO operativa (correo, portal o dirección) | Art. 28 LFPDPPP | [✓/✗/Parcial] | | |
| 2.2 | Hay un responsable designado para atender solicitudes ARCO | Art. 30 LFPDPPP | [✓/✗] | | |
| 2.3 | El plazo de respuesta de 20 días hábiles se respeta | Art. 32 LFPDPPP | [✓/✗/Incierto] | | |
| 2.4 | Existe registro de solicitudes ARCO con fecha de recepción | | [✓/✗/Parcial] | | |
| 2.5 | Existe procedimiento de verificación de identidad del titular | Art. 29 LFPDPPP | [✓/✗] | | |
| 2.6 | Las respuestas informan sobre medios de impugnación ante el INAI | Art. 34 LFPDPPP | [✓/✗/Incierto] | | |

#### Dominio 3: Medidas de seguridad

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 3.1 | Existen medidas de seguridad administrativas documentadas | Arts. 19-22 LFPDPPP | [✓/✗/Parcial] | | |
| 3.2 | Existen medidas de seguridad físicas (control de acceso a instalaciones) | | [✓/✗/Parcial] | | |
| 3.3 | Existen medidas de seguridad técnicas (cifrado, control de acceso digital) | | [✓/✗/Parcial] | | |
| 3.4 | Las medidas de seguridad son proporcionales a los datos tratados | | [✓/✗/Incierto] | | |
| 3.5 | Para datos sensibles: las medidas de seguridad son reforzadas | | [✓/✗/N/A] | | |
| 3.6 | Existe inventario o registro de los tratamientos de datos | | [✓/✗] | | |

#### Dominio 4: Encargados y transferencias

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 4.1 | Existe contrato con cada encargado que trata datos en nombre del responsable | Arts. 50-53 REGLAMENTO | [✓/✗/Parcial] | | |
| 4.2 | Los contratos de encargados incluyen obligaciones de confidencialidad y seguridad | | [✓/✗/Parcial] | | |
| 4.3 | Las transferencias a terceros tienen base legal (consentimiento o excepción) | Art. 37 LFPDPPP | [✓/✗/Parcial] | | |
| 4.4 | Las transferencias internacionales tienen base legal y contrato si aplica | Art. 37 LFPDPPP | [✓/✗/N/A] | | |
| 4.5 | Los contratos de encargados internacionales incluyen cláusulas de protección de datos | | [✓/✗/N/A] | | |

#### Dominio 5: Vulneraciones y respuesta a incidentes

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 5.1 | Existe protocolo de respuesta a incidentes de seguridad documentado | Art. 38 LFPDPPP | [✓/✗] | | |
| 5.2 | El protocolo incluye el plazo de 72 horas para notificar al INAI | Art. 38 LFPDPPP | [✓/✗/Parcial] | | |
| 5.3 | El protocolo incluye criterios para notificar a titulares afectados | Art. 38 LFPDPPP | [✓/✗/Parcial] | | |
| 5.4 | Existe registro de incidentes y vulneraciones ocurridas | | [✓/✗] | | |
| 5.5 | Se ha realizado al menos un ejercicio de respuesta a incidentes (tabletop o simulacro) | | [✓/✗] | | |

#### Dominio 6: EIPD (si el módulo está activo)

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 6.1 | Se realizan EIPDs para nuevos procesos con datos sensibles | Lineamientos INAI | [✓/✗/N/A] | | |
| 6.2 | Existe un umbral formal para activar una EIPD | | [✓/✗] | | |
| 6.3 | Las EIPDs están documentadas y archivadas | | [✓/✗/Parcial] | | |

#### Dominio 7: Gobernanza interna

| # | Obligación | Base legal | Estado | Severidad | Evidencia |
|---|---|---|---|---|---|
| 7.1 | Existe un responsable interno de protección de datos (DPO o equivalente) | Art. 30 LFPDPPP | [✓/✗/Parcial] | | |
| 7.2 | Existe capacitación en protección de datos para el personal | Art. 21 LFPDPPP | [✓/✗/Parcial] | | |
| 7.3 | Existe política interna de protección de datos documentada | | [✓/✗] | | |
| 7.4 | Los contratos laborales y de prestación de servicios incluyen cláusulas de confidencialidad de datos | | [✓/✗/Parcial] | | |

### 4. Tabla resumen de hallazgos

Producir tabla ordenada por severidad:

| # | Hallazgo | Dominio | Severidad | Artículo | Acción recomendada | Plazo sugerido |
|---|---|---|---|---|---|---|
| | | | 🔴 | | | Inmediato |
| | | | 🟠 | | | 4 semanas |
| | | | 🟡 | | | 3 meses |
| | | | 🟢 | | | Próximo ciclo |

Marcar con `[model knowledge — verify]` todas las citas de artículos. Marcar con `[review]` los hallazgos cuya severidad depende de hechos que el skill no puede verificar directamente (ej., "¿se realizan realmente EIPDs?" requiere verificación interna).

### 5. Plan de remediación priorizado

Producir plan en tres horizontes:

**Inmediato (0-30 días) — hallazgos 🔴:**
- [Lista de acciones concretas con responsable sugerido]

**Corto plazo (1-3 meses) — hallazgos 🟠:**
- [Lista de acciones concretas]

**Mediano plazo (3-6 meses) — hallazgos 🟡:**
- [Lista de acciones concretas]

### 6. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Cobertura:** [dominios evaluados / dominios no evaluados por falta de información]
> - **Hallazgos totales:** [N] — 🔴 [N] bloqueantes / 🟠 [N] altos / 🟡 [N] medios / 🟢 [N] bajos
> - **Marcado para tu criterio:** [N elementos marcados `[review]`]
> - **Antes de usar este diagnóstico:** [los 1-2 hallazgos más urgentes]

### 7. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Profundizar en un dominio** — Ejecuto un análisis más detallado del dominio que me señales.
> 2. **Redactar un plan de acción** — Produciré un plan de remediación con responsable, plazo y recursos estimados para presentar al Director Jurídico o al Consejo.
> 3. **Revisar el aviso de privacidad** — `/privacidad-legal-mexico:aviso-privacidad` con el checklist completo.
> 4. **Ver esto como dashboard** — Construiré una vista HTML con tabla por severidad y grafica de distribución.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
