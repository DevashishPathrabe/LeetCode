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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode Sum = new ListNode(0);
        ListNode current = Sum;
        int carry = 0;
        while(l1 != null || l2 != null){
            if(l1 == null){
                l1 = new ListNode(0);
            }
            else if(l2 == null){
                l2 = new ListNode(0);
            }
            int addition = l1.val + l2.val + carry;
            if(addition >= 10){
                carry = 1;
                current.next = new ListNode(addition-10);
            }
            else{
                carry = 0;
                current.next = new ListNode(addition);
            }
            current = current.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        if(carry > 0){
            current.next = new ListNode(carry);
        }
        return Sum.next;
    }
}