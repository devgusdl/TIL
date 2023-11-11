-- 11_substr.sql

-- SELECT SUBSTR(<str>, <start>, <length>) ' 문자열, 시작점, 길이
-- SELECT SUBSTR(<str>, <start>)

SELECT SUBSTR('HELLO, WORLD', 1, 4);
SELECT SUBSTR('HELLO, WORLD', 2, 4);

SELECT SUBSTR('HELLO, WORLD', 8);
SELECT SUBSTR('HELLO, WORLD', -5);
SELECT SUBSTR('HELLO, WORLD', -5, 2);

-- concat이랑 같이 쓰기
SELECT CONCAT(SUBSTR(title, 1, 10), '...') FROM books;
SELECT CONCAT(SUBSTR(author_lname, 1, 1), '. ', author_fname) FROM books;

-- 이름 short title 및 성 이니셜 + 이름 으로 변경
SELECT CONCAT(SUBSTR(title, 1, 10), '...') AS 'short title',
	   CONCAT(SUBSTR(author_lname, 1, 1), '. ', author_fname) AS 'name'
FROM books;