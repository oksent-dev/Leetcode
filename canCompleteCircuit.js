/*
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, 
return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique
*/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let totalGas = 0;
    let totalCost = 0;
    let tankAmount = 0;
    let startIdx = 0;
    for (let i = 0; i < gas.length; i++) {
        totalGas += gas[i];
        totalCost += cost[i];
        tankAmount += gas[i] - cost[i];
        if (tankAmount < 0) {
            startIdx = i + 1;
            tankAmount = 0;
        }
    }
    return totalGas >= totalCost ? startIdx : -1;
};

// test cases:
console.log(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])); // 3