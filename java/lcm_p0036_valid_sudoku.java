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
import java.util.Set;

class Solution {

  // Time Complexity: O(1) - 3 ms -> 55.29%
  // Space Complexity: O(1) - 44.58 MB -> 42.64%
  public boolean isValidSudoku(char[][] board) {

    HashSet<Character> rowSet = new HashSet<>();
    HashSet<Character> columnSet = new HashSet<>();
    HashMap<Integer, HashSet<Character>> squareMap = new HashMap<>();

    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        char rowNum = board[i][j];
        char columnNum = board[j][i];
        int squareIdx = (i / 3) * 3 + (j / 3);

        if (rowNum != '.') {
          if (rowSet.contains(rowNum) || squareMap.computeIfAbsent(squareIdx, k -> new HashSet<>()).contains(rowNum)) {
            return false;
          }

          rowSet.add(rowNum);
          squareMap.get(squareIdx).add(rowNum);
        }

        if (columnNum != '.') {
          if (columnSet.contains(columnNum)) {
            return false;
          }

          columnSet.add(columnNum);
        }
      }

      rowSet.clear();
      columnSet.clear();
    }

    return true;
  }

  // Time Complexity: O(1) - 2 ms -> 78.69%
  // Space Complexity: O(1) - 44.45 MB -> 50.83%
  @SuppressWarnings("unchecked")
  public boolean isValidSudokuAlt(char[][] board) {

    Set<Character>[] rows = new Set[9];
    Set<Character>[] columns = new Set[9];
    Set<Character>[] squares = new Set[9];
    for (int i = 0; i < 9; i++) {
      rows[i] = new HashSet<>();
      columns[i] = new HashSet<>();
      squares[i] = new HashSet<>();
    }

    for (int rowIdx = 0; rowIdx < 9; rowIdx++) {
      for (int colIdx = 0; colIdx < 9; colIdx++) {
        char currNum = board[rowIdx][colIdx];
        int squareIdx = (rowIdx / 3) * 3 + (colIdx / 3);

        if (currNum == '.') {
          continue;
        }

        if (rows[rowIdx].contains(currNum) || columns[colIdx].contains(currNum) || squares[squareIdx].contains(currNum)) {
          return false;
        }
        else {
          rows[rowIdx].add(currNum);
          columns[colIdx].add(currNum);
          squares[squareIdx].add(currNum);
        }
      }
    }

    return true;
  }
}

/*
  methods:
  1. hash set - rows, hash set - columns, hash map - squares 
  2. hash set arrays - all (most optimal method)
*/