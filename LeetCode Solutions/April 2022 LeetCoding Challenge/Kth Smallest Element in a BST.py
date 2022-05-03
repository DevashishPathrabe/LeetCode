# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        result = []
        while(stack or root):
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root)
            root = root.right
        return result[k-1].val