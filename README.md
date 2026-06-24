# ETL Data Pipeline using Python & SQL

A complete ETL (Extract, Transform, Load) data pipeline that processes 
sales data automatically and generates a business dashboard report.

## What this project does
- **Extract** – Reads raw sales data from CSV file
- **Transform** – Cleans missing values, adds calculated columns using Pandas
- **Load** – Stores cleaned data into SQLite database with 3 SQL tables
- **Report** – Generates automated HTML dashboard with revenue analysis

## Technologies Used
- Python 3
- Pandas
- SQLite & SQL
- HTML

## Project Structure
etl_project/
├── main.py              # Run this file to start pipeline
├── step1_extract.py     # Extract data from CSV
├── step2_transform.py   # Clean & transform data
├── step3_load.py        # Load into SQL database
├── step4_report.py      # Generate HTML report
├── requirements.txt     # Required packages
└── sales.csv            # Sample sales data (25 records)

## How to Run
pip install pandas openpyxl
python main.py

## Output
- SQL Database with 3 tables (orders, completed_orders, category_summary)
- HTML Sales Dashboard showing:
  - Total Revenue: Rs. 5,63,500
  - Monthly revenue trends
  - Category-wise analysis
  - Top 5 customers
  - City-wise performance

## Key Results
| Metric | Value |
|--------|-------|
| Total Revenue | Rs. 5,63,500 |
| Completed Orders | 20 |
| Avg Order Value | Rs. 28,175 |
| Top City | Mumbai (Rs. 2,47,000) |
| Top Category | Electronics (Rs. 4,55,600) |
