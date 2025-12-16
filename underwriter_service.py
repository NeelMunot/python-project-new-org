from database import load_data, save_data, get_next_id, UNDERWRITERS_FILE, POLICIES_FILE
from models import VehiclePolicy
from utils import validate_date, add_days, get_current_date, calculate_premium, validate_vehicle_no, validate_phone_no, validate_vehicle_type, validate_policy_type

def underwriter_login():
    print("\n--- UnderWriter Login ---")
    try:
        uid = int(input("Enter User ID: "))
    except ValueError:
        print("Invalid User ID format")
        return None

    password = input("Enter Password: ")
    
    underwriters = load_data(UNDERWRITERS_FILE)
    for uw in underwriters:
        if uw['uid'] == uid and uw['password'] == password:
            return uid
    
    print("Invalid Credentials!")
    return None

def create_vehicle_insurance(underwriter_id):
    print("\n--- Create New Vehicle Insurance ---")
    
    while True:
        vehicle_no = input("Enter Vehicle No (e.g., KA01 AB1234): ")
        if validate_vehicle_no(vehicle_no):
            break
        print("Invalid Vehicle No! Must contain a space and be alphanumeric.")

    while True:
        vehicle_type = input("Enter Vehicle Type (2-wheeler/4-wheeler): ")
        if validate_vehicle_type(vehicle_type):
            break
        print("Invalid Vehicle Type! Must be '2-wheeler' or '4-wheeler'.")

    customer_name = input("Enter Customer Name: ")
    
    try:
        engine_no = int(input("Enter Engine No: "))
        chasis_no = int(input("Enter Chasis No: "))
        
        while True:
            phone_no = int(input("Enter Phone No (10 digits): "))
            if validate_phone_no(phone_no):
                break
            print("Invalid Phone No! Must be 10 digits.")
            
    except ValueError:
        print("Invalid numeric input!")
        return

    while True:
        policy_type = input("Enter Policy Type (Full Insurance/ThirdParty): ")
        if validate_policy_type(policy_type):
            break
        print("Invalid Policy Type! Must be 'Full Insurance' or 'ThirdParty'.")
    
    while True:
        from_date = input("Enter From Date (YYYY-MM-DD): ")
        if validate_date(from_date):
            break
        print("Invalid Date Format!")

    to_date = add_days(from_date, 365)
    premium_amt = calculate_premium(vehicle_type, policy_type)
    policy_no = get_next_id(POLICIES_FILE, "policy_no")
    
    new_policy = VehiclePolicy(policy_no, vehicle_no, vehicle_type, customer_name, engine_no, chasis_no, phone_no, policy_type, premium_amt, from_date, to_date, underwriter_id)
    
    policies = load_data(POLICIES_FILE)
    policies.append(new_policy.to_dict())
    save_data(POLICIES_FILE, policies)
    
    print(f"Policy Created Successfully! Policy No: {policy_no}, Premium: {premium_amt}")

def renew_policy(underwriter_id):
    print("\n--- Renew Policy ---")
    try:
        policy_id = int(input("Enter Policy ID: "))
    except ValueError:
        print("Invalid Policy ID format")
        return

    policies = load_data(POLICIES_FILE)
    found_policy = None
    
    for p in policies:
        if p['policy_no'] == policy_id:
            found_policy = p
            break
    
    if found_policy:
        print(f"Policy Details: {found_policy}")
        confirm = input("Enter 'R' to confirm renewal: ")
        if confirm.upper() == 'R':
            try:
                new_premium = float(input("Enter Updated Premium Amount: "))
                if new_premium <= 0:
                    print("Premium amount must be positive.")
                    return
            except ValueError:
                print("Invalid Amount")
                return

            current_date = get_current_date()
            old_to_date = found_policy['to_date']
            
            if current_date > old_to_date:
                new_from_date = current_date
            else:
                new_from_date = add_days(old_to_date, 1)
            
            new_to_date = add_days(new_from_date, 365)
            
            # Create new policy record
            new_policy_no = get_next_id(POLICIES_FILE, "policy_no")
            new_policy = VehiclePolicy(
                new_policy_no,
                found_policy['vehicle_no'],
                found_policy['vehicle_type'],
                found_policy['customer_name'],
                found_policy['engine_no'],
                found_policy['chasis_no'],
                found_policy['phone_no'],
                found_policy['policy_type'],
                new_premium,
                new_from_date,
                new_to_date,
                underwriter_id # Logged in user gets credit
            )
            
            policies.append(new_policy.to_dict())
            save_data(POLICIES_FILE, policies)
            print(f"Policy Renewed Successfully! New Policy No: {new_policy_no}")
    else:
        print("Policy ID not found.")

def change_policy_type():
    print("\n--- Change Policy Type ---")
    try:
        policy_id = int(input("Enter Policy ID: "))
    except ValueError:
        print("Invalid Policy ID format")
        return

    policies = load_data(POLICIES_FILE)
    found_idx = -1
    
    for i, p in enumerate(policies):
        if p['policy_no'] == policy_id:
            found_idx = i
            break
    
    if found_idx != -1:
        policy = policies[found_idx]
        if policy['policy_type'].lower() == "thirdparty":
            print("There's no provision to update the policy type from Third party to full Insurance")
        elif policy['policy_type'].lower() == "full insurance":
            print("Press U to update the insurance type from full insurance to third party")
            choice = input("Enter Choice: ")
            if choice.upper() == 'U':
                policies[found_idx]['policy_type'] = "ThirdParty"
                # Recalculate premium? Requirement doesn't explicitly say, but usually yes. 
                # For now, just updating type as per requirement text.
                save_data(POLICIES_FILE, policies)
                print("Policy Type Updated Successfully!")
            else:
                print("Invalid choice")
    else:
        print("Policy ID not found.")

def view_policies():
    print("\n--- View Policies ---")
    print("1. View all Insurance")
    print("2. View Insurance by Vehicle Id") # Requirement says Vehicle Id, but usually Vehicle No is unique. Assuming Vehicle No or we need a Vehicle ID field? US009 says VehicleNo is String. Let's assume VehicleNo.
    print("3. View Insurance by Policy Id")
    
    choice = input("Enter Choice: ")
    policies = load_data(POLICIES_FILE)
    
    if choice == '1':
        for p in policies:
            print(p)
    elif choice == '2':
        v_no = input("Enter Vehicle No: ") # Interpreting Vehicle Id as Vehicle No
        found = False
        for p in policies:
            if p['vehicle_no'] == v_no:
                print(p)
                found = True
        if not found:
            print("No policies found for this Vehicle No.")
    elif choice == '3':
        try:
            p_id = int(input("Enter Policy ID: "))
            found = False
            for p in policies:
                if p['policy_no'] == p_id:
                    print(p)
                    found = True
                    break
            if not found:
                print("Policy ID not found.")
        except ValueError:
            print("Invalid Policy ID")
    else:
        print("Invalid Choice")

def underwriter_menu():
    uid = underwriter_login()
    if uid is None:
        return

    while True:
        print("\n--- UnderWriter Menu ---")
        print("1. Create a new Vehicle Insurance")
        print("2. Renewal of a Policy")
        print("3. Changing of a policy")
        print("4. View Policy")
        print("5. Exit") # Added Exit for navigation
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            create_vehicle_insurance(uid)
        elif choice == '2':
            renew_policy(uid)
        elif choice == '3':
            change_policy_type()
        elif choice == '4':
            view_policies()
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")
