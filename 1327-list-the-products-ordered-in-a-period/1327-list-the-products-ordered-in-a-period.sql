SELECT p.product_name, o.unit
FROM (
    SELECT product_id, SUM(unit) as unit
    FROM Orders
    # WHERE order_date >= "2020-02-01" AND order_date <= "2020-02-29"
    WHERE DATE_FORMAT(order_date, '%b-%Y') = 'Feb-2020'
    GROUP BY product_id
    HAVING SUM(unit) > 99
) o
LEFT JOIN Products as p
ON p.product_id = o.product_id ;