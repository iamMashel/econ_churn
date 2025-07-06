-- Average Rating by Product
SELECT 
    p.product_name,
    AVG(r.rating) AS avg_rating,
    COUNT(*) AS review_count
FROM reviews r
JOIN products p ON r.product_id = p.product_id
GROUP BY p.product_name
ORDER BY avg_rating DESC
LIMIT 10;
