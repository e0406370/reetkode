/*
  LCE 1652. Defuse the Bomb

  You have a bomb to defuse, and your time is running out!
  Your informer will provide you with a circular array code of length of n and a key k.

  To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
  - If k > 0, replace the ith number with the sum of the next k numbers.
  - If k < 0, replace the ith number with the sum of the previous k numbers.
  - If k == 0, replace the ith number with 0.

  As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
  Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

  Constraints:
  - n == code.length
  - 1 <= n <= 100
  - 1 <= code[i] <= 100
  - -(n - 1) <= k <= n - 1

  Topics: 
  - Array
  - Sliding Window
*/

class Solution {
  public int[] decrypt(int[] code, int k) {
    int n = code.length;
    int[] temp = code.clone();

    for (int i = 0; i < n; i++) {
      if (k == 0) {
        code[i] = 0;
      }
      if (k > 0) {
        code[i] = getSumOfNextNums(temp, i + 1, k);
      }
      if (k < 0) {
        code[i] = getSumOfPreviousNums(temp, i - 1, k);
      }
    }

    return code;
  }

  private int getSumOfNextNums(int[] arr, int idx, int k) {
    int sum = 0;
    k = Math.abs(k);

    while (k != 0) {
      if (idx == arr.length) {
        idx = 0;
      }

      sum += arr[idx];

      idx++;
      k--;
    }

    return sum;
  }

  private int getSumOfPreviousNums(int[] arr, int idx, int k) {
    int sum = 0;
    k = Math.abs(k);

    while (k != 0) {
      if (idx == -1) {
        idx = arr.length - 1;
      }

      sum += arr[idx];

      idx--;
      k--;
    }

    return sum;
  }
}

// Time Complexity: O(n * k) - 1 ms -> 53.04%
// Space Complexity: O(n) - 42.11 MB -> 54.19%