# 데이터의 형식(정수형, 문자형, 실수형, 날짜형)과 형 변환
## 정수형
- 정수형은 소수점이 없는 숫자. 즉 인원 수, 가격, 수량 등에 많이 사용한다. 
 - TINYINT : -128 ~ 127
 - SMALLINT : -32,768 ~ 32,767
 - INT : 약 -21억 ~ 21억
 - BIGINT : 약 -900경 ~ 900 경


```PYTHON
USE market_db;
CREATE TABLE hongong4 (
    tinyint_col  TINYINT,
    smallint_col SMALLINT,
    int_col    INT,
    bigint_col BIGINT );

INSERT INTO hongong4 VALUES(127, 32767, 2147483647, 9000000000000000000);

INSERT INTO hongong4 VALUES(128, 32768, 2147483648, 90000000000000000000); # 범위 초과

DROP TABLE IF EXISTS buy, member;
CREATE TABLE member # 회원 테이블
( mem_id      CHAR(8) NOT NULL PRIMARY KEY, #회원 아이디(PK)
  mem_name        VARCHAR(10) NOT NULL, # 이름
  mem_number    INT NOT NULL,  # 인원수
  addr          CHAR(2) NOT NULL, # 주소(경기,서울,경남 식으로 2글자만입력)
  phone1        CHAR(3), # 연락처의 국번(02, 031, 055 등)
  phone2        CHAR(8), # 연락처의 나머지 전화번호(하이픈제외)
  height        SMALLINT,  # 평균 키
  debut_date    DATE  # 데뷔 일자
);

DROP TABLE IF EXISTS member;
CREATE TABLE member # 회원 테이블
( mem_id      CHAR(8) NOT NULL PRIMARY KEY, # 회원 아이디(PK)
  mem_name        VARCHAR(10) NOT NULL, # 이름
  mem_number    TINYINT  NOT NULL,  # 인원수
  addr          CHAR(2) NOT NULL, # 주소(경기,서울,경남 식으로 2글자만입력)
  phone1        CHAR(3), # 연락처의 국번(02, 031, 055 등)
  phone2        CHAR(8), # 연락처의 나머지 전화번호(하이픈제외)
  height        TINYINT UNSIGNED,  # 평균 키
  debut_date    DATE  # 데뷔 일자
);

```
## 문자형
- CHAR(개수) : 
  - 1 ~ 255 고정형문자
  - 속도가 더 빠름
  - 글자크기가 고정된것은 char로 
- VARCHAR(개수): 
  - 1 ~ 16383 가변형문자
  - 공간이 효율적이다
  - 글자 크기가 다양한것은 varchar로
```python
DROP TABLE IF EXISTS member;
CREATE TABLE member # 회원 테이블
( mem_id      CHAR(8) NOT NULL PRIMARY KEY, # 회원 아이디(PK)
  mem_name        VARCHAR(10) NOT NULL, # 이름
  mem_number    TINYINT  NOT NULL,  # 인원수
  addr          CHAR(2) NOT NULL, # 주소(경기,서울,경남 식으로 2글자만입력)
  phone1        CHAR(3), # 연락처의 국번(02, 031, 055 등)
  phone2        CHAR(8), # 연락처의 나머지 전화번호(하이픈제외)
  height        TINYINT UNSIGNED,  # 평균 키
  debut_date    DATE  # 데뷔 일자
);

CREATE TABLE big_table (
  data1  CHAR(255), # 255까지 가능
  data2  VARCHAR(16384) ); # 16383까지 가능 

CREATE DATABASE netflix_db;
USE netflix_db;
CREATE TABLE movie 
  (movie_id        INT,
   movie_title     VARCHAR(30),
   movie_director  VARCHAR(20),
   movie_star      VARCHAR(20),
   movie_script    LONGTEXT, # 긴 글
   movie_film      LONGBLOB # 영화 파일
); 

```
## 실수형
- FLOAT : 소수점 아래 7자리까지 표현
- DOUBLE : 소수점 아래 15자리까지 표현

## 날짜형
- DATE : 날짜만 저장 YYYY-MM-DD 형식으로 사용
- TIME : 시간만 저장 HH:MM:SS 형식으로 사용
- DATETIME : 날짜 및 시간을 저장. YYYY-MM-DD HH:MM:SS 형식으로 사용

## 변수의  사용
- 문법
```PYTHON
SET @변수이름 = 변수의 값 ; # 변수의 선언 및 대입
SELECT @변수이름 ; # 변수의 값 출력
```

```python
USE market_db;
SET @myVar1 = 5 ;
SET @myVar2 = 4.25 ; # 임시로 변수 저장(영구 저장이 아님)

SELECT @myVar1 ;
SELECT @myVar1 + @myVar2 ; # 변수 출력

SET @txt = '가수 이름==> ' ;
SET @height = 166;
SELECT @txt , mem_name FROM member WHERE height > @height ;


SET @count = 3; # LIMIT에 변수를 사용하면 오류가 뜸
SELECT mem_name, height FROM member ORDER BY height LIMIT @count;

SET @count = 3; # 오류가 나기 때문에 사용하는것이 PREPARE, EXECUTE 이다
PREPARE mySQL FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?'; # 준비(?물음표를 쓰고 준비)
EXECUTE mySQL USING @count; # 실행(물음표에 대입)
```
## 데이터 형변환
- 명시적인 변환 CAST( 값 AS 데이터_형식 [ (길이) ] )
- 암시적인 변환 CONVERT( 값, 데이터_형식[ (길이) ] )
```PYTHON
SELECT AVG(price) '평균 가격' FROM buy;

SELECT CAST(AVG(price) AS SIGNED)  '평균 가격'  FROM buy ; # 부호가 있는 정수형으로 변환
-- 또는
SELECT CONVERT(AVG(price) , SIGNED)  '평균 가격'  FROM buy ; # 동일한 결과 

SELECT CAST('2022$12$12' AS DATE);
SELECT CAST('2022/12/12' AS DATE);
SELECT CAST('2022%12%12' AS DATE);
SELECT CAST('2022@12@12' AS DATE);

SELECT num, CONCAT(CAST(price AS CHAR), 'X', CAST(amount AS CHAR) ,'=' ) '가격X수량',
    price*amount '구매액' 
  FROM buy ;

SELECT '100' + '200' ; # 문자와 문자를 더함 (정수로 변환되서 연산됨)
SELECT CONCAT('100', '200'); # 문자와 문자를 연결 (문자로 처리)
SELECT CONCAT(100, '200'); # 정수와 문자를 연결 (정수가 문자로 변환되서 처리)
SELECT 1 > '2mega'; # 정수인 2로 변환되어서 비교
SELECT 3 > '2MEGA'; # 정수인 2로 변환되어서 비교
SELECT 0 = 'mega2'; # 문자는 0으로 변환됨

```