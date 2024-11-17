/*
  LCM 17. Letter Combinations of a Phone Number

  Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
  Return the answer in any order.

  A mapping of digits to letters (just like on the telephone buttons) is given below.
  Note that 1 does not map to any letters.

  Constraints:
  - 0 <= digits.length <= 4
  - digits[i] is a digit in the range ['2', '9'].

  Topics: 
  - Hash Table 
  - String
  - Backtracking
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
  public List<String> letterCombinations(String digits) {

    if (digits.isEmpty()) {
      return new ArrayList<>();
    }

    Map<Integer, Character[]> digitToLetterMap = new HashMap<>();
    digitToLetterMap.put(2, new Character[] { 'a', 'b', 'c' });
    digitToLetterMap.put(3, new Character[] { 'd', 'e', 'f' });
    digitToLetterMap.put(4, new Character[] { 'g', 'h', 'i' });
    digitToLetterMap.put(5, new Character[] { 'j', 'k', 'l' });
    digitToLetterMap.put(6, new Character[] { 'm', 'n', 'o' });
    digitToLetterMap.put(7, new Character[] { 'p', 'q', 'r', 's' });
    digitToLetterMap.put(8, new Character[] { 't', 'u', 'v' });
    digitToLetterMap.put(9, new Character[] { 'w', 'x', 'y', 'z' });

    List<String> combinations = new ArrayList<>();
    StringBuilder sb = new StringBuilder();

    backtrack(digits, digitToLetterMap, combinations, sb, 0);

    return combinations;
  }

  private void backtrack(String str, Map<Integer, Character[]> mp, List<String> lst, StringBuilder sb, int idx) {

    // base case
    if (idx == str.length()) {
      lst.add(sb.toString());

      return;
    }

    int digit = str.charAt(idx) - '0';
    for (char ch : mp.get(digit)) {
      sb.append(ch);

      backtrack(str, mp, lst, sb, idx + 1);

      sb.deleteCharAt(idx);
    }
  }
}

// n => no. of digits in the input string, k => average number of letters per digit
// Time Complexity: O(n * k^n) - 0 ms -> 100.00% 
// Space Complexity: O(n * k^n) - 41.72 MB -> 88.77%