/*
  LCE 607. Sales Person
  -> PostgreSQL

  Table: SalesPerson

  +-----------------+---------+
  | Column Name     | Type    |
  +-----------------+---------+
  | sales_id        | int     |
  | name            | varchar |
  | salary          | int     |
  | commission_rate | int     |
  | hire_date       | date    |
  +-----------------+---------+
  - sales_id is the primary key (column with unique values) for this table.
  - Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
  

  Table: Company

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | com_id      | int     |
  | name        | varchar |
  | city        | varchar |
  +-------------+---------+
  - com_id is the primary key (column with unique values) for this table.
  - Each row of this table indicates the name and the ID of a company and the city in which the company is located.
  

  Table: Orders

  +-------------+------+
  | Column Name | Type |
  +-------------+------+
  | order_id    | int  |
  | order_date  | date |
  | com_id      | int  |
  | sales_id    | int  |
  | amount      | int  |
  +-------------+------+
  - order_id is the primary key (column with unique values) for this table.
  - com_id is a foreign key (reference column) to com_id from the Company table.
  - sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
  - Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
  
  Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

  Return the result table in any order.
*/

SELECT name
FROM SalesPerson
WHERE name NOT IN (
    SELECT sp.name
    FROM SalesPerson sp
    LEFT JOIN Orders o ON sp.sales_id = o.sales_id
    LEFT JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)

-- exclusion using NOT IN operator