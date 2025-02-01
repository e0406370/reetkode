/*
  LCM 46. Permutations

  Given an array nums of distinct integers, return all the possible permutations.
  You can return the answer in any order.

  Constraints:
  - 1 <= nums.length <= 6
  - -10 <= nums[i] <= 10
  - All the integers of nums are unique.

  Topics: 
  - Array
  - Backtracking
*/

import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<List<Integer>> permute(int[] nums) {
    
    int n = nums.length;
    List<List<Integer>> perms = new ArrayList<>();
    List<Integer> perm = new ArrayList<>();

    backtrack(nums, n, perms, perm);

    return perms;
  }

  private void backtrack(int[] nums, int n, List<List<Integer>> perms, List<Integer> perm) {
    
    // base case
    if (perm.size() == n) {
      perms.add(new ArrayList<>(perm));
      
      return;
    }

    for (int i = 0; i < n; i++) {
      int num = nums[i];
      
      if (perm.contains(num)) {
        continue;
      }

      perm.add(num);

      backtrack(nums, n, perms, perm);

      perm.remove(perm.size() - 1);
    }
  }
}

// Time Complexity: O(n!) - 2 ms -> 44.07%
// Space Complexity: O(n) - 44.97 MB -> 7.24%