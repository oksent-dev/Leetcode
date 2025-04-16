/*
Given a string s, return the longest palindromic substring in s.
*/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  if (s.length <= 1) {
    return s;
  }

  function expandFromCenter(left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left--;
      right++;
    }
    return s.slice(left + 1, right);
  }

  let maxStr = s[0];

  for (let i = 0; i < s.length - 1; i++) {
    const odd = expandFromCenter(i, i);
    const even = expandFromCenter(i, i + 1);

    if (odd.length > maxStr.length) {
      maxStr = odd;
    }
    if (even.length > maxStr.length) {
      maxStr = even;
    }
  }

  return maxStr;
};

// Test cases
console.log(longestPalindrome("babad")); // "bab" or "aba"
console.log(longestPalindrome("cbbd")); // "bb"
