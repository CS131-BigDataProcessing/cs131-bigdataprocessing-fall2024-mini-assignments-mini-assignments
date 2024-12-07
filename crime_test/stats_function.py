# Calculate the mean age from the 'Vict age' column
def calculate_mean_age(data):
    if 'Vict Age' not in data.columns:
        raise ValueError("'Vict Age' column not found in data")
    if data['Vict Age'].isnull().all():
        raise ValueError("The 'Vict Age' column empty.")
    return data['Vict Age'].mean()



#Calculates the median age from the 'Vict age' column.
def calculate_median_age(data):
    if 'Vict Age' not in data.columns:
        raise ValueError("'Vict Age' column not found in data")
    if data['Vict Age'].isnull().all():
        raise ValueError("The 'Vict Age' column empty.")
    return data['Vict Age'].median()