-- practice04.sql

USE pet_shop;

-- 1. 모든 고양이의 id 만 조회
SELECT id FROM cats;

-- 2. 모든 고양이의 이름과 종만 조회
SELECT name, bresed FROM cats;

-- 3. 종이 Tabby 인 고양이의 이름과 나이만 조회
SELECT name, age FROM cats WHERE breed = 'Tabby';

-- 4. id 와 나이가 같은 고양이의 id와 나이만 조회
SELECT id, age FROM cats WHERE age=id;

SELECT id AS '번호', age AS '나이'
FROM cats WHERE id=age;

