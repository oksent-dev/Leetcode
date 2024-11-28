/*
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (s.length === 0 || t.length === 0) {
    return "";
  }
  const charMap = {};
  for (let char of t) {
    charMap[char] = (charMap[char] || 0) + 1;
  }
  let left = 0;
  let right = 0;
  let count = t.length;
  let minLen = Infinity;
  let minStart = 0;
  while (right < s.length) {
    if (charMap[s[right]] > 0) {
      count--;
    }
    charMap[s[right]]--;
    right++;
    while (count === 0) {
      if (right - left < minLen) {
        minLen = right - left;
        minStart = left;
      }
      if (charMap[s[left]] === 0) {
        count++;
      }
      charMap[s[left]]++;
      left++;
    }
  }
  return minLen === Infinity ? "" : s.slice(minStart, minStart + minLen);
};

// test cases
console.log(minWindow("ADOBECODEBANC", "ABC")); // "BANC"
console.log(minWindow("a", "a")); // "a"
console.log(minWindow("a", "aa")); // ""
