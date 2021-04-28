update users set salary = abs(random()/1000000000000000);

-- Querying data based on salary:
SELECT * FROM users
WHERE salary BETWEEN 1000 AND 2000
ORDER BY salary ASC;