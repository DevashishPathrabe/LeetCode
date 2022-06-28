# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        head1 = headA
        head2 = headB
        while(head1 != head2):
            if(head1 == None):
                head1 = headB
            else:
                head1 = head1.next
            if(head2 == None):
                head2 = headA
            else:
                head2 = head2.next
        return head1