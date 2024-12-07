# validate_functions.py

import pandas as pd

def validate_vict_sex(df):
    if 'Vict sex' not in df.columns:
        raise ValueError("Column 'Vict sex' is missing.")
    invalid_sex = df['Vict sex'].isnull() | ~df['Vict sex'].isin(['M', 'F'])
    return not invalid_sex.any()

def validate_vict_age(df):
    if 'Vict age' not in df.columns:
        raise ValueError("Column 'Vict age' is missing.")
    invalid_age = df['Vict age'].isnull() | (df['Vict age'] < 1) | (df['Vict age'] > 100)
    return not invalid_age.any()

