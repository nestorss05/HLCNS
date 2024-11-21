from wordle.Wordle import Wordle

## Debido a que seleccionaJuego() elige uno aleatorio, este test requiere varios intentos para funcionar
def test_seleccionaJuegoAngel():
    Wordle.seleccionaJuego()
    assert Wordle.palabraJuego == "ANGEL"

## Debido a que seleccionaJuego() elige uno aleatorio, este test requiere varios intentos para funcionar
def test_seleccionaJuegoJamon():
    Wordle.seleccionaJuego()
    assert Wordle.palabraJuego == "JAMON"

def test_seleccionaJuegoInvalido():
    Wordle.seleccionaJuego()
    assert Wordle.palabraJuego != "MONJA"