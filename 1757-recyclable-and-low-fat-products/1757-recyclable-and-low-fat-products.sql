# Write your MySQL query statement below
SELECT p.product_id
FROM Products as p
WHERE p.low_fats = 'Y' and p.recyclable = 'Y';