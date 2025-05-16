/**
LCE 2620. Counter

Given an integer n, return a counter function.
This counter function initially returns n and then returns 1 more than the previous value every subsequent time it is called (n, n + 1, n + 2, etc).

Constraints:
- -1000 <= n <= 1000
- 0 <= calls.length <= 1000
- calls[i] === "call"
*/

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