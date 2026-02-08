import pytest
from typing import Union
from app.operations import addition, subtraction, multiplication, division

Number = Union[int, float]


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ],
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    assert addition(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
    ],
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    assert subtraction(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 10, 0),
        (-2, -3, 6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
    ],
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    assert multiplication(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ],
)
def test_division(a: Number, b: Number, expected: float) -> None:
    assert division(a, b) == expected


@pytest.mark.parametrize("a", [1, -1, 0])
def test_division_by_zero(a: Number) -> None:
    with pytest.raises(ValueError, match=r"Division by zero is not allowed\."):
        division(a, 0)
