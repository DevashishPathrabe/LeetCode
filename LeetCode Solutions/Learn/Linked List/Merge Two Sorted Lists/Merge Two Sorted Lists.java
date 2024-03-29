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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newNode = new ListNode(0);
        ListNode requiredNode = newNode;
        while (l1 != null || l2 != null){
            if (l1 == null){
                requiredNode.next = l2;
                break;
            }
            if (l2 == null){
                requiredNode.next = l1;
                break;
            }
            if (l1.val > l2.val){
                requiredNode.next = new ListNode(l2.val);
                l2 = l2.next;
            } else{
                requiredNode.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            requiredNode = requiredNode.next;
        }
        return newNode.next;
    }
}