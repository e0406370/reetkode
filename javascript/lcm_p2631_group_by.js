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
