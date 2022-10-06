# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    minNumberOfCameras = 0
    def minCameraCover(self, root: TreeNode) -> int:
        def helper(node: TreeNode) -> int:
            if(not node):
                return 0
            value = helper(node.left) + helper(node.right)
            if(value == 0):
                return 3
            if(value < 3):
                return 0
            self.minNumberOfCameras += 1
            return 1
        if(helper(root) > 2):
            return self.minNumberOfCameras + 1
        else:
            return self.minNumberOfCameras