# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head):
            return
        length = 1
        tail = head
        while (tail.next):
            tail = tail.next
            length += 1
        k %= length
        if (k == 0):
            return head
        stepsToNewHead = length - k
        tail.next = head
        while (stepsToNewHead > 0):
            tail = tail.next
            stepsToNewHead -= 1
        newHead = tail.next
        tail.next = None
        return newHead