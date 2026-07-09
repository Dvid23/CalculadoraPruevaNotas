def validar_nota(nota):
    if nota < 0 or nota > 20:
        raise ValueError("La nota debe estar entre 0 y 20")

def calcular_ep1(sub1, sub2, sub3):
    validar_nota(sub1)
    validar_nota(sub2)
    validar_nota(sub3)
    return (sub1 * 0.30) + (sub2 * 0.30) + (sub3 * 0.40)


def calcular_ep2(sub4, sub5, sub6):
    validar_nota(sub4)
    validar_nota(sub5)
    validar_nota(sub6)
    return (sub4 * 0.30) + (sub5 * 0.30) + (sub6 * 0.40)


def calcular_promo(sub1, sub2, sub3, sub4, sub5, sub6, evp, evf):
    validar_nota(evp)
    validar_nota(evf)
    ep1 = calcular_ep1(sub1, sub2, sub3)
    ep2 = calcular_ep2(sub4, sub5, sub6)
    final = (0.20 * ep1) + (0.30 * evp) + (0.20 * ep2) + (0.30 * evf)
    return round(final, 2)