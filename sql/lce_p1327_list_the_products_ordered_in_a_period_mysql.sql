/*
  LCE 1327. List the Products Ordered in a Period
  -> MySQL

  Table: Products

  +------------------+---------+
  | Column Name      | Type    |
  +------------------+---------+
  | product_id       | int     |
  | product_name     | varchar |
  | product_category | varchar |
  +------------------+---------+
  - product_id is the primary key (column with unique values) for this table.
  - This table contains data about the company's products.
  

  Table: Orders

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | product_id    | int     |
  | order_date    | date    |
  | unit          | int     |
  +---------------+---------+
  - This table may have duplicate rows.
  - product_id is a foreign key (reference column) to the Products table.
  - unit is the number of products ordered in order_date.

  Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

  Return the result table in any order.
*/

SELECT product_name, SUM(unit) AS unit
FROM Products P
LEFT JOIN Orders O ON P.product_id = O.product_id
WHERE O.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY P.product_id
HAVING unit >= 100