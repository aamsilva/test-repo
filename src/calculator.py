"""Simple calculator module with intentional bugs for testing."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Divide a by b.

    BUG: No check for division by zero!
    """
    # BUG: Should check if b == 0 and raise ZeroDivisionError with clear message
    return a / b


def power(base: Number, exponent: int) -> Number:
    """Calculate base raised to exponent.

    BUG: Doesn't handle negative exponents correctly.
    """
    result = 1
    # BUG: This only works for positive exponents
    for _ in range(exponent):
        result *= base
    return result


def factorial(n: int) -> int:
    """Calculate factorial of n.

    BUG: No validation for negative numbers!
    """
    # BUG: Should validate n >= 0
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def average(numbers: list[Number]) -> float:
    """Calculate average of a list of numbers.

    BUG: No check for empty list!
    """
    # BUG: Should check if list is empty
    return sum(numbers) / len(numbers)


def percentage(value: Number, total: Number) -> float:
    """Calculate what percentage value is of total.

    BUG: No validation for total being zero!
    """
    # BUG: Should check if total == 0
    return (value / total) * 100
