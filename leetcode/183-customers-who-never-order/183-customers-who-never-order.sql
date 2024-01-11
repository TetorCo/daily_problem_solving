# Write your MySQL query statement below
SELECT cus.name as Customers
FROM Customers as cus
LEFT JOIN Orders as ord
ON cus.id = ord.customerId 
WHERE ord.id is null;