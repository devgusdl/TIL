-- practice05.sql

SELECT * FROM cats;

-- 1.이름이 Jackson 인 고양이의 이름을 Jack 으로 바꾸기
UPDATE cats SET name='Jack' WHERE name = 'Jackson';

-- 2.Ringo 의 종을 ‘British Shorthair’ 로 바꾸기
UPDATE cats SET breed='British Shorthair' WHERE name = 'Ringo';

-- 3.종이 Maine Coon 인 고양이들의 나이를 12로 바꾸기
UPDATE cats SET age=12 WHERE breed = 'Maine Coon';

SELECT * FROM cats;
