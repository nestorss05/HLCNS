from parchis.Parchis import Parchis

def test_esGanadorJ1():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 20
    objeto.fichaJ2 = 15
    ganador = Parchis.esGanador(objeto)
    assert ganador == objeto.nomJ1

def test_esGanadorJ2():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 15
    objeto.fichaJ2 = 20
    ganador = Parchis.esGanador(objeto)
    assert ganador == objeto.nomJ2

def test_esGanadorNadie():
    objeto = Parchis("Pepe", "Pepitto")
    objeto.fichaJ1 = 15
    objeto.fichaJ2 = 19
    ganador = Parchis.esGanador(objeto)
    assert ganador == ""