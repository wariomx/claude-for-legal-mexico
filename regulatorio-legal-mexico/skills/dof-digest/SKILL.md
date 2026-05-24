---
description: >
  Extrae del Diario Oficial de la Federación (DOF) las publicaciones relevantes
  para el sector y reguladores configurados en el perfil de práctica. Clasifica
  cada publicación por regulador, tipo de disposición y nivel de impacto.
  Produce un digest estructurado con las publicaciones críticas al inicio,
  un resumen ejecutivo para el cliente, y un archivo YAML de seguimiento.
  Requiere el PDF o texto del DOF, o un conector DOF configurado.
argument-hint: "[fecha o rango de fechas] [--sector nombre] [--regulador nombre]"
---

# Skill: dof-digest (regulatorio-legal-mexico)

## Propósito

El DOF publica cientos de entradas al día. Este skill filtra el ruido: extrae solo las publicaciones que impactan a los sectores y reguladores configurados en el perfil de práctica, las clasifica por nivel de impacto, y produce un digest listo para distribuir al equipo y al cliente.

## Flujo

### Paso 0: leer configuración

Leer el perfil de práctica en la ruta activa. Extraer:
- Sectores monitoreados
- Reguladores activos (módulos habilitados)
- Palabras clave de alerta
- Umbral de relevancia

Si no hay configuración: "Ejecuta `/regulatorio-legal-mexico:cold-start-interview` primero — este skill necesita saber qué sectores y reguladores monitorear."

### Paso 1: obtener el contenido del DOF

**Si hay conector DOF disponible:** usar el MCP para obtener las publicaciones del día o rango de fechas indicado. Registrar en la nota del revisor: `[DOF]`.

**Si no hay conector DOF:** buscar el contenido en la carpeta configurada (`~/.claude/plugins/config/claude-for-legal/regulatorio-legal-mexico/dof/` o `.claude-legal/regulatorio-legal-mexico/dof/`). Si tampoco hay archivos ahí, buscar vía web el índice del DOF para la fecha indicada y pedir al usuario que descargue el PDF relevante.

Si no se puede obtener el contenido del DOF: "No tengo acceso al DOF para la fecha indicada. Opciones: (a) conecta un MCP de DOF, (b) descarga el PDF del DOF desde https://www.dof.gob.mx y deposítalo en la carpeta `dof/`, o (c) pega el texto directamente aquí."

### Paso 2: filtrar publicaciones relevantes

Leer el contenido del DOF y filtrar las publicaciones que:
1. Provienen de los reguladores configurados (COFECE, CNBV, COFEPRIS, IFT, CRE, CONAMER, SHCP, SAT, SE, SADER, SSA, u otros relevantes).
2. Mencionan los sectores monitoreados.
3. Coinciden con las palabras clave de alerta.
4. Son disposiciones de aplicación general (normas, circulares, acuerdos, decretos) — no solo avisos administrativos de baja relevancia.

### Paso 3: clasificar cada publicación

Para cada publicación relevante, asignar:

**Tipo de disposición:**
- Decreto / Reforma legislativa
- Regla / Circular / Acuerdo de carácter general
- NOM (Norma Oficial Mexicana) — proyecto o definitiva
- Resolución administrativa individual (solo si afecta directamente al cliente)
- Convocatoria / licitación
- Acuerdo administrativo de trámite
- Aviso informativo

**Nivel de impacto:**
- 🔴 Crítico — modifica obligaciones, plazos o sanciones que aplican directamente al cliente
- 🟠 Alto — puede aplicar al cliente; requiere análisis antes de determinar impacto
- 🟡 Medio — relevante para el sector pero impacto indirecto
- 🟢 Bajo — informativo; no genera acción inmediata

**Acción requerida:**
- Revisar y actuar antes de [fecha]
- Analizar impacto
- Monitorear implementación
- Archivar como referencia

### Paso 4: producir el digest

```
CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL

⚠️ Nota del revisor
- Fuentes: [DOF verificado ✓ | conector no disponible — procesado desde PDF / texto proporcionado | model knowledge — verify]
- Período cubierto: [fecha o rango]
- Publicaciones revisadas: N total · N relevantes encontradas
- Antes de confiar: [verificar fechas de entrada en vigor y textos completos de las disposiciones marcadas 🔴]

---

**DOF Digest — [fecha]**
**Período:** [fecha inicio] al [fecha fin]

**Resumen ejecutivo**
[2-4 oraciones: cuántas publicaciones relevantes, qué reguladores, qué impactos críticos]

---

🔴 **Crítico — acción requerida**

**[Número de DOF] — [Regulador]**
*[Título de la publicación]*
**Tipo:** [tipo de disposición]
**Publicado:** [fecha]
**Entra en vigor:** [fecha] `[verify]`
**Impacto:** [descripción en 2-3 oraciones del impacto directo en el cliente]
**Acción requerida:** [qué hacer y antes de cuándo]
**Ver:** [URL DOF] `[fuente: DOF | model knowledge — URL no disponible]`

---

🟠 **Alto — analizar antes de [fecha]**

• **[Regulador]** — [título] — [una línea de impacto] — [URL]

---

🟡 **Medio — relevante para el sector**

• **[Regulador]** — [título] — [una línea de relevancia]

---

🟢 **Informativo — archivar**

• [N publicaciones de bajo impacto listadas en una línea cada una]

---

**Archivo de seguimiento:** `dof/seguimiento-[fecha].yaml` (creado automáticamente)

```

### Paso 5: escribir archivo de seguimiento

Crear `dof/seguimiento-[fecha].yaml` en la carpeta de trabajo con estructura:

```yaml
fecha: [AAAA-MM-DD]
periodo_cubierto:
  inicio: [fecha]
  fin: [fecha]
publicaciones:
  - id: [número DOF]
    regulador: [regulador]
    titulo: [título]
    tipo: [tipo]
    impacto: critico|alto|medio|bajo
    entra_vigor: [fecha]
    accion: [descripción]
    url: [URL]
    estado: pendiente|en_analisis|resuelto
```

### Paso 6: árbol de decisión

> **¿Qué sigue?**
> 1. **Analizar una publicación específica** — profundizo en el texto completo y el impacto para tu empresa.
> 2. **Redactar alerta al cliente** — preparo una versión de este digest sin encabezado de confidencialidad y en lenguaje accesible.
> 3. **Preparar comentarios a consulta pública** — si hay NOM o regla en consulta, `/regulatorio-legal-mexico:comentarios-regulatorios` prepara la respuesta.
> 4. **Redactar respuesta a requerimiento** — si alguna publicación genera un requerimiento directo, `/regulatorio-legal-mexico:respuesta-regulador` lo maneja.
> 5. **Archivar y esperar** — el seguimiento queda en el YAML para la siguiente revisión.

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
