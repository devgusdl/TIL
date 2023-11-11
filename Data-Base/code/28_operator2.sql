-- 28_operator2.sql

-- AND
SELECT title, author_lname, released_year FROM books
WHERE released_year > 2010 AND author_lname = 'Eggers';

SELECT title, author_lname, released_year FROM books
WHERE
	released_year > 2010
    AND
    author_lname = 'Eggers'
    AND
    title LIKE '%novel%';
    
SELECT title, released_year FROM books
WHERE released_year >= 2000 AND released_year % 2 = 1;

-- OR
SELECT title, author_lname, released_year FROM books
WHERE released_year > 2010 OR author_lname = 'Eggers';

SELECT title, pages FROM books
WHERE pages < 200 OR title LIKE '%stories%';

-- BETWEEN
SELECT title, released_year FROM books
WHERE
	released_year >= 2004
    AND
    released_year <= 2015;
    
SELECT title, released_year FROM books
WHERE released_year BETWEEN 2004 AND 2014;

SELECT title, pages FROM books 
WHERE pages NOT BETWEEN 200 AND 300;
    
SELECT title, pages FROM books 
WHERE pages < 200 OR pages > 300;

-- IN
SELECT title, author_lname FROM books
WHERE author_lname = 'Carver' 
	OR author_lname = 'Lahiri'
	OR author_lname = 'Smith';

SELECT title, author_lname FROM books
WHERE author_lname IN ('Carver', 'Lahiri', 'Smith');

SELECT title, author_lname FROM books
WHERE author_lname NOT IN ('Carver', 'Lahiri', 'Smith');


