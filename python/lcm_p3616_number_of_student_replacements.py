"""
LCM 3616. Number of Student Replacements (Premium)

You are given an integer array ranks where ranks[i] represents the rank of the ith student arriving in order. A lower number indicates a better rank.

Initially, the first student is selected by default.

A replacement occurs when a student with a strictly better rank arrives and replaces the current selection.

Return the total number of replacements made.

Constraints:
- 1 <= ranks.length <= 10^5​​​​
- 1 <= ranks[i] <= 10^5

Topics:
- Array
- Simulation
"""


class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:
        curr = ranks[0]
        ctr = 0

        for i in range(1, len(ranks)):
            if ranks[i] < curr:
                curr = ranks[i]
                ctr += 1

        return ctr


# Time Complexity: O(n) - 37 ms -> 24.00%
# Space Complexity: O(1) - 28.70 MB -> 58.40%
