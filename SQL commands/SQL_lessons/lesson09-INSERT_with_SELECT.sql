-- Inserting data in a table using another table:
INSERT INTO profiles
(bio, description, user_id)
-- Concatenating strings with ||:
SELECT (first_name || "'s bio"), 
(first_name || "'s description"), 
id 
from users;