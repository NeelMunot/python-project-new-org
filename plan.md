# Star Protect Vehicle - Console Application Plan

## 1. Project Setup
- [ ] Create project directory structure.
- [ ] Create `data` directory for JSON files.
- [ ] Create `models.py` for data classes.
- [ ] Create `database.py` for file handling (persistence).
- [ ] Create `utils.py` for helper functions (date parsing, validation).
- [ ] Create `admin_service.py` for Admin logic.
- [ ] Create `underwriter_service.py` for UnderWriter logic.
- [ ] Create `main.py` for the application entry point and menu loop.

## 2. Data Models (`models.py`)
- [ ] Define `UnderWriter` class.
    - Attributes: `uid` (int), `name` (str), `dob` (str/date), `joining_date` (str/date), `password` (str).
- [ ] Define `VehiclePolicy` class.
    - Attributes: `policy_no` (int), `vehicle_no` (str), `vehicle_type` (str), `customer_name` (str), `engine_no` (int), `chasis_no` (int), `phone_no` (int), `policy_type` (str), `premium_amt` (float), `from_date` (str/date), `to_date` (str/date), `underwriter_id` (int).

## 3. Persistence Layer (`database.py`)
- [ ] Implement `load_data(filename)` to read JSON.
- [ ] Implement `save_data(filename, data)` to write JSON.
- [ ] Initialize default Admin credentials (hardcoded or in a config).
- [ ] Manage auto-increment IDs for UnderWriters and Policies.

## 4. Utility Functions (`utils.py`)
- [ ] Date validation and parsing.
- [ ] Password complexity check (alphanumeric + special char).
- [ ] Input validation helpers.
- [ ] Date arithmetic (add days).

## 5. Admin Features (`admin_service.py`)
- [ ] **US002**: Admin Login (Default: admin/admin123).
- [ ] **US003**: Register UnderWriter.
    - Auto-generate ID.
    - Validate password.
- [ ] **US004**: Search UnderWriter.
    - View All.
    - Search by ID.
- [ ] **US005**: Update UnderWriter Password.
- [ ] **US006**: Delete UnderWriter.
- [ ] **US007**: View Vehicles by UnderWriter ID.

## 6. UnderWriter Features (`underwriter_service.py`)
- [ ] **US008**: UnderWriter Login.
- [ ] **US009**: Create New Vehicle Insurance.
    - Auto-generate Policy No.
    - Auto-calculate Premium (Logic needed: e.g., based on type).
    - Auto-calculate ToDate.
- [ ] **US010**: Renew Policy.
    - Check expiry.
    - Update dates.
    - Create new record (history) or update existing? Requirement says "new record will be created".
- [ ] **US011**: Change Policy Type.
    - Full -> Third Party only.
- [ ] **US012**: View Policies.
    - View All.
    - View by Vehicle ID.
    - View by Policy ID.

## 7. Main Application (`main.py`)
- [ ] **US001**: Main Menu (Admin vs UnderWriter).
- [ ] Implement main loop.
- [ ] Handle navigation and exit.

## 8. Testing & Refinement
- [ ] Verify all User Stories.
- [ ] Check edge cases (invalid IDs, dates).
- [ ] Ensure data persistence works.
