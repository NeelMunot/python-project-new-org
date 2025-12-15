from admin_service import admin_menu
from underwriter_service import underwriter_menu
from database import ensure_data_files

def main():
    ensure_data_files()
    print("Welcome to Star Protect Vehicle System")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Admin Login")
        print("2. UnderWriter Login")
        print("3. Exit")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            admin_menu()
        elif choice == '2':
            underwriter_menu()
        elif choice == '3':
            print("Exiting Application...")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    main()
