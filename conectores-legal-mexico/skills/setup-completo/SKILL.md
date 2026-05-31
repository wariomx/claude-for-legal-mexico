---
name: setup-completo
description: >
  Configuración inicial completa para todos los plugins de derecho mexicano.
  Captura el perfil del despacho una vez, permite seleccionar las áreas de
  práctica relevantes, verifica conectores y configura solo los plugins
  instalados. Usa en instalación nueva o con --redo para reconfigurar todo,
  --from <N|plugin> para retomar desde un paso, --check-integrations para
  re-verificar conectividad, o --new-client <nombre> para crear un directorio
  aislado de cliente.
argument-hint: "[--redo | --from <N|plugin> | --check-integrations | --local | --new-client <nombre>]"
---

# /setup-completo

Wizard de configuración para los plugins de derecho mexicano. Captura datos
compartidos una sola vez y configura los plugins instalados y seleccionados.

---

## Paso 0 — Parsear banderas y detectar estado

Antes de mostrar cualquier cosa:

**Banderas activas:**
- `--redo`: marcar todos los plugins como `pendiente` (forzar re-ejecución completa).
- `--from <N>` o `--from <plugin-slug>`: marcar ese paso/plugin y todos los siguientes como `pendiente`; dejar los anteriores como están.
- `--check-integrations`: ir directo al Paso 5 (re-verificación de conectividad en todos los plugins instalados).
- `--local`: todas las rutas de config son locales (`.claude-legal/<plugin>/CLAUDE.md` en el directorio actual) en vez de globales. Pasar `--local` a cada cold-start-interview.
- `--new-client <nombre>`: al final del wizard global, crear `./<nombre>/`, re-ejecutar Pasos 1-7 con `--local` y `--cwd ./<nombre>/`.

**Detectar plugins instalados.** Para cada plugin conocido, verificar si su directorio existe Y tiene un `plugin.json` válido. Marcar como `(no instalado)` los que no existen:

| Plugin | Slug | Ruta de config global |
|--------|------|-----------------------|
| Conectores | conectores-legal-mexico | `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md` |
| Corporativo | corporativo-legal-mexico | `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` |
| Litigación | litigacion-legal-mexico | `~/.claude/plugins/config/claude-for-legal/litigacion-legal-mexico/CLAUDE.md` |
| Propiedad Intelectual | propiedad-intelectual-legal-mexico | `~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md` |
| Laboral | laboral-legal-mexico | `~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/CLAUDE.md` |
| Privacidad | privacidad-legal-mexico | `~/.claude/plugins/config/claude-for-legal/privacidad-legal-mexico/CLAUDE.md` |
| Regulatorio | regulatorio-legal-mexico | `~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/CLAUDE.md` |
| Fiscal | fiscal-legal-mexico | `~/.claude/plugins/config/claude-for-legal/fiscal-legal-mexico/CLAUDE.md` |
| Seguros y Fianzas | seguros-legal-mexico | `~/.claude/plugins/config/claude-for-legal/seguros-legal-mexico/CLAUDE.md` |
| IA y Gobernanza | ia-governanza-legal-mexico | `~/.claude/plugins/config/claude-for-legal/ia-governanza-legal-mexico/CLAUDE.md` |

Para cada CLAUDE.md encontrado, determinar estado:
- No existe → `pendiente`
- Contiene `<!-- SETUP PAUSED AT: -->` → `pausado`
- Contiene `[PLACEHOLDER]` sin pausa → `incompleto`
- Poblado → `configurado`

**Wizard state:** si existe `~/.claude/plugins/config/claude-for-legal/setup-wizard-state.md`, leerlo para detectar el último paso completado. Permite `--from N` entre sesiones.

---

## Paso 1 — Presentación inicial

Mostrar resumen adaptado al estado actual:

> **Configuración de los plugins de derecho mexicano**
>
> Plugins instalados detectados: [lista con estado]
>
> [Si `company-profile.md` no existe]: Capturaré el perfil del despacho una sola vez — todos los plugins lo reusan.
> [Si `company-profile.md` existe]: Ya tienes un perfil de despacho guardado.
>
> Pasos del wizard:
> 1. **Perfil del despacho** — nombre, tipo, ciudad, headcount [estado]
> 2. **Perfil de cliente** — tipos de clientes, industrias, tamaño de asuntos [estado]
> 3. **Selección de áreas de práctica** — elegir qué plugins configurar [estado]
> 4. **Conectores** — verificar MCPs disponibles [estado]
> 5. **Configuración por área** — cold-start de cada plugin seleccionado [estado]
> 6. **Agentes** — revisar qué agentes quedan activos [estado]
> 7. **Directorios de clientes** (opcional) — `--new-client <nombre>` [estado]
> 8. **Resumen** [pendiente]
>
> Tiempo estimado: ~5 min rápido, ~30 min completo. Di "pausa" en cualquier momento para guardar progreso.
>
> ¿Arrancamos?

Esperar confirmación.

---

## Paso 2 — Perfil del despacho / empresa

Si `company-profile.md` ya existe y no es `--redo`: mostrar resumen y preguntar si desea actualizarlo.

