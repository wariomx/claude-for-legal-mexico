---
description: >
  Entrevista de configuración inicial para el plugin laboral-legal-mexico.
  Construye el perfil de práctica laboral (módulos activos, parámetros de
  cálculo, postura de conciliación, documentos semilla) y lo escribe en
  ~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/CLAUDE.md.
  Usar --local para crear un perfil aislado por cliente en
  .claude-legal/laboral-legal-mexico/CLAUDE.md. Usar --check-integrations
  para re-verificar conexiones MCP sin re-hacer la entrevista. Usar --redo
  para re-ejecutar la entrevista completa. Usar --module para agregar un
  módulo individual sin re-configurar toda la práctica.
argument-hint: "[--local] [--check-integrations] [--redo] [--module <nombre>]"
---

## Bandera --local

Si el usuario ejecuta `/laboral-legal-mexico:cold-start-interview --local`, escribir el perfil en `.claude-legal/laboral-legal-mexico/CLAUDE.md` en el directorio de trabajo actual (perfil por cliente/proyecto). Recordarle que agregue `.claude-legal/` a `.gitignore` — contiene datos del cliente que no deben versionarse.

# /cold-start-interview

## Instrucciones

1. **Leer el perfil existente primero.** Antes de hacer la primera pregunta, verificar si ya existe un CLAUDE.md configurado en la ruta activa (local o global). Si existe y no tiene `[PLACEHOLDER]`, decir: "Ya tienes un perfil configurado. ¿Quieres re-ejecutar la entrevista completa (`--redo`), agregar un módulo (`--module <nombre>`), o ajustar secciones específicas (`/laboral-legal-mexico:customize`)?" Detener aquí y esperar respuesta.

2. **Verificar el perfil de empresa.** Leer `~/.claude/plugins/config/claude-for-legal/company-profile.md` (o `.claude-legal/company-profile.md` si `--local`). Si no existe, incluir las preguntas de empresa en la Parte 0. Si existe, mostrar un resumen de 3 líneas y preguntar si los datos son correctos para esta práctica laboral antes de continuar.

3. **Presentar la entrevista en partes.** No hacer todas las preguntas a la vez. Completar cada parte, confirmar, y avanzar. Permitir que el usuario responda varias preguntas en un solo mensaje; inferir las respuestas de forma natural.

4. **Inferir donde sea posible.** Si el usuario dice "somos una empresa de tecnología con 200 empleados en CDMX", inferir que aplican NOM-035 Fase 2 y NOM-037 si hay teletrabajadores, y que la jurisdicción principal es CDMX. Confirmar la inferencia en vez de preguntar lo obvio.

5. **Detectar y cargar documentos semilla.** Si el usuario menciona que tiene contratos tipo, convenios de terminación o escritos anteriores, pedirle que los suba o pegue. Extraer formato, lenguaje de resolución y estructura — no inventarlos.

6. **Verificar integraciones MCP.** Al final de la entrevista, intentar conectar cada MCP configurado en `.mcp.json` y reportar estado. Para integraciones no disponibles, registrar la alternativa manual en el perfil.

7. **Escribir el perfil.** Escribir el CLAUDE.md completado en la ruta activa. Usar la plantilla de `laboral-legal-mexico/CLAUDE.md` como estructura base, rellenando todos los `[PLACEHOLDER]` con las respuestas de la entrevista. Omitir secciones de módulos que el usuario no activó. Confirmar la ruta de escritura antes de escribir.

## --check-integrations

Si el usuario ejecuta `--check-integrations`: probar cada MCP de `.mcp.json` y reportar estado actual. Actualizar solo la sección `## Integraciones disponibles` del CLAUDE.md activo. No re-hacer la entrevista.

## Propósito

El perfil de práctica es el único insumo que hace que este plugin sea tuyo. Sin él, todos los skills producen resultados genéricos que no corresponden a tu práctica, tus documentos semilla, tu postura de riesgo ni tu cadena de escalamiento. La entrevista toma entre 10 y 15 minutos; los skills que la usan toman segundos en vez de minutos.

## Parte 0 — Empresa (si company-profile.md no existe)

- ¿Cuál es el nombre legal de la entidad? ¿Cuál es su industria o sector?
- ¿Cuántos trabajadores tiene? ¿En cuántos estados opera?
- ¿La empresa es privada, pública (BMV), o subsidiaria de empresa pública?
- ¿Cuál es la jurisdicción principal donde están los trabajadores?

## Parte 1 — Perfil de práctica

- ¿Cuál es tu rol? (Abogado titulado / profesional jurídico | No abogado con acceso a asesor | No abogado sin asesor)
- ¿Cómo describes tu tipo de práctica? (Despacho solo/pequeño | Despacho mediano/grande | Jurídico interno | Gobierno/clínica)
- ¿Tienes despacho externo de laboral? ¿Cuándo lo involucras?
- ¿Cuál es tu umbral para escalar un asunto laboral al Director Jurídico o al Director General?

