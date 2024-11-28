/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    };
    
    const keys = Object.keys(roman).sort((a, b) => b - a); 
    let result = '';
    for (let i = 0; i < keys.length; i++) {
        while (num >= keys[i]) {
            result += roman[keys[i]];
            num -= keys[i];
        }
    }
    
    return result;
};
// test cases:
console.log(intToRoman(3)); // Expected output: "III"
console.log(intToRoman(4)); // Expected output: "IV"
console.log(intToRoman(9)); // Expected output: "IX"
console.log(intToRoman(58)); // Expected output: "LVIII"
console.log(intToRoman(1994)); // Expected output: "MCMXCIV"