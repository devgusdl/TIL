-- 20_like.sql

-- 완전히 조건과 동일
SELECT * FROM books WHERE author_fname='Dave';

-- 패턴 탐색
-- % : 0~N 개 뭐라도 올 수 있는 와일드카드
-- _ : 정확히 한 글자만 올 수 있는 와일드카드

-- 이름에 'da' 가 들어감
SELECT * FROM books WHERE author_fname LIKE '%da%';
-- 'da' 로 시작하는 이름
SELECT * FROM books WHERE author_fname LIKE 'da%';
-- 'da' 로 끝나는 이름
SELECT * FROM books WHERE author_fname LIKE '%da';
-- 책 제목이 ':' 이 있는 책
SELECT * FROM books WHERE title LIKE '%:%';

-- 이름이 'da' 뒤에 정확히 두글자
SELECT * FROM books WHERE author_fname LIKE 'da__';
-- 이름이 정확히 4글자인 경우
SELECT * FROM books WHERE author_fname LIKE '____';
SELECT DISTINCT author_fname FROM books WHERE author_fname LIKE '____';

-- Escape) 책 제목에 '10%' 가 들어가는 책 (10\% 역슬레시)
SELECT * FROM books WHERE title LIKE '%10\%%';

