# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        node.next = head
        d, dv = {}, []
        s, nodeV = 0, node
        while nodeV:
            s += nodeV.val
            if s not in d:
                d[s] = nodeV
                dv.append(s)
            else:
                d[s].next = nodeV.next
                while dv[-1] != s:
                    t = dv.pop()
                    del d[t]
            nodeV = nodeV.next
        return node.next