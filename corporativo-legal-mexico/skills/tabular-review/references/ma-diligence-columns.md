# Debida Diligencia de F&A — Conjunto Estándar de Columnas

El esquema predeterminado para una revisión de contratos de la sociedad objetivo del lado comprador. Comienza aquí, luego añade o elimina columnas según la operación. Este es un punto de partida, no una lista de verificación exhaustiva — las declaraciones del Contrato de Compraventa de Acciones y la lista de requerimientos determinan lo que realmente importa.

```yaml
schema:
  name: "Debida Diligencia F&A — Estándar"
  columns:
    - id: counterparty
      label: "Contraparte"
      type: verbatim
      prompt: "Nombre de la parte contratante distinta de la sociedad objetivo, exactamente como aparece."

    - id: agreement_type
      label: "Tipo de Contrato"
      type: classify
      options: [msa, purchase_order, license_in, license_out, lease, services, supply, distribution, nda, joint_venture, loan, guaranty, employment, other]
      prompt: "¿Qué tipo de contrato es?"

    - id: effective_date
      label: "Fecha de Vigencia"
      type: date
      prompt: "¿Cuándo entró en vigor este contrato?"

    - id: term
      label: "Vigencia"
      type: duration
      prompt: "¿Cuál es el plazo inicial?"

    - id: auto_renewal
      label: "Renovación Automática"
      type: classify
      options: [none, annual, fixed_period, evergreen]
      prompt: "¿El contrato se renueva automáticamente? ¿Con qué periodicidad?"

    - id: termination_for_convenience
      label: "Terminación sin Causa"
      type: classify
      options: [none, either_party, target_only, counterparty_only]
      prompt: "¿Alguna de las partes puede dar por terminado sin causa? ¿Quién?"

    - id: termination_notice
      label: "Plazo de Aviso de Terminación"
      type: duration
      prompt: "¿Con cuánta anticipación se debe notificar la terminación?"

    - id: change_of_control
      label: "Cambio de Control"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, automatic_termination, notice_only, counterparty_right_to_terminate]
      prompt: "¿El contrato aborda un cambio de control de la sociedad objetivo? ¿Qué lo detona y qué consecuencias tiene?"

    - id: assignment
      label: "Cesión"
      type: classify
      options: [silent, consent_required, consent_not_unreasonably_withheld, freely_assignable, assignable_to_affiliates, non_assignable]
      prompt: "¿Puede la sociedad objetivo ceder este contrato? ¿Qué restricciones aplican?"

    - id: exclusivity
      label: "Exclusividad / Cláusula de No Competencia"
      type: classify
      options: [none, exclusive_supplier, exclusive_customer, non_compete, non_solicit, territory_restriction, most_favored_nation]
      prompt: "¿El contrato restringe a alguna de las partes de competir o contratar con terceros?"

    - id: liability_cap
      label: "Límite de Responsabilidad"
      type: currency
      prompt: "¿Existe un límite de responsabilidad? ¿Cuál es el monto o multiplicador?"

    - id: indemnification
      label: "Indemnización"
      type: classify
      options: [none, mutual, target_indemnifies, counterparty_indemnifies, ip_only, third_party_claims_only]
      prompt: "¿Quién indemniza a quién y por qué conceptos?"

    - id: governing_law
      label: "Ley Aplicable"
      type: verbatim
      prompt: "¿Qué legislación rige el contrato?"

    - id: dispute_resolution
      label: "Resolución de Controversias"
      type: classify
      options: [litigation, arbitration_binding, arbitration_nonbinding, mediation_first, silent]
      prompt: "¿Cómo se resuelven las controversias?"

    - id: most_favored_nation
      label: "Nación Más Favorecida / Protección de Precios"
      type: classify
      options: [none, mfn_pricing, price_matching, benchmarking_right]
      prompt: "¿Existe una cláusula de nación más favorecida o de protección de precios?"

    - id: minimum_commitments
      label: "Compromisos Mínimos de Compra / Volumen"
      type: currency
      prompt: "¿Existen compromisos mínimos de compra, volumen o gasto?"

    - id: ip_ownership
      label: "Titularidad de Propiedad Intelectual"
      type: classify
      options: [each_owns_own, target_owns_work_product, counterparty_owns_work_product, joint, license_only, silent]
      prompt: "¿Quién es titular de la propiedad intelectual creada o utilizada bajo el contrato?"

    - id: confidentiality_term
      label: "Supervivencia de Confidencialidad"
      type: duration
      prompt: "¿Por cuánto tiempo sobreviven las obligaciones de confidencialidad después de la terminación?"

    - id: insurance_requirements
      label: "Requisitos de Seguro"
      type: classify
      options: [none, general_liability, professional_liability, cyber, workers_comp, umbrella]
      prompt: "¿Qué seguros deben mantenerse vigentes?"

    - id: audit_rights
      label: "Derechos de Auditoría"
      type: classify
      options: [none, counterparty_may_audit_target, target_may_audit_counterparty, mutual]
      prompt: "¿Alguna de las partes tiene derechos de auditoría?"

    - id: notices
      label: "Requisitos de Notificación"
      type: verbatim
      prompt: "¿Cuál es el domicilio y método de notificación de la sociedad objetivo?"
```

## Adiciones comunes por tipo de operación

- **Tecnología / objetivos con alta carga de PI:** custodia de código fuente (_escrow_), restricciones de código abierto, derechos sobre datos, derechos de entrenamiento de modelos, acceso a APIs
- **Salud / ciencias de la vida:** presencia de convenios de confidencialidad de datos de salud, obligaciones de presentación regulatoria, correspondencia con COFEPRIS, obligaciones de ensayos clínicos
- **Contratistas del gobierno:** requisitos de consentimiento para novación, cláusulas de flujo descendente (_flow-down_), habilitaciones de seguridad, citas de la Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público
- **Bienes raíces:** opciones de renovación, escalamiento de renta, provisiones de mantenimiento de áreas comunes, subordinación, requisitos de certificación de estoppel
- **Financiero regulado:** condiciones de aprobación regulatoria, requisitos de capital, detonadores de presentación ante CNBV/BMV

## Recortes comunes para un primer pase rápido

Para una revisión inicial con presión de tiempo, estas 6 columnas responden el 80% de las preguntas tempranas de la operación: counterparty, effective_date, term, change_of_control, assignment, termination_for_convenience. Ejecuta esas primero, expande el esquema una vez que el equipo de la operación haya priorizado.
