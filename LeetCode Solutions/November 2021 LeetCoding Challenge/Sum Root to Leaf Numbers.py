# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, current = 0):
            if not root:
                return 0
            if not root.left and not root.right:
                return current*10 + root.val
            return helper(root.left,current*10 + root.val) + helper(root.right, current*10 + root.val)
        return helper(root)