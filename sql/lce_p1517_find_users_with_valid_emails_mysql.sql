/*
  LCE 1517. Find Users With Valid E-Mails
  -> MySQL

  Table: Users

  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | user_id       | int     |
  | name          | varchar |
  | mail          | varchar |
  +---------------+---------+
  - user_id is the primary key (column with unique values) for this table.
  - This table contains information of the users signed up in a website. Some e-mails are invalid.

  Write a solution to find the users who have valid emails.

  A valid e-mail has a prefix name and a domain where:
  - The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. 
  - The prefix name must start with a letter.
  - The domain is '@leetcode.com'.

  Return the result table in any order.
*/

SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$'

/*
  - reference: https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/

  - ^ => marks start of string
  - [a-z] => matches any lower case letter
  - [A-Z] => matches any upper case letter
  - [0-9] => matches any digit from 0 through to 9
  - * => matches >= 0 instances of string preceding it
  - $ => marks end of string

  - note: [.] is explicitly used as . itself matches any single character!

 - In MySQL, REGEXP and RLIKE are synonymous operators used for performing regular expression matching. 
  The primary difference between REGEXP and RLIKE is that REGEXP is the standard operator, while RLIKE is just an alias for it.
*/