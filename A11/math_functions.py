#Creating power and divide functions

def power(base, exponent):
    """
        Raises a number to a power.
    """
    return base ** exponent


def divide(numerator, denominator):
    """
        Divides a number by another number.
    """
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator

