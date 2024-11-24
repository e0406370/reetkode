/*
  LCM 36. Valid Sudoku

  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
  1. Each row must contain the digits 1-9 without repetition.
  2. Each column must contain the digits 1-9 without repetition.
  3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
  
  Note:
  - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  - Only the filled cells need to be validated according to the mentioned rules.

  Constraints:
  - board.length == 9
  - board[i].length == 9
  - board[i][j] is a digit 1-9 or '.'.

  Topics: 
  - Array 
  - Hash Table 
  - Matrix
*/

import java.util.HashMap;
import java.util.HashSet;

class Solution {

  // Time Complexity: O(1) - 6 ms -> 30.63%
  // Space Complexity: O(1) - 44.33 MB -> 59.89%
  public boolean isValidSudoku(char[][] board) {

    HashSet<Character> rowSet = new HashSet<>();
    HashSet<Character> columnSet = new HashSet<>();
    HashMap<Integer, HashSet<Character>> squareMap = new HashMap<>();

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        char rowNum = board[i][j];
        char columnNum = board[j][i];
        int squareIdx = (i / 3) * 3 + (j / 3);

        if (rowSet.contains(rowNum)) {
          return false;
        }
        if (columnSet.contains(columnNum)) {
          return false;
        }
        if (squareMap.containsKey(squareIdx) && squareMap.get(squareIdx).contains(rowNum)) {
          return false;
        }

        if (rowNum != '.') {
          rowSet.add(rowNum);
          squareMap.computeIfAbsent(squareIdx, k -> new HashSet<>()).add(rowNum);
        }
        if (columnNum != '.') {
          columnSet.add(columnNum);
        }
      }

      rowSet.clear();
      columnSet.clear();
    }

    return true;
  }
}