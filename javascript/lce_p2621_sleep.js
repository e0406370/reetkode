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
