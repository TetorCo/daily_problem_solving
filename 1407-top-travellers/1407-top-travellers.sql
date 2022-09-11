# Write your MySQL query statement below
SELECT u.name, IF(r.distance, SUM(r.distance), 0) as travelled_distance
FROM Users as u
LEFT JOIN Rides as r
ON u.id = r.user_id 
GROUP BY r.user_id 
ORDER BY SUM(r.distance) DESC, u.name ;