-- 10_concat.sql
-- concat 함수 : 문자열 데이터 이어서 붙이기
SELECT CONCAT('s', 'q', 'l');

SELECT CONCAT(author_fname, '!!!') FROM books;

-- 전체이름으로 바꿔주기
SELECT CONCAT(author_fname,' ', author_lname) FROM books;

-- 이름 full_name으로 변경
SELECT CONCAT(author_fname,' ', author_lname) AS full_name FROM books

-- 문자열 사이에 구분자 넣기
SELECT CONCAT('!', 's', 'q', 'l');
SELECT CONCAT_WS('!', 's', 'q', 'l');

SELECT CONCAT_WS('-', title, author_fname, author_lname) AS summary FROM books;