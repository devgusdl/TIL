-- 12_replace.sql
-- 문자열에서 a를 b로 대체하기 ( 문자열, a, b)
SELECT REPLACE('HELLO WORLD', 'HELL', '****');
SELECT REPLACE('apple', 'p', 'P');

SELECT REPLACE(title, ' ', '-') AS 'new title' FROM books;

-- tip: 띄어쓰기가 있을때는 ''를 붙인다