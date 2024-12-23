/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */

// closure
var createCounter = function (init) {
  let currentCount = init;

  return {
    increment: function () {
      currentCount += 1;
      return currentCount;
    },
    decrement: function () {
      currentCount -= 1;
      return currentCount;
    },
    reset: function () {
      currentCount = init;
      return currentCount;
    },
  };
};

// closure with shortened syntax
var createCounter = function (init) {
  let currentCount = init;

  return {
    increment: () => ++currentCount,
    decrement: () => --currentCount,
    reset: () => (currentCount = init),
  };
};

// closure with separately created functions
var createCounter = function (init) {
  let currentCount = init;

  function increment() {
    return ++currentCount;
  }

  function decrement() {
    return --currentCount;
  }

  function reset() {
    return (currentCount = init);
  }

  return { increment, decrement, reset };
};

// classes
class Counter {
  constructor(init) {
    this.init = init;
    this.currentCount = init;
  }

  increment() {
    return ++this.currentCount;
  }

  decrement() {
    return --this.currentCount;
  }

  reset() {
    return (this.currentCount = this.init);
  }
}

function createCounter(init) {
  return new Counter(init);
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

/**
 * Feature            Closures                                    Classes
 * -----------------------------------------------------------------------------
 * Encapsulation       currentCount is private and not             By default, properties
 *                     directly accessible.                        like currentCount are public.
 *
 * Direct Access       Not possible for currentCount. Must         Possible unless private
 *                     use methods.                                fields (#) are used.
 *
 * Syntax              Functional programming style.               Object-oriented programming style.
 *
 * State Management    State is tied to the function closure.      State is tied to the instance (this).
 */
