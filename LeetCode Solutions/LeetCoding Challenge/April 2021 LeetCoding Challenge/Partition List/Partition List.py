# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        frontTemp, backTemp = ListNode(0), ListNode(0)
        front, back, current = frontTemp, backTemp, head
        while (current):
            if (current.val < x):
                front.next = current
                front = current
            else:
                back.next = current
                back = current
            current = current.next
        front.next, back.next = backTemp.next, None
        return frontTemp.next