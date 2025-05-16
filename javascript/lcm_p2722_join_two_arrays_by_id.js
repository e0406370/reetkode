/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */

var join = function (arr1, arr2) {
  const map = new Map();

  arr1.forEach((val) => {
    map.set(val.id, val);
  });

  arr2.forEach((val) => {
    if (!map.has(val.id)) {
      map.set(val.id, val);
    }
    else {
      const olderObj = map.get(val.id);
      const newerObj = val;
      for (const key of Object.keys(newerObj)) {
        olderObj[key] = newerObj[key];
      }
    }
  });

  const res = [];
  for (const key of map.keys()) {
    res.push(map.get(key));
  }
  res.sort((a, b) => (a.id - b.id))

  return res;
};
