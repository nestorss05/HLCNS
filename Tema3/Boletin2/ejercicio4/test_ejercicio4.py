import pytest

from ejercicio4 import *

def test_kaprekar_6174():
    assert kaprekar(6174) == 0

def test_kaprekar_1111():
    assert kaprekar(1111) == 8

def test_kaprekar_11111():
    with pytest.raises(Exception) as r:
        kaprekar(11111)
    assert str(r.value) == "No puede tener mas de cinco caracteres"

def test_kaprekar_3524():
    assert kaprekar(3524) == 3

def test_kaprekar_9():
    assert kaprekar(9) == 4

def test_kaprekar_1121():
    assert kaprekar(1121) == 5