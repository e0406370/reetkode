/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
// note that fn is the callback

// access element by index
var reduce = function (nums, fn, init) {
  if (nums.length == 0) {
    return init;
  }

  for (i = 0; i < nums.length; i++) {
    init = fn(init, nums[i]);
  }

  return init;
};

// for ...of loop (retrieve element)
var reduce = function (arr, fn, initialVal) {
  let accumulator = initialVal;

  for (const element of arr) {
    accumulator = fn(accumulator, element);
  }

  return accumulator;
};

// array.forEach loop
var reduce = function (arr, fn, initialVal) {
  let accumulator = initialVal;

  arr.forEach((element) => {
    accumulator = fn(accumulator, element);
  });

  return accumulator;
};

// for ...in loop (retrieve index)
var reduce = function (arr, fn, initialVal) {
  let accumulator = initialVal;

  for (const index in arr) {
    accumulator = fn(accumulator, arr[index]);
  }

  return accumulator;
};
