# laboral-legal-mexico

Plugin de Claude Code para práctica laboral bajo la Ley Federal del Trabajo (LFT) en México.

## Skills

| Skill | Descripción |
|---|---|
| `/laboral-legal-mexico:cold-start-interview` | Entrevista de configuración inicial — construye el perfil de práctica laboral |
| `/laboral-legal-mexico:customize` | Ajusta secciones del perfil de práctica sin re-ejecutar la entrevista completa |
| `/laboral-legal-mexico:matter-intake` | Abre un nuevo asunto laboral y captura hechos clave, partes y pretensiones |
| `/laboral-legal-mexico:termination-risk` | Evalúa el riesgo de una terminación individual o colectiva bajo la LFT |
| `/laboral-legal-mexico:liquidacion-calculator` | Calcula indemnización constitucional, prima de antigüedad y conceptos de liquidación |
| `/laboral-legal-mexico:cjfca-conciliacion` | Prepara escritos y estrategia para la etapa prejudicial ante el CJFCA |
| `/laboral-legal-mexico:nom-compliance` | Audita brechas de cumplimiento NOM-035/037-STPS y genera plan de acción |
| `/laboral-legal-mexico:escrito-laboral` | Redacta escritos procesales (contestación, excepciones, ofrecimiento de pruebas) |

## Agente

| Agente | Descripción |
|---|---|
| `vigilante-plazos-laborales` | Vigila plazos procesales y de cumplimiento del portafolio de asuntos laborales activos |

## Instalación

```bash
claude plugin install laboral-legal-mexico
```

Después de instalar, ejecuta la entrevista de configuración:

```
/laboral-legal-mexico:cold-start-interview
```

## Dependencias

- `conectores-legal-mexico` — servidores MCP para DOF, SCJN IUS y Semanario Judicial

## Autor

Softlaw S.A. de C.V. — wario@soft.law
