-- Left join shows all the left table values, even if there is no relation between the data and the right table:
SELECT u.id as uid, p.id as pid,
u.first_name, p.bio
FROM users AS u
LEFT JOIN profiles AS p
ON u.id = p.user_id;