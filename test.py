import pytest
from main import MathOperations


@pytest.mark.parametrize("a, b, expected", [(1,2,3),(-1,-2,-3),(10.5,10.5,21)])
def test_addition_with_parametrize(a,b, expected):
    x = MathOperations()
    assert x.addition(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [(2,1,1),(-1,-2,-3),(10.5,10.5, 0)])
def test_substraction_with_parametrize(a,b, expected):
    x = MathOperations()
    assert x.substraction(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [(2,2,4),(-6,-2,-12),(10.5,10.5,110.25)])
def test_multiplication_with_parametrize(a,b, expected):
    x = MathOperations()
    assert x.multiplication(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [(6,2,3),(-40,-2,-20),(10.5,3.4,2.333)])
def test_division_with_parametrize(a,b, expected):
    x = MathOperations()
    assert x.division(a,b) == expected

