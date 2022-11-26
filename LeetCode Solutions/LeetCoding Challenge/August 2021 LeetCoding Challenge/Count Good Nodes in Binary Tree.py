# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node,pathMax,count):
            if node == None:
                return count
            if pathMax <= node.val: 
                count += 1
            count = helper(node.left, max(pathMax, node.val), count)
            count = helper(node.right,max(pathMax, node.val), count)
            return count
        return helper(root, root.val, 0)