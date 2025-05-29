/*
  LCE 1068. Product Sales Analysis I
  -> PostgreSQL

  Table: Sales

  +-------------+-------+
  | Column Name | Type  |
  +-------------+-------+
  | sale_id     | int   |
  | product_id  | int   |
  | year        | int   |
  | quantity    | int   |
  | price       | int   |
  +-------------+-------+
  - (sale_id, year) is the primary key (combination of columns with unique values) of this table.
  - product_id is a foreign key (reference column) to Product table.
  - Each row of this table shows a sale on the product product_id in a certain year.
  - Note that the price is per unit.
  

  Table: Product

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | product_id   | int     |
  | product_name | varchar |
  +--------------+---------+
  - product_id is the primary key (column with unique values) of this table.
  - Each row of this table indicates the product name of each product.
  
  Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

  Return the resulting table in any order.
*/

SELECT p.product_name, s.year, s.price
FROM Sales s INNER JOIN Product p
USING (product_id)

/* 
  ref: https://www.postgresql.org/docs/current/queries-table-expressions.html
  
  - INNER JOIN
  For each row R1 of T1, the joined table has a row for each row in T2 that satisfies the join condition with R1.

  - LEFT (OUTER) JOIN
  First, an inner join is performed.
  Then, for each row in T1 that does not satisfy the join condition with any row in T2, 
  a joined row is added with null values in columns of T2. Thus, the joined table always has at least one row for each row in T1.

  - RIGHT (OUTER) JOIN
  First, an inner join is performed.
  Then, for each row in T2 that does not satisfy the join condition with any row in T1,
  a joined row is added with null values in columns of T1. This is the converse of a left join: the result table will always have a row for each row in T2.
*/
