# ia-governanza-legal-mexico

Gobernanza legal de inteligencia artificial para organizaciones en México con atención al EU AI Act y el marco mexicano emergente.

## Qué hace este plugin

Este plugin ayuda a equipos jurídicos y de cumplimiento a gestionar las obligaciones legales derivadas del uso de sistemas de inteligencia artificial, con dos marcos regulatorios en paralelo:

- **EU AI Act (Reglamento 2024/1689):** aplica a organizaciones mexicanas con nexo europeo — clientes, empleados, filiales o contratos en la Unión Europea.
- **Marco mexicano de IA:** en 2026 no existe una ley de IA aprobada en México; las obligaciones se derivan de LGPDPPSP, LFPDPPP, LFT Art. 163, COFECE, CCF y LFDA.

**El campo regulatorio está en evolución.** Toda referencia a fechas de aplicación, artículos y guías del EU AI Act requiere verificación contra fuentes primarias. Los skills lo marcan explícitamente.

## Instalación

```
/plugin install ia-governanza-legal-mexico@claude-for-legal-mexico
```

Después de instalar, ejecuta la entrevista de configuración inicial:

```
/ia-governanza-legal-mexico:cold-start-interview
```

## Skills disponibles

| Skill | Qué hace |
|---|---|
| `/ia-governanza-legal-mexico:cold-start-interview` | Configura el plugin con el perfil de práctica de gobernanza de IA de tu organización — inventario de sistemas, nexo europeo, política existente, contratos con proveedores. Primera ejecución obligatoria. |
| `/ia-governanza-legal-mexico:customize` | Ajusta un elemento del perfil de práctica sin volver a ejecutar la entrevista completa — postura de riesgo, responsables, umbrales de triaje, herramientas permitidas. |
| `/ia-governanza-legal-mexico:use-case-triage` | Clasifica un nuevo caso de uso de IA conforme a la pirámide de riesgo del EU AI Act (prohibido / alto / limitado / mínimo / GPAI) y el marco mexicano. Determina si requiere evaluación de impacto y actualiza el registro de casos de uso. |
| `/ia-governanza-legal-mexico:impact-assessment` | Evaluación de impacto por capas (datos, modelo, output, deployment) para identificar riesgos de privacidad, discriminación, responsabilidad, seguridad y cumplimiento. Produce reporte con plan de mitigación. |
| `/ia-governanza-legal-mexico:vendor-contract-review` | Revisa contratos con proveedores de IA — training-on-data, propiedad de outputs, liability caps, indemnización, cumplimiento EU AI Act, notificación de brechas, portabilidad al terminar. |
| `/ia-governanza-legal-mexico:eu-ai-act-exposure` | Análisis de exposición al EU AI Act — determina si aplica (test de nexo europeo), clasifica sistemas por riesgo, mapea obligaciones y fechas de cumplimiento, produce hoja de ruta. |
| `/ia-governanza-legal-mexico:ai-policy-draft` | Redacta o revisa la política interna de uso responsable de IA — usos permitidos y prohibidos, herramientas aprobadas, proceso de aprobación de nuevos casos de uso, supervisión humana obligatoria, reporte de incidentes. |

## Nota sobre aplicabilidad del EU AI Act a empresas mexicanas

El EU AI Act aplica extraterritorialmente. Una empresa mexicana puede quedar sujeta a sus obligaciones si:

- Pone en servicio o usa sistemas de IA cuyos outputs son utilizados en la UE
- Tiene clientes, empleados o filiales en la UE
- Es proveedor de una empresa con operaciones en la UE

`/ia-governanza-legal-mexico:eu-ai-act-exposure` hace el análisis de nexo antes de clasificar sistemas. Si no hay nexo europeo, los sistemas solo quedan sujetos al marco mexicano vigente.

## Dependencias

Este plugin requiere `conectores-legal-mexico` para integraciones con LegalDataHunter, Google Drive y Slack. Las integraciones son opcionales — el plugin funciona sin ellas usando conocimiento del modelo con etiquetas `[model knowledge — verify]`.

## Autor

Softlaw S.A. de C.V. — wario@soft.law
