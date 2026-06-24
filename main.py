# ============================================================
# 🚀 MAIN ETL PIPELINE RUNNER
# Run this file to execute all 4 steps automatically
# Usage: python3 main.py
# ============================================================

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from step1_extract   import extract_data
from step2_transform import transform_data
from step3_load      import load_data
from step4_report    import generate_reports

print("\n🚀 ETL PIPELINE STARTING...\n")

# Step 1: Extract
raw_df = extract_data("data/sales.csv")

# Step 2: Transform
clean_df, revenue_df = transform_data(raw_df)

# Step 3: Load into database
load_data(clean_df, revenue_df)

# Step 4: Generate reports
generate_reports()

print("\n" + "=" * 50)
print("✅ ETL PIPELINE COMPLETE!")
print("=" * 50)
print("📁 Output files:")
print("   output/sales_database.db    ← SQL database")
print("   reports/sales_report.html   ← Open in browser")
print("   reports/monthly_revenue.csv")
print("   reports/category_summary.csv")
print("   reports/top_customers.csv")
print("   reports/city_revenue.csv")
