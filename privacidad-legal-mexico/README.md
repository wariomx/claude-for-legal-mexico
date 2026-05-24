# privacidad-legal-mexico

Plugin de protección de datos personales para el ecosistema jurídico mexicano. Cubre el cumplimiento de la Ley Federal de Protección de Datos Personales en Posesión de Particulares (LFPDPPP) y la Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (LGPDPPSP) ante el Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales (INAI).

## Instalación

```
claude plugin install privacidad-legal-mexico@claude-for-legal-mexico
```

Después de instalar, ejecuta la entrevista de configuración inicial:

```
/privacidad-legal-mexico:cold-start-interview
```

La entrevista tarda entre 10 y 15 minutos en configuración completa (2 minutos en modo rápido) y todos los skills del plugin dependen de ella.

## Descripción

Este plugin asiste a equipos jurídicos y de cumplimiento en organizaciones del sector privado y público con:

- Redacción y revisión de avisos de privacidad (simplificado, corto, integral) conforme a Arts. 15-17 LFPDPPP
- Gestión de solicitudes de derechos ARCO (Acceso, Rectificación, Cancelación, Oposición) con cómputo automático de plazos hábiles
- Análisis de transferencias internacionales de datos y revisión de contratos con encargados (DPA)
- Evaluaciones de impacto en la protección de datos (EIPD)
- Protocolo de respuesta a vulneraciones de seguridad con cómputo del plazo de 72 horas para notificación al INAI
- Diagnóstico de brechas de cumplimiento con plan de remediación priorizado
- Preparación para procedimientos ante el INAI (Procedimiento de Protección de Derechos, Verificación, Denuncia)

## Skills

| Skill | Descripción |
|---|---|
| `/privacidad-legal-mexico:cold-start-interview` | Entrevista de configuración inicial — configura el perfil de práctica y activa los módulos relevantes |
| `/privacidad-legal-mexico:customize` | Ajusta configuración del plugin sin re-ejecutar la entrevista completa |
| `/privacidad-legal-mexico:aviso-privacidad` | Redacta o revisa avisos de privacidad (simplificado / corto / integral) con verificación de elementos obligatorios |
| `/privacidad-legal-mexico:arco-response` | Gestiona solicitudes ARCO — recepción, clasificación, cómputo de plazos hábiles y borrador de respuesta |
| `/privacidad-legal-mexico:vulneracion-notificacion` | Protocolo de respuesta a vulneraciones — análisis de la obligación de notificar al INAI en 72 horas y borrador de aviso |
| `/privacidad-legal-mexico:gap-analysis` | Diagnóstico de cumplimiento LFPDPPP/LGPDPPSP con tabla de hallazgos por severidad y plan de remediación |
| `/privacidad-legal-mexico:contrato-datos` | Revisión o redacción de cláusulas de protección de datos — DPA, cláusulas responsable-encargado, transferencias internacionales |

## Marco legal cubierto

- Ley Federal de Protección de Datos Personales en Posesión de Particulares (LFPDPPP) — sector privado
- Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados (LGPDPPSP / LGPDPPSOH) — sector público
- Reglamento de la LFPDPPP
- Lineamientos del INAI (Avisos de Privacidad, Medidas de Seguridad, Transferencias Internacionales)
- Criterios de resoluciones del INAI en procedimientos de protección de derechos

## Dependencias

Este plugin requiere el plugin `conectores-legal-mexico` (instalado automáticamente como dependencia). Los conectores MCP para investigación jurídica (LegalDataHunter), almacenamiento de documentos (Google Drive, SharePoint, Box) y Slack se configuran a través de ese plugin.

## Licencia

Copyright 2026 Softlaw S.A. de C.V. Todos los derechos reservados.

Los contenidos de este plugin constituyen material de apoyo para profesionales del derecho. No constituyen asesoría jurídica ni sustituyen el criterio de un abogado titulado.
