"""
Cálculo de notas (Proceso 1, Proceso 2 y promedio final).

Se elimina la redundancia que había entre calcular_ep1 / calcular_ep2
(ambas hacían exactamente lo mismo) y entre validar el "tipo" y el
"rango" de la nota por separado. Ahora una sola función,
validar_nota(), se encarga de:
  1. Verificar que sea un número (int o float, no bool).
  2. Verificar que sea positivo y esté en el rango 0-20.
"""


def validar_nota(nota, nombre="nota"):
    """Valida que 'nota' sea un número real entre 0 y 20 (inclusive)."""
    if isinstance(nota, bool) or not isinstance(nota, (int, float)):
        raise TypeError(f"{nombre} debe ser un número")
    if nota < 0 or nota > 20:
        raise ValueError(f"{nombre} debe estar entre 0 y 20")
    return nota


def _promedio_ponderado(a, b, c, nombres):
    """Núcleo común para calcular un EP: 30% + 30% + 40%."""
    for nombre, valor in zip(nombres, (a, b, c)):
        validar_nota(valor, nombre)
    return (a * 0.30) + (b * 0.30) + (c * 0.40)


def calcular_ep1(sub1, sub2, sub3):
    return _promedio_ponderado(sub1, sub2, sub3, ("sub1", "sub2", "sub3"))


def calcular_ep2(sub4, sub5, sub6):
    return _promedio_ponderado(sub4, sub5, sub6, ("sub4", "sub5", "sub6"))


def calcular_promo(sub1, sub2, sub3, sub4, sub5, sub6, evp, evf):
    validar_nota(evp, "evp")
    validar_nota(evf, "evf")
    ep1 = calcular_ep1(sub1, sub2, sub3)
    ep2 = calcular_ep2(sub4, sub5, sub6)
    final = (0.20 * ep1) + (0.30 * evp) + (0.20 * ep2) + (0.30 * evf)
    return round(final, 2)