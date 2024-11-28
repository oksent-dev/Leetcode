/*
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher 
has published at least h papers that have each been cited at least h times.
*/

/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((a, b) => a - b);
    let n = citations.length;
    for(let i = 0; i < n; i++){
        if(citations[i] >= n - i){
            return n - i;
        }
    }
    return 0;
};

// test cases:
console.log(hIndex([3,0,6,1,5])); // 3