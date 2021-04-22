-- Inner join shows the intersection values:
SELECT u.id as uid, p.id as pid,
u.first_name, p.bio
-- Left table:
FROM users AS u
-- Refering that we are using an inner join (right table):
INNER JOIN profiles AS p
-- Defining the join condition:
ON u.id = p.user_id
-- WHERE u.first_name LIKE '%am%'
-- ORDER BY u.first_name ASC
-- LIMIT 5;