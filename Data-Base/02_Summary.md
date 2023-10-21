# SQL CRUD
## SQL 특징
- MySQL에서 데이터베이스에 대한 작업 명령은 SQL 구문을 이용하여 처리됩니다. 

> SELECT * FROM Reservation;
- SQL 고정 명령어는 대문자로, 내가 짓는 이름은 소문자로, (소문자도 가능하나 대문자가 권장)
```
1. SELECT * FROM Reservation;

2. select * from Reservation;

3. SeLeCt * FrOm Reservation;
```
- 반드시 새미콜론 ';'으로 끝나기, 끝나지 않으면 실행되지 않음. (workbrench 제외)
- 띄어쓰기와 줄 바꿈은 적절하게. DB는 신경 쓰지 않음
- 주석은 '--'
```
1. # 한 줄 주석
2. -- 한 줄 주석
3. /* 두 줄
   이상의
   주석 */
```
- 컬럼명은 여러 단어일 경우 따옴표로 감쌈. 한 단어일 경우 안 감싸도 됨
- 값은 문자열일 경우 따옴표로 감싼다.
- 문자열 속 따옴표는 이스케이프 문자열 ('\')로 사용한다.

## Create
MySQL에서는 CREATE 문을 사용하여 데이터베이스와 테이블을 만들 수 있다.
- DataBase
```python
# 모든 데이터베이스 목록 표시
SHOW DATABASES;

# 데이터베이스 지우기 
DROP DATABASE [DB명];

# 데이터베이스 생성
> CREATE DATABASE [DB명];

# DB사용 
USE [DB명];
```
- Table 
```python
# 테이블 생성
CREATE TABLE people(
	first_name VARCHAR(20),
	last_name VARCHAR(20),
    age INT
);

# 테이블 정보 확인(Describe)
DESC people;

# 현재 테이블에있는것들을 확인
SHOW TABLES;

# 테이블 삭제
DROP TABLE people;

# -- * = 모든 컬럼 확인
SELECT * FROM dogs1;
```
## Insert
INSERT INTO 문과 함께 VALUES 절을 사용하여 해당 테이블에 새로운 레코드를 추가 가능
```python
# 기본문법
INSERT INTO <table>(<col1>,<col2>)
> VALUES(<val>,<val2>);

# 예시
INSERT INTO dogs1 (name, breed, age)
VALUES
	('짱구', '요크셔', 5),
    ('소리', '포메',3),
    ('가을','치와와',10);
```

## Read
```python
# 기본 문법
SELECT * FROM cats;
SELECT name FROM cats;

# 예시
SELECT age, breed From cats;

# 특정조건이 있을때
SELECT * FROM cats WHERE age=4;
SELECT name FROM cats WHERE age=4;
SELECT age breed FROM cats WHERE age=4;

# AS 구문 활용법(변경)
SELECT name AS '이름' FROM cats;
SELECT name AS '이름', breed AS '종' FROM cats;
```

## Update
```python
# 기본 문법
UPDATE <table> SET <col>=<val> WHERE <condition>; 

SELECT * FROM cats;

# 예시
UPDATE cats SET age=100 WHERE name = 'Misty';

UPDATE cats SET age=age+1 WHERE name = 'Jackson';
```

## Delete
```python
# 기본 문법
DELETE FROM <table> WHERE <condition>;

# 예시
DELETE FROM cats WHERE name='Misty';
```
만약 WHERE 절을 생략하면, 해당 테이블에 저장된 모든 데이터가 삭제됩니다.
> DELETE FROM 테이블이름;

## 제약 조건(constraint)
데이터의 무결성을 지키기 위해, 데이터를 입력받을 때 실행되는 검사 규칙

이러한 제약 조건은 CREATE 문으로 테이블을 생성할 때나 ALTER 문으로 필드를 추가할 때도 설정 가능


MySQL에서 사용할 수 있는 제약 조건은 다음과 같습니다.

1. `NOT NULL`

- NULL : NULL 값 혀용
  - 해당 컬럼이 필수 값이 아닌 경우 사용
- NOT NULL : NULL 값 허용 X
  - 해당 컬럼이 필수 값인 경우 사용
- 기본적으로 NULL/NoT NULL 제약조건 생략시 NULL 로 인식한다.
```
CREATE TABLE dogs2(
name VARCHAR(20) NOT NULL, 
age INT NOT NULL
);
```

2. `PRIMARY KEY`
```
INSERT INTO dogs4()
VALUES (), (), (), ();

SELECT * FROM dogs4;

CREATE TABLE dogs5(
	id INT NOT NULL PRIMARY KEY,
    name VARCHAR(20) NOT NULL DEFAULT '멍멍이',
    age INT NOT NULL DEFAULT '0'
);

```
id 자동 순서대로 추가기능
```
id 자동 순서대로 추가
CREATE TABLE uniq_dogs(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL DEFAULT '멍멍이',
    age INT NOT NULL DEFAULT '0'
);
```

3. `DEFAULT`

기본값 제약조건 : 기본값 정의는 값을 입력하지 않았을경우 "자동으로 입력될 기본값을 미리 지정해 놓는 것"

```
CREATE TABLE dogs3 (
	name VARCHAR(20) DEFAULT 'No name',
    age INT DEFAULT 0
);
```