/*
  LCM 1341. Movie Rating
  -> MySQL

  Table: Movies

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | movie_id      | int     |
  | title         | varchar |
  +---------------+---------+
  - movie_id is the primary key (column with unique values) for this table.
  - title is the name of the movie.
  

  Table: Users

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | user_id       | int     |
  | name          | varchar |
  +---------------+---------+
  - user_id is the primary key (column with unique values) for this table.
  - The column 'name' has unique values.

  Table: MovieRating

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | movie_id      | int     |
  | user_id       | int     |
  | rating        | int     |
  | created_at    | date    |
  +---------------+---------+
  - (movie_id, user_id) is the primary key (column with unique values) for this table.
  - This table contains the rating of a movie by a user in their review.
  - created_at is the user's review date. 

  Write a solution to:
  - Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
  - Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
*/

(SELECT U.name AS results
 FROM MovieRating MR
 LEFT JOIN Users U ON MR.user_id = U.user_id
 GROUP BY U.user_id
 ORDER BY COUNT(U.user_id) DESC, U.name ASC
 LIMIT 1)

UNION ALL

(SELECT M.title AS results
 FROM MovieRating MR
 LEFT JOIN Movies M ON MR.movie_id = M.movie_id
 WHERE YEAR(MR.created_at) = 2020 AND MONTH(MR.created_at) = 2
 GROUP BY MR.movie_id
 ORDER BY AVG(MR.rating) DESC, M.title ASC
 LIMIT 1);