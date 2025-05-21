/*
  LCM 550. Game Play Analysis IV
  -> MySQL

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

  Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. 
  In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date.
  Then, divide that number by the total number of players.
*/

WITH Temp AS (
  SELECT player_id, MIN(event_date) AS event_date
  FROM Activity
  GROUP BY player_id
)

SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Temp), 2) AS fraction 
FROM Activity A
LEFT JOIN Temp T ON A.player_id = T.player_id
WHERE A.event_date = T.event_date + INTERVAL 1 DAY

-- reference: https://dev.mysql.com/doc/refman/8.4/en/expressions.html#temporal-intervals