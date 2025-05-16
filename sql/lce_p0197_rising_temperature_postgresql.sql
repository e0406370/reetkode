/*
  LCE 197. Rising Temperature
  -> PostgreSQL

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

-- Method 1: standard INNER JOIN
SELECT w1.id
FROM Weather w1 INNER JOIN Weather W2
ON w1.recordDate = w2.recordDate + 1
AND w1.temperature > w2.temperature

-- Method 2: Cartesian product = CROSS JOIN
SELECT W1.id
FROM Weather W1, Weather W2
WHERE W1.recordDate = W2.recordDate + 1
AND W1.temperature > W2.temperature

-- reference: 
  -- M1: https://www.postgresql.org/docs/17/queries-table-expressions.html#:~:text=The%20join%20condition%20specified%20with%20ON%20can%20also%20contain%20conditions%20that%20do%20not%20relate%20directly%20to%20the%20join