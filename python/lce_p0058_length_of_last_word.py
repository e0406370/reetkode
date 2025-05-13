"""
LCE 58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Constraints:
- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.

Topics:
- String
"""


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.95 MB -> 17.42%
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        return len(words[-1])

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.91 MB -> 17.42%
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break

            res += 1

        return res

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.78 MB -> 60.85%
    def lengthOfLastWord(self, s: str) -> int:
        have_skip_last = False

        res = 0
        for i in range(len(s) - 1, -1, -1):
            if not have_skip_last:
                if s[i] != " ":
                    res = 1
                    have_skip_last = True

            else:
                if s[i] == " ":
                    break

                res += 1

        return res


"""
  methods:
  1. using in-built strip() and split()
  2. using strip() only, iterate from back
  3. no strip() or split(), iterate from back
"""
