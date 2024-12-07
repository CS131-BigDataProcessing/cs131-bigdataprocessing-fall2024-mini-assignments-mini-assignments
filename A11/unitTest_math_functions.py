# unitTest_math_functions.py

import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):

    # Edge cases for power function
    def test_power_zero_exponent(self):
        self.assertEqual(power(5, 0), 1)  # Any number raised to power 0 is 1

    def test_power_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)  # 2^(-3) = 1 / (2^3) = 0.125

    def test_power_zero_base(self):
        self.assertEqual(power(0, 5), 0)  # 0 raised to any power is 0

    # Edge cases for divide function
    def test_divide_zero_dividend(self):
        self.assertEqual(divide(0, 5), 0)  # 0 divided by any number is 0

    def test_divide_zero_divisor(self):
        with self.assertRaises(ValueError):  # Division by zero should raise an error
            divide(5, 0)

    def test_divide_negative_divisor(self):
        self.assertEqual(divide(10, -2), -5)  # Division with negative divisor


