/*
  LCE 1082. Sales Analysis I (Premium)
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
  - This table can have repeated rows.
  - product_id is a foreign key (reference column) to the Product table.
  - Each row of this table contains some information about one sale.  

  Write a solution that reports the best seller by total sales price. If there is a tie, report them all.

  Return the result table in any order.
*/

-- Method 1: CTE with rank() window function
WITH cte AS (
    SELECT seller_id, rank() OVER (ORDER BY sum(price) DESC) AS rank
    FROM Sales
    GROUP BY seller_id
)
SELECT seller_id 
FROM cte
WHERE rank = 1

-- Method 2: CTE with max() aggregate function
WITH cte AS (
    SELECT seller_id, sum(price) AS total_price
    FROM Sales
    GROUP BY seller_id
)
SELECT seller_id
FROM cte
WHERE total_price = (SELECT max(total_price) FROM cte)

-- Method 3: subquery with ORDER BY DESC and LIMIT 1 to retrieve the maximum
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING sum(price) = (
    SELECT sum(price) AS total_price
    FROM Sales
    GROUP BY seller_id
    ORDER BY total_price DESC
    LIMIT 1
)