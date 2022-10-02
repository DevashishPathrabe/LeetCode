# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Sum = ListNode(0)
        current = Sum
        carry = 0
        while (l1 or l2):
            if (not l1):
                l1 = ListNode(0)
            elif (not l2):
                l2 = ListNode(0)
            addition = l1.val + l2.val + carry
            if (addition >= 10):
                carry = 1
                current.next = ListNode(addition-10)
            else:
                carry = 0
                current.next = ListNode(addition)  
            current = current.next
            l1 = l1.next
            l2 = l2.next
        if (carry > 0):
            current.next = ListNode(carry)        
        return Sum.next