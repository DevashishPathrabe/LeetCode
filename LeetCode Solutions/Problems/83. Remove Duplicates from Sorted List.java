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
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode temp = head.next;
        ListNode previous = head;
        while(temp != null){
            if(temp.val == previous.val){
                previous.next = temp.next;
            } else{
                previous = temp;
            }
            temp = temp.next;
        }
        return head;
    }
}