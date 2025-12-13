import sys
from pathlib import Path
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (add, subtract, multiply, divide, min, logarithm, 
                 square, sine, cosine, square_root, percentage)

# Basic Operations Tests

def test_add_positive():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -3) == -8

def test_add_mixed():
    assert add(10, -5) == 5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_floats():
    assert abs(add(2.5, 3.7) - 6.2) < 0.0001


def test_subtract_positive():
    assert subtract(10, 3) == 7

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_result_negative():
    assert subtract(3, 10) == -7


def test_multiply_positive():
    assert multiply(4, 5) == 20

def test_multiply_negative():
    assert multiply(-3, 4) == -12

def test_multiply_by_zero():
    assert multiply(100, 0) == 0

def test_multiply_floats():
    assert abs(multiply(2.5, 4.0) - 10.0) < 0.0001


def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, 2) == -5

def test_divide_floats():
    assert abs(divide(7.5, 2.5) - 3.0) < 0.0001

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# Advanced Operations Tests

def test_logarithm_natural():
    assert abs(logarithm(math.e) - 1.0) < 0.0001

def test_logarithm_base_10():
    assert abs(logarithm(100, 10) - 2.0) < 0.0001

def test_logarithm_base_2():
    assert abs(logarithm(8, 2) - 3.0) < 0.0001

def test_logarithm_zero():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(0)

def test_logarithm_negative():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(-5)

def test_logarithm_invalid_base_zero():
    with pytest.raises(ValueError, match="Base must be positive and not equal to 1"):
        logarithm(10, 0)

def test_logarithm_invalid_base_one():
    with pytest.raises(ValueError, match="Base must be positive and not equal to 1"):
        logarithm(10, 1)

def test_logarithm_invalid_base_negative():
    with pytest.raises(ValueError, match="Base must be positive and not equal to 1"):
        logarithm(10, -2)


def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-4) == 16

def test_square_zero():
    assert square(0) == 0

def test_square_float():
    assert abs(square(2.5) - 6.25) < 0.0001


def test_sine_zero():
    assert abs(sine(0) - 0.0) < 0.0001

def test_sine_pi_over_2():
    assert abs(sine(math.pi / 2) - 1.0) < 0.0001

def test_sine_pi():
    assert abs(sine(math.pi)) < 0.0001

def test_sine_negative():
    assert abs(sine(-math.pi / 2) - (-1.0)) < 0.0001


def test_cosine_zero():
    assert abs(cosine(0) - 1.0) < 0.0001

def test_cosine_pi_over_2():
    assert abs(cosine(math.pi / 2)) < 0.0001

def test_cosine_pi():
    assert abs(cosine(math.pi) - (-1.0)) < 0.0001

def test_cosine_negative():
    assert abs(cosine(-math.pi) - (-1.0)) < 0.0001


def test_square_root_positive():
    assert abs(square_root(25) - 5.0) < 0.0001

def test_square_root_zero():
    assert square_root(0) == 0

def test_square_root_float():
    assert abs(square_root(6.25) - 2.5) < 0.0001

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-4)


def test_percentage_basic():
    assert abs(percentage(50, 200) - 25.0) < 0.0001

def test_percentage_100():
    assert abs(percentage(100, 100) - 100.0) < 0.0001

def test_percentage_over_100():
    assert abs(percentage(150, 100) - 150.0) < 0.0001

def test_percentage_zero_value():
    assert percentage(0, 100) == 0

def test_percentage_zero_total():
    with pytest.raises(ValueError, match="Total cannot be zero"):
        percentage(50, 0)

def test_percentage_negative():
    assert abs(percentage(-25, 100) - (-25.0)) < 0.0001


# Min Function Tests

def test_min_first_smaller():
    assert min(3, 6) == 3

def test_min_second_smaller():
    assert min(6, 3) == 3

def test_min_equal():
    assert min(5, 5) == 5

def test_min_negative():
    assert min(-5, -3) == -5

def test_min_mixed():
    assert min(-5, 3) == -5

def test_min_zero():
    assert min(0, 5) == 0
