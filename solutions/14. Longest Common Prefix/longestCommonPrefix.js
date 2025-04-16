/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
*/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length === 0) {
    return "";
  }
  let shortest = strs[0];
  for (let str of strs) {
    if (str.length < shortest.length) {
      shortest = str;
    }
  }

  let prefix = "";
  for (let i = 0; i < shortest.length; i++) {
    for (let j = 0; j < strs.length; j++) {
      if (shortest[i] !== strs[j][i]) {
        return prefix;
      }
    }
    prefix += shortest[i];
  }

  return prefix;
};

// Test cases
console.log(longestCommonPrefix(["flower", "flow", "flight"])); // "fl"
console.log(longestCommonPrefix(["dog", "racecar", "car"])); // ""
