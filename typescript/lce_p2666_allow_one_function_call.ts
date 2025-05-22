/*
  LCE 2666. Allow One Function Call

  Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.

  - The first time the returned function is called, it should return the same result as fn.
  - Every subsequent time it is called, it should return undefined.
*/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type OnceFn = (...args: JSONValue[]) => JSONValue | undefined;

function once(fn: Function): OnceFn {

  var calls = 0;

  return function (...args) {
    calls++;

    if (calls == 1) {
      return fn(...args); // note that fn expects multiple parameters instead of a single array argument (refer to test case descriptions)
    }
    else {
      return undefined;
    }
  };
}

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */