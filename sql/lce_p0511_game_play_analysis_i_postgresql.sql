/*
  LCE 511. Game Play Analysis I
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
  
  Write a solution to find the first login date for each player.

  Return the result table in any order.
*/

-- Method 1: using GROUP BY and min()
SELECT player_id, min(event_date) AS first_login
FROM Activity
GROUP BY player_id

-- Method 2: CTE with rank() window function
WITH R AS (
    SELECT player_id, event_date, rank() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rank
    FROM Activity
)
SELECT player_id, event_date AS first_login
FROM R
WHERE R.rank = 1

-- reference: 
  -- M1: https://www.postgresql.org/docs/current/tutorial-agg.html
  -- M1: https://www.postgresql.org/docs/17/functions-aggregate.html
  -- M2: https://www.postgresql.org/docs/current/queries-with.html
  -- M2: https://www.postgresql.org/docs/17/tutorial-window.html