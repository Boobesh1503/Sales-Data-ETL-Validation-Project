INSERT INTO target_sales
SELECT
    order_id,
    customer_id,
    customer_name,
    product_id,
    product_name,
    category,
    order_date,
    quantity,
    unit_price,
    discount_percent,

    (quantity * unit_price * discount_precent / 100),

    (quantity * unit_price)
    - (quantity * unit_price * discount_precent / 100),

    CASE
        WHEN ((quantity * unit_price)
        - (quantity * unit_price * discount_precent / 100)) >= 5000
        THEN 'High Value'
        ELSE 'Normal'
    END,

    city,
    payment_mode

FROM source_sales;