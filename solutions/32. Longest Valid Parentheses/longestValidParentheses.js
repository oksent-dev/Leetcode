/*
Given a string containing just the characters '(' and ')', 
return the length of the longest valid (well-formed) parentheses substring.
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function (s) {
  const stack = [-1];
  let maxLen = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i);
    } else {
      stack.pop();
      if (stack.length === 0) {
        stack.push(i);
      } else {
        maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
      }
    }
  }

  return maxLen;
};

// Test cases
console.log(longestValidParentheses("(()")); // 2
console.log(longestValidParentheses(")()())")); // 4
console.log(longestValidParentheses("")); // 0
