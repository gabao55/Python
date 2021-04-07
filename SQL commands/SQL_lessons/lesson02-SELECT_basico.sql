-- Selecting all columns:
SELECT 
	* 
FROM 
	users;

-- Selecting specific columns:
SELECT
	email, id, first_name
FROM
	users;
	
-- Selecting same columns with nicknames:
SELECT
	email as e, id, first_name fn
FROM
	users;