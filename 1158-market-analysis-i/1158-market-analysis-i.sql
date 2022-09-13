# Write your MySQL query statement below
SELECT u.user_id as buyer_id, u.join_date, COUNT(o.order_date) as orders_in_2019
FROM Users as u
LEFT JOIN Orders as o ON u.user_id = o.buyer_id AND YEAR(o.order_date) = '2019'
GROUP BY u.user_id ;