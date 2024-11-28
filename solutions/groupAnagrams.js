/*
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
*/

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const anagrams = {};
  for (let str of strs) {
    const sortedStr = str.split("").sort().join("");
    if (anagrams[sortedStr]) {
      anagrams[sortedStr].push(str);
    } else {
      anagrams[sortedStr] = [str];
    }
  }
  return Object.values(anagrams);
};

// Test cases
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])); // [["bat"],["nat","tan"],["ate","eat","tea"]]
console.log(groupAnagrams([""])); // [[""]]
