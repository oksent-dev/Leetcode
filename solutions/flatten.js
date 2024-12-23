/*
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and 
the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
  if (root === null) return null;

  let stack = [root];
  let prev = null;

  while (stack.length > 0) {
    let node = stack.pop();

    if (node.right !== null) stack.push(node.right);
    if (node.left !== null) stack.push(node.left);

    if (prev !== null) {
      prev.right = node;
      prev.left = null;
    }

    prev = node;
  }
};

// Test Cases
import TreeNode from "../utils/treeNode.js";
var tree = new TreeNode(1, new TreeNode(2, new TreeNode(3), new TreeNode(4)), new TreeNode(5, null, new TreeNode(6)));
flatten(tree); // 1 -> 2 -> 3 -> 4 -> 5 -> 6
while (tree !== null) {
  console.log(tree.val);
  tree = tree.right;
}
