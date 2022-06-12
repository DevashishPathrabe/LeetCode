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
    public ListNode swapPairs(ListNode head) {
        if(head == null){
            return null;
        }
        if(head.next == null){
            return head;
        }
        if(head.next.next == null){
            ListNode newHeader = head.next;
            newHeader.next = head;
            head.next = null;
            return newHeader;
        }
        ListNode nextPairHeader = head.next.next;
        ListNode newHeader = head.next;
        newHeader.next = head;
        head.next = swapPairs(nextPairHeader);
        return newHeader;
    }
}