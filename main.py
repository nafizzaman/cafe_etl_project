from etl.extract import extract_orders
from etl.transform import transform_orders
from etl.load import load_to_sql
from ui.cli import cli_menu

if __name__ == "__main__":
    cli_menu()

# df = extract_orders()
# print(df.head())


# df_raw = extract_orders()
# df_clean = transform_orders(df_raw)

# print("\n[Cleaned Data]")
# print(df_clean.head())


# df_raw = extract_orders()
# df_clean = transform_orders(df_raw)
# load_to_sql(df_clean)



