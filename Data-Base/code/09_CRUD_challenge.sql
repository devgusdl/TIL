-- 09_CRUD_challenge.sql

-- 1.새로운 DB 생성 (shirts_db)
CREATE DATABASE shirts_db;

USE shirts_db;

-- 2.shirts_db 에 shirts 테이블 생성
	-- 	id ⇒ INT, PK, AUTO_INCREMENT
	-- 	article ⇒ VARCHAR 50
	-- 	color ⇒ VARCHAR 50
	--  shirt_size ⇒ VARCHAR 5
	--  last_worn ⇒ INT

CREATE TABLE shirts(
	id INT PRIMARY KEY AUTO_INCREMENT,
	article VARCHAR(50),
	color VARCHAR(50),
	shirt_size VARCHAR(5),
	last_worn INT
    );
    


-- 3.입력 데이터 코드
-- INSERT INTO shirts (article, color, shirt_size, last_worn)  
-- VALUES 
-- 	('t-shirt', 'white', 'S', 10),
-- 	('t-shirt', 'green', 'S', 200),
-- 	('polo shirt', 'black', 'M', 10),
-- 	('tank top', 'blue', 'S', 50),
-- 	('t-shirt', 'pink', 'S', 0),
-- 	('polo shirt', 'red', 'M', 5),
-- 	('tank top', 'white', 'S', 200),
-- 	('tank top', 'blue', 'M', 15);
INSERT INTO shirts (article, color, shirt_size, last_worn)  
VALUES 
	('t-shirt', 'white', 'S', 10),
	('t-shirt', 'green', 'S', 200),
	('polo shirt', 'black', 'M', 10),
	('tank top', 'blue', 'S', 50),
	('t-shirt', 'pink', 'S', 0),
	('polo shirt', 'red', 'M', 5),
	('tank top', 'white', 'S', 200),
	('tank top', 'blue', 'M', 15);
    
-- 	1.새로운 데이터 ‘polo shirt’, ‘purlple’, ‘M’, 50 입력
INSERT INTO shirts(article, color, shirt_size, last_worn)
VALUES
	('polo shirt', 'purlple', 'M', 50);
    
SELECT * FROM shirts;

-- 	2.모든 셔츠의 article과 color 만 출력
SELECT article, color FROM shirts;

-- 	3.모든 M 사이즈 셔츠를 출력하되, id는 제외
SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size ='M';

-- 	4.모든 폴로 셔츠의 사이즈를 L로 변경
UPDATE shirts SET shirt_size = 'L' WHERE article = 'polo shirt';


-- 	5.last_worn 이 15인 셔츠의 last_worn 을 0으로 변경
UPDATE shirts SET last_worn = 0 WHERE last_worn = 15;


-- 	6.모든 흰색 셔츠의 사이즈를 ‘XS’ 로 바꾸고 색을 ‘off white’ 로 변경
UPDATE shirts SET shirt_size = 'XS',color = 'off white' WHERE color = 'white';


-- 	7.last_worn 이 200일인 셔츠 모두 삭제
DELETE FROM shirts WHERE last_worn=200;

-- 	8.모든 tank_top 삭제
DELETE FROM shirts WHERE article = 'tank top';

-- 	9.모든 셔츠 삭제
DELETE FROM shirts;

-- 	10.셔츠 테이블 삭제
DROP  TABLE shirts;
