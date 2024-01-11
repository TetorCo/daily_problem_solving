# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product as p
LEFT JOIN Sales as s
ON p.product_id = s.product_id
GROUP BY s.product_id
HAVING MAX(s.sale_date) <= '2019-03-31' AND MIN(s.sale_date) >= '2019-01-01' ;