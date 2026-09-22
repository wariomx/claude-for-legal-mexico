---
type: llm
weight: 2
---

Evalúa la higiene de citas legales. Marca PASS si se cumplen las tres condiciones siguientes; marca FAIL solo si alguna se incumple de forma clara.

1. **Cita Jalisco.** La respuesta fundamenta al menos tres hallazgos distintos con artículos del Código Civil del Estado de Jalisco. Son ejemplos válidos, entre otros: 1983-1986 (legitimación), 2023 (contenido mínimo), 2025-2028 (preferencia), 2026 (derecho del tanto), 2035 o 2143 (avisos de terminación), 2045 (plazo máximo e inscripción en comercio), 2051 (prórroga), 2003-2004 (mejoras), 1313 (pena convencional), 1976-1979 o 1981 Bis (intereses), 1743 (prescripción de rentas), 2146 (venta judicial).
2. **No disfraza otro código.** La respuesta NO presenta como artículos de Jalisco los números del Código Civil Federal o del Código Civil de la Ciudad de México sobre arrendamiento (por ejemplo 2398, 2406, 2448, 2448-A a 2448-L, 2478 a 2489). Si los menciona, dice expresamente que son de otro ordenamiento. Si no aparece ninguno de esos números, esta condición se cumple.
3. **Declara la procedencia.** La respuesta indica de dónde provienen las citas, de cualquiera de estas formas: etiquetas en línea como `[settled — last confirmed ...]`, `[VERIFICAR ...]` o `[model knowledge — verify]`; una nota del revisor o sección de fuentes que explique qué citas vienen de una referencia verificada y cuáles deben verificarse; o una advertencia expresa de que los artículos deben confirmarse contra el texto vigente. Basta con UNA de estas formas presente de manera visible; no es necesario que cada cita individual lleve etiqueta.

No penalices la extensión, el formato ni el estilo. No exijas que la respuesta cite un artículo concreto de la lista de ejemplos.
