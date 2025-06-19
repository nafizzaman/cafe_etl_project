import os
import logging
from etl.extract import extract_orders
from etl.transform import transform_orders
from etl.load import load_to_sql

# Setup logging
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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
        print("6. Run full ETL pipeline")
        print("7. Export cleaned data to output.csv")
        print("8. View raw CSV data")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            df_raw = extract_orders()
            logging.info("Extracted data from CSV")
        elif choice == '2':
            if df_raw is None:
                print("[!] Please run extraction first.")
            else:
                df_clean = transform_orders(df_raw)
                logging.info("Transformed data (PII removed, cleaned)")
        elif choice == '3':
            if df_clean is None:
                print("[!] Please run transform first.")
            else:
                load_to_sql(df_clean)
                logging.info("Loaded data into SQL Server")
        elif choice == '4':
            if df_clean is not None:
                print(df_clean)
            else:
                print("[!] No cleaned data to show.")
        elif choice == '5':
            clear_screen()
        elif choice == '6':
            df_raw = extract_orders()
            df_clean = transform_orders(df_raw)
            load_to_sql(df_clean)
            logging.info("Ran full ETL pipeline")
        elif choice == '7':
            if df_clean is not None:
                df_clean.to_csv("output.csv", index=False)
                print("[Export] Saved cleaned data to output.csv")
                logging.info("Exported cleaned data to output.csv")
            else:
                print("[!] No cleaned data to export.")
        elif choice == '8':
            if df_raw is not None:
                print(df_raw)
            else:
                print("[!] No raw data to show. Run extraction first.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("[!] Invalid option. Try again.")
