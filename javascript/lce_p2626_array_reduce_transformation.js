/**
LCE 2626. Array Reduce Transformation

Given an integer array nums, a reducer function fn, and an initial value init,
return the final result obtained by executing the fn function on each element of the array,
sequentially, passing in the return value from the calculation on the preceding element.

This result is achieved through the following operations: val = fn(init, nums[0]), val = fn(val, nums[1]), val = fn(val, nums[2]), ... until every element in the array has been processed. 
The ultimate value of val is then returned.

If the length of the array is 0, the function should return init.

Please solve it without using the built-in Array.reduce method.

Constraints:
- 0 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
- 0 <= init <= 1000
*/

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
