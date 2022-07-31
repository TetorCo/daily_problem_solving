# Write your MySQL query statement below
SELECT *
FROM Cinema as cin
WHERE cin.id%2 != 0 and cin.description != 'boring'
ORDER BY cin.rating DESC;