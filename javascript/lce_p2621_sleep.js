/**
LCE 2621. Sleep

Given a positive integer millis, write an asynchronous function that sleeps for millis milliseconds.
It can resolve any value.

Note that minor deviation from millis in the actual sleep duration is acceptable.

Constraints:
- 1 <= millis <= 1000
*/

/**
 * @param {number} millis
 * @return {Promise}
 */

// asynchronous programming with Promises and setTimeout with return => returns Promise
async function sleep(millis) {
  return new Promise((resolve, reject) => {
    try {
      setTimeout(() => {
        console.log(`Delayed for ${millis} ms`);
        resolve();
      }, millis);
    }
    catch (err) {
      reject(err);
    }
  });
}

// asynchronous programming with Promises and setTimeout without return => returns undefined (no return is mentioned but async will return Promise if there is return)
async function sleep(milliseconds) {
  await new Promise((res) => setTimeout(res, milliseconds));
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
