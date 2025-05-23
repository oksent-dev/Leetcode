/*
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
*/

function sumOfSquares(n) {
  let sum = 0;
  while (n > 0) {
    sum += (n % 10) ** 2;
    n = Math.floor(n / 10);
  }
  return sum;
}

/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
  let slow = n;
  let fast = n;
  do {
    slow = sumOfSquares(slow);
    fast = sumOfSquares(sumOfSquares(fast));
  } while (slow !== fast);
  return slow === 1;
};

// Test cases
console.log(isHappy(19)); // true
console.log(isHappy(2)); // false
