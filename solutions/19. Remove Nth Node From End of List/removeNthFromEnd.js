/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.
*/
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
  let current = head;
  let size = 1;
  while (current.next !== null) {
    size++;
    current = current.next;
  }
  n = size - n + 1;
  let previous = null;
  current = head;
  while (n - 1) {
    previous = current;
    current = current.next;
    n--;
  }
  if (previous === null && current.next === null && n === 1) {
    return null;
  } else if (previous === null) {
    return head.next;
  } else {
    previous.next = current.next;
  }
  return head;
};

// Test cases:
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
const n = 2;
const result = removeNthFromEnd(head, n);
console.log(result); // [1, 2, 3, 5]
