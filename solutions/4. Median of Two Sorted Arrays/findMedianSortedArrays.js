/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
*/

function findMedian(sortedArray) {
  const length = sortedArray.length;
  if (length % 2 === 0) {
    const middleIndex1 = length / 2 - 1;
    const middleIndex2 = length / 2;
    const value1 = sortedArray[middleIndex1];
    const value2 = sortedArray[middleIndex2];
    return (value1 + value2) / 2;
  } else {
    const middleIndex = Math.floor(length / 2);
    return sortedArray[middleIndex];
  }
}
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  if (nums1.length == 0) return findMedian(nums2);
  else if (nums2.length == 0) return findMedian(nums1);
  else if (nums1.length == 1 && nums2.length == 1) return (nums1[0] + nums2[0]) / 2;
  let lastValue = {
    arr: 0,
    value: 0,
    prevValue: 0,
  };
  let idx = [0, 0];
  const middle = Math.floor((nums1.length + nums2.length) / 2) + 1;
  let i = 0;
  while (i < middle) {
    if (nums1[idx[0]] <= nums2[idx[1]]) {
      lastValue["arr"] = 1;
      lastValue["prevValue"] = lastValue["value"];
      lastValue["value"] = nums1[idx[0]];
      idx[0]++;
    } else {
      lastValue["arr"] = 2;
      lastValue["prevValue"] = lastValue["value"];
      lastValue["value"] = nums2[idx[1]];
      idx[1]++;
    }
    i++;
    if (nums1.length === idx[0]) {
      while (i < middle) {
        lastValue["arr"] = 2;
        lastValue["prevValue"] = lastValue["value"];
        lastValue["value"] = nums2[idx[1]];
        idx[1]++;
        i++;
      }
      break;
    } else if (nums2.length === idx[1]) {
      while (i < middle) {
        lastValue["arr"] = 1;
        lastValue["prevValue"] = lastValue["value"];
        lastValue["value"] = nums1[idx[0]];
        idx[0]++;
        i++;
      }
      break;
    }
  }
  if ((nums1.length + nums2.length) % 2 === 0) return (lastValue["value"] + lastValue["prevValue"]) / 2;
  return lastValue["value"];
};

// test case:
console.log(findMedianSortedArrays([1, 3], [2])); // 2.0
console.log(findMedianSortedArrays([1, 2], [3, 4])); // 2.5
