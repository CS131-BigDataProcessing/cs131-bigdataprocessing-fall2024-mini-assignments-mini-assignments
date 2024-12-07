# test_stats_functions.py

import unittest
from stats_functions import mean_age, median_age

class TestStatsFunctions(unittest.TestCase):

    def test_mean_age(self):
        self.assertEqual(mean_age(pd.Series([20, 30, 40, 50])), 35)
        self.assertEqual(mean_age(pd.Series([1, 2, 3, 4, 5])), 3)

    def test_median_age(self):
        self.assertEqual(median_age(pd.Series([20, 30, 40, 50])), 35)
        self.assertEqual(median_age(pd.Series([1, 2, 3, 4, 5])), 3)

    def test_mean_age_empty(self):
        self.assertEqual(mean_age(pd.Series([])), pd.NA)

    def test_median_age_empty(self):
        self.assertEqual(median_age(pd.Series([])), pd.NA)

    def test_mean_age_single_value(self):
        self.assertEqual(mean_age(pd.Series([30])), 30)

    def test_median_age_single_value(self):
        self.assertEqual(median_age(pd.Series([30])), 30)


