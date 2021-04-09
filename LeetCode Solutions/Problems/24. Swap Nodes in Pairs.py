# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head is None):
            return None
        if(head.next is None):
            return head
        if(head.next.next is None):
            newHeader = head.next
            newHeader.next = head
            head.next = None
            return newHeader
        nextPairHeader = head.next.next
        newHeader = head.next
        newHeader.next = head
        head.next = self.swapPairs(nextPairHeader)
        return newHeader