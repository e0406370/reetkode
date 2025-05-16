/**
LCE 2727. Is Object Empty

Given an object or an array, return if it is empty.

- An empty object contains no key-value pairs.
- An empty array contains no elements.

You may assume the object or array is the output of JSON.parse.

Constraints:
- obj is a valid JSON object or array
- 2 <= JSON.stringify(obj).length <= 10^5
*/

/**
 * @param {Object|Array} obj
 * @return {boolean}
 */

// using JSON.stringify
var isEmpty = function(obj) {
    return JSON.stringify(obj).length <= 2
};

// check if it is Array first => if yes, use length directly, else use Object.keys.length
var isEmpty = function (obj) {
  if (Array.isArray(obj)) {
      return obj.length === 0
    }
    return Object.keys(obj).length === 0
};

// using loop
var isEmpty = function(obj) {
    for (const _ in obj) return false
    return true
};