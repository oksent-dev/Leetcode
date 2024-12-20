/*
Given the head of a linked list, rotate the list to the right by k places.
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
var rotateRight = function (head, k) {
  if (!head) return head;
  let length = 1;
  let tail = head;

  while (tail.next) {
    tail = tail.next;
    length++;
  }

  k = k % length;
  if (k === 0) return head;

  let newTail = head;
  for (let i = 1; i < length - k; i++) {
    newTail = newTail.next;
  }

  let newHead = newTail.next;
  newTail.next = null;
  tail.next = head;

  return newHead;
};

// Test Cases
import ListNode from "../utils/listNode.js";
var head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(4);
head.next.next.next.next = new ListNode(5);
head = rotateRight(head, 2); // 4 -> 5 -> 1 -> 2 -> 3
while (head) {
  console.log(head.val);
  head = head.next;
}
