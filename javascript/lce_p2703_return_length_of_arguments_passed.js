/**
LCE 2703. Return Length of Arguments Passed

Write a function argumentsLength that returns the count of arguments passed to it.

Constraints:
- args is a valid JSON array
- 0 <= args.length <= 100
*/

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */

// ... => rest parameter (accepts indefinite number of arguments)
var argumentsLength = function(...args) {
    return args.length
};

// using argument object (special object available inside all JS functions except arrow functions)
var argumentsLength = function(...args) {
    return arguments.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */