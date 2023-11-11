-- 16_etc_functions.sql

-- 문자열에 삽입하기  (문자열, 시작점, 뒤에 잡아먹는수, 삽입문자)
SELECT INSERT('Hello justin', 6, 0, ' There');
SELECT INSERT('Hello justin', 6, 3, ' There');

-- 글자뽑기(substr과 같은 효과)
SELECT LEFT('omglol!', 3);
SELECT RIGHT('omglol!', 4);

SELECT LEFT(author_lname, 1) FROM books;
SELECT SUBSTR(author_lname, 1, 1) FROM books;

-- 반복하기
SELECT REPEAT('ha', 5);

-- 공백 없애기
SELECT TRIM('     wow     ');