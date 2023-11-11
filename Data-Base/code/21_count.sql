-- 21_count.sql
-- books에 있는 기록들 개수 다 세기
SELECT COUNT(*) FROM books;
SELECT COUNT(id) FROM books;

-- 중복없이 개수 세기
SELECT COUNT(DISTINCT author_lname) FROM books;

SELECT COUNT(title) FROM books WHERE title LIKE '%the%';
SELECT COUNT(*) FROM books WHERE title LIKE '%the%';
-- Error (aggregated - non aggregated 는 동시에 조회 불과)
SELECT title, COUNT(*) FROM books WHERE title LIKE '%the%';