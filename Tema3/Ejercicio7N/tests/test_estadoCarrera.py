from parchis.Parchis import Parchis

def test_estadoCarreraGanaJ1():
    objeto = Parchis( "Pepe", "Pepitto")
    objeto.fichaJ1 = 15
    objeto.fichaJ2 = 13
    ganando = Parchis.estadoCarrera(objeto)
    assert ganando == objeto.nomJ1

def test_estadoCarreraGanaJ2():
    objeto = Parchis( "Pepe", "Pepitto")
    objeto.fichaJ1 = 13
    objeto.fichaJ2 = 15
    ganando = Parchis.estadoCarrera(objeto)
    assert ganando == objeto.nomJ2