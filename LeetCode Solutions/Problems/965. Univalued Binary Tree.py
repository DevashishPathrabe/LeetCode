# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if(root):
            self.val = root.val
            def helper(root):
                if(root == None):
                    return True
                return (root.val == self.val) and helper(root.left) and helper(root.right)
            return helper(root)
        return True