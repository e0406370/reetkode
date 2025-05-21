/*
  LCE 1581. Customer Who Visited but Did Not Make Any Transactions
  -> MS SQL Server

  Table: Visits

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | visit_id    | int     |
  | customer_id | int     |
  +-------------+---------+
  - visit_id is the column with unique values for this table.
  - This table contains information about the customers who visited the mall.

  Table: Transactions

  +----------------+---------+
  | Column Name    | Type    |
  +----------------+---------+
  | transaction_id | int     |
  | visit_id       | int     |
  | amount         | int     |
  +----------------+---------+
  - transaction_id is column with unique values for this table.
  - This table contains information about the transactions made during the visit_id.

  Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
  
  Return the result table sorted in any order.
*/

SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM [Visits] V
LEFT JOIN [Transactions] T ON V.visit_id = T.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id

-- WHERE clause must come before the GROUP BY clause!