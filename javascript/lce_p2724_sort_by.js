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
