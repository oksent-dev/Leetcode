/*
Given a positive integer n, write a function that returns the number of 
set bits in its binary representation (also known as the Hamming weight).
*/

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function (n) {
  let count = 0;
  while (n) {
    count += n & 1;
    n >>>= 1;
  }
  return count;
};

// Test cases
console.log(hammingWeight(11)); // 3
console.log(hammingWeight(128)); // 1
console.log(hammingWeight(2147483645)); // 30
