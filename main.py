from etl.extract import extract_orders
from etl.extract import extract_orders
from etl.transform import transform_orders

df = extract_orders()
print(df.head())


df_raw = extract_orders()
df_clean = transform_orders(df_raw)

print("\n[Cleaned Data]")
print(df_clean.head())
