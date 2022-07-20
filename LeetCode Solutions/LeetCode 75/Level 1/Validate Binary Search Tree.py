# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def helper(root, left, right):
            if(root):
                if(left >= root.val or root.val >= right):
                    self.result = False
                    return
                helper(root.left, left, root.val)
                helper(root.right, root.val, right)
        helper(root, float("-inf"), float('inf'))
        return self.result