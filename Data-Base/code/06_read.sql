-- 06_read.sql

USE pet_shop;

CREATE TABLE cats (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT
);

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
       
-- READ
SELECT * FROM cats;
SELECT name FROM cats;
SELECT age, breed From cats;

-- 특정 조건을 만족하는 애를 가져옴
SELECT * FROM cats WHERE age=4;
SELECT name FROM cats WHERE age=4;
SELECT age breed FROM cats WHERE age=4;

-- 대소문자가 상관없음(Case Insensitive)
SELECT * FROM cats WHERE name='Egg';
SELECT * FROM cats WHERE name='egg';
SELECT * FROM cats WHERE name='eGg';

-- AS 구문 활용법(변경)
SELECT name AS '이름' FROM cats;
SELECT name AS '이름', breed AS '종' FROM cats;
