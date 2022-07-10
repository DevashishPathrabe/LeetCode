# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def longestPath(node, value):
            if node:
                left, right = longestPath(node.left, node.val), longestPath(node.right, node.val)
                self.ans = max(self.ans, left + right)
                if value == node.val:
                    return max(left, right) + 1
            return 0
        longestPath(root, None)
        return self.ans