/**
LCE 2666. Allow One Function Call

Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.

- The first time the returned function is called, it should return the same result as fn.
- Every subsequent time it is called, it should return undefined.

Constraints:
- calls is a valid JSON array
- 1 <= calls.length <= 10
- 1 <= calls[i].length <= 100
- 2 <= JSON.stringify(calls).length <= 1000
*/

/**
 * @param {Function} fn
 * @return {Function}
 */

// rest syntax
var once = function (fn) {
  count = 1;

  return function (...args) {
    if (count == 0) {
      return undefined;
    }

    count--;
    return fn(...args);
  };
};

// implicitly return undefined
var once = function (fn) {
  let hasBeenCalled = false;

  return function (...args) {
    if (!hasBeenCalled) {
      hasBeenCalled = true;

      return fn(...args);
    }
  };
};

// bind function to context
var once = function (fn) {
  let hasBeenCalled = false;

  return function (...args) {
    if (!hasBeenCalled) {
      hasBeenCalled = true;

      return fn.apply(this, args);
    }
  };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
