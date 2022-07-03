# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        result = []
        def recurse(node):
            if not node:
                return
            recurse(node.next)
            while stack and stack[-1] <= node.val:
                stack.pop()
            result.append(0 if not stack else stack[-1])
            stack.append(node.val)
        recurse(head)
        return result[::-1]