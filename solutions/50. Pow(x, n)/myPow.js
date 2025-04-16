/*
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
*/

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
  if (n === 0) return 1;
  if (n < 0) return 1 / myPow(x, -n);
  if (n % 2 === 0) return myPow(x * x, n / 2);
  return x * myPow(x, n - 1);
};

// Test cases
console.log(myPow(2, 10)); // 1024
console.log(myPow(2.1, 3)); // 9.261
console.log(myPow(2, -2)); // 0.25
