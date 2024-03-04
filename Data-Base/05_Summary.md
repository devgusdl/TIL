# SELECT 절의 형식(ORDER BY 절과 GROUP BY 절)
## SELECT 절의 형식
```
SELECT 열_이름
    FROM 테이블_이름
    WHERE 조건식
    GROUP BY 열_이름
    HAVING 조건식
    ORDER BY 열_이름
    LIMIT 숫자
```
## ORDER BY 절
- ORDER BY 로 하면 오름차순 (낮은 순서대로)
  - ASC 는 생략 가능
- 뒤에 DESC 붙이면 내림차순 (높은 순서대로)
```python
SELECT mem_id, mem_name, debut_date 
   FROM member 
   ORDER BY debut_date; # ASC 생략 가능

SELECT mem_id, mem_name, debut_date 
   FROM member 
   ORDER BY debut_date DESC; # 내림차순
   
SELECT mem_id, mem_name, debut_date, height
   FROM member 
   ORDER BY height DESC
   WHERE height  >= 164;  # 오류 발생  왜?  WHERE과 ORDER의 순서가 바뀌어서 
   
SELECT mem_id, mem_name, debut_date, height
   FROM member 
   WHERE height  >= 164
   ORDER BY height DESC; # 올바른 순서

   
SELECT mem_id, mem_name, debut_date, height
   FROM member 
   WHERE height  >= 164
   ORDER BY height DESC, debut_date ASC; # 동률일때 키는 내림차순, 데뷔일자는 오름차순
```

## 행 지정 (얼만큼 보고싶은지 설정)
```PYTHON
SELECT *
   FROM member 
   LIMIT 3; # 3개만 보고싶다
   
SELECT mem_name, debut_date
   FROM member
   ORDER BY debut_date
   LIMIT 3;
   
SELECT mem_name, height
   FROM member
   ORDER BY height DESC
   LIMIT 3,2; # 3번째부터 두개행 (3등부터 2개)
```

## DISTINCT 문
```PYTHON 
   
SELECT addr FROM member;

SELECT addr FROM member ORDER BY addr;

SELECT DISTINCT addr FROM member; # 중복된건 삭제하고 하나만 보여줌

```

## GROUP BY 절
```PYTHON

SELECT mem_id, amount FROM buy ORDER BY mem_id;

SELECT mem_id, SUM(amount) FROM buy GROUP BY mem_id; # 아이디별로 그룹으로 묶어 합계를 계산하라

SELECT mem_id "회원 아이디", SUM(amount) "총 구매 개수"
   FROM buy GROUP BY mem_id; # 별칭을 줘서 깔끔하게


SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
   FROM buy GROUP BY mem_id; # 총 합계 계산
   
SELECT AVG(amount) "평균 구매 개수" FROM buy; # 전체에 대한 평균

SELECT mem_id, AVG(amount) "평균 구매 개수" 
	FROM buy
	GROUP BY mem_id; # 멤버별로 평균 계산
```
## COUNT (행의 개수 세기)
```PYTHON
SELECT COUNT(*) FROM member;

SELECT COUNT(phone1) "연락처가 있는 회원" FROM member;
```
# HAVING 절
```PYTHON
SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
   FROM buy 
   GROUP BY mem_id;

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
   FROM buy 
   WHERE SUM(price*amount) > 1000 
   GROUP BY mem_id;  # GROUP 함수는 WHERE을 쓸 수 없다!!!!

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
   FROM buy 
   GROUP BY mem_id   
   HAVING SUM(price*amount) > 1000 ; # HAVING절 사용하기

SELECT mem_id "회원 아이디", SUM(price*amount) "총 구매 금액"
   FROM buy 
   GROUP BY mem_id   
   HAVING SUM(price*amount) > 1000
   ORDER BY SUM(price*amount) DESC; # HAVING절 내림차순 # 심화
```