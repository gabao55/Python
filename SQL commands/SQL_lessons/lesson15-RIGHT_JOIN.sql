-- Right join shows all the right table values, even if there is no relation between the data and the left table:
SELECT u.id as uid, p.id as pid,
u.first_name, p.bio
FROM users AS u
RIGHT JOIN profiles AS p
ON u.id = p.user_id;