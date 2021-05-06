-- Counting how often a name appears at the users table:
SELECT first_name, count(id) as total FROM users
GROUP BY first_name
-- Ordering by the total times a name appears at the table:
ORDER BY total DESC;