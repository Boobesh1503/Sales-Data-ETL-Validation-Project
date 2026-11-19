import csv
from pathlib import Path

csv_file = Path("01_Source_Data/Sales_ETL_Validation_Project_60Rows.csv")

with open(csv_file, newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

print("\n========== DATA QUALITY ISSUES ==========\n")

# 1. Duplicate order IDs
order_ids = [row["order_id"] for row in rows]

for order_id in set(order_ids):
    if order_ids.count(order_id) > 1:
        print(f"Duplicate order_id: {order_id}")

# 2. Empty values
for row_number, row in enumerate(rows, start=2):
    for column, value in row.items():
        if value.strip() == "":
            print(f"Empty value | Row {row_number} | Column: {column}")

# 3. Invalid quantity
for row_number, row in enumerate(rows, start=2):
    if row["quantity"].strip():
        if int(row["quantity"]) <= 0:
            print(f"Invalid quantity | Row {row_number} | Value: {row['quantity']}")

# 4. Invalid unit price
for row_number, row in enumerate(rows, start=2):
    if row["unit_price"].strip():
        if float(row["unit_price"]) <= 0:
            print(f"Invalid unit_price | Row {row_number} | Value: {row['unit_price']}")

# 5. Invalid discount
for row_number, row in enumerate(rows, start=2):
    if row["discount_percent"].strip():
        discount = float(row["discount_percent"])

        if not 0 <= discount <= 100:
            print(f"Invalid discount | Row {row_number} | Value: {discount}")

print("\n========== SCAN COMPLETED ==========")