"""
LCE 3491. Phone Number Prefix (Premium)

You are given a string array numbers that represents phone numbers.

Return true if no phone number is a prefix of any other phone number; otherwise, return false.

Constraints:
- 2 <= numbers.length <= 50
- 1 <= numbers[i].length <= 50
- All numbers contain only digits '0' to '9'.

Topics:
- Array
- Math
"""


class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        # sort numbers lexographically
        numbers.sort()

        for i in range(1, len(numbers)):
            if numbers[i].startswith(numbers[i - 1]):
                return False

        return True


# Time Complexity: O(n log n) - 3 ms -> 100.00%
# Space Complexity: O(1) - 17.98 MB -> 45.50%
