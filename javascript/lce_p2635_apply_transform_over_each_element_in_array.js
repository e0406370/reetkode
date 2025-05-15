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