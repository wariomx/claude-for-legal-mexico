---
name: customize
description: >
  Ajusta secciones específicas del perfil de práctica laboral sin re-ejecutar
  la entrevista completa. Úsalo para actualizar parámetros de cálculo, cambiar
  documentos semilla, activar un nuevo módulo, o corregir datos después de
  una restructuración o cambio de política.
argument-hint: "[nombre de sección o módulo a ajustar]"
---

# /customize

## Secciones ajustables

El perfil de práctica de `laboral-legal-mexico` tiene las siguientes secciones personalizables:

1. **Perfil de empresa** — nombre, industria, tamaño, jurisdicción (edita en `company-profile.md` para que cambie en todos los plugins)
2. **Quién usa este plugin** — rol del usuario, contacto de abogado
3. **Integraciones disponibles** — estado de conexiones MCP (preferir `--check-integrations` para re-verificar automáticamente)
4. **Módulos activos** — activar o desactivar módulos; ajustar parámetros dentro de cada módulo
5. **Terminación y Liquidación** — tipo de terminaciones, parámetros de salario integrado, documentos semilla
6. **Conciliación CJFCA** — centro de conciliación, representante, postura, documentos semilla
7. **NOM-035/037-STPS** — estatus de cumplimiento, fechas de aplicación, políticas
8. **IMSS/INFONAVIT** — números de registro, prima de riesgo, responsable, alertas
9. **Contratación y Onboarding** — tipos de contrato, REPSE, documentos semilla
10. **Plataformas Digitales** — modalidad, seguro, IMSS 3A

## Cómo funciona

1. **Leer la configuración activa.** Verificar la ruta activa en el orden de resolución:
   a. `.claude-legal/laboral-legal-mexico/CLAUDE.md` (local, si existe)
   b. `~/.claude/plugins/config/claude-for-legal/laboral-legal-mexico/CLAUDE.md` (global)
   Si ninguna existe o tiene `[PLACEHOLDER]`, redirigir: "Tu práctica no está configurada todavía — ejecuta `/laboral-legal-mexico:cold-start-interview` primero."

2. **Identificar la sección.** Si el usuario especificó una sección o módulo como argumento, ir directo a esa sección. Si no, mostrar la lista de secciones ajustables y preguntar cuál quiere modificar.

3. **Hacer cambios dirigidos.** Preguntar solo lo necesario para la sección a ajustar. No re-preguntar campos que ya están llenos y que el usuario no quiere cambiar.

4. **Actualizar el archivo.** Escribir solo la sección modificada. Confirmar antes de escribir.

5. **Confirmar.** Decir qué cambió y en qué ruta se escribió.

## Salvaguardas

- **No borrar módulos activos** sin confirmar explícitamente con el usuario.
- **No sobrescribir documentos semilla** sin verificar que el usuario realmente quiere reemplazarlos.
- **No tocar `company-profile.md`** desde este skill — redirigir al usuario si quiere cambiar datos de empresa.
- Si el cambio afecta un cálculo activo (p. ej., cambiar el salario integrado base), advertir: "Este cambio afectará cálculos de liquidación futuros. Los cálculos anteriores en el registro de asuntos no se retroactúan. ¿Confirmas?"

---

*Esto no es recomendación legal ni consultoría jurídica. La inteligencia artificial no sustituye la inteligencia humana. En caso de un problema legal, consulta a tu abogado de confianza. Para servicios de automatización legaltech o uso comercial de esta tecnología, escribe a wario@soft.law*
