-- 00_show_create_db.sql
-- SQL 고정 명령어는 대문자로, 내가 짓는 이름은 소문자로, (소문자도 가능하나 대문자가 권장)
-- 반드시 새미콜론 ';'으로 끝나기, 끝나지 않으면 실행되지 않음. (workbrench 제외)
-- 띄어쓰기와 줄 바꿈은 적절하게. DB는 신경 쓰지 않음
-- 주석은 '--'
-- 컬럼명은 여러 단어일 경우 따옴표로 감쌈. 한 단어일 경우 안 감싸도 됨
-- 값은 문자열일 경우 따옴표로 감싼다.
-- 문자열 속 따옴표는 이스케이프 문자열 ('\')로 사용한다.

-- 모든 데이터베이스 목록 보여주기.
-- SHOW DATABASES;

-- 테스트 만들기
-- CREATE DATABASE test;

-- 테스트 지우기 
DROP DATABASE petshop;

-- 데이터베이스 생성
CREATE DATABASE petshop;

-- 터미널에서 ~쓰기 
USE pet_shop;