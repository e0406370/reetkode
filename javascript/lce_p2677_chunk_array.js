/**
LCE 2677. Chunk Array

Given an array arr and a chunk size size, return a chunked array.

A chunked array contains the original elements in arr, but consists of subarrays each of length size.
The length of the last subarray may be less than size if arr.length is not evenly divisible by size.

You may assume the array is the output of JSON.parse.
In other words, it is valid JSON.

Please solve it without using lodash's _.chunk function.

Constraints:
- arr is a valid JSON array
- 2 <= JSON.stringify(arr).length <= 10^5
- 1 <= size <= arr.length + 1
*/

/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */


// plain push
// Time: O(n)
// Space: O(n)
var chunk = function (arr, size) {
  let chunks = [];
  let temp = [];

  for (const num of arr) {
    temp.push(num);

    if (temp.length === size) {
      chunks.push(temp);
      temp = [];
    }
  }

  if (temp.length) {
    chunks.push(temp);
  }

  return chunks;
};

// using slicing (recommended)
// Time: O(n)
// Space: O(1)
var chunk = function (arr, size) {
  let chunks = [];
  let ptr = 0;

  while (ptr < arr.length) {
    chunks.push(arr.slice(ptr, ptr + size));
    ptr += size;
  }

  return chunks;
};
