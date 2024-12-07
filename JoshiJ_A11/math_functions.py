# math_functions.py

def power(base, exponent):
    """
    Raises base to the power of exponent.
    """
    return base ** exponent

def divide(dividend, divisor):
    """
    Divides dividend by divisor. Raises ValueError if divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend / divisor

