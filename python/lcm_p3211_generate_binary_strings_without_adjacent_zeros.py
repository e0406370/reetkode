"""
LCM 3211. Generate Binary Strings Without Adjacent Zeros

You are given a positive integer n.

A binary string x is valid if all substrings of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

Constraints:
- 1 <= n <= 18

Topics:
- String
- Backtracking
- Bit Manipulation
"""


class Solution:
    def dfs(self, size: int, s: str, lst: list) -> List[str]:
        if size == len(s):
            lst.append(s)
            return

        for i in range(2):
            if i == 0 and s and s[-1] == "0":
                continue

            self.dfs(size, s + str(i), lst)

        return lst

    def validStrings(self, n: int) -> List[str]:
        return self.dfs(n, "", [])


# Time Complexity: O(2^n) - 63 ms -> 26.49%
# Space Complexity: O(2^n) - 19.08 MB -> 83.41%