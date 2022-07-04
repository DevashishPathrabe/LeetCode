# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getDepth(node):
            if(not node):
                return 0
            return 1 + max(getDepth(node.left), getDepth(node.right))
        if(not root):
            return true
        return abs(getDepth(node.left) - getDepth(node.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)