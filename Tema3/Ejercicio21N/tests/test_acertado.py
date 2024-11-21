from wordle.Wordle import Wordle

def test_AcertadoTrue():
    Wordle.palabraJuego = "ANGEL"
    acertado = Wordle.acertado("ANGEL")
    assert acertado == True

def test_AcertadoFalse():
    Wordle.palabraJuego = "ANGEL"
    acertado = Wordle.acertado("ENGOA")
    assert acertado == False