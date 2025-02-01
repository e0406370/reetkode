/*
  LCE 3340. Check Balanced String

  You are given a string num consisting of only digits. 
  A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

  Return true if num is balanced, otherwise return false.

  Constraints:
  - 2 <= num.length <= 100
  - num consists of digits only

  Topics: 
  - String
*/

class Solution {
  public boolean isBalanced(String num) {

    int evenSum = 0;
    int oddSum = 0;

    for (int i = 0; i < num.length(); i++) {
      int digit = num.charAt(i) - '0';

      if (i % 2 == 0) {
        evenSum += digit;
      }
      else {
        oddSum += digit;
      }
    }
    
    return evenSum == oddSum;
  }
}

// Time Complexity: O(n) - 1 ms -> 99.36%
// Space Complexity: O(1) - 41.85 MB -> 92.55%