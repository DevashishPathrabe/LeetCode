# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if(not root):
            return False
        def helper(node, total):
            if(node):
                if(not node.left and not node.right):
                    return total + node.val == sum
                return helper(node.left, total + node.val) or helper(node.right, total + node.val)
        return helper(root, 0)