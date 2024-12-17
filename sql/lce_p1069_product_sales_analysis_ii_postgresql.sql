/*
  LCE 1069. Product Sales Analysis II (Premium)
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
  
  Write a solution that reports the total quantity sold for every product id.

  Return the resulting table in any order.
*/

SELECT p.product_id, sum(s.quantity) AS total_quantity
FROM Sales s INNER JOIN Product p
USING (product_id)
GROUP BY p.product_id