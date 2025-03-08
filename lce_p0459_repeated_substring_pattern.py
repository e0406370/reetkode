"""
  LCE 459. Repeated Substring Pattern

  Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

  Constraints:
  - 1 <= s.length <= 10^4
  - s consists of lowercase English letters.

  Topics:
  - String
  - String Matching
"""


class Solution:

    # Time Complexity: O(n^2) - 81 ms -> 17.39%
    # Space Complexity: O(n) - 17.62 MB -> 96.11%
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(n // 2):
            pattern = s[: i + 1] * (n // (i + 1))

            if pattern == s:
                return True

        return False

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.79 MB -> 83.57%
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s * 2
        t = t[:-1]
        t = t[1:]

        return s in t


"""
  methods:
  1. using divisors: iterate over all prefix substrings of length i to n // 2 then concatenate each prefix n // i times
  2. advanced approach
"""
