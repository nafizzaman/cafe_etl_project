from etl.extract import extract_orders

df = extract_orders()
print(df.head())
