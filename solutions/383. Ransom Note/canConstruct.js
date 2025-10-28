/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
*/

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  let magazineArr = magazine.split("");
  for (let i = 0; i < ransomNote.length; i++) {
    let index = magazineArr.indexOf(ransomNote[i]);
    if (index === -1) {
      return false;
    }
    magazineArr.splice(index, 1);
  }
  return true;
};

// test cases:
console.log(canConstruct("a", "b")); // false
console.log(canConstruct("aa", "ab")); // false
console.log(canConstruct("aa", "aab")); // true
