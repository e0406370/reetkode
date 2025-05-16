/*
  LCE 597. Friend Requests I: Overall Acceptance Rate
  -> PostgreSQL

  Table: FriendRequest

  +----------------+---------+
  | Column Name    | Type    |
  +----------------+---------+
  | sender_id      | int     |
  | send_to_id     | int     |
  | request_date   | date    |
  +----------------+---------+
  - This table may contain duplicates (In other words, there is no primary key for this table in SQL).
  - This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date of the request.
  

  Table: RequestAccepted

  +----------------+---------+
  | Column Name    | Type    |
  +----------------+---------+
  | requester_id   | int     |
  | accepter_id    | int     |
  | accept_date    | date    |
  +----------------+---------+
  - This table may contain duplicates (In other words, there is no primary key for this table in SQL).
  - This table contains the ID of the user who sent the request, the ID of the user who accepted the request, and the date when the request was accepted.
  
  Find the overall acceptance rate of requests, which is the number of acceptance divided by the number of requests.
  Return the answer rounded to 2 decimals places.

  Note that:
  - The accepted requests are not necessarily from the table FriendRequest. 
    In this case, count the total accepted requests (no matter whether they are in the original requests or not), and divide it by the number of requests to get the acceptance rate.

  - It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once.
    In this case, the ‘duplicated’ requests or acceptances are only counted once.

  - If there are no requests at all, you should return 0.00 as the accept_rate.
*/

WITH 
total AS (
    SELECT 
        CASE count(DISTINCT (sender_id, send_to_id))
            WHEN 0 THEN 1
            ELSE count(DISTINCT (sender_id, send_to_id))
        END
        AS count
    FROM FriendRequest
)
,
accepted AS (
    SELECT count(DISTINCT (requester_id, accepter_id)) AS count
    FROM RequestAccepted
)

SELECT round(accepted.count * 1.0 / total.count, 2) AS accept_rate
FROM total, accepted

-- references:
  -- https://www.postgresql.org/docs/current/queries-with.html
  -- https://www.postgresql.org/docs/current/functions-conditional.html
  -- https://www.postgresql.org/docs/17/functions-math.html