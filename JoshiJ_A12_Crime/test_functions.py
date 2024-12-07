# test_functions.py

import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean_age, calculate_median_age

class TestValidateFunctions(unittest.TestCase):

    def test_validate_vict_sex(self):
        df = pd.DataFrame({'Vict sex': ['M', 'F', 'M', None]})
        self.assertFalse(validate_vict_sex(df))

    def test_validate_vict_age(self):
        df = pd.DataFrame({'Vict age': [25, 35, 200, 0]})
        self.assertFalse(validate_vict_age(df))

class TestStatsFunctions(unittest.TestCase):

    def test_calculate_mean_age(self):
        df = pd.DataFrame({'Vict age': [20, 30, 40]})
        self.assertEqual(calculate_mean_age(df), 30)

    def test_calculate_median_age(self):
        df = pd.DataFrame({'Vict age': [20, 30, 40]})
        self.assertEqual(calculate_median_age(df), 30)

