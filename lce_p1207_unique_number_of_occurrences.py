"""
LCE 1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000

Topics:
- Array
- Hash Table
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)

        return len(set(cnt.values())) == len(set((cnt.keys())))
