-- practice09.sql

-- 1. 테이블의 모든 책 수(재고아님)를 조회
SELECT COUNT(*) FROM books;

-- 2.각 년도별 오름차순으로 출판된 책 수(재고아님)조회
SELECT released_year, COUNT(*) 
FROM books GROUP BY released_year ORDER BY released_year;

-- 3.모든 책의 재고 수를 조회
SELECT SUM(stock_quantity) FROM books;

-- 4.각 작가(이름+성)의 발매 년도의 평균 조회
SELECT 
	author_fname,
    author_lname,
    AVG(released_year)
FROM books
GROUP BY author_fname, author_lname;

-- 5.가장 긴 책의 작가 풀네임(이름+성)과 페이지 조회(서브쿼리 활용)
SELECT 
	CONCAT(author_fname, ' ', author_lname) AS 'full name',
    pages
FROM books
WHERE pages = (SELECT MAX(pages) FROM books);

-- 6.컬럼 세개를 a.년도 year(기준으로 오름차순 정렬) b.년도별 책 수 books c.년도별 책의 평균 페이지 수 avg pages
SELECT
	released_year AS 'year',
    COUNT(*) AS '# books',
    AVG(pages) AS 'avg pages'
FROM books
GROUP BY released_year
ORDER BY released_year;
