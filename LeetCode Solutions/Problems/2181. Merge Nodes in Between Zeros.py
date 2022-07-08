# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = temp = head.next
        prev = None
        sum = 0
        while temp:
            sum += temp.val
            if temp.val == 0:
                current.val = sum
                sum = 0
                prev = current
                current = current.next
            temp = temp.next
        prev.next = None
        return head.next