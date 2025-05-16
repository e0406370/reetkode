/*
  LCE 512. Game Play Analysis II (Premium)
  -> PostgreSQL

  Table: Activity

  +--------------+---------+
  | Column Name  | Type    |
  +--------------+---------+
  | player_id    | int     |
  | device_id    | int     |
  | event_date   | date    |
  | games_played | int     |
  +--------------+---------+
  - (player_id, event_date) is the primary key (combination of columns with unique values) of this table.
  - This table shows the activity of players of some games.
  - Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
  
  Write a solution to report the device that is first logged in for each player.

  Return the result table in any order.
*/

-- Method 1: subquery and multi-value use of the IN comparison operator
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT player_id, min(event_date)
    FROM Activity
    GROUP BY player_id
)

-- Method 2: CTE with rank() window funciton
WITH R AS (
    SELECT player_id, device_id, rank() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rank
    FROM Activity
)
SELECT player_id, device_id
FROM R
WHERE R.rank = 1

-- Method 3: using first_value() window function
SELECT 
    DISTINCT player_id, 
    first_value(device_id) OVER (PARTITION BY player_id ORDER BY event_date) AS device_id
FROM Activity

-- reference:
  -- M1, M2: refer to lce_p0511
  -- M3: https://www.postgresql.org/docs/17/functions-window.html