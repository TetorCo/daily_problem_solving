# Write your MySQL query statement below
SELECT d.name as Department, e.name as employee, e.salary as Salary
FROM Employee as e
JOIN Department as d
ON e.departmentId = d.id
WHERE Salary = (SELECT MAX(Salary) FROM Employee WHERE departmentId = e.departmentId) ;