Si no existe o `--redo`:

Preguntar:
1. Nombre del despacho o empresa
2. Tipo: despacho externo / área legal interna / consultor independiente / despacho boutique
3. Ciudad(es) principal(es) de práctica
4. Headcount aproximado del equipo legal (1-5 / 6-20 / 21-50 / 50+)
5. Industria principal de los clientes (si área legal interna: industria propia)
6. ¿Opera en múltiples jurisdicciones estatales? Si sí, ¿cuáles?

Escribir `~/.claude/plugins/config/claude-for-legal/company-profile.md` con los datos capturados. (O `.claude-legal/company-profile.md` si `--local`.)

Confirmar:
> ✓ **Perfil del despacho guardado.** Todos los plugins lo leerán automáticamente.

---

## Paso 3 — Perfil de cliente

Preguntar:
1. Tipos de cliente principales: persona moral / persona física / gobierno / startup / multinacional / mixto
2. Tamaño típico de asunto: <$500k / $500k-$5M / $5M-$50M / >$50M MXN en litigio o valor de transacción
3. ¿Clientes con operaciones internacionales? ¿Principales países?
4. ¿Sectores clave de los clientes? (fintech, salud, manufactura, retail, energía, tecnología, otro)

Guardar en `company-profile.md` bajo sección `## Perfil de cliente`. Confirmar.

---

## Paso 4 — Selección de áreas de práctica

Mostrar menú de selección. Marcar `(no instalado)` los plugins que no están presentes en el sistema:

> **¿Qué áreas de práctica quieres configurar ahora?**
> Selecciona todas las que aplican (puedes agregar más después con `--from <plugin>`):
>
> [ ] **Corporativo** — F&A, Consejo de Administración, Administración de Entidades
> [ ] **Litigación** — Juicio Ordinario/Ejecutivo Mercantil, Amparo, etapa probatoria
> [ ] **Propiedad Intelectual** — marcas, patentes, derechos de autor, OSS
> [ ] **Laboral** — LFT, liquidación, CJFCA, NOM-035/037, IMSS/INFONAVIT
> [ ] **Privacidad** — LGPDPPSP/LFPDPPP, avisos, ARCO, INAI, EIPDs
> [ ] **Regulatorio** — COFECE, CNBV, COFEPRIS, IFT, DOF, CONAMER
> [ ] **Fiscal** — SAT, CFDI 4.0, auditorías, TFJA, PRODECON
> [ ] **Seguros y Fianzas** — LCS, LISF, CNSF, siniestros, reaseguro, CONDUSEF
> [ ] **IA y Gobernanza** — EU AI Act, riesgo IA, políticas, contratos IA
>
> (Los plugins marcados `(no instalado)` requieren instalación previa — puedes configurarlos ahora, pero los skills no estarán disponibles hasta instalarlos.)

Guardar selección. Confirmar: "Configurando: [lista]. ¿Correcto?"

---

## Paso 5 — Conectores

Si `$est_conectores == configurado` y no `--redo`: mostrar ✓ y saltar.

Si no:
> **[Conectores] — verificando conectividad MCP**
> Verifico que los MCPs estén respondiendo antes de que los otros plugins los necesiten.

Ejecutar la entrevista completa de `/conectores-legal-mexico:cold-start-interview`, siguiendo todas sus instrucciones. Al terminar:
> ✓ **Conectores configurado.**

---

## Paso 6 — Configuración por área de práctica

Para cada plugin seleccionado en el Paso 4, en este orden: corporativo → litigacion → propiedad-intelectual → laboral → privacidad → regulatorio → fiscal → seguros → ia-governanza:

Si ya está `configurado` y no `--redo`:
> ✓ **[Plugin] ya configurado.** Saltando.

Si `pendiente`, `pausado` o `incompleto`:

Anunciar:
> **[[N]/[total seleccionados]] [Nombre del plugin]**
> [Si `company-profile.md` existe]: Perfil del despacho ya guardado — lo salto.

Ejecutar la entrevista completa de `/<plugin-slug>:cold-start-interview`, siguiendo todas sus instrucciones (incluyendo la lógica de `company-profile.md`). Al terminar:
> ✓ **[Plugin] configurado.** [Avanzando al siguiente... / Último plugin configurado.]

Guardar progreso en `setup-wizard-state.md` después de cada plugin completado.

---

## Paso 6 (alternativo) — `--check-integrations`

Cuando se invoca con `--check-integrations`:

1. Ejecutar `--check-integrations` en cada plugin instalado.
2. Mostrar tabla resumen:

> **Estado de integraciones — todos los plugins**
>
> | Integración | Conectores | Corp. | Lit. | PI | Laboral | Privacidad | Regulatorio | Fiscal | Seguros | IA |
> |---|---|---|---|---|---|---|---|---|---|---|
> | LegalDataHunter | [✓/✗/⚪] | ... | | | | | | | | |
> | CJJ Boletín | [✓/✗/⚪] | — | [✓/✗/⚪] | — | — | — | — | — | — | — |
> | MXLegal (STJJ) | [✓/✗/⚪] | — | [✓/✗/⚪] | — | — | — | — | — | — | — |
> | Solve Intelligence | [✓/✗/⚪] | — | — | [✓/✗/⚪] | — | — | — | — | — | — |
> | Slack | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] | [✓/✗/⚪] |
> | Google Drive / Box | [✓/✗/⚪] | ... | | | | | | | | |

