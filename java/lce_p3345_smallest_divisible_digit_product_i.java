/*
  LCE 3345. Smallest Divisible Digit Product I

  You are given two integers n and t.
  Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

  Constraints:
  - 1 <= n <= 100
  - 1 <= t <= 10

  Topics: 
  - Math
  - Enumeration
*/

class Solution {
  public int smallestNumber(int n, int t) {

    while (getDigitsProduct(n) % t != 0) {
      n++;
    }
    
    return n;
  }

  private int getDigitsProduct(int num) {
    
    int prod = 1;

    while (num > 0) {
      prod *= (num % 10);
      num /= 10;
    }

    return prod;
  }
}

// Time Complexity: O(k * log(n)) - 1 ms -> 100.00%
// Space Complexity: O(1) - 41.31 MB -> 7.58%