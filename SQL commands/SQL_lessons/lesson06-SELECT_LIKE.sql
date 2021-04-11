-- Select like returns a similar value to the specified
-- Selecting everything that finishes with an "a":
SELECT * FROM users
WHERE first_name LIKE '%a';

-- Selecting everything that begins with an "be":
SELECT * FROM users
WHERE first_name LIKE 'be%';

-- Selecting everything that contains an "mo":
SELECT * FROM users
WHERE first_name LIKE '%mo%';

-- Selecting everything that contains an "j" separated from "cob" by one character:
SELECT * FROM users
WHERE first_name LIKE 'j_cob';

-- Selecting everything that contains five characters:
SELECT * FROM users
WHERE first_name LIKE '_____';