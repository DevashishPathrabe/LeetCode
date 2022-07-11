# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(n1, l1):
            if not n1:
                return
            if not n1.left and not n1.right and n1.val not in l1:
                l1.append(n1.val)
            if(n1.left):
                helper(n1.left, l1)
            if(n1.right):
                helper(n1.right, l1)
            return l1
        l1 = []
        l2 = []
        return helper(root1, l1) == helper(root2, l2)