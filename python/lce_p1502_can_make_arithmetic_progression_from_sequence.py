"""
  LCE 1502. Can Make Arithmetic Progression From Sequence

  A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

  Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

  Constraints:
  - 2 <= arr.length <= 1000
  - 10^6 <= arr[i] <= 10^6

  Topics:
  - Array
  - Sorting
"""


class Solution:
  
    # Time Complexity: O(n log n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.80 MB -> 84.66%
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True

    # Time Complexity: O(n) - 3 ms -> 19.68%
    # Space Complexity: O(n) - 17.96 MB -> 35.66%  
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        num_set = set(arr)

        len_arr = len(arr)
        len_set = len(num_set)

        # only 1 element in set
        # => all elements are equal, arr can be AP
        if len_set == 1:
            return True

        # no. of elements in set < no. of elements in arr
        # => some elements are equal and some are not, arr cannot be AP
        if len_set < len_arr:
            return False

        min_num = 10 ** 6
        max_num = -10 ** 6
        for num in arr:
            min_num = min(num, min_num)
            max_num = max(num, max_num)

        diff = (max_num - min_num) // (len_arr - 1)

        # skip checking min_num and max_num
        for i in range(min_num + diff, max_num, diff):
            if i not in num_set:
                return False

        return True


"""
  methods:
  1. sorting: viable method due to 2 <= arr.length <= 1000 constraint
  2. use d = (first_ele + last_ele) / (arr_size - 1) then check each iteration in range(first_ele + diff, last_ele, diff) exists in arr
"""