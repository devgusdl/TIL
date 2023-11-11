-- 01_table.sql

CREATE TABLE cats (
    name VARCHAR(50),
    age INT
);
-- 현재 테이블에있는것들을 보여줘
SHOW TABLES;
-- ~에관한 내용을 보여줘(describe)
DESC cats;
-- 삭제하기
DROP TABLE cats;

CREATE TABLE dogs1(
	name VARCHAR(50),
	breed VARCHAR(50),
	 age INT
);

DESC dogs1;