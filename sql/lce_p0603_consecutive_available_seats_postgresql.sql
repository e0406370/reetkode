/*
  LCE 603. Consecutive Available Seats (Premium)
  -> PostgreSQL

  Table: Cinema

  +-------------+------+
  | Column Name | Type |
  +-------------+------+
  | seat_id     | int  |
  | free        | bool |
  +-------------+------+
  seat_id is an auto-increment column for this table.
  Each row of this table indicates whether the ith seat is free or not. 1 means free while 0 means occupied.
  
  Find all the consecutive available seats in the cinema.

  Return the result table ordered by seat_id in ascending order.

  The test cases are generated so that more than two seats are consecutively available.
*/

-- Method 1: using abs function to retrieve consecutive seats
SELECT DISTINCT c1.seat_id
FROM Cinema c1 INNER JOIN Cinema c2
ON abs(c1.seat_id - c2.seat_id) = 1
AND (c1.free = 1 AND c2.free = 1)
ORDER BY seat_id ASC

-- Method 2: using subqueries to retrieve consecutive seats
SELECT seat_id
FROM Cinema
WHERE free = 1
AND
(
    seat_id + 1 IN (SELECT seat_id FROM Cinema WHERE free = 1)
    OR 
    seat_id - 1 IN (SELECT seat_id FROM Cinema WHERE free = 1)
)
ORDER BY seat_id ASC

-- consecutive seats include:
  -- start: check for succeeding seat
  -- middle: check for BOTH preceding and succeeding seats
  -- end: check for preceding seat

-- references:
  -- M1: https://www.postgresql.org/docs/17/functions-math.html