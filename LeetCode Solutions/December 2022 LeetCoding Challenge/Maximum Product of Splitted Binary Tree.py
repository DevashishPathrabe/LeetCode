# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root == None:
                return 0
            currentSum = helper(root.left) + helper(root.right) + root.val
            self.ans = max(self.ans, currentSum * (self.totalSum - currentSum))
            return currentSum
        self.ans, self.totalSum = 0, 0
        self.totalSum = helper(root)
        helper(root)
        return self.ans % (10 ** 9 + 7)