/**
 * @param {number} n
 * @return {Function} counter
 */

// postfix increment
var createCounter = function (n) {
  return () => {
    return n++;
  };
};

// prefix decrement at the start, followed by prefix increment every time this function is invoked
var createCounter = function (n) {
  --n;
  return () => {
    return ++n;
  };
};

/**
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

/**
 * notes:
 * 
 * closure 
 * - arrow function returned by createCounter has access to the n variable in its enclosing scope, even after createCounter has finished executing
 * 
 * persistent state
 * - since the n variable is stored in the closure, its value persists between calls to the returned function
 * 
 */