import os
from etl.extract import extract_orders
from etl.transform import transform_orders
from etl.load import load_to_sql

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cli_menu():
    df_raw = None
    df_clean = None

    while True:
        print("\n🧃 Café ETL Menu")
        print("----------------------")
        print("1. Extract data from CSV")
        print("2. Transform data (clean + remove PII)")
        print("3. Load data into SQL Server")
        print("4. View cleaned data")
        print("5. Clear screen")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            df_raw = extract_orders()
        elif choice == '2':
            if df_raw is None:
                print("[!] Please run extraction first.")
            else:
                df_clean = transform_orders(df_raw)
        elif choice == '3':
            if df_clean is None:
                print("[!] Please run transform first.")
            else:
                load_to_sql(df_clean)
        elif choice == '4':
            if df_clean is not None:
                print(df_clean)
            else:
                print("[!] No cleaned data to show.")
        elif choice == '5':
            clear_screen()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid option. Try again.")
