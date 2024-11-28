/*
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated   string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
*/

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function (s, words) {
  if (s.length === 0 || words.length === 0) {
    return [];
  }
  const wordLen = words[0].length;
  const wordCount = words.length;
  const wordMap = {};
  for (let word of words) {
    wordMap[word] = (wordMap[word] || 0) + 1;
  }
  const result = [];
  for (let i = 0; i < wordLen; i++) {
    let left = i;
    let right = i;
    let count = 0;
    let seen = {};
    while (right + wordLen <= s.length) {
      const word = s.slice(right, right + wordLen);
      right += wordLen;
      if (wordMap[word]) {
        seen[word] = (seen[word] || 0) + 1;
        count++;
        while (seen[word] > wordMap[word]) {
          const firstWord = s.slice(left, left + wordLen);
          seen[firstWord]--;
          count--;
          left += wordLen;
        }
        if (count === wordCount) {
          result.push(left);
        }
      } else {
        seen = {};
        count = 0;
        left = right;
      }
    }
  }
  return result;
};

// test case:
console.log(findSubstring("barfoothefoobarman", ["foo", "bar"])); // [0,9]
