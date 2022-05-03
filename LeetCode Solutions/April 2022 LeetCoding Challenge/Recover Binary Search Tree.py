# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        previous = TreeNode(-math.inf)
        def helper(root):
            nonlocal previous, first, second
            if root == None:
                return
            helper(root.left)
            if root.val < previous.val:
                if not first:
                    first = previous
                second = root
            previous = root
            helper(root.right)
        helper(root)
        first.val,second.val = second.val,first.val