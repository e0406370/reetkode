/*
  LCE 577. Employee Bonus
  -> PostgreSQL

  Table: Employee

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | empId       | int     |
  | name        | varchar |
  | supervisor  | int     |
  | salary      | int     |
  +-------------+---------+
  - empId is the column with unique values for this table.
  - Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
  

  Table: Bonus

  +-------------+------+
  | Column Name | Type |
  +-------------+------+
  | empId       | int  |
  | bonus       | int  |
  +-------------+------+
  - empId is the column of unique values for this table.
  - empId is a foreign key (reference column) to empId from the Employee table.
  - Each row of this table contains the id of an employee and their respective bonus.

  Write a solution to report the name and bonus amount of each employee with a bonus less than 1000. 

  Return the result table in any order.
*/

SELECT E.name, B.bonus
FROM Employee E LEFT JOIN Bonus B
ON E.empId = B.empId
WHERE B.bonus IS NULL OR B.bonus < 1000

-- reference:
  -- https://www.postgresql.org/docs/17/functions-comparison.html