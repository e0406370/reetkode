"""
LCE 1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of English uppercase letters.

Topics:
- Math
- String
"""


class Solution:

    # Time Complexity: O(m + n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.61 MB -> 92.10%
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check that concatenating str1 to str2 is the same as concatenating str2 to str1
        if str1 + str2 != str2 + str1:
            return ""

        # determine the shorter and longer strings
        if len(str1) < len(str2):
            shorter = str1
            longer = str2
        else:
            shorter = str2
            longer = str1

        len_shorter, len_longer = len(shorter), len(longer)

        for i in range(len_shorter + 1, -1, -1):

            # retrieve the greatest common divisor between the length of str1 and str2
            if len_shorter % i == 0 and len_longer % i == 0:
                return shorter[:i]

        return ""

    # Time Complexity: O(m + n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.86 MB -> 49.41%
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # check that concatenating str1 to str2 is the same as concatenating str2 to str1
        if str1 + str2 != str2 + str1:
            return ""

        # retrieve the greatest common divisor between the length of str1 and str2
        div = math.gcd(len(str1), len(str2))

        return str1[:div]


"""
  methods:
  1. retrieve gcd by iteration from the back
  2. retrieve gcd by using in-built method
"""
