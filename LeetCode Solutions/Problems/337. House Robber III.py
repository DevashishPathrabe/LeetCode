# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            leftNode, leftChildren = dfs(node.left) if node.left else (0,0)
            rightNode, rightChildren = dfs(node.right) if node.right else (0,0)
            return node.val + leftChildren + rightChildren, max(leftNode + rightNode, leftNode + rightChildren, leftChildren + rightChildren, leftChildren + rightNode)
        if(root):
            return max(dfs(root))
        else:
            return 0