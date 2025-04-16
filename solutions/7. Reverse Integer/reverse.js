/*
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  if (x === 0) return x;
  let sign = x < 0 ? true : false;
  x = Math.abs(x).toString();
  x = x.split("").reverse();
  for (let i = 0; i < x.length; i++) {
    if (x[i] === "0") {
      x.splice(i, 1);
      i--;
    } else break;
  }
  x = parseInt(x.join(""), 10);
  if (x > 2147483647) return 0;
  if (sign) x *= -1;
  return x;
};

// Test cases
console.log(reverse(123)); // 321
console.log(reverse(-123)); // -321
