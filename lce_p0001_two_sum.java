/*
  LCE 1. Two Sum

  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

  You can return the answer in any order.

  Constraints:
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - -10^9 <= target <= 10^9
  - Only one valid answer exists.

  Topics: 
  - Array
  - Hash Table
*/

import java.util.HashMap;
import java.util.Map;

class Solution {

  // Time Complexity: O(n) - 2 ms -> 98.88%
  // Space Complexity: O(n) - 44.8 MB -> 48.36%
  public int[] twoSum(int[] nums, int target) {

    Map<Integer, Integer> indexMap = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      int diff = target - num;

      if (indexMap.containsKey(diff)) {
        return new int[] { indexMap.get(diff), i };
      }

      indexMap.put(num, i);
    }

    return new int[] { -1, -1 };
  }

  // Time Complexity: O(n) - 4 ms -> 60.41%
  // Space Complexity: O(n) - 44.3 MB -> 97.08%
  public int[] twoSumAlt(int[] nums, int target) {

    int n = nums.length;
    Map<Integer, Integer> indexMap = new HashMap<>();

    for (int i = 0; i < n; i++) {
      indexMap.put(nums[i], i);
    }

    for (int i = 0; i < n; i++) {
      int num = nums[i];
      int diff = target - num;

      if (indexMap.containsKey(diff) && i != indexMap.get(diff)) {
        return new int[] { i, indexMap.get(diff) };
      }
    }

    return new int[] { -1, -1 };
  }
}

/*
  methods:
  1. hash map - single pass (i - larger index)
  2. hash map - double pass (i - smaller index)
*/