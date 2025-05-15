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
