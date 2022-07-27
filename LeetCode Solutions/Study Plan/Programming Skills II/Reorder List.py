# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        temp, half, previous = head, head, None
        while temp.next != None and temp.next.next != None:
            temp = temp.next.next
            half = half.next
        if temp.next != None:
            half = half.next
        while half != None:
            temp = half.next
            half.next = previous
            previous = half
            half = temp
        half = previous
        while head != None and half != None:
            temp = head.next
            previous = half.next
            head.next = half
            half.next = temp
            head = temp
            half = previous
        if head != None and head.next != None:
            head.next.next = None