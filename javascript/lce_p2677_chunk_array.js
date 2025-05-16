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
