/*
Given the root of a binary tree, return the inorder traversal of its nodes' values.
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
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  const result = [];
  function inorder(node) {
    if (!node) return;
    inorder(node.left);
    result.push(node.val);
    inorder(node.right);
  }
  inorder(root);
  return result;
};

//  Test cases
import TreeNode from "../utils/treeNode.js";
const tree = new TreeNode(1, null, new TreeNode(2, new TreeNode(3)));
console.log(inorderTraversal(tree)); // [1,3,2]
console.log(inorderTraversal(null)); // []
console.log(inorderTraversal(new TreeNode(1))); // [1]
