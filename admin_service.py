from database import load_data, save_data, get_next_id, UNDERWRITERS_FILE, POLICIES_FILE
from models import UnderWriter
from utils import validate_date, validate_password

def admin_login():
    print("\n--- Admin Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username == "admin" and password == "admin123":
        return True
    else:
        print("Invalid Credentials!")
        return False

def register_underwriter():
    print("\n--- Register UnderWriter ---")
    name = input("Enter Name: ")
    
    while True:
        dob = input("Enter DOB (YYYY-MM-DD): ")
        if validate_date(dob):
            break
        print("Invalid Date Format!")

    while True:
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        if validate_date(joining_date):
            break
        print("Invalid Date Format!")

    while True:
        password = input("Enter Default Password (Alphanumeric + Special Char): ")
        if validate_password(password):
            break
        print("Password must be alphanumeric and contain at least one special character!")

    uid = get_next_id(UNDERWRITERS_FILE, "uid")
    new_uw = UnderWriter(uid, name, dob, joining_date, password)
    
    underwriters = load_data(UNDERWRITERS_FILE)
    underwriters.append(new_uw.to_dict())
    save_data(UNDERWRITERS_FILE, underwriters)
    
    print(f"UnderWriter Registered Successfully! ID: {uid}")

def search_underwriter():
    print("\n--- Search UnderWriter ---")
    print("1. View All UnderWriters")
    print("2. View UnderWriter by ID")
    choice = input("Enter Choice: ")

    underwriters = load_data(UNDERWRITERS_FILE)

    if choice == '1':
        if not underwriters:
            print("No UnderWriters found.")
        for uw in underwriters:
            print(uw)
    elif choice == '2':
        while True:
            uid_input = input("Enter UnderWriter ID: ")
            if not uid_input.isdigit():
                 print("Invalid ID format.")
                 continue
            
            uid = int(uid_input)
            found = False
            for uw in underwriters:
                if uw['uid'] == uid:
                    print(uw)
                    found = True
                    break
            
            if found:
                break
            else:
                print("Invalid UnderWriter Id")
                print("1. Re-Enter UnderWriter Id")
                print("2. Go Back")
                sub_choice = input("Enter Choice: ")
                if sub_choice == '2':
                    break
    else:
        print("Invalid Choice")

def update_underwriter_password():
    print("\n--- Update UnderWriter Password ---")
    while True:
        uid_input = input("Enter UnderWriter ID: ")
        if not uid_input.isdigit():
             print("Invalid ID format.")
             continue
        
        uid = int(uid_input)
        underwriters = load_data(UNDERWRITERS_FILE)
        found_idx = -1
        
        for i, uw in enumerate(underwriters):
            if uw['uid'] == uid:
                found_idx = i
                break
        
        if found_idx != -1:
            while True:
                new_password = input("Enter New Password (Alphanumeric + Special Char): ")
                if validate_password(new_password):
                    break
                print("Password must be alphanumeric and contain at least one special character!")
            
            underwriters[found_idx]['password'] = new_password
            save_data(UNDERWRITERS_FILE, underwriters)
            print("Password Updated Successfully!")
            break
        else:
            print("Invalid UnderWriter Id")
            print("1. Re-Enter UnderWriter Id")
            print("2. Go Back")
            sub_choice = input("Enter Choice: ")
            if sub_choice == '2':
                break

def delete_underwriter():
    print("\n--- Delete UnderWriter ---")
    while True:
        uid_input = input("Enter UnderWriter ID: ")
        if not uid_input.isdigit():
             print("Invalid ID format.")
             continue
        
        uid = int(uid_input)
        underwriters = load_data(UNDERWRITERS_FILE)
        found_idx = -1
        
        for i, uw in enumerate(underwriters):
            if uw['uid'] == uid:
                found_idx = i
                break
        
        if found_idx != -1:
            print("Are you sure you want to delete?")
            print("1. Yes")
            print("2. No")
            confirm = input("Enter Choice: ")
            if confirm == '1':
                del underwriters[found_idx]
                save_data(UNDERWRITERS_FILE, underwriters)
                print("UnderWriter Deleted Successfully!")
                break
            else:
                break
        else:
            print("Invalid UnderWriter Id")
            print("1. Re-Enter UnderWriter Id")
            print("2. Go Back")
            sub_choice = input("Enter Choice: ")
            if sub_choice == '2':
                break

def view_vehicles_by_underwriter():
    print("\n--- View Vehicles by UnderWriter ---")
    uid_input = input("Enter UnderWriter ID: ")
    if not uid_input.isdigit():
            print("Invalid ID format.")
            return

    uid = int(uid_input)
    
    # Verify UnderWriter exists first (optional but good practice)
    underwriters = load_data(UNDERWRITERS_FILE)
    uw_exists = any(uw['uid'] == uid for uw in underwriters)
    
    if not uw_exists:
        print("UnderWriter ID not found.")
        return

    policies = load_data(POLICIES_FILE)
    found_policies = [p for p in policies if p['underwriter_id'] == uid]
    
    if not found_policies:
        print("No vehicles registered by this UnderWriter.")
    else:
        for p in found_policies:
            print(f"PolicyNo: {p['policy_no']}, VehicleNo: {p['vehicle_no']}, Type: {p['vehicle_type']}, Customer: {p['customer_name']}, Premium: {p['premium_amt']}")

def admin_menu():
    if not admin_login():
        return

    while True:
        print("\n--- Admin Menu ---")
        print("1. UnderWriter Registration")
        print("2. Search UnderWriter by Id")
        print("3. Update UnderWriter password")
        print("4. Delete UnderWriter by Id")
        print("5. View All UnderWriter") # Mapped to Search Underwriter -> View All
        print("6. View All Vehicle specific to underWriter Id")
        print("7. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            register_underwriter()
        elif choice == '2':
            search_underwriter() # Handles both view all and by ID, but we can direct to specific flow if needed.
        elif choice == '3':
            update_underwriter_password()
        elif choice == '4':
            delete_underwriter()
        elif choice == '5':
             # Reusing search_underwriter logic but forcing view all could be cleaner, 
             # but for now let's just call search_underwriter and user picks 1
             search_underwriter()
        elif choice == '6':
            view_vehicles_by_underwriter()
        elif choice == '7':
            break
        else:
            print("Invalid Choice!")
