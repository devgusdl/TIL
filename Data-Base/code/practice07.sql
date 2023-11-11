-- practice07.sql

-- 1 책 제목의 공백을 ->로 바꿔서 출력 별칭title
SELECT REPLACE(title, ' ', '->') AS title FROM books;

-- 2 작가의 성(lname)을 제대로/거꾸로 출력 별칭 forwards/backwards
SELECT author_lname AS forwards, REVERSE(author_lname) AS backwards
FROM books;

-- 3 풀네임(fname-lname)을 모두 대문자로 출력 별칭 full name in caps
SELECT UPPER(CONCAT(author_fname, ' ', author_lname)) AS 'full name in caps' 
FROM books;

SELECT UPPER(CONCAT_WS(' ', author_fname, author_lname)) AS 'full name in caps' 
FROM books;

-- 4 책 제목과 출간 연도를 조합하여 문장으로 출력 , 별칭 summary
SELECT CONCAT(title, ' was released in ', released_year) AS summary 
FROM books;

-- 5 책 제목과 제목 글자수를 출력 ,별칭 title, character count
SELECT title, CHAR_LENGTH(title) AS 'character count' 
FROM books;

-- 6 3개의 컬럼 a. 짧은제목(제목앞 10글자와 뒤에 ...으로 구성) 별칭은 short title
-- b. 작가 이름을 성, 이름으로 구성, 별칭은 author
-- c. 재고를 12 in stock 과 같은 문장으로 구성. 별칭은 quantity
SELECT 
	CONCAT(SUBSTR(title, 1, 10), '...') AS 'short title', 
    CONCAT(author_lname, ',', author_fname) AS 'author', 
    CONCAT(stock_quantity, ' in stock') AS 'quantity' 
FROM books;