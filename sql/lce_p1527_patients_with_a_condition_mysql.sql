/*
  LCE 1527. Patients With a Condition
  -> MySQL

  Table: Patients

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | patient_id   | int     |
  | patient_name | varchar |
  | conditions   | varchar |
  +--------------+---------+
  - patient_id is the primary key (column with unique values) for this table.
  - 'conditions' contains 0 or more code separated by spaces. 
  - This table contains information of the patients in the hospital.

  Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes.
  Type I Diabetes always starts with DIAB1 prefix.
  
  Return the result table in any order.
*/

SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions REGEXP '^DIAB1| DIAB1'

/*
  - reference: https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/

  - ^ => marks start of string
  - p1|p2|p3 => alternation; matches any of the patterns p1, p2, or p3

  - In MySQL, REGEXP and RLIKE are synonymous operators used for performing regular expression matching. 
  The primary difference between REGEXP and RLIKE is that REGEXP is the standard operator, while RLIKE is just an alias for it.
*/