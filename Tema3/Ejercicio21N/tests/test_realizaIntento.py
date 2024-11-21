from wordle.Wordle import Wordle

def test_realizarIntentoAngelInvalido():
    objeto = Wordle()
    Wordle.palabraJuego = "ANGEL"
    Wordle.realizaIntento(objeto, "ENGOA")
    assert Wordle.pistas[0] == ["ANGEL", "*NG-*"]

## Tests a hacer: IntentoAngelValido, Intento4Letras, Intento6Letras