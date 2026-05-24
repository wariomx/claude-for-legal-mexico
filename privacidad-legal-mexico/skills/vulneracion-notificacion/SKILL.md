---
description: >
  Protocolo de respuesta a vulneración de seguridad de datos personales —
  análisis de la obligación de notificación al INAI (72 horas), borrador de
  aviso al INAI y a los titulares afectados, y checklist de contención.
argument-hint: "[--fecha-descubrimiento <AAAA-MM-DD>]"
---

# /vulneracion-notificacion

## Cuándo se ejecuta

La organización ha detectado o sospecha un incidente de seguridad que pudo haber comprometido datos personales. El skill ayuda a: (a) determinar si el incidente es una "vulneración" en el sentido del Art. 38 LFPDPPP; (b) calcular el plazo de 72 horas para notificar al INAI; (c) redactar el aviso al INAI; y (d) evaluar si se debe notificar a los titulares afectados.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Responsable de activar el protocolo (CISO / Director Jurídico / área de privacidad)
- Criterio interno de "vulneración significativa"
- Tipos de datos personales tratados (especialmente si hay datos sensibles)
- Módulo de Vulneraciones activo

Si el módulo no está activo o el perfil no existe, detenerse y pedir cold-start-interview.

### 2. Intake del incidente

Preguntar (o extraer del reporte del usuario):

| Campo | Valor |
|---|---|
| **Fecha y hora de descubrimiento** | [CAMPO CRÍTICO — el plazo de 72h corre desde este momento] |
| Descripción del incidente | |
| Sistemas o bases de datos afectados | |
| Tipos de datos personales comprometidos | |
| Número estimado de titulares afectados | |
| ¿El incidente sigue activo? | Sí / No / Incierto |
| Medidas de contención adoptadas | |
| ¿Se ha determinado la causa raíz? | |

**REGLA DURA — Fecha de descubrimiento:**
El plazo de 72 horas corre desde el momento en que el responsable "tiene conocimiento" de la vulneración, no desde que se confirma, no desde que se investigó, no desde que se reportó internamente al nivel correcto. El conocimiento de cualquier empleado del responsable puede ser suficiente para activar el plazo. Cuando hay duda sobre cuándo inició el plazo, marcar con `[review: momento de inicio del plazo — criterio INAI]`. `[model knowledge — verify]`

### 3. Determinar si el incidente es una "vulneración" bajo la LFPDPPP

El Art. 38 LFPDPPP define vulneración de seguridad como el "acceso, transmisión, modificación o destrucción no autorizados de datos personales" que ocurra en cualquier fase del tratamiento. `[settled — last confirmed 2026-05-24]`

Criterios de análisis:

| Criterio | Sí / No / Incierto | Notas |
|---|---|---|
| ¿Hubo acceso no autorizado a datos personales? | | |
| ¿Hubo transmisión no autorizada de datos personales? | | |
| ¿Hubo modificación no autorizada de datos personales? | | |
| ¿Hubo destrucción no autorizada de datos personales? | | |
| ¿Los datos afectados son personales (identifican o identifican a personas físicas)? | | |
| ¿El responsable los tenía bajo su custodia o los trataba? | | |

Si algún criterio es "Sí" o "Incierto": proceder con el análisis de notificación. No esperar confirmación total antes de activar el protocolo — el plazo de 72h corre. `[review: determinar si el incidente califica como vulneración]`

### 4. Cómputo del plazo de 72 horas

**Plazo:** 72 horas contadas desde que el responsable tuvo conocimiento de la vulneración. `[settled — last confirmed 2026-05-24]`

El plazo es en **horas**, no en días hábiles. Cuenta sábados, domingos y días festivos.

Si se proporcionó `--fecha-descubrimiento`: calcular la fecha y hora límite de notificación al INAI.

Marcar con: `[review: plazo INAI 72h vence AAAA-MM-DD HH:MM — confirmar fecha/hora de descubrimiento]`

**Consecuencias del incumplimiento:** El Art. 64 LFPDPPP establece sanciones económicas al responsable por incumplir la obligación de notificación. El monto depende de la gravedad y los ingresos del responsable. `[model knowledge — verify montos actualizados de sanciones]`

### 5. Checklist de contención

