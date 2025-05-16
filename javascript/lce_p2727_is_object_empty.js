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