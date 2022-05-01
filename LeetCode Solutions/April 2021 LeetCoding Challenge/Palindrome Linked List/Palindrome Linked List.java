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
        ListNode slow = head, fast = head, previous = null;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        previous = slow;
        slow = slow.next;
        previous.next = null;
        while (slow != null){
            ListNode temp = slow.next;
            slow.next = previous;
            previous = slow;
            slow = temp;
        }
        fast = head;
        slow = previous;
        while (slow != null){
            if (fast.val != slow.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
}