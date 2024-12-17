/*
  LCE 1084. Sales Analysis III (Premium)
  -> PostgreSQL

  Table: Product

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | product_id   | int     |
  | product_name | varchar |
  | unit_price   | int     |
  +--------------+---------+
  - product_id is the primary key (column with unique values) of this table.
  - Each row of this table indicates the name and the price of each product.

  Table: Sales

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | seller_id   | int     |
  | product_id  | int     |
  | buyer_id    | int     |
  | sale_date   | date    |
  | quantity    | int     |
  | price       | int     |
  +-------------+---------+
  - This table can have duplicate rows.
  - product_id is a foreign key (reference column) to the Product table.
  - Each row of this table contains some information about one sale.

  Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

  Return the result table in any order.
*/

SELECT p.product_id, p.product_name
FROM Product p INNER JOIN Sales s
USING (product_id)
GROUP BY p.product_id, p.product_name
HAVING min(s.sale_date) >= '2019-01-01' AND max(s.sale_date) <= '2019-03-31'

-- reference:
  -- https://www.postgresql.org/docs/current/functions-aggregate.html