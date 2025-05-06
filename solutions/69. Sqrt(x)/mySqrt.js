/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
*/

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  return Math.floor(Math.sqrt(x));
};

// Test cases
console.log(mySqrt(4)); // 2
console.log(mySqrt(8)); // 2
