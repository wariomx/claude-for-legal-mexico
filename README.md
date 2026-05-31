# Claude para la Industria Legal

Agentes de referencia, skills y conectores de datos para los flujos de trabajo legales más comunes — jurídico comercial, privacidad, producto, corporativo, laboral, litigación, regulatorio, gobernanza de IA, propiedad intelectual, seguros, y la formación jurídica (clínicas jurídicas y estudiantes de derecho).

> **¿Primera vez aquí?** Comienza con [QUICKSTART.md](QUICKSTART.md) — instala en 60 segundos. Este README es la referencia completa.

Todo está disponible **de dos formas desde una sola fuente**: instálalo como plugin de [Claude Cowork](https://claude.com/product/cowork) o [Claude Code](https://claude.com/product/claude-code), o despliégalo a través de la [API de Agentes Gestionados de Claude](https://docs.claude.com/en/api/managed-agents) detrás de tu propio motor de flujo de trabajo. El mismo system prompt, las mismas skills — tú eliges dónde corre.

## Primeros Pasos en Cowork
- [Instala Claude Desktop](https://claude.com/download)
- Obtén acceso a Claude Cowork
- Sigue las instrucciones del video a continuación:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

> [!IMPORTANT]
> **Toda salida de estos plugins es un borrador para revisión del abogado — no es asesoría legal, no es una conclusión jurídica, no sustituye a un abogado.** Están construidos con salvaguardas que lo reflejan: atribución de fuente en cada cita, valores conservadores por defecto en privilegio y decisiones legales subjetivas, supuestos de jurisdicción expuestos, y compuertas explícitas antes de presentar, enviar o actuar sobre cualquier documento. Un abogado revisa, verifica y asume la responsabilidad profesional de todo lo que sale de la oficina. Estos plugins hacen esa revisión más rápida; no la reemplazan.
>
> **Estos plugins no representan las posiciones legales de Anthropic.** Son herramientas que ayudan a los abogados a analizar asuntos. Cuando un skill incluye un ítem de lista de verificación, un marco sugerido, una bandera de riesgo, o una caracterización de jurisprudencia o guía regulatoria, eso es un apoyo al análisis propio del abogado revisor, no una declaración de la posición de Anthropic sobre el derecho. El derecho en muchas de estas áreas es incierto y está en evolución. El abogado que usa el plugin — no el plugin, y no Anthropic — es responsable de las posiciones legales adoptadas en su trabajo.

## Licenciamiento

Los plugins en este repositorio están licenciados bajo dos términos diferentes:

- **Plugins upstream** (commercial-legal, privacy-legal, product-legal, corporate-legal, employment-legal, regulatory-legal, ai-governance-legal, litigation-legal, law-student, legal-clinic, legal-builder-hub, ip-legal, cocounsel-legal) — **Apache 2.0**. Ver el archivo `LICENSE` raíz y `NOTICE`.

- **Plugins México** (conectores-legal-mexico, corporativo-legal-mexico, litigacion-legal-mexico, propiedad-intelectual-legal-mexico, laboral-legal-mexico, privacidad-legal-mexico, regulatorio-legal-mexico, fiscal-legal-mexico, ia-governanza-legal-mexico, seguros-legal-mexico) — **AGPLv3+**. Libres de usar, modificar y distribuir bajo la Licencia Pública General de Affero GNU v3.0 o posterior — incluyendo uso comercial, siempre que las modificaciones se compartan bajo los mismos términos. Una licencia comercial (sin el requisito de compartir de la AGPLv3) está disponible — contactar **wario@soft.law**. Ver `LICENSE` y `LICENSE-EXCEPTIONS.md` en cada directorio de plugin.

Lo que hay en el repositorio:

- **Plugins por área de práctica** que cubren trabajo legal de jurídico interno, despacho y académico — cada uno construido alrededor de una entrevista de configuración que aprende tu manual de práctica y un perfil de práctica `CLAUDE.md` que todas las skills leen.
- **Cookbooks de agentes gestionados** para los flujos de trabajo con monitoreo programado (vigilante de renovaciones, vigilante de expedientes, monitor de feeds regulatorios, revisión de data room, radar de lanzamientos).
- **Conectores MCP** en productividad general (Slack, Google Drive, Box) y sistemas específicos para legal (Ironclad, DocuSign, iManage, Everlaw, CourtListener, y más).
- **[Agentes con nombre](#agentes)** — agentes de flujo de trabajo completo con nombres por tipo de trabajo y un único comando para ejecutar cada uno.

## Agentes

Cada agente recibe el nombre del flujo de trabajo que ejecuta. Son la superficie más común — comienza con los que corresponden a tu trabajo, luego ajusta el skill subyacente, el perfil de práctica y los conectores a cómo lo hace tu equipo.

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de Contratos con Proveedores** | Revisa un MSA de proveedor contra tu playbook y produce un memo con redline | `commercial-legal` | `/commercial-legal:review` |
| **Triador de NDAs** | Triaje VERDE/AMARILLO/ROJO de NDAs entrantes para que solo los difíciles lleguen al escritorio del abogado | `commercial-legal` | `/commercial-legal:review` |
| **Trazador de Enmiendas** | Traza cómo ha cambiado un contrato a través de su acuerdo base y cada enmienda | `commercial-legal` | `/commercial-legal:amendment-history` |
| **Vigilante de Renovaciones** | Escanea el registro de contratos por fechas de cancelación y renovación | `commercial-legal` | agente programado |
| **Debrief de Cierre** | Barrido semanal de acuerdos firmados con desviaciones del playbook | `commercial-legal` | agente programado |
| **Monitor de Playbook** | Vigila el registro de desviaciones y propone actualizaciones cuando una cláusula ha derivado | `commercial-legal` | agente programado |
| **Enrutador de Escaladas** | Enruta asuntos contractuales al aprobador correcto y redacta la solicitud | `commercial-legal` | `/commercial-legal:escalation-flagger` |
| **Revisión Tabular de Debida Diligencia** | Revisión tabular de un data room con una fila por documento y cada celda citada | `corporate-legal` | `/corporate-legal:tabular-review` |
| **Extractor de Hallazgos** | Lee documentos de VDR y extrae hallazgos por categorías y umbrales de la casa | `corporate-legal` | `/corporate-legal:diligence-issue-extraction` |
| **Redactor de Consentimiento del Consejo** | Redacta consentimientos escritos unánimes en formato casa con búsqueda de precedentes | `corporate-legal` | `/corporate-legal:written-consent` |
| **Constructor de Calendario de Contratos Materiales** | Construye el anexo de revelaciones a partir de hallazgos de debida diligencia | `corporate-legal` | `/corporate-legal:material-contract-schedule` |
| **Rastreador de Cumplimiento de Entidades** | Calcula fechas de presentación por jurisdicción y tipo de entidad | `corporate-legal` | `/corporate-legal:entity-compliance` |
| **Conductor de Lista de Cierre** | Rastrea cada condición, consentimiento, documento y presentación que bloquea el cierre | `corporate-legal` | `/corporate-legal:closing-checklist` |
| **Manual de Integración** | Plan de integración post-cierre por fases con seguimiento de consentimientos | `corporate-legal` | `/corporate-legal:integration-management` |
| **Vigilante de Data Room** | Monitorea el VDR por nuevas cargas y publica el estatus de la lista de cierre | `corporate-legal` | agente programado |
| **Revisor de Terminaciones** | Ejecuta una terminación propuesta contra indicadores de riesgo por jurisdicción | `employment-legal` | `/employment-legal:termination-review` |
| **Revisor de Contrataciones** | Revisa cartas de oferta y cláusulas restrictivas con verificación de jurisdicción | `employment-legal` | `/employment-legal:hiring-review` |
| **Clasificador de Trabajadores** | Evalúa un contrato propuesto contra el test de la jurisdicción aplicable | `employment-legal` | `/employment-legal:worker-classification` |
| **Rastreador de Ausencias** | Monitorea ausencias abiertas con alertas de plazos FMLA/CFRA/PFL/ADA | `employment-legal` | agente programado |
| **Director de Investigaciones** | Abre, rastrea, complementa y resume asuntos de investigación interna | `employment-legal` | `/employment-legal:investigation-open` |
| **Redactor de Políticas** | Redacta políticas laborales con suplementos estatales donde la ley difiere | `employment-legal` | `/employment-legal:policy-drafting` |
| **Planificador de Expansión Internacional** | Inicia la planificación EOR vs. entidad para un nuevo país | `employment-legal` | `/employment-legal:expansion-kickoff` |
| **Q&A de Salarios y Jornada** | Q&A laboral consciente de jurisdicción para el canal de "preguntas rápidas" | `employment-legal` | `/employment-legal:wage-hour-qa` |
| **Respondedor de DSAR** | Redacta acuses de recibo y respuestas de DSAR dentro de los plazos legales | `privacy-legal` | `/privacy-legal:dsar-response` |
| **Revisor de DPA** | Revisa un DPA contra tu playbook como responsable o encargado | `privacy-legal` | `/privacy-legal:dpa-review` |
| **Generador de PIA** | Genera una Evaluación de Impacto de Privacidad en formato casa | `privacy-legal` | `/privacy-legal:pia-generation` |
| **Triador de Privacidad** | Decide si una actividad de tratamiento necesita PIA, DPIA de GDPR, o puede proceder | `privacy-legal` | `/privacy-legal:use-case-triage` |
| **Verificador de Brechas de Privacidad** | Coteja una regulación nueva contra la política y práctica actual de privacidad | `privacy-legal` | `/privacy-legal:reg-gap-analysis` |
| **Monitor de Política de Privacidad** | Barre PIAs, revisiones de DPA y resultados de triaje por desviación de política | `privacy-legal` | `/privacy-legal:policy-monitor` |
| **Revisor de Lanzamientos** | Revisa un lanzamiento de producto contra tu calibración de riesgo | `product-legal` | `/product-legal:launch-review` |
| **Verificador de Claims de Marketing** | Señala copias que necesitan sustentación, reencuadre o eliminación | `product-legal` | `/product-legal:marketing-claims-review` |
| **Triaje "¿Esto es un problema?"** | Respuesta rápida para la pregunta de Slack — coincide patrones con tu calibración | `product-legal` | `/product-legal:is-this-a-problem` |
| **Vigilante de Lanzamientos** | Vigila el rastreador de lanzamientos por lanzamientos próximos que necesitan revisión | `product-legal` | agente programado |
| **Vigilante de Feeds Regulatorios** | Consulta feeds regulatorios y redacta el resumen del lunes | `regulatory-legal` | agente programado |
| **Verificación Regulatoria a Demanda** | Consulta feeds regulatorios ahora y reporta novedades | `regulatory-legal` | `/regulatory-legal:reg-feed-watcher` |
| **Diff de Política** | Coteja un cambio regulatorio contra la biblioteca de políticas | `regulatory-legal` | `/regulatory-legal:policy-diff` |
| **Rastreador de Brechas** | Rastreador de brechas abiertas — qué está señalado y aún no cerrado | `regulatory-legal` | `/regulatory-legal:gaps` |
| **Redactor de Políticas Regulatorias** | Borrador de política cerrando una brecha — propuesta para revisión, no edición directa | `regulatory-legal` | `/regulatory-legal:policy-redraft` |
| **Rastreador de Comentarios NPRM** | Revisa períodos abiertos de comentarios de NPRM, registra decisiones, rastrea plazos | `regulatory-legal` | `/regulatory-legal:comments` |
| **Triador de Casos de Uso de IA** | Clasifica casos de uso de IA propuestos contra tu registro | `ai-governance-legal` | `/ai-governance-legal:use-case-triage` |
| **Evaluador de Impacto de IA** | Ejecuta una evaluación de impacto de IA en los regímenes en alcance | `ai-governance-legal` | `/ai-governance-legal:aia-generation` |
| **Revisor de IA de Proveedores** | Revisa términos de IA por entrenamiento sobre datos, responsabilidad y brechas de política | `ai-governance-legal` | `/ai-governance-legal:vendor-ai-review` |
| **Verificador de Brechas de Regulación de IA** | Coteja una nueva regulación de IA contra tu postura actual de gobernanza | `ai-governance-legal` | `/ai-governance-legal:reg-gap-analysis` |
| **Monitor de Política de IA** | Barre AIAs, triajes y revisiones de proveedores por desviación de política | `ai-governance-legal` | `/ai-governance-legal:policy-monitor` |
| **Evaluador de Disponibilidad de Marca** | Primera revisión de disponibilidad con verificación de knockout y heurísticas de confusión | `ip-legal` | `/ip-legal:clearance` |
| **Redactor de Carta de Requerimiento** | Redacta o triaje una carta de requerimiento, calibrado a tu postura de enforcement | `ip-legal` | `/ip-legal:cease-desist` |
| **Takedown DMCA** | Redacta un takedown, triaje uno recibido, o redacta un contra-aviso §512(g) | `ip-legal` | `/ip-legal:takedown` |
| **Verificador de Cumplimiento OSS** | Clasifica licencias de código abierto contra tu modelo de despliegue | `ip-legal` | `/ip-legal:oss-review` |
| **Triador de FTO** | Primera mirada estructurada a patentes potencialmente bloqueantes — triaje, no una opinión | `ip-legal` | `/ip-legal:fto-triage` |
| **Triador de Infracción de PI** | Triaje a través de los cuatro derechos de PI — factores, no una conclusión | `ip-legal` | `/ip-legal:infringement-triage` |
| **Revisor de Cláusulas de PI** | Revisa cláusulas de cesión, titularidad, licencia, garantías e indemnidades | `ip-legal` | `/ip-legal:ip-clause-review` |
| **Rastreador de Portafolio de PI** | Registros, renovaciones, cuotas de mantenimiento, declaraciones de uso | `ip-legal` | `/ip-legal:portfolio` |
| **Vigilante de Renovaciones de PI** | Reporte programado de plazos del registro de portafolio de PI | `ip-legal` | agente programado |
| **Constructor de Cuadros de Elementos** | Cuadro de elementos por elemento, patente o causa de acción civil | `litigation-legal` | `/litigation-legal:claim-chart` |
| **Vigilante de Expedientes** | Monitorea expedientes judiciales por presentaciones y plazos | `litigation-legal` | agente programado |
| **Vigilante de Expedientes (México)** | Vigila expedientes en el Poder Judicial Federal y CJJ; calcula plazos procesales | `litigacion-legal-mexico` | agente programado |
| **Verificador Jurídico** | QA de skills y documentos: verifica plazos, artículos y vigencia contra fuentes primarias mexicanas | `litigacion-legal-mexico` | `/litigacion-legal-mexico:verificador-juridico` |
| **Vigilante de Renovaciones PI (México)** | Reporte priorizado de vencimientos ante IMPI e INDAUTOR | `propiedad-intelectual-legal-mexico` | agente programado |
| **Redactor de Requerimiento** | Redacta carta de requerimiento con compuerta pre-envío y salida .docx | `litigation-legal` | `/litigation-legal:demand-draft` |
| **Intake de Requerimiento** | Recopilación de contexto pre-redacción — partes, hechos, fundamento, palanca | `litigation-legal` | `/litigation-legal:demand-intake` |
| **Triaje de Requerimiento Recibido** | Triaje de requerimiento entrante — opciones, cotejo con portafolio, entrega | `litigation-legal` | `/litigation-legal:demand-received` |
| **Triaje de Citatorio** | Clasifica, delimita y planifica el cumplimiento de un nuevo citatorio | `litigation-legal` | `/litigation-legal:subpoena-triage` |
| **Constructor de Cronología** | Construye o actualiza una cronología desde fuentes declaradas y cargas | `litigation-legal` | `/litigation-legal:chronology` |
| **Preparación de Deposición** | Construye un esquema de deposición vinculado a la teoría del caso | `litigation-legal` | `/litigation-legal:deposition-prep` |
| **Redactor de Sección de Escrito** | Redacta una sección de escrito en estilo casa, coherente con la teoría del caso | `litigation-legal` | `/litigation-legal:brief-section-drafter` |
| **Revisor de Registro de Confidencialidad** | Primera revisión del registro de privilegio — llamadas obvias + señalamientos | `litigation-legal` | `/litigation-legal:privilege-log-review` |
| **Retención Documental** | Emitir, refrescar, liberar o reportar sobre retenciones documentales | `litigation-legal` | `/litigation-legal:legal-hold` |
| **Intake de Asunto** | Intake uniforme de nuevo asunto — escribe matter.md, history.md, adjunta al log | `litigation-legal` | `/litigation-legal:matter-intake` |
| **Briefing de Asunto** | Briefing profundo de un asunto para llamada con DG o abogados externos | `litigation-legal` | `/litigation-legal:matter-briefing` |
| **Estatus de Portafolio** | Distribución de riesgo, plazos próximos, asuntos sin movimiento | `litigation-legal` | `/litigation-legal:portfolio-status` |
| **Estatus de Abogados Externos** | Genera borradores de solicitud de estatus semanal para el portafolio activo | `litigation-legal` | `/litigation-legal:oc-status` |
| **Intake de Clínica** | Intake estructurado de cliente con identificación de problemas y señalamientos de conflicto | `legal-clinic` | `/legal-clinic:client-intake` |
| **Scaffold de Memo de Caso** | Memo de análisis con estructura IRAC y brechas de investigación señaladas | `legal-clinic` | `/legal-clinic:memo` |
| **Hoja de Ruta de Investigación** | Estatutos, áreas de jurisprudencia, términos de búsqueda — pistas, no citas | `legal-clinic` | `/legal-clinic:research-start` |
| **Rastreador de Plazos de Clínica** | Agregar, reportar, actualizar y cerrar plazos con advertencias de responsabilidad | `legal-clinic` | `/legal-clinic:deadlines` |
| **Resumen de Estatus de Caso** | Estatus del caso por audiencia — cliente, profesor o listo para tribunal | `legal-clinic` | `/legal-clinic:status` |
| **Redactor de Carta al Cliente** | Correspondencia rutinaria — confirmaciones, solicitudes de documentos, actualizaciones | `legal-clinic` | `/legal-clinic:client-letter` |
| **Incorporación de Estudiante** | Inducción de semestre — procedimientos de clínica, recorrido de herramientas | `legal-clinic` | `/legal-clinic:ramp` |
| **Entrega de Semestre** | Memos de entrega de casos al fin de semestre | `legal-clinic` | `/legal-clinic:semester-handoff` |
| **Cola de Revisión del Supervisor** | Cola de revisión del profesor (cuando supervisión formal está configurada) | `legal-clinic` | `/legal-clinic:supervisor-review-queue` |
| **Coach de Preparación para el Examen** | Práctica de MBE y ensayos, dirigida a materias débiles | `law-student` | `/law-student:bar-prep-questions` |
| **Sargento de Taladro Socrático** | Él pregunta, tú respondes, él contraargumenta — no da la respuesta | `law-student` | `/law-student:socratic-drill` |
| **Calificador de IRAC** | Califica tu ensayo IRAC en estructura, identificación de problemas, reglas, análisis | `law-student` | `/law-student:irac-practice` |
| **Resumidor de Casos** | Resume un caso en tu formato preferido | `law-student` | `/law-student:case-brief` |
| **Constructor de Esquemas** | Construye o extiende un esquema desde notas de clase y libro de texto | `law-student` | `/law-student:outline-builder` |
| **Preparación para Clase** | Predice las preguntas del profesor y las practica antes de clase | `law-student` | `/law-student:cold-call-prep` |
| **Pronosticador de Examen** | Analiza exámenes pasados del mismo profesor; pronostica énfasis probables | `law-student` | `/law-student:exam-forecast` |
| **Crítico de Escritura Legal** | Retroalimentación estructural sobre un borrador — nunca reescribe | `law-student` | `/law-student:legal-writing` |
| **Maestro de Tarjetas de Memoria** | Genera o practica tarjetas — cubetas estilo Leitner | `law-student` | `/law-student:flashcards` |
| **Planificador de Estudio** | Plan de estudio a largo plazo con sesiones programadas | `law-student` | `/law-student:study-plan` |
| **Navegador del Registro de Skills** | Busca skills legales de comunidad en registros vigilados | `legal-builder-hub` | `/legal-builder-hub:registry-browser` |
| **Instalador de Skills** | Instala un skill de comunidad con verificaciones de confianza y QA | `legal-builder-hub` | `/legal-builder-hub:skill-installer` |
| **QA de Skills** | Evalúa un skill contra el Marco de Diseño de Skills Legales | `legal-builder-hub` | `/legal-builder-hub:skills-qa` |
| **Recomendador de Skills de Comunidad** | Sugiere skills de comunidad basado en actividad reciente en otros plugins | `legal-builder-hub` | `/legal-builder-hub:related-skills-surfacer` |
| **Actualizador de Skills de Comunidad** | Verifica actualizaciones de skills de comunidad instalados | `legal-builder-hub` | `/legal-builder-hub:auto-updater` |
| **Sincronización de Registro** | Verificación periódica de registros vigilados por skills nuevos y actualizados | `legal-builder-hub` | agente programado |

Para despliegue como Agente Gestionado — `agent.yaml`, subagentes hoja, ejemplos de eventos de dirección y notas de seguridad por agente — ver **[managed-agent-cookbooks/](./managed-agent-cookbooks)**.

## Plugins para México

Este repositorio incluye plugins adaptados al sistema jurídico mexicano. Cada plugin contextualiza su equivalente estadounidense al derecho civil codificado de México, la jurisprudencia de la SCJN, y los procedimientos ante las autoridades mexicanas.

| Plugin | Qué hace | Skills | Agentes |
|---|---|---|---|
| **[conectores-legal-mexico](./conectores-legal-mexico/)** | Conectores MCP compartidos — LegalDataHunter, Solve Intelligence, CJJ (Jalisco), MXLegal (STJJ), Slack, Google Drive, Box, iManage. Dependencia automática de los otros plugins. Incluye `/setup-completo` para configurar todos los plugins en un solo comando | 3 | — |
| **[corporativo-legal-mexico](./corporativo-legal-mexico/)** | F&A, debida diligencia, Consejo de Administración, gestión de entidades bajo LGSM — SA de CV, S de RL de CV, SAS | 13 | — |
| **[litigacion-legal-mexico](./litigacion-legal-mexico/)** | Portafolio de litigios, plazos procesales, cuadros de elementos, cronologías, plantillas de demanda (7 tipos), redacción de escritos, preparación de pruebas, monitoreo de boletín judicial CJJ | 22 | 2 |
| **[propiedad-intelectual-legal-mexico](./propiedad-intelectual-legal-mexico/)** | Portafolio de PI ante IMPI e INDAUTOR, FTO, clearance de marca, cartas de requerimiento, derechos morales (LFDA Art. 19), reservas de derechos | 13 | 1 |
| **[laboral-legal-mexico](./laboral-legal-mexico/)** | Práctica laboral bajo la LFT — riesgo de terminación, cálculo de liquidación constitucional, conciliación CJFCA, cumplimiento NOM-035/037-STPS, IMSS/INFONAVIT, plataformas digitales | 11 | 1 |
| **[privacidad-legal-mexico](./privacidad-legal-mexico/)** | Cumplimiento de la LGPDPPSP/LFPDPPP ante el INAI — avisos de privacidad, solicitudes ARCO, transferencias internacionales, EIPD, notificación de vulneraciones | 9 | — |
| **[regulatorio-legal-mexico](./regulatorio-legal-mexico/)** | Práctica regulatoria federal — COFECE, CNBV, COFEPRIS, CONAMER, respuesta a requerimientos, comentarios públicos. Incluye agente monitor-dof | 8 | 1 |
| **[fiscal-legal-mexico](./fiscal-legal-mexico/)** | Práctica fiscal — revisión de CFDI 4.0, requerimientos SAT, auditorías, litigación ante el TFJA, procedimientos PRODECON, planeación fiscal | 8 | — |
| **[ia-governanza-legal-mexico](./ia-governanza-legal-mexico/)** | Gobernanza de IA — clasificación de riesgo EU AI Act, evaluaciones de impacto, revisión de contratos con proveedores de IA, políticas internas de uso | 7 | — |
| **[seguros-legal-mexico](./seguros-legal-mexico/)** | Seguros y fianzas bajo la LGSF — revisión de pólizas, trámites CNSF, análisis de cobertura, disputas de siniestros, reaseguro, solvencia RCS, recursos CONDUSEF | 10 | — |

### Instalación rápida

```bash
# 1. Registrar el repo como marketplace local
claude plugin marketplace add .

# 2. Instalar los plugins — conectores-legal-mexico se instala automáticamente como dependencia
claude plugin install corporativo-legal-mexico@claude-for-legal-mexico
claude plugin install litigacion-legal-mexico@claude-for-legal-mexico
claude plugin install propiedad-intelectual-legal-mexico@claude-for-legal-mexico
claude plugin install laboral-legal-mexico@claude-for-legal-mexico
claude plugin install privacidad-legal-mexico@claude-for-legal-mexico
claude plugin install regulatorio-legal-mexico@claude-for-legal-mexico
claude plugin install fiscal-legal-mexico@claude-for-legal-mexico
claude plugin install ia-governanza-legal-mexico@claude-for-legal-mexico
claude plugin install seguros-legal-mexico@claude-for-legal-mexico

# 3. Configurar la clave API de LegalDataHunter (se guarda en el llavero del sistema, no en variables de entorno)
claude plugin configure conectores-legal-mexico@claude-for-legal-mexico
# Ingresar la clave cuando se solicite: legaldatahunter_api_key → sk-...

# 4. Exportar credenciales del Portal Ciudadano CJJ al perfil del shell (solo si usas litigacion en Jalisco)
echo 'export CJJ_NILO_EMAIL="usuario@ejemplo.com"' >> ~/.zshrc
echo 'export CJJ_NILO_PASSWORD="tu-contraseña"' >> ~/.zshrc
echo 'export CJJ_NILO_PUBLIC_TOKEN="YWxwaGEx"' >> ~/.zshrc
source ~/.zshrc

# 5. Configurar todos los plugins en un solo comando (~5 min rápido, ~20 min completo)
/conectores-legal-mexico:setup-completo
# Configura conectores → corporativo → litigacion → PI en secuencia.
# Pregunta empresa/industria/jurisdicción una sola vez; los plugins siguientes lo reusan.
# Para retomar si se interrumpe: /conectores-legal-mexico:setup-completo --from litigacion
```

> **Credenciales seguras:** La clave de LegalDataHunter se almacena en el llavero del sistema a través de `plugin configure` — no se escribe en variables de entorno ni en archivos. Las credenciales CJJ usan variables de entorno porque el plugin no tiene soporte `userConfig` todavía.

### Variables de entorno

| Variable | Plugin | Descripción |
|---|---|---|
| `CJJ_NILO_EMAIL` | litigacion | Correo del Portal Ciudadano CJJ (Jalisco) — para API Nilo autenticada |
| `CJJ_NILO_PASSWORD` | litigacion | Contraseña del Portal Ciudadano CJJ |
| `CJJ_NILO_PUBLIC_TOKEN` | litigacion | Token público del API Nilo |

La clave de LegalDataHunter ya no va aquí — se configura con `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` y se guarda en el llavero del sistema. **Nunca hacer commit de credenciales al repositorio.**

### Diferencias clave con los plugins estadounidenses

- **Sistema jurídico civil codificado** — las leyes federales y estatales son la fuente primaria; la jurisprudencia (SCJN) vincula solo cuando se cumple el umbral (5 resoluciones consecutivas)
- **Secreto profesional** — reemplaza el attorney-client privilege y work product; más estrecho que el equivalente estadounidense
- **No existe patent agent privilege** — solo abogados titulados con cédula profesional gozan de secreto profesional
- **Derechos morales (LFDA Art. 19)** — perpetuos, inalienables, irrenunciables para todas las obras
- **Marco institucional dual de PI** — IMPI (propiedad industrial) + INDAUTOR (derechos de autor)
- **Enforcement** — IMPI administrativo + civil (daños y perjuicios) + penal (UEIDDAPI)
- **Monitoreo judicial** — boletín CJJ (Jalisco) vía API pública + Portal Ciudadano autenticado

## Estructura del Repositorio

```
commercial-legal/         # jurídico comercial interno — revisión de proveedores/NDA/SaaS, renovaciones, escaladas
corporate-legal/          # debida diligencia F&A, listas de cierre, consentimientos del consejo, cumplimiento de entidades
employment-legal/         # revisión de contrataciones/terminaciones, clasificación de trabajadores, ausencias, investigaciones
privacy-legal/            # DPA, DSAR, PIA, triaje de privacidad, monitor de política
product-legal/            # revisión de lanzamientos, claims de marketing, triaje "¿es esto un problema?"
regulatory-legal/         # vigilante de feeds regulatorios, diff de política, rastreador de brechas, comentarios NPRM
ai-governance-legal/      # triaje de casos de uso de IA, AIAs, revisión de IA de proveedor, brecha regulatoria de IA
ip-legal/                 # clearance de marca, FTO, C&D, DMCA, OSS, cláusulas de PI, portafolio
litigation-legal/         # portafolio, asuntos, retenciones, requerimientos, prep de deposición, cuadros de elementos
conectores-legal-mexico/  # conectores MCP compartidos — LegalDataHunter, CJJ, MXLegal, integraciones de productividad
corporativo-legal-mexico/ # F&A, debida diligencia, Consejo, entidades — derecho mexicano
litigacion-legal-mexico/  # portafolio de litigios, plazos, escritos, boletín CJJ — derecho mexicano
propiedad-intelectual-legal-mexico/ # PI ante IMPI/INDAUTOR, FTO, marcas, derechos morales — derecho mexicano
laboral-legal-mexico/     # LFT, liquidación, CJFCA, NOM-035/037, IMSS/INFONAVIT — derecho mexicano
privacidad-legal-mexico/  # LGPDPPSP, avisos de privacidad, ARCO, INAI — derecho mexicano
regulatorio-legal-mexico/ # COFECE, CNBV, COFEPRIS, CONAMER, DOF — derecho mexicano
fiscal-legal-mexico/      # SAT, CFDI, TFJA, PRODECON — derecho mexicano
ia-governanza-legal-mexico/ # gobernanza de IA, EU AI Act, proveedores de IA — con nexo mexicano
seguros-legal-mexico/     # LGSF, CNSF, pólizas, siniestros, reaseguro — derecho mexicano
legal-clinic/             # configuración de clínica, incorporación de estudiantes, intake, plazos, memos, entregas
law-student/              # taladro socrático, esquemas, IRAC, preparación para el examen, tarjetas de memoria
legal-builder-hub/        # descubrimiento e instalación de skills de comunidad con compuerta de confianza
external_plugins/         # plugins construidos por socios y mantenidos por sus proveedores
  cocounsel-legal/        # Thomson Reuters — Westlaw Deep Research vía el MCP de CoCounsel Legal
managed-agent-cookbooks/  # cookbooks de Agentes Gestionados de Claude — un directorio por agente programado
  diligence-grid/
  docket-watcher/
  launch-radar/
  reg-monitor/
  renewal-watcher/
scripts/                  # deploy-managed-agent.sh · validate.py · orchestrate.py · lint-tool-scope.py · test-cookbooks.sh
.claude-plugin/
  marketplace.json        # registro de plugins
.env                      # variables de entorno locales (NO hacer commit) — ver sección "Variables de entorno"
```

Cada directorio de plugin tiene la misma forma:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # plantilla de perfil de práctica — llenado por /<plugin>:cold-start-interview
  README.md
  skills/                 # skills — cada uno es un comando de barra /<plugin>:<skill>
  agents/                 # agentes programados (si los hay)
  hooks/                  # hooks pre- y post-herramienta (si los hay)
```

## Primeros Pasos

### Claude Cowork

En Cowork:

1. Abre la pestaña **Cowork**.
2. Haz clic en **Personalizar** en la barra lateral izquierda.
3. Haz clic en **Explorar plugins** e instala los que quieras, **o** sube un archivo de plugin personalizado (cualquier directorio de plugin comprimido).

Después de instalar, las skills se activan automáticamente cuando son relevantes, los comandos de barra están disponibles vía `/`, y los agentes programados corren según la cadencia establecida en su frontmatter.

### Claude Code

```bash
# Agrega el marketplace (usa la ruta absoluta a este repo o una URL de GitHub)
/plugin marketplace add <ruta-a-este-repo>

# Instala un plugin — elige los que corresponden a tu práctica
/plugin install commercial-legal@claude-for-legal-mexico
/plugin install privacy-legal@claude-for-legal-mexico
/plugin install corporate-legal@claude-for-legal-mexico

# Reinicia Claude Code, luego ejecuta la configuración para cada plugin instalado.
# Esto escribe tu perfil de práctica en ~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md
/commercial-legal:cold-start-interview
/privacy-legal:cold-start-interview
/corporate-legal:cold-start-interview
```

**Ejecuta la entrevista de configuración primero.** Cada otro skill en un plugin lee del perfil de práctica que escribe. Saltarse la configuración es la razón más común por la que un skill produce resultados genéricos. La entrevista toma 10–20 minutos por plugin y te pedirá que señales documentos semilla (un MSA firmado, un playbook, un memo de revisión previo — lo que encaje con el plugin). Más material semilla es mejor; una opción de **inicio rápido** está disponible si quieres ser productivo en 2 minutos y refinar después.

**Comienza conectando una herramienta de investigación.** Todo lo demás es mejor con una, y las citas no son verificadas sin ella. Ver [Conectores MCP](#conectores-mcp) a continuación para la lista completa — CourtListener, Trellis, Descrybe y Solve Intelligence son las herramientas de investigación que los guardianes de citas buscan.

Actualizaciones: `/plugin update`.

### Agentes Gestionados de Claude

Para los agentes programados — monitor de feeds regulatorios, vigilante de renovaciones, vigilante de expedientes, revisión de data room, radar de lanzamientos — despliega detrás de tu propio orquestador:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
scripts/deploy-managed-agent.sh reg-monitor
scripts/deploy-managed-agent.sh renewal-watcher
scripts/deploy-managed-agent.sh docket-watcher
scripts/deploy-managed-agent.sh diligence-grid
scripts/deploy-managed-agent.sh launch-radar
```

Cada plantilla bajo [`managed-agent-cookbooks/`](./managed-agent-cookbooks) hace referencia al mismo system prompt y skills que su contraparte plugin. El script de despliegue resuelve referencias de archivos, sube skills, crea subagentes hoja y hace POST del orquestador a `/v1/agents`. Ver [`scripts/orchestrate.py`](./scripts/orchestrate.py) para un bucle de eventos de referencia que enruta eventos `handoff_request` entre agentes vía tu propia capa de orquestación.

> **Vista Previa de Investigación:** la delegación de subagentes (`callable_agents`) es una capacidad en vista previa y admite un solo nivel de delegación. Ver READMEs por agente para el nivel de seguridad y guía de entrega.

## Cómo se Integra Todo

| | Qué es | Dónde vive |
|---|---|---|
| **Plugins** | Paquetes de área de práctica autónomos — skills, agentes, hooks y una plantilla de perfil de práctica. Instala los que necesites. | `<plugin>/` |
| **Skills** | Experiencia de dominio, convenciones y métodos paso a paso en los que Claude se apoya automáticamente cuando son relevantes — y acciones de barra que activas explícitamente: `/commercial-legal:review`, `/privacy-legal:dsar-response`, `/litigation-legal:claim-chart`. | `<plugin>/skills/<skill>/SKILL.md` |
| **Agentes** | Flujos de trabajo programados o basados en eventos. Corre en segundo plano, publica en un canal o escribe un archivo. | `<plugin>/agents/` |
| **Perfil de práctica** | `CLAUDE.md` en lenguaje llano que describe tu playbook, reglas de escalada y estilo de la casa. Todos los skills lo leen. | `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md` |
| **Conectores** | [Servidores MCP](https://modelcontextprotocol.io/) que conectan a Claude con tus datos — CLM, DMS, e-discovery, plataformas de investigación, productividad. | `.mcp.json` (por plugin) |
| **Cookbooks de agentes gestionados** | `agent.yaml` + subagentes nivel 1 + ejemplos de dirección para despliegue sin cabeza. | `managed-agent-cookbooks/<slug>/` |

Todo es markdown y JSON. Sin paso de compilación.

## Plugins por Área

Agrupados por dónde se ubica el trabajo. La entrevista de configuración de cada plugin es lo que lo adapta a tu equipo — comienza allí.

### Transaccional y consultivo

| Plugin | Qué agrega |
|---|---|
| **[commercial-legal](./commercial-legal)** | Revisión de contratos con proveedores, NDAs y suscripciones SaaS consciente del playbook. Trazado de enmiendas. Registro de renovaciones con alertas de cancelación. Enrutamiento de escaladas. Resúmenes para partes interesadas. |
| **[corporate-legal](./corporate-legal)** | Debida diligencia F&A con revisión tabular y cita por celda. Anexos de revelaciones, listas de cierre, consentimientos escritos, actas del consejo. Rastreador de cumplimiento de entidades. Integración post-cierre. |
| **[privacy-legal](./privacy-legal)** | Triaje de privacidad (PIA vs DPIA vs proceder), generación de PIA, revisión de DPA como responsable o encargado, respuesta de DSAR. Monitor de política vigila la desviación entre política y práctica. |
| **[product-legal](./product-legal)** | Revisión de lanzamientos contra la calibración de riesgo de la casa. Verificación de claims de marketing. Triaje "¿esto es un problema?" para preguntas de Slack. Evaluación de riesgo de funcionalidades. |
| **[employment-legal](./employment-legal)** | Revisión de contrataciones y terminaciones con banderas por jurisdicción. Clasificación de trabajadores. Rastreador de ausencias (FMLA/CFRA/PFL/ADA). Investigaciones internas. Redacción de políticas con suplementos estatales. |
| **[ai-governance-legal](./ai-governance-legal)** | Triaje de casos de uso de IA contra tu registro. Evaluaciones de impacto en los regímenes en alcance. Revisión de IA de proveedor. Análisis de brecha regulación-política. |
| **[regulatory-legal](./regulatory-legal)** | Vigilante de feeds regulatorios, diff de política, rastreador de brechas, rastreador de períodos de comentarios NPRM. El resumen del lunes por la mañana que tu equipo realmente lee. |
| **[ip-legal](./ip-legal)** | Clearance de marca, triaje de FTO, redacción y triaje de C&D, takedown DMCA y contra-aviso, cumplimiento de OSS, revisión de cláusulas de PI, seguimiento de portafolio. |

### Litigación

| Plugin | Qué agrega |
|---|---|
| **[litigation-legal](./litigation-legal)** | Trabaja dos superficies. **Jurídico interno/portafolio:** intake de asuntos, estatus de portafolio, retenciones documentales, estatus de abogados externos, requerimientos. **Despacho/independiente:** construcción de cronologías, cuadros de elementos (patentes y civil), preparación de deposición, revisión de registro de confidencialidad, redacción de escritos. |

### Aprendizaje y práctica

| Plugin | Qué agrega |
|---|---|
| **[law-student](./law-student)** | Taladro socrático, resumen de casos, construcción de esquemas, calificación de IRAC, preparación para clase, tarjetas de memoria, preparación para el examen de barra, pronóstico de examen, planificación de estudio. **Modo aprendizaje, no modo respuesta** — nunca escribe la respuesta por ti. |
| **[legal-clinic](./legal-clinic)** | Configuración del profesor e incorporación de estudiantes al semestre. Guía de supervisor por área de práctica con postura pedagógica (asistir / guiar / enseñar). Intake estructurado con identificación de problemas entre áreas. Seguimiento de plazos con precaución por responsabilidad profesional. Memos, cartas al cliente, entregas de semestre. Construido dentro de la Opinión Formal ABA 512. |

### Ecosistema

| Plugin | Qué agrega |
|---|---|
| **[legal-builder-hub](./legal-builder-hub)** | Descubrimiento e instalación de skills de comunidad con una capa de confianza real — registros vigilados, un marco de QA (`/legal-builder-hub:skills-qa`), actualizaciones con SHA fijo, y una verificación de confianza obligatoria antes de que cualquier cosa aterrice en tu entorno. |

### Externos / construidos por socios

Los plugins bajo [`external_plugins/`](./external_plugins) son construidos y mantenidos por sus proveedores. Se instalan desde este marketplace como cualquier otro plugin, pero el proveedor es dueño del código, el conector y el canal de soporte.

| Plugin | Construido por | Qué agrega |
|---|---|---|
| **[cocounsel-legal](./external_plugins/cocounsel-legal)** | Thomson Reuters | Westlaw Deep Research con reportes completamente citados — jurisprudencia, estatutos, regulaciones, Practical Law y fuentes secundarias en hasta tres jurisdicciones de EE.UU. por ejecución. Requiere suscripción a CoCounsel Legal con el conector MCP habilitado. Soporte: cocounselsupport@tr.com. |

## La capa de confianza para skills legales de comunidad

La comunidad está construyendo skills legales rápidamente — registros como `lpm-skills` de LegalOps Consulting y Lawvable ya listan decenas. Pero nadie certifica los skills de comunidad, y un abogado que instala un skill aleatorio de GitHub está instalando código que corre con acceso a sus archivos de asuntos, su perfil de práctica y sus conectores de investigación.

`legal-builder-hub` le da al ecosistema la capa de confianza que le falta:

- **Revisión de seguridad** — escaneo de contenido oculto, detección de inyección, verificación estructural de confianza en cada instalación
- **Lista de permitidos** — compuerta de fuente restrictiva por defecto (registros, editores, conectores, licencias)
- **Compuerta de licencias** — política de licencias consciente del contexto de despliegue (personal / interno de despacho / incrustación en producto)
- **Compuerta de vigencia** — rastrea si el contenido de referencia incluido ha pasado su ventana de verificación, y advierte en la invocación
- **Re-escaneo en actualización** — un skill que estaba limpio en v1.0 y fue comprometido en v1.1 se detecta
- **Log de instalación** — un registro auditable de qué está instalado, de dónde, bajo qué licencia, con qué veredicto de revisión

La lista de permitidos es restrictiva por defecto. El modo permisivo es una elección explícita. Un no-abogado es enrutado a su contacto abogado, no a un botón de "instalar de todos modos".

Los skills de comunidad pasan por la misma revisión de diseño (`/legal-builder-hub:skills-qa`) que los plugins de primera parte. Si construyes para abogados, ejecuta el QA contra tu propio skill antes de publicar.

## Conectores MCP

> [!IMPORTANT]
> **Conecta una herramienta de investigación primero.** Cada plugin viene con conectores de investigación legal ya configurados — CourtListener, Trellis, Descrybe, Solve Intelligence y otros dependiendo del área de práctica. Los autorizas una vez, y a partir de entonces Claude extrae de fuentes autorizadas y verifica sus citas contra bases de datos actuales. Las citas que llegan a través de un conector de investigación están etiquetadas con la fuente. Las citas solo del conocimiento del modelo se marcan `[verificar]` y, si no hay ninguna herramienta de investigación conectada, la nota del revisor encima del entregable registra que las fuentes no fueron verificadas. Los conectores son los que hacen que las citas sean confiables — configúralos antes de configurar cualquier otra cosa.

Estos plugins incluyen conectores para los sistemas en los que viven los equipos legales.

| Conector | Qué le da a Claude | Plugins | Notas |
|---|---|---|---|
| **Slack** | Leer canales, buscar, enviar mensajes y canvases | todos los plugins | Tu workspace |
| **Google Drive** | Leer documentos, hojas, presentaciones; obtener por enlace | todos los plugins | Tu cuenta |
| **CoCounsel Legal (Thomson Reuters)** | Westlaw Deep Research — reportes citados de jurisprudencia, estatutos, regulaciones, Practical Law | `cocounsel-legal` | Suscripción del cliente; OAuth |
| **Box** | Leer archivos y carpetas en VDRs y salas de asuntos | `corporate-legal` | Tu tenant |
| **Ironclad** | Leer el registro de contratos, fechas de renovación, cláusulas | `commercial-legal` | Suscripción del cliente |
| **DocuSign / DocuSign CLM** | Estado de sobres, contratos ejecutados, metadatos de CLM | `commercial-legal` | Suscripción del cliente |
| **iManage** | Leer desde el DMS — espacios de trabajo de asuntos, versiones de documentos | `commercial-legal`, `corporate-legal` | Suscripción del cliente |
| **Everlaw** | Producciones de e-discovery, conjuntos etiquetados, cronologías | `litigation-legal` | Suscripción del cliente |
| **LegalDataHunter** | 16M+ documentos jurídicos mexicanos — SCJN IUS, Semanario Judicial, DOF, IMPI, INDAUTOR, OrdenJuridico, SAT, jurisprudencia y legislación federal y estatal | `conectores-legal-mexico` (dependencia compartida) | Clave API — vía `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico` |
| **Portal CJJ / API Nilo** | Boletín judicial y expedientes del Consejo de la Judicatura de Jalisco — juzgados mercantiles ZMG | `litigacion-legal-mexico` | Pública para boletín; credenciales Nilo para expedientes autenticados |
| **CourtListener** | Expedientes federales y opiniones | `legal-clinic`, `ip-legal`, `litigation-legal`, `law-student` | Pública; clave API opcional |
| **Trellis** | Expedientes y mociones de tribunales estatales | `litigation-legal` | Suscripción del cliente |
| **Aurora** | Gestión de asuntos estilo clínica y calendarios | `litigation-legal` | Suscripción del cliente |
| **Definely** | Redacción en documento y verificación de términos definidos | `commercial-legal`, `corporate-legal` | Suscripción del cliente |
| **Lawve AI** | Asistencia en revisión de contratos y bibliotecas de cláusulas | `legal-builder-hub` | Suscripción del cliente |
| **Courtroom5** | Flujo de trabajo para litigante sin representación | `legal-clinic` | Suscripción del cliente |
| **Descrybe** | Investigación y resumen de jurisprudencia | `legal-clinic`, `ip-legal`, `law-student` | Suscripción del cliente |
| **Solve Intelligence** | Redacción y gestión de patentes | `corporate-legal`, `ip-legal` | Suscripción del cliente |
| **TopCounsel** | Enrutamiento de asuntos y panel de abogados externos | `commercial-legal`, `corporate-legal`, `litigation-legal` | Suscripción del cliente |
| **Linear** | Rastreador de lanzamientos, seguimiento de asuntos | `product-legal` | Workspace del cliente |
| **Atlassian (Jira)** | Rastreador de lanzamientos, seguimiento de asuntos | `product-legal` | Workspace del cliente |
| **Asana** | Rastreador de lanzamientos, seguimiento de proyectos | `product-legal` | Workspace del cliente |

> Los conectores marcados "Suscripción del cliente" necesitan la propia cuenta y clave API del cliente. Para conectores de clave API en los plugins mexicanos, configura vía `claude plugin configure conectores-legal-mexico@claude-for-legal-mexico`. Para conectores OAuth (Box, Slack, Drive, iManage), autoriza a través de Claude Cowork → Configuración → Conectores, o usa `claude mcp auth` en Claude Code.

> **¿Construyendo un conector?** Ver [CONNECTORS.md](./CONNECTORS.md) para lo que es un buen servidor MCP legal y cómo enviar el tuyo para inclusión.

## Claude para Microsoft 365

Los abogados viven en Word y Excel. **Cada skill que toca contratos en este repositorio está redactado para funcionar en la barra lateral de Claude para Word, con cambios controlados como modo de salida.** Eso incluye `commercial-legal:review` (contratos con proveedores, NDAs, suscripciones SaaS), `commercial-legal:amendment-history`, `ip-legal:ip-clause-review`, `ai-governance-legal:vendor-ai-review`, `privacy-legal:dpa-review`, y la extracción de debida diligencia en `corporate-legal`. Un revisor acepta o rechaza cada cambio exactamente como lo haría para un marcado humano — numeración, términos definidos, referencias cruzadas y estilos son preservados.

Los skills de Excel producen libros de trabajo que abren limpiamente: `corporate-legal:tabular-review` escribe un `.xlsx` de múltiples hojas con una hoja de fuentes, `litigation-legal:claim-chart` escribe un cuadro de elementos por elemento con columnas de citas, `corporate-legal:entity-compliance` escribe el registro de cumplimiento con columnas de plazos, y `commercial-legal:renewal-tracker` exporta el registro de renovaciones ordenado por fecha de cancelación.

Instala Claude para Microsoft 365 desde **[Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/wa200010453)**. Una vez instalado, los skills de cualquier plugin que hayas habilitado están disponibles desde la barra lateral vía `/`, y los conectores son accesibles desde la misma superficie. Un solo hilo puede abarcar Word, Excel, PowerPoint y Outlook.

Para administradores de TI que despliegan el complemento contra tu propia nube (Vertex AI, Bedrock o una pasarela interna) en lugar de la API de Anthropic, ver el conjunto de herramientas separado [`claude-for-msft-365-install`](https://github.com/anthropics/financial-services/tree/main/claude-for-msft-365-install).

## Personalización

Estas son plantillas de referencia. Mejoran cuando las ajustas a cómo trabaja tu equipo — y el mecanismo de personalización es el plugin mismo, no un archivo de configuración enterrado en un repositorio.

- **Ejecuta la entrevista de configuración.** **Es** el mecanismo de personalización. Pregunta cómo funciona tu práctica, lee tus documentos semilla y escribe tu perfil de práctica. Cada otro skill lee de ese perfil. Un `/commercial-legal:cold-start-interview` con cinco MSAs firmados, tu playbook y tu matriz de escalada hará que los skills de revisión sean notablemente más precisos.
- **Edita el perfil de práctica.** Tu perfil vive en `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`. Edítalo directamente para correcciones pequeñas — un umbral de escalada incorrecto, una nueva integración, una actualización de política. Sobrevive las actualizaciones del plugin.
- **Vuelve a ejecutar la configuración.** `/<plugin>:cold-start-interview` de nuevo para una re-entrevista completa cuando tu práctica cambia materialmente (nueva jurisdicción, nuevo CLM, nueva política).
- **Intercambia conectores.** Apunta `.mcp.json` a tu CLM, DMS, plataforma de e-discovery, rastreador de lanzamientos, HRIS. Los skills fallan elegantemente cuando un conector no está configurado — sin no-ops silenciosos.
- **Trae tu playbook y plantillas.** Agrega tu terminología, estilo de la casa y plantillas con marca al `CLAUDE.md` y `references/` del plugin. Los skills los tomarán.
- **Bifurca skills para el estilo de la casa.** Cada skill es un archivo markdown bajo `skills/`. Edita los pasos, las compuertas, el formato de salida.
- **Agrega agentes programados.** Los agentes bajo `<plugin>/agents/` son markdown con un horario estilo cron. Agrega los tuyos para los vigilantes que necesita tu equipo.

Sin paso de compilación. Todo es markdown y JSON.

## Referencia de Skills y Comandos

El mapa completo a través de todos los plugins. La entrevista de configuración es lo primero que hay que ejecutar en cualquier plugin.

### ai-governance-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/ai-governance-legal:cold-start-interview` | cold-start-interview | Configuración inicial — aprende tu práctica de gobernanza de IA |
| `/ai-governance-legal:ai-inventory` | ai-inventory | Inventario por sistema bajo el EU AI Act — rastrea el rol y nivel de riesgo de cada sistema |
| `/ai-governance-legal:use-case-triage` | use-case-triage | Clasifica caso de uso de IA — aprobado, condicional, o no |
| `/ai-governance-legal:aia-generation` | aia-generation | Ejecuta una evaluación de impacto de IA en formato casa |
| `/ai-governance-legal:vendor-ai-review` | vendor-ai-review | Revisa términos de IA de proveedor contra posiciones de gobernanza |
| `/ai-governance-legal:reg-gap-analysis` | reg-gap-analysis | Coteja una nueva regulación de IA contra tu postura de gobernanza |
| `/ai-governance-legal:policy-monitor` | policy-monitor | Mantiene la política de IA al día con la práctica |
| `/ai-governance-legal:policy-starter` | policy-starter | Redacta una política de uso de IA de la firma adaptada a tu perfil de práctica |
| `/ai-governance-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |

### legal-builder-hub

| Comando | Skill | Qué hace |
|---|---|---|
| `/legal-builder-hub:cold-start-interview` | cold-start-interview | Entrevista de perfil de práctica y recomendación de paquete inicial |
| `/legal-builder-hub:registry-browser` | registry-browser | Busca skills legales de comunidad en registros vigilados |
| `/legal-builder-hub:skill-installer` | skill-installer | Instala un skill de comunidad con verificaciones de confianza |
| `/legal-builder-hub:skills-qa` | skills-qa | Evalúa un skill contra el Marco de Diseño |
| `/legal-builder-hub:related-skills-surfacer` | related-skills-surfacer | Sugiere skills de comunidad por actividad en otros plugins |
| `/legal-builder-hub:auto-updater` | auto-updater | Verifica actualizaciones de skills de comunidad instalados |
| `/legal-builder-hub:disable` | skill-manager | Deshabilita un skill de comunidad sin eliminar archivos |
| `/legal-builder-hub:uninstall` | skill-manager | Desinstala un skill de comunidad instalado vía el hub |
| programado | registry-sync (agente) | Verificación periódica de registros vigilados por actualizaciones |

### legal-clinic

| Comando | Skill | Qué hace |
|---|---|---|
| `/legal-clinic:cold-start-interview` | cold-start-interview | Configuración del profesor — áreas, jurisdicción, estilo de supervisión |
| `/legal-clinic:build-guide` | build-guide | Guía de práctica por área del profesor — intake, postura pedagógica, compuertas de revisión |
| `/legal-clinic:ramp` | ramp | Incorporación de estudiante al semestre con ejercicios de práctica |
| `/legal-clinic:client-intake` | client-intake | Intake estructurado con identificación de problemas entre áreas |
| `/legal-clinic:client-comms-log` | client-comms-log | Registra una comunicación con cliente — registro solo-adjunta por caso |
| `/legal-clinic:research-start` | research-start | Hoja de ruta de investigación — estatutos, jurisprudencia, términos de búsqueda |
| `/legal-clinic:memo` | memo | Memo de análisis con estructura IRAC y brechas de investigación señaladas |
| `/legal-clinic:draft` | draft | Primer borrador de un documento común de clínica |
| `/legal-clinic:client-letter` | client-letter · plain-language-letters | Correspondencia rutinaria con clientes desde plantillas |
| `/legal-clinic:status` | status | Estatus del caso por audiencia — cliente, profesor, listo para tribunal |
| `/legal-clinic:deadlines` | deadlines | Rastrea plazos de caso con advertencias de responsabilidad profesional |
| `/legal-clinic:supervisor-review-queue` | supervisor-review-queue | Cola de revisión del profesor (si supervisión formal) |
| `/legal-clinic:semester-handoff` | semester-handoff | Memos de entrega de casos al fin de semestre |

### commercial-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/commercial-legal:cold-start-interview` | cold-start-interview | Configuración inicial — aprende tu práctica de contratos comerciales |
| `/commercial-legal:review` | vendor-agreement-review · nda-review · saas-msa-review | Revisa contrato con proveedor, NDA o suscripción SaaS |
| `/commercial-legal:amendment-history` | amendment-history | Traza cambios contractuales a través del acuerdo base y enmiendas |
| `/commercial-legal:renewal-tracker` | renewal-tracker | Muestra contratos con plazos de cancelación dentro de 90 días |
| `/commercial-legal:escalation-flagger` | escalation-flagger | Enruta un asunto contractual y redacta la solicitud |
| `/commercial-legal:review-proposals` | (interno) | Revisa y aprueba propuestas pendientes de actualización de playbook |
| `/commercial-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| — | stakeholder-summary | Traduce una revisión en resumen para partes interesadas del negocio |
| programado | renewal-watcher (agente) | Barrido semanal del registro de renovaciones |
| programado | deal-debrief (agente) | Superficie semanal de acuerdos firmados con desviaciones |
| programado | playbook-monitor (agente) | Propone actualizaciones de playbook cuando una cláusula ha derivado |

### corporate-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/corporate-legal:cold-start-interview` | cold-start-interview | Configuración de la casa, con opción `--new-deal` de inicio |
| `/corporate-legal:tabular-review` | tabular-review | Revisión tabular — una fila por documento, cada celda citada |
| `/corporate-legal:diligence-issue-extraction` | diligence-issue-extraction | Extrae hallazgos de documentos VDR según umbrales de la casa |
| `/corporate-legal:material-contract-schedule` | material-contract-schedule | Construye el calendario de contratos materiales para disclosure schedule |
| `/corporate-legal:closing-checklist` | closing-checklist | Qué bloquea el cierre con ruta crítica |
| `/corporate-legal:written-consent` | written-consent | Redacta consentimiento del consejo o comité en formato casa |
| `/corporate-legal:entity-compliance` | entity-compliance | Rastreador de cumplimiento de entidades por jurisdicción |
| `/corporate-legal:integration-management` | integration-management | Rastreador de integración post-cierre con seguimiento de consentimientos |
| `/corporate-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| — | board-minutes | Redacta actas del consejo o comité en formato casa |
| — | deal-team-summary | Agrega hallazgos de debida diligencia en briefing del equipo de deal |
| — | ai-tool-handoff | Detecta Luminance/Kira, controla calidad de salida de herramienta masiva |
| programado | dataroom-watcher (agente) | Monitorea cargas al VDR y publica estatus de lista de cierre |

### employment-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/employment-legal:cold-start-interview` | cold-start-interview | Configuración inicial — aprende jurisdicciones y reglas de escalada |
| `/employment-legal:wage-hour-qa` | wage-hour-qa | Q&A laboral y de salarios/jornada consciente de jurisdicción |
| `/employment-legal:hiring-review` | hiring-review | Revisa carta de oferta y cláusulas restrictivas |
| `/employment-legal:termination-review` | termination-review | Revisión de terminación con detección de banderas de alto riesgo |
| `/employment-legal:worker-classification` | worker-classification | Clasifica un contrato propuesto contra el test de la jurisdicción |
| `/employment-legal:policy-drafting` | policy-drafting | Redacta política laboral con suplementos estatales |
| `/employment-legal:leave-tracker` | leave-tracker | Verifica ausencias abiertas por alertas de plazo |
| `/employment-legal:log-leave` | log-leave | Agrega una nueva ausencia al registro de ausencias |
| `/employment-legal:investigation-open` | internal-investigation | Abre un nuevo asunto de investigación interna |
| `/employment-legal:investigation-add` | internal-investigation | Agrega datos a una investigación abierta — documentos, notas |
| `/employment-legal:investigation-memo` | internal-investigation | Redacta o actualiza el memo de investigación privilegiado |
| `/employment-legal:investigation-query` | internal-investigation | Hace preguntas contra un log de investigación abierto |
| `/employment-legal:investigation-summary` | internal-investigation | Redacta resumen por audiencia desde el memo de investigación |
| `/employment-legal:expansion-kickoff` | international-expansion | Inicia la planificación de expansión para un nuevo país |
| `/employment-legal:expansion-update` | international-expansion | Actualiza el estatus de un proyecto de expansión en curso |
| `/employment-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| — | handbook-updates | Coteja cambios al manual y señala impactos en suplementos estatales |
| programado | leave-tracker (agente) | Monitor semanal de ausencias abiertas con plazos duros |

### ip-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/ip-legal:cold-start-interview` | cold-start-interview | Configuración inicial — aprende tu práctica y postura de PI |
| `/ip-legal:clearance` | clearance | Primera revisión de disponibilidad de marca — knockout + marcas similares |
| `/ip-legal:fto-triage` | fto-triage | Triaje de libertad de operación, no una opinión de FTO |
| `/ip-legal:invention-intake` | invention-intake | Primera revisión de divulgación de invención — novedad, obviedad, §101, fechas críticas |
| `/ip-legal:cease-desist` | cease-desist | Redacta una C&D o triaje de una recibida |
| `/ip-legal:takedown` | takedown | Aviso DMCA, triaje de respuesta, o contra-aviso §512(g) |
| `/ip-legal:infringement-triage` | infringement-triage | Triaje de infracción en los cuatro derechos de PI |
| `/ip-legal:ip-clause-review` | ip-clause-review | Revisa cláusulas de PI — cesión, licencia, garantías |
| `/ip-legal:oss-review` | oss-review | Verificación de cumplimiento de licencias de código abierto |
| `/ip-legal:portfolio` | portfolio | Rastrea plazos y renovaciones del portafolio de PI |
| `/ip-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| programado | ip-renewal-watcher (agente) | Reporte semanal de plazos del portafolio de PI |

### litigation-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/litigation-legal:cold-start-interview` | cold-start-interview | Configuración inicial — riesgo, panorama, estilo de escrito casa |
| `/litigation-legal:matter-intake` | matter-intake | Intake de nuevo asunto — escribe matter.md y history |
| `/litigation-legal:matter-briefing` | matter-briefing | Briefing profundo de un asunto para una llamada |
| `/litigation-legal:matter-update` | matter-update | Adjunta un evento fechado al historial de un asunto |
| `/litigation-legal:portfolio-status` | portfolio-status | Resumen del portafolio — riesgo, plazos, asuntos sin movimiento |
| `/litigation-legal:matter-close` | matter-close | Cierra un asunto — archiva, conserva registro |
| `/litigation-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| `/litigation-legal:demand-intake` | demand-intake | Contexto pre-redacción — partes, hechos, palanca |
| `/litigation-legal:demand-draft` | demand-draft | Redacta carta de requerimiento con compuerta FRE 408 y salida .docx |
| `/litigation-legal:demand-received` | demand-received | Triaje de requerimiento entrante — opciones, cotejo con portafolio |
| `/litigation-legal:subpoena-triage` | subpoena-triage | Triaje de citatorio — alcance, carga, privilegio, plan |
| `/litigation-legal:legal-hold` | legal-hold | Emitir, refrescar, liberar o reportar sobre retenciones documentales |
| `/litigation-legal:oc-status` | oc-status | Emails de solicitud de estatus semanal a abogados externos |
| `/litigation-legal:claim-chart` | claim-chart | Cuadro de elementos — patente o causa de acción civil |
| `/litigation-legal:chronology` | chronology | Construye o actualiza una cronología desde fuentes y cargas |
| `/litigation-legal:deposition-prep` | deposition-prep | Esquema de deposición vinculado a la teoría del caso |
| `/litigation-legal:privilege-log-review` | privilege-log-review | Primera revisión del registro de privilegio con señalamientos |
| `/litigation-legal:brief-section-drafter` | brief-section-drafter | Redacta una sección de escrito en estilo casa |
| programado | docket-watcher (agente) | Monitorea expedientes judiciales por presentaciones y plazos |

### privacy-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/privacy-legal:cold-start-interview` | cold-start-interview | Configuración inicial — aprende tu práctica de privacidad |
| `/privacy-legal:use-case-triage` | use-case-triage | Determina PIA vs DPIA de GDPR vs proceder |
| `/privacy-legal:pia-generation` | pia-generation | Genera una Evaluación de Impacto de Privacidad en formato casa |
| `/privacy-legal:dpa-review` | dpa-review | Revisa un DPA — detecta automáticamente responsable vs encargado |
| `/privacy-legal:dsar-response` | dsar-response | Acompaña un DSAR y redacta la respuesta — verificar, localizar, evaluar |
| `/privacy-legal:reg-gap-analysis` | reg-gap-analysis | Coteja una regulación contra la política y práctica actual |
| `/privacy-legal:policy-monitor` | policy-monitor | Mantiene la política de privacidad al día con la práctica |
| `/privacy-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |

### product-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/product-legal:cold-start-interview` | cold-start-interview | Configuración inicial — conecta rastreador de lanzamientos, aprende calibración |
| `/product-legal:is-this-a-problem` | is-this-a-problem | Respuesta rápida "¿esto es un problema?" para preguntas rápidas |
| `/product-legal:launch-review` | launch-review | Revisión completa de lanzamiento contra marco y calibración |
| `/product-legal:marketing-claims-review` | marketing-claims-review | Revisa copia de marketing por claims que necesitan trabajo |
| `/product-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| — | feature-risk-assessment | Análisis profundo de riesgo en una sola funcionalidad cuando la revisión de lanzamiento lo señala |
| programado | launch-watcher (agente) | Monitorea rastreador de lanzamientos por revisiones próximas |

### regulatory-legal

| Comando | Skill | Qué hace |
|---|---|---|
| `/regulatory-legal:cold-start-interview` | cold-start-interview | Configuración inicial — lista de vigilados, índice de políticas, materialidad |
| `/regulatory-legal:reg-feed-watcher` | reg-feed-watcher | Consulta feeds regulatorios ahora y reporta novedades |
| `/regulatory-legal:policy-diff` | policy-diff | Coteja un cambio regulatorio contra la biblioteca de políticas |
| `/regulatory-legal:gaps` | gap-surfacer | Rastreador de brechas abiertas — qué está señalado y no cerrado |
| `/regulatory-legal:policy-redraft` | policy-redraft | Borrador de política cerrando una brecha — propuesta para revisión del dueño de política |
| `/regulatory-legal:comments` | (rastreador) | Revisa períodos abiertos de comentarios NPRM y plazos |
| `/regulatory-legal:matter-workspace` | matter-workspace | Gestiona espacios de trabajo de asuntos (nivel de práctica) |
| programado | reg-change-monitor (agente) | Barrido programado de feeds regulatorios con filtro de materialidad |

### law-student

| Comando | Skill | Qué hace |
|---|---|---|
| `/law-student:cold-start-interview` | cold-start-interview | Entrevista sobre ti — clases, examen de barra, estilo de aprendizaje |
| `/law-student:socratic-drill` | socratic-drill | Taladro socrático — él pregunta, tú respondes, él contraargumenta |
| `/law-student:case-brief` | case-brief | Resume un caso en tu formato preferido |
| `/law-student:outline-builder` | outline-builder | Construye o extiende un esquema en tu formato |
| `/law-student:irac-practice` | irac-practice | Califica ensayo IRAC — estructura, problemas, reglas, análisis |
| `/law-student:legal-writing` | legal-writing | Retroalimentación estructural sobre tu escritura — nunca reescribe |
| `/law-student:cold-call-prep` | cold-call-prep | Predice las preguntas del profesor y las practica |
| `/law-student:bar-prep-questions` | bar-prep-questions | Preguntas de MBE o ensayo dirigidas a materias débiles |
| `/law-student:flashcards` | flashcards | Genera o practica tarjetas — cubetas estilo Leitner |
| `/law-student:exam-forecast` | exam-forecast | Analiza exámenes pasados para pronosticar énfasis probables |
| `/law-student:study-plan` | study-plan | Construye o actualiza un plan de estudio a largo plazo |
| `/law-student:session` | study-plan | Ejecuta una sesión enfocada de N preguntas; actualiza el plan |

### conectores-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/conectores-legal-mexico:setup-completo` | setup-completo | Configura los plugins en secuencia — conectores → corporativo → litigacion → PI. Pregunta empresa/industria/jurisdicción una sola vez. Flags: `--redo`, `--from <plugin>`, `--check-integrations` |
| `/conectores-legal-mexico:cold-start-interview` | cold-start-interview | Configura solo los conectores MCP — verifica conectividad con llamada real, guía configuración de LegalDataHunter y CJJ |
| `/conectores-legal-mexico:customize` | customize | Ajusta un conector específico (canal Slack, clave API, estado) sin re-entrevista completa |

### corporativo-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/corporativo-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica corporativa |
| `/corporativo-legal-mexico:tabular-review` | tabular-review | Revisión tabular de data room — una fila por documento, cada celda citada |
| `/corporativo-legal-mexico:diligence-issue-extraction` | diligence-issue-extraction | Extrae hallazgos de VDR según categorías y umbrales de materialidad |
| `/corporativo-legal-mexico:material-contract-schedule` | material-contract-schedule | Construye calendario de contratos materiales para disclosure schedule |
| `/corporativo-legal-mexico:closing-checklist` | closing-checklist | Condiciones, consentimientos, documentos y filings pendientes para cierre |
| `/corporativo-legal-mexico:written-consent` | written-consent | Redacta consentimiento escrito de Consejo o Asamblea en formato casa |
| `/corporativo-legal-mexico:board-minutes` | board-minutes | Redacta Acta de Sesión del Consejo de Administración |
| `/corporativo-legal-mexico:entity-compliance` | entity-compliance | Seguimiento de obligaciones corporativas por entidad y jurisdicción |
| `/corporativo-legal-mexico:integration-management` | integration-management | Plan de integración post-cierre con seguimiento de consentimientos |
| `/corporativo-legal-mexico:deal-team-summary` | deal-team-summary | Agrega hallazgos de debida diligencia en briefing ejecutivo |
| `/corporativo-legal-mexico:ai-tool-handoff` | ai-tool-handoff | Detecta salida de herramienta de revisión masiva y ejecuta QA |
| `/corporativo-legal-mexico:matter-workspace` | matter-workspace | Administra espacios de trabajo por asunto |
| `/corporativo-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista completa |

### litigacion-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/litigacion-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — riesgo, panorama, estilo casa |
| `/litigacion-legal-mexico:matter-intake` | matter-intake | Intake de asunto nuevo — escribe matter.md, history.md, log |
| `/litigacion-legal-mexico:matter-briefing` | matter-briefing | Briefing profundo de un asunto para llamada con DJ u OC |
| `/litigacion-legal-mexico:matter-update` | matter-update | Agrega evento fechado al historial del asunto |
| `/litigacion-legal-mexico:portfolio-status` | portfolio-status | Resumen del portafolio — riesgo, plazos, asuntos sin movimiento |
| `/litigacion-legal-mexico:matter-close` | matter-close | Cierra asunto — archiva, conserva registro |
| `/litigacion-legal-mexico:matter-workspace` | matter-workspace | Administra espacios de trabajo por asunto |
| `/litigacion-legal-mexico:demand-intake` | demand-intake | Pre-redacción — partes, hechos, fundamentos, palanca, privilegio |
| `/litigacion-legal-mexico:demand-draft` | demand-draft | Redacta carta de requerimiento con compuerta pre-envío y salida .docx |
| `/litigacion-legal-mexico:demand-received` | demand-received | Triaje de requerimiento recibido — opciones, portafolio, entrega |
| `/litigacion-legal-mexico:requerimiento-triage` | requerimiento-triage | Triaje rápido de requerimiento externo recibido |
| `/litigacion-legal-mexico:legal-hold` | legal-hold | Emite, refresca, libera o reporta sobre retenciones documentales |
| `/litigacion-legal-mexico:oc-status` | oc-status | Genera borradores de solicitud de estatus semanal a abogados externos |
| `/litigacion-legal-mexico:claim-chart` | claim-chart | Cuadro de elementos — patente o causa de acción civil/mercantil |
| `/litigacion-legal-mexico:chronology` | chronology | Construye o actualiza cronología desde fuentes y cargas |
| `/litigacion-legal-mexico:plantillas-demanda` | plantillas-demanda | Plantillas de demanda para 7 tipos de juicio: ordinario mercantil, ejecutivo mercantil, oral mercantil, ordinario civil, hipotecario, requerimiento de pago, arrendamiento/renta |
| `/litigacion-legal-mexico:redaccion-escritos` | redaccion-escritos | Redacta escritos judiciales en formato procesal mexicano |
| `/litigacion-legal-mexico:preparacion-pruebas` | preparacion-pruebas | Organiza y prepara pruebas para audiencia o período probatorio |
| `/litigacion-legal-mexico:revision-confidencialidad` | revision-confidencialidad | Revisión de registros de confidencialidad y secreto profesional |
| `/litigacion-legal-mexico:revision-expedientes-jalisco` | revision-expedientes-jalisco | Consulta expedientes en el sistema Nilo del CJJ (Jalisco) |
| `/litigacion-legal-mexico:boletin-monitor` | boletin-monitor | Monitorea el boletín diario del CJJ por nombre de parte |
| `/litigacion-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |
| — | verificador-juridico (agente) | QA jurídica de skills y documentos — verifica plazos, artículos, vigencia contra fuentes primarias |
| programado | vigilante-expedientes (agente) | Vigila expedientes judiciales; calcula plazos; publica reporte de estado |

### propiedad-intelectual-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/propiedad-intelectual-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — IMPI, INDAUTOR, postura de enforcement |
| `/propiedad-intelectual-legal-mexico:portafolio` | portafolio | Seguimiento de marcas, patentes y derechos de autor ante IMPI e INDAUTOR |
| `/propiedad-intelectual-legal-mexico:clearance` | clearance | Búsqueda de disponibilidad de marca — knockout + marcas similares |
| `/propiedad-intelectual-legal-mexico:fto-triage` | fto-triage | Triaje FTO — primera mirada a patentes potencialmente bloqueantes |
| `/propiedad-intelectual-legal-mexico:invention-intake` | invention-intake | Primera revisión de divulgación de invención — novedad, actividad inventiva |
| `/propiedad-intelectual-legal-mexico:triaje-infraccion` | triaje-infraccion | Triaje de infracción en los cuatro derechos de PI |
| `/propiedad-intelectual-legal-mexico:carta-requerimiento` | carta-requerimiento | Redacta o triaje carta de requerimiento / cesación |
| `/propiedad-intelectual-legal-mexico:notificacion-infraccion` | notificacion-infraccion | Notificación de infracción ante IMPI (procedimiento administrativo) |
| `/propiedad-intelectual-legal-mexico:revision-clausulas-pi` | revision-clausulas-pi | Revisa cláusulas de PI — cesión, licencia, garantías, indemnidades |
| `/propiedad-intelectual-legal-mexico:reservas-derechos` | reservas-derechos | Registro y seguimiento de reservas de derechos ante INDAUTOR (LFDA Art. 173) |
| `/propiedad-intelectual-legal-mexico:oss-review` | oss-review | Revisión de cumplimiento de licencias de código abierto |
| `/propiedad-intelectual-legal-mexico:matter-workspace` | matter-workspace | Administra espacios de trabajo por asunto |
| `/propiedad-intelectual-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |
| programado | vigilante-renovaciones (agente) | Reporte semanal de vencimientos de PI — marcas, patentes, reservas |

### laboral-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/laboral-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica laboral |
| `/laboral-legal-mexico:termination-risk` | termination-risk | Análisis de riesgo de terminación con banderas LFT por escenario |
| `/laboral-legal-mexico:liquidacion-calculator` | liquidacion-calculator | Calcula liquidación constitucional (3 meses + 20 días/año) + proporcionales |
| `/laboral-legal-mexico:matter-intake` | matter-intake | Intake de asunto laboral — hechos, fundamento, exposición económica |
| `/laboral-legal-mexico:imss-infonavit-review` | imss-infonavit-review | Revisión de cumplimiento IMSS/INFONAVIT — cuotas, avisos, SUA |
| `/laboral-legal-mexico:nom-compliance` | nom-compliance | Evaluación de cumplimiento NOM-035/037-STPS — factores de riesgo psicosocial |
| `/laboral-legal-mexico:plataformas-digitales` | plataformas-digitales | Clasificación y cumplimiento para trabajadores de plataformas digitales |
| `/laboral-legal-mexico:plazo-calendar` | plazo-calendar | Calendario de plazos fatales procesales en materia laboral |
| `/laboral-legal-mexico:escrito-laboral` | escrito-laboral | Redacta escritos laborales en formato procesal mexicano |
| `/laboral-legal-mexico:cjfca-conciliacion` | cjfca-conciliacion | Preparación y seguimiento de conciliación ante el CJFCA |
| `/laboral-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |
| programado | vigilante-plazos-laborales (agente) | Monitor semanal de plazos fatales laborales del portafolio |

### privacidad-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/privacidad-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica de privacidad |
| `/privacidad-legal-mexico:aviso-privacidad` | aviso-privacidad | Redacta y revisa avisos de privacidad bajo la LGPDPPSP y LFPDPPP |
| `/privacidad-legal-mexico:arco-response` | arco-response | Gestiona solicitudes ARCO con cómputo de plazos hábiles |
| `/privacidad-legal-mexico:contrato-datos` | contrato-datos | Revisa y redacta contratos con encargados de tratamiento |
| `/privacidad-legal-mexico:eipd` | eipd | Evaluación de Impacto en la Protección de Datos (EIPD) |
| `/privacidad-legal-mexico:gap-analysis` | gap-analysis | Análisis de brecha de cumplimiento contra la LGPDPPSP/LFPDPPP |
| `/privacidad-legal-mexico:inai-procedimiento` | inai-procedimiento | Preparación de procedimientos ante el INAI |
| `/privacidad-legal-mexico:transferencias-internacionales` | transferencias-internacionales | Análisis y documentación de transferencias internacionales de datos |
| `/privacidad-legal-mexico:vulneracion-notificacion` | vulneracion-notificacion | Notificación de vulneraciones de seguridad en 72 horas |
| `/privacidad-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |

### regulatorio-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/regulatorio-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — reguladores vigilados, umbral de materialidad |
| `/regulatorio-legal-mexico:cofece-triage` | cofece-triage | Triaje de asuntos de competencia económica bajo la LFCE |
| `/regulatorio-legal-mexico:cofepris-tramite` | cofepris-tramite | Preparación de trámites sanitarios ante la COFEPRIS |
| `/regulatorio-legal-mexico:dof-digest` | dof-digest | Resumen y análisis de publicaciones relevantes del DOF |
| `/regulatorio-legal-mexico:comentarios-regulatorios` | comentarios-regulatorios | Redacta comentarios públicos a proyectos normativos |
| `/regulatorio-legal-mexico:respuesta-regulador` | respuesta-regulador | Redacta respuesta a requerimiento de cualquier regulador federal |
| `/regulatorio-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |
| programado | monitor-dof (agente) | Vigilancia semanal del DOF — normas, decretos y resoluciones relevantes |

### fiscal-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/fiscal-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica fiscal |
| `/fiscal-legal-mexico:cfdi-review` | cfdi-review | Revisión de CFDI 4.0 — estructura, requisitos, complementos |
| `/fiscal-legal-mexico:sat-discrepancy` | sat-discrepancy | Análisis de discrepancias y requerimientos del SAT |
| `/fiscal-legal-mexico:auditoria-sat` | auditoria-sat | Preparación para auditorías SAT — visita domiciliaria, revisión de gabinete |
| `/fiscal-legal-mexico:tfja-litigacion` | tfja-litigacion | Litigación contencioso-administrativa ante el TFJA |
| `/fiscal-legal-mexico:prodecon-tramite` | prodecon-tramite | Gestión de procedimientos PRODECON — acuerdo conclusivo, queja |
| `/fiscal-legal-mexico:planeacion-fiscal` | planeacion-fiscal | Análisis de opciones de planeación fiscal lícita — tratados de doble imposición |
| `/fiscal-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |

### ia-governanza-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/ia-governanza-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica de gobernanza de IA |
| `/ia-governanza-legal-mexico:use-case-triage` | use-case-triage | Clasifica casos de uso de IA — registro, riesgo EU AI Act, nexo europeo |
| `/ia-governanza-legal-mexico:impact-assessment` | impact-assessment | Evaluación de impacto de IA en los regímenes en alcance |
| `/ia-governanza-legal-mexico:vendor-contract-review` | vendor-contract-review | Revisa contratos con proveedores de IA — titularidad, entrenamiento, responsabilidad |
| `/ia-governanza-legal-mexico:eu-ai-act-exposure` | eu-ai-act-exposure | Análisis de exposición al EU AI Act para operaciones con nexo UE |
| `/ia-governanza-legal-mexico:ai-policy-draft` | ai-policy-draft | Redacta políticas internas de uso de IA |
| `/ia-governanza-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |

### seguros-legal-mexico

| Comando | Skill | Qué hace |
|---|---|---|
| `/seguros-legal-mexico:cold-start-interview` | cold-start-interview | Entrevista de configuración — perfil de práctica de seguros y fianzas |
| `/seguros-legal-mexico:poliza-review` | poliza-review | Revisión de pólizas de seguros y fianzas — cobertura, exclusiones, condiciones |
| `/seguros-legal-mexico:siniestro-intake` | siniestro-intake | Intake y análisis inicial de siniestro — hechos, cobertura, plazo de reclamación |
| `/seguros-legal-mexico:cobertura-analysis` | cobertura-analysis | Análisis de cobertura para disputas — aplicabilidad, exclusiones, sublímites |
| `/seguros-legal-mexico:cnsf-compliance` | cnsf-compliance | Cumplimiento regulatorio ante la CNSF — circulares, obligaciones periódicas |
| `/seguros-legal-mexico:producto-filing` | producto-filing | Registro y actualización de productos ante la CNSF |
| `/seguros-legal-mexico:reaseguro-review` | reaseguro-review | Revisión de contratos de reaseguro y retrocesión |
| `/seguros-legal-mexico:solvencia-rcs` | solvencia-rcs | Análisis de requerimiento de capital de solvencia (RCS) |
| `/seguros-legal-mexico:recurso-condusef` | recurso-condusef | Preparación de recursos de revisión y respuesta ante la CONDUSEF |
| `/seguros-legal-mexico:customize` | customize | Personaliza el perfil de práctica sin re-entrevista |

### cocounsel-legal (Thomson Reuters)

| Comando | Skill | Qué hace |
|---|---|---|
| `/cocounsel-legal:deep-research` | deep-research | Ejecuta Westlaw Deep Research — inicia, consulta y presenta un reporte completamente citado |

## Contribuciones

Todo aquí es markdown y JSON. Bifurca, edita, PR.

- **Nuevo skill** → agrégalo bajo `<plugin>/skills/<nombre-del-skill>/SKILL.md` con el frontmatter que usan los skills existentes (`name`, `description`, `argument-hint`). Mantén la descripción bajo 1024 caracteres — es la señal de activación. El skill es invocable como `/<plugin>:<nombre-del-skill>`. Marca los skills de pura referencia como `user-invocable: false`.
- **Nuevo agente** → agrega `<plugin>/agents/<nombre>.md` con frontmatter de programación y el system prompt. Agrega un `managed-agent-cookbooks/<nombre>/` correspondiente si quieres despliegue sin cabeza.
- **Skills de comunidad** → usa `/legal-builder-hub:skill-installer` para probar un skill de comunidad en tu entorno. El hub ejecuta `/legal-builder-hub:skills-qa` contra cada skill antes de instalar — puntúa el skill contra el Marco de Diseño de Skills Legales (nueve parámetros de diseño, tres modos de falla legal, una verificación de superficie de confianza) y rechaza cualquiera que falle.
- **Valida cookbooks antes de hacer push** → `bash scripts/test-cookbooks.sh` ejecuta en seco cada cookbook de agente gestionado y revisa el alcance de herramientas del orquestador.

## Licencia

Licenciado bajo la [Licencia Apache, Versión 2.0](LICENSE).

Copyright 2026 Anthropic PBC.
