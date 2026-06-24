# ============================================================
# STEP 1: EXTRACT
# Read raw data from CSV file
# ============================================================

import pandas as pd

def extract_data(filepath):
    print("=" * 50)
    print("STEP 1: EXTRACTING DATA FROM CSV")
    print("=" * 50)

    # Read the CSV file into a DataFrame (like a table)
    df = pd.read_csv(filepath)

    print(f"✅ File loaded: {filepath}")
    print(f"📊 Rows found: {len(df)}")
    print(f"📋 Columns found: {list(df.columns)}")
    print("\n--- First 5 rows (preview) ---")
    print(df.head())
    print("\n--- Data types ---")
    print(df.dtypes)

    return df

if __name__ == "__main__":
    df = extract_data("data/sales.csv")
