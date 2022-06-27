# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = [None, None]
        self.search(root, p, q, result)
        return result[0]
    def search(self, node, p, q, result):
        if node:
            left = self.search(node.left, p, q, result)
            right = self.search(node.right, p, q, result)
            m = True if node.val in (p.val, q.val) else False
            if left + right + m >= 2:
                result[0] = node
                result[1] = node.val
            elif left + right + m > 0:
                return True
            return False
        return False