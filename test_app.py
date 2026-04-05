import pytest
from app import add, subtract, multiply, divide, calculate


class TestAdd:
    def test_positive_numbers(self):
        assert add(10, 5) == 15

    def test_negative_numbers(self):
        assert add(-3, -7) == -10

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 5) == 5

    def test_negative_result(self):
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_basic(self):
        assert multiply(4, 3) == 12

    def test_by_zero(self):
        assert multiply(99, 0) == 0


class TestDivide:
    def test_basic(self):
        assert divide(10, 5) == 2.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


class TestCalculate:
    def test_valid_operations(self):
        assert calculate("add", 1, 2) == 3
        assert calculate("subtract", 5, 3) == 2
        assert calculate("multiply", 3, 4) == 12
        assert calculate("divide", 8, 4) == 2.0

    def test_unknown_operation(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            calculate("power", 2, 3)
