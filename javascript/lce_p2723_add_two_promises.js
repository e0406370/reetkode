/**
LCE 2723. Add Two Promises

Given two promises promise1 and promise2, return a new promise. promise1 and promise2 will both resolve with a number.
The returned promise should resolve with the sum of the two numbers.

Constraints:
- promise1 and promise2 are promises that resolve with a number
*/

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */

// using Promise.all with Promise.then
var addTwoPromises = async function (promise1, promise2) {
  try {
    return Promise.all([promise1, promise2]).then((values) => {
      res = values.reduce((acc, curr) => acc + curr, 0);
      return res;
    });
  }
  catch (err) {
    console.error(err);
    throw err; // rethrow the error to maintain the behavior of propagating the error to the caller
  }
};

// using only await
var addTwoPromises = async function(promise1, promise2) {
  try {
    return await promise1 + await promise2;
  }
  catch (err) {
    console.error(err);
    throw err; // rethrow the error to maintain the behavior of propagating the error to the caller
  }
};

// using only Promise.then
var addTwoPromises = async function(promise1, promise2) {
  try {
    return promise1.then((val) => promise2.then((val2) => val + val2))
  }
  catch (err) {
    console.error(err);
    throw err; // rethrow the error to maintain the behavior of propagating the error to the caller
  }
};

// count promises
var addTwoPromises = async function (promise1, promise2) {
  return new Promise((resolve, reject) => {
    let count = 2;
    let res = 0; 
    
    [promise1, promise2].forEach(async promise => {
      try {
        const subRes = await promise;
        res += subRes;
        count--;

        if (count === 0) {
          resolve(res);
        }
      }
      catch (err) {
        reject(err);
      }
    });
  });
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
