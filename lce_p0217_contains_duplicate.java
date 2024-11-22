/*
  LCE 217. Contains Duplicate

  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

  Constraints:
  - 1 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9

  Topics: 
  - Array
  - Hash Table
  - Sorting
*/

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

class Solution {

  // Time Complexity: O(n) - 10 ms -> 89.14%
  // Space Complexity: O(n) - 57.7 MB -> 65.77%
  public boolean containsDuplicate(int[] nums) {

    HashSet<Integer> seen = new HashSet<>();

    for (int num : nums) {
      if (seen.contains(num)) {
        return true;
      }

      seen.add(num);
    }

    return false;
  }

  // Time Complexity: O(n) - 30 ms -> 5.04%
  // Space Complexity: O(n) - 57.7 MB -> 69.61%
  public boolean containsDuplicateAlt1(int[] nums) {

    HashMap<Integer, Integer> freqMap = new HashMap<>();

    for (int num : nums) {
      freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
    }

    for (int num : freqMap.keySet()) {
      if (freqMap.get(num) > 1) {
        return true;
      }
    }

    return false;
  }

  // Time Complexity: O(n + max) - MLE
  // Space Complexity: O(max) = MLE
  public boolean containsDuplicateAlt2(int[] nums) {

    int max = 0;
    for (int num : nums) {
      num = Math.abs(num);
      max = (num > max) ? num : max;
    }

    int[] freqArr = new int[max * 2 + 1];
    for (int num : nums) {
      freqArr[num + max]++;
    }

    for (int freq : freqArr) {
      if (freq > 1) {
        return true;
      }
    }

    return false;
  }

  // Time Complexity: O(n log n) - 21 ms -> 9.55%
  // Space Complexity: O(1) - 55.7 MB 0> 74.54%
  public boolean containsDuplicateAlt3(int[] nums) {

    Arrays.sort(nums);

    for (int i = 0; i < nums.length - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        return true;
      }
    }

    return false;
  }

  // Time Complexity: O(n^2) - TLE
  // Space Complexity: O(1) - TLE
  public boolean containsDuplicateAlt4(int[] nums) {

    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] == nums[j]) {
          return true;
        }
      }
    }

    return false;
  }

  // Time Complexity: O(n) - 24 ms -> 5.41%
  // Space Complexity: O(n) - 58.5 MB -> 27.31%
  public boolean containsDuplicateAlt5(int[] nums) {

    return Arrays.stream(nums).distinct().count() < nums.length;
  }
}

/*
  methods:
  1. hash set (recommended)
  2. hash map (overkill due to extra overhead)
  3. frequency array (MLE, only works if constraints on nums[i] are minimal)
  4. sorting (not recommended due to O(n log n) runtime)
  5. brute force (TLE, only works if constraints on nums.length are minimal)
  6. streaming (compare hash set length and nums.length)
*/