def validate_vict_sex(data):
    """
    Validates that 'Vict sex' column contains only 'M', 'F', and no NULL values.
    """
    if 'Vict Sex' not in data.columns:
        raise ValueError("'Vict Sex' column not found in data")
    if data['Vict Sex'].isnull().any():
        return False
    if not data['Vict Sex'].isin(['M', 'F']).all():
        return False
    return True

def validate_vict_age(data):
    """
    Validates that 'Vict age' column contains values between 1 and 100 and no NULL values.
    """
    if 'Vict Age' not in data.columns:
        raise ValueError("'Vict Age' column not found in data")
    if data['Vict Age'].isnull().any():
        return False
    if not data['Vict Age'].between(1, 100).all():
        return False
    return True