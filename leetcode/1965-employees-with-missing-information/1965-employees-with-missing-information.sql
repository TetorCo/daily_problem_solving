# Write your MySQL query statement below
/* SELECT e1.employee_id
FROM 
    (SELECT *
    FROM Employees
    LEFT JOIN Salaries
    USING (employee_id)
    UNION
    SELECT *
    FROM Employees
    RIGHT JOIN Salaries
    USING (employee_id)) as e1
WHERE e1.name IS NULL OR e1.salary IS NULL
ORDER BY e1.employee_id ; */

SELECT e1.employee_id
FROM
    (SELECT e.employee_id, e.name, s.salary
     FROM Employees as e
     LEFT JOIN Salaries as s
     ON e.employee_id = s.employee_id
     UNION
     SELECT s.employee_id, e.name, s.salary
     FROM Employees as e
     RIGHT JOIN Salaries as s
     ON e.employee_id = s.employee_id
    ) as e1
WHERE e1.name IS NULL OR e1.salary IS NULL
ORDER BY e1.employee_id ;