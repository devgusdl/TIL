-- practice08.sql

-- 1 제목에 stories가 들어간 모든 책들의 제목 조회
SELECT title FROM books WHERE title LIKE '%stories%';

-- 2 가장 페이지가 많은 책의 제목과 페이지 수 조회 limit사용
SELECT title, pages FROM books 
ORDER BY pages DESC LIMIT 1;

-- 3 가장 최근에 발매된 책 3권을 제목=발매년도 로 구성하여 조회 a. 별칭 summary
SELECT CONCAT(title, '-', released_year) AS summary 
FROM books ORDER BY released_year DESC LIMIT 3;

-- 4 성에 공백''가 포함된 책의 제목과 작가 성만 조회
SELECT title, author_lname FROM books 
WHERE author_lname LIKE '% %';

-- 5 가장 재고가 작은 책 3개의 제목, 출판년도, 재고 조회
SELECT title, released_year, stock_quantity FROM books
ORDER BY stock_quantity LIMIT 3;

-- 6 책의 제목과 작가의 성을 성 =>제목 순서로 오름차순 정렬하여 조회
SELECT title, author_lname FROM books 
ORDER BY author_lname, title;

-- 7 작가의 이름과 성을 합쳐서 a-z순으로 중복없이 대문자로 한명씩 외치기 . 별칭shoutout
SELECT 
	DISTINCT UPPER(
		CONCAT(author_fname, ' ', author_lname, '!!!') 
	) AS shoutout 
FROM books ORDER BY shoutout;