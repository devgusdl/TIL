-- 31_check.sql

CREATE TABLE users1 (
	username VARCHAR(20) NOT NULL UNIQUE,
    age INT CHECK (age > 0) NOT NULL
);


INSERT INTO users1(username, age) VALUES('김철수', 0);
INSERT INTO users1(username, age) VALUES('김철수', 2);

CREATE TABLE palindrome1 (
	word VARCHAR(100) CHECK(word = REVERSE(word))
);

INSERT INTO palindrome1 (word) VALUES ('apple');
INSERT INTO palindrome1 (word) VALUES ('assa');

-- Name Constraints
CREATE TABLE users2(
	username VARCHAR(20) NOT NULL UNIQUE,
    age INT NOT NULL,
    CONSTRAINT age_must_be_positive CHECK (age >= 0)
);

INSERT INTO users2(username, age) VALUES('김철수', -1);

CREATE TABLE palindrome2 (
  word VARCHAR(100) NOT NULL,
  CONSTRAINT word_must_be_palindrome CHECK(REVERSE(word) = word)
);

INSERT INTO palindrome2(word) VALUES ('agge');

-- multi columns constraint
CREATE TABLE companies (
	name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    CONSTRAINT name_and_address_cannot_be_same UNIQUE (name, address)
);
-- name, address 조합이 같은건 불가능
INSERT INTO companies(name, address)
VALUES ('apple inc', 'cupertino, CA');

INSERT INTO companies(name, address)
VALUES ('banana inc', 'cupertino, CA');

INSERT INTO companies(name, address)
VALUES ('apple inc', 'seoul, KR');


CREATE TABLE houses (
	buy_price INT NOT NULL,
    sell_price INT NOT NULL,
    CONSTRAINT sell_gte_buy CHECK(sell_price >= buy_price)
);

INSERT INTO houses (buy_price, sell_price)
VALUES(10, 20);
-- ERROR
INSERT INTO houses (buy_price, sell_price)
VALUES(20, 10);











