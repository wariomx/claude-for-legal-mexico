---
description: >
  Redacción o revisión de aviso de privacidad conforme a LFPDPPP/LGPDPPSP —
  simplificado, corto o integral. Verifica que contenga todos los elementos
  obligatorios (Arts. 15-17 LFPDPPP), identifica finalidades secundarias y
  brechas de consentimiento, y produce versión lista para revisión del abogado.
argument-hint: "[--tipo simplificado|corto|integral] [--revisar <ruta>]"
---

# /aviso-privacidad

## Cuándo se ejecuta

El usuario quiere revisar un aviso de privacidad existente para verificar cumplimiento, o redactar uno nuevo desde cero. Aplica para avisos del sector privado (LFPDPPP) y sector público (LGPDPPSP). El skill bifurca según `--tipo` o según lo que indique el perfil de práctica.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público)
- Tipos de datos personales tratados (especialmente si hay datos sensibles o de menores)
- Módulo de Avisos de Privacidad activo — repositorio de avisos, fecha de última revisión
- Tipo de aviso solicitado (simplificado / corto / integral)

Si el perfil no existe o contiene `[PLACEHOLDER]`, detenerse: "Ejecuta `/privacidad-legal-mexico:cold-start-interview` primero."

### 2. Determinar el modo

**Modo revisión (`--revisar <ruta>` o el usuario comparte un aviso existente):**
- Leer el aviso proporcionado.
- Ejecutar el checklist de elementos obligatorios (ver abajo).
- Producir tabla de hallazgos con severidad.
- Si el usuario no especificó `--tipo`, inferir el tipo del aviso por su extensión y contenido.

**Modo redacción (no se proporcionó aviso):**
- Preguntar: "¿Redactamos un aviso [simplificado / corto / integral]? ¿O los tres?" (Si el perfil ya lo indica, confirmar en una línea.)
- Preguntar por el canal de recolección de datos (en persona, portal web, app móvil, contrato, etiqueta física) — el tipo de aviso depende del canal.
- Redactar el aviso con todos los elementos obligatorios, marcando con `[review]` cualquier elemento que dependa de información que el perfil no tiene.

### 3. Checklist de elementos obligatorios

#### Aviso integral (Art. 15 LFPDPPP) `[settled — last confirmed 2026-05-24]`

| # | Elemento | Presente | Notas |
|---|---|---|---|
| 1 | Identidad y domicilio del responsable | | |
| 2 | Finalidades del tratamiento (primarias y secundarias diferenciadas) | | |
| 3 | Opciones y medios para ejercer derechos ARCO | | |
| 4 | Transferencias y sus finalidades (si aplica) | | |
| 5 | Procedimiento y medios para que el titular revoque su consentimiento | | |
| 6 | Opciones para limitar el uso o divulgación de datos personales | | |
| 7 | Uso de cookies, web beacons u otras tecnologías de rastreo (si aplica) | | |
| 8 | Si hay datos sensibles: recabar consentimiento expreso y por escrito | | |
| 9 | Si hay datos de menores: recabar consentimiento de padre/tutor | | |
| 10 | Mecanismo para notificar cambios al aviso | | |

#### Aviso simplificado (Art. 16 LFPDPPP) `[settled — last confirmed 2026-05-24]`

| # | Elemento | Presente | Notas |
|---|---|---|---|
| 1 | Identidad del responsable | | |
| 2 | Finalidades del tratamiento | | |
| 3 | Referencia al aviso integral (URL o medio de acceso) | | |

#### Aviso corto

El aviso corto es un formato intermedio no regulado expresamente por artículo propio — es una práctica aceptada por el INAI para medios con espacio limitado. Debe incluir al menos los elementos del aviso simplificado más las finalidades secundarias si las hay. `[model knowledge — verify]`

### 4. Análisis de finalidades

Identificar y separar:
- **Finalidades primarias:** necesarias para la relación con el titular (prestación del servicio, ejecución del contrato). No requieren consentimiento adicional si se informan en el aviso y el titular continúa la relación.
- **Finalidades secundarias:** no necesarias para la relación (marketing, perfilado, cesión a terceros comerciales). Requieren consentimiento tácito (el titular puede oponerse) o expreso según su naturaleza.

Marcar con `[review]` cualquier finalidad que parezca necesaria para la relación pero que pudiera calificarse como secundaria, o viceversa.

### 5. Análisis de base legal de tratamiento

Para cada finalidad, identificar la base legal invocada:
- **Consentimiento** — el titular lo otorga libre e informadamente. Para datos sensibles: expreso y por escrito.
- **Ejecución de contrato** — el tratamiento es necesario para cumplir la obligación contractual con el titular.
- **Obligación legal** — el tratamiento está requerido por ley (ej., SAT requiere RFC, IMSS requiere datos del trabajador).
- **Interés legítimo** — aplica en sector privado con reservas; el INAI ha reconocido esta base en lineamientos pero su alcance es debatido. `[model knowledge — verify]`

### 6. Transferencias

Si el aviso declara transferencias, verificar:
- ¿Está identificado el destinatario (o al menos la categoría de destinatario)?
- ¿Están listadas las finalidades de la transferencia?
- ¿Se indica si el titular puede oponerse o si la transferencia es necesaria para la relación?
- ¿Se incluyen transferencias a encargados (los encargados en general no requieren consentimiento del titular pero sí un contrato)?

Distinguir transferencia (el tercero pasa a ser responsable) de transmisión a encargado (el tercero trata en nombre del responsable). La confusión entre ambas es una brecha frecuente. `[settled — last confirmed 2026-05-24]`

### 7. Nota del revisor

Antes del entregable, incluir:

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Tipo de aviso analizado:** [simplificado / corto / integral]
> - **Marcado para tu criterio:** [N elementos marcados `[review]` | ninguno]
> - **Antes de publicar:** [las 1-2 cosas más urgentes]

### 8. Entregable

**Modo revisión:** Producir:
1. Tabla de hallazgos con severidad (🔴 elemento obligatorio ausente / 🟠 elemento presente pero deficiente / 🟡 recomendable / 🟢 conforme).
2. Texto del aviso con marcas `[review]` en línea en los elementos que requieren criterio del abogado.
3. Lista de elementos a agregar o corregir.

**Modo redacción:** Producir el borrador completo del aviso en el formato solicitado. Marcar con `[review]` cualquier campo que dependa de información no disponible en el perfil (ej., domicilio exacto del responsable, datos de contacto ARCO).

### 9. Árbol de decisión

> **¿Qué sigue? Elige una opción:**
> 1. **Corregir el aviso** — Produciré la versión corregida con los elementos faltantes o deficientes resueltos.
> 2. **Escalar para revisión** — Redactaré una nota de escalamiento con las brechas críticas identificadas.
> 3. **Revisar la base legal de una finalidad específica** — Analizo la base legal invocada para la finalidad que me señales.
> 4. **Ejecutar gap-analysis completo** — `/privacidad-legal-mexico:gap-analysis` para un diagnóstico integral de cumplimiento más allá del aviso.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
