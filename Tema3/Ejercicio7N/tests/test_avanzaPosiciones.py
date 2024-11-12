from parchis.Parchis import Parchis

def test_avanzaPosicionesJ1():
    objeto = Parchis( "Pepe", "Pepitto")
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    Parchis.avanzaPosiciones(objeto,1)
    assert objeto.fichaJ1 == 2

def test_avanzaPosicionesJ2():
    objeto = Parchis( "Pepe", "Pepitto")
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    Parchis.avanzaPosiciones(objeto,2)
    assert objeto.fichaJ2 == 2

def test_avanzaPosiciones3_2():
    objeto = Parchis( "Pepe", "Pepitto")
    objeto.fichaJ2 = 3
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    Parchis.avanzaPosiciones(objeto,2)
    assert objeto.fichaJ2 == 5

def test_avanzaPosicionesMas20():
    objeto = Parchis( "Pepe", "Pepitto")
    objeto.fichaJ1 = 19
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    Parchis.avanzaPosiciones(objeto, 1)
    assert objeto.fichaJ1 == 19