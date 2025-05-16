/**
LCE 2629. Function Composition

Given an array of functions [f1, f2, f3, ..., fn], return a new function fn that is the function composition of the array of functions.

The function composition of [f(x), g(x), h(x)] is fn(x) = f(g(h(x))).

The function composition of an empty list of functions is the identity function f(x) = x.

You may assume each function in the array accepts one integer as input and returns one integer as output.

Constraints:
- -1000 <= x <= 1000
- 0 <= functions.length <= 1000
- all functions accept and return a single integer
*/

/**
 * @param {Function[]} functions
 * @return {Function}
 */

// conventional
var compose = function (functions) {
  return function (x) {
    for (i = functions.length - 1; i >= 0; i--) {
      x = functions[i](x);
    }

    return x;
  };
};

// Array.reduceRight
var compose = function (functions) {
  return function (x) {
    return functions.reduceRight((acc, f) => f(acc), x);
  };
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
