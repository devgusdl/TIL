# SQL 고급 문법
## 두 테이블을 묶는 조인
### 일대다 관계
```python
SELECT <열 목록>
FROM <첫 번쨰 테이블>
    INNER JOIN <두 번째 테이블>
    ON < 조인될 조건>
[WHERE 검색 조건] 
```
```PYTHON
USE market_db;
SELECT * 
   FROM buy
     INNER JOIN member
     ON buy.mem_id = member.mem_id # 조건
   WHERE buy.mem_id = 'GRL'; 

SELECT * 
   FROM buy
     INNER JOIN member
     ON buy.mem_id = member.mem_id;
     
SELECT mem_id, mem_name, prod_name, addr, CONCAT(phone1, phone2) AS '연락처' # 어느 테이블을 지정하는지 모름
   FROM buy
     INNER JOIN member
     ON buy.mem_id = member.mem_id;

SELECT buy.mem_id, mem_name, prod_name, addr, CONCAT(phone1, phone2) AS '연락처' # 앞에 buy를 씀으로써 어느 테이블을 지정하는건지 알 수 있음
   FROM buy
     INNER JOIN member
     ON buy.mem_id = member.mem_id;

```
## 외부조인
```
SELECT <열 목록>
FROM < 첫번째 테이블 (LEFT 테이블)>
    <LEFT : RIGHT : FULL> OUTER JOIN < 두번째 테이블 (RIGHT 테이블)>
    ON< 조인될 조건>
[WHERE 검색 조건];
```
```python
SELECT B.mem_id, M.mem_name, B.prod_name, M.addr,  # 하나하나 쓸 수 있지만 너무 코드가 길어짐
        CONCAT(M.phone1, M.phone2) AS '연락처' 
   FROM buy B
     INNER JOIN member M # 별명 지정
     ON B.mem_id = M.mem_id;
          
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr 
   FROM buy B
     INNER JOIN member M
     ON B.mem_id = M.mem_id
   ORDER BY M.mem_id;

SELECT DISTINCT M.mem_id, M.mem_name, M.addr
   FROM buy B
     INNER JOIN member M
     ON B.mem_id = M.mem_id
   ORDER BY M.mem_id;
   
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
   FROM member M
     LEFT OUTER JOIN buy B # LEFT
     ON M.mem_id = B.mem_id
   ORDER BY M.mem_id;

SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
   FROM buy B
     RIGHT OUTER JOIN member M # RIGHT / 테이블의 위치만 바뀐것
     ON M.mem_id = B.mem_id
   ORDER BY M.mem_id;
   
SELECT DISTINCT M.mem_id, B.prod_name, M.mem_name, M.addr
   FROM member M
     LEFT OUTER JOIN buy B
     ON M.mem_id = B.mem_id
   WHERE B.prod_name IS NULL
   ORDER BY M.mem_id;

```

## 기타 조인
상호조인 : 전체 다 조인해서 데이터가 많아짐
```PYTHON
SELECT * 
   FROM buy 
     CROSS JOIN member ;

SELECT COUNT(*) "데이터 개수" # 대용량의 데이터를 만들수있음 
   FROM sakila.inventory
      CROSS JOIN world.city;

SELECT COUNT(*) "데이터 개수"
   FROM sakila.inventory
      CROSS JOIN world.city;

CREATE TABLE cross_table
    SELECT *
       FROM sakila.actor
          CROSS JOIN world.country;

SELECT * FROM cross_table LIMIT 5;
```
# 형식
```
SELECT<열 목록>
FROM < 테이블 >별칭A
    INNER JOIN < 테이블> 별칭 B
    ON<조인될 조건>
[WHERE 검색 조건]
```
```
USE market_db;
CREATE TABLE emp_table (emp CHAR(4), manager CHAR(4), phone VARCHAR(8));

INSERT INTO emp_table VALUES('대표', NULL, '0000');
INSERT INTO emp_table VALUES('영업이사', '대표', '1111');
INSERT INTO emp_table VALUES('관리이사', '대표', '2222');
INSERT INTO emp_table VALUES('정보이사', '대표', '3333');
INSERT INTO emp_table VALUES('영업과장', '영업이사', '1111-1');
INSERT INTO emp_table VALUES('경리부장', '관리이사', '2222-1');
INSERT INTO emp_table VALUES('인사부장', '관리이사', '2222-2');
INSERT INTO emp_table VALUES('개발팀장', '정보이사', '3333-1');
INSERT INTO emp_table VALUES('개발주임', '정보이사', '3333-1-1');

SELECT A.emp "직원" , B.emp "직속상관", B.phone "직속상관연락처"
   FROM emp_table A
      INNER JOIN emp_table B
         ON A.manager = B.emp
   WHERE A.emp = '경리부장';
```