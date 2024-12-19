/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.
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
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  let dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;
  let curr = head;

  while (curr) {
    if (curr.next && curr.val === curr.next.val) {
      while (curr.next && curr.val === curr.next.val) {
        curr = curr.next;
      }
      prev.next = curr.next;
    } else {
      prev = prev.next;
    }
    curr = curr.next;
  }

  return dummy.next;
};

// Test Cases
import ListNode from "../utils/listNode.js";
var head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
head.next.next.next = new ListNode(3);
head.next.next.next.next = new ListNode(4);
head.next.next.next.next.next = new ListNode(4);
head.next.next.next.next.next.next = new ListNode(5);
head = deleteDuplicates(head); // 1 -> 2 -> 5
while (head) {
  console.log(head.val);
  head = head.next;
}
