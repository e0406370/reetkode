/**
LCM 2722. Join Two Arrays by ID

Given two arrays arr1 and arr2, return a new array joinedArray.
All the objects in each of the two inputs arrays will contain an id field that has an integer value. 

joinedArray is an array formed by merging arr1 and arr2 based on their id key.
The length of joinedArray should be the length of unique values of id.
The returned array should be sorted in ascending order based on the id key.

If a given id exists in one array but not the other, the single object with that id should be included in the result array without modification.

If two objects share an id, their properties should be merged into a single object:
- If a key only exists in one object, that single key-value pair should be included in the object.
- If a key is included in both objects, the value in the object from arr2 should override the value from arr1.

Constraints:
- arr1 and arr2 are valid JSON arrays
- Each object in arr1 and arr2 has a unique integer id key
- 2 <= JSON.stringify(arr1).length <= 10^6
- 2 <= JSON.stringify(arr2).length <= 10^6
*/

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
