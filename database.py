import json
import os
from datetime import datetime, timedelta

DATA_DIR = "data"
UNDERWRITERS_FILE = os.path.join(DATA_DIR, "underwriters.json")
POLICIES_FILE = os.path.join(DATA_DIR, "policies.json")

def ensure_data_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(UNDERWRITERS_FILE):
        with open(UNDERWRITERS_FILE, 'w') as f:
            json.dump([], f)
    if not os.path.exists(POLICIES_FILE):
        with open(POLICIES_FILE, 'w') as f:
            json.dump([], f)

def load_data(filename):
    ensure_data_files()
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(filename, data):
    ensure_data_files()
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_next_id(filename, id_field):
    data = load_data(filename)
    if not data:
        return 1001 # Start IDs from 1001
    
    max_id = 0
    for item in data:
        if item.get(id_field, 0) > max_id:
            max_id = item.get(id_field)
    return max_id + 1
