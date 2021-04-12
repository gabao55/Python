-- Select order orders the data by a criterium:
-- Ordering by ascendent id, then in case of equal id, order by descendent first_name:
SELECT id, first_name, email FROM users
WHERE id BETWEEN 30 AND 80
ORDER BY id ASC, first_name DESC;