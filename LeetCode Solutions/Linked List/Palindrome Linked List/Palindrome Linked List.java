/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null){
            return true;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        slow = reverseList(slow);
        fast = head;
        while (slow != null){
            if (slow.val != fast.val){
                return false;
            }
            slow = slow.next;
            fast = fast.next;
        }
        return true;
    }
    public ListNode reverseList(ListNode node){
        ListNode current = node;
        ListNode previous = null;
        while (current != null){
            ListNode currentNext = current.next;
            current.next = previous;
            previous = current;
            current = currentNext;
        }
        return previous;
    }
}