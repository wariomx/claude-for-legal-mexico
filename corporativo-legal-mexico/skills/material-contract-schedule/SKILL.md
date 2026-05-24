---
name: material-contract-schedule
description: >
  Construir el anexo de revelaciones de contratos relevantes a partir de
  hallazgos de debida diligencia, aplicando la definición de Contrato Relevante
  del contrato de compraventa de acciones y formateando conforme al formato de
  anexos del contrato. Usar cuando el usuario diga "construir el anexo de
  contratos", "anexo de revelaciones", "anexo 3.X", "lista de contratos
  relevantes", o al redactar anexos de revelaciones.
argument-hint: "[ruta del contrato de compraventa de acciones, o pegar la definición de Contrato Relevante]"
---

# /material-contract-schedule

1. Cargar el contrato de compraventa de acciones → definición de Contrato Relevante + formato de anexo.
2. Usar el flujo de trabajo descrito abajo.
3. Aplicar la definición a los hallazgos de debida diligencia. Señalar casos límite.
4. Formatear conforme al contrato. El overlay de consentimientos alimenta el checklist de cierre.

---

## Contexto del asunto

**Contexto del asunto.** Revisar `## Espacios de trabajo por asunto` en el CLAUDE.md a nivel práctica. Si `Enabled` es `✗` (el valor predeterminado para usuarios in-house), omitir el resto de este párrafo — las habilidades usan el contexto a nivel práctica y la maquinaria de asuntos es invisible. Si está habilitado y no hay un asunto activo, preguntar: "¿Para qué asunto es esto? Ejecuta `/corporativo-legal-mexico:matter-workspace switch <slug>` o di `practice-level`." Cargar el `matter.md` del asunto activo para contexto específico del asunto y modificaciones. Escribir las salidas en la carpeta del asunto en `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/matters/<matter-slug>/`. Nunca leer archivos de otro asunto a menos que `Cross-matter context` esté en `on`.

---

## Propósito

El contrato de compraventa de acciones tiene una declaración: "El Anexo 3.X lista todos los Contratos Relevantes." Esta habilidad construye ese anexo a partir de los hallazgos de debida diligencia — qué contratos son relevantes conforme a la definición del contrato, en el formato que el contrato requiere.

## Cargar contexto

- Borrador del contrato de compraventa de acciones — para la definición de "Contrato Relevante" y el formato del anexo
- `~/.claude/plugins/config/claude-for-legal/corporativo-legal-mexico/CLAUDE.md` → umbrales de materialidad (pueden diferir de la definición del contrato — usar la del contrato)
- Hallazgos de debida diligencia de diligence-issue-extraction — datos a nivel contrato

## Flujo de trabajo

### Paso 1: Obtener la definición

Extraer la definición de "Contrato Relevante" del contrato de compraventa de acciones — la definición del CCA controla. Las diferencias en la estructura de la operación (compraventa de acciones vs. compraventa de activos vs. fusión) pueden cambiar cómo se interpreta un criterio, y las capas de regulación por industria (salud, defensa, servicios financieros, telecomunicaciones, contratos con el gobierno) pueden agregar requisitos de consentimiento que viven fuera del CCA. Si la operación involucra alguna de esas capas, investigar las reglas aplicables de anti-cesión o novación (por ejemplo, contratos con el gobierno federal bajo la Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público; reguladores sectoriales como CNBV, CRE, IFT, COFEPRIS) y citar la regla aplicable.

Categorías comunes de criterios a buscar en la definición del CCA — estas no sustituyen la lectura del CCA, y la lista que el CCA use es la que controla:

- Umbral de valor en dólares o pesos (anual o acumulado)
- Duración del contrato
- Cláusula de cambio de control o restricción de cesión
- Exclusividad o cláusula de no competencia
- Contratos con los N principales clientes o proveedores
- Arrendamiento de bienes inmuebles
- Licencias de propiedad intelectual (entrantes y salientes)
- Contratos con partes relacionadas
- Contratos con el gobierno (Ley de Adquisiciones, Ley de Obras Públicas)
- Contratos fuera del curso ordinario de negocios

