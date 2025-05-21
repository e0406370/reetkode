/*
  LCE 1731. The Number of Employees Which Report to Each Employee
  -> MySQL

  Table: Employees

  +-------------+----------+
  | Column Name | Type     |
  +-------------+----------+
  | employee_id | int      |
  | name        | varchar  |
  | reports_to  | int      |
  | age         | int      |
  +-------------+----------+
  - employee_id is the column with unique values for this table.
  - This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 
  
  For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

  Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

  Return the result table ordered by employee_id.
*/

SELECT E1.employee_id, E1.name, COUNT(E2.name) AS reports_count, ROUND(AVG(E2.age)) AS average_age
FROM Employees E1, Employees E2
WHERE E1.employee_id = E2.reports_to
GROUP BY E1.employee_id
ORDER BY E1.employee_id

-- round to nearest integer: https://stackoverflow.com/questions/12361220/how-to-round-down-to-nearest-integer-in-mysql