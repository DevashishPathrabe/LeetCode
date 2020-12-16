# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = None
    def isValidBST(self, root: TreeNode) -> bool:
        if(not root):
            return True
        if(not self.isValidBST(root.left)):
            return False
        if(self.last is not None and self.last >= root.val):
            return False
        self.last = root.val
        return self.isValidBST(root.right)