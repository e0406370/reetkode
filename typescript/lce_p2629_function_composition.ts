/*
  LCE 2629. Function Composition

  Given an array of functions [f1, f2, f3, ..., fn], return a new function fn that is the function composition of the array of functions.

  The function composition of [f(x), g(x), h(x)] is fn(x) = f(g(h(x))).
  The function composition of an empty list of functions is the identity function f(x) = x.

  You may assume each function in the array accepts one integer as input and returns one integer as output.
*/

type F = (x: number) => number;

function compose(functions: F[]): F {

  return function (x) {

    var len = functions.length;

    for (let idx = len - 1; idx >= 0; idx--) {
      x = functions[idx](x);
    }

    return x;
  };
}

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
