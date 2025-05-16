/**
 * @return {null|boolean|number|string|Array|Object}
 */

// regular if check
Array.prototype.last = function () {
  if (this.length) {
    return this[this.length - 1];
  }

  return -1;
};

// ternary operator
Array.prototype.last = function () {
  return this.length === 0 ? -1 : this[this.length - 1];
};

// using nullish coalescing operator with Array.prototype.at() method
Array.prototype.last = function () {
  return this.at(-1) ?? -1;
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */
