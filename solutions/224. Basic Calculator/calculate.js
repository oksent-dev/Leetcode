/*
Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
*/

/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  let stack = [];
  let result = 0;
  let num = 0;
  let sign = 1;
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (char === " ") {
      continue;
    } else if (char === "+") {
      result += sign * num;
      num = 0;
      sign = 1;
    } else if (char === "-") {
      result += sign * num;
      num = 0;
      sign = -1;
    } else if (char === "(") {
      stack.push(result);
      stack.push(sign);
      result = 0;
      sign = 1;
    } else if (char === ")") {
      result += sign * num;
      num = 0;
      result *= stack.pop();
      result += stack.pop();
    } else {
      num = num * 10 + parseInt(char);
    }
  }
  return result + sign * num;
};

// Test cases
console.log(calculate("1 + 1")); // 2
console.log(calculate(" 2-1 + 2 ")); // 3
console.log(calculate("(1+(4+5+2)-3)+(6+8)")); // 23
