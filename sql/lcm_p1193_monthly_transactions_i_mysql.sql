/*
  LCM 1193. Monthly Transactions I
  -> MySQL

  Table: Transactions

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | id            | int     |
  | country       | varchar |
  | state         | enum    |
  | amount        | int     |
  | trans_date    | date    |
  +---------------+---------+
  - id is the primary key of this table.
  - The table has information about incoming transactions.
  - The state column is an enum of type ["approved", "declined"].

  Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

  Return the result table in any order.
*/

SELECT
  DATE_FORMAT(trans_date, '%Y-%m') AS month, 
  country, 
  COUNT(*) AS trans_count, 
  SUM(IF(state = 'approved', 1, 0)) AS approved_count, 
  SUM(amount) AS trans_total_amount,
  SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount 
FROM Transactions
GROUP BY month, country

-- reference: https://dev.mysql.com/doc/refman/8.4/en/date-and-time-functions.html#function_date-format