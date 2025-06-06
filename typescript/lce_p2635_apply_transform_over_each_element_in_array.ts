/*
  LCE 2635. Apply Transform Over Each Element in Array

  Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

  The returned array should be created such that returnedArray[i] = fn(arr[i], i).

  Please solve it without the built-in Array.map method.
*/

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  
  for (let idx = 0; idx < arr.length; idx++) {
    arr[idx] = fn(arr[idx], idx);
  }

  return arr;
}
