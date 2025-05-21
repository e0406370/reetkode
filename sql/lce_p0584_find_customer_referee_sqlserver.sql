/*
  LCE 584. Find Customer Referee
  -> MS SQL Server

  Table: Customer

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | name        | varchar |
  | referee_id  | int     |
  +-------------+---------+
  - In SQL, id is the primary key column for this table.
  - Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

  Find the names of the customer that are NOT referred by the customer with id = 2.
  
  Return the result table in any order.
*/

SELECT name
FROM [Customer]
WHERE COALESCE(referee_id, '') != 2

-- COALESCE is used to handle NULL values; if referee_id is NULL, it will replaced with an empty string ''.