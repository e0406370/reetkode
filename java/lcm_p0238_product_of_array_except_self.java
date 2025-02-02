/*
  LCM 238. Product of Array Except Self

  Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

  You must write an algorithm that runs in O(n) time and without using the division operation.

  Constraints:
  - 2 <= nums.length <= 105
  - -30 <= nums[i] <= 30
  - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

  Topics: 
  - Array
  - Prefix Sum
*/

class Solution {

  // Time Complexity: O(n) - 1 ms -> 99.63%
  // Space Complexity: O(n) - 55.1 MB -> 88.07%
  public int[] productExceptSelf(int[] nums) {

    int n = nums.length;

    int[] res = new int[n];
    for (int i = 0; i < n; i++) res[i] = 1;

    int prefixProd = nums[0];
    for (int i = 1; i < n; i++) {
      res[i] *= prefixProd;
      prefixProd *= nums[i];
    }

    int suffixProd = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      res[i] *= suffixProd;
      suffixProd *= nums[i];
    }

    return res;
  }

  // Time Complexity: O(n) - 2 ms -> 88.73%
  // Space Complexity: O(n) - 56.3 MB -> 12.09%
  public int[] productExceptSelfAlt1(int[] nums) {

    int n = nums.length;
    int[] answer = new int[n];

    int[] first = new int[n];
    first[0] = 1;
    for (int i = 1; i < n; i++) {
      first[i] = nums[i - 1] * first[i - 1];
    }

    int[] second = new int[n];
    second[n - 1] = 1;
    for (int j = n - 2; j >= 0; j--) {
      second[j] = nums[j + 1] * second[j + 1];
    }

    for (int k = 0; k < n; k++) {
      answer[k] = first[k] * second[k];
    }

    return answer;
  }

  // Time Complexity: O(n^2) - TLE
  // Space Complexity: O(n) - TLE
  public int[] productExceptSelfAlt2(int[] nums) {

    int n = nums.length;
    int[] ans = new int[n];

    for (int i = 0; i < n; i++) {
      int prod = 1;

      for (int j = 0; j < n; j++) {
        if (i != j) {
          prod *= nums[j];
        }
      }

      ans[i] = prod;
    }

    return ans;
  }
}

/*
  methods:
  1. prefix prod & suffix prod - 1 result arr
  2. prefix prod & suffix prod - 1 result arr + prefix arr + suffix arr
  3. brute force 
*/