/*
  LCE 268. Missing Number

  Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

  Constraints:
  - n == nums.length
  - 1 <= n <= 10^4
  - 0 <= nums[i] <= n
  - All the numbers of nums are unique.

  Topics: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
*/

class Solution {

  /*
    - XOR is commutative: A ^ B = B ^ A
    - XOR is associative: (A ^ B) ^ C = A ^ (B ^ C)
    - XORing something twice removes it: A ^ A = 0
    - XORing with zero does nothing: A ^ 0 = A
  */
  
  public int missingNumber(int[] nums) {

    int n = nums.length;

    int firstSumXOR = 0;
    int secondSumXOR = 0;

    // e.g. all in [0, n] => [0, 1, 2, 3]
    for (int i = 0; i <= n; i++) {
      firstSumXOR ^= i;
    }

    // e.g. nums =>  [3, 0, 1]
    for (int num : nums) {
      secondSumXOR ^= num;
    }

    return firstSumXOR ^ secondSumXOR; // 2
  }
}

// Time Complexity: O(n) - 0 ms -> 100.00%
// Space Complexity: O(1) - 45.26 MB -> 40.66%