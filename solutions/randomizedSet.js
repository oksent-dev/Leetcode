/*
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
*/

var RandomizedSet = function() {
    this.set = new Set();
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function(val) {
    if(this.set.has(val)){
        return false;
    }
    this.set.add(val);
    return true;
};

/** 
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function(val) {
    if(!this.set.has(val)){
        return false;
    }
    this.set.delete(val);
    return true;
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function() {
    let arr = Array.from(this.set);
    return arr[Math.floor(Math.random() * arr.length)];
};
// test cases:
let randomSet = new RandomizedSet();
console.log(randomSet.insert(1)); // true
console.log(randomSet.remove(2)); // false
console.log(randomSet.insert(2)); // true
console.log(randomSet.getRandom());