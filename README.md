# Star Protect Vehicle Insurance System

## Overview
A console-based application for managing vehicle insurance policies. The system supports two roles: Administrator and UnderWriter. It allows Administrators to manage UnderWriter accounts and UnderWriters to manage vehicle insurance policies, including creation, renewal, and modification.

## Features

### Administrator
- **Login**: Secure access with default credentials.
- **Manage UnderWriters**:
  - Register new UnderWriters (Auto-generated ID).
  - Search UnderWriters by ID or View All.
  - Update UnderWriter passwords.
  - Delete UnderWriters.
- **View Reports**: View all vehicles registered by a specific UnderWriter.

### UnderWriter
- **Login**: Access using credentials created by the Admin.
- **Manage Policies**:
  - Create new Vehicle Insurance Policies (Auto-calculated premium and dates).
  - Renew existing policies.
  - Change Policy Type (Full Insurance to Third Party).
  - View Policies (All, by Vehicle ID, or by Policy ID).

## Prerequisites
- Python 3.x

## Setup & Installation
1. Clone the repository or download the source code.
2. Ensure you have Python installed.
3. No external dependencies are required (uses standard libraries).

## How to Run
1. Open a terminal/command prompt in the project directory.
2. Run the main application:
   ```bash
   python main.py
   ```

## Default Credentials
**Administrator Login:**
- **Username:** `admin`
- **Password:** `admin123`

**UnderWriter Login:**
- Use the **User ID** generated upon registration (e.g., 1001).
- Use the **Password** set during registration.

## Project Structure
- `main.py`: Application entry point and main menu.
- `admin_service.py`: Contains logic for Administrator features.
- `underwriter_service.py`: Contains logic for UnderWriter features.
- `models.py`: Defines `UnderWriter` and `VehiclePolicy` classes.
- `database.py`: Handles loading and saving data to JSON files.
- `utils.py`: Utility functions for validation, date manipulation, and calculations.
- `data/`: Directory containing `underwriters.json` and `policies.json` for data persistence.

## Data Persistence
All data is stored in JSON files within the `data/` directory. This ensures that UnderWriter accounts and Insurance Policies are preserved between application restarts.
