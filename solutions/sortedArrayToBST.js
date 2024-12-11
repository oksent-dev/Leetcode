/*
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function (nums) {
  return _sortedArrayToBST(nums, 0, nums.length - 1);
};

function _sortedArrayToBST(nums, left, right) {
  if (left > right) return null;
  const mid = Math.floor((left + right) / 2);
  const root = new TreeNode(nums[mid]);
  root.left = _sortedArrayToBST(nums, left, mid - 1);
  root.right = _sortedArrayToBST(nums, mid + 1, right);
  return root;
}

// Test cases
import TreeNode from "../utils/TreeNode.js";

function inOrder(root) {
  if (!root) return;
  inOrder(root.left);
  process.stdout.write(`${root.val} `);
  inOrder(root.right);
}
const nums = [-10, -3, 0, 5, 9];
const root = sortedArrayToBST(nums);
inOrder(root); // [-10,-3,0,5,9]
