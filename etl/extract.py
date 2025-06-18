import pandas as pd
import os

def extract_orders(csv_path='data/orders.csv'):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"File not found: {csv_path}")
    
    try:
        df = pd.read_csv(csv_path, dtype={"Card Number": str})
        print("[Extract] Loaded CSV successfully.")
        return df
    except Exception as e:
        print(f"[Extract] Failed to read CSV: {e}")
        return None
