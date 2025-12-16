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

def validate_vehicle_no(vehicle_no):
    # String with a space and Alphanumeric value
    # Example: "KA01 AB1234" or "KA 01" - Requirement says "String with a space and Alphanumeric value"
    # Let's assume it must contain at least one space and be alphanumeric (ignoring the space for alphanumeric check)
    if " " not in vehicle_no:
        return False
    parts = vehicle_no.split()
    for part in parts:
        if not part.isalnum():
            return False
    return True

def validate_phone_no(phone_no):
    # Integer consisting of 10 digits
    s_phone = str(phone_no)
    if len(s_phone) == 10 and s_phone.isdigit():
        return True
    return False

def validate_vehicle_type(vehicle_type):
    return vehicle_type.lower() in ["2-wheeler", "4-wheeler"]

def validate_policy_type(policy_type):
    return policy_type.lower() in ["full insurance", "thirdparty"]

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
