/*
  LCM 1829. Maximum XOR for Each Query

  You are given a sorted array nums of n non-negative integers and an integer maximumBit.

  You want to perform the following query n times:
  1. Find a non-negative integer k < 2^maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
  2. Remove the last element from the current array nums.

  Return an array answer, where answer[i] is the answer to the ith query.

  Constraints:
  - nums.length == n
  - 1 <= n <= 105
  - 1 <= maximumBit <= 20
  - 0 <= nums[i] < 2^maximumBit
  - nums​​​ is sorted in ascending order.

  Topics: 
  - Array
  - Bit Manipulation
  - Prefix Sum
*/

class Solution {
  public int[] getMaximumXor(int[] nums, int maximumBit) {

    int n = nums.length;

    // ∵ k < 2 ^ maximumBit
    int maximumK = (int) Math.pow(2, maximumBit) - 1;

    // create prefix XOR array (must be in reverse order, as per description)
    int[] prefXORArr = new int[n];
    prefXORArr[n - 1] = nums[0];
    for (int i = 1; i < n; i++) {
      prefXORArr[n - 1 - i] = prefXORArr[n - i] ^ nums[i];
    }
 
    // derive k for each prefXORArr[i] by making use of a ^ b = c <=> a ^ c = b property
    for (int i = n - 1; i >= 0; i--) {
      prefXORArr[i] ^= maximumK;
    }

    return prefXORArr;
  }
}

// Time Complexity: O(n) - 3 ms -> 53.17%
// Space Complexity: O(n) - 58.70 MB -> 69.25%