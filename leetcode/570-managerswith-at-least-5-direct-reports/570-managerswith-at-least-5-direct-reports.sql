ELECT e.name
FROM Employee as e, (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) > 4
) manager_id
WHERE e.id = manager_id.managerId ;