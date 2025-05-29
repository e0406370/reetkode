/*
  LCM 1321. Restaurant Growth
  -> MySQL

  Table: Customer

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | customer_id   | int     |
  | name          | varchar |
  | visited_on    | date    |
  | amount        | int     |
  +---------------+---------+
  - In SQL,(customer_id, visited_on) is the primary key for this table.
  - This table contains data about customer transactions in a restaurant.
  - visited_on is the date on which the customer with ID (customer_id) has visited the restaurant.
  - amount is the total paid by a customer.

  You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

  Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). average_amount should be rounded to two decimal places.

  Return the result table ordered by visited_on in ascending order.
*/

SELECT
    visited_on, 
    (
        SELECT SUM(amount)
        FROM Customer C2
        WHERE C2.visited_on BETWEEN DATE_SUB(C1.visited_on, INTERVAL 6 DAY) AND C1.visited_on
    ) 
    AS amount,
    (
        SELECT ROUND(SUM(amount) / 7, 2)
        FROM Customer C2
        WHERE C2.visited_on BETWEEN DATE_SUB(C1.visited_on, INTERVAL 6 DAY) AND C1.visited_on
    )
    AS average_amount
FROM Customer C1
GROUP BY visited_on
ORDER BY visited_on ASC
LIMIT 999
OFFSET 6

/* - need to offset records for the first 6 days since we are looking at a seven days window.
   - OFFSET needs to be used together with LIMIT, set LIMIT to a sufficiently high arbitrary number
*/