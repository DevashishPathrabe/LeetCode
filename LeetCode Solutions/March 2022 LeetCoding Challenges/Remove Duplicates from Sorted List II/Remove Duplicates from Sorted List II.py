# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head
        newNode = ListNode(0)
        newNode.next = head
        tail = newNode
        result = -1
        while (head):
            if (head.next and head.val == head.next.val):
                result = 1
                head = head.next
            else:
                if (result == 1):
                    tail.next = head.next
                else:
                    tail = tail.next
                head = head.next
                result = -1
        return newNode.next