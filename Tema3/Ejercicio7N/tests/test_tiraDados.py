from parchis.Parchis import Parchis

def test_tiraDados():
    Parchis.tiraDados()
    assert 1 <= Parchis.dado1 <= 6
    assert 1 <= Parchis.dado2 <= 6