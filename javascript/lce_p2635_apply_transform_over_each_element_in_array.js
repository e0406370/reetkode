/**
LCE 2635. Apply Transform Over Each Element in Array

Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

The returned array should be created such that returnedArray[i] = fn(arr[i], i).

Please solve it without the built-in Array.map method.

Constraints:
- 0 <= arr.length <= 1000
- -10^9 <= arr[i] <= 10^9
- fn returns an integer.
*/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
// note that fn is the callback

// in-memory transformation (~10 ms for 5M size)
var map = function(arr, fn) {
    for (i = 0; i < arr.length; i++) {
        arr[i] = fn(arr[i], i)
    }
    return arr
};

// preallocate memory (~40 ms for 5M size)
var map = function(arr, fn) {
    const newArr = new Array(arr.length)

    for (i = 0; i < arr.length; i++) {
        newArr[i] = fn(arr[i], i)
    }
    return newArr
};

// push values onto array (~200 ms for 5M size)
var map = (arr, fn) => {
    const newArr = []

    for (i = 0; i < arr.length; i++) {
        newArr.push(fn(arr[i], i))
    }
    return newArr
}

// writing values onto initially empty array (~250 ms for 5M size)
var map = (arr, fn) => {
    const newArr = [];

    for (i = 0; i < arr.length; i++) {
        newArr[i] = fn(arr[i], i)
    }
    return newArr
}

// for... in loop (~1000 ms for 5M size)
var map = (arr, fn) => {
    const newArr = new Array(arr.length)

    for (i in arr) {
        newArr[i] = fn(arr[i], Number(i))
    }
    return newArr
}