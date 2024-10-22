from ejercicio4.ejercicio4 import ordenaAsc, ordenaDesc


def test_ordenar():
    assert ordenaAsc("6253") == 2356

def test_ordenar_desc():
    assert ordenaDesc("6253") == 6532