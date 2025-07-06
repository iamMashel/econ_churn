-- PRODUCT INSIGHTS

-- Top-Selling Products
SELECT 
    p.product_name,
    SUM(o.quantity) AS units_sold,
    SUM((o.price - o.discount) * o.quantity) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;


--  Return Rate by Category

SELECT 
    p.category,
    COUNT(DISTINCT r.order_id)::FLOAT / COUNT(DISTINCT o.order_id) AS return_rate
FROM returns r
JOIN orders o ON r.order_id = o.order_id
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY return_rate DESC;
