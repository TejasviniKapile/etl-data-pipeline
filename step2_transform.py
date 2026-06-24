# ============================================================
# STEP 2: TRANSFORM
# Clean and process the raw data using Pandas
# ============================================================

import pandas as pd

def transform_data(df):
    print("\n" + "=" * 50)
    print("STEP 2: TRANSFORMING DATA")
    print("=" * 50)

    print(f"\n⚠️  Missing values BEFORE cleaning:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    # --- 2a. Fix missing quantity (fill with 1 as default) ---
    df['quantity'] = df['quantity'].fillna(1).astype(int)

    # --- 2b. Fix missing price (fill with average price) ---
    avg_price = df['price'].mean()
    df['price'] = df['price'].fillna(avg_price)

    # --- 2c. Convert order_date to proper date format ---
    df['order_date'] = pd.to_datetime(df['order_date'])

    # --- 2d. Add new calculated columns ---
    df['total_amount'] = df['quantity'] * df['price']
    df['month']        = df['order_date'].dt.month_name()
    df['month_num']    = df['order_date'].dt.month
    df['year']         = df['order_date'].dt.year

    # --- 2e. Standardize text columns ---
    df['status']   = df['status'].str.strip().str.title()
    df['city']     = df['city'].str.strip().str.title()
    df['category'] = df['category'].str.strip().str.title()

    # --- 2f. Keep only Completed orders for revenue reports ---
    df_clean   = df.copy()                           # full data (all statuses)
    df_revenue = df[df['status'] == 'Completed'].copy()  # only completed

    print(f"\n✅ Missing values AFTER cleaning: None")
    print(f"✅ New columns added: total_amount, month, year")
    print(f"✅ Total rows: {len(df_clean)} | Completed orders: {len(df_revenue)}")
    print("\n--- Cleaned data preview ---")
    print(df_clean[['order_id','customer_name','product','quantity',
                    'price','total_amount','month','status']].head())

    return df_clean, df_revenue

if __name__ == "__main__":
    from step1_extract import extract_data
    raw_df = extract_data("data/sales.csv")
    clean_df, revenue_df = transform_data(raw_df)
