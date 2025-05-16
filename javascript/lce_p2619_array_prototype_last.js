/**
LCE 2619. Array Prototype Last

Write code that enhances all arrays such that you can call the array.last() method on any array and it will return the last element.
If there are no elements in the array, it should return -1.

You may assume the array is the output of JSON.parse.

Constraints:
- arr is a valid JSON array
- 0 <= arr.length <= 1000
*/

/**
 * @return {null|boolean|number|string|Array|Object}
 */

// regular if check
Array.prototype.last = function () {
  if (this.length) {
    return this[this.length - 1];
  }

  return -1;
};

// ternary operator
Array.prototype.last = function () {
  return this.length === 0 ? -1 : this[this.length - 1];
};

// using nullish coalescing operator with Array.prototype.at() method
Array.prototype.last = function () {
  return this.at(-1) ?? -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
