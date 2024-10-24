from ejercicio3 import comprobarCodigo

def test_codigoLongitudMayorA13():
    assert comprobarCodigo(84145330438475) == False

def test_codigoCorrectoEAN13():
    assert comprobarCodigo(8414533043847) == True

def test_codigoIncorrectoEAN13():
    assert comprobarCodigo(5129365779425) == False

def test_codigoCorrrectoEAN13_10len():
    assert comprobarCodigo(8414533046) == True

def test_codigoCorrectoEAN8():
    assert comprobarCodigo(65839522) == True

def test_codigoIncorrectoEAN8():
    assert comprobarCodigo(65839521) == False

def test_codigoCorrrectoEAN8_5len():
    assert comprobarCodigo(65832) == True