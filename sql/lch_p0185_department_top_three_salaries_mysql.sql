/*
  LCH 185. Department Top Three Salaries
  -> MySQL

  Table: Employee

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | id           | int     |
  | name         | varchar |
  | salary       | int     |
  | departmentId | int     |
  +--------------+---------+
  - id is the primary key (column with unique values) for this table.
  - departmentId is a foreign key (reference column) of the ID from the Department table.
  - Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
  

  Table: Department

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | name        | varchar |
  +-------------+---------+
  - id is the primary key (column with unique values) for this table.
  - Each row of this table indicates the ID of a department and its name.
 

  A company's executives are interested in seeing who earns the most money in each of the company's departments.
  A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

  Write a solution to find the employees who are high earners in each of the departments.

  Return the result table in any order.
*/

WITH Temp AS (
  SELECT
    name,
    salary,
    departmentId,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS 'rank'
  FROM Employee
)

SELECT D.name AS Department, T.name AS Employee, T.salary AS Salary
FROM Temp T
LEFT JOIN Department D ON T.departmentId = D.id
WHERE T.rank IN (1, 2, 3)

-- reference: https://dev.mysql.com/doc/refman/8.4/en/window-function-descriptions.html#function_rank