/*
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function (head, k) {
  let dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  let curr = head;
  let count = 0;

  const reverse = (prev, next) => {
    let last = prev.next;
    let curr = last.next;

    while (curr !== next) {
      last.next = curr.next;
      curr.next = prev.next;
      prev.next = curr;
      curr = last.next;
    }

    return last;
  };
  while (curr) {
    count++;
    if (count % k === 0) {
      prev = reverse(prev, curr.next);
      curr = prev.next;
    } else {
      curr = curr.next;
    }
  }

  return dummy.next;
};

// Test Cases
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
var head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);
var k = 2;
head = reverseKGroup(head, k); // 2 -> 1 -> 4 -> 3 -> 5
while (head) {
  console.log(head.val);
  head = head.next;
}
