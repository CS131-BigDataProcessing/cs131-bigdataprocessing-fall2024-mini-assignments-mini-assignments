# math_functions.py

def power(base, exp):
    """Raises a base to the power of exp."""
    if exp < 0:
        return 1 / power(base, -exp)  # Handle negative exponents
    return base ** exp

def divide(a, b):
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")  # Handle division by zero
    return a / b

