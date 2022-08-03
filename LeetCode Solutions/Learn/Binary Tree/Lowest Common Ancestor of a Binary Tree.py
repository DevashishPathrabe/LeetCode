# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if(root in (None, p, q)):
                return root
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            if(left and right):
                return root
            else:
                return left or right
        node = helper(root, p, q)
        return node