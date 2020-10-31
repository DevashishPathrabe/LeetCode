# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if(not root):
            return True
        def isMirror(p,q) -> bool:
            if(not p and not q):
                return True
            if((p and not q) or (not p and q) or (p.val != q.val)):
                return False
            if(not isMirror(p.left, q.right)):
                return False
            if(not isMirror(p.right, q.left)):
                return False
            return True
        return isMirror(root.left, root.right)