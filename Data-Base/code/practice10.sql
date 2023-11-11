-- practice10.sql

-- 1. 1980년 이전(미만)에 출간된 모든 책의 수   
SELECT COUNT(*) FROM books WHERE released_year < 1980;

-- 2 작가 성이 eggers 이거나 chabon인 모든 책 조회
SELECT * FROM books WHERE author_lname IN ('Eggers', 'Chabon');

-- 3 작가 성이 lahiri가 2000년 이후 출간한 모든 책 조회
SELECT * FROM books WHERE author_lname = 'Lahiri' AND released_year > 2000;

-- 4 책 페이지가 100이상 200이하인 모든 책의 제목,페이지 수 조회
SELECT title, pages FROM books WHERE pages BETWEEN 100 AND 200;

-- 5 작가의 성이 c나 s로 시작하는 작가의 모든 책의 제목과 성 조회
SELECT title, author_lname FROM books 
WHERE author_lname LIKE 'C%'
OR author_lname LIKE 'S%';

-- 6 3개 컬럼
-- a. title: 제목
-- b. stock_quantity 재고 수
-- c. type 다음 조건에 따라 결정
-- 1. 제목에 stories가 들어가면 type a 
-- 2. 제목에 kids나 heartbreaking이 들어가면 type B
-- 3. 그 외에는 모두 type c
SELECT
	title,
    stock_quantity,
    CASE
		WHEN title LIKE '%stories%' THEN 'A'
        WHEN title LIKE '%kids%' OR title LIKE '%heartbreaking%' THEN 'B'
        ELSE 'C'
    END AS 'type'
FROM books;
