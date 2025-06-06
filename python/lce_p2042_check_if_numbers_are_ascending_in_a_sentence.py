"""
LCE 2042. Check if Numbers Are Ascending in a Sentence

A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

Return true if so, or false otherwise.

Constraints:
- 3 <= s.length <= 200
- s consists of lowercase English letters, spaces, and digits from 0 to 9, inclusive.
- The number of tokens in s is between 2 and 100, inclusive.
- The tokens in s are separated by a single space.
- There are at least two numbers in s.
- Each number in s is a positive number less than 100, with no leading zeros.
- s contains no leading or trailing spaces.

Topics:
- String
"""


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split(" ")
        prev_num = 0

        for token in tokens:
            if token.isnumeric():
                if (curr_num := int(token)) <= prev_num:
                    return False

                prev_num = curr_num

        return True


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.92 MB -> 7.78%
