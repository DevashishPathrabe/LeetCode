# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepestDepth(node, depth):
            if(not node):
                return node, depth
            left, leftDepth = deepestDepth(node.left, depth + 1)
            right, rightDepth = deepestDepth(node.right, depth + 1)
            if(leftDepth > rightDepth):
                return left, leftDepth
            if(rightDepth > leftDepth):
                return right, rightDepth
            return node, leftDepth
        return deepestDepth(root, 0)[0]