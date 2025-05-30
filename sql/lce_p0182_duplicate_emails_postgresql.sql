/*
  LCE 182. Duplicate Emails
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

  Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
  
  Return the result table in any order.
*/

SELECT email AS EMAIL
FROM Person
GROUP BY email
HAVING count(email) > 1

-- HAVING selects group rows AFTER groups and aggregates are computed

-- reference: 
  -- https://www.postgresql.org/docs/current/tutorial-agg.html