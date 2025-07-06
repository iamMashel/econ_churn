
-- Revenue, AOV, Orders
SELECT 
    SUM((price - discount) * quantity) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    AVG((price - discount) * quantity) AS avg_order_value
FROM orders;


--  Monthly Sales Trend
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM((price - discount) * quantity) AS revenue
FROM orders
GROUP BY month
ORDER BY month;


