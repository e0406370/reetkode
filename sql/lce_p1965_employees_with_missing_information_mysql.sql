/*
  LCE 1965. Employees With Missing Information
  -> MySQL

  Table: Employees

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | employee_id | int     |
  | name        | varchar |
  +-------------+---------+
  - employee_id is the column with unique values for this table.
  - Each row of this table indicates the name of the employee whose ID is employee_id.
  

  Table: Salaries

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | employee_id | int     |
  | salary      | int     |
  +-------------+---------+
  - employee_id is the column with unique values for this table.
  - Each row of this table indicates the salary of the employee whose ID is employee_id.

  Write a solution to report the IDs of all the employees with missing information.
  The information of an employee is missing if:
  - The employee's name is missing, or
  - The employee's salary is missing.
  
  Return the result table ordered by employee_id in ascending order.
*/

SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)

UNION

SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)

ORDER BY employee_id ASC