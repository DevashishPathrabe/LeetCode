# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        vals = []
        for head in lists:
            while (head is not None):
                vals.append(head.val)
                head = head.next
        vals.sort()
        if (vals == []):
            return None
        else:
            head = ListNode(vals[0])
            temp = head
            for i in range(1, len(vals)):
                temp.next = ListNode(vals[i])
                temp = temp.next
        return head