"""
  LCE 2283. Check if Number Has Equal Digit Count and Digit Value

  You are given a 0-indexed string num of length n consisting of digits.

  Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

  Constraints:
  - n == num.length
  - 1 <= n <= 10
  - num consists of digits.

  Topics:
  - Hash Table
  - String
  - Counting
"""

from collections import Counter


class Solution:

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(1) - 17.89 MB -> 30.20%
    def digitCount(self, num: str) -> bool:
        freq_arr = [0] * 10
        for d in num:
            freq_arr[int(d)] += 1

        for i in range(len(num)):
            if int(num[i]) != freq_arr[i]:
                return False

        return True

    # Time Complexity: O(n) - 0 ms -> 100.00%
    # Space Complexity: O(n) - 18.04 MB -> 14.67%
    def digitCountAlt(self, num: str) -> bool:
        ctr = Counter(num)

        for i in range(len(num)):
            if int(num[i]) != ctr[str(i)]:
                return False

        return True


"""
  methods:
  1. frequency array
  2. in-built counter
"""
