/*
  LCM 1164. Product Price at a Given Date
  -> MySQL

  Table: Products

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | product_id    | int     |
  | new_price     | int     |
  | change_date   | date    |
  +---------------+---------+
  - (product_id, change_date) is the primary key (combination of columns with unique values) of this table.
  - Each row of this table indicates that the price of some product was changed to a new price at some date.

  Write a solution to find the prices of all products on 2019-08-16. 
  Assume the price of all products before any change is 10.

  Return the result table in any order.
*/

WITH 
Changed AS (
    SELECT product_id, new_price AS price
    FROM Products
    WHERE (product_id, change_date) IN
    (
      SELECT product_id, MAX(change_date)
      FROM Products
      WHERE change_date <= '2019-08-16'
      GROUP BY product_id
    )
),
Unchanged AS (
    SELECT product_id, 10 AS price
    FROM Products
    WHERE product_id NOT IN (SELECT product_id FROM Changed)
)

SELECT product_id, price
FROM Changed

UNION

SELECT product_id, price
FROM Unchanged

-- reference: https://dev.mysql.com/doc/refman/8.4/en/with.html