# Write your MySQL query statement below
SELECT a.sell_date, COUNT(DISTINCT(a.product)) as num_sold, GROUP_CONCAT(DISTINCT(a.product) ORDER BY a.product) as products
FROM Activities as a
GROUP BY a.sell_date ;