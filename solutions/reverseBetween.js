/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
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
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
  if (!head) return null;
  let dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  for (let i = 0; i < left - 1; i++) {
    prev = prev.next;
  }
  let start = prev.next;
  let then = start.next;
  for (let i = 0; i < right - left; i++) {
    start.next = then.next;
    then.next = prev.next;
    prev.next = then;
    then = start.next;
  }
  return dummy.next;
};

// Test cases
import ListNode from "../utils/ListNode.js";
const head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);
reverseBetween(head, 2, 4); // [1,4,3,2,5]
let curr = head;
while (curr) {
  process.stdout.write(`${curr.val} `);
  curr = curr.next;
}
