-- Showing all the tables:
SELECT 
    name
FROM 
    sqlite_master 
WHERE 
    type ='table' AND 
    name NOT LIKE 'sqlite_%';

-- Showing table's info:	
PRAGMA table_info('users');

-- Inserting one data into the database:
INSERT into users (first_name, last_name, email, password_hash) VALUES
("Luiz", "Miranda", "123@gmail.com", "abcd");

-- Inserting multiple data into the database:
INSERT into users (first_name, last_name, email, password_hash) VALUES
("Luiz", "Micao", "1234@gmail.com", "abcde"), 
("Maria", "da Silva", "maria@hotmail.com", "senha1"),
("Julia", "" , "julinha@gmail.com", "senha2");