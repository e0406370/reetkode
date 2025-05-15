"""
LCE 2124. Check if All A's Appears Before All B's

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string.
Otherwise, return false.

Constraints:
- 1 <= s.length <= 100
- s[i] is either 'a' or 'b'.

Topics:
- String
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.65 MB -> 38.67%
    def checkString(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True

        max_idx_a = s.find("a")
        min_idx_b = s.find("b")
        if max_idx_a == -1 or min_idx_b == -1:
            return True

        for i in range(n):
            if s[i] == "a":
                max_idx_a = i

        return max_idx_a < min_idx_b

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.69 MB -> 38.67%
    def checkStringAlt(self, s: str) -> bool:
        return s.find("ba") == -1


"""
  methods:
  1. checking latest a must appear before earliest b (from left to right)
  2. checking no occurrences of "ba" as substring
"""
