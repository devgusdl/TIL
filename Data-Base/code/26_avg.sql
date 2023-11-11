-- 26_avg.sql

-- GROUP BY 없이
SELECT AVG(pages) FROM books;

-- GROUP BY 
SELECT
	author_fname,
    author_lname,
    AVG(pages),
    SUM(pages) / COUNT(*)
FROM books
GROUP BY author_fname, author_lname;