/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// note that fn is the callback

var filter = function (arr, fn) {
  const filteredArr = [];

  for (i = 0; i < arr.length; i++) {
    if (fn(arr[i], i)) {
      filteredArr.push(arr[i]);
    }
  }

  return filteredArr;
};

// can use similar approaches from lce_p2635
