import pytest
from main import MathOperations


@pytest.mark.parametrize("a, b, expected", [(1,2,3),(-1,-2,-3),(10.5,10.5,21)])
def test_addition_with_parametrize(a,b, expected):
    assert MathOperations.addition(a,b) == expected