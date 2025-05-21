/*
  LCE 1633. Percentage of Users Attended a Contest
  -> MS SQL Server

  Table: Users

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | user_id     | int     |
  | user_name   | varchar |
  +-------------+---------+
  - user_id is the primary key (column with unique values) for this table.
  - Each row of this table contains the name and the id of a user.
  

  Table: Register

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | contest_id  | int     |
  | user_id     | int     |
  +-------------+---------+
  - (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
  - Each row of this table contains the id of a user and the contest they registered into.

  Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
  
  Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.
*/

SELECT contest_id, ROUND(1.00 * COUNT(user_id) / (SELECT COUNT(*) FROM [Users]) * 100, 2) AS percentage
FROM [Register] 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

-- multiplying by 1.00 ensures floating-point division and prevents truncation of decimal places