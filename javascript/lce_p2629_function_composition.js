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
