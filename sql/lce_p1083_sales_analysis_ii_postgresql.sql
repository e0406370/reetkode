/*
  LCE 1083. Sales Analysis II (Premium)
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
  - This table might have repeated rows.
  - product_id is a foreign key (reference column) to the Product table.
  - buyer_id is never NULL. 
  - sale_date is never NULL. 
  - Each row of this table contains some information about one sale.

  Write a solution to report the buyers who have bought S8 but not iPhone. Note that S8 and iPhone are products presented in the Product table.

  Return the result table in any order.
*/

-- Method 1: exclusion using EXCEPT set operation
SELECT DISTINCT s.buyer_id
FROM Sales s INNER JOIN Product p
USING (product_id)
WHERE p.product_name = 'S8'
EXCEPT
SELECT DISTINCT s.buyer_id
FROM Sales s INNER JOIN Product p
USING (product_id)
WHERE p.product_name = 'iPhone'

-- Method 2: exclusion using NOT IN operator
WITH cte AS(
    SELECT s.buyer_id, p.product_name
    FROM Sales s INNER JOIN Product p
    USING (product_id)
)
SELECT DISTINCT buyer_id
FROM cte
WHERE product_name = 'S8'
AND buyer_id NOT IN (
    SELECT buyer_id
    FROM cte
    WHERE product_name = 'iPhone'
)

-- Method 3: conditional aggregation
SELECT DISTINCT s.buyer_id
FROM Sales s INNER JOIN Product p
USING (product_id)
GROUP BY s.buyer_id
HAVING sum(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) > 0
AND sum(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) = 0

-- Method 4: filter using string_agg aggregate function
SELECT DISTINCT s.buyer_id
FROM Sales s INNER JOIN Product p
USING (product_id)
GROUP BY s.buyer_id
HAVING string_agg(p.product_name, ',') LIKE '%S8%'
AND string_agg(p.product_name, ',') NOT LIKE '%iPhone%'

-- reference:
  -- M1: https://www.postgresql.org/docs/current/queries-union.html
  -- M2: https://www.postgresql.org/docs/current/functions-subquery.html
  -- M3: https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-CASE
  -- M4: https://www.postgresql.org/docs/current/functions-aggregate.html