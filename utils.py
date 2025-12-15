import re
from datetime import datetime, timedelta

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_password(password):
    # Alphanumeric and at least one special character
    if len(password) < 6: # Basic length check
        return False
    if not re.search("[a-zA-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def add_days(date_text, days):
    date_obj = datetime.strptime(date_text, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

def calculate_premium(vehicle_type, policy_type):
    # Basic logic for premium calculation
    base_premium = 1000
    if vehicle_type.lower() == "4-wheeler":
        base_premium *= 2
    
    if policy_type.lower() == "full insurance":
        base_premium *= 1.5
    
    return base_premium
