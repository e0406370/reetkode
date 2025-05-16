/**
LCE 2724. Sort By

Given an array arr and a function fn, return a sorted array sortedArr.
You can assume fn only returns numbers and those numbers determine the sort order of sortedArr.
sortedArr must be sorted in ascending order by fn output.

You may assume that fn will never duplicate numbers for a given array.

Constraints:
- arr is a valid JSON array
- fn is a function that returns a number
- 1 <= arr.length <= 5 * 10^5
*/

/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */

// using subtraction-based comparator
var sortBy = function (arr, fn) {
  arr.sort((a, b) => fn(a) - fn(b));
  return arr;
};

// using comparison-based comparator
var sortBy = function (arr, fn) {
  function swap(a, b) {
    return fn(a) < fn(b) ? -1 : 1;
  }

  return arr.sort(swap);
};
