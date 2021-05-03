UPDATE users as u
INNER JOIN profiles as p 
ON p.user_id = u.id
SET p.bio = CONCAT(p.bio, 'updated')
WHERE u.first_name='Katelyn';