# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product as p
LEFT JOIN Sales as s
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31' ;