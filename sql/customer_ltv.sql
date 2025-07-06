 -- Most Valuable Customers
 SELECT 
    c.customer_id,
    SUM((o.price - o.discount) * o.quantity) AS total_spent,
    COUNT(DISTINCT o.order_id) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;


-- Repeat Purchase Rate
SELECT 
    ROUND(
        100.0 * COUNT(DISTINCT customer_id) FILTER (WHERE order_count > 1) / COUNT(DISTINCT customer_id), 2
    ) AS repeat_purchase_rate
FROM (
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
) sub;
