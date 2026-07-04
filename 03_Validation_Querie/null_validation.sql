-- Null Validation --

SELECT *
FROM target_sales
WHERE customer_id IS NULL
   OR customer_name IS NULL
   OR product_id IS NULL
   OR product_name IS NULL
   OR category IS NULL
   OR order_date IS NULL
   OR quantity IS NULL
   OR unit_price IS NULL
   OR city IS NULL
   OR payment_mode IS NULL;