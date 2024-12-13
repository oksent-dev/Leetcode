/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.
/*

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
  if (!preorder.length || !inorder.length) {
    return null;
  }

  const root = new TreeNode(preorder[0]);
  const rootIndex = inorder.indexOf(preorder[0]);

  root.left = buildTree(preorder.slice(1, rootIndex + 1), inorder.slice(0, rootIndex));
  root.right = buildTree(preorder.slice(rootIndex + 1), inorder.slice(rootIndex + 1));

  return root;
};

// Test cases
import TreeNode from "../utils/TreeNode.js";
function inOrder(root) {
  const arr = [];
  function traverse(node) {
    if (node.left) traverse(node.left);
    arr.push(node.val);
    if (node.right) traverse(node.right);
  }
  traverse(root);
  return arr;
}

let root = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]);
console.log(inOrder(root)); // [9, 3, 15, 20, 7]
