-- 18_order_by.sql

SELECT id, author_fname, author_lname FROM books;

SELECT id, author_fname, author_lname 
FROM books ORDER BY author_fname;

-- 기본값(오름차순)
SELECT id, author_fname, author_lname 
FROM books ORDER BY author_fname ASC;
-- 내림차순
SELECT id, author_fname, author_lname 
FROM books ORDER BY author_fname DESC;

SELECT * FROM books ORDER BY stock_quantity;
SELECT * FROM books ORDER BY stock_quantity DESC;

-- ORDER BY 기준이 되는 컬럼을 숫자로 지정(비추)
SELECT id, author_fname, author_lname 
FROM books ORDER BY 2 DESC;

-- 여러 컬럼으로 정렬(컬럼 우선순위 있음)
SELECT author_lname, released_year, title FROM books 
ORDER BY author_lname, released_year;

SELECT author_lname, released_year, title FROM books 
ORDER BY released_year, author_lname;

SELECT author_lname, released_year, title FROM books 
ORDER BY author_lname, released_year DESC;

SELECT author_lname, released_year, title FROM books 
ORDER BY author_lname DESC, released_year DESC;

-- 가상의 컬럼으로도 정렬 가능
SELECT id, CONCAT(author_fname, ' ', author_lname) AS author 
FROM books ORDER BY author;