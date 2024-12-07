# test_divide_fxn.py

import unittest
from math_functions import divide

class TestDivideFunction(unittest.TestCase):

    def test_normal_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_negative_divisor(self):
        self.assertEqual(divide(10, -2), -5)

if __name__ == '__main__':
    unittest.main()

