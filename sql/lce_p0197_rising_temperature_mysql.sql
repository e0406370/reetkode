/*
  LCE 197. Rising Temperature
  -> MySQL

  Table: Weather

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | id            | int     |
  | recordDate    | date    |
  | temperature   | int     |
  +---------------+---------+
  - id is the column with unique values for this table.
  - There are no different rows with the same recordDate.
  - This table contains information about the temperature on a certain day.

  Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
  
  Return the result table in any order.
*/

SELECT W1.id
FROM Weather W1, Weather W2
WHERE DATEDIFF(W1.recordDate, W2.recordDate) = 1
AND W1.temperature > W2.temperature

-- reference: https://dev.mysql.com/doc/refman/8.4/en/date-and-time-functions.html#function_datediff
-- cartesian product (or cross join) approach -> every row in W1 is paired with every row in W2