SELECT e.name, b.bonus
FROM Employee as e
LEFT JOIN Bonus as b
ON e.empId = b.empId 
WHERE b.bonus < 1000 || b.bonus is null;