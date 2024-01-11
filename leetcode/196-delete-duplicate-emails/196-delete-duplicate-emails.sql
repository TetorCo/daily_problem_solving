# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE one
FROM Person as one, Person as two 
WHERE one.id > two.id AND one.email=two.email ;