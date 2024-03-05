# 데이터 변경을 위한 SQL문(INSERT, UPDATE, DELETE)
## INSERT 기본 문법
- INSERT INTO 테이블[(열1,열2,...)] VALUES (값1, 값2 ...)

```python
USE market_db;
CREATE TABLE hongong1 (toy_id  INT, toy_name CHAR(4), age INT);
INSERT INTO hongong1 VALUES (1, '우디', 25);  # 값 입력 

INSERT INTO hongong1(toy_id, toy_name) VALUES (2, '버즈'); # 열 지정

INSERT INTO hongong1(toy_name,age, toy_id) VALUES ('제시', 20, 3);

CREATE TABLE hongong2 ( 
   toy_id  INT AUTO_INCREMENT PRIMARY KEY, 
   toy_name CHAR(4), 
   age INT); # AUTO_INCREMENT 자동 입력 할대(PRIMARY KEY 필수)

INSERT INTO hongong2 VALUES (NULL, '보핍', 25);
INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES (NULL, '렉스', 21);
SELECT * FROM hongong2; # NULL값을 넣으면 자동으로 됌

SELECT LAST_INSERT_ID(); # 어디까지 입력됐는지 확인 

ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL, '재남', 35);
SELECT * FROM hongong2; # 마지막 값을 100으로 

CREATE TABLE hongong3 ( 
   toy_id  INT AUTO_INCREMENT PRIMARY KEY, 
   toy_name CHAR(4), 
   age INT);
ALTER TABLE hongong3 AUTO_INCREMENT=1000; # 시작 값을 1000으로 
SET @@auto_increment_increment=3; # 3씩 늘어나게하기 1000 -> 1003 -> 1006
```
## INSERT INTO ~ SELECT 문
- 기본 문법
```
INSERT INTO 테이블 이름(열 이름1, 열이름2, ...) 
    SELECT 문 ;
```
```PYTHON
INSERT INTO hongong3 VALUES (NULL, '토마스', 20);
INSERT INTO hongong3 VALUES (NULL, '제임스', 23);
INSERT INTO hongong3 VALUES (NULL, '고든', 25);
SELECT * FROM hongong3;

SELECT COUNT(*) FROM world.city;

DESC world.city; # 구성을 알려줌

SELECT * FROM world.city LIMIT 5; # 5개만 보기

CREATE TABLE city_popul ( city_name CHAR(35), population INT);

INSERT INTO city_popul
    SELECT Name, Population FROM world.city;
    
```
## UPDATE 기본 문법
- 형식
```
UPDATE 테이블 이름
    SET 열1 = 값1, 열2 = 값2, ...
    WHERE 조건 ;
```
    
```PYTHON
USE market_db;
UPDATE city_popul
    SET city_name = '서울'
    WHERE city_name = 'Seoul'; # 영문 서울을 한글 서울로 UPDATE
SELECT  * FROM city_popul WHERE  city_name = '서울'; 

UPDATE city_popul
    SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
SELECT  * FROM city_popul WHERE  city_name = '뉴욕';


UPDATE city_popul
    SET population = population / 10000 ;
SELECT * FROM city_popul LIMIT 5;
```
## DELETE 기본 문법
```PYTHON
DELETE FROM city_popul 
    WHERE city_name LIKE 'New%'; # NEW로 시작하는 것들은 지워라

DELETE FROM city_popul 
    WHERE city_name LIKE 'New%' 
    LIMIT 5;

CREATE TABLE big_table1 (SELECT * FROM world.city , sakila.country); 
CREATE TABLE big_table2 (SELECT * FROM world.city , sakila.country); 
CREATE TABLE big_table3 (SELECT * FROM world.city , sakila.country); 
SELECT COUNT(*) FROM big_table1;

DELETE FROM big_table1;
DROP TABLE big_table2;
TRUNCATE TABLE big_table3;


```