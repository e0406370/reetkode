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