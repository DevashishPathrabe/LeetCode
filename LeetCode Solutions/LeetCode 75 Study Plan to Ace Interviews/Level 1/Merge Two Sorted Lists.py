# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newnode = ListNode(0)
        requiredNode = newnode
        while(True):
            if not list1:
                requiredNode.next = list2
                break
            if not list2:
                requiredNode.next = list1
                break
            if list1.val > list2.val:
                requiredNode.next = ListNode(list2.val)
                list2 = list2.next
            else:
                requiredNode.next = ListNode(list1.val)
                list1 = list1.next
            requiredNode = requiredNode.next
        return newnode.next