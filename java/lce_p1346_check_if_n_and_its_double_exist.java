/*
  LCE 1346. Check If N and Its Double Exist

  Given an array arr of integers, check if there exist two indices i and j such that :

  - i != j
  - 0 <= i, j < arr.length
  - arr[i] == 2 * arr[j]

  Constraints:
  - 2 <= arr.length <= 500
  - -10^3 <= arr[i] <= 10^3

  Topics: 
  - Array 
  - Hash Table 
  - Two Pointers 
  - Binary Search 
  - Sorting
*/

import java.util.HashSet;
import java.util.Set;

class Solution {

  // Time Complexity: O(n) - 2 ms -> 90.34%
  // Space Complexity: O(n) - 43.17 MB -> 50.69%
  public boolean checkIfExist(int[] arr) {

    Set<Integer> seen = new HashSet<>();
    for (int i = 0; i < arr.length; i++) {
      int curr = arr[i];

      if (seen.contains(curr * 2)) {
        return true;
      }
      else if (curr % 2 == 0 && seen.contains(curr / 2)) {
        return true;
      }
      else {
        seen.add(curr);
      }
    }

    return false;
  }
  
  // Time Complexity: O(n^2) - 3 ms -> 27.12%
  // Space Complexity: O(1) - 43.14 MB -> 50.69%
  public boolean checkIfExistAlt(int[] arr) {

    for (int i = 0; i < arr.length; i++) {
      for (int j = i + 1; j < arr.length; j++) {
        if (arr[i] * 2 == arr[j]) {
          return true;
        }
        if (arr[i] % 2 == 0 && arr[i] / 2 == arr[j]) {
          return true;
        }
      }
    }

    return false;
  }
}

/*
  methods:
  1. set lookup
  2. brute force
*/