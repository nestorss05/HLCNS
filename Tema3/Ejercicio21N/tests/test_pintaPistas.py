from wordle.Wordle import Wordle

def test_pintaPistasVacio():
    tabla = Wordle.pintaPistas()
    filas = "----- | -----\n"
    filas += "----- | -----\n"
    filas += "----- | -----\n"
    filas += "----- | -----\n"
    filas += "----- | -----\n"
    filas += "----- | -----"
    assert tabla == filas

def test_pintaPistasLlenoValido():
    ## Este test depende de realizaIntento, por lo que por ahora este test no funciona
    tabla = Wordle.pintaPistas()
    filas = "ANGEL | -NG--\n"
    filas += "ANGEL | *NG*L\n"
    filas += "ANGEL | ANGEL\n"
    filas += "----- | -----\n"
    filas += "----- | -----\n"
    filas += "----- | -----"
    assert tabla == filas