-- WHERE indicates the table that is refered.
-- Filtering registers:
SELECT
	*
FROM
	users
WHERE
	id="5";
	
SELECT
	*
FROM
	users
WHERE
	id>=5;
	
SELECT
	*
FROM
	users
WHERE
	id<>5 AND first_name="Luiz" OR password_hash="senha2";