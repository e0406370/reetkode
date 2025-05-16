/**
LCE 2704. To Be Or Not To Be

Write a function expect that helps developers test their code.
It should take in any value val and return an object with the following two functions.

- toBe(val) accepts another value and returns true if the two values === each other.
If they are not equal, it should throw an error "Not Equal".

- notToBe(val) accepts another value and returns true if the two values !== each other.
If they are equal, it should throw an error "Equal".
*/

/**
 * @param {string} val
 * @return {Object}
 */

// function expression
var expect = function (val) {
  return {
    toBe: (val2) => {
      if (val !== val2) throw new Error("Not Equal");
      return true;
    },
    notToBe: (val2) => {
      if (val === val2) throw new Error("Equal");
      return true;
    },
  };
};

// using ES6 classes
class Expect {
  constructor(val) {
    this.val = val;
  }

  toBe(val2) {
    if (this.val !== val2) {
      throw new Error("Not Equal");
    }
    return true;
  }

  notToBe(val2) {
    if (this.val === val2) {
      throw new Error("Equal");
    }
    return true;
  }
}

function expect(val) {
  return new Expect(val);
}

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
