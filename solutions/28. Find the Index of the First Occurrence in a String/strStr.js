/*
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
*/
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  for (let i = 0; i + needle.length <= haystack.length; i++) {
    let check = true;
    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] != needle[j]) {
        check = false;
        break;
      }
    }
    if (check) {
      return i;
    }
  }
  return -1;
};

// Test cases
console.log(strStr("sadbutsad", "sad")); // 9
console.log(strStr("leetcode", "leeto")); // -1
