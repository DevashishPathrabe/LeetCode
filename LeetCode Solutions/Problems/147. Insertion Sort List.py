# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = ListNode(0)
        node.next = head
        while(head and head.next):
            if(head.val <= head.next.val):
                head = head.next
            else:
                node_1 = node
                nodetoinsert = head.next
                while(node_1.next.val < nodetoinsert.val):
                    node_1 = node_1.next
                head.next = nodetoinsert.next
                node_1.next, nodetoinsert.next = nodetoinsert, node_1.next
        return node.next