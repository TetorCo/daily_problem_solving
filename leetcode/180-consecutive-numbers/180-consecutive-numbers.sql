SELECT DISTINCT(num) as ConsecutiveNums
FROM (
    SELECT num, LEAD(num, 1) over() as num1, LEAD(num, 2) over() as num2
    FROM Logs
) logs
WHERE num = num1 AND num1 = num2 ;

# WITH new_logs as
# (
#     SELECT num, LEAD(num, 1) over() as num1, LEAD(num, 2) over() as num2
#     FROM Logs
# )

# SELECT DISTINCT(num) as ConsecutiveNums
# FROM new_logs
# WHERE num = num1 AND num = num2 ;