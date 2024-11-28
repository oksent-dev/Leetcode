/* 
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 
*/

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const result = [];
  function backtrack(open, close, current) {
    if (current.length === 2 * n) {
      result.push(current);
      return;
    }
    if (open < n) backtrack(open + 1, close, current + "(");
    if (close < open) backtrack(open, close + 1, current + ")");
  }
  backtrack(0, 0, "");
  return result;
};
