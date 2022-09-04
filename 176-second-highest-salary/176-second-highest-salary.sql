# Write your MySQL query statement below
/*SELECT max(salary) as 'SecondHighestSalary'
FROM Employee
WHERE salary < (SELECT max(salary) FROM Employee) ; */

SELECT IFNULL(
    Null,
    (SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC LIMIT 1 OFFSET 1)
) as 'SecondHighestSalary'