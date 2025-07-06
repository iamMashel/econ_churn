-- CUSTOMER RETENTION INSIGHTS (SQL-based cohort)
-- Cohort Analysis Prep (by first order month)

SELECT 
    c.customer_id,
    DATE_TRUNC('month', c.first_order_date) AS cohort_month,
    DATE_TRUNC('month', o.order_date) AS order_month
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;
