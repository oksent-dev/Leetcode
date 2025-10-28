/*
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.
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
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function (inorder, postorder) {
  if (inorder.length === 0 || postorder.length === 0) return null;

  let root = new TreeNode(postorder.pop());
  let inorderIndex = inorder.indexOf(root.val);

  root.right = buildTree(inorder.slice(inorderIndex + 1), postorder);
  root.left = buildTree(inorder.slice(0, inorderIndex), postorder);

  return root;
};

// Test Cases
import TreeNode from "../../utils/treeNode.js";
function inOrderTraversal(root) {
  if (root === null) return;

  inOrderTraversal(root.left);
  console.log(root.val);
  inOrderTraversal(root.right);
}
var tree = buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]);
inOrderTraversal(tree); // 9, 3, 15, 20, 7
