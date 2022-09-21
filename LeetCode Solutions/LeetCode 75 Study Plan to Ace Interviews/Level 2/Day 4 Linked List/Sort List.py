# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return None
        newList = []
        current = head
        head1 = current
        while(head):
            newList.append(head.val)
            head = head.next
        newList.sort()
        i = 0
        while(current):
            current.val = newList[i]
            current = current.next
            i += 1
        return head1