/*
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
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
 * @param {TreeNode} root
 * @return {number}
 */
var countNodes = function (root) {
  if (root === null) return 0;

  let leftHeight = 0;
  let left = root;
  while (left !== null) {
    leftHeight++;
    left = left.left;
  }

  let rightHeight = 0;
  let right = root;
  while (right !== null) {
    rightHeight++;
    right = right.right;
  }

  if (leftHeight === rightHeight) {
    return Math.pow(2, leftHeight) - 1;
  }

  return 1 + countNodes(root.left) + countNodes(root.right);
};

// Test Cases
import TreeNode from "../utils/treeNode.js";
var tree = new TreeNode(1);
tree.left = new TreeNode(2);
tree.right = new TreeNode(3);
tree.left.left = new TreeNode(4);
tree.left.right = new TreeNode(5);
tree.right.left = new TreeNode(6);
console.log(countNodes(tree)); // 6
