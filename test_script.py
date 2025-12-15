from database import ensure_data_files, load_data, save_data, UNDERWRITERS_FILE, POLICIES_FILE
from models import UnderWriter, VehiclePolicy
from utils import validate_password, add_days, calculate_premium

def test_app():
    print("Testing Application Components...")
    
    # 1. Database Init
    ensure_data_files()
    print("Database initialized.")

    # 2. Utils
    assert validate_password("Admin@123") == True
    assert validate_password("admin") == False
    print("Password validation passed.")
    
    assert add_days("2023-01-01", 10) == "2023-01-11"
    print("Date addition passed.")
    
    prem = calculate_premium("4-wheeler", "Full Insurance")
    print(f"Calculated Premium: {prem}")

    # 3. Models & Persistence
    uw = UnderWriter(1001, "Test User", "1990-01-01", "2023-01-01", "Pass@123")
    data = [uw.to_dict()]
    save_data(UNDERWRITERS_FILE, data)
    loaded = load_data(UNDERWRITERS_FILE)
    assert len(loaded) == 1
    assert loaded[0]['name'] == "Test User"
    print("UnderWriter persistence passed.")

    vp = VehiclePolicy(2001, "KA 01 AB 1234", "4-wheeler", "Cust Name", 123, 456, 9876543210, "Full Insurance", 3000.0, "2023-01-01", "2024-01-01", 1001)
    p_data = [vp.to_dict()]
    save_data(POLICIES_FILE, p_data)
    loaded_p = load_data(POLICIES_FILE)
    assert len(loaded_p) == 1
    print("Policy persistence passed.")
    
    print("All basic tests passed!")

if __name__ == "__main__":
    test_app()
