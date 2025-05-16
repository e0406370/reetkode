/**
LCM 2637. Promise Time Limit

Given an asynchronous function fn and a time t in milliseconds, return a new time limited version of the input function.
fn takes arguments provided to the time limited function.

The time limited function should follow these rules:
- If the fn completes within the time limit of t milliseconds, the time limited function should resolve with the result.
- If the execution of the fn exceeds the time limit, the time limited function should reject with the string "Time Limit Exceeded".

Constraints:
- 0 <= inputs.length <= 10
- 0 <= t <= 1000
- fn returns a promise
*/

/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */

// handle clearing timeout
var timeLimit = function (fn, t) {
  return async function (...args) {
    return new Promise((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        reject("Time Limit Exceeded");
      }, t);

      fn(...args)
        .then(resolve)
        .catch(reject)
        .finally(() => clearTimeout(timeoutId));
    });
  };
}; 

// promise race
var timeLimit = function (fn, t) {
  return async function (...args) {
    const timeLimitPromise = new Promise((resolve, reject) => {
      setTimeout(() => reject("Time Limit Exceeded"), t);
    });

    const returnedPromise = fn(...args);
  
    return Promise.race([timeLimitPromise, returnedPromise]);
  };
};

// async/await + clearing timeout
var timeLimit = function(fn, t) {
  return async function(...args) {
    return new Promise(async (resolve, reject) => {
      const timeout = setTimeout(() => {
        reject("Time Limit Exceeded");
      }, t);

      try {
        const result = await fn(...args);
        resolve(result);
      }
      catch (err) {
        reject(err);
      }
      finally {
        clearTimeout(timeout);
      }
    });
  };
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */

/**
Input: 
fn = async (n) => { 
  await new Promise(res => setTimeout(res, 100)); 
  return n * n; 
}
inputs = [5]
t = 50
Output: {"rejected":"Time Limit Exceeded","time":50}
Explanation:
const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
   const res = await limited(...inputs)
   result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} 
catch (err) {
   result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms.
It rejects at t=50ms because the time limit was reached.
*/