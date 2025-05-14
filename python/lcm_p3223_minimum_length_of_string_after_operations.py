"""
LCM 3223. Minimum Length of String After Operations

You are given a string s.

You can perform the following process on s any number of times:

- Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
- Delete the closest occurrence of s[i] located to the left of i.
- Delete the closest occurrence of s[i] located to the right of i.

Return the minimum length of the final string s that you can achieve.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of lowercase English letters.

Topics:
- Hash Table
- String
- Counting
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        ctr = Counter(s)
        res = 0

        for v in ctr.values():
            res += 2 if v % 2 == 0 else 1

        return res


# Time Complexity: O(n) - 130 ms -> 92.82%
# Space Complexity: O(n) - 18.98 MB -> 22.33%
