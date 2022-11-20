# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if(not head or not head.next or left == right):
            return head
        tempHead = ListNode(val = -1, next = head)
        previousPosition = tempHead
        for _ in range(left - 1):
            previousPosition = previousPosition.next
        currentPosition = previousPosition.next
        for _ in range(right - left):
            nextPosition = currentPosition.next
            currentPosition.next = nextPosition.next
            nextPosition.next = previousPosition.next
            previousPosition.next = nextPosition
        return tempHead.next