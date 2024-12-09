/*
  LCE 613. Shortest Distance in a Line (Premium)
  -> PostgreSQL

  Table: Point

  +-------------+------+
  | Column Name | Type |
  +-------------+------+
  | x           | int  |
  +-------------+------+
  In SQL, x is the primary key column for this table.
  Each row of this table indicates the position of a point on the X-axis.
  
  Find the shortest distance between any two points from the Point table.
*/

SELECT min(distance) AS shortest
FROM (
    SELECT abs(p1.x - p2.x) AS distance
    FROM Point p1, Point p2
    WHERE p1.x <> p2.x
)