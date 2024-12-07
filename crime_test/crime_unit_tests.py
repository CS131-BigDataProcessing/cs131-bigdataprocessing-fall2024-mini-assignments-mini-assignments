import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age
from stats_function import calculate_mean_age, calculate_median_age

class Test_stats_function(unittest.TestCase):

    def setUp(self):
        try:
            self.dataset = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
        except FileNotFoundError:
            raise FileNotFoundError("Crime_Data_from_2020_to_Present.csv not found.")

    #Test calculate mean function
    def test_calculate_mean_age(self):
        calculate_mean = calculate_mean_age(self.dataset)
        self.assertIsInstance(calculate_mean, (float, int), "Mean should be an integer value")
        self.assertGreater(calculate_mean, 0, "Mean should be greater than 0")

    def test_calculate_median_age(self):
        calculate_median = calculate_median_age(self.dataset)
        self.assertIsInstance(calculate_median, (float, int), "Median should be an integer value")
        self.assertGreater(calculate_median, 0, "Median should be greater than 0")


class Test_validate_functions(unittest.TestCase):
    def setUp(self):
        try:
            self.dataset = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
        except FileNotFoundError:
            raise FileNotFoundError("Crime_Data_from_2020_to_Present.csv not found.")

    def test_validate_vict_sex(self):
        # Test validate_vict_sex with the real dataset.
        test_vict_sex = validate_vict_sex(self.dataset)
        self.assertIsInstance(test_vict_sex, bool, "Result should be a boolean.")
        self.assertFalse(test_vict_sex)  # 'Vict Sex' column validation must fail as expected

    def test_validate_vict_age(self):
        #Test validate_vict_age with the dataset
        test_vict_age = validate_vict_age(self.dataset)
        self.assertIsInstance(test_vict_age, bool, "Result should be a boolean.")
        self.assertFalse(test_vict_age)  # 'Vict Age' column validation must fail as expected


if __name__ == "__main__":
    unittest.main()