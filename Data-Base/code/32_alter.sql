-- 32_alter.sql

-- Add Column
ALTER TABLE companies 
ADD COLUMN phone VARCHAR(15);

-- 논리적 오류 (
ALTER TABLE companies
ADD COLUMN employee_count INT NOT NULL;

ALTER TABLE companies
ADD COLUMN income INT NOT NULL DEFAULT 1; -- default 값을 줘야함 안그러면 0으로 표시됌


-- Delete Column
ALTER TABLE companies
DROP COLUMN phone;

-- Rename Table
RENAME TABLE companies TO suppliers;
ALTER TABLE suppliers RENAME TO companies;

-- Rename Column
ALTER TABLE companies
RENAME COLUMN name TO company_name;

-- Update Column
ALTER TABLE companies
MODIFY company_name VARCHAR(100) DEFAULT '???';

-- Rename & Update Column
ALTER TABLE companies
CHANGE company_name name VARCHAR(255) DEFAULT '???' NOT NULL;

-- Update Constraints
ALTER TABLE houses
ADD CONSTRAINT positive_buy_price CHECK (buy_price >= 0);

ALTER TABLE houses DROP CONSTRAINT positive_buy_price;