## Parte 2 — Módulos a activar

Presentar la lista de módulos disponibles y preguntar cuáles aplican:

1. **Terminación y Liquidación** — cálculos de liquidación, convenios, cartas de rescisión
2. **Conciliación CJFCA** — etapa prejudicial obligatoria, escritos de comparecencia
3. **NOM-035/037-STPS** — cumplimiento de normas de factores psicosociales y teletrabajo
4. **IMSS/INFONAVIT** — gestión de obligaciones de seguridad social
5. **Contratación y Onboarding** — contratos, avisos de privacidad, reglamento interior
6. **Plataformas Digitales** — trabajadores de aplicaciones (reforma 2021)

El usuario puede activar todos o solo los que aplican. Para cada módulo activado, hacer las preguntas específicas de la parte correspondiente.

## Parte 3 — Terminación y Liquidación (si se activó)

- ¿Cuál es el tipo de terminaciones más frecuente? (sin causa / con causa / rescisión por trabajador / colectiva)
- ¿Usan período de prueba (Art. 39-A LFT)? ¿Para qué puestos?
- ¿El cálculo de liquidación usa salario diario ordinario o salario diario integrado?
- ¿Qué componentes variables se integran al salario? (comisiones, bonos, ayudas, etc.)
- ¿Tienes un convenio de terminación tipo? ¿Puedes subirlo?
- ¿Los convenios se ratifican ante el Tribunal Laboral (Art. 33 LFT)?

## Parte 4 — Conciliación CJFCA (si se activó)

- ¿Ante cuál Centro de Conciliación compareces habitualmente? (CJFCA federal / centro estatal)
- ¿Quién representa a la empresa en la conciliación?
- ¿Cuál es la postura habitual: buscar acuerdo en primera audiencia o agotar la etapa?
- ¿Tienes un escrito de comparecencia tipo o un convenio de conciliación tipo?

## Parte 5 — NOM-035/037-STPS (si se activó)

- ¿Cuántos trabajadores tiene la empresa? (determina fases NOM-035)
- ¿Qué porcentaje trabaja en modalidad de teletrabajo?
- ¿Ya aplicaron los cuestionarios de factores psicosociales NOM-035?
- ¿Tienen política de prevención de riesgos psicosociales?
- ¿Tienen política y contrato de teletrabajo NOM-037?

## Parte 6 — IMSS/INFONAVIT (si se activó)

- ¿Cuál es el número de registro patronal IMSS? ¿Y el de INFONAVIT?
- ¿Cuál es la clase y prima de riesgo de trabajo actual?
- ¿Quién gestiona los pagos bimestrales IMSS/INFONAVIT? ¿Qué sistema usan?
- ¿Han tenido diferencias o auditorías recientes del IMSS?

## Parte 7 — Contratación y Onboarding (si se activó)

- ¿Qué tipos de contrato usan? (indeterminado / determinado / obra / prueba / capacitación inicial)
- ¿La empresa usa subcontratación de servicios especializados? ¿Tienen registro REPSE?
- ¿Tienes un contrato individual tipo? ¿Puedes subirlo?
- ¿Tienen Reglamento Interior de Trabajo registrado ante la STPS?

## Parte 8 — Plataformas Digitales (si se activó)

- ¿La empresa opera como plataforma digital o contrata a través de una?
- ¿Cuántos trabajadores de plataforma tienen?
- ¿Tienen contratado el seguro de accidentes obligatorio (Art. 291-G LFT)?
- ¿Han iniciado el registro en IMSS bajo la modalidad 3A?

## Escritura del perfil

Después de la entrevista:

1. Rellenar el CLAUDE.md con todas las respuestas.
2. Incluir solo los módulos activados en la sección `## Módulos activos`.
3. Marcar con `[settled — last confirmed 2026-05-24]` los artículos LFT y NOM verificados.
4. Actualizar la fecha en el encabezado: `Generado por cold-start el [FECHA]`.
5. Confirmar la ruta de escritura al usuario antes de escribir.
6. Después de escribir, decir: "Perfil escrito en [ruta]. Puedes ajustar secciones individuales con `/laboral-legal-mexico:customize`. Para abrir el primer asunto, ejecuta `/laboral-legal-mexico:matter-intake`."

## Tono y modos de falla

**Tono:** Conversacional, directo. No usar jerga técnica innecesaria. Si el usuario no sabe la respuesta a una pregunta (p. ej., el número exacto de registro patronal), anotar `[PLACEHOLDER — completar]` y continuar.

**Modos de falla a evitar:**
- No preguntar más de 4-5 preguntas a la vez.
- No inventar documentos semilla — si el usuario no los sube, dejar los campos en `[PLACEHOLDER]`.
- No escribir el perfil antes de confirmar la ruta.
- No re-ejecutar la entrevista si el usuario solo quiere ajustar una sección — redirigir a `/laboral-legal-mexico:customize`.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
