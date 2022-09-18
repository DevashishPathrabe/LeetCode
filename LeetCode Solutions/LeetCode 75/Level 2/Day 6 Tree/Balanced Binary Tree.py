# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        self.answer = True
        def helper(root):
            left, right = 0, 0
            if(root.left):
                left += helper(root.left)
            if(root.right):
                right += helper(root.right)
            if(abs(left-right) > 1):
                self.answer = False
            return max(left, right) + 1
        helper(root)
        return self.answer