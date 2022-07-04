# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    gSum = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        self.bstToGst( root.right)
        root.val += self.gSum
        self.gSum = max( self.gSum, root.val)
        self.bstToGst( root.left)
        return root