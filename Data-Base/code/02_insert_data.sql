-- 02_insert_data.sql

USE pet_shop;

-- INSERT INTO <table>(<col1>,<col2>)
-- VALUES(<val>,<val2>);

INSERT INTO dogs1 (name, breed, age)
VALUES ('맥스', '말티즈', 4);

-- * = 모든 컬럼
SELECT * FROM dogs1;

INSERT INTO dogs1 (name, breed, age)
VALUES
	('짱구', '요크셔', 5),
    ('소리', '포메',3),
    ('가을','치와와',10);
    
SELECT * FROM dogs1;