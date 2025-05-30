/*
  LCE 1484. Group Sold Products By The Date
  -> MySQL

  Table: Activities

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | sell_date   | date    |
  | product     | varchar |
  +-------------+---------+
  - There is no primary key (column with unique values) for this table. It may contain duplicates.
  - Each row of this table contains the product name and the date it was sold in a market.

  Write a solution to find for each date the number of different products sold and their names.
  The sold products names for each date should be sorted lexicographically.

  Return the result table ordered by sell_date.
*/

SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC

-- https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html#function_group-concat