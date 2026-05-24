---
description: >
  Ejecuta la entrevista de configuración inicial para conocer la práctica fiscal
  del despacho o empresa y escribir el perfil de práctica. Usa en la primera
  instalación o con --redo para reconfigurar. Es el ÚNICO skill que debe
  ejecutarse en instalación nueva.
argument-hint: "[--redo | --check-integrations | --local]"
---

# Skill: cold-start-interview (fiscal-legal-mexico)

## Propósito

Este skill construye el perfil de práctica fiscal que todos los demás skills de este plugin leen antes de producir cualquier resultado. Sin él, los outputs son genéricos y podrían no corresponder al régimen, las obligaciones reales ni la situación ante el SAT del cliente. La entrevista tarda entre 10 y 15 minutos; invertirlos al inicio calibra todos los comandos del plugin.

## Flujo

### Paso 0: verificar estado actual

Lee el perfil de práctica en este orden:

1. **Local:** `.claude-legal/fiscal-legal-mexico/CLAUDE.md` en el directorio de trabajo actual.
2. **Global:** `~/.claude/plugins/config/claude-for-legal/fiscal-legal-mexico/CLAUDE.md`.

- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSED AT: -->`** → ofrecer reanudar desde esa sección.
- **Contiene `[PLACEHOLDER]` sin comentario de pausa** → ofrecer iniciar de nuevo o retomar.
- **Poblado sin placeholders** → ya configurado; omitir a menos que se pase `--redo`.

Si se pasa `--redo`: mostrar un diff del perfil actual antes de sobreescribir y pedir confirmación.

Si se pasa `--check-integrations`: omitir la entrevista. Re-ejecutar únicamente la verificación de integraciones del Paso 2 y reescribir la tabla `## Integraciones disponibles` en el perfil activo.

Si se pasa `--local`: escribir en `.claude-legal/fiscal-legal-mexico/CLAUDE.md` (crear directorios padre si no existen). Sin este flag, escribir en la ruta global.

### Paso 1: perfil compartido de la empresa

Busca `~/.claude/plugins/config/claude-for-legal/company-profile.md` (o `.claude-legal/company-profile.md` si hay config local activa).

- **Si existe:** lee y muestra: "Eres [nombre], [sector], RFC [RFC]. ¿Correcto? (Di 'actualizar' para cambiar el perfil compartido.)" Si confirma, salta las preguntas de empresa — ir directo al Paso 3.
- **Si no existe:** este plugin es el primero en configurarse. Hacer las preguntas de empresa del Paso 3 y escribir también el perfil compartido al terminar.

### Paso 2: verificar integraciones

Comprueba qué conectores están realmente respondiendo (no solo configurados):

- **Portal SAT / Buzón Tributario** — intenta una consulta simple; reporta ✓ solo si responde.
- **TFJA portal digital** — verifica acceso.
- **PRODECON portal** — verifica acceso.
- **Almacenamiento de documentos** (Drive, SharePoint, Box) — verifica acceso.
- **Slack** — verifica acceso.

Reporta en tabla: ✓ conectado (probado) / ⚪ configurado pero no verificado / ✗ no encontrado.

Un conector listado en `.mcp.json` es *disponible*, no *conectado*. Nunca reportar ✓ sin una llamada real que haya respondido.

### Paso 3: entrevista — perfil fiscal

Haz las preguntas en bloques de 2-3. Pausa y espera respuesta antes de continuar.

**Sección A — Perfil fiscal básico** (omitir si ya está en company-profile.md):
1. ¿Nombre de la entidad y RFC?
2. ¿Tipo de persona y régimen fiscal? (Persona moral — régimen general / RESICO / actividades agrícolas / maquiladora / otro; persona física — actividad empresarial / honorarios / RESICO / arrendamiento / otro)
3. ¿ADSC asignada (Administración Desconcentrada de Servicios al Contribuyente)?
4. ¿Sector económico y actividad principal (clave de actividad SAT)?

**Sección B — Obligaciones principales:**
5. ¿Qué impuestos declara periódicamente? (ISR mensual/anual, IVA mensual, IEPS, retenciones de ISR e IVA, nómina electrónica)
6. ¿Tiene obligaciones internacionales? (precios de transferencia, tratados de doble imposición, revelación de esquemas reportables — Arts. 197-202 CFF)

**Sección C — CFDI y facturación:**
7. ¿Versión CFDI en uso? (debe ser 4.0) ¿Tipo de comprobantes frecuentes? (facturas, notas de crédito, recibos de nómina, complemento de pagos, carta porte)
8. ¿Nombre del PAC (Proveedor Autorizado de Certificación) habitual?

**Sección D — Historial SAT:**
9. ¿Hay cartas invitación activas? ¿Requerimientos en curso?
10. ¿Hay auditorías activas? (visita domiciliaria / gabinete / electrónica — indicar período revisado)
11. ¿Hay acuerdos conclusivos PRODECON previos o en proceso? ¿Asuntos ante TFJA activos?

**Sección E — Módulos a activar:**
12. ¿Cuáles módulos deseas activar? (CFDI Review / Discrepancias SAT / Auditorías SAT / Litigación TFJA / PRODECON / Planeación Fiscal)

**Sección F — Documentos semilla:**
13. ¿Tienes disponible alguno de estos documentos para que el plugin los indexe?
    - Última declaración anual
    - Dictamen fiscal (si aplica)
    - Contratos con partes relacionadas (si hay precios de transferencia)
    - Estructura corporativa (si hay holding o subsidiarias)

### Paso 4: revisar y completar

Antes de escribir el perfil, lista todas las preguntas que se saltaron o quedaron con placeholder. Pregunta: "Antes de guardar la configuración, esto quedó abierto: [lista]. ¿Quieres completarlo ahora o dejarlo como placeholder?" Espera la respuesta. Nunca escribir placeholders silenciosos.

### Paso 5: escribir el perfil de práctica

Escribe en la ruta activa (local o global) el archivo de configuración usando la plantilla en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`. Activa solo los módulos elegidos en la Sección E.

Confirma al usuario: "Perfil guardado en [ruta]. Re-ejecuta `/fiscal-legal-mexico:cold-start-interview --redo` para modificar o `--check-integrations` para reverificar conectores."

---

**⚠️ Nota del revisor:** El RFC y la ADSC deben verificarse directamente en el portal SAT (sat.gob.mx) — no confiar únicamente en los datos proporcionados por el usuario. Los regímenes fiscales y las obligaciones específicas pueden cambiar con la Resolución de Miscelánea Fiscal (RMF) vigente `[model knowledge — verify]`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
