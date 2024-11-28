/**
 * @param {string} s
 * @return {boolean}
 */

var isNumber = function(s) {
    const regex = /^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$/;
    return regex.test(s);
};

// test cases:
console.log(isNumber("0")); // Expected output: true
console.log(isNumber("e")); // Expected output: false