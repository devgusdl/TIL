# 인덱스
- 데이터를 조회할때 빠르게 조회되도록 도와주는 방법
- 인덱스 만드는 방법: CREATE INDEX idx_인덱스이름 ON 테이블명(컬럼명);
```python
SELECT * FROM member WHERE member_name = '아이유';

CREATE INDEX idx_member_name ON member(member_name);
```


# 뷰
- 가상의 테이블(실체가 없음)
- 바로가기 아이콘 같은 개념
- 뷰 만드는 방법
```python
CREATE VIEW member_view
AS
	SELECT * FROM member; # 테이블에 접근하는 쿼리문


SELECT * FROM member_view;
```
- 원리: 
  - 사용자 ->(뷰에 접근)  SELECT문 <->(내부적으로 연결됨)   테이블 
- 쓰는 이유 : 보안 문제

# 스토어드 프로시저
- 스토어드 프로시저는 MYSQL에서 프로그래밍 기능을 사용할 수 있도록 도와준다
- ex)python, java, c 처럼 프로그래밍 로직을 구현할 수 있음
- 스토어드 프로시저 만드는 방법
```python

DELIMITER //
CREATE PROCEDURE myProc() # 이름은 자유
BEGIN
	SELECT * FROM member WHERE member_name = '나훈아';
	SELECT * FROM member WHERE member_name = '아이유';
END //product
DELIMITER ; # 저장 프로세스를 묶어주는 약속


CALL myProc();  # 저장된 것을 부르는 코드

```
- begin과 end사이로 실행 범위를 지정할 수 있고 delimiter = 구분자 개념