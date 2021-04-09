-- Between selects a range of numeric values:
SELECT * FROM users
WHERE
	created_at BETWEEN '2021-09-04 11:33:50'
AND 
	'2021-11-22 06:47:54';
