"""
LCE 3498. Reverse Degree of a String

Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:
1. For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
2. Sum these products for all characters in the string.

Return the reverse degree of s.

Constraints:
- 1 <= s.length <= 1000
- s contains only lowercase English letters.

Topics:
- String
- Simulation
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        len_s = len(s)
        base_a = ord("a")

        reverse_degree = 0
        for i in range(len_s):
            reverse_degree += (i + 1) * (26 - (ord(s[i]) - base_a))

        return reverse_degree


# Time Complexity: O(n) - 3 ms -> 98.44%
# Space Complexity: O(1) - 17.88 MB -> 36.81%
