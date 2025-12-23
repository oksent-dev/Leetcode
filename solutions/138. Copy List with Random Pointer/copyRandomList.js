/*
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
*/

function _Node(val, next = null, random = null) {
  this.val = val;
  this.next = next;
  this.random = random;
}

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function (head) {
  if (!head) return null;
  let map = new Map();
  let curr = head;
  while (curr) {
    map.set(curr, new _Node(curr.val));
    curr = curr.next;
  }
  curr = head;
  while (curr) {
    map.get(curr).next = curr.next ? map.get(curr.next) : null;
    map.get(curr).random = curr.random ? map.get(curr.random) : null;
    curr = curr.next;
  }
  return map.get(head);
};

// Test cases
const head = new _Node(7);
head.next = new _Node(13);
head.next.random = head;
head.next.next = new _Node(11);
head.next.next.random = head.next;
head.next.next.next = new _Node(10);
head.next.next.next.random = head.next.next;
head.next.next.next.next = new _Node(1);
head.next.next.next.next.random = head;
head.random = null;
console.log(copyRandomList(head)); // [7, null] -> [13, 0] -> [11, 1] -> [10, 2] -> [1, 0]
