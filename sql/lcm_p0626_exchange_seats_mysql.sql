/*
  LCM 626. Exchange Seats
  -> MySQL

  Table: Seat

  +-------------+---------+
  | Column Name | Type    |
  +-------------+---------+
  | id          | int     |
  | student     | varchar |
  +-------------+---------+
  - id is the primary key (unique value) column for this table.
  - Each row of this table indicates the name and the ID of a student.
  - The ID sequence always starts from 1 and increments continuously.

  Write a solution to swap the seat id of every two consecutive students.
  If the number of students is odd, the id of the last student is not swapped.

  Return the result table ordered by id in ascending order.
*/

-- Method 1: using CASE WHEN to swap seat id except last student
SELECT 
    CASE 
        WHEN
            mod(id, 2) = 0
        THEN
            id - 1
        WHEN
            mod(id, 2) <> 0 AND id + 1 IN (SELECT id FROM Seat)
        THEN
            id + 1
        ELSE
            id
    END
    AS id,
    student
FROM Seat
ORDER BY id ASC   


-- Method 2: using UNION ALL to swap seat id, then use row_number() to clean up seat id for last student
WITH Temp AS (
    SELECT id - 1 AS id, student
    FROM Seat
    WHERE id % 2 = 0

    UNION ALL

    SELECT id + 1 AS id, student
    FROM Seat
    WHERE id % 2 <> 0
)

SELECT row_number() OVER w AS 'id', student
FROM Temp
WINDOW w AS (ORDER BY id ASC)