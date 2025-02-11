"""
  LCE 3174. Clear Digits

  You are given a string s.

  Your task is to remove all digits by doing this operation repeatedly:
  - Delete the first digit and the closest non-digit character to its left.
  
  Return the resulting string after removing all digits.

  Constraints:
  - 1 <= s.length <= 100
  - s consists only of lowercase English letters and digits.
  - The input is generated such that it is possible to delete all digits.

  Topics:
  - String
  - Stack
  - Simulation
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i].isdigit():
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(n) - 17.85 MB -> 27.74%
