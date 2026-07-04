-- Source to Target Validation --

SELECT
    s.order_id,
    s.customer_id AS source_customer_id,
    t.customer_id AS target_customer_id,
    s.product_id AS source_product_id,
    t.product_id AS target_product_id
FROM source_sales s
JOIN target_sales t
ON s.order_id = t.order_id
WHERE s.customer_id <> t.customer_id
   OR s.product_id <> t.product_id;