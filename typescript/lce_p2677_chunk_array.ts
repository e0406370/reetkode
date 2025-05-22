/*
  LCE 2677. Chunk Array

  Given an array arr and a chunk size size, return a chunked array.

  A chunked array contains the original elements in arr, but consists of subarrays each of length size.
  The length of the last subarray may be less than size if arr.length is not evenly divisible by size.

  You may assume the array is the output of JSON.parse. In other words, it is valid JSON.

  Please solve it without using lodash's _.chunk function.
*/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {

  var chunked: Obj[][] = [];

  for (let idx = 0; idx < arr.length; idx += size) {
    var chunk = arr.slice(idx, idx + size);
    chunked.push(chunk);
  }

  return chunked;
};
