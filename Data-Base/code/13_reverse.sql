-- 13_reverse.sql
-- 문자열 반대로 변경
SELECT REVERSE('apple');

-- 문자열 대칭으로 변경
SELECT CONCAT(author_fname, REVERSE(author_fname)) AS strange_name
FROM books;