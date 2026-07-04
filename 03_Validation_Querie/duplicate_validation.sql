-- Duplicate Validation --

SELECT
    customer_id,
    product_id,
    order_date,
    COUNT(*) AS duplicate_count
FROM target_sales
GROUP BY
    customer_id,
    product_id,
    order_date
HAVING COUNT(*) > 1;