La definición del CCA es la prueba. Aplicarla mecánicamente — todo contrato que cumpla cualquier criterio de la definición del CCA va en el anexo.

### Paso 2: Aplicar la definición a los hallazgos

Para cada contrato revisado en la debida diligencia:

| Contrato | Cumple criterio(s) | Incluir |
|---|---|---|
| [nombre] | [$X+ valor anual; cláusula de cambio de control] | Sí |
| [nombre] | [ninguno] | No |

**Casos límite a señalar para decisión humana:**
- Contrato con valor de $X-1 (justo debajo del umbral) pero importante para el negocio
- Contrato que cumple un criterio pero será terminado de todos modos
- Acuerdos verbales o cartas complementarias que pueden o no contar

### Paso 3: Reunir datos del anexo

Para cada contrato incluido, el anexo típicamente requiere:

| Campo | Fuente |
|---|---|
| Nombre de la contraparte | Contrato |
| Título/tipo de contrato | Contrato |
| Fecha | Contrato |
| Vigencia / vencimiento | Contrato |
| Valor anual/total | Contrato o datos de la administración |
| Qué criterio de materialidad cumple | Análisis del Paso 2 |
| Consentimiento requerido para la operación | Hallazgo de debida diligencia |
| Referencia VDR | Inventario de debida diligencia |

Extraer de las extracciones de debida diligencia existentes. Si falta un campo, señalarlo — no adivinar.

### Paso 4: Formatear conforme al contrato

Los anexos de revelaciones tienen un formato — usualmente una lista numerada o una tabla, a veces con sub-partes por tipo de contrato. Igualar el formato de los otros anexos en el borrador del contrato.

```markdown
## Anexo 3.[X] — Contratos Relevantes

Los siguientes son los Contratos Relevantes a la fecha del presente:

### (a) Contratos con Clientes

1. [Título del Contrato], de fecha [fecha], entre [Target] y [Contraparte].
   [Descripción breve si el formato lo requiere.]
   [VDR: ruta]

2. [...]

### (b) Contratos con Proveedores

[...]

### (c) Bienes Inmuebles

[...]

[etc. — sub-partes conforme a la estructura de la definición del contrato]
```

### Paso 5: Overlay de seguimiento de consentimientos

Por separado (no en el anexo mismo — esto es interno), dar seguimiento a cuáles contratos del anexo requieren consentimiento.

> El overlay de consentimientos y cualquier borrador de trabajo del anexo previo a su entrega se derivan de materiales de debida diligencia protegidos por secreto profesional y/o confidencialidad. Heredan su estatus de protección — la distribución fuera del círculo de confidencialidad puede comprometer dicha protección. El anexo en sí, una vez entregado como exhibición del CCA ejecutado, es un documento de la operación y no está protegido; eliminar cualquier anotación interna antes de la entrega.

| Anexo # | Contraparte | Consentimiento requerido | Estatus | Responsable | Vencimiento |
|---|---|---|---|---|---|
| 3.X(a)(1) | [nombre] | Sí — Cambio de control §12.2 | Solicitado | [nombre] | [fecha] |

Esto alimenta closing-checklist.

## Verificación cruzada

Antes de entregar:

- Todo contrato que cumplió un criterio está en el anexo (completitud)
- Ningún contrato está en el anexo que no cumpla un criterio (sin sobre-revelación — es una declaración, no un vaciado de datos)
- El anexo es consistente con las demás declaraciones (un contrato en el Anexo 3.X que crea un gravamen también debería estar en el anexo de gravámenes)
- Cada entrada tiene una cita al VDR para que los abogados del comprador puedan localizar el documento subyacente

## Handoffs

- **Desde diligence-issue-extraction:** Los hallazgos a nivel contrato son el insumo.
- **Hacia closing-checklist:** Los elementos de consentimiento van al checklist.

## Lo que esta habilidad no hace

- No decide la definición de materialidad — esa está en el contrato de compraventa de acciones.
- No obtiene consentimientos — da seguimiento a cuáles se necesitan.
- No redacta la declaración — llena el anexo al que la declaración hace referencia.
