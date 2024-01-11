SELECT e.employee_id, e.name, e1.reports_count, e1.average_age
FROM Employees as e, (
  SELECT reports_to, COUNT(reports_to) as reports_count, ROUND(SUM(age) / COUNT(age)) as average_age
  FROM Employees
  WHERE reports_to IS NOT NULL
  GROUP BY reports_to
) e1
WHERE e.employee_id = e1.reports_to 
ORDER BY e.employee_id ;