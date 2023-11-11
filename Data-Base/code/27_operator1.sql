-- 27_operator1.sql
SELECT 1 + 1;
SELECT 3 - 2;
SELECT 10 * 3;
SELECT 5 / 2;
SELECT 5 % 2;
-- 몫
SELECT 5 DIV 2;
-- 제곱
SELECT POW(2, 3);

-- IS NULL
SELECT * FROM books WHERE title = NULL; -- 작동안함
SELECT * FROM books WHERE title IS NULL; 
DELETE FROM books WHERE title IS NULL;


-- 홀수년도에 출판된 책
SELECT title, released_year FROM books
WHERE released_year % 2 = 1;

-- !=
SELECT * FROM books WHERE released_year = 2017;
SELECT * FROM books WHERE released_year != 2017;

SELECT * FROM books WHERE author_lname = 'Gaiman';
SELECT * FROM books WHERE author_lname != 'Gaiman';

-- NOT LIKE
SELECT * FROM books WHERE title LIKE '%e%';
SELECT * FROM books WHERE title NOT LIKE '%e%';

-- >, < (GT, LT)
SELECT * FROM books WHERE released_year > 2005;
SELECT * FROM books WHERE pages < 500;

-- >=, <= (GTE, LTE)
SELECT * FROM books WHERE pages > 634;
SELECT * FROM books WHERE pages >= 634;
SELECT * FROM books WHERE released_year <= 1985;


