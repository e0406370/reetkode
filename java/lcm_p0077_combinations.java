/*
  LCM 77. Combinations

  Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
  You may return the answer in any order.

  Constraints:
  - 1 <= n <= 20
  - 1 <= k <= n

  Topics:
  - Backtracking
*/

import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<List<Integer>> combine(int n, int k) {

    List<List<Integer>> combs = new ArrayList<>();

    backtrack(combs, new ArrayList<>(), n, k, 1);

    return combs;
  }

  private void backtrack(List<List<Integer>> combs, List<Integer> comb, int n, int k, int start) {

    // base case
    if (comb.size() == k) {
      combs.add(new ArrayList<>(comb));

      return;
    }

    for (int i = start; i <= n; i++) {
      comb.add(i);

      backtrack(combs, comb, n, k, i + 1); // i + 1 ∵ to skip previous index for subsequent iteration, in order to prevent duplicate combinations

      comb.remove(comb.size() - 1);
    }
  }
}

// Time Complexity: O(k * n C k) - 23 ms -> 25.33%
// Space Complexity: O(k + k * n C k) - 94.63 MB -> 32.29%