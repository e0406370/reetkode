/**
LCM 2623. Memoize

Given a function fn, return a memoized version of that function.

A memoized function is a function that will never be called twice with the same inputs.
Instead it will return a cached value.

You can assume there are 3 possible input functions: sum, fib, and factorial.

- sum accepts two integers a and b and returns a + b.
  Assume that if a value has already been cached for the arguments (b, a) where a != b, it cannot be used for the arguments (a, b).
  For example, if the arguments are (3, 2) and (2, 3), two separate calls should be made.

- fib accepts a single integer n and returns 1 if n <= 1 or fib(n - 1) + fib(n - 2) otherwise.

- factorial accepts a single integer n and returns 1 if n <= 1 or factorial(n - 1) * n otherwise.

Constraints:
- 0 <= a, b <= 10^5
- 1 <= n <= 10
- 1 <= actions.length <= 10^5
- actions.length === values.length
- actions[i] is one of "call" and "getCallCount"
- fnName is one of "sum", "factorial" and "fib"
*/

/**
 * @param {Function} fn
 * @return {Function}
 */

// rest/spread syntax + JSON.stringify()
function memoize(fn) {
  const cache = new Map();

  return function (...args) {
    key = JSON.stringify(args);

    if (cache.has(key)) {
      return cache.get(key);
    }

    res = fn(...args);
    cache.set(key, res);

    return res;
  };
}

// optimise based on numeric constraints + Function.apply
function memoize(fn) {
  const cache = new Map();

  return function () {
    let key = arguments[0];

    if (arguments[1]) {
      key += arguments[1] * 100001;
    }

    const result = cache.get(key);
    if (result !== undefined) {
      return result;
    }

    const functionOutput = fn.apply(null, arguments);
    cache.set(key, functionOutput);

    return functionOutput;
  };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */
