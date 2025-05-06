/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
*/
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 1) {
    return 1;
  }
  let a = 1,
    b = 1;
  let c;
  for (let i = 2; i <= n; i++) {
    c = b + a;
    a = b;
    b = c;
  }
  return c;
};

// Test cases
console.log(climbStairs(2)); // 2
console.log(climbStairs(3)); // 3
