# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if(not root):
                return 0
            left = helper(root.left)
            right = helper(root.right)
            m1 = max(max(left, right)+root.val, root.val)
            m2 = max(m1, left+right+root.val)
            self.pathSum = max(self.pathSum, m2)
            return m1
        self.pathSum = float('-inf')
        helper(root)
        return self.pathSum