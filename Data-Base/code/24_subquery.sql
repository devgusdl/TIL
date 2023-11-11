-- 24_subquery.sql

-- 가장 페이지가 긴 책의 제목

-- Error: aggregated - non aggregated 는 함께 조회 불가능
SELECT MAX(pages), title FROM books;

-- 가장 긴 책이 여러권일 경우 정확하지 않음
SELECT title, pages FROM books 
ORDER BY pages DESC LIMIT 1;

-- 2줄 쿼리
SELECT MAX(pages) FROM books;
SELECT title, pages FROM books WHERE pages=634;

-- 1줄로(쿼리안에 쿼리를 넣음)
SELECT title, pages FROM books 
WHERE pages = (SELECT MAX(pages) FROM books);

-- 가장 오래된 책은?
SELECT title, released_year FROM books
WHERE released_year = (SELECT MIN(released_year) FROM books);
