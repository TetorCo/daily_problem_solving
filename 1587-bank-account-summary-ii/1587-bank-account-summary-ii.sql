# Write your MySQL query statement below
SELECT us.name, SUM(tr.amount) as balance
FROM Transactions as tr
LEFT JOIN Users as us
ON us.account = tr.account
GROUP BY tr.account
HAVING balance >= 10000;