# seguros-legal-mexico

Plugin de Claude Code para práctica de seguros y fianzas en México — LCS, LISF, CNSF y CONDUSEF.

## Skills

| Skill | Descripción |
|---|---|
| `/seguros-legal-mexico:cold-start-interview` | Entrevista de configuración inicial — construye el perfil de práctica de seguros |
| `/seguros-legal-mexico:customize` | Ajusta secciones del perfil de práctica sin re-ejecutar la entrevista completa |
| `/seguros-legal-mexico:poliza-review` | Revisa una póliza conforme a la LCS — carátula, condiciones generales, exclusiones y endosos |
| `/seguros-legal-mexico:siniestro-intake` | Triaje de siniestro: cobertura aplicable, plazos fatales LCS Art. 66, aviso a aseguradora |
| `/seguros-legal-mexico:cobertura-analysis` | Analiza cobertura vs. exclusiones para un riesgo o siniestro específico |
| `/seguros-legal-mexico:cnsf-compliance` | Análisis de brecha regulatoria CNSF para operadores (LISF): gobierno corporativo, capital y PLD |
| `/seguros-legal-mexico:solvencia-rcs` | Análisis del Requerimiento de Capital de Solvencia (RCS) — Solvencia II mexicano bajo LISF |
| `/seguros-legal-mexico:reaseguro-review` | Revisa contratos de reaseguro: proporcional, no proporcional, retención, exclusiones |
| `/seguros-legal-mexico:recurso-condusef` | Gestiona queja, conciliación y arbitraje ante CONDUSEF por disputas con aseguradoras |
| `/seguros-legal-mexico:producto-filing` | Prepara el expediente de registro de producto ante la CNSF: nota técnica, condiciones generales, tarifas |

## Instalación

```bash
claude plugin install seguros-legal-mexico
```

Después de instalar, ejecuta la entrevista de configuración:

```
/seguros-legal-mexico:cold-start-interview
```

## Dependencias

- `conectores-legal-mexico` — servidores MCP para DOF, SCJN IUS y Semanario Judicial

## Autor

Softlaw S.A. de C.V. — wario@soft.law
