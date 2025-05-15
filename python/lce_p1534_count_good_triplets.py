"""
LCE 1534. Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c
where |x| denotes the absolute value of x.

Return the number of good triplets.

Constraints:
- 3 <= arr.length <= 100
- 0 <= arr[i] <= 1000
- 0 <= a, b, c <= 1000

Topics:
- Array
- Enumeration
"""


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_triplets = 0
        n = len(arr)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:

                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_triplets += 1

        return good_triplets


# Time Complexity: O(n^3) - 178 ms -> 76.35%
# Space Complexity: O(1) - 17.77 MB -> 61.28%
