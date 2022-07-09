# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp = ListNode(next=head)
        left, right, node = temp, head, 0
        while(right):
            node, right = node+1, right.next
        for i in range(node // k):
            current = left.next
            for j in range(k - 1):
                nxt = current.next
                left.next, nxt.next, current.next = nxt, left.next, nxt.next
            left = current
        return temp.next