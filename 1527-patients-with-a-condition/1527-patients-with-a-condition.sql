# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE conditions REGEXP '\\bDIAB1'
/*WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%' ;*/