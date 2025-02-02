"""
  LCE 3110. Score of a String

  You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

  Return the score of s.

  Constraints:
  - 2 <= s.length <= 100
  - s consists only of lowercase English letters.

  Topics:
  - String
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))

        return score


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 17.85 MB -> 24.26%
