/*
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] <= result[result.length - 1][1]) {
      result[result.length - 1][1] = Math.max(result[result.length - 1][1], intervals[i][1]);
    } else {
      result.push(intervals[i]);
    }
  }
  return result;
};

// Test cases
console.log(
  merge([
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18]
  ])
); // [[1,6],[8,10],[15,18]]
console.log(
  merge([
    [1, 4],
    [4, 5]
  ])
); // [[1,5]]
