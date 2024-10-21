from ejercicio5 import *

def test_ejercicio5_003():
    assert ascensor("0 0 3") == 3

def test_ejercicio5_005():
    assert ascensor("0 0 5") == 5

def test_ejercicio5_015():
    assert ascensor("0 1 5") == 5

def test_ejercicio5_315():
    assert ascensor("3 1 5") == 6

def test_ejercicio5_31m5():
    assert ascensor("3 1 -5") == 8

def test_ejercicio5_3m35():
    assert ascensor("3 -3 5") == 14

def test_ejercicio5_m315():
    assert ascensor("-3 1 5") == 8

def test_ejercicio5_31582():
    assert ascensor("3 1 5 8 2") == 15

def test_ejercicio5_3158256():
    assert ascensor("3 1 5 8 2 5 6") == 19

def test_ejercicio5_3158m256():
    assert ascensor("3 1 5 8 -2 5 6") == 27