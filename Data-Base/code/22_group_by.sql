-- 22_group_by.sql

SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;
SELECT author_lname FROM books GROUP BY author_lname;

SELECT author_lname, COUNT(title) FROM books GROUP BY author_lname;

-- 작가 last_name 별 책이 많은 순
SELECT author_lname, COUNT(title) AS counter
FROM books GROUP BY author_lname
ORDER BY counter DESC;

SELECT author_lname, author_fname, COUNT(*) FROM books 
GROUP BY author_lname, author_fname;

-- 가상의 그룹 만들기
SELECT  
	CONCAT(author_lname, ' ', author_fname) AS fullname, 
    COUNT(*) 
FROM books 
GROUP BY fullname;
