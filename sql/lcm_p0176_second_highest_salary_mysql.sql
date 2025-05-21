/*
  LCM 176. Second Highest Salary
  -> MySQL

  Table: Employee

  +-------------+------+
  | Column Name | Type |
  +-------------+------+
  | id          | int  |
  | salary      | int  |
  +-------------+------+
  - id is the primary key (column with unique values) for this table.
  - Each row of this table contains information about the salary of an employee.

  Write a solution to find the second highest distinct salary from the Employee table. 
  If there is no second highest salary, return null (return None in Pandas).
*/

SELECT COALESCE(
    (SELECT salary 
     FROM Employee
     GROUP BY salary
     ORDER BY salary DESC 
     LIMIT 1 OFFSET 1
    ), 
    NULL
) AS SecondHighestSalary;