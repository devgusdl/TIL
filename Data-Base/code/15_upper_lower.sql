-- 15_upper_lower.sql
-- 대문자, 소문자로 변경
SELECT UPPER('hello');
SELECT LOWER('WORLD');

SELECT UPPER(title) AS upper_title FROM books;
SELECT LOWER(title) AS upper_title FROM books;

-- 'I LOVE <BOOK_TITLE>!!!'
SELECT UPPER(CONCAT('i love ', title, '!!!')) FROM books;
SELECT CONCAT('I LOVE ', UPPER(title), '!!!') FROM books;