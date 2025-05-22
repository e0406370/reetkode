/*
  LCE 2665. Counter II

  Write a function createCounter. It should accept an initial integer init. It should return an object with three functions.

  The three functions are:
  - increment() increases the current value by 1 and then returns it.
  - decrement() reduces the current value by 1 and then returns it.
  - reset() sets the current value to init and then returns it.
*/
  
type Counter = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter(init: number): Counter {

  var initial = init;

  return {
    increment: () => {
      init++;
      return init;
    },
    decrement: () => {
      init--;
      return init;
    },
    reset: () => {
      init = initial;
      return init;
    }
  };
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
