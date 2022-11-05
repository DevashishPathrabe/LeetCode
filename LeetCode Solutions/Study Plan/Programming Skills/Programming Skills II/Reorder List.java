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
    public void reorderList(ListNode head) {
        if (head == null){
            return;
        }
        ListNode temp = head, half = head, previous = null;
        while (temp.next != null && temp.next.next != null){
            temp = temp.next.next;
            half = half.next;
        }
        if (temp.next != null){
            half = half.next;
        }
        while(half != null){
            temp = half.next;
            half.next = previous;
            previous = half;
            half = temp;
        }
        half = previous;
        while (head != null && half != null){
            temp = head.next;
            previous = half.next;
            head.next = half;
            half.next = temp;
            head = temp;
            half = previous;
        }
        if (head != null && head.next != null){
            head.next.next = null;
        }
    }
}