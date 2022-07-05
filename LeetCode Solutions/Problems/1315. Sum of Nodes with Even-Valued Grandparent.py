# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 
        self.sum = 0
        self.helper(root, None, None)        
        return self.sum
    
    def helper(self,child, parent, grandParent):
        if not child:
            return
        if grandParent != None and grandParent.val % 2 == 0:
            self.sum += child.val
        self.helper(child.left, child, parent)
        self.helper(child.right, child, parent)