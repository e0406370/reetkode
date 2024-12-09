/*
  LCE 196. Delete Duplicate Emails
  -> PostgreSQL

  Table: Person

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | email       | varchar |
  +-------------+---------+
  - id is the primary key (column with unique values) for this table.
  - Each row of this table contains an email. The emails will not contain uppercase letters.

  Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

  For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
  For Pandas users, please note that you are supposed to modify Person in place.

  After running your script, the answer shown is the Person table.
  The driver will first compile and run your piece of code and then show the Person table.
  The final order of the Person table does not matter.
*/

-- Method 1: subquery using rank() window function
DELETE FROM 
    Person
USING (
    SELECT id, rank() OVER (PARTITION BY email ORDER BY id ASC) AS rank
    FROM Person
) R
WHERE 
    Person.id = R.id 
AND 
    R.rank > 1;

-- Method 2: querying same table twice -> Cartesian Product
DELETE FROM 
    Person P1
USING 
    Person P2
WHERE
    P1.email = P2.email
AND
    P1.id > P2.id

-- M1 is faster than M2
  -- subquery R in M1 computes ranks in a single scan then joins with the main table Person
  -- nested iterations in M2 involves iterating through all rows in P2 for each row in P1

-- reference: 
  -- M1, M2: https://www.postgresql.org/docs/17/sql-delete.html
  -- M1: https://www.postgresql.org/docs/17/tutorial-window.html
