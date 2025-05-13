"""
LCE 3461. Check If Digits Are Equal in String After Operations I

You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
- For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
- Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.

Return true if the final two digits in s are the same; otherwise, return false.

Constraints:
- 3 <= s.length <= 100
- s consists of only digits.

Topics:
- Math 
- String 
- Simulation 
- Combinatorics 
- Number Theory
"""


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while (n := len(s)) != 2:
            s = "".join(
                (str((int(s[i - 1]) + int(s[i])) % 10) for i in range(1, n))
            )

        return s[0] == s[1]


# Time Complexity: O(n^2) - 89 ms -> 60.70%
# Space Complexity: O(n) - 17.62 MB -> 94.79%
