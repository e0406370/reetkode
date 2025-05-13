"""
LCE 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

Topics:
- Hash Table
- Math
- String
"""


class Solution:

    # Time Complexity: O(n) - 4 ms -> 65.06%
    # Space Complexity: O(1) - 17.92 MB -> 21.24%
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        exceptions = {
            ("I", "V"),
            ("I", "X"),
            ("X", "L"),
            ("X", "C"),
            ("C", "D"),
            ("C", "M"),
        }

        res = roman_map[s[0]]
        for i in range(1, len(s)):
            prev, curr = s[i - 1], s[i]

            if (prev, curr) in exceptions:
                res -= roman_map[prev]
                res += roman_map[curr] - roman_map[prev]

            else:
                res += roman_map[curr]

        return res

    # Time Complexity: O(n) - 1 ms -> 88.04%
    # Space Complexity: O(1) - 17.82 MB -> 40.75%
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }

        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                res -= roman_map[s[i]]

            else:
                res += roman_map[s[i]]

        return res


"""
  methods:
  1. using tuples(prev, curr) to check for exceptions
  2. cleaner approach
"""
