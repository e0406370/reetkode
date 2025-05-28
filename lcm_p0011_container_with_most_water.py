"""
LCM 11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

Topics:
- Array
- Two Pointers
- Greedy
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_water = 0

        while left_ptr < right_ptr:
            left_height = height[left_ptr]
            right_height = height[right_ptr]

            temp_water = min(left_height, right_height) * (right_ptr - left_ptr)
            max_water = max(temp_water, max_water)

            if left_height < right_height:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_water


# Time Complexity: O(n) - 106 ms -> 42.00%
# Space Complexity: O(1) - 28.36 MB -> 90.40%
