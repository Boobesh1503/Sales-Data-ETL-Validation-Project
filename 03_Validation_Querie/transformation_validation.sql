-- Transformation Validation --

SELECT
    order_id,
    quantity,
    unit_price,
    discount_percent,
    discount_amount,
    final_amount,
    order_status
FROM target_sales
LIMIT 10; 