---

## Paso 7 — Agentes

Mostrar qué agentes quedan activos según los plugins configurados:

> **Agentes activos con tu configuración actual:**
>
> | Agente | Plugin | Estado |
> |--------|--------|--------|
> | vigilante-expedientes | litigacion-legal-mexico | [activo/inactivo] |
> | vigilante-renovaciones | propiedad-intelectual-legal-mexico | [activo/inactivo] |
> | dataroom-watcher | corporativo-legal-mexico | [activo/inactivo] |
> | vigilante-plazos-laborales | laboral-legal-mexico | [activo/inactivo] |
> | monitor-dof | regulatorio-legal-mexico | [activo/inactivo] |
>
> Para activar los agentes, deben estar configurados como agentes programados en tu entorno de Claude Code.

Si algún agente requiere canal de Slack y el canal no está configurado en el perfil, preguntar una sola vez: "¿Canal de Slack para alertas de agentes? (puede ser el mismo para todos)"

---

## Paso 8 — Directorio de cliente (--new-client)

Si se invocó con `--new-client <nombre>` o el usuario quiere crear un directorio aislado:

1. Crear `./<nombre>/` en el directorio actual.
2. Agregar `.claude-legal/` al `.gitignore` local si no está ya.
3. Notificar: "Creando directorio de cliente `<nombre>/`. Ahora re-ejecuto el wizard con `--local` para escribir la config de este cliente en `<nombre>/.claude-legal/`."
4. Re-ejecutar Pasos 2-6 con `--local --cwd ./<nombre>/`.
5. Al terminar, mostrar: "Config de cliente `<nombre>` escrita en `./<nombre>/.claude-legal/`. Desde esa carpeta, todos los skills usan este perfil."

Sin `--new-client`: preguntar opcionalemente: "¿Quieres crear un directorio aislado para un cliente específico ahora? (`--new-client <nombre>`)"

---

## Paso 9 — Resumen final

> **✓ Configuración completa**
>
> | Plugin | Estado | Ruta |
> |--------|--------|------|
> | Conectores | ✓ Activo | `~/.claude/plugins/config/claude-for-legal/conectores-legal-mexico/CLAUDE.md` |
> | [Cada plugin configurado...] | ✓ Activo | [ruta] |
> | [Plugins no seleccionados] | — No configurado | — |
>
> **Perfil compartido:** `~/.claude/plugins/config/claude-for-legal/company-profile.md`
>
> **Para empezar:**
> - `/litigacion-legal-mexico:matter-intake` — admitir un asunto
> - `/corporativo-legal-mexico:closing-checklist` — checklist de cierre
> - `/laboral-legal-mexico:termination-risk` — análisis de riesgo de terminación
> - `/privacidad-legal-mexico:aviso-privacidad` — redactar aviso de privacidad
> - `/regulatorio-legal-mexico:dof-digest` — novedades DOF
> - `/fiscal-legal-mexico:cfdi-review` — revisar un CFDI
> - `/seguros-legal-mexico:poliza-review` — revisar una póliza de seguros
> - `/ia-governanza-legal-mexico:use-case-triage` — clasificar un caso de uso de IA
>
> **Para reconfigurar:**
> - `/conectores-legal-mexico:setup-completo --redo` — todo de nuevo
> - `/conectores-legal-mexico:setup-completo --from <plugin>` — desde un plugin
> - `/conectores-legal-mexico:setup-completo --check-integrations` — solo conectividad
> - `/conectores-legal-mexico:setup-completo --new-client <nombre>` — nuevo cliente

---

## Banderas

| Bandera | Comportamiento |
|---------|----------------|
| *(ninguna)* | Configurar solo los plugins no configurados, en el orden del wizard. |
| `--redo` | Re-ejecutar todo. Mostrar diff antes de sobrescribir cada CLAUDE.md. |
| `--from <N>` | Re-ejecutar desde el paso N. |
| `--from <plugin-slug>` | Re-ejecutar desde ese plugin en el Paso 6. |
| `--check-integrations` | Re-verificar conectividad en todos los plugins instalados, sin re-entrevistar. |
| `--local` | Escribir todo en `.claude-legal/` del directorio actual. |
| `--new-client <nombre>` | Crear `<nombre>/`, re-ejecutar el wizard con `--local` en esa carpeta. |

---

## Manejo de pausas

Si el usuario dice "pausa", "alto" o "déjame volver":
1. Terminar el plugin en curso escribiendo config parcial con `<!-- SETUP PAUSED AT: [sección] -->`.
2. Actualizar `setup-wizard-state.md` con el último paso completado.
3. Mostrar:
   > **Progreso guardado.** Para continuar:
   > `/conectores-legal-mexico:setup-completo --from <paso-donde-pausaste>`
4. No continuar con los plugins siguientes.
