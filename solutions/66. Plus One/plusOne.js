/*
You are given a large integer represented as an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
*/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  for (let i = digits.length - 1; i > 0; i--) {
    if (digits[i] + 1 > 9) {
      digits[i] = 0;
    } else {
      digits[i] += 1;
      return digits;
    }
  }
  if (digits[0] + 1 > 9) {
    digits[0] = 0;
    digits.unshift(1);
    return digits;
  }
  digits[0] += 1;
  return digits;
};

// Test cases
console.log(plusOne([1, 2, 3])); // [1,2,4]
