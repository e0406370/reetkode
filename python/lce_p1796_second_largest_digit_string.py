"""
LCE 1796. Second Largest Digit in a String

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters.

Topics:
- Hash Table
- String
"""


class Solution:

    # Time Complexity: O(n) - 43 ms -> 5.80%
    # Space Complexity: O(1) - 16.49 MB -> 100.00%
    def secondHighest(self, s: str) -> int:

        digits = sorted({int(x) for x in s if x.isdigit()}, reverse=True)

        if len(digits) < 2:
            return -1
        else:
            return digits[1]

    # Time Complexity: O(n) - 5 ms -> 31.63%
    # Space Complexity: O(1) - 17.85 MB -> 34.94%
    def secondHighest(self, s: str) -> int:
        first_highest = -1
        second_highest = -1

        N = len(s)
        for i in range(N):
            curr = s[i]

            if curr.isdigit():
                curr = int(curr)

                if curr > first_highest:
                    second_highest = first_highest
                    first_highest = curr

                elif first_highest > curr and curr > second_highest:
                    second_highest = curr

        return second_highest


"""
  methods:
  1. use sorted set and filter for digits
  2. use 2 variables (first_highest, second_highest)
"""
