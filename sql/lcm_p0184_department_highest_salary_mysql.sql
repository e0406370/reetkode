/*
  LCM 184. Department Highest Salary
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
  - departmentId is a foreign key (reference columns) of the ID from the Department table.
  - Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
  

  Table: Department

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | name        | varchar |
  +-------------+---------+
  - id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
  - Each row of this table indicates the ID of a department and its name.

  Write a solution to find employees who have the highest salary in each of the departments.

  Return the result table in any order.
*/

SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Employee E
LEFT JOIN Department D ON E.departmentId = D.id
WHERE (E.departmentId, E.salary) IN (
  SELECT departmentId, MAX(salary)
  FROM Employee
  GROUP BY departmentId
)