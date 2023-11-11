-- 19_limit.sql
-- 개수 제한
SELECT * FROM books LIMIT 5;

SELECT * FROM books
ORDER BY stock_quantity DESC
LIMIT 5;

-- LIMIT 뒤에 숫자를 2개 쓰면, 앞의 개수, 개수
SELECT * FROM books LIMIT 0, 5;
SELECT * FROM books LIMIT 5, 5;
SELECT * FROM books LIMIT 10, 5;

-- LIMIT 은 종료지점이 부족하면 그냥 최대한 가져옴
SELECT * FROM books LIMIT 15, 5;
SELECT * FROM books LIMIT 1000000;
