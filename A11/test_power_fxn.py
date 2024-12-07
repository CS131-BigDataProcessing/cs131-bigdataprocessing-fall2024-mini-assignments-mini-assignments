# test_power_fxn.py

import unittest
from math_functions import power

class TestPowerFunction(unittest.TestCase):

    def test_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_negative_exponent(self):
        self.assertEqual(power(2, -3), 0.125)

if __name__ == '__main__':
    unittest.main()

