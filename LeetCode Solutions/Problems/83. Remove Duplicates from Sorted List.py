# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(not head):
            return head
        temp = head.next
        previous = head
        while(temp):
            if(temp.val == previous.val):
                previous.next = temp.next
            else:
                previous = temp
            temp = temp.next
        return head