Antes de redactar el aviso al INAI, verificar que se han adoptado medidas básicas de contención:

- [ ] Aislar los sistemas afectados del resto de la red
- [ ] Preservar evidencia del incidente (logs, capturas, registros de acceso) — la preservación es necesaria para la investigación y para el aviso al INAI
- [ ] Cambiar credenciales comprometidas o potencialmente comprometidas
- [ ] Notificar internamente al responsable de activar el protocolo
- [ ] Documentar todas las acciones adoptadas con fecha y hora
- [ ] Verificar si hay obligaciones contractuales de notificación a clientes o a encargados
- [ ] Verificar si aplica alguna obligación sectorial adicional (CNBV para sector financiero, COFEPRIS para sector salud) `[model knowledge — verify regulación sectorial aplicable]`

### 6. Análisis de notificación a titulares

La LFPDPPP requiere notificar a los titulares afectados cuando la vulneración "afecte de forma significativa sus derechos o intereses." `[settled — last confirmed 2026-05-24]`

Factores para evaluar significatividad:

| Factor | Presente | Severidad |
|---|---|---|
| Datos sensibles comprometidos (salud, biométricos, etc.) | | 🔴 |
| Datos patrimoniales o financieros (cuenta bancaria, tarjeta) | | 🔴 |
| Datos de menores comprometidos | | 🔴 |
| Más de [umbral del perfil de práctica] titulares afectados | | 🟠 |
| Datos pueden usarse para robo de identidad | | 🔴 |
| Datos ya fueron usados de forma maliciosa | | 🔴 |
| Datos de identificación básica (nombre, correo) sin contexto sensible | | 🟡 |

Marcar con `[review]` la determinación de significatividad — es un juicio jurídico que puede ser objeto de procedimiento ante el INAI si el titular lo impugna.

### 7. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Plazo INAI:** `[review: vence AAAA-MM-DD HH:MM — confirmar fecha/hora de descubrimiento]`
> - **Notificación a titulares:** `[review: determinar si la vulneración afecta significativamente derechos]`
> - **Marcado para tu criterio:** [N elementos marcados `[review]` | ninguno]
> - **Antes de notificar:** Confirmar fecha de descubrimiento, revisar medidas de contención, aprobar con [responsable según perfil]

### 8. Borrador de aviso al INAI

El aviso al INAI debe incluir como mínimo `[model knowledge — verify elementos requeridos por INAI]`:

1. **Datos del responsable:** razón social, RFC, domicilio fiscal, nombre y datos de contacto del responsable de privacidad o persona de contacto.
2. **Descripción del incidente:** qué ocurrió, cómo, cuándo se detectó.
3. **Datos personales afectados:** categorías de datos y, si es posible, número aproximado de titulares.
4. **Posibles consecuencias:** qué riesgos puede generar la vulneración para los titulares.
5. **Medidas adoptadas:** acciones de contención, investigación y corrección implementadas.
6. **Acciones para notificar a titulares:** si se notificará a los titulares, por qué canal y en qué plazo.
7. **Datos de contacto** para seguimiento.

Producir el borrador marcando con `[review]` cualquier campo que dependa de información no disponible (ej., número exacto de titulares, causa raíz si aún se investiga).

### 9. Borrador de notificación a titulares (si aplica)

Si se determinó que la vulneración es significativa, producir borrador de comunicación a los titulares en lenguaje llano:
- Qué ocurrió
- Qué datos fueron afectados
- Qué riesgos pueden enfrentar
- Qué medidas adoptó el responsable
- Qué pueden hacer los titulares para protegerse
- Datos de contacto del responsable para preguntas

### 10. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Finalizar el aviso al INAI** — Revisaré el borrador y te daré la versión final. Recuerda: el plazo vence en `[review: AAAA-MM-DD HH:MM]`.
> 2. **Redactar comunicación a titulares** — Si determinaste que la vulneración es significativa, produciré el borrador de notificación masiva.
> 3. **Escalar internamente** — Redactaré una nota de escalamiento al [responsable según el perfil] con los hechos clave y las decisiones que se necesitan.
> 4. **Evaluar obligaciones sectoriales adicionales** — Análisis de si algún regulador sectorial (CNBV, COFEPRIS, otro) tiene obligaciones de notificación específicas.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
