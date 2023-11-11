-- 05_primary.sql

INSERT INTO dogs4()
VALUES (), (), (), ();

SELECT * FROM dogs4;

CREATE TABLE dogs5(
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL DEFAULT '멍멍이',
    age INT NOT NULL DEFAULT '0'
);

INSERT INTO dogs5 (id, name, age)
VALUES
	(1, '골드', 3),
    (2, '실버', 3);
    
SELECT * FROM dogs5;

INSERT INTO dogs5(id, name, age)
VALUES(100, '브론즈', 3);


-- id 자동 순서대로 추가
CREATE TABLE uniq_dogs(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL DEFAULT '멍멍이',
    age INT NOT NULL DEFAULT '0'
);

INSERT INTO uniq_dogs (name, age)
VALUES
	('골드', 3),
    ('실버', 4),
    ('브론즈', 5);

SELECT * FROM uniq_dogs;


INSERT INTO uniq_dogs ()
VALUES (), (), (), ();