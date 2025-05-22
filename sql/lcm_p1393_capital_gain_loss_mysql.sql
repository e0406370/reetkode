/*
  LCM 1393. Capital Gain/Loss
  -> MySQL

  Table: Stocks

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | stock_name    | varchar |
  | operation     | enum    |
  | operation_day | int     |
  | price         | int     |
  +---------------+---------+
  - (stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
  - The operation column is an ENUM (category) of type ('Sell', 'Buy')
  - Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
  - It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day.
  - It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.

  Write a solution to report the Capital gain/loss for each stock.
  The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

  Return the result table in any order.
*/

SELECT stock_name, (SUM(IF(operation = 'Sell', price, 0)) - SUM(IF(operation = 'Buy', price, 0))) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;

/*
  basic syntax of the SUM IF:

  SELECT SUM(IF(condition, value_to_sum, 0))
  FROM table_name;

  - condition: The condition that you want to apply.
  - value_to_sum: The value that you want to sum if the condition is true.
  - 0: The value to sum if the condition is false. You can change it to any default value you want.
*/