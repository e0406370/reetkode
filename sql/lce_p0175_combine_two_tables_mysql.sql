/*
  LCE 175. Combine Two Tables
  -> MySQL

  Table: Person

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | personId    | int     |
  | lastName    | varchar |
  | firstName   | varchar |
  +-------------+---------+
  - personId is the primary key (column with unique values) for this table.
  - This table contains information about the ID of some persons and their first and last names.
  

  Table: Address

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | addressId   | int     |
  | personId    | int     |
  | city        | varchar |
  | state       | varchar |
  +-------------+---------+
  - addressId is the primary key (column with unique values) for this table.
  - Each row of this table contains information about the city and state of one person with ID = PersonId.

  Write a solution to report the first name, last name, city, and state of each person in the Person table.
  If the address of a personId is not present in the Address table, report null instead.
  
  Return the result table in any order.
*/

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A ON P.personId = A.personId

/*
  MySQL LEFT JOIN is a type of outer join that returns all records from the left table and matches records from the right table. 
  If there is no match, the result is NULL from the right table. 
  This join is also known as Left Outer Join.

  reference: https://www.geeksforgeeks.org/mysql-left-join/
*/