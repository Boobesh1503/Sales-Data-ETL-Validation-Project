CREATE TABLE target_sales (
    order_id INT,
    customer_id VARCHAR(10),
    customer_name VARCHAR(50),
    product_id VARCHAR(10),
    product_name VARCHAR(50),
    category VARCHAR(30),
    order_date DATE,
    quantity INT,
    unit_price DECIMAL(10,2),
    discount_percent DECIMAL(5,2),
    discount_amount DECIMAL(10,2),
    final_amount DECIMAL(10,2),
    order_status VARCHAR(20),
    city VARCHAR(30),
    payment_mode VARCHAR(30)
);