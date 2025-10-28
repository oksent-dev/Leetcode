/*
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

function isMirror(node1, node2) {
  if (!node1 && !node2) return true;
  if (!node1 || !node2) return false;
  return node1.val === node2.val && isMirror(node1.left, node2.right) && isMirror(node1.right, node2.left);
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (!root) return true;
  return isMirror(root.left, root.right);
};

// Test cases
import TreeNode from "../../utils/treeNode.js";

let root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(2);
root.left.left = new TreeNode(3);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(4);
root.right.right = new TreeNode(3);
console.log(isSymmetric(root)); // true

root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(2);
root.left.right = new TreeNode(3);
root.right.right = new TreeNode(3);
console.log(isSymmetric(root)); // false
