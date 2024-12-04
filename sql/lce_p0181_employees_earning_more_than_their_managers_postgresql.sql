/*
  LCE 181. Employees Earning More Than Their Managers
  -> PostgreSQL

  Table: Employee

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | name        | varchar |
  | salary      | int     |
  | managerId   | int     |
  +-------------+---------+
  - id is the primary key (column with unique values) for this table.
  - Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

  Write a solution to find the employees who earn more than their managers.

  Return the result table in any order.
*/

-- Method 1: AND clause -> processed BEFORE the join
SELECT E1.name AS Employee
FROM Employee E1 INNER JOIN Employee E2
ON E1.managerId = E2.id
AND E1.salary > E2.salary

-- Method 2: WHERE clause -> processed AFTER the join
SELECT E1.name AS Employee
FROM Employee E1 INNER JOIN Employee E2
ON E1.managerId = E2.id
WHERE E1.salary > E2.salary

-- E1 refers to Employees, E2 refers to Managers

-- reference: 
  -- https://www.postgresql.org/docs/17/queries-table-expressions.html