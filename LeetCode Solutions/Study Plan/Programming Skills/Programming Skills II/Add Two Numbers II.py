# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        while(l1):
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while(l2):
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        sum = num1 + num2
        current = head = ListNode(0)
        if(sum == 0):
            return head
        while(sum > 0):
            head.next = ListNode(sum % 10, head.next)
            sum //= 10
        return current.next