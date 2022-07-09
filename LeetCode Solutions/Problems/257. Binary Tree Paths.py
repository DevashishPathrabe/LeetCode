# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            leftTree = helper(root.left)
            rightTree = helper(root.right)
            left = [str(root.val) + ('->' + path) for path in leftTree]
            right = [str(root.val) + ('->' + path) for path in rightTree]
            return left + right
        return helper(root)