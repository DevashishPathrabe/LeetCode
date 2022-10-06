# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        current, count = head, 0
        while(current):
            current = current.next
            count += 1
        def helper(i: int, j: int) -> TreeNode:
            if(j < i):
                return None
            mid, node = i + j >> 1, TreeNode()
            node.left = helper(i, mid - 1)
            node.val, current[0] = current[0].val, current[0].next
            node.right = helper(mid + 1, j)
            return node
        current = [head]
        return helper(1, count)