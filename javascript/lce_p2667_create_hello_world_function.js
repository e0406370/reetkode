/**
LCE 2667. Create Hello World Function

Write a function createHelloWorld.
It should return a new function that always returns "Hello World".

Constraints:
- 0 <= args.length <= 10
*/

/**
 * @return {Function}
 */

// arrow syntax
var createHelloWorld = function () {
  return () => "Hello World";
};

// function syntax
var createHelloWorld = function () {
  return function () {
    return "Hello World";
  };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

/**
 * example 1: factory function
 * ===========================
 * var createHelloWorld = function() {
 *    return () => "Hello World"
 * }
 * 
 * const f = createHelloWorld(); // 'f' is the returned function (arrow function)
 * f(); // invokes the returned function; output: "Hello World"
 * 
 * 
 * example 2: normal function
 * ==========================
 * var createHelloWorld = () => "Hello World"
 * 
 * const f = createHelloWorld; // 'f' directly references the 'createHelloWorld' function
 * f(); // invokes the 'createHelloWorld' function directly; output: "Hello World"
 */