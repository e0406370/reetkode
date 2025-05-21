/*
  LCE 1407. Top Travellers
  -> MySQL

  Table: Users

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | id            | int     |
  | name          | varchar |
  +---------------+---------+
  - id is the column with unique values for this table.
  - name is the name of the user.
  

  Table: Rides

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | id            | int     |
  | user_id       | int     |
  | distance      | int     |
  +---------------+---------+
  - id is the column with unique values for this table.
  - user_id is the id of the user who traveled the distance "distance".

  Write a solution to report the distance traveled by each user.
  Return the result table ordered by travelled_distance in descending order.
  If two or more users traveled the same distance, order them by their name in ascending order.

  Return the result table in any order.
*/

SELECT U.name, COALESCE(SUM(R.distance), 0) AS travelled_distance
FROM Users U
LEFT JOIN Rides R ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, U.name ASC