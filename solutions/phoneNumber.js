/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

*/

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits.length === 0) return [];

  const phone = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz"
  };
  result = [];

  function backtrack(index, current) {
    if (index === digits.length) {
      result.push(current);
      return;
    }

    for (let i = 0; i < phone[digits[index]].length; i++) {
      backtrack(index + 1, current + phone[digits[index]][i]);
    }
  }

  backtrack(0, "");

  return result;
};
// test cases:
console.log(letterCombinations("23")); // Expected output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
