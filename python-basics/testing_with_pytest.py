"""
testing_with_pytest.py

This file introduces unit testing in Python using pytest.
Run tests using:
    pytest testing_with_pytest.py
"""

# Example function to test
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ------------------------
# Tests start here
# ------------------------

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False  # should not reach here
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
