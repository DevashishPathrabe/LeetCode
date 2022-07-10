# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        m1, m2 = inf, inf
        def helper(node):
            nonlocal m1, m2
            if not node:
                return
            m1 = m1 if m1 < node.val else node.val
            if (m1 != node.val):
                m2 = m2 if m2 < node.val else node.val
            if(node.left):
                helper(node.left)
            if(node.right):
                helper(node.right)
            return m2 if m2 != inf else -1
        return helper(root)