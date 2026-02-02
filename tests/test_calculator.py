"""Tests for calculator module - some will fail due to bugs."""

import pytest

from src.calculator import (
    add,
    average,
    divide,
    factorial,
    multiply,
    percentage,
    power,
    subtract,
)


class TestBasicOperations:
    """Tests for basic arithmetic operations."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        assert add(-2, 5) == 3

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        assert subtract(3, 5) == -2

    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12


class TestDivide:
    """Tests for divide function - will expose the division by zero bug."""

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_with_remainder(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        """Test that divide raises ValueError when divisor is zero."""
        with pytest.raises(ValueError) as excinfo:
            divide(10, 0)
        assert "Cannot divide by zero" in str(excinfo.value)

    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0.0


class TestPower:
    """Tests for power function - will expose negative exponent bug."""

    def test_power_positive_exponent(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_one_exponent(self):
        assert power(7, 1) == 7

    def test_power_negative_exponent(self):
        """BUG: This test will FAIL - power doesn't handle negative exponents."""
        result = power(2, -2)
        assert result == 0.25  # 2^-2 = 1/4 = 0.25


class TestFactorial:
    """Tests for factorial function - will expose negative input bug."""

    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_negative_raises_error(self):
        """BUG: This test will FAIL - factorial doesn't validate negative input."""
        with pytest.raises(ValueError) as excinfo:
            factorial(-5)
        assert "must be non-negative" in str(excinfo.value).lower()


class TestAverage:
    """Tests for average function - will expose empty list bug."""

    def test_average_positive_numbers(self):
        assert average([1, 2, 3, 4, 5]) == 3.0

    def test_average_single_number(self):
        assert average([42]) == 42.0

    def test_average_with_floats(self):
        assert average([1.5, 2.5, 3.0]) == pytest.approx(2.333, rel=0.01)

    def test_average_empty_list_raises_error(self):
        """BUG: This test will FAIL - average doesn't handle empty list."""
        with pytest.raises(ValueError) as excinfo:
            average([])
        assert "empty" in str(excinfo.value).lower()


class TestPercentage:
    """Tests for percentage function - will expose zero total bug."""

    def test_percentage_normal(self):
        assert percentage(25, 100) == 25.0

    def test_percentage_half(self):
        assert percentage(50, 200) == 25.0

    def test_percentage_zero_value(self):
        assert percentage(0, 100) == 0.0

    def test_percentage_zero_total_raises_error(self):
        """BUG: This test will FAIL - percentage doesn't handle zero total."""
        with pytest.raises(ValueError) as excinfo:
            percentage(50, 0)
        assert "total cannot be zero" in str(excinfo.value).lower()
