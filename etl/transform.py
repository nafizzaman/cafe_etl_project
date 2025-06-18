import pandas as pd

def transform_orders(df):
    print("[Transform] Starting data transformation...")

    # Drop PII columns
    df = df.drop(columns=['Customer Name', 'Card Number'], errors='ignore')

    # Convert Date/Time to datetime
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')

    # Remove rows with missing or invalid key fields
    df = df.dropna(subset=['Drink', 'Qty', 'Price', 'Branch', 'Payment Type', 'Date/Time'])

    # Remove rows with invalid quantity or price
    df = df[(df['Qty'] > 0) & (df['Price'] > 0)]

    print("[Transform] Transformation complete.")
    return df
