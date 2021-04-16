-- Using limit for imposing limits of shown values for my select:
SELECT id, first_name, email 
FROM users
WHERE id BETWEEN 30 AND 80
ORDER BY id ASC
LIMIT 5;

-- Using offset for defining the start point of the limit:
SELECT id, first_name, email 
FROM users
WHERE id BETWEEN 30 AND 80
ORDER BY id ASC
LIMIT 5 OFFSET 15;