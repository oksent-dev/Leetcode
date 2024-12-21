/*
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function (head, x) {
  let less = new ListNode(0);
  let greater = new ListNode(0);
  let lessHead = less;
  let greaterHead = greater;

  while (head) {
    if (head.val < x) {
      less.next = head;
      less = less.next;
    } else {
      greater.next = head;
      greater = greater.next;
    }
    head = head.next;
  }

  greater.next = null;
  less.next = greaterHead.next;

  return lessHead.next;
};

// Test Cases
import ListNode from "../utils/listNode.js";
var head = new ListNode(1);
head.next = new ListNode(4);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(2);
head.next.next.next.next = new ListNode(5);
head.next.next.next.next.next = new ListNode(2);
head = partition(head, 3); // 1 -> 2 -> 2 -> 4 -> 3 -> 5
while (head) {
  console.log(head.val);
  head = head.next;
}
