-- SQL solution
-- Problem: Customer Order Frequency

SELECT c.customer_id, c.name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Product p ON o.product_id = p.product_id
GROUP BY c.customer_id, c.name
HAVING
    SUM(CASE WHEN MONTH(o.order_date) = 6 THEN o.quantity * p.price ELSE 0 END) >= 100
    AND
    SUM(CASE WHEN MONTH(o.order_date) = 7 THEN o.quantity * p.price ELSE 0 END) >= 100;
