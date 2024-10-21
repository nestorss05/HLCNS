from ejercicio1 import *

def test_cifradoCesar_a():
    assert cifradoCesar("a", 1) == "b"

def test_cifradoCesar_b():
    assert cifradoCesar("b", 3) == "e"

def test_cifradoCesar_z():
    assert cifradoCesar("z", 1) == "a"

def test_cifradoCesar_ab():
    assert cifradoCesar("ab", 1) == "bc"

def test_cifradoCesar_za():
    assert cifradoCesar("za", 2) == "bc"

def test_cifradoCesar_espacios():
    assert cifradoCesar("ab c", 2) == "cd e"

def test_cifradoCesar_comas():
    assert cifradoCesar("ab, c", 2) == "cd, e"