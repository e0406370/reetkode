/*
  LCM 3220. Odd and Even Transactions
  -> MySQL

  Table: transactions

  +------------------+------+
  | Column Name      | Type | 
  +------------------+------+
  | transaction_id   | int  |
  | amount           | int  |
  | transaction_date | date |
  +------------------+------+
  - The transactions_id column uniquely identifies each row in this table.
  - Each row of this table contains the transaction id, amount and transaction date.

  Write a solution to find the sum of amounts for odd and even transactions for each day.
  If there are no odd or even transactions for a specific date, display as 0.

  Return the result table ordered by transaction_date in ascending order.
*/

SELECT transaction_date, SUM(IF(amount % 2 != 0, amount, 0)) AS odd_sum, SUM(IF(amount % 2 = 0, amount, 0)) AS even_sum
FROM Transactions
GROUP BY transaction_date
ORDER BY transaction_date ASC

/*
  basic syntax of the SUM IF:

  SELECT SUM(IF(condition, value_to_sum, 0))
  FROM table_name;

  - condition: The condition that you want to apply.
  - value_to_sum: The value that you want to sum if the condition is true.
  - 0: The value to sum if the condition is false. You can change it to any default value you want.
*/