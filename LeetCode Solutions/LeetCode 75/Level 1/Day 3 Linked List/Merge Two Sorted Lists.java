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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newNode = new ListNode(0);
        ListNode requiredNode = newNode;
        while(list1 != null || list2 != null){
            if(list1 == null){
                requiredNode.next = list2;
                break;
            }
            if(list2 == null){
                requiredNode.next = list1;
                break;
            }
            if(list1.val > list2.val){
                requiredNode.next = new ListNode(list2.val);
                list2 = list2.next;
            } else{
                requiredNode.next = new ListNode(list1.val);
                list1 = list1.next;
            }
            requiredNode = requiredNode.next;
        }
        return newNode.next;
    }
}