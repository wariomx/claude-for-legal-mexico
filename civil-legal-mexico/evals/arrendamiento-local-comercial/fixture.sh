#!/usr/bin/env bash
# Siembra un perfil de práctica LOCAL (resolución .claude-legal/ del CWD) para que la
# compuerta del Paso 0 de revision-arrendamiento encuentre configuración sin tocar
# ~/.claude/plugins/config del usuario real.
set -euo pipefail
# 1. Copiar el contrato sintético al CWD del agente (add_dirs no lo expone como archivo).
CASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$CASE_DIR/resources/contrato.md" ]; then
  cp "$CASE_DIR/resources/contrato.md" ./contrato.md
else
  echo "fixture: no encuentro $CASE_DIR/resources/contrato.md" >&2
  exit 1
fi
# 2. Perfil de práctica local.
mkdir -p .claude-legal/civil-legal-mexico
cat > .claude-legal/company-profile.md <<'PROFILE'
# Perfil de empresa (fixture de eval)

**Nombre de la entidad:** Despacho de prueba civil-legal-mexico
**Industria / sector:** servicios jurídicos
**Jurisdicción principal:** Guadalajara, Jalisco
**Tamaño del equipo legal:** 2
**Tipo de práctica:** Despacho solo/pequeño
PROFILE
cat > .claude-legal/civil-legal-mexico/CLAUDE.md <<'PROFILE'
# Perfil de Práctica Civil
*Generado por cold-start el 2026-09-22 (fixture de eval). Módulos activos: [Arrendamiento]*

## Perfil de la empresa

**Nombre de la entidad:** Despacho de prueba civil-legal-mexico
**Perfil civil:** despacho civilista
**Jurisdicción principal:** Guadalajara, Jalisco
**Escalamiento:** socio responsable
**Tipo de práctica:** Despacho solo/pequeño

## Quién usa este plugin

**Rol:** Abogado titulado / profesional jurídico
**Contacto de abogado:** N/A

## Entidades federativas

**Entidad principal:** Jalisco
**Entidades adicionales:** ninguna
**Regla cuando el asunto no indica entidad:** preguntar siempre; nunca asumir la principal.

| Entidad | Código civil aplicable | Referencia verificada en el plugin | Código procesal vigente / estatus CNPCF | RPP |
|---|---|---|---|---|
| Jalisco | Código Civil del Estado de Jalisco | ✓ `skills/revision-arrendamiento/references/ccj-jalisco-arrendamiento.md` (arrendamiento) | `[VERIFICAR]` | Registro Público de la Propiedad y de Comercio de Jalisco |

## Integraciones disponibles

| Integración | Estado | Alternativa si no está disponible |
|---|---|---|
| LegalDataHunter | ✗ | citas con etiqueta de fuente local o `[VERIFICAR]` |

## Resultados

Encabezado: `CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO — PREPARADO BAJO LA DIRECCIÓN DE ASESOR JURÍDICO — PROTEGIDO POR SECRETO PROFESIONAL`. Nota del revisor en un bloque arriba del entregable. Escala 🔴 Bloqueante / 🟠 Alto / 🟡 Medio / 🟢 Bajo. Leyenda obligatoria al pie.

## Espacios de trabajo por asunto

**Habilitado:** ✗
**Asunto activo:** ninguno
**Contexto cruzado entre asuntos:** desactivado

## Arrendamiento

**Lado habitual:** ambos según el asunto
**Destinos frecuentes:** comercio / habitación
**Volumen:** ocasional
**Machote de casa:** ninguno
**Posiciones de playbook:**
- Depósito: un mes, devolución en 30 días contra acta de entrega
- Incremento anual: INPC
- Fiador u obligado solidario: solo comercial; exigir extensión expresa a prórrogas
- Pena por terminación anticipada: tres meses de renta
- Inscripción en RPP: siempre arriba del umbral legal
**Umbral de escalamiento:** renta mensual mayor a MXN 100,000
PROFILE
echo "fixture: contrato.md y perfil local sembrados en $(pwd)"
