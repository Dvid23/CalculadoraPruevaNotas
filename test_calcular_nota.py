from calcular_nota import calcular_ep1, calcular_ep2, calcular_promo

def test_calcular_ep1():
    assert calcular_ep1(7, 8, 8) == 7.7

def test_calcular_ep2():
    assert calcular_ep2(10, 12, 15) == 12.6

def test_calcular_promo():
    resultado = calcular_promo(sub1=7, sub2=8, sub3=8, sub4=10, sub5=12, sub6=15, evp=7, evf=14)
    assert resultado == 10.99

def test_rechaza_negativos_en_ep1():
    try:
        calcular_ep1(-1, 8, 8)
        assert False, "Debio lanzar un error"
    except ValueError:
        assert True

def test_rechaza_negativos_en_promo():
    try:
        calcular_promo(sub1=7, sub2=8, sub3=8, sub4=10, sub5=12, sub6=15, evp=-5, evf=14)
        assert False, "Debio lanzar un error"
    except ValueError:
        assert True

def test_rechaza_nota_mayor_a_20():
    try:
        calcular_ep1(25, 8, 8)
        assert False, "Debio lanzar un error"
    except ValueError:
        assert True