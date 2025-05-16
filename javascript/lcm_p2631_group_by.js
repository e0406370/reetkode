/**
LCM 2631. Group By

Write code that enhances all arrays such that you can call the array.groupBy(fn) method on any array and it will return a grouped version of the array.

A grouped array is an object where each key is the output of fn(arr[i]) and each value is an array containing all items in the original array which generate that key.

The provided callback fn will accept an item in the array and return a string key.

The order of each value list should be the order the items appear in the array.
Any order of keys is acceptable.

Please solve it without lodash's _.groupBy function.

Constraints:
- 0 <= array.length <= 10^5
- fn returns a string
*/

/**
 * @param {Function} fn
 * @return {Object}
 */

// using Map
Array.prototype.groupBy = function (fn) {
  let map = new Map();

  for (const obj of this) {
    let key = fn(obj);

    if (!map[key]) {
      map[key] = [];
    }

    map[key].push(obj);
  }

  return map;
};

// using standard {} notation
Array.prototype.groupBy = function (fn) {
  const res = {};

  for (const obj of this) {
    const key = fn(obj);

    if (key in res) {
      res[key].push(obj);
    }
    else {
      res[key] = [obj];
    }
  }

  return res;
};

// using reduce method
Array.prototype.groupBy = function (fn) {
  return this.reduce((accum, item) => {
    const key = fn(item);

    accum[key] ||= [];
    accum[key].push(item);

    return accum;
  }, {});
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
