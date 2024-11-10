/*
  LCE 2490. Circular Sentence

  A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
  - For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
  
  Words consist of only uppercase and lowercase English letters.
  Uppercase and lowercase English letters are considered different.

  A sentence is circular if:
  - The last character of a word is equal to the first character of the next word.
  - The last character of the last word is equal to the first character of the first word.
  For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
  However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

  Given a string sentence, return true if it is circular. Otherwise, return false.

  Constraints:
  - 1 <= sentence.length <= 500
  - sentence consist of only lowercase and uppercase English letters and spaces.
  - The words in sentence are separated by a single space.
  - There are no leading or trailing spaces.

  Topics: 
  - String
*/

class Solution {
  public boolean isCircularSentence(String sentence) {
      
    String[] words = sentence.split(" ");
    int n = words.length;

    // The last character of a word is equal to the first character of the next word.
    boolean condition1 = true;
    for (int i = 0; i < n - 1; i++) {
      if (words[i].charAt(words[i].length() - 1) != words[i + 1].charAt(0)) {
        condition1 = false;
        break;
      }
    }

    // The last character of the last word is equal to the first character of the first word.
    boolean condition2 = true;
    condition2 = words[n - 1].charAt(words[n - 1].length() - 1) == words[0].charAt(0);

    return (n == 1) ? condition2 : condition1 && condition2;
  }
}

// Time Complexity: O(n) - 1 ms -> 88.49%
// Space Complexity: O(n) - 42.14 MB -> 21.59%