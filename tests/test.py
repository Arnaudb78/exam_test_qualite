import pytest
from main import MathOperations


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (10.5, 10.5, 21),
    ('chat', 'chien', None)
])
def test_addition_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (-1, -2, 1),
    (10.5, 10.5, 0)
])
def test_subtraction_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (-6, -2, 12),
    (10.5, 10.5, 110.25)
    ])
def test_multiplication_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (-40, -2, 20),
    (10.5, 2.5, 4.2)])
def test_division_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.division(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 2),
    (-5, 3, -125),
    (2, 0, 1),
    (9, 0.5, 3)])
def test_power_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.power(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 2),
    (-10, -4, -2),
    (2, 1, 0)])
def test_modulo_with_parametrize(a, b, expected):
    x = MathOperations()
    assert x.modulo(a, b) == expected
