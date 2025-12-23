/* 
Given two strings s and t, return true if t is an anagram
 of s, and false otherwise. 
*/
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }
  let s1 = s.split("").sort().join("");
  let t1 = t.split("").sort().join("");
  return s1 === t1;
};

// test cases:
console.log(isAnagram("anagram", "nagaram")); // true
console.log(isAnagram("rat", "car")); // false
