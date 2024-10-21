from ejercicio2 import *

def test_velocidad_d32t4():
    assert velocidad("D=32 T=4") == "V=8"

## Test que actualmente no funciona
def test_velocidad_t4v8():
    assert velocidad("T=4 V=8") == "D=32"