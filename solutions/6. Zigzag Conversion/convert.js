/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (numRows === 1) return s;

  const matrix = new Array(numRows).fill(numRows).map(() => new Array(0));
  let row = 0;
  let col = 0;
  let state = true;
  for (let i = 0; i < s.length; i++) {
    if (state) {
      matrix[row][col] = s[i];
      if (row + 1 === numRows) {
        col++;
        row--;
        if (row !== 0) state = false;
      } else row++;
    } else {
      matrix[row][col] = s[i];
      col++;
      row--;
      if (row === 0) state = true;
    }
  }
  let output = "";
  matrix.forEach((row) => {
    row.forEach((char) => {
      output += char;
    });
  });
  return output;
};

// test cases:
console.log(convert("PAYPALISHIRING", 3)); // "PAHNAPLSIIGYIR"
console.log(convert("PAYPALISHIRING", 4)); // "PINALSIGYAHRPI"
