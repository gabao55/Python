DELETE p.bio FROM users as u
LEFT JOIN profiles as p 
ON p.user_id = u.id
WHERE u.first_name='Katelyn';	