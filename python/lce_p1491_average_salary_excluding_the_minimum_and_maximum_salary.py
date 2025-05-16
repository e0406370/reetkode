"""
  LCE 1491. Average Salary Excluding the Minimum and Maximum Salary

  You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

  Return the average salary of employees excluding the minimum and maximum salary.
  Answers within 10-5 of the actual answer will be accepted.

  Constraints:
  - 3 <= salary.length <= 100
  - 1000 <= salary[i] <= 106
  - All the integers of salary are unique.

  Topics:
  - Array
  - Sorting
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        mini = 10**6
        maxi = 1000
        total = 0

        for sal in salary:
            mini = min(sal, mini)
            maxi = max(sal, maxi)
            total += sal

        total -= (mini + maxi)
        return total / (len(salary) - 2)


# Time Complexity: O(n) - 0 ms -> 100.00%
# Space Complexity: O(1) - 18.03 MB -> 23.14%
