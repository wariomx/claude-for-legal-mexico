# propiedad-intelectual-legal-mexico

Plugin de Claude Code para la práctica de **propiedad intelectual bajo derecho
mexicano**. Adaptado del plugin `ip-legal` (derecho estadounidense) al sistema
legal mexicano, con cobertura dual de propiedad industrial (IMPI / LFPPI) y
derechos de autor (INDAUTOR / LFDA).

## Marco institucional

| Institución | Materia | Ley base |
|---|---|---|
| **IMPI** | Propiedad industrial: marcas, patentes, modelos de utilidad, diseños industriales, secretos industriales, avisos comerciales, denominaciones de origen | LFPPI |
| **INDAUTOR** | Derechos de autor, derechos conexos, reservas de derechos al uso exclusivo | LFDA |

## Instalación

```bash
claude plugin install ./propiedad-intelectual-legal-mexico
```

Después de instalar, ejecutar la entrevista de configuración:

```
/propiedad-intelectual-legal-mexico:cold-start-interview
```

La entrevista toma ~10-15 minutos y configura el perfil de práctica, portafolio
e integraciones. Todos los skills dependen de esta configuración.

## Skills (13)

| Skill | Descripción | Ámbito |
|---|---|---|
| `carta-requerimiento` | Redacta cartas de requerimiento (cease & desist) y cartas amigables por infracción | IMPI + LFDA |
| `clearance` | Búsqueda de disponibilidad y evaluación de riesgo de confusión para marcas | IMPI |
| `cold-start-interview` | Configura el plugin con perfil de práctica y portafolio | Ambos |
| `customize` | Ajusta configuración post-entrevista | Ambos |
| `fto-triage` | Evaluación de libertad de operación (Freedom to Operate) | IMPI |
| `invention-intake` | Evalúa invenciones para patentabilidad y rutas de protección | IMPI + LFT |
| `matter-workspace` | Crea y gestiona espacios de trabajo por asunto | Ambos |
| `notificacion-infraccion` | Notificaciones de infracción a ISPs, plataformas y mercados en línea | LFDA + IMPI |
| `oss-review` | Revisión de cumplimiento de licencias de código abierto | LFDA |
| `portafolio` | Gestión del portafolio de PI — registros, renovaciones, estatus | IMPI + INDAUTOR |
| `reservas-derechos` | Búsqueda, solicitud y seguimiento de reservas de derechos ante INDAUTOR | INDAUTOR |
| `revision-clausulas-pi` | Revisa cláusulas de PI en contratos — cesión, licencia, obra por encargo | LFDA + LFPPI |
| `triaje-infraccion` | Clasifica y evalúa situaciones de infracción — riesgo, vías de acción | IMPI + LFDA |

## Agentes (1)

| Agente | Descripción |
|---|---|
| `vigilante-renovaciones` | Monitoreo semanal de vencimientos del portafolio — marcas (10 años + declaración de uso a 3 años), patentes (anualidades), diseños industriales (quinquenios), reservas de derechos (INDAUTOR) |

## Enrutamiento entre plugins

Este plugin se integra con otros plugins de la familia `-legal-mexico`:

- **`litigacion-legal-mexico:claim-chart`** — cuando una infracción requiere
  chart de elementos para litigio
- **`corporativo-legal-mexico:revision-contratos`** — cuando una cláusula de PI
  está en un contrato comercial más amplio

## Conectores (MCP Servers)

| Servidor | Uso |
|---|---|
| Solve Intelligence | Búsqueda de patentes, arte previo, análisis de reivindicaciones |
| LegalDataHunter | Búsqueda agregada de documentos jurídicos mexicanos (16M+ docs — SCJN, DOF, IMPI, INDAUTOR) |
| Slack | Comunicación del equipo, alertas de renovación |
| Google Drive | Almacenamiento de documentos |
| Box | Almacenamiento de documentos |
| iManage | Gestión documental |
| Definely | Análisis de contratos y documentos |

## Herramientas de práctica IMPI

Estas son herramientas del practicante referenciadas en los skills (NO son
servidores MCP):

- **Marcanet** — Búsqueda de marcas registradas y en trámite
- **MARCia** — Sistema de consulta de marcas del IMPI
- **VIDOC** — Visor de documentos y expedientes
- **SIGA** — Sistema Integral de Gestión de Asuntos

## Reglas clave

1. **Derechos morales (LFDA Art. 19):** perpetuos, inalienables, irrenunciables
   para todas las obras. Cualquier cláusula que pretenda cederlos es nula.
2. **Secreto profesional:** solo abogados titulados con cédula gozan de
   privilegio. No existe "patent agent privilege" en México.
3. **Reforma LFPPI 2026:** patentes provisionales, nuevos tipos de marca
   (posición, movimiento, multimedia), protección anti-ambush marketing.
4. **Inventos de empleados (LFT Art. 163):** clasificación tripartita
   (empresa/trabajador/libre) que determina titularidad.
5. **Sin DMCA:** México no tiene DMCA. La vía de notificación a ISPs es
   limitada (LFDA Art. 231 bis, reforma T-MEC).

## Configuración

La configuración del usuario se almacena en:
```
~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/CLAUDE.md
```

El portafolio de PI se almacena en:
```
~/.claude/plugins/config/claude-for-legal/propiedad-intelectual-legal-mexico/portfolio.yaml
```

## Autor

Anthropic (adaptado para México)
