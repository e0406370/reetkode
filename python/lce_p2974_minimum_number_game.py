"""
LCE 2974. Minimum Number Game

You are given a 0-indexed integer array nums of even length and there is also an empty array arr.
Alice and Bob decided to play a game where in every round Alice and Bob will do one move.

The rules of the game are as follows:
- Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
- Now, first Bob will append the removed element in the array arr, and then Alice does the same.
- The game continues until nums becomes empty.

Return the resulting array arr.

Constraints:
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 100
- nums.length % 2 == 0

Topics:
- Array,
- Sorting,
- Heap (Priority Queue),
- Simulation
"""


class Solution:

    # Time Complexity: O(n^2) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.50 MB -> 98.59%
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []

        while nums:
            min_alice = min(nums)
            nums.remove(min_alice)

            min_bob = min(nums)
            nums.remove(min_bob)

            arr.append(min_bob)
            arr.append(min_alice)

        return arr

    # Time Complexity: O(n log n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 17.87 MB -> 36.90%
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []

        for i in range(1, len(nums), 2):
            arr.append(nums[i])
            arr.append(nums[i - 1])

        return arr


"""
  methods:
  1. min() => O(n), remove => O(n), O(n) + O(n - 2) + O(n - 4) + ... + O(2) = O(n ^ 2)
  2. sort nums in ascending orders first to retrieve minimum
"""
