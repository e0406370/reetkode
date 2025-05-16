/*
  LCE 586. Customer Placing the Largest Number of Orders
  -> PostgreSQL

  Table: Orders

  +-----------------+----------+
  | Column Name     | Type     |
  +-----------------+----------+
  | order_number    | int      |
  | customer_number | int      |
  +-----------------+----------+
  - order_number is the primary key (column with unique values) for this table.
  - This table contains information about the order ID and the customer ID.
  
  Write a solution to find the customer_number for the customer who has placed the largest number of orders.

  The test cases are generated so that exactly one customer will have placed more orders than any other customer.
*/

-- Method 1: using ORDER BY and LIMIT
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY count(order_number) DESC
LIMIT 1

-- Method 2: using nested subqueries
SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING count(*) = (
    SELECT max(count)
    FROM (
        SELECT count(*) AS count
        FROM Orders
        GROUP BY customer_number
    )
)

-- reference: 
  -- M1: https://www.postgresql.org/docs/17/queries-limit.html
  -- M2: https://www.postgresql.org/docs/17/functions-aggregate.html