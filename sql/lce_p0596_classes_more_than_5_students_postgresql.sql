/*
  LCE 596. Classes More Than 5 Students
  -> PostgreSQL

  Table: Courses

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | student     | varchar |
  | class       | varchar |
  +-------------+---------+
  - (student, class) is the primary key (combination of columns with unique values) for this table.
  - Each row of this table indicates the name of a student and the class in which they are enrolled.
  
  Write a solution to find all the classes that have at least five students.

  Return the result table in any order.
*/

-- Method 1: using GROUP BY and HAVING
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5

-- Method 2: using subquery
SELECT class
FROM (
    SELECT class, COUNT(*) AS count
    FROM Courses
    GROUP BY class
)
WHERE count >= 5