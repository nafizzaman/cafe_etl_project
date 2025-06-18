import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()  # Load DB config from .env

def load_to_sql(df):
    print("[Load] Connecting to SQL Server...")

    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"TrustServerCertificate=yes;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("[Load] Connected. Inserting data...")

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO Orders (Drink, Qty, Price, Branch, PaymentType, OrderDateTime)
                VALUES (?, ?, ?, ?, ?, ?)
            """, row.Drink, row.Qty, row.Price, row.Branch, row['Payment Type'], row['Date/Time'])

        conn.commit()
        print(f"[Load] Inserted {len(df)} rows into SQL Server.")
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"[Load] Error: {e}")
