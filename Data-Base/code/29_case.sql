-- 29_case.sql

-- 2000년 이후에 출간된 책은 현대문학
-- 2000년 이전에 출간된 책은 고전문학
SELECT title, released_year, 
	CASE 
		WHEN released_year >= 2000 THEN '현대 문학'
        ELSE '고전 문학'
    END AS genre
FROM books;


SELECT title, stock_quantity, 
	CASE 
		WHEN stock_quantity BETWEEN 0 AND 40 THEN '*'
        WHEN stock_quantity BETWEEN 41 AND 70 THEN '**'
        WHEN stock_quantity BETWEEN 71 AND 100 THEN '***'
        WHEN stock_quantity BETWEEN 101 AND 140 THEN '****'
		ELSE '*****'
    END AS stars
FROM books;


SELECT title, stock_quantity, 
	CASE 
		WHEN stock_quantity < 40 THEN '*'
        WHEN stock_quantity < 70 THEN '**'
        WHEN stock_quantity < 100 THEN '***'
        WHEN stock_quantity < 140 THEN '****'
		ELSE '*****'
    END AS stars
FROM books;
