SELECT c.customer_id
FROM Customer as c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT(c.product_key)) =  (
  SELECT COUNT(DISTINCT(product_key))
  FROM Product
) ;