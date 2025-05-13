"""
LCM 2657. Find the Prefix Common Array of Two Arrays

You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Constraints:
- 1 <= A.length == B.length == n <= 50
- 1 <= A[i], B[i] <= n
- It is guaranteed that A and B are both a permutation of n integers.

Topics:
- Array
- Hash Table
- Bit Manipulation
"""


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_A = set()
        seen_B = set()

        n = len(A)
        C = [0] * n
        prefix_cnt = 0
        for i in range(n):
            curr_A = A[i]
            curr_B = B[i]

            seen_A.add(curr_A)
            seen_B.add(curr_B)

            if curr_A in seen_B:
                prefix_cnt += 1

            if curr_B in seen_A and curr_A != curr_B:
                prefix_cnt += 1

            C[i] = prefix_cnt

        return C


# Time Complexity: O(n) - 2 ms -> 94.32%
# Space Complexity: O(n) - 17.80 MB -> 65.02%
