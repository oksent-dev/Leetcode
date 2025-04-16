/*
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
*/

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function (dividend, divisor) {
  if (divisor === 0) return NaN;

  const isNegative = dividend < 0 !== divisor < 0;
  dividend = Math.abs(dividend);
  divisor = Math.abs(divisor);

  if (dividend === divisor) return isNegative ? -1 : 1;

  let quotient = 0;
  while (dividend >= divisor) {
    let temp = divisor;
    let multiple = 1;
    while (dividend >= temp + temp) {
      temp += temp;
      multiple += multiple;
    }
    dividend -= temp;
    quotient += multiple;
  }
  if (isNegative) quotient = -quotient;
  return Math.min(Math.max(-Math.pow(2, 31), quotient), Math.pow(2, 31) - 1);
};

// Test cases
console.log(divide(10, 3)); // 3
console.log(divide(7, -3)); // -2
