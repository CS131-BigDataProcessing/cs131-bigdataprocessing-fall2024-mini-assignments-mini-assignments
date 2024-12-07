# stats_function.py

import pandas as pd
import numpy as np

def calculate_mean_age(df):
    if 'Vict age' not in df.columns:
        raise ValueError("Column 'Vict age' is missing.")
    return np.mean(df['Vict age'])

def calculate_median_age(df):
    if 'Vict age' not in df.columns:
        raise ValueError("Column 'Vict age' is missing.")
    return np.median(df['Vict age'])


