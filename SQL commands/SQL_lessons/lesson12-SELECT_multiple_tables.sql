-- Selecting multiple tables:
SELECT u.id AS uid, p.id AS pid,
p.bio, u.first_name
FROM users AS u, profiles AS p
WHERE u.id = p.user_id;