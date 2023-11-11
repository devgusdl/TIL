-- practice02.sql

-- 1. practice db 사용
USE practice;

-- 2. 테이블 people 생성
-- 3. fitst_name VARCHAR(20)
-- 4. last_name VARCHAR(20)
-- 5. age INT
CREATE TABLE people(
	first_name VARCHAR(20),
	last_name VARCHAR(20),
    age INT
    );
    
-- 6. 테이블 확인
DESC people;

-- 7. 데이터 입력
INSERT INTO people (last_name, first_name, age)
VALUES
	('김','현',26),
    ('김','루이',6),
    ('김','벼리',2);

-- 8. people 테이블의 모든 데이터 조회
SELECT * FROM people;
