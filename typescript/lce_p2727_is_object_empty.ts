/*
  LCE 2727. Is Object Empty

  Given an object or an array, return if it is empty.
  - An empty object contains no key-value pairs.
  - An empty array contains no elements.

  You may assume the object or array is the output of JSON.parse.
*/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | JSONValue[];

function isEmpty(obj: Obj): boolean {

  // type of obj is JSONValue[]
  if (Array.isArray(obj)) {
    return obj.length == 0;
  }
  // type of obj is Record<string, JSONValue>
  else if (typeof obj == 'object' && obj != null) {
    return Object.keys(obj).length == 0;
  }
  // other types
  else {
    return false;
  }
};
