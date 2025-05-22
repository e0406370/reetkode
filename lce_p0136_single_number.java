/*
  LCE 136. Single Number

  Given a non-empty array of integers 'nums', every element appears twice except for one. 
  Find that single one. Must implement linear runtime complexity and constant extra space.

  Constraints:
  - 1 <= nums.length <= 3 * 10^4
  - -3 * 10^4 <= nums[i] <= 3 * 10^4
  - Each element in the array appears twice except for one element which appears only once.

  Topics: 
  - Array 
  - Bit Manipulation
*/

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

class Solution {

  /*
    - XOR is commutative: A ^ B = B ^ A
    - XOR is associative: (A ^ B) ^ C = A ^ (B ^ C)
    - XORing something twice removes it: A ^ A = 0
    - XORing with zero does nothing: A ^ 0 = A
  */

  // Time Complexity: O(n) - 1 ms -> 99.84%
  // Space Complexity: O(1) - 46.15 MB -> 33.01%
  public int singleNumber(int[] nums) {

    int singleNum = 0;

    for (int num : nums) {

      singleNum = singleNum ^ num; // making use of XOR (^) properties
    }

    return singleNum;
  }

  // Time Complexity: O(n) - 13 ms -> 20.07%
  // Space Complexity: O(n) - 44.72 MB -> 94.59%
  public int singleNumberAlt(int[] nums) {

    int singleNumber = 0;

    Map<Integer, Integer> numFreqs = new HashMap<>();

    for (int num : nums) {

      int currFreq = numFreqs.getOrDefault(num, 0);
      numFreqs.put(num, currFreq + 1);
    }

    for (Entry<Integer, Integer> entry : numFreqs.entrySet()) {

      if (entry.getValue() == 1) {
        singleNumber = entry.getKey();
        break;
      }
    }

    return singleNumber;
  }
}

/*
  methods:
  1. XOR properties (A ^ A = 0 and A ^ 0 = A) to filter the single number
  2. frequency map to find the single number
*/