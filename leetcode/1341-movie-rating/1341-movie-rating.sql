(SELECT u.name as results
FROM Users as u, (
    SELECT COUNT(user_id) as cnt_user, user_id
    FROM MovieRating
    GROUP BY user_id
) u1
WHERE u.user_id = u1.user_id
ORDER BY u1.cnt_user DESC, u.name
LIMIT 1)
UNION ALL
(SELECT m.title as results
FROM Movies as m, (
    SELECT ROUND(SUM(rating) / COUNT(rating), 1) as rating, movie_id
    FROM MovieRating
    WHERE DATE_FORMAT(created_at, '%b-%Y') = 'Feb-2020'
    GROUP BY movie_id
) m1
WHERE m.movie_id = m1.movie_id
ORDER BY m1.rating DESC, m.title
LIMIT 1)