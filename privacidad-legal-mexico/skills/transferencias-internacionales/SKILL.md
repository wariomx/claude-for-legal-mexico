---
description: >
  Analiza la licitud de transferencias internacionales de datos personales bajo
  la LFPDPPP — verifica si el país destino cuenta con nivel adecuado de
  protección, y si no, qué mecanismo aplica (cláusulas contractuales,
  consentimiento, excepción). Produce un análisis de riesgo y el instrumento
  contractual recomendado.
argument-hint: "[--destino <pais>] [--tipo intragrupo|encargado|controlador-independiente]"
---

# /transferencias-internacionales

## Cuándo se ejecuta

La organización está por transferir datos personales a una entidad o servidor ubicado fuera de México — proveedor en nube extranjero, filial internacional, socio comercial en otro país, o plataforma SaaS con sede fuera del territorio nacional. El skill analiza la base legal disponible y produce el instrumento de soporte recomendado.

## Instrucciones

### 1. Leer el perfil de práctica

Leer `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md`. Extraer:
- Tipo de responsable (sector privado / público)
- Transferencias internacionales habituales (destinos, proveedores en nube, estructura corporativa internacional)
- Mecanismo legal en uso actualmente (si está configurado)
- ¿Hay contratos DPA firmados con los proveedores internacionales?

Si el perfil no existe, continuar con advertencia de falta de configuración.

### 2. Establecer los hechos de la transferencia

Preguntar o extraer del caso:

| Elemento | Valor |
|---|---|
| País de origen de los datos | México |
| País o región de destino | |
| Categorías de datos que se transfieren | |
| ¿Incluye datos sensibles? (Art. 3 Fr. VI LFPDPPP) | Sí / No |
| ¿Incluye datos de menores? | Sí / No |
| Finalidad de la transferencia | |
| Tipo de destinatario | Filial / empresa del mismo grupo / encargado / controlador independiente |
| Frecuencia de la transferencia | Ocasional / Continua / Por lotes |
| ¿Hay contrato vigente con el destinatario? | Sí (tipo: ) / No |

### 3. Análisis de base legal — Arts. 36-37 LFPDPPP

Evaluar en orden las bases legales disponibles, de más sólida a menos sólida:

#### Base 1: Adecuación del nivel de protección

Verificar si el país destino ofrece un nivel de protección equivalente al de la LFPDPPP. México no ha publicado una lista formal de países con nivel adecuado de protección equivalente al mecanismo de adecuación de la UE. `[model knowledge — verify si el INAI ha publicado lineamientos o lista de países reconocidos como adecuados]`

Países cuya legislación ofrece marcos de privacidad reconocidos internacionalmente (referencia):
- Unión Europea y EEA: GDPR — marco robusto `[model knowledge — verify]`
- Reino Unido: UK GDPR post-Brexit `[model knowledge — verify]`
- Canadá: PIPEDA / Ley 25 (Quebec) `[model knowledge — verify]`
- Argentina, Colombia, Chile: leyes de protección de datos personales `[model knowledge — verify]`
- EUA: marco fragmentado (CCPA en California; no hay ley federal sectorial equivalente) — **no asumir adecuación** `[model knowledge — verify]`

**Si la adecuación es incierta o no existe: pasar a la siguiente base.**

#### Base 2: Cláusulas contractuales

El responsable transfiere los datos al destinatario mediante un contrato que obliga al destinatario a observar las mismas obligaciones que tiene el responsable bajo la LFPDPPP. `[settled — last confirmed 2026-05-24]` (Art. 68 Reglamento LFPDPPP)

Esta es la base recomendada para transferencias a encargados (procesadores) y para transferencias continuas a países sin adecuación confirmada.

**Cláusulas mínimas del contrato de transferencia:**

| Cláusula | Contenido requerido |
|---|---|
| Limitación de finalidad | El destinatario solo puede usar los datos para la finalidad declarada |
| Obligaciones de seguridad | El destinatario implementa medidas equivalentes a las del responsable |
| Restricción de transferencias posteriores | El destinatario no puede transferir los datos a un tercero sin autorización expresa |
| Derechos de auditoría | El responsable puede auditar el cumplimiento del destinatario |
| Notificación de vulneraciones | El destinatario notifica al responsable cualquier incidente de seguridad en un plazo definido |
| Obligaciones ante solicitudes ARCO | El destinatario coopera con el responsable para atender solicitudes ARCO |
| Datos sensibles | Si aplica: salvaguardas adicionales proporcionales al riesgo `[settled — last confirmed 2026-05-24]` (Art. 9 LFPDPPP) |
| Terminación y devolución / destrucción | Al terminar la relación, el destinatario devuelve o destruye los datos |

#### Base 3: Consentimiento expreso del titular

El titular otorga consentimiento libre, específico e informado para la transferencia. `[settled — last confirmed 2026-05-24]`

**Advertencia:** esta base es arriesgada para transferencias continuas o a gran escala. El consentimiento puede ser revocado en cualquier momento, y obtener consentimiento para cada nueva transferencia es operativamente inviable. **No se recomienda como base principal para transferencias recurrentes.** `[review: evaluar si el consentimiento es la base más adecuada para este caso]`

#### Base 4: Excepciones del Art. 37 LFPDPPP `[model knowledge — verify excepciones vigentes]`

| Excepción | ¿Aplica? | Notas |
|---|---|---|
| Tratado o convención internacional del que México sea parte | `[review]` | |
| Urgencia médica o sanitaria que involucre al titular | `[review]` | |
| Transferencia necesaria para la prevención o diagnóstico médico | `[review]` | |
| Transferencia para la protección de intereses vitales del titular | `[review]` | |
| Transferencia necesaria para la ejecución de un contrato entre el titular y el responsable | `[review]` | |
| Transferencia para la salvaguarda del interés público | `[review]` | |
| Transferencia para el reconocimiento, ejercicio o defensa de un derecho en un proceso judicial | `[review]` | |

### 4. Análisis específico para transferencias intragrupo

Cuando el destinatario es una filial, subsidiaria, o entidad del mismo grupo corporativo:

- La LFPDPPP no crea una exención automática para transferencias intragrupo — se necesita base legal de todos modos. `[settled — last confirmed 2026-05-24]`
- Opciones recomendadas para grupos corporativos:
  - **Acuerdo intragrupo** con cláusulas de protección de datos que vinculen a todas las entidades del grupo a las obligaciones de la LFPDPPP
  - **Binding Corporate Rules (BCRs)** — marco más robusto para grupos multinacionales, pero más complejo de implementar `[model knowledge — verify si el INAI reconoce BCRs como mecanismo válido]`

### 5. Nexo con el GDPR — verificación de doble cumplimiento

Si la transferencia involucra datos de personas ubicadas en la UE, o si el destinatario está establecido en la UE, pueden aplicar simultáneamente la LFPDPPP Y el GDPR. `[model knowledge — verify]`

México no cuenta con una decisión de adecuación de la Unión Europea — las transferencias entre empresas mexicanas y empresas de la UE requieren análisis bajo ambas leyes. Señalar para análisis separado con especialista en GDPR si:
- El responsable tiene clientes o empleados en la UE `[review]`
- El destinatario está establecido en la UE y puede estar sujeto al GDPR `[review]`
- Los datos transferidos fueron originalmente recolectados de personas en la UE `[review]`

### 6. Evaluación de riesgo por flujo de transferencia

Para cada flujo de transferencia identificado, calificar:

| Flujo | Destino | Datos | Base legal | Contrato vigente | Riesgo |
|---|---|---|---|---|---|
| [Flujo 1] | | | | Sí/No | 🔴/🟠/🟡/🟢 |
| [Flujo 2] | | | | Sí/No | 🔴/🟠/🟡/🟢 |

**Escala de riesgo:**
- 🔴 **Bloqueante:** transferencia sin base legal — detener hasta regularizar.
- 🟠 **Alto:** base legal presente pero sin contrato firmado o con contrato incompleto — regularizar en 30 días.
- 🟡 **Medio:** contrato vigente pero sin cláusulas de datos sensibles o sin derechos de auditoría — revisar en próximo ciclo.
- 🟢 **Bajo:** base legal sólida, contrato completo, medidas de seguridad documentadas.

### 7. Nota del revisor

> **⚠️ Nota del revisor**
> - **Fuentes:** [LegalDataHunter ✓ / no conectado — citas de conocimiento del modelo, verificar]
> - **Flujos analizados:** [N flujos de transferencia]
> - **Riesgo más alto identificado:** [🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo]
> - **Nexo GDPR:** `[review: verificar si aplica doble cumplimiento LFPDPPP + GDPR]`
> - **Lista de países adecuados:** `[model knowledge — verify lista INAI vigente]` — México no tiene mecanismo de adecuación formal con la UE. Las transferencias con entidades europeas requieren análisis bajo ambas leyes.
> - **Marcado para tu criterio:** [N elementos marcados `[review]` en línea]
> - **Antes de activar las transferencias:** Firmar contratos pendientes, verificar cláusulas de datos sensibles si aplica, aprobar con [responsable según perfil]

### 8. Árbol de decisión

> **¿Qué siges? Elige una opción:**
> 1. **Redactar el contrato de transferencia / DPA** — Produciré un borrador del contrato de transferencia internacional con las cláusulas mínimas requeridas, adaptado al tipo de destinatario y datos involucrados.
> 2. **Redactar el acuerdo intragrupo** — Si la transferencia es a una filial o entidad del mismo grupo, produciré el acuerdo intragrupo con cláusulas de protección de datos.
> 3. **Analizar el nexo GDPR** — Si hay elementos europeos en la cadena, identificaré qué obligaciones adicionales aplican bajo el GDPR y qué mecanismo de transferencia hacia México aplica desde la UE.
> 4. **Actualizar el aviso de privacidad** — Si la transferencia internacional no estaba declarada en el aviso de privacidad, ajustaré el aviso para reflejarla correctamente.
> 5. **Algo diferente** — dime qué necesitas.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
