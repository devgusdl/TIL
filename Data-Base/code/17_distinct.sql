-- 17_distinct.sql (uniq)
-- 중복되지 않은 이름을 보고싶을 때
SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;

SELECT released_year FROM books;
SELECT DISTINCT released_year FROM books;

-- 풀 네임에서 중복을 없이 보려면
SELECT DISTINCT CONCAT(author_fname, ' ', author_lname) AS full_name 
FROM books;

SELECT DISTINCT author_fname, author_lname FROM books;
-- 3 컬럼이 모두 중복되는 경우가 없으므로 전체 레코드가 조회됨
SELECT DISTINCT author_fname, author_lname, released_year FROM books;