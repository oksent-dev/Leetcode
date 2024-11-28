/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
*/

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  let stack = [];
  let i = 0,
    water = 0;
  while (i < height.length) {
    if (!stack.length || height[i] <= height[stack[stack.length - 1]]) {
      stack.push(i++);
    } else {
      let top = stack.pop();
      if (stack.length) {
        let distance = i - stack[stack.length - 1] - 1;
        let bounded_height = Math.min(height[i], height[stack[stack.length - 1]]) - height[top];
        water += distance * bounded_height;
      }
    }
  }
  return water;
};
// test cases:
console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])); // [0,1,0,2,1,0,1,3,2,1,2,1] => 6
