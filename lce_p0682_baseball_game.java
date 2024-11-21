/*
  LCE 682. Baseball Game

  You are keeping the scores for a baseball game with strange rules. 
  At the beginning of the game, you start with an empty record.

  You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
  - An integer x.
    Record a new score of x.
  - '+'.
    Record a new score that is the sum of the previous two scores.
  - 'D'.
    Record a new score that is the double of the previous score.
  - 'C'.
    Invalidate the previous score, removing it from the record.
  
  Return the sum of all the scores on the record after applying all the operations.

  The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

  Constraints:
  - 1 <= operations.length <= 1000
  - operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
  - For operation "+", there will always be at least two previous scores on the record.
  - For operations "C" and "D", there will always be at least one previous score on the record.

  Topics: 
  - Array
  - Stack
  - Simulation
*/

import java.util.Stack;

class Solution {
  public int calPoints(String[] operations) {

    Stack<Integer> stack = new Stack<>();

    for (String opr : operations) {
      if (opr.equals("+")) {
        int lastElement = stack.pop();
        int secondLastElement = stack.peek();

        stack.add(lastElement);
        stack.add(secondLastElement + lastElement);
      } 
      else if (opr.equals("D")) {
        stack.add(stack.peek() * 2);
      } 
      else if (opr.equals("C")) {
        stack.pop();
      } 
      else {
        stack.add(Integer.parseInt(opr));
      }
    }

    int sum = 0;

    while (!stack.isEmpty()) {
      sum += stack.pop();
    }

    return sum;
  }
}

// Time Complexity: O(n) - 2 ms -> 93.51%
// Space Complexity: O(n) - 41.60 MB -> 59.50%