/*
  LCE 1280. Students and Examinations
  -> MySQL

  Table: Students

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | student_id    | int     |
  | student_name  | varchar |
  +---------------+---------+
  - student_id is the primary key (column with unique values) for this table.
  - Each row of this table contains the ID and the name of one student in the school.
  

  Table: Subjects

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | subject_name | varchar |
  +--------------+---------+
  - subject_name is the primary key (column with unique values) for this table.
  - Each row of this table contains the name of one subject in the school.
  

  Table: Examinations

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | student_id   | int     |
  | subject_name | varchar |
  +--------------+---------+
  - There is no primary key (column with unique values) for this table. It may contain duplicates.
  - Each student from the Students table takes every course from the Subjects table.
  - Each row of this table indicates that a student with ID student_id attended the exam of subject_name.

  Write a solution to find the number of times each student attended each exam.

  Return the result table ordered by student_id and subject_name.
*/

SELECT ST.student_id, ST.student_name, SU.subject_name, COUNT(E.subject_name) AS attended_exams
FROM Students ST
CROSS JOIN Subjects SU
LEFT JOIN Examinations E ON ST.student_id = E.student_id AND SU.subject_name = E.subject_name
GROUP BY ST.student_name, SU.subject_name
ORDER BY ST.student_id, SU.subject_name

-- reference: https://www.geeksforgeeks.org/mysql-cross-join/