import unittest
from math_functions import power, divide


class TestMathFunctions(unittest.TestCase):
    #Unit testing for math functions
    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -4), 0.0625)

    def test_zero_exponent(self):
        self.assertEqual(power(3, 0), 1)

    #Unit testing for divide functions
    def test_divide_positive(self):
        self.assertEqual(power(10, 2), 100)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_zero_divisor(self):
        with self.assertRaises(ValueError):
            divide(10, 0)