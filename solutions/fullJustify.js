/*
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
*/

/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function (words, maxWidth) {
  const result = [];
  let line = [];
  let currentLineLength = 0;
  for (let i = 0; i < words.length; i++) {
    if (currentLineLength + line.length + words[i].length <= maxWidth) {
      line.push(words[i]);
      currentLineLength += words[i].length;
    } else {
      let spaces = maxWidth - currentLineLength;
      let space = line.length > 1 ? Math.floor(spaces / (line.length - 1)) : spaces;
      let extraSpaces = line.length > 1 ? spaces % (line.length - 1) : 0;
      let lineStr = "";
      for (let j = 0; j < line.length; j++) {
        lineStr += line[j];
        if (j < line.length - 1) {
          lineStr += " ".repeat(space);
          if (extraSpaces > 0) {
            lineStr += " ";
            extraSpaces--;
          }
        }
      }
      lineStr += " ".repeat(maxWidth - lineStr.length);
      result.push(lineStr);
      line = [words[i]];
      currentLineLength = words[i].length;
    }
  }
  result.push(line.join(" ") + " ".repeat(maxWidth - line.join(" ").length));
  return result;
};

// test cases
console.log(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16));
console.log(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16));
console.log(
  fullJustify(
    [
      "Science",
      "is",
      "what",
      "we",
      "understand",
      "well",
      "enough",
      "to",
      "explain",
      "to",
      "a",
      "computer.",
      "Art",
      "is",
      "everything",
      "else",
      "we",
      "do",
    ],
    20
  )
);
