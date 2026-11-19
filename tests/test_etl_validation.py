import csv
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent

CSV_FILE = (
    PROJECT_ROOT
    / "01_Source_Data"
    / "Sales_ETL_Validation_Project_60Rows.csv"
)

TRANSFORMATION_SQL = (
    PROJECT_ROOT
    / "02_SQL_Scripts"
    / "etl_transformation.sql"
)

EXPECTED_COLUMNS = [
    "order_id",
    "customer_id",
    "customer_name",
    "product_id",
    "product_name",
    "category",
    "order_date",
    "quantity",
    "unit_price",
    "discount_percent",
    "city",
    "payment_mode",
]


@pytest.fixture
def sales_data():
    with open(CSV_FILE, newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


# 1. Source file validation
def test_source_file_exists():
    assert CSV_FILE.exists()


# 2. Column validation
def test_expected_columns(sales_data):
    assert list(sales_data[0].keys()) == EXPECTED_COLUMNS


# 3. Record count validation
def test_expected_record_count(sales_data):
    assert len(sales_data) == 60


# 4. Duplicate record validation
def test_duplicate_order_ids_are_detected(sales_data):
    order_ids = [row["order_id"] for row in sales_data]

    duplicates = [
        order_id
        for order_id in set(order_ids)
        if order_ids.count(order_id) > 1
    ]

    assert duplicates == ["1010"]


# 5. Missing value validation
def test_expected_missing_values_are_detected(sales_data):
    missing_values = []

    for row_number, row in enumerate(sales_data, start=2):
        for column, value in row.items():
            if value.strip() == "":
                missing_values.append((row_number, column))

    expected_missing_values = [
        (12, "customer_id"),
        (19, "order_date"),
        (35, "quantity"),
        (58, "city"),
    ]

    assert missing_values == expected_missing_values


# 6. Quantity validation
def test_quantity_data_quality(sales_data):
    invalid_quantities = []

    for row_number, row in enumerate(sales_data, start=2):
        value = row["quantity"].strip()

        if value == "" or int(value) <= 0:
            invalid_quantities.append(row_number)

    assert invalid_quantities == [35]


# 7. Unit price validation
def test_invalid_unit_prices_are_detected(sales_data):
    invalid_prices = []

    for row_number, row in enumerate(sales_data, start=2):
        price = float(row["unit_price"])

        if price <= 0:
            invalid_prices.append((row_number, price))

    assert invalid_prices == [(23, -500.0)]


# 8. Discount validation
def test_invalid_discounts_are_detected(sales_data):
    invalid_discounts = []

    for row_number, row in enumerate(sales_data, start=2):
        discount = float(row["discount_percent"])

        if not 0 <= discount <= 100:
            invalid_discounts.append((row_number, discount))

    assert invalid_discounts == [(41, 120.0)]


# 9. Transformation SQL file validation
def test_transformation_sql_exists():
    assert TRANSFORMATION_SQL.exists()


# 10. SQL column name validation
def test_transformation_column_name_is_correct():
    sql = TRANSFORMATION_SQL.read_text(encoding="utf-8").lower()

    assert "discount_percent" in sql
    assert "discount_precent" not in sql


# 11. Discount calculation validation
def test_discount_calculation():
    quantity = 2
    unit_price = 1000
    discount_percent = 10

    discount_amount = (
        quantity * unit_price * discount_percent / 100
    )

    assert discount_amount == 200


# 12. Final amount calculation validation
def test_final_amount_calculation():
    quantity = 2
    unit_price = 1000
    discount_percent = 10

    gross_amount = quantity * unit_price

    discount_amount = (
        gross_amount * discount_percent / 100
    )

    final_amount = gross_amount - discount_amount

    assert final_amount == 1800


# 13. High value order validation
def test_high_value_order_status():
    final_amount = 5000

    status = (
        "High Value"
        if final_amount >= 5000
        else "Normal"
    )

    assert status == "High Value"


# 14. Normal order validation
def test_normal_order_status():
    final_amount = 4999

    status = (
        "High Value"
        if final_amount >= 5000
        else "Normal"
    )

    assert status == "Normal"