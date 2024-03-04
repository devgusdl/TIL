# SQL 기본 문법
```python
USE market_db; # DB 선택

SELECT * FROM member; 

SELECT * FROM market_db.member;

SELECT mem_name FROM member;

SELECT addr, debut_date, mem_name
	FROM member; # SELECT 뒤에 지정 가능

SELECT addr 주소, debut_date "데뷔 일자", mem_name 
	FROM member; # 별명 붙이기 
```

## 조건 붙이기
### 1. 지정 검색
```PYTHON

SELECT * FROM member WHERE mem_name = '블랙핑크';

SELECT * FROM member WHERE mem_number = 4; # 지정 검색

SELECT mem_id, mem_name 
	FROM member 
	WHERE height <= 162;  # 조건문 붙이기 162이하인 멤버 아이디와, 이름
```
### 2. AND, OR 구문
```PYTHON
SELECT mem_name, height, mem_number 
	FROM member 
	WHERE height >= 165 AND mem_number > 6; # AND 조건문

SELECT mem_name, height, mem_number 
	FROM member 
	WHERE height >= 165 OR mem_number > 6; # OR 조건문

SELECT mem_name, height 
	FROM member 
	WHERE height >= 163 AND height <= 165;  

SELECT mem_name, height 
   FROM member 
   WHERE height BETWEEN 163 AND 165;  # BETWEEN, AND 로 변경 가능
   
SELECT mem_name, addr 
   FROM member 
   WHERE addr = '경기' OR addr = '전남' OR addr = '경남';  
   
SELECT mem_name, addr 
   FROM member 
   WHERE addr IN('경기', '전남', '경남'); # IN()로 하면 OR 과 같은 의미
```
### 3. 검색 방법
```PYTHON
SELECT * 
   FROM member 
   WHERE mem_name LIKE '우%'; # 우% = 우로 시작하는 멤버 

SELECT * 
   FROM member 
   WHERE mem_name LIKE '__핑크'; # 어떤 어떤 핑크라고 끝나는 멤버

# 심화 검색
SELECT height FROM member WHERE mem_name = '에이핑크';

SELECT mem_name, height FROM member WHERE height > 164;

SELECT mem_name, height FROM member
	WHERE height > (SELECT height FROM member WHERE mem_name = '에이핑크');

```