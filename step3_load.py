# ============================================================
# STEP 3: LOAD
# Save cleaned data into a SQL database (SQLite)
# SQLite = a database stored as a single file, no server needed
# ============================================================

import sqlite3
import pandas as pd
import os

DB_PATH = "output/sales_database.db"

def load_data(df_clean, df_revenue):
    print("\n" + "=" * 50)
    print("STEP 3: LOADING DATA INTO SQL DATABASE")
    print("=" * 50)

    os.makedirs("output", exist_ok=True)

    # Connect to SQLite (creates the file if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)

    # --- Save full cleaned data as table "orders" ---
    df_clean.to_sql("orders", conn, if_exists="replace", index=False)
    print(f"✅ Table 'orders' created — {len(df_clean)} rows saved")

    # --- Save revenue data as table "completed_orders" ---
    df_revenue.to_sql("completed_orders", conn, if_exists="replace", index=False)
    print(f"✅ Table 'completed_orders' created — {len(df_revenue)} rows saved")

    # --- Create a summary table using SQL ---
    summary_query = """
        SELECT
            category,
            COUNT(order_id)         AS total_orders,
            SUM(quantity)           AS total_units,
            ROUND(SUM(total_amount), 2) AS total_revenue,
            ROUND(AVG(total_amount), 2) AS avg_order_value
        FROM completed_orders
        GROUP BY category
        ORDER BY total_revenue DESC
    """
    df_summary = pd.read_sql_query(summary_query, conn)
    df_summary.to_sql("category_summary", conn, if_exists="replace", index=False)
    print(f"✅ Table 'category_summary' created")

    # --- Verify what's in the database ---
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"\n📂 Tables in database: {[t[0] for t in tables]}")
    print(f"📁 Database saved at: {DB_PATH}")

    conn.close()
    return DB_PATH

def query_database(query, db_path=DB_PATH):
    """Helper: run any SQL query and get results as DataFrame"""
    conn = sqlite3.connect(db_path)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

if __name__ == "__main__":
    from step1_extract import extract_data
    from step2_transform import transform_data
    raw_df = extract_data("data/sales.csv")
    clean_df, revenue_df = transform_data(raw_df)
    load_data(clean_df, revenue_df)
