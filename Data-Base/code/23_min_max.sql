-- 23_min_max.sql

-- GROUP BY 없이 사용
SELECT MIN(released_year) FROM books;
SELECT MAX(pages) FROM books;
SELECT MIN(author_lname), MAX(author_lname) FROM books;

-- GROUP BY 함께 사용
-- 작가별 출판한 책 수, 가장 오래된 책 출판 년도, 가장 최근 책 출판년도
SELECT  -- 그루핑 했을 때 조회 가능한 것: 1) aggregate / 2) grouped col
	author_lname AS '성',
    author_fname AS '이름',
    COUNT(title) AS '책 수',
	MIN(released_year) AS '최고',
    MAX(released_year) AS '최신'
FROM books
GROUP BY author_lname, author_fname;