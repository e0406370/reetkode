/*
  LCM 128. Longest Consecutive Sequence

  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

  You must write an algorithm that runs in O(n) time.

  Constraints:
  - 0 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9

  Topics: 
  - Array
  - Hash Table
  - Union Find
*/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {

  // Time Complexity: O(n) - 1105 ms -> 19.98%
  // Space Complexity: O(n) - 66.0 MB -> 53.50%
  public int longestConsecutive(int[] nums) {

    int maxLength = 0;
    int currLength = 0;

    Set<Integer> set = new HashSet<>();
    for (int num : nums) set.add(num);

    for (int num : nums) {

      // process only starting numbers
      if (!set.contains(num - 1)) {
        currLength = 0;

        while (set.contains(num++)) {
          currLength++;
        }

        maxLength = Math.max(currLength, maxLength);
      }
    }

    return maxLength;
  }

  // Time Complexity: O(n log n) - 16 ms -> 91.59%
  // Space Complexity: O(1) - 56.8 MB -> 81.76%
  public int longestConsecutiveAlt(int[] nums) {

    int n = nums.length;
    if (n == 0 || n == 1) {
      return n;
    }

    int maxLength = 1;
    int currLength = 1;

    Arrays.sort(nums);
    int prevNum = nums[0];

    for (int i = 1; i < n; i++) {

      // check for consecutive numbers
      if (nums[i] == prevNum + 1) {
        currLength++;
      }
      // check if curr num is not a dupe of the prev num
      else if (nums[i] != prevNum) {
        currLength = 1;
      }

      prevNum = nums[i];
      maxLength = Math.max(currLength, maxLength);
    }

    return maxLength;
  }
}

/*
  methods:
  1. hash set - process only the starting numbers, then build the sequences
  2. sorting - check all possible sequences
*/