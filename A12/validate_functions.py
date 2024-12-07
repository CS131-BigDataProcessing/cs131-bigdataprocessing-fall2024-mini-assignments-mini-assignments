# validate_functions.py

import pandas as pd

def validate_sex(sex):
    """
    Validate the 'Vict sex' column to be 'M' or 'F'.
    """
    if pd.isnull(sex) or sex not in ['M', 'F']:
        return False
    return True

def validate_age(age):
    """
    Validate the 'Vict age' column to be between 1 and 100.
    """
    if pd.isnull(age) or not (1 <= age <= 100):
        return False
    return True

