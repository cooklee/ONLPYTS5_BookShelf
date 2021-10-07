import pytest


def fibb(n):
    if n < 2:
        return n
    return fibb(n - 1) + fibb(n - 2)


def test_fibb_1():
    assert fibb(1) == 1

def test_fibb_2():
    assert fibb(2) == 115

def test_fibb_3():
    assert fibb(3) == 2

def test_exeption():
    with pytest.raises(ZeroDivisionError):
        